#!/usr/bin/env python3
"""
Garvis Unity Build Workflow
Complete workflow for Unity build orchestration

This workflow:
1. Triggers Unity build via n8n
2. Monitors build status
3. Verifies deployment
4. Reports status centrally

Usage:
    python scripts/garvis-unity-build-workflow.py --trigger    # Trigger build
    python scripts/garvis-unity-build-workflow.py --monitor    # Monitor existing build
    python scripts/garvis-unity-build-workflow.py --full       # Trigger + Monitor + Verify

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys
import time
import argparse
import requests
import subprocess
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))

from modules.build_tracker import BuildTracker
from modules.status_reporter import StatusReporter
from modules.api_cache import APICache

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
NC = '\033[0m'

# Configuration
GAME_REPO = "rashadwest/BTEBallCODE"
N8N_BASE_URL = "http://192.168.1.226:5678"
WEBHOOK_PATH = "/webhook/unity-build"
MAX_WAIT_TIME = 1800  # 30 minutes
CHECK_INTERVAL = 30  # Check every 30 seconds

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

def print_step(text):
    print(f"{CYAN}→ {text}{NC}")

def trigger_build(request: str = "Garvis: Unity build", branch: str = "main", status_reporter: Optional[StatusReporter] = None) -> Dict:
    """Trigger Unity build via n8n webhook"""
    print_step(f"Triggering Unity build via n8n...")
    
    url = f"{N8N_BASE_URL}{WEBHOOK_PATH}"
    payload = {
        "request": request,
        "branch": branch,
        "source": "garvis-unity-build-workflow",
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        
        result_data = response.json() if response.content else {}
        
        # Check if build was triggered or skipped
        if result_data.get('status') == 'skipped':
            result = {
                "status": "skipped",
                "message": result_data.get('message', 'Build skipped'),
                "reason": result_data.get('reason', 'Unknown')
            }
            print_warning(f"Build skipped: {result['message']}")
        else:
            result = {
                "status": "triggered",
                "message": "Unity build triggered successfully",
                "response": result_data,
                "timestamp": datetime.now().isoformat()
            }
            print_success("Unity build triggered")
        
        if status_reporter:
            status_reporter.report("unity_build_trigger", {
                "status": result["status"],
                "message": result.get("message", ""),
                "timestamp": result.get("timestamp")
            })
        
        return result
    
    except requests.exceptions.ConnectionError:
        error_msg = f"Cannot connect to n8n at {url}"
        print_error(error_msg)
        return {
            "status": "error",
            "error": error_msg,
            "note": "Check if n8n is running and accessible"
        }
    except requests.exceptions.Timeout:
        error_msg = "n8n webhook timeout"
        print_error(error_msg)
        return {
            "status": "error",
            "error": error_msg
        }
    except Exception as e:
        error_msg = f"Error triggering build: {str(e)}"
        print_error(error_msg)
        return {
            "status": "error",
            "error": error_msg
        }

def monitor_build(commit_sha: Optional[str] = None, run_id: Optional[str] = None, 
                  status_reporter: Optional[StatusReporter] = None) -> Dict:
    """Monitor Unity build status"""
    tracker = BuildTracker()
    
    # Get commit SHA if not provided
    if not commit_sha and not run_id:
        print_step("Getting latest commit SHA...")
        commit_sha = tracker.get_latest_commit_sha()
        if not commit_sha:
            return {
                "status": "error",
                "error": "Could not get latest commit SHA"
            }
        print_info(f"Latest commit: {commit_sha[:8]}")
    
    # Find build
    if run_id:
        print_step(f"Monitoring build run: {run_id}")
        build = {"run_id": run_id}
    else:
        print_step(f"Finding build for commit: {commit_sha[:8]}")
        build = tracker.find_build_for_commit(commit_sha)
        if not build:
            return {
                "status": "pending",
                "message": "Build not found yet (may still be queued)",
                "commit": commit_sha
            }
    
    print_info(f"Found build: {build['run_id']}")
    print_info(f"Status: {build.get('status', 'unknown')}")
    
    # Wait for build completion
    print_step("Waiting for build to complete...")
    print_info(f"Checking every {CHECK_INTERVAL} seconds (max {MAX_WAIT_TIME // 60} minutes)")
    
    build_result = tracker.wait_for_build_completion(build["run_id"], MAX_WAIT_TIME)
    
    # Report status
    if build_result["status"] == "completed":
        conclusion = build_result.get("conclusion", "unknown")
        if conclusion == "success":
            print_success(f"Build completed successfully! (took {build_result['wait_time']}s)")
        else:
            print_error(f"Build completed with status: {conclusion}")
    elif build_result["status"] == "timeout":
        print_warning(f"Build monitoring timeout after {MAX_WAIT_TIME // 60} minutes")
    else:
        print_warning(f"Build status: {build_result['status']}")
    
    if status_reporter:
        status_reporter.report("unity_build_monitor", {
            "status": build_result["status"],
            "conclusion": build_result.get("conclusion"),
            "run_id": build_result.get("run_id"),
            "wait_time": build_result.get("wait_time")
        })
    
    return build_result

def verify_deployment(status_reporter: Optional[StatusReporter] = None) -> Dict:
    """Verify Unity build deployment to Netlify"""
    print_step("Verifying deployment...")
    
    # Check Netlify site
    site_url = "https://ballcode.netlify.app"
    
    try:
        response = requests.get(site_url, timeout=10)
        http_code = response.status_code
        
        if http_code in [200, 301, 302]:
            print_success(f"Site is accessible (HTTP {http_code})")
            result = {
                "status": "success",
                "site_url": site_url,
                "http_code": http_code
            }
        else:
            print_warning(f"Site returned HTTP {http_code}")
            result = {
                "status": "warning",
                "site_url": site_url,
                "http_code": http_code
            }
    except Exception as e:
        print_error(f"Could not verify deployment: {str(e)}")
        result = {
            "status": "error",
            "error": str(e),
            "site_url": site_url
        }
    
    if status_reporter:
        status_reporter.report("unity_deployment", result)
    
    return result

def full_workflow(request: str = "Garvis: Unity build", branch: str = "main", 
                  commit_sha: Optional[str] = None, status_reporter: Optional[StatusReporter] = None) -> Dict:
    """Complete workflow: Trigger + Monitor + Verify"""
    print_header("🚀 GARVIS UNITY BUILD WORKFLOW")
    
    results = {}
    
    # Step 1: Trigger build
    print(f"\n{BLUE}STEP 1: TRIGGER BUILD{NC}")
    print("-" * 60)
    trigger_result = trigger_build(request, branch, status_reporter)
    results["trigger"] = trigger_result
    
    if trigger_result.get("status") != "triggered":
        print_error("Build not triggered. Stopping workflow.")
        return results
    
    # Step 2: Monitor build
    print(f"\n{BLUE}STEP 2: MONITOR BUILD{NC}")
    print("-" * 60)
    
    # Wait a moment for build to start
    print_info("Waiting for build to start...")
    time.sleep(10)
    
    monitor_result = monitor_build(commit_sha, None, status_reporter)
    results["monitor"] = monitor_result
    
    # Step 3: Verify deployment (if build succeeded)
    if monitor_result.get("conclusion") == "success":
        print(f"\n{BLUE}STEP 3: VERIFY DEPLOYMENT{NC}")
        print("-" * 60)
        verify_result = verify_deployment(status_reporter)
        results["verify"] = verify_result
    else:
        print_warning("Skipping deployment verification (build did not succeed)")
        results["verify"] = {"status": "skipped", "reason": "Build failed"}
    
    return results

def main():
    """Main workflow function"""
    parser = argparse.ArgumentParser(
        description='Garvis Unity Build Workflow',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Trigger build
  python scripts/garvis-unity-build-workflow.py --trigger
  
  # Monitor existing build
  python scripts/garvis-unity-build-workflow.py --monitor
  
  # Full workflow (trigger + monitor + verify)
  python scripts/garvis-unity-build-workflow.py --full
  
  # Monitor specific commit
  python scripts/garvis-unity-build-workflow.py --monitor --commit abc1234
  
  # Monitor specific run ID
  python scripts/garvis-unity-build-workflow.py --monitor --run-id 123456789
        """
    )
    
    parser.add_argument('--trigger', action='store_true', help='Trigger Unity build')
    parser.add_argument('--monitor', action='store_true', help='Monitor build status')
    parser.add_argument('--verify', action='store_true', help='Verify deployment')
    parser.add_argument('--full', action='store_true', help='Full workflow (trigger + monitor + verify)')
    parser.add_argument('--request', type=str, default='Garvis: Unity build', help='Build request message')
    parser.add_argument('--branch', type=str, default='main', help='Git branch')
    parser.add_argument('--commit', type=str, help='Commit SHA to monitor')
    parser.add_argument('--run-id', type=str, help='GitHub Actions run ID to monitor')
    
    args = parser.parse_args()
    
    # Initialize status reporter
    status_reporter = StatusReporter()
    
    # Determine mode
    if args.full:
        results = full_workflow(args.request, args.branch, args.commit, status_reporter)
    elif args.trigger:
        results = {"trigger": trigger_build(args.request, args.branch, status_reporter)}
    elif args.monitor:
        results = {"monitor": monitor_build(args.commit, args.run_id, status_reporter)}
    elif args.verify:
        results = {"verify": verify_deployment(status_reporter)}
    else:
        # Default to full workflow
        results = full_workflow(args.request, args.branch, args.commit, status_reporter)
    
    # Print summary
    print_header("📊 WORKFLOW SUMMARY")
    
    for step, result in results.items():
        status = result.get("status", "unknown")
        if status == "success" or status == "triggered" or status == "completed":
            print_success(f"{step.title()}: {result.get('message', 'Success')}")
        elif status == "skipped":
            print_info(f"{step.title()}: {result.get('message', 'Skipped')}")
        elif status == "error":
            print_error(f"{step.title()}: {result.get('error', 'Failed')}")
        else:
            print_warning(f"{step.title()}: {status}")
    
    # Show overall status
    overall_status = status_reporter.get_status().get("overall", "unknown")
    print()
    print_info(f"Overall Status: {overall_status}")
    print_info(f"Status File: {status_reporter.status_file}")
    print()

if __name__ == "__main__":
    main()


