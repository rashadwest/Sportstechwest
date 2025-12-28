#!/usr/bin/env python3
"""
Push UI/UX Improvement Scripts to Unity Repository
Copies UI/UX scripts from Unity-Scripts/ to BTEBallCODE repository via GitHub API
"""

import sys
import json
import base64
import subprocess
from pathlib import Path

REPO = "rashadwest/BTEBallCODE"
SCRIPTS_TO_PUSH = [
    {
        "local_path": "Unity-Scripts/ImprovedButton.cs",
        "repo_path": "Assets/Scripts/ImprovedButton.cs",
        "message": "Add ImprovedButton: Enhanced button component with selection states, glow effects, and animations"
    },
    {
        "local_path": "Unity-Scripts/GameModeButton.cs",
        "repo_path": "Assets/Scripts/GameModeButton.cs",
        "message": "Update GameModeButton: Card-style game mode buttons with selection states"
    },
    {
        "local_path": "Unity-Scripts/MainActionButton.cs",
        "repo_path": "Assets/Scripts/MainActionButton.cs",
        "message": "Add MainActionButton: Enhanced BallCode and Skins buttons with pulsing animation"
    },
    {
        "local_path": "Unity-Scripts/ExitButton.cs",
        "repo_path": "Assets/Scripts/ExitButton.cs",
        "message": "Add ExitButton: Larger, more visible exit button with orange hover"
    },
    {
        "local_path": "Unity-Scripts/FeatureButton.cs",
        "repo_path": "Assets/Scripts/FeatureButton.cs",
        "message": "Add FeatureButton: Card-style Leaderboard and Settings buttons"
    },
    {
        "local_path": "Unity-Scripts/Editor/UIUXButtonSetupHelper.cs",
        "repo_path": "Assets/Editor/UIUXButtonSetupHelper.cs",
        "message": "Add UIUXButtonSetupHelper: Auto-apply UI/UX improvements to buttons"
    },
    {
        "local_path": "Unity-Scripts/BookMenuManager.cs",
        "repo_path": "Assets/Scripts/BookMenuManager.cs",
        "message": "Fix BookMenuManager: Add TMPro support, fix GameModeManager/LevelDataManager references with reflection"
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
    print("🎨 Pushing UI/UX Improvement Scripts to Unity Repository")
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
    print("✅ UI/UX script push complete!")
    print()
    print("Results:")
    for result in results:
        status_emoji = "✅" if result["success"] else "❌"
        print(f"   {status_emoji} {result['file']}")
    print()
    print("⚠️  IMPORTANT: Scripts are pushed, but UI won't change until:")
    print("   1. Components are applied to buttons in Unity Editor")
    print("   2. Button GameObjects are configured with new components")
    print("   3. Unity project is built and deployed")
    print()
    print("Next Steps:")
    print("   - Open Unity project")
    print("   - Apply ImprovedButton/GameModeButton/MainActionButton to buttons")
    print("   - Configure button settings")
    print("   - Build and deploy")

if __name__ == "__main__":
    main()

