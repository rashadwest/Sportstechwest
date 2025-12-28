"""
Garvis Unity Pusher Module
Standardized Unity file pushing via GitHub API

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import base64
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

# Configuration
UNITY_REPO = "rashadwest/BTEBallCODE"

class UnityPusher:
    """Standardized Unity deployment via GitHub API"""
    
    def __init__(self, repo: str = UNITY_REPO):
        self.repo = repo
    
    def push_file(self, local_path: Path, repo_path: str, message: str) -> Dict:
        """Push a single file to Unity repository via GitHub API"""
        if not local_path.exists():
            return {
                "success": False,
                "error": f"File not found: {local_path}"
            }
        
        try:
            # Read file content
            content = local_path.read_text()
            content_b64 = base64.b64encode(content.encode()).decode()
            
            url = f"repos/{self.repo}/contents/{repo_path}"
            
            # Check if file exists
            check_result = subprocess.run(
                ["gh", "api", url],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            data = {
                "message": message,
                "content": content_b64,
                "branch": "main"
            }
            
            if check_result.returncode == 0:
                # File exists, get SHA for update
                existing = json.loads(check_result.stdout)
                data["sha"] = existing["sha"]
                action = "updated"
            else:
                action = "created"
            
            # Push file
            result = subprocess.run(
                ["gh", "api", f"{url}", "--method", "PUT", "--input", "-"],
                input=json.dumps(data),
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                return {
                    "success": True,
                    "action": action,
                    "file": repo_path,
                    "message": f"✅ {repo_path} {action} successfully"
                }
            else:
                return {
                    "success": False,
                    "error": result.stderr[:200] if result.stderr else "Unknown error",
                    "file": repo_path
                }
        
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "API call timeout",
                "file": repo_path
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "file": repo_path
            }
    
    def push_levels(self, level_files: List[str], levels_path: Path, commit_message: str = "Garvis: Add book levels") -> Dict:
        """Push multiple level files to Unity repository"""
        results = {"pushed": [], "failed": []}
        
        for level_file in level_files:
            source = levels_path / level_file
            repo_path = f"Assets/StreamingAssets/Levels/{level_file}"
            message = f"{commit_message} - {level_file}"
            
            result = self.push_file(source, repo_path, message)
            
            if result["success"]:
                results["pushed"].append(level_file)
            else:
                results["failed"].append({
                    "file": level_file,
                    "error": result.get("error", "Unknown error")
                })
        
        return results
    
    def push_scripts(self, script_mappings: List[Dict], base_path: Path) -> Dict:
        """Push multiple script files to Unity repository
        
        script_mappings format:
        [
            {
                "local_path": "Unity-Scripts/GameModeButton.cs",
                "repo_path": "Assets/Scripts/GameModeButton.cs",
                "message": "Update GameModeButton"
            },
            ...
        ]
        """
        results = {"pushed": [], "failed": []}
        
        for mapping in script_mappings:
            local_path = base_path / mapping["local_path"]
            repo_path = mapping["repo_path"]
            message = mapping["message"]
            
            result = self.push_file(local_path, repo_path, message)
            
            if result["success"]:
                results["pushed"].append(repo_path)
            else:
                results["failed"].append({
                    "file": repo_path,
                    "error": result.get("error", "Unknown error")
                })
        
        return results


