#!/usr/bin/env python3
"""
Garvis n8n Reviewer - Automated n8n Execution Review System
Reviews n8n workflow executions, identifies issues, and provides insights

Copyright © 2025 Rashad West. All Rights Reserved.

Usage:
    python scripts/garvis-n8n-reviewer.py --yesterday
    python scripts/garvis-n8n-reviewer.py --workflow <workflow_name>
    python scripts/garvis-n8n-reviewer.py --all
"""

import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timedelta

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

# Configuration
N8N_URL = "http://192.168.1.226:5678"
WORKFLOWS = {
    "unity-build": "Unity Build Orchestrator",
    "full-integration": "Full Integration",
    "screenshot-fix": "Screenshot to Fix",
    "garvis": "Garvis Orchestrator"
}

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

def get_n8n_executions(workflow_name: Optional[str] = None, since: Optional[datetime] = None) -> List[Dict]:
    """Get n8n workflow executions"""
    try:
        # Use n8n API to get executions
        # Note: This requires n8n API access or webhook
        # For now, we'll use a simplified approach
        
        # Check if we can access n8n
        result = subprocess.run(
            ["curl", "-s", f"{N8N_URL}/healthz"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode != 0:
            print_warning("Cannot access n8n API directly")
            print_info("Using alternative method: Check n8n UI manually")
            return []
        
        # If we had API access, we would fetch executions here
        # For now, return empty and provide manual instructions
        return []
    except Exception as e:
        print_warning(f"Could not fetch n8n executions: {e}")
        return []

def analyze_execution(execution: Dict) -> Dict:
    """Analyze a single execution for issues"""
    analysis = {
        "status": execution.get("finished", False),
        "success": execution.get("data", {}).get("resultData", {}).get("error") is None,
        "issues": [],
        "warnings": [],
        "insights": []
    }
    
    # Check for errors
    if not analysis["success"]:
        error = execution.get("data", {}).get("resultData", {}).get("error", {})
        analysis["issues"].append({
            "type": "error",
            "message": error.get("message", "Unknown error"),
            "node": error.get("node", {}).get("name", "Unknown")
        })
    
    # Check execution time
    started_at = execution.get("startedAt")
    stopped_at = execution.get("stoppedAt")
    if started_at and stopped_at:
        duration = (stopped_at - started_at).total_seconds()
        if duration > 300:  # More than 5 minutes
            analysis["warnings"].append({
                "type": "slow_execution",
                "duration": duration,
                "message": f"Execution took {duration:.1f} seconds"
            })
    
    return analysis

def generate_review_report(executions: List[Dict], workflow_name: Optional[str] = None) -> str:
    """Generate comprehensive review report"""
    report = []
    report.append("=" * 60)
    report.append("GARVIS N8N EXECUTION REVIEW")
    report.append("=" * 60)
    report.append(f"Timestamp: {datetime.now().isoformat()}")
    if workflow_name:
        report.append(f"Workflow: {workflow_name}")
    report.append("")
    
    if not executions:
        report.append("⚠️  No executions found or n8n API not accessible")
        report.append("")
        report.append("MANUAL REVIEW INSTRUCTIONS:")
        report.append("1. Open n8n UI: http://192.168.1.226:5678")
        report.append("2. Go to 'Executions' tab")
        report.append("3. Review recent executions for:")
        report.append("   - Failed executions (red)")
        report.append("   - Slow executions (>5 minutes)")
        report.append("   - Error messages in node outputs")
        report.append("4. Check each workflow:")
        report.append("   - Unity Build Orchestrator")
        report.append("   - Full Integration")
        report.append("   - Screenshot to Fix")
        report.append("   - Garvis Orchestrator")
        report.append("")
        return "\n".join(report)
    
    # Summary
    total = len(executions)
    successful = sum(1 for e in executions if analyze_execution(e)["success"])
    failed = total - successful
    
    report.append("SUMMARY:")
    report.append(f"  Total Executions: {total}")
    report.append(f"  ✅ Successful: {successful}")
    report.append(f"  ❌ Failed: {failed}")
    report.append("")
    
    # Detailed analysis
    report.append("DETAILED ANALYSIS:")
    for i, execution in enumerate(executions[:10], 1):  # Last 10
        analysis = analyze_execution(execution)
        report.append(f"\nExecution #{i}:")
        report.append(f"  Status: {'✅ Success' if analysis['success'] else '❌ Failed'}")
        
        if analysis["issues"]:
            report.append("  Issues:")
            for issue in analysis["issues"]:
                report.append(f"    - {issue['type']}: {issue['message']}")
        
        if analysis["warnings"]:
            report.append("  Warnings:")
            for warning in analysis["warnings"]:
                report.append(f"    - {warning['type']}: {warning['message']}")
    
    report.append("")
    report.append("=" * 60)
    
    return "\n".join(report)

def check_workflow_status(workflow_name: str) -> Dict:
    """Check if a workflow is active and accessible"""
    status = {
        "name": workflow_name,
        "active": False,
        "accessible": False,
        "webhook": None
    }
    
    # Map workflow names to webhooks
    webhook_map = {
        "unity-build": "/webhook/unity-build",
        "full-integration": "/webhook/ballcode-dev",
        "screenshot-fix": "/webhook/screenshot-fix",
        "garvis": "/webhook/garvis"
    }
    
    webhook_path = webhook_map.get(workflow_name)
    if webhook_path:
        status["webhook"] = f"{N8N_URL}{webhook_path}"
        
        # Test webhook
        try:
            result = subprocess.run(
                ["curl", "-s", "-X", "POST", f"{N8N_URL}{webhook_path}", 
                 "-H", "Content-Type: application/json",
                 "-d", '{"test": true}'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                status["accessible"] = True
                # Check if it's a 404 (not active) or 200 (active)
                if "404" not in result.stdout:
                    status["active"] = True
        except:
            pass
    
    return status

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Garvis n8n Reviewer")
    parser.add_argument("--yesterday", action="store_true", help="Review yesterday's executions")
    parser.add_argument("--workflow", help="Review specific workflow")
    parser.add_argument("--all", action="store_true", help="Review all workflows")
    parser.add_argument("--status", action="store_true", help="Check workflow status")
    
    args = parser.parse_args()
    
    print_header("GARVIS N8N REVIEWER")
    
    # Check workflow status if requested
    if args.status:
        print_info("Checking workflow status...")
        print()
        
        for workflow_id, workflow_name in WORKFLOWS.items():
            status = check_workflow_status(workflow_id)
            print(f"Workflow: {workflow_name}")
            if status["active"]:
                print_success("  Status: Active")
            else:
                print_warning("  Status: Not Active")
            
            if status["webhook"]:
                print_info(f"  Webhook: {status['webhook']}")
            print()
    
    # Get executions
    since = None
    if args.yesterday:
        since = datetime.now() - timedelta(days=1)
    
    workflow_name = args.workflow or (WORKFLOWS.get(args.workflow) if args.workflow else None)
    
    print_info("Fetching executions...")
    executions = get_n8n_executions(workflow_name, since)
    
    # Generate report
    report = generate_review_report(executions, workflow_name)
    print(report)
    
    # Save report
    report_file = Path("documents") / f"GARVIS-N8N-REVIEW-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    report_file.parent.mkdir(exist_ok=True)
    report_file.write_text(report)
    print_info(f"Report saved: {report_file}")
    
    # Provide manual review instructions
    print()
    print_header("MANUAL REVIEW INSTRUCTIONS")
    print_info("Since n8n API access is limited, use these steps:")
    print()
    print("1. Open n8n UI:")
    print(f"   {N8N_URL}")
    print()
    print("2. Go to 'Executions' tab (left sidebar)")
    print()
    print("3. Review recent executions:")
    print("   - Look for failed executions (red)")
    print("   - Check execution times")
    print("   - Review error messages")
    print()
    print("4. Check each workflow:")
    for workflow_id, workflow_name in WORKFLOWS.items():
        print(f"   - {workflow_name}")
    print()
    print("5. For each failed execution:")
    print("   - Click on it to see details")
    print("   - Check which node failed")
    print("   - Review error messages")
    print("   - Note any patterns")

if __name__ == "__main__":
    main()


