#!/usr/bin/env python3
"""
Garvis Unified Deployment System
Single entry point for all deployment operations

Consolidates:
- garvis-push.py (quick deployment)
- garvis-deployment-automation.py (full automation)
- garvis-post-deployment.py (verification)
- garvis-deploy-all.py (deploy everything)

Usage:
    python scripts/garvis-deploy.py --quick          # Fast push (website + game)
    python scripts/garvis-deploy.py --full           # Complete automation (push + build + verify)
    python scripts/garvis-deploy.py --verify         # Post-deployment verification only
    python scripts/garvis-deploy.py --game           # Game deployment only
    python scripts/garvis-deploy.py --website        # Website deployment only

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys
import subprocess
import argparse
from pathlib import Path
from typing import Dict, Optional

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))

# Import modules
from modules.build_tracker import BuildTracker
from modules.status_reporter import StatusReporter
from modules.unity_pusher import UnityPusher
from modules.api_cache import APICache

# Import shared utilities from garvis-push.py
sys.path.insert(0, str(Path(__file__).parent))
import importlib.util
garvis_push_spec = importlib.util.spec_from_file_location(
    "garvis_push",
    Path(__file__).parent / "garvis-push.py"
)
garvis_push = importlib.util.module_from_spec(garvis_push_spec)
garvis_push_spec.loader.exec_module(garvis_push)

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

# Configuration
WEBSITE_PATH = Path("/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode")
GAME_LEVELS_PATH = Path("/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels")
WORKFLOW_DIR = Path(__file__).parent.parent

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

def deploy_website(commit_message: str = "Garvis: Deploy website updates", status_reporter: Optional[StatusReporter] = None) -> Dict:
    """Deploy website to GitHub"""
    print_info("Checking website for changes...")
    
    # Use function from garvis-push.py
    result = garvis_push.push_website(commit_message)
    
    if status_reporter:
        status_reporter.report("website", {
            "status": result.get("status", "unknown"),
            "message": result.get("message", ""),
            "error": result.get("error")
        })
    
    return result

def deploy_game_levels(commit_message: str = "Garvis: Add Book 1, 2, 3 levels with curriculum", 
                       status_reporter: Optional[StatusReporter] = None) -> Dict:
    """Deploy game levels to Unity repository via GitHub API"""
    print_info("Pushing game levels via GitHub API...")
    
    pusher = UnityPusher()
    results = pusher.push_levels(LEVEL_FILES, GAME_LEVELS_PATH, commit_message)
    
    if results["failed"]:
        return {
            "status": "error",
            "error": f"Failed to push: {', '.join([f['file'] for f in results['failed']])}",
            "pushed": results["pushed"],
            "failed": results["failed"]
        }
    
    if not results["pushed"]:
        return {
            "status": "skipped",
            "message": "No levels to push"
        }
    
    result = {
        "status": "success",
        "message": f"Pushed {len(results['pushed'])} level files",
        "files": results["pushed"]
    }
    
    if status_reporter:
        status_reporter.report("game", {
            "status": "success",
            "files": results["pushed"],
            "message": result["message"]
        })
    
    return result

def trigger_unity_build(status_reporter: Optional[StatusReporter] = None) -> Dict:
    """Trigger Unity build via n8n webhook"""
    import requests
    import os
    
    n8n_url = os.getenv("N8N_BASE_URL", "http://192.168.1.226:5678")
    url = f"{n8n_url}/webhook/unity-build"
    
    payload = {
        "request": "Build Unity game",
        "branch": "main",
        "source": "garvis-deploy"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        
        result_data = response.json() if response.content else {}
        
        result = {
            "status": "success",
            "message": "Unity build triggered",
            "response": result_data
        }
        
        if status_reporter:
            status_reporter.report("unity_build", {
                "status": "triggered",
                "message": "Build triggered via n8n"
            })
        
        return result
    except Exception as e:
        result = {
            "status": "warning",
            "message": "Unity build trigger unavailable",
            "note": "Build will trigger automatically when files are pushed to GitHub"
        }
        
        if status_reporter:
            status_reporter.report("unity_build", {
                "status": "warning",
                "error": str(e)
            })
        
        return result

def verify_deployment(commit_sha: Optional[str] = None, status_reporter: Optional[StatusReporter] = None) -> Dict:
    """Verify deployment (build status, levels, n8n)"""
    print_header("POST-DEPLOYMENT VERIFICATION")
    
    tracker = BuildTracker()
    
    # Get commit SHA if not provided
    if not commit_sha:
        commit_sha = tracker.get_latest_commit_sha()
        if not commit_sha:
            return {
                "status": "error",
                "error": "Could not get latest commit SHA"
            }
    
    print_info(f"Verifying deployment for commit: {commit_sha[:8]}")
    
    # Find build
    build = tracker.find_build_for_commit(commit_sha)
    if not build:
        return {
            "status": "pending",
            "message": "Build not found yet (may still be queued)"
        }
    
    print_info(f"Found build: {build['run_id']}")
    
    # Wait for build
    build_result = tracker.wait_for_build_completion(build["run_id"])
    
    # Verify levels
    levels_result = tracker.verify_levels_in_game(LEVEL_FILES)
    
    verification = {
        "commit": commit_sha,
        "build": build_result,
        "levels": levels_result,
        "status": "success" if build_result.get("conclusion") == "success" else "failed"
    }
    
    if status_reporter:
        status_reporter.report("verification", verification)
    
    return verification

def quick_deploy(commit_message: Optional[str] = None, status_reporter: Optional[StatusReporter] = None) -> Dict:
    """Quick deployment: Push website and game levels"""
    print_header("🚀 QUICK DEPLOYMENT")
    
    results = {}
    
    # Deploy website
    print(f"\n{BLUE}📦 WEBSITE{NC}")
    print("-" * 60)
    results["website"] = deploy_website(
        commit_message or "Garvis: Quick deployment",
        status_reporter
    )
    
    # Deploy game levels
    print(f"\n{BLUE}🎮 GAME LEVELS{NC}")
    print("-" * 60)
    results["game"] = deploy_game_levels(
        commit_message or "Garvis: Quick deployment - Book levels",
        status_reporter
    )
    
    # Trigger build if game deployment succeeded
    if results["game"].get("status") == "success":
        print(f"\n{BLUE}🔨 UNITY BUILD{NC}")
        print("-" * 60)
        results["unity_build"] = trigger_unity_build(status_reporter)
    
    return results

def full_deploy(commit_message: Optional[str] = None, status_reporter: Optional[StatusReporter] = None) -> Dict:
    """Full deployment: Push + Build + Verify"""
    print_header("🚀 FULL DEPLOYMENT")
    
    results = {}
    
    # Step 1: Quick deploy
    print(f"\n{BLUE}STEP 1: DEPLOY{NC}")
    print("-" * 60)
    deploy_results = quick_deploy(commit_message, status_reporter)
    results.update(deploy_results)
    
    # Step 2: Verify
    if deploy_results.get("game", {}).get("status") == "success":
        print(f"\n{BLUE}STEP 2: VERIFY{NC}")
        print("-" * 60)
        results["verification"] = verify_deployment(None, status_reporter)
    
    return results

def main():
    """Main deployment function"""
    parser = argparse.ArgumentParser(
        description='Garvis Unified Deployment System',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Quick deployment (push only)
  python scripts/garvis-deploy.py --quick
  
  # Full deployment (push + build + verify)
  python scripts/garvis-deploy.py --full
  
  # Verify existing deployment
  python scripts/garvis-deploy.py --verify
  
  # Deploy game only
  python scripts/garvis-deploy.py --game
  
  # Deploy website only
  python scripts/garvis-deploy.py --website
  
  # Execute Full Integration (AI-driven updates)
  python scripts/garvis-execute-full-integration.py "Update Book 1"
        """
    )
    
    parser.add_argument('--quick', action='store_true', help='Quick deployment (push only)')
    parser.add_argument('--full', action='store_true', help='Full deployment (push + build + verify)')
    parser.add_argument('--verify', action='store_true', help='Post-deployment verification only')
    parser.add_argument('--game', action='store_true', help='Deploy game levels only')
    parser.add_argument('--website', action='store_true', help='Deploy website only')
    parser.add_argument('--message', type=str, help='Custom commit message')
    parser.add_argument('--commit', type=str, help='Commit SHA for verification (--verify mode)')
    
    args = parser.parse_args()
    
    # Initialize status reporter
    status_reporter = StatusReporter()
    
    # Determine mode
    if args.verify:
        results = verify_deployment(args.commit, status_reporter)
    elif args.game:
        results = {"game": deploy_game_levels(args.message, status_reporter)}
    elif args.website:
        results = {"website": deploy_website(args.message, status_reporter)}
    elif args.full:
        results = full_deploy(args.message, status_reporter)
    else:
        # Default to quick
        results = quick_deploy(args.message, status_reporter)
    
    # Print summary
    print_header("📊 DEPLOYMENT SUMMARY")
    
    for component, result in results.items():
        status = result.get("status", "unknown")
        if status == "success":
            print_success(f"{component.title()}: {result.get('message', 'Success')}")
        elif status == "skipped":
            print_info(f"{component.title()}: {result.get('message', 'Skipped')}")
        elif status == "error":
            print_error(f"{component.title()}: {result.get('error', 'Failed')}")
        else:
            print_warning(f"{component.title()}: {status}")
    
    # Show overall status
    overall_status = status_reporter.get_status().get("overall", "unknown")
    print()
    print_info(f"Overall Status: {overall_status}")
    print_info(f"Status File: {status_reporter.status_file}")
    print()

if __name__ == "__main__":
    main()

