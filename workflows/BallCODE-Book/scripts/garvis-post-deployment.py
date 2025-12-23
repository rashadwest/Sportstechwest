#!/usr/bin/env python3
"""
Garvis Post-Deployment System - Automated Post-Deployment Verification
Handles all post-deployment tasks automatically

Copyright © 2025 Rashad West. All Rights Reserved.

Usage:
    python scripts/garvis-post-deployment.py --commit <commit_sha>
    python scripts/garvis-post-deployment.py --auto
"""

import sys
import subprocess
from pathlib import Path
from typing import Dict, List
from datetime import datetime

# Import other Garvis modules (using importlib for files with dashes)
import importlib.util
garvis_build_monitor_path = Path(__file__).parent / "garvis-build-monitor.py"
garvis_n8n_reviewer_path = Path(__file__).parent / "garvis-n8n-reviewer.py"

if garvis_build_monitor_path.exists():
    spec = importlib.util.spec_from_file_location("garvis_build_monitor", garvis_build_monitor_path)
    garvis_build_monitor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(garvis_build_monitor)
    wait_for_build_completion = garvis_build_monitor.wait_for_build_completion
    verify_levels_in_game = garvis_build_monitor.verify_levels_in_game
    get_latest_commit_sha = garvis_build_monitor.get_latest_commit_sha
    find_build_for_commit = garvis_build_monitor.find_build_for_commit
else:
    # Fallback if module not found
    def wait_for_build_completion(*args, **kwargs): return {}
    def verify_levels_in_game(*args, **kwargs): return {}
    def get_latest_commit_sha(*args, **kwargs): return None
    def find_build_for_commit(*args, **kwargs): return None

if garvis_n8n_reviewer_path.exists():
    spec = importlib.util.spec_from_file_location("garvis_n8n_reviewer", garvis_n8n_reviewer_path)
    garvis_n8n_reviewer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(garvis_n8n_reviewer)
    check_workflow_status = garvis_n8n_reviewer.check_workflow_status
    WORKFLOWS = garvis_n8n_reviewer.WORKFLOWS
else:
    WORKFLOWS = {}
    def check_workflow_status(*args, **kwargs): return {}

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

def run_post_deployment_checks(commit_sha: str) -> Dict:
    """Run all post-deployment checks"""
    results = {
        "commit": commit_sha,
        "timestamp": datetime.now().isoformat(),
        "build": {},
        "levels": {},
        "n8n": {},
        "overall": "pending"
    }
    
    print_header("GARVIS POST-DEPLOYMENT SYSTEM")
    print_info(f"Commit: {commit_sha[:8]}")
    print()
    
    # Step 1: Monitor Build
    print_header("STEP 1: MONITOR BUILD")
    build = find_build_for_commit(commit_sha)
    if build:
        run_id = build["databaseId"]
        print_info(f"Found build: {run_id}")
        build_result = wait_for_build_completion(run_id)
        results["build"] = build_result
        
        if build_result.get("status") == "success":
            print_success("Build completed successfully!")
        else:
            print_error(f"Build {build_result.get('status')}")
    else:
        print_warning("No build found for this commit")
        results["build"] = {"status": "not_found"}
    
    print()
    
    # Step 2: Verify Levels
    print_header("STEP 2: VERIFY LEVELS")
    if results["build"].get("status") == "success":
        level_results = verify_levels_in_game()
        results["levels"] = level_results
        
        all_verified = all(r.get("exists") for r in level_results.values())
        if all_verified:
            print_success("All levels verified!")
        else:
            print_warning("Some levels not verified")
    else:
        print_warning("Skipping level verification (build not successful)")
    
    print()
    
    # Step 3: Review n8n Executions
    print_header("STEP 3: REVIEW N8N EXECUTIONS")
    n8n_status = {}
    for workflow_id, workflow_name in WORKFLOWS.items():
        status = check_workflow_status(workflow_id)
        n8n_status[workflow_id] = status
        
        if status["active"]:
            print_success(f"{workflow_name}: Active")
        else:
            print_warning(f"{workflow_name}: Not Active")
    
    results["n8n"] = n8n_status
    print()
    
    # Overall Status
    if results["build"].get("status") == "success" and all(r.get("exists") for r in results["levels"].values()):
        results["overall"] = "success"
        print_success("POST-DEPLOYMENT CHECKS: ALL PASSED")
    else:
        results["overall"] = "partial"
        print_warning("POST-DEPLOYMENT CHECKS: SOME ISSUES")
    
    return results

def generate_post_deployment_report(results: Dict) -> str:
    """Generate comprehensive post-deployment report"""
    report = []
    report.append("=" * 60)
    report.append("GARVIS POST-DEPLOYMENT REPORT")
    report.append("=" * 60)
    report.append(f"Timestamp: {datetime.now().isoformat()}")
    report.append(f"Commit: {results.get('commit', 'unknown')[:8]}")
    report.append("")
    
    # Build Status
    report.append("BUILD STATUS:")
    build = results.get("build", {})
    if build.get("status") == "success":
        report.append("  ✅ Build completed successfully")
        if build.get("elapsed"):
            report.append(f"  ⏱️  Time: {build['elapsed'] // 60}m {build['elapsed'] % 60}s")
    elif build.get("status") == "failed":
        report.append("  ❌ Build failed")
    else:
        report.append(f"  ⏳ Build status: {build.get('status', 'unknown')}")
    report.append("")
    
    # Level Verification
    report.append("LEVEL VERIFICATION:")
    levels = results.get("levels", {})
    for level_id, result in levels.items():
        if result.get("exists"):
            report.append(f"  ✅ {level_id}.json: Verified")
        else:
            report.append(f"  ❌ {level_id}.json: Not verified")
    report.append("")
    
    # n8n Status
    report.append("N8N WORKFLOW STATUS:")
    n8n = results.get("n8n", {})
    for workflow_id, status in n8n.items():
        workflow_name = WORKFLOWS.get(workflow_id, workflow_id)
        if status.get("active"):
            report.append(f"  ✅ {workflow_name}: Active")
        else:
            report.append(f"  ⚠️  {workflow_name}: Not Active")
    report.append("")
    
    # Overall
    report.append("OVERALL STATUS:")
    if results.get("overall") == "success":
        report.append("  ✅ ALL CHECKS PASSED")
    else:
        report.append("  ⚠️  SOME CHECKS FAILED")
    report.append("")
    report.append("=" * 60)
    
    return "\n".join(report)

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Garvis Post-Deployment System")
    parser.add_argument("--commit", help="Commit SHA to verify")
    parser.add_argument("--auto", action="store_true", help="Auto-detect latest commit")
    
    args = parser.parse_args()
    
    # Determine commit
    if args.auto:
        commit_sha = get_latest_commit_sha()
        if not commit_sha:
            print_error("Could not get latest commit")
            sys.exit(1)
    elif args.commit:
        commit_sha = args.commit
    else:
        print_error("Must specify --commit or --auto")
        sys.exit(1)
    
    # Run checks
    results = run_post_deployment_checks(commit_sha)
    
    # Generate report
    report = generate_post_deployment_report(results)
    print()
    print(report)
    
    # Save report
    report_file = Path("documents") / f"GARVIS-POST-DEPLOYMENT-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    report_file.parent.mkdir(exist_ok=True)
    report_file.write_text(report)
    print_info(f"Report saved: {report_file}")
    
    # Exit code
    if results.get("overall") == "success":
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

