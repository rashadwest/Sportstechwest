#!/usr/bin/env python3
"""
Garvis Push - One-Command Deployment System
Push everything with a single prompt

Usage:
    python scripts/garvis-push.py
    python scripts/garvis-push.py --website
    python scripts/garvis-push.py --game
    python scripts/garvis-push.py --all
"""

import sys
import subprocess
import json
from pathlib import Path
from typing import List, Dict, Optional

# Colors for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

# Paths
WEBSITE_PATH = Path("/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode")
GAME_LEVELS_PATH = Path("/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels")
UNITY_REPO_PATH = Path("/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts")

# Repositories
WEBSITE_REPO = "rashadwest/BallCode"
GAME_REPO = "rashadwest/BTEBallCODE"

# Level files to push
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

def check_git_status(repo_path: Path) -> Dict:
    """Check git status and return changes"""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )
        return {
            'has_changes': bool(result.stdout.strip()),
            'changes': result.stdout.strip()
        }
    except Exception as e:
        return {'error': str(e)}

def push_website(commit_message: str = "Garvis: Deploy website updates") -> Dict:
    """Push website to GitHub"""
    print_info("Checking website for changes...")
    
    status = check_git_status(WEBSITE_PATH)
    if status.get('error'):
        return {'status': 'error', 'error': status['error']}
    
    if not status.get('has_changes'):
        return {'status': 'skipped', 'message': 'No changes to commit'}
    
    try:
        # Add all changes
        subprocess.run(
            ["git", "add", "-A"],
            cwd=WEBSITE_PATH,
            check=True
        )
        
        # Commit
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            cwd=WEBSITE_PATH,
            check=True
        )
        
        # Push
        push_result = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=WEBSITE_PATH,
            capture_output=True,
            text=True
        )
        
        if push_result.returncode == 0:
            print_success(f"Website pushed to {WEBSITE_REPO}")
            return {
                'status': 'success',
                'message': f'Pushed to {WEBSITE_REPO}',
                'output': push_result.stdout
            }
        else:
            print_error(f"Website push failed: {push_result.stderr}")
            return {'status': 'error', 'error': push_result.stderr}
    except subprocess.CalledProcessError as e:
        print_error(f"Website push error: {str(e)}")
        return {'status': 'error', 'error': str(e)}

def push_game_levels(commit_message: str = "Garvis: Add Book 1, 2, 3 levels with curriculum") -> Dict:
    """Push game levels to Unity repository"""
    print_info("Checking game levels...")
    
    # Check if Unity repo is cloned locally
    if not (UNITY_REPO_PATH / ".git").exists():
        print_warning("Unity repository not found locally")
        print_info("Game levels need to be pushed via GitHub UI")
        print_info(f"Files to upload: {', '.join(LEVEL_FILES)}")
        return {
            'status': 'manual_required',
            'message': 'Unity repo not found locally - use GitHub UI',
            'files': LEVEL_FILES,
            'instructions': f'Upload to: {GAME_REPO}/Assets/StreamingAssets/Levels/'
        }
    
    # Check if level files exist
    missing_files = []
    for level_file in LEVEL_FILES:
        if not (GAME_LEVELS_PATH / level_file).exists():
            missing_files.append(level_file)
    
    if missing_files:
        return {
            'status': 'error',
            'error': f'Missing level files: {", ".join(missing_files)}'
        }
    
    # Copy level files to Unity repo
    target_path = UNITY_REPO_PATH / "Assets" / "StreamingAssets" / "Levels"
    target_path.mkdir(parents=True, exist_ok=True)
    
    copied_files = []
    for level_file in LEVEL_FILES:
        source = GAME_LEVELS_PATH / level_file
        if source.exists():
            import shutil
            shutil.copy(source, target_path / level_file)
            copied_files.append(level_file)
    
    if not copied_files:
        return {'status': 'error', 'error': 'No level files to copy'}
    
    # Check for changes
    status = check_git_status(UNITY_REPO_PATH)
    if not status.get('has_changes'):
        return {'status': 'skipped', 'message': 'No changes to commit'}
    
    try:
        # Add changes
        subprocess.run(
            ["git", "add", "-A"],
            cwd=UNITY_REPO_PATH,
            check=True
        )
        
        # Commit
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            cwd=UNITY_REPO_PATH,
            check=True
        )
        
        # Push
        push_result = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=UNITY_REPO_PATH,
            capture_output=True,
            text=True
        )
        
        if push_result.returncode == 0:
            print_success(f"Game levels pushed to {GAME_REPO}")
            return {
                'status': 'success',
                'message': f'Pushed levels to {GAME_REPO}',
                'files': copied_files
            }
        else:
            print_error(f"Game levels push failed: {push_result.stderr}")
            return {'status': 'error', 'error': push_result.stderr}
    except subprocess.CalledProcessError as e:
        print_error(f"Game levels push error: {str(e)}")
        return {'status': 'error', 'error': str(e)}

