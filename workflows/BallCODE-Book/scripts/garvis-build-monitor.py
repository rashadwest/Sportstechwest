#!/usr/bin/env python3
"""
Garvis Build Monitor - Automated Unity Build Monitoring System
Monitors Unity builds, verifies completion, and handles next steps automatically

Copyright © 2025 Rashad West. All Rights Reserved.

Usage:
    python scripts/garvis-build-monitor.py --commit <commit_sha>
    python scripts/garvis-build-monitor.py --latest
    python scripts/garvis-build-monitor.py --watch <run_id>
"""

import sys
import time
import json
import subprocess
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime, timedelta

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

# Configuration
GAME_REPO = "rashadwest/BTEBallCODE"
WORKFLOW_FILE = "unity-webgl-build.yml"
NETLIFY_SITE = "ballcode"
MAX_WAIT_TIME = 1800  # 30 minutes max wait
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

def get_latest_commit_sha() -> Optional[str]:
    """Get latest commit SHA from Unity repo"""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{GAME_REPO}/commits/main", "--jq", ".sha"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        print_error(f"Failed to get latest commit: {e}")
        return None

def find_build_for_commit(commit_sha: str) -> Optional[Dict]:
    """Find GitHub Actions run for a specific commit"""
    try:
        result = subprocess.run(
            ["gh", "run", "list", "--repo", GAME_REPO, "--workflow", WORKFLOW_FILE, 
             "--json", "databaseId,status,conclusion,headSha,createdAt,updatedAt,displayTitle"],
            capture_output=True,
            text=True,
            check=True
        )
        runs = json.loads(result.stdout)
        
        # Find run matching commit SHA
        for run in runs:
            if run.get("headSha", "").startswith(commit_sha):
                return run
        
        return None
    except Exception as e:
        print_error(f"Failed to find build: {e}")
        return None

def get_build_status(run_id: int) -> Dict:
    """Get current status of a build"""
    try:
        result = subprocess.run(
            ["gh", "run", "view", str(run_id), "--repo", GAME_REPO, "--json", 
             "status,conclusion,headSha,createdAt,updatedAt,displayTitle,url"],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except Exception as e:
        print_error(f"Failed to get build status: {e}")
        return {}

def check_netlify_deploy() -> Dict:
    """Check latest Netlify deployment status"""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{GAME_REPO}/deployments", "--jq", 
             ".[0] | {state: .state, created_at: .created_at, updated_at: .updated_at, url: .statuses_url}"],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout) if result.stdout.strip() else {}
    except Exception as e:
        print_warning(f"Could not check Netlify deploy: {e}")
        return {}

def wait_for_build_completion(run_id: int, max_wait: int = MAX_WAIT_TIME) -> Dict:
    """Monitor build until completion"""
    print_info(f"Monitoring build {run_id}...")
    print_info(f"Max wait time: {max_wait // 60} minutes")
    print()
    
    start_time = time.time()
    last_status = None
    
    while True:
        elapsed = int(time.time() - start_time)
        
        if elapsed > max_wait:
            print_error(f"Build timeout after {max_wait // 60} minutes")
            return {"status": "timeout", "elapsed": elapsed}
        
        build_status = get_build_status(run_id)
        current_status = build_status.get("status", "unknown")
        conclusion = build_status.get("conclusion")
        
        # Status changed
        if current_status != last_status:
            print_info(f"Status: {current_status.upper()}")
            if build_status.get("url"):
                print_info(f"View: {build_status['url']}")
            last_status = current_status
        
        # Build completed
        if conclusion:
            elapsed_min = elapsed // 60
            elapsed_sec = elapsed % 60
            
            if conclusion == "success":
                print_success(f"Build completed successfully!")
                print_info(f"Time: {elapsed_min}m {elapsed_sec}s")
                return {
                    "status": "success",
                    "conclusion": conclusion,
                    "elapsed": elapsed,
                    "run_id": run_id,
                    "url": build_status.get("url")
                }
            else:
                print_error(f"Build {conclusion}")
                print_info(f"Time: {elapsed_min}m {elapsed_sec}s")
                return {
                    "status": "failed",
                    "conclusion": conclusion,
                    "elapsed": elapsed,
                    "run_id": run_id,
                    "url": build_status.get("url")
                }
        
        # Wait before next check
        time.sleep(CHECK_INTERVAL)
        print(f"⏳ Waiting... ({elapsed // 60}m {elapsed % 60}s)", end="\r")

