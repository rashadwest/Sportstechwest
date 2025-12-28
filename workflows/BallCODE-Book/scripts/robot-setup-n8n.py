#!/usr/bin/env python3
"""
Robot: Automated n8n Setup & Testing
Sets environment variables and tests everything automatically

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import json
import requests
from pathlib import Path
from datetime import datetime

# n8n Configuration
N8N_URL = "http://192.168.1.226:5678"
N8N_HOST = "192.168.1.226"

# Required environment variables
REQUIRED_ENV_VARS = {
    "GITHUB_REPO_OWNER": "rashadwest",
    "GITHUB_REPO_NAME": "BTEBallCODE",
    "GITHUB_WORKFLOW_FILE": "unity-webgl-build.yml",
    "NETLIFY_SITE_ID": "",  # Will need to be set
    "NETLIFY_SITE_NAME": "ballcode-game",
    "N8N_INSTANCE_ROLE": "prod",
    "WORKFLOW_PATH": "/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"
}

def print_header(title):
    """Print formatted header."""
    print("\n" + "=" * 70)
    print(f"🤖 {title}")
    print("=" * 70)

def check_n8n_connectivity():
    """Check if n8n is accessible."""
    print_header("Checking n8n Connectivity")
    try:
        response = requests.get(f"{N8N_URL}/healthz", timeout=5)
        if response.status_code == 200:
            print("✅ n8n is accessible")
            return True
        else:
            print(f"❌ n8n returned {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to n8n: {e}")
        print(f"   URL: {N8N_URL}")
        return False

def create_env_setup_instructions():
    """Create instructions for setting env vars in n8n."""
    print_header("Environment Variables Setup Instructions")
    
    print("\n📋 Required Environment Variables:")
    print()
    for key, default in REQUIRED_ENV_VARS.items():
        if default:
            print(f"   {key} = {default}")
        else:
            print(f"   {key} = [NEEDS TO BE SET]")
    
    print("\n🔧 To Set in n8n:")
    print(f"   1. Open: {N8N_URL}")
    print("   2. Click Settings (gear icon) → Environment Variables")
    print("   3. Add each variable above")
    print("   4. Save")
    print("   5. Restart n8n: sudo systemctl restart n8n")
    print()
    
    # Create setup script for Pi
    script_content = f"""#!/bin/bash
# Automated n8n Environment Variables Setup
# Run this on the Pi where n8n is running

echo "🤖 Setting up n8n environment variables..."

# Check if n8n service exists
if systemctl list-unit-files | grep -q n8n.service; then
    echo "📋 n8n is running as a service"
    echo ""
    echo "To set environment variables:"
    echo "1. Edit n8n service file:"
    echo "   sudo nano /etc/systemd/system/n8n.service"
    echo ""
    echo "2. Add Environment variables in [Service] section:"
    echo "   [Service]"
    echo "   Environment=\"GITHUB_REPO_OWNER=rashadwest\""
    echo "   Environment=\"GITHUB_REPO_NAME=BTEBallCODE\""
    echo "   Environment=\"GITHUB_WORKFLOW_FILE=unity-webgl-build.yml\""
    echo "   Environment=\"NETLIFY_SITE_NAME=ballcode-game\""
    echo "   Environment=\"N8N_INSTANCE_ROLE=prod\""
    echo ""
    echo "3. Reload and restart:"
    echo "   sudo systemctl daemon-reload"
    echo "   sudo systemctl restart n8n"
else
    echo "📋 n8n is running manually"
    echo ""
    echo "Set environment variables in n8n UI:"
    echo "1. Open: {N8N_URL}"
    echo "2. Settings → Environment Variables"
    echo "3. Add each variable"
fi

