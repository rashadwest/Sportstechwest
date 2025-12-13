#!/usr/bin/env python3
"""
n8n Workflow Deployment Verification Script
Checks if workflow is deployed and configured correctly

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import json
import subprocess
import sys
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
WORKFLOW_FILE = PROJECT_ROOT / "n8n-unity-automation-workflow-FINAL-WORKING.json"

def check_workflow_file():
    """Check if workflow file exists and is valid JSON."""
    print("📄 Checking workflow file...")
    
    if not WORKFLOW_FILE.exists():
        print(f"  ❌ Workflow file not found: {WORKFLOW_FILE}")
        return False
    
    try:
        with open(WORKFLOW_FILE, 'r') as f:
            workflow = json.load(f)
        
        print(f"  ✅ Workflow file found: {WORKFLOW_FILE.name}")
        print(f"  ✅ Valid JSON structure")
        
        # Check for key components
        if 'nodes' in workflow:
            node_count = len(workflow['nodes'])
            print(f"  ✅ Contains {node_count} nodes")
        else:
            print("  ⚠️  No 'nodes' key found")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"  ❌ Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return False

def check_schedule_trigger():
    """Check if schedule trigger is configured correctly."""
    print("⏰ Checking schedule trigger...")
    
    try:
        with open(WORKFLOW_FILE, 'r') as f:
            workflow = json.load(f)
        
        schedule_nodes = [n for n in workflow.get('nodes', []) 
                         if n.get('type') == 'n8n-nodes-base.scheduleTrigger']
        
        if not schedule_nodes:
            print("  ⚠️  No schedule trigger found")
            return False
        
        for node in schedule_nodes:
            schedule = node.get('parameters', {}).get('rule', {})
            # n8n scheduleTrigger may be configured either via cronExpression or interval.
            cron = schedule.get('cronExpression')
            if cron:
                if cron.strip() == "0 * * * *":
                    print("  ✅ Schedule trigger configured for hourly execution (cronExpression)")
                    return True
                print(f"  ⚠️  Schedule trigger cronExpression is not hourly: {cron}")
                print("     Run: python3 scripts/update-n8n-schedule.py")
                return False

            interval = schedule.get('interval', [{}])[0] if schedule.get('interval') else {}
            if interval.get('field') == 'hours' and interval.get('hoursInterval') == 1:
                print("  ✅ Schedule trigger configured for hourly execution (interval)")
                return True
            if interval.get('field') == 'hours' and interval.get('hoursInterval') == 6:
                print("  ⚠️  Schedule trigger set to every 6 hours (should be hourly)")
                print("     Run: python3 scripts/update-n8n-schedule.py")
                return False

            print(f"  ⚠️  Schedule trigger found but configuration unclear: {schedule}")
            return False
        
        return False
        
    except Exception as e:
        print(f"  ❌ Error checking schedule: {e}")
        return False

def check_environment_variables():
    """Check if required environment variables are documented."""
    print("🔐 Checking environment variables...")
    
    required_vars = [
        'OPENAI_API_KEY',
        'GITHUB_TOKEN',
        'NETLIFY_AUTH_TOKEN',
        'N8N_WEBHOOK_URL'
    ]
    
    print("  📋 Required environment variables:")
    for var in required_vars:
        # Check if documented in any config file
        env_file = PROJECT_ROOT / ".env.example"
        if env_file.exists():
            with open(env_file, 'r') as f:
                if var in f.read():
                    print(f"    ✅ {var} (documented)")
                else:
                    print(f"    ⚠️  {var} (not documented)")
        else:
            print(f"    ⚠️  {var} (check manually)")
    
    return True

def check_deployment_script():
    """Check if deployment script exists and is executable."""
    print("🚀 Checking deployment script...")
    
    deploy_script = PROJECT_ROOT / "deploy-n8n-workflow.sh"
    
    if not deploy_script.exists():
        print(f"  ⚠️  Deployment script not found: {deploy_script}")
        return False
    
    if not os.access(deploy_script, os.X_OK):
        print(f"  ⚠️  Deployment script not executable")
        print(f"     Run: chmod +x {deploy_script}")
        return False
    
    print(f"  ✅ Deployment script found and executable")
    return True

def generate_verification_report():
    """Generate a verification report."""
    print()
    print("=" * 60)
    print("📊 n8n Deployment Verification Report")
    print("=" * 60)
    print()
    
    checks = {
        "Workflow File": check_workflow_file(),
        "Schedule Trigger": check_schedule_trigger(),
        "Environment Variables": check_environment_variables(),
        "Deployment Script": check_deployment_script(),
    }
    
    print()
    print("=" * 60)
    print("📋 Summary")
    print("=" * 60)
    
    passed = sum(1 for v in checks.values() if v)
    total = len(checks)
    
    for check, result in checks.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status}: {check}")
    
    print()
    print(f"Progress: {passed}/{total} checks passed ({passed*100//total}%)")
    print()
    
    if passed == total:
        print("✅ All checks passed! Workflow is ready for deployment.")
    else:
        print("⚠️  Some checks failed. Review issues above.")
        print()
        print("🔧 Next Steps:")
        if not checks["Schedule Trigger"]:
            print("  1. Update schedule to hourly: python3 scripts/update-n8n-schedule.py")
        if not checks["Deployment Script"]:
            print("  2. Make deployment script executable: chmod +x deploy-n8n-workflow.sh")
        print("  3. Deploy workflow: ./deploy-n8n-workflow.sh")
        print("  4. Verify in n8n UI that workflow is active")
    
    return passed == total

def main():
    """Run verification checks."""
    success = generate_verification_report()
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

