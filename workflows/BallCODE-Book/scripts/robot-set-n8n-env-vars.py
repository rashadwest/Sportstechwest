#!/usr/bin/env python3
"""
Robot: Set n8n Environment Variables
AIMCODE Solution - Option A: System-Level Variables

Detects n8n installation method and sets environment variables appropriately.
"""

import os
import sys
import subprocess
import json
from pathlib import Path

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*60}{NC}")
    print(f"{BLUE}{text:^60}{NC}")
    print(f"{BLUE}{'='*60}{NC}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{NC}")

def print_error(text):
    print(f"{RED}❌ {text}{NC}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{NC}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{NC}")

def check_ssh_access(host="192.168.1.226", user="pi"):
    """Check if SSH access to Pi is available."""
    try:
        result = subprocess.run(
            ["ssh", "-o", "ConnectTimeout=5", "-o", "BatchMode=yes", 
             f"{user}@{host}", "echo 'connected'"],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0
    except:
        return False

def detect_n8n_installation(host="192.168.1.226", user="pi"):
    """Detect how n8n is installed on Pi."""
    print_info("Detecting n8n installation method...")
    
    # Check systemd
    try:
        result = subprocess.run(
            ["ssh", f"{user}@{host}", "systemctl", "status", "n8n"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print_success("Found: n8n running via systemd")
            return "systemd"
    except:
        pass
    
    # Check docker
    try:
        result = subprocess.run(
            ["ssh", f"{user}@{host}", "docker", "ps", "|", "grep", "n8n"],
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        if "n8n" in result.stdout:
            print_success("Found: n8n running via Docker")
            return "docker"
    except:
        pass
    
    # Check npm/pm2
    try:
        result = subprocess.run(
            ["ssh", f"{user}@{host}", "pm2", "list", "|", "grep", "n8n"],
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        if "n8n" in result.stdout:
            print_success("Found: n8n running via pm2")
            return "pm2"
    except:
        pass
    
    print_warning("Could not detect n8n installation method")
    return "unknown"

def set_systemd_env_vars(host="192.168.1.226", user="pi"):
    """Set environment variables in systemd service file."""
    print_info("Setting environment variables in systemd service...")
    
    service_file = "/etc/systemd/system/n8n.service"
    
    # Get Netlify Site ID from user
    netlify_site_id = input(f"\n{YELLOW}Enter Netlify Site ID: {NC}").strip()
    if not netlify_site_id:
        print_error("Netlify Site ID is required")
        return False
    
    # Variables to set
    env_vars = {
        "GITHUB_REPO_OWNER": "rashadwest",
        "GITHUB_REPO_NAME": "BTEBallCODE",
        "GITHUB_WORKFLOW_FILE": "unity-webgl-build.yml",
        "NETLIFY_SITE_ID": netlify_site_id
    }
    
    # Read current service file
    try:
        result = subprocess.run(
            ["ssh", f"{user}@{host}", "sudo", "cat", service_file],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode != 0:
            print_error(f"Cannot read service file: {result.stderr}")
            return False
        
        service_content = result.stdout
        
        # Check if [Service] section exists
        if "[Service]" not in service_content:
            print_error("Service file missing [Service] section")
            return False
        
        # Add environment variables
        env_lines = []
        for key, value in env_vars.items():
            env_line = f'Environment="{key}={value}"'
            if env_line not in service_content:
                env_lines.append(env_line)
        
        if not env_lines:
            print_success("Environment variables already set")
            return True
        
        # Add after [Service] line
        lines = service_content.split('\n')
        new_lines = []
        service_section_found = False
        
        for line in lines:
            new_lines.append(line)
            if line.strip() == "[Service]":
                service_section_found = True
                # Add environment variables after [Service]
                for env_line in env_lines:
                    new_lines.append(env_line)
        
        if not service_section_found:
            print_error("Could not find [Service] section")
            return False
        
        new_content = '\n'.join(new_lines)
        
        # Write to temp file, then copy to Pi
        temp_file = "/tmp/n8n.service"
        with open(temp_file, 'w') as f:
            f.write(new_content)
        
        # Copy to Pi
        subprocess.run(
            ["scp", temp_file, f"{user}@{host}:{temp_file}"],
            check=True
        )
        
        # Move to final location with sudo
        subprocess.run(
            ["ssh", f"{user}@{host}", "sudo", "mv", temp_file, service_file],
            check=True
        )
        
        # Reload systemd and restart
        print_info("Reloading systemd daemon...")
        subprocess.run(
            ["ssh", f"{user}@{host}", "sudo", "systemctl", "daemon-reload"],
            check=True
        )
        
        print_info("Restarting n8n service...")
        subprocess.run(
            ["ssh", f"{user}@{host}", "sudo", "systemctl", "restart", "n8n"],
            check=True
        )
        
        print_success("Environment variables set and n8n restarted")
        return True
        
    except subprocess.CalledProcessError as e:
        print_error(f"Error setting variables: {e}")
        return False
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        return False

def verify_env_vars(host="192.168.1.226", user="pi"):
    """Verify environment variables are accessible."""
    print_info("Verifying environment variables...")
    
    # Test by triggering workflow
    import requests
    try:
        response = requests.post(
            f"http://{host}:5678/webhook/unity-build",
            json={"request": "Verify env vars", "branch": "main"},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            if "error" in data and "Missing required env var" in str(data.get("error", "")):
                print_error("Environment variables not accessible")
                return False
            else:
                print_success("Environment variables are accessible")
                return True
        else:
            print_warning(f"Unexpected response: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Verification failed: {e}")
        return False

def main():
    """Main robot function."""
    print_header("Robot: Set n8n Environment Variables (AIMCODE Solution)")
    
    # Step 1: Check SSH access
    print("\n1. Checking SSH access to Pi...")
    if not check_ssh_access():
        print_error("Cannot access Pi via SSH")
        print_warning("Falling back to Option B: Hardcode in workflow")
        print_info("See: COMPLETE-SETUP-SOLUTION.md for Option B")
        return False
    
    print_success("SSH access available")
    
    # Step 2: Detect installation method
    print("\n2. Detecting n8n installation method...")
    method = detect_n8n_installation()
    
    if method == "unknown":
        print_error("Cannot determine n8n installation method")
        print_warning("Falling back to Option B: Hardcode in workflow")
        return False
    
    # Step 3: Set variables based on method
    print(f"\n3. Setting environment variables ({method})...")
    
    if method == "systemd":
        success = set_systemd_env_vars()
    elif method == "docker":
        print_warning("Docker method not yet implemented")
        print_info("Manual steps: Edit docker-compose.yml or add env vars to docker run command")
        return False
    elif method == "pm2":
        print_warning("pm2 method not yet implemented")
        print_info("Manual steps: Edit .env file or pm2 ecosystem file")
        return False
    else:
        print_error(f"Unknown method: {method}")
        return False
    
    if not success:
        return False
    
    # Step 4: Verify
    print("\n4. Verifying environment variables...")
    if verify_env_vars():
        print_success("✅ All environment variables set successfully!")
        print("\nNext steps:")
        print("  1. Run: python scripts/verify-garvis-unity-integration.py")
        print("  2. Run: python scripts/garvis-command.py --one-thing 'Test' --tasks 'Build Unity game'")
        return True
    else:
        print_warning("Verification failed, but variables may still be set")
        print_info("Check n8n logs for details")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)

