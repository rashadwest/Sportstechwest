#!/usr/bin/env python3
"""
Push Book Menu Scripts to Unity Repository
Copies scripts from Unity-Scripts/ to BTEBallCODE repository via GitHub API
"""

import sys
import json
import base64
import subprocess
from pathlib import Path

REPO = "rashadwest/BTEBallCODE"
SCRIPTS_TO_PUSH = [
    {
        "local_path": "Unity-Scripts/GameModeButton.cs",
        "repo_path": "Assets/Scripts/GameModeButton.cs",
        "message": "Update GameModeButton: Add Book mode support"
    },
    {
        "local_path": "Unity-Scripts/BookMenuManager.cs",
        "repo_path": "Assets/Scripts/BookMenuManager.cs",
        "message": "Add BookMenuManager: Book 1-3 selection UI"
    },
    {
        "local_path": "Unity-Scripts/Editor/BookMenuSetupHelper.cs",
        "repo_path": "Assets/Editor/BookMenuSetupHelper.cs",
        "message": "Add BookMenuSetupHelper: Auto-setup editor script"
    },
    {
        "local_path": "Unity-Scripts/Editor/BookButtonSetupHelper.cs",
        "repo_path": "Assets/Editor/BookButtonSetupHelper.cs",
        "message": "Add BookButtonSetupHelper: Auto-add Book button editor script"
    }
]

def push_file_via_github_api(local_path, repo_path, message):
    """Push a file to GitHub repository via API"""
    source = Path(local_path)
    if not source.exists():
        print(f"❌ {local_path} not found")
        return False
    
    content = source.read_text()
    content_b64 = base64.b64encode(content.encode()).decode()
    
    url = f"repos/{REPO}/contents/{repo_path}"
    
    # Check if file exists
    check_result = subprocess.run(
        ["gh", "api", url],
        capture_output=True,
        text=True
    )
    
    data = {
        "message": message,
        "content": content_b64,
        "branch": "main"
    }
    
    if check_result.returncode == 0:
        # File exists, get SHA
        existing = json.loads(check_result.stdout)
        data["sha"] = existing["sha"]
        print(f"📝 Updating {repo_path}...")
    else:
        print(f"➕ Creating {repo_path}...")
    
    # Push file
    result = subprocess.run(
        ["gh", "api", f"{url}", "--method", "PUT", "--input", "-"],
        input=json.dumps(data),
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"   ✅ {repo_path} pushed successfully")
        return True
    else:
        print(f"   ❌ {repo_path} failed:")
        print(f"      {result.stderr[:200]}")
        return False

def main():
    """Main function"""
    print("=" * 60)
    print("🚀 Pushing Book Menu Scripts to Unity Repository")
    print("=" * 60)
    print()
    print(f"Repository: {REPO}")
    print()
    
    results = []
    for script in SCRIPTS_TO_PUSH:
        success = push_file_via_github_api(
            script["local_path"],
            script["repo_path"],
            script["message"]
        )
        results.append({
            "file": script["repo_path"],
            "success": success
        })
        print()
    
    print("=" * 60)
    print("✅ Script push complete!")
    print()
    print("Results:")
    for result in results:
        status_emoji = "✅" if result["success"] else "❌"
        print(f"   {status_emoji} {result['file']}")
    print()
    print("Next: GitHub Actions will auto-build Unity project")
    print("      Then deploy to Netlify (ballcode.netlify.app)")

if __name__ == "__main__":
    main()


