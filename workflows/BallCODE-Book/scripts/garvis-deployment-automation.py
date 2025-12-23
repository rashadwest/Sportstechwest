#!/usr/bin/env python3
"""
Garvis Deployment Automation - Complete Automated Deployment System
Handles push → build → verify → report automatically

Copyright © 2025 Rashad West. All Rights Reserved.

Usage:
    python scripts/garvis-deployment-automation.py --push-levels
    python scripts/garvis-deployment-automation.py --full-deployment
"""

import sys
import subprocess
from pathlib import Path
from typing import Dict, List
from datetime import datetime

# Import Garvis modules (using importlib for files with dashes)
import importlib.util
garvis_build_monitor_path = Path(__file__).parent / "garvis-build-monitor.py"
garvis_post_deployment_path = Path(__file__).parent / "garvis-post-deployment.py"

if garvis_build_monitor_path.exists():
    spec = importlib.util.spec_from_file_location("garvis_build_monitor", garvis_build_monitor_path)
    garvis_build_monitor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(garvis_build_monitor)
    get_latest_commit_sha = garvis_build_monitor.get_latest_commit_sha
    wait_for_build_completion = garvis_build_monitor.wait_for_build_completion
    verify_levels_in_game = garvis_build_monitor.verify_levels_in_game
else:
    def get_latest_commit_sha(*args, **kwargs): return None
    def wait_for_build_completion(*args, **kwargs): return {}
    def verify_levels_in_game(*args, **kwargs): return {}

if garvis_post_deployment_path.exists():
    spec = importlib.util.spec_from_file_location("garvis_post_deployment", garvis_post_deployment_path)
    garvis_post_deployment = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(garvis_post_deployment)
    run_post_deployment_checks = garvis_post_deployment.run_post_deployment_checks
else:
    def run_post_deployment_checks(*args, **kwargs): return {}

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

GAME_REPO = "rashadwest/BTEBallCODE"
LEVELS_PATH = Path("/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels")
LEVEL_FILES = [
    "book1_foundation_block.json",
    "book2_decision_crossover.json",
    "book3_pattern_loop.json"
]

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

def push_levels_to_github() -> Dict:
    """Push level files to GitHub using gh CLI"""
    print_header("PUSHING LEVELS TO GITHUB")
    
    results = {"pushed": [], "failed": []}
    
    for level_file in LEVEL_FILES:
        source = LEVELS_PATH / level_file
        if not source.exists():
            print_error(f"{level_file} not found")
            results["failed"].append(level_file)
            continue
        
        print_info(f"Pushing {level_file}...")
        
        try:
            # Use gh CLI to push file
            result = subprocess.run(
                ["gh", "api", f"repos/{GAME_REPO}/contents/Assets/StreamingAssets/Levels/{level_file}",
                 "--method", "PUT",
                 "-f", f"message=Add {level_file} with curriculum (Garvis automated)",
                 "-f", f"content=@-",
                 "-f", "branch=main"],
                input=source.read_bytes(),
                capture_output=True,
                check=True
            )
            
            print_success(f"{level_file} pushed successfully")
            results["pushed"].append(level_file)
        except subprocess.CalledProcessError as e:
            print_error(f"{level_file} failed: {e.stderr.decode()[:200]}")
            results["failed"].append(level_file)
        except Exception as e:
            print_error(f"{level_file} failed: {e}")
            results["failed"].append(level_file)
    
    return results

def full_deployment_automation() -> Dict:
    """Complete automated deployment: push → build → verify"""
    print_header("GARVIS FULL DEPLOYMENT AUTOMATION")
    
    deployment = {
        "timestamp": datetime.now().isoformat(),
        "push": {},
        "build": {},
        "verification": {},
        "status": "pending"
    }
    
    # Step 1: Push Levels
    print_header("STEP 1: PUSH LEVELS")
    push_results = push_levels_to_github()
    deployment["push"] = push_results
    
    if push_results["failed"]:
        print_error("Some files failed to push")
        deployment["status"] = "failed"
        return deployment
    
    print_success("All levels pushed successfully!")
    print()
    
    # Step 2: Get commit and monitor build
    print_header("STEP 2: MONITOR BUILD")
    commit_sha = get_latest_commit_sha()
    if not commit_sha:
        print_error("Could not get commit SHA")
        deployment["status"] = "failed"
        return deployment
    
    print_info(f"Latest commit: {commit_sha[:8]}")
    
    # Step 3: Run post-deployment checks
    print_header("STEP 3: POST-DEPLOYMENT VERIFICATION")
    verification = run_post_deployment_checks(commit_sha)
    deployment["verification"] = verification
    
    if verification.get("overall") == "success":
        deployment["status"] = "success"
        print_success("DEPLOYMENT COMPLETE: ALL CHECKS PASSED")
    else:
        deployment["status"] = "partial"
        print_warning("DEPLOYMENT COMPLETE: SOME CHECKS FAILED")
    
    return deployment

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Garvis Deployment Automation")
    parser.add_argument("--push-levels", action="store_true", help="Push level files only")
    parser.add_argument("--full-deployment", action="store_true", help="Full automated deployment")
    
    args = parser.parse_args()
    
    if args.push_levels:
        results = push_levels_to_github()
        if results["failed"]:
            sys.exit(1)
    elif args.full_deployment:
        deployment = full_deployment_automation()
        
        # Save deployment report
        report_file = Path("documents") / f"GARVIS-DEPLOYMENT-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
        report_file.parent.mkdir(exist_ok=True)
        
        report = f"""# Garvis Deployment Report

**Timestamp:** {deployment['timestamp']}
**Status:** {deployment['status']}

## Push Results
- Pushed: {len(deployment['push'].get('pushed', []))}
- Failed: {len(deployment['push'].get('failed', []))}

## Verification
- Overall: {deployment['verification'].get('overall', 'unknown')}
"""
        report_file.write_text(report)
        print_info(f"Report saved: {report_file}")
        
        if deployment["status"] == "success":
            sys.exit(0)
        else:
            sys.exit(1)
    else:
        print_error("Must specify --push-levels or --full-deployment")
        sys.exit(1)

if __name__ == "__main__":
    main()

