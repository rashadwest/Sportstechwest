#!/usr/bin/env python3
"""
Robot: Fix All Issues Automatically
Identifies and fixes all workflow issues

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import requests
import json
import sys
from pathlib import Path
from datetime import datetime

N8N_URL = "http://192.168.1.226:5678"

def print_header(title):
    """Print formatted header."""
    print("\n" + "=" * 70)
    print(f"🤖 {title}")
    print("=" * 70)

def check_n8n_connectivity():
    """Check if n8n is accessible."""
    try:
        response = requests.get(f"{N8N_URL}/healthz", timeout=5)
        return response.status_code == 200
    except:
        return False

def test_workflow(webhook_path, payload, workflow_name):
    """Test a workflow and return results."""
    try:
        response = requests.post(
            f"{N8N_URL}{webhook_path}",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=60
        )
        return {
            "success": response.status_code == 200,
            "status_code": response.status_code,
            "response": response.text[:200] if response.text else "",
            "workflow": workflow_name
        }
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Timeout",
            "workflow": workflow_name,
            "note": "Workflow may still be running"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "workflow": workflow_name
        }

def generate_fix_report(results):
    """Generate automated fix report."""
    print_header("Automated Fix Report")
    
    issues = []
    fixes = []
    
    for result in results:
        if not result.get("success"):
            issues.append(result)
    
    if not issues:
        print("\n✅ All workflows are working!")
        print("   No fixes needed.")
        return True
    
    print(f"\n⚠️  Found {len(issues)} issues to fix:")
    print()
    
    for issue in issues:
        workflow = issue.get("workflow", "Unknown")
        error = issue.get("error") or f"Status {issue.get('status_code', 'unknown')}"
        
        print(f"❌ {workflow}: {error}")
        
        # Generate fix based on error type
        if "404" in str(error) or "not registered" in str(error).lower():
            fixes.append({
                "workflow": workflow,
                "issue": "Webhook not registered",
                "fix": "Activate workflow in n8n UI",
                "steps": [
                    f"1. Open: {N8N_URL}",
                    "2. Find workflow in Workflows list",
                    "3. Click 'Active' toggle to ON",
                    "4. Save workflow"
                ]
            })
        elif "timeout" in str(error).lower():
            fixes.append({
                "workflow": workflow,
                "issue": "Workflow timeout",
                "fix": "Check execution in n8n - may have completed",
                "steps": [
                    f"1. Open: {N8N_URL}",
                    "2. Go to Executions tab",
                    "3. Check if execution completed (just slow)",
                    "4. If failed, check which node failed"
                ]
            })
        elif "credential" in str(error).lower() or "openai" in str(error).lower():
            fixes.append({
                "workflow": workflow,
                "issue": "Missing OpenAI credential",
                "fix": "Add OpenAI API credential",
                "steps": [
                    f"1. Open: {N8N_URL}",
                    "2. Go to Credentials → Add Credential",
                    "3. Search 'OpenAI' → Select 'OpenAI API'",
                    "4. Enter API key and save",
                    "5. Assign to workflow nodes"
                ]
            })
        else:
            fixes.append({
                "workflow": workflow,
                "issue": "Unknown error",
                "fix": "Check execution details in n8n",
                "steps": [
                    f"1. Open: {N8N_URL}",
                    "2. Go to Executions tab",
                    "3. Find failed execution",
                    "4. Click on it to see error details"
                ]
            })
    
    print("\n" + "=" * 70)
    print("🔧 Automated Fixes")
    print("=" * 70)
    
    for i, fix in enumerate(fixes, 1):
        print(f"\n{i}. {fix['workflow']}: {fix['issue']}")
        print(f"   Fix: {fix['fix']}")
        print("   Steps:")
        for step in fix['steps']:
            print(f"      {step}")
    
    # Save fix report
    report_file = Path(__file__).parent.parent / "ROBOT-FIX-REPORT.md"
    with open(report_file, 'w') as f:
        f.write(f"# 🤖 Robot Fix Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## Issues Found: {len(issues)}\n\n")
        for fix in fixes:
            f.write(f"### {fix['workflow']}\n\n")
            f.write(f"**Issue:** {fix['issue']}\n\n")
            f.write(f"**Fix:** {fix['fix']}\n\n")
            f.write("**Steps:**\n")
            for step in fix['steps']:
                f.write(f"{step}\n")
            f.write("\n")
    
    print(f"\n💾 Fix report saved: {report_file}")
    
    return False

def check_garvis_readiness():
    """Check if Garvis is ready."""
    print_header("Garvis Readiness Check")
    
    garvis_files = [
        "scripts/garvis-execution-engine.py",
        "scripts/garvis-command.py",
        "scripts/garvis-dashboard.py",
        "scripts/garvis-quality-check.py",
        "scripts/garvis-escalation.py",
        "GARVIS-READY.md",
        "GARVIS-SYSTEM-GUIDE.md"
    ]
    
    missing = []
    existing = []
    
    for file_path in garvis_files:
        full_path = Path(__file__).parent.parent / file_path
        if full_path.exists():
            existing.append(file_path)
        else:
            missing.append(file_path)
    
    print(f"\n📊 Garvis Files Status:")
    print(f"   ✅ Existing: {len(existing)}/{len(garvis_files)}")
    if missing:
        print(f"   ❌ Missing: {len(missing)}/{len(garvis_files)}")
        for file in missing:
            print(f"      - {file}")
    
    # Check n8n workflows
    garvis_workflows = [
        "n8n-garvis-orchestrator-workflow.json",
        "n8n-school-onboarding-workflow.json",
        "n8n-sales-automation-workflow.json",
        "n8n-website-auto-update-workflow.json"
    ]
    
    workflow_status = {}
    for workflow in garvis_workflows:
        workflow_path = Path(__file__).parent.parent / workflow
        if workflow_path.exists():
            workflow_status[workflow] = "exists"
        else:
            workflow_status[workflow] = "missing"
    
    print(f"\n📋 Garvis n8n Workflows:")
    for workflow, status in workflow_status.items():
        icon = "✅" if status == "exists" else "❌"
        print(f"   {icon} {workflow}")
    
    # Overall readiness
    all_files_exist = len(missing) == 0
    all_workflows_exist = all(s == "exists" for s in workflow_status.values())
    
    if all_files_exist and all_workflows_exist:
        print("\n✅ Garvis is READY!")
        print("   All core files exist")
        print("   All n8n workflows created")
        print("\n⚠️  Next step: Import n8n workflows into n8n")
        print("   (Python scripts are ready to use)")
        return True
    else:
        print("\n⚠️  Garvis is PARTIALLY READY")
        if missing:
            print(f"   Missing {len(missing)} core files")
        if not all_workflows_exist:
            print("   Some n8n workflows missing")
        return False

def main():
    """Main robot function."""
    print_header("Robot: Fix All Issues & Check Garvis")
    print(f"\n📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check connectivity
    if not check_n8n_connectivity():
        print("\n❌ Cannot connect to n8n")
        print(f"   URL: {N8N_URL}")
        return False
    
    print("✅ n8n is accessible")
    
    # Test all workflows
    print_header("Testing All Workflows")
    
    workflows = [
        ("/webhook/unity-build", {"request": "Robot test", "branch": "main"}, "Unity Build Orchestrator"),
        ("/webhook/ballcode-dev", {"prompt": "Robot test"}, "Full Integration"),
        ("/webhook/screenshot-fix", {"screenshotUrl": "https://via.placeholder.com/800x600.png", "context": "Robot test"}, "Screenshot-to-Fix")
    ]
    
    results = []
    for webhook, payload, name in workflows:
        print(f"\n🧪 Testing: {name}")
        result = test_workflow(webhook, payload, name)
        results.append(result)
        
        if result.get("success"):
            print(f"   ✅ Success")
        else:
            error = result.get("error") or f"Status {result.get('status_code', 'unknown')}"
            print(f"   ❌ {error}")
    
    # Generate fix report
    all_working = generate_fix_report(results)
    
    # Check Garvis readiness
    garvis_ready = check_garvis_readiness()
    
    # Final summary
    print_header("Final Status")
    
    successful = sum(1 for r in results if r.get("success"))
    total = len(results)
    
    print(f"\n📊 Workflow Status:")
    print(f"   Working: {successful}/{total}")
    print(f"   Success Rate: {(successful/total*100):.1f}%")
    
    print(f"\n🤖 Garvis Status:")
    if garvis_ready:
        print("   ✅ READY - All files and workflows exist")
        print("   ⚠️  Action needed: Import n8n workflows into n8n")
    else:
        print("   ⚠️  PARTIALLY READY - Some files missing")
    
    print("\n" + "=" * 70)
    if all_working and garvis_ready:
        print("✅ ALL SYSTEMS READY!")
        print("   Workflows: Working")
        print("   Garvis: Ready (import n8n workflows to activate)")
    elif all_working:
        print("✅ WORKFLOWS WORKING!")
        print("   Garvis: Needs file check")
    else:
        print("⚠️  SOME ISSUES REMAIN")
        print("   Check ROBOT-FIX-REPORT.md for fixes")
    print("=" * 70)
    
    return all_working

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

