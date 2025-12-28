#!/usr/bin/env python3
"""
Full Integration: Apply Game Updates
Takes AI-generated game updates and applies them to the Unity game system.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Optional

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))
from modules.unity_pusher import UnityPusher

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
UNITY_LEVELS_DIR = PROJECT_ROOT / "Unity-Scripts" / "Levels"
UNITY_SCRIPTS_DIR = PROJECT_ROOT / "Unity-Scripts"

def apply_game_updates(game_updates_json: str) -> dict:
    """Apply game updates from AI generation."""
    try:
        # Parse AI-generated JSON
        # Handle both direct JSON or wrapped in choices/message format
        if isinstance(game_updates_json, str):
            try:
                updates = json.loads(game_updates_json)
            except json.JSONDecodeError:
                # Try to extract JSON from markdown or text
                import re
                json_match = re.search(r'\{[\s\S]*\}', game_updates_json)
                if json_match:
                    updates = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            updates = game_updates_json
        
        # Extract updates
        unity_scripts = updates.get('unityScripts', [])
        level_files = updates.get('levelFiles', [])
        exercise_config = updates.get('exerciseConfig', {})
        integration_data = updates.get('integrationData', {})
        
        results = {
            "status": "success",
            "files_updated": [],
            "files_pushed": [],
            "errors": [],
            "exercise_config": exercise_config,
            "integration_data": integration_data
        }
        
        # Apply Unity C# scripts
        for script in unity_scripts:
            try:
                file_name = script.get('file', '')
                code = script.get('code', '')
                
                if not file_name or not code:
                    results["errors"].append(f"Invalid script data: missing file or code")
                    continue
                
                # Ensure .cs extension
                if not file_name.endswith('.cs'):
                    file_name += '.cs'
                
                file_path = UNITY_SCRIPTS_DIR / file_name
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text(code, encoding='utf-8')
                
                results["files_updated"].append(str(file_path))
            except Exception as e:
                results["errors"].append(f"Error applying script {script.get('file', 'unknown')}: {str(e)}")
        
        # Apply level JSON files
        pusher = UnityPusher()
        for level in level_files:
            try:
                file_name = level.get('file', '')
                level_json = level.get('json', {})
                
                if not file_name or not level_json:
                    results["errors"].append(f"Invalid level data: missing file or json")
                    continue
                
                # Ensure .json extension
                if not file_name.endswith('.json'):
                    file_name += '.json'
                
                # Save locally first
                local_path = UNITY_LEVELS_DIR / file_name
                local_path.parent.mkdir(parents=True, exist_ok=True)
                local_path.write_text(json.dumps(level_json, indent=2), encoding='utf-8')
                
                results["files_updated"].append(str(local_path))
                
                # Push to Unity repository
                repo_path = f"Assets/StreamingAssets/Levels/{file_name}"
                push_result = pusher.push_file(
                    local_path=local_path,
                    repo_path=repo_path,
                    message=f"Full Integration: Add/update level {file_name}"
                )
                
                if push_result.get('success'):
                    results["files_pushed"].append(repo_path)
                else:
                    results["errors"].append(f"Failed to push {file_name}: {push_result.get('error', 'Unknown error')}")
                    
            except Exception as e:
                results["errors"].append(f"Error applying level {level.get('file', 'unknown')}: {str(e)}")
        
        # Determine overall status
        if results["errors"]:
            results["status"] = "partial" if results["files_updated"] else "error"
        else:
            results["status"] = "success"
        
        results["summary"] = {
            "scripts_applied": len(unity_scripts),
            "levels_applied": len(level_files),
            "files_updated_count": len(results["files_updated"]),
            "files_pushed_count": len(results["files_pushed"]),
            "errors_count": len(results["errors"])
        }
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "files_updated": [],
            "files_pushed": [],
            "errors": [str(e)]
        }

if __name__ == "__main__":
    # Read from stdin or file argument
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        if input_path.exists():
            input_json = input_path.read_text(encoding='utf-8')
        else:
            input_json = sys.argv[1]  # Treat as JSON string
    else:
        input_json = sys.stdin.read()
    
    result = apply_game_updates(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)