def verify_levels_in_game() -> Dict:
    """Verify that levels are accessible in the game"""
    print_header("Verifying Levels in Game")
    
    levels_to_check = [
        "book1_foundation_block",
        "book2_decision_crossover",
        "book3_pattern_loop"
    ]
    
    results = {}
    game_url = f"https://{NETLIFY_SITE}.netlify.app"
    
    print_info(f"Game URL: {game_url}")
    print_info("Checking if levels are accessible...")
    print()
    
    # Check if levels exist in repo
    for level_id in levels_to_check:
        try:
            result = subprocess.run(
                ["gh", "api", f"repos/{GAME_REPO}/contents/Assets/StreamingAssets/Levels/{level_id}.json"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print_success(f"{level_id}.json exists in repository")
                results[level_id] = {"exists": True, "status": "verified"}
            else:
                print_error(f"{level_id}.json not found in repository")
                results[level_id] = {"exists": False, "status": "missing"}
        except Exception as e:
            print_warning(f"Could not verify {level_id}: {e}")
            results[level_id] = {"exists": None, "status": "unknown", "error": str(e)}
    
    return results

def generate_build_report(build_result: Dict, level_verification: Dict) -> str:
    """Generate comprehensive build report"""
    report = []
    report.append("=" * 60)
    report.append("GARVIS BUILD MONITOR REPORT")
    report.append("=" * 60)
    report.append(f"Timestamp: {datetime.now().isoformat()}")
    report.append("")
    
    # Build Status
    report.append("BUILD STATUS:")
    if build_result.get("status") == "success":
        report.append(f"  ✅ Build completed successfully")
        report.append(f"  ⏱️  Time: {build_result.get('elapsed', 0) // 60}m {build_result.get('elapsed', 0) % 60}s")
    elif build_result.get("status") == "failed":
        report.append(f"  ❌ Build failed: {build_result.get('conclusion', 'unknown')}")
    else:
        report.append(f"  ⏳ Build status: {build_result.get('status', 'unknown')}")
    
    if build_result.get("url"):
        report.append(f"  🔗 View: {build_result.get('url')}")
    report.append("")
    
    # Level Verification
    report.append("LEVEL VERIFICATION:")
    for level_id, result in level_verification.items():
        if result.get("exists"):
            report.append(f"  ✅ {level_id}.json: Verified")
        elif result.get("exists") is False:
            report.append(f"  ❌ {level_id}.json: Missing")
        else:
            report.append(f"  ⚠️  {level_id}.json: Unknown")
    report.append("")
    
    # Next Steps
    report.append("NEXT STEPS:")
    if build_result.get("status") == "success":
        report.append("  1. ✅ Build complete - Game should be live")
        report.append("  2. ⏳ Test levels in game at: https://ballcode.netlify.app")
        report.append("  3. ⏳ Verify all 3 book levels work correctly")
    elif build_result.get("status") == "failed":
        report.append("  1. ❌ Build failed - Check logs for errors")
        report.append("  2. ⏳ Review GitHub Actions logs")
        report.append("  3. ⏳ Fix issues and retry")
    else:
        report.append("  1. ⏳ Build still in progress - Continue monitoring")
    
    report.append("")
    report.append("=" * 60)
    
    return "\n".join(report)

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Garvis Build Monitor")
    parser.add_argument("--commit", help="Commit SHA to monitor")
    parser.add_argument("--latest", action="store_true", help="Monitor latest commit")
    parser.add_argument("--watch", type=int, help="Watch specific run ID")
    parser.add_argument("--no-wait", action="store_true", help="Don't wait, just check status")
    parser.add_argument("--verify-levels", action="store_true", help="Verify levels after build")
    
    args = parser.parse_args()
    
    print_header("GARVIS BUILD MONITOR")
    
    # Determine which build to monitor
    if args.watch:
        run_id = args.watch
        print_info(f"Monitoring run ID: {run_id}")
    elif args.latest or args.commit:
        commit_sha = args.commit or get_latest_commit_sha()
        if not commit_sha:
            print_error("Could not determine commit SHA")
            sys.exit(1)
        
        print_info(f"Finding build for commit: {commit_sha[:8]}...")
        build = find_build_for_commit(commit_sha)
        
        if not build:
            print_error("No build found for this commit")
            sys.exit(1)
        
        run_id = build["databaseId"]
        print_info(f"Found build: {run_id}")
        print_info(f"Status: {build.get('status', 'unknown')}")
    else:
        print_error("Must specify --commit, --latest, or --watch")
        sys.exit(1)
    
    # Check current status
    build_status = get_build_status(run_id)
    current_status = build_status.get("status", "unknown")
    conclusion = build_status.get("conclusion")
    
    print()
    print_info(f"Current Status: {current_status.upper()}")
    if conclusion:
        print_info(f"Conclusion: {conclusion.upper()}")
    if build_status.get("url"):
        print_info(f"View: {build_status['url']}")
    print()
    
    # Wait for completion if not done
    if not args.no_wait and not conclusion:
        build_result = wait_for_build_completion(run_id)
    else:
        build_result = {
            "status": conclusion or current_status,
            "run_id": run_id,
            "url": build_status.get("url")
        }
    
    # Verify levels if requested
    level_verification = {}
    if args.verify_levels or build_result.get("status") == "success":
        level_verification = verify_levels_in_game()
    
    # Generate report
    report = generate_build_report(build_result, level_verification)
    print()
    print(report)
    
    # Save report
    report_file = Path("documents") / f"GARVIS-BUILD-REPORT-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    report_file.parent.mkdir(exist_ok=True)
    report_file.write_text(report)
    print_info(f"Report saved: {report_file}")
    
    # Exit code based on result
    if build_result.get("status") == "success":
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