echo ""
echo "✅ Setup instructions complete"
"""
    
    script_file = Path(__file__).parent / "setup-n8n-env-on-pi.sh"
    with open(script_file, 'w') as f:
        f.write(script_content)
    os.chmod(script_file, 0o755)
    
    print(f"💾 Created setup script: {script_file}")
    print("   (Run this on the Pi to set environment variables)")
    
    return script_file

def test_all_workflows():
    """Test all workflow webhooks."""
    print_header("Testing All Workflows")
    
    workflows = {
        "unity-build": {
            "name": "Unity Build Orchestrator",
            "webhook": "/webhook/unity-build",
            "payload": {"request": "Robot test", "branch": "main"}
        },
        "full-integration": {
            "name": "Full Integration - AI Analysis",
            "webhook": "/webhook/ballcode-dev",
            "payload": {"prompt": "Robot test - verify system"}
        },
        "screenshot-fix": {
            "name": "Screenshot-to-Fix Automation",
            "webhook": "/webhook/screenshot-fix",
            "payload": {"screenshotUrl": "https://example.com/test.png", "context": "Robot test"}
        }
    }
    
    results = {}
    
    for workflow_id, config in workflows.items():
        print(f"\n🧪 Testing: {config['name']}")
        try:
            response = requests.post(
                f"{N8N_URL}{config['webhook']}",
                json=config["payload"],
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            success = response.status_code == 200
            status_icon = "✅" if success else "❌"
            
            print(f"   {status_icon} Status: {response.status_code}")
            
            if response.text:
                print(f"   Response: {response.text[:150]}")
            
            results[workflow_id] = {
                "success": success,
                "status_code": response.status_code,
                "response": response.text[:200] if response.text else ""
            }
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            results[workflow_id] = {"success": False, "error": str(e)}
    
    return results

def check_credentials():
    """Check if credentials are needed."""
    print_header("Credentials Check")
    
    print("\n📋 Required Credentials:")
    print("   1. OpenAI API (for Screenshot-to-Fix and Full Integration)")
    print("   2. GitHub Actions Token (for Unity Build Orchestrator)")
    print("   3. Netlify API Token (for Unity Build Orchestrator)")
    print()
    print("💡 To add credentials:")
    print(f"   1. Open: {N8N_URL}")
    print("   2. Click 'Credentials' in sidebar")
    print("   3. Add each credential")
    print("   4. Assign to workflow nodes")
    print()

def generate_comprehensive_report(results):
    """Generate comprehensive test report."""
    print_header("Comprehensive Test Report")
    
    successful = sum(1 for r in results.values() if r.get("success"))
    total = len(results)
    success_rate = (successful / total * 100) if total > 0 else 0
    
    print(f"\n📊 Test Results:")
    print(f"   Total Workflows: {total}")
    print(f"   Successful: {successful}")
    print(f"   Failed: {total - successful}")
    print(f"   Success Rate: {success_rate:.1f}%")
    print()
    
    print("📋 Detailed Results:")
    for workflow_id, result in results.items():
        status = "✅" if result.get("success") else "❌"
        workflow_name = {
            "unity-build": "Unity Build Orchestrator",
            "full-integration": "Full Integration",
            "screenshot-fix": "Screenshot-to-Fix"
        }.get(workflow_id, workflow_id)
        
        print(f"   {status} {workflow_name}")
        if not result.get("success"):
            error = result.get("error") or f"Status {result.get('status_code', 'unknown')}"
            print(f"      Error: {error}")
    
    # Save report
    report_file = Path(__file__).parent.parent / "ROBOT-TEST-REPORT.json"
    with open(report_file, 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "n8n_url": N8N_URL,
            "results": results,
            "summary": {
                "total": total,
                "successful": successful,
                "failed": total - successful,
                "success_rate": success_rate
            }
        }, f, indent=2)
    
    print(f"\n💾 Report saved: {report_file}")
    
    return success_rate == 100

def main():
    """Main robot function."""
    print_header("Robot: Automated n8n Setup & Testing")
    print(f"\n📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎯 Goal: Set environment variables and test all workflows")
    
    # Step 1: Check connectivity
    if not check_n8n_connectivity():
        print("\n❌ Cannot connect to n8n. Fix connectivity first.")
        return False
    
    # Step 2: Create env var setup instructions
    create_env_setup_instructions()
    
    # Step 3: Check credentials
    check_credentials()
    
    # Step 4: Test workflows
    results = test_all_workflows()
    
    # Step 5: Generate report
    all_passed = generate_comprehensive_report(results)
    
    # Summary
    print_header("Summary & Next Steps")
    
    if all_passed:
        print("\n✅ All workflows are working!")
        print("   No action needed.")
    else:
        print("\n⚠️  Some workflows need attention:")
        print()
        print("   1. Set environment variables in n8n:")
        print(f"      - Open: {N8N_URL}")
        print("      - Settings → Environment Variables")
        print("      - Add all required variables")
        print()
        print("   2. Add credentials if missing:")
        print("      - OpenAI API (for AI workflows)")
        print("      - GitHub Token (for Unity Build)")
        print("      - Netlify Token (for Unity Build)")
        print()
        print("   3. Check n8n Executions tab for error details")
        print()
        print("   4. Restart n8n after setting variables:")
        print("      ssh pi@192.168.1.226")
        print("      sudo systemctl restart n8n")
        print()
        print("   5. Re-run this script to verify fixes:")
        print("      python3 scripts/robot-setup-n8n.py")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)


