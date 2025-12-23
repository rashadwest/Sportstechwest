#!/usr/bin/env python3
"""
Push Game Levels to Unity Repository
Uses GitHub API if token available, otherwise provides instructions
"""

import sys
import json
import base64
import requests
from pathlib import Path

# Level files to push
LEVELS_PATH = Path("/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels")
REPO = "rashadwest/BTEBallCODE"
BASE_PATH = "Assets/StreamingAssets/Levels"

LEVEL_FILES = [
    "book1_foundation_block.json",
    "book2_decision_crossover.json",
    "book3_pattern_loop.json"
]

def push_via_github_api(github_token):
    """Push levels via GitHub API"""
    print("🚀 Pushing game levels via GitHub API...")
    print(f"   Repository: {REPO}")
    print(f"   Path: {BASE_PATH}")
    print()
    
    results = []
    
    for level_file in LEVEL_FILES:
        source = LEVELS_PATH / level_file
        if not source.exists():
            print(f"❌ {level_file} not found")
            continue
        
        content = source.read_text()
        content_b64 = base64.b64encode(content.encode()).decode()
        
        url = f"https://api.github.com/repos/{REPO}/contents/{BASE_PATH}/{level_file}"
        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        # Check if file exists
        check = requests.get(url, headers=headers)
        
        data = {
            "message": f"Add {level_file} with curriculum (Garvis)",
            "content": content_b64,
            "branch": "main"
        }
        
        if check.status_code == 200:
            existing = check.json()
            data["sha"] = existing["sha"]
            print(f"📝 Updating {level_file}...")
        else:
            print(f"➕ Creating {level_file}...")
        
        response = requests.put(url, headers=headers, json=data)
        
        if response.status_code in [200, 201]:
            print(f"   ✅ {level_file} pushed successfully")
            results.append({"file": level_file, "status": "success"})
        else:
            print(f"   ❌ {level_file} failed: {response.status_code}")
            print(f"      {response.text[:200]}")
            results.append({"file": level_file, "status": "error", "error": response.text})
    
    return results

def main():
    """Main function"""
    print("=" * 60)
    print("🎮 Push Game Levels to Unity Repository")
    print("=" * 60)
    print()
    
    # Check for GitHub token
    import os
    github_token = os.getenv("GITHUB_TOKEN") or os.getenv("GITHUB_PAT")
    
    if github_token:
        # Push via API
        results = push_via_github_api(github_token)
        print()
        print("=" * 60)
        print("✅ Level push complete!")
        print("   GitHub Actions will auto-build and deploy to Netlify")
        print()
        print("Results:")
        for result in results:
            status_emoji = "✅" if result["status"] == "success" else "❌"
            print(f"   {status_emoji} {result['file']}: {result['status']}")
    else:
        # Provide instructions
        print("⚠️  GitHub token not found in environment")
        print()
        print("OPTION 1: Set GitHub Token (Recommended)")
        print("   export GITHUB_TOKEN='your_token_here'")
        print("   python scripts/push-game-levels.py")
        print()
        print("OPTION 2: Push via GitHub UI (Easiest)")
        print("   1. Go to: https://github.com/rashadwest/BTEBallCODE")
        print(f"   2. Navigate to: {BASE_PATH}/ (create folder if needed)")
        print("   3. Click: 'Add file' → 'Upload files'")
        print("   4. Upload these files:")
        for level_file in LEVEL_FILES:
            source = LEVELS_PATH / level_file
            if source.exists():
                print(f"      - {level_file} ({source.stat().st_size} bytes)")
        print("   5. Commit message: 'Add Book 1, 2, 3 levels with curriculum (Garvis)'")
        print("   6. Click: 'Commit changes'")
        print()
        print("OPTION 3: Use Garvis Command")
        print("   python scripts/garvis-command.py \\")
        print("     --one-thing 'Push game levels' \\")
        print("     --tasks 'Push levels to GitHub, Trigger Unity build'")
        print()
        print("=" * 60)

if __name__ == "__main__":
    main()