def trigger_unity_build() -> Dict:
    """Trigger Unity build via n8n webhook"""
    import requests
    import os
    
    n8n_url = os.getenv("N8N_BASE_URL", "http://192.168.1.226:5678")
    url = f"{n8n_url}/webhook/unity-build"
    
    payload = {
        "request": "Build with Book 1, 2, 3 levels",
        "branch": "main",
        "source": "garvis-push"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        
        result = response.json() if response.content else {}
        if result.get('status') == 'skipped':
            print_warning(f"Unity build skipped: {result.get('message', 'Build locked')}")
        else:
            print_success("Unity build triggered")
        
        return {
            'status': 'success',
            'message': 'Unity build triggered',
            'response': result
        }
    except requests.exceptions.RequestException as e:
        print_warning(f"Unity build trigger failed: {str(e)}")
        return {
            'status': 'warning',
            'message': 'Unity build trigger unavailable',
            'note': 'Build will trigger automatically when levels are pushed to GitHub'
        }

def main():
    """Main deployment function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Garvis Push - One-Command Deployment')
    parser.add_argument('--website', action='store_true', help='Push website only')
    parser.add_argument('--game', action='store_true', help='Push game levels only')
    parser.add_argument('--all', action='store_true', help='Push everything (default)')
    parser.add_argument('--message', type=str, help='Custom commit message')
    
    args = parser.parse_args()
    
    # Default to --all if no specific option
    if not (args.website or args.game):
        args.all = True
    
    print_header("🚀 Garvis Push - One-Command Deployment")
    
    results = {}
    
    # Push website
    if args.all or args.website:
        print(f"\n{BLUE}📦 WEBSITE DEPLOYMENT{NC}")
        print("-" * 60)
        website_result = push_website(
            args.message or "Garvis: Deploy website updates"
        )
        results['website'] = website_result
        print()
    
    # Push game levels
    if args.all or args.game:
        print(f"\n{BLUE}🎮 GAME DEPLOYMENT{NC}")
        print("-" * 60)
        game_result = push_game_levels(
            args.message or "Garvis: Add Book 1, 2, 3 levels with curriculum"
        )
        results['game'] = game_result
        
        # If manual required, show instructions
        if game_result.get('status') == 'manual_required':
            print()
            print_warning("Manual push required via GitHub UI:")
            print_info(f"1. Go to: https://github.com/{GAME_REPO}")
            print_info(f"2. Navigate to: Assets/StreamingAssets/Levels/")
            print_info("3. Upload these files:")
            for level_file in game_result.get('files', []):
                source = GAME_LEVELS_PATH / level_file
                if source.exists():
                    size = source.stat().st_size
                    print_info(f"   - {level_file} ({size} bytes)")
            print_info(f"4. Commit message: {args.message or 'Add Book 1, 2, 3 levels with curriculum'}")
        
        # Trigger Unity build if levels were pushed successfully
        if game_result.get('status') == 'success':
            print()
            print_info("Triggering Unity build...")
            build_result = trigger_unity_build()
            results['unity_build'] = build_result
        
        print()
    
    # Summary
    print_header("📊 DEPLOYMENT SUMMARY")
    
    if 'website' in results:
        status = results['website'].get('status', 'unknown')
        if status == 'success':
            print_success(f"Website: {results['website'].get('message', 'Pushed')}")
        elif status == 'skipped':
            print_info(f"Website: {results['website'].get('message', 'No changes')}")
        else:
            print_error(f"Website: {results['website'].get('error', 'Failed')}")
    
    if 'game' in results:
        status = results['game'].get('status', 'unknown')
        if status == 'success':
            print_success(f"Game: {results['game'].get('message', 'Pushed')}")
            if 'files' in results['game']:
                print_info(f"   Files: {', '.join(results['game']['files'])}")
        elif status == 'manual_required':
            print_warning("Game: Manual push required (see instructions above)")
        elif status == 'skipped':
            print_info(f"Game: {results['game'].get('message', 'No changes')}")
        else:
            print_error(f"Game: {results['game'].get('error', 'Failed')}")
    
    if 'unity_build' in results:
        status = results['unity_build'].get('status', 'unknown')
        if status == 'success':
            print_success("Unity Build: Triggered")
        else:
            print_warning(f"Unity Build: {results['unity_build'].get('message', 'Unavailable')}")
    
    print()
    print_info("Next steps:")
    print_info("1. Check Netlify dashboard for deployments")
    print_info("2. Verify website is updated")
    print_info("3. Verify game has new levels")
    print()

if __name__ == "__main__":
    main()

