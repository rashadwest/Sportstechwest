#!/usr/bin/env python3
"""
Robot: Unity Next Steps Guide
Checks Unity build status, GitHub Actions, and provides next steps after UI/UX improvements.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
UNITY_REPO = "rashadwest/BTEBallCODE"

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
NC = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*70}{NC}")
    print(f"{BLUE}{text:^70}{NC}")
    print(f"{BLUE}{'='*70}{NC}\n")

def print_section(text):
    print(f"\n{CYAN}{'─'*70}{NC}")
    print(f"{CYAN}{text}{NC}")
    print(f"{CYAN}{'─'*70}{NC}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{NC}")

def print_error(text):
    print(f"{RED}❌ {text}{NC}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{NC}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{NC}")

def check_github_actions_status():
    """Check latest GitHub Actions workflow run status."""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{UNITY_REPO}/actions/runs", "--jq", ".workflow_runs[0]"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            run = json.loads(result.stdout)
            status = run.get("status", "unknown")
            conclusion = run.get("conclusion", "unknown")
            workflow_name = run.get("name", "Unknown Workflow")
            created_at = run.get("created_at", "")
            html_url = run.get("html_url", "")
            
            print_section("GitHub Actions Status")
            print_info(f"Workflow: {workflow_name}")
            print_info(f"Status: {status}")
            print_info(f"Conclusion: {conclusion}")
            print_info(f"Created: {created_at}")
            
            if status == "completed":
                if conclusion == "success":
                    print_success("✅ Build completed successfully!")
                    return True, html_url
                else:
                    print_error(f"❌ Build failed: {conclusion}")
                    return False, html_url
            elif status == "in_progress":
                print_warning("⏳ Build in progress...")
                return None, html_url
            else:
                print_info(f"Status: {status}")
                return None, html_url
        else:
            print_warning("Could not fetch GitHub Actions status")
            return None, None
    except Exception as e:
        print_warning(f"Error checking GitHub Actions: {e}")
        return None, None

def check_netlify_status():
    """Check Netlify deployment status."""
    try:
        # Try to get Netlify site info
        result = subprocess.run(
            ["gh", "api", "repos/rashadwest/BTEBallCODE"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        print_section("Netlify Deployment")
        print_info("Site: ballcode.netlify.app")
        print_info("Check deployment status at: https://app.netlify.com/sites/ballcode")
        print_info("Live site: https://ballcode.netlify.app")
        
        return True
    except Exception as e:
        print_warning(f"Could not check Netlify status: {e}")
        return False

def check_unity_scene_changes():
    """Check if Main Menu scene has been modified."""
    try:
        result = subprocess.run(
            ["cd", "/Users/rashadwest/BTEBallCODE", "&&", "git", "status", "--short", "Assets/Scenes/Main Menu.unity"],
            shell=True,
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if "Main Menu.unity" in result.stdout:
            print_section("Scene Changes")
            print_success("Main Menu scene has changes")
            return True
        else:
            print_info("No uncommitted scene changes")
            return False
    except:
        return False

def provide_next_steps(build_status, build_url):
    """Provide next steps based on current status."""
    print_section("Next Steps")
    
    if build_status is True:
        print_success("Build completed successfully!")
        print_info("1. Check Netlify deployment:")
        print("   https://app.netlify.com/sites/ballcode")
        print_info("2. Test game on live site:")
        print("   https://ballcode.netlify.app")
        print_info("3. Verify UI/UX improvements:")
        print("   - Game mode buttons (Chess, Coding, Freeplay, Mathlete)")
        print("   - Hover effects")
        print("   - Selection states")
        print("   - Card-style design")
        
    elif build_status is False:
        print_error("Build failed!")
        print_info("1. Check GitHub Actions logs:")
        if build_url:
            print(f"   {build_url}")
        print_info("2. Fix any compilation errors")
        print_info("3. Push fixes and retry build")
        
    elif build_status is None:
        print_warning("Build status unknown or in progress")
        print_info("1. Check GitHub Actions:")
        if build_url:
            print(f"   {build_url}")
        print_info("2. Wait for build to complete")
        print_info("3. Then check Netlify deployment")
        
    else:
        print_info("1. Monitor GitHub Actions build:")
        print("   https://github.com/rashadwest/BTEBallCODE/actions")
        print_info("2. Once build completes, check Netlify:")
        print("   https://app.netlify.com/sites/ballcode")
        print_info("3. Test game on live site:")
        print("   https://ballcode.netlify.app")

def main():
    """Main function."""
    print_header("🤖 Robot: Unity Next Steps Guide")
    
    print_info(f"Repository: {UNITY_REPO}")
    print_info(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check GitHub Actions
    build_status, build_url = check_github_actions_status()
    
    # Check Netlify
    check_netlify_status()
    
    # Check scene changes
    check_unity_scene_changes()
    
    # Provide next steps
    provide_next_steps(build_status, build_url)
    
    # Additional actions
    print_section("Quick Actions")
    print_info("To check build status manually:")
    print("   gh run list --repo rashadwest/BTEBallCODE")
    print()
    print_info("To view latest build logs:")
    print("   gh run view --repo rashadwest/BTEBallCODE --log")
    print()
    print_info("To trigger a new build:")
    print("   git commit --allow-empty -m 'Trigger build' && git push")
    print()
    print_info("To test UI/UX improvements locally:")
    print("   1. Open Unity Editor")
    print("   2. Open Main Menu scene")
    print("   3. Press Play")
    print("   4. Test game mode buttons")
    
    print()
    print_section("Summary")
    if build_status is True:
        print_success("✅ Ready to test on live site!")
    elif build_status is False:
        print_error("❌ Build failed - check logs and fix issues")
    else:
        print_warning("⏳ Waiting for build to complete...")
    
    print()

if __name__ == "__main__":
    main()


