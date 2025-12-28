"""
Garvis Build Tracker Module
Unified build monitoring and status tracking with caching

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import time
import json
import subprocess
from typing import Dict, Optional
from datetime import datetime, timedelta

# Configuration
GAME_REPO = "rashadwest/BTEBallCODE"
WORKFLOW_FILE = "unity-webgl-build.yml"
MAX_WAIT_TIME = 1800  # 30 minutes
CHECK_INTERVAL = 30  # Check every 30 seconds
CACHE_TTL = 60  # Cache for 60 seconds

class BuildTracker:
    """Unified build tracking with caching"""
    
    def __init__(self, cache_ttl: int = CACHE_TTL):
        self.cache = {}
        self.cache_ttl = cache_ttl
        self.repo = GAME_REPO
        self.workflow = WORKFLOW_FILE
    
    def _get_cached(self, key: str) -> Optional[Dict]:
        """Get cached value if not expired"""
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.cache_ttl:
                return value
            else:
                del self.cache[key]
        return None
    
    def _set_cache(self, key: str, value: Dict):
        """Cache value with timestamp"""
        self.cache[key] = (value, time.time())
    
    def get_latest_commit_sha(self) -> Optional[str]:
        """Get latest commit SHA from Unity repo"""
        cache_key = "latest_commit"
        cached = self._get_cached(cache_key)
        if cached:
            return cached.get("sha")
        
        try:
            result = subprocess.run(
                ["gh", "api", f"repos/{self.repo}/commits/main", "--jq", ".sha"],
                capture_output=True,
                text=True,
                check=True,
                timeout=10
            )
            sha = result.stdout.strip()
            self._set_cache(cache_key, {"sha": sha})
            return sha
        except Exception:
            return None
    
    def find_build_for_commit(self, commit_sha: str) -> Optional[Dict]:
        """Find GitHub Actions run for a specific commit"""
        cache_key = f"build_{commit_sha}"
        cached = self._get_cached(cache_key)
        if cached:
            return cached
        
        try:
            result = subprocess.run(
                ["gh", "run", "list", "--repo", self.repo, "--workflow", self.workflow,
                 "--json", "databaseId,status,conclusion,headSha,createdAt,updatedAt,displayTitle"],
                capture_output=True,
                text=True,
                check=True,
                timeout=10
            )
            runs = json.loads(result.stdout)
            
            # Find run matching commit SHA
            for run in runs:
                if run.get("headSha", "").startswith(commit_sha) or commit_sha.startswith(run.get("headSha", "")):
                    build_info = {
                        "run_id": str(run["databaseId"]),
                        "status": run.get("status", "unknown"),
                        "conclusion": run.get("conclusion"),
                        "created_at": run.get("createdAt"),
                        "updated_at": run.get("updatedAt"),
                        "title": run.get("displayTitle", "")
                    }
                    self._set_cache(cache_key, build_info)
                    return build_info
            
            return None
        except Exception:
            return None
    
    def get_build_status(self, run_id: str) -> Dict:
        """Get current build status for a run ID"""
        cache_key = f"status_{run_id}"
        cached = self._get_cached(cache_key)
        if cached:
            return cached
        
        try:
            result = subprocess.run(
                ["gh", "run", "view", run_id, "--repo", self.repo, "--json", 
                 "status,conclusion,createdAt,updatedAt,displayTitle"],
                capture_output=True,
                text=True,
                check=True,
                timeout=10
            )
            run_data = json.loads(result.stdout)
            status = {
                "status": run_data.get("status", "unknown"),
                "conclusion": run_data.get("conclusion"),
                "created_at": run_data.get("createdAt"),
                "updated_at": run_data.get("updatedAt"),
                "title": run_data.get("displayTitle", "")
            }
            self._set_cache(cache_key, status)
            return status
        except Exception:
            return {"status": "unknown", "conclusion": None}
    
    def wait_for_build_completion(self, run_id: str, timeout: int = MAX_WAIT_TIME) -> Dict:
        """Wait for build to complete, checking every CHECK_INTERVAL seconds"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            status = self.get_build_status(run_id)
            
            if status["status"] == "completed":
                return {
                    "status": "completed",
                    "conclusion": status.get("conclusion"),
                    "run_id": run_id,
                    "wait_time": int(time.time() - start_time)
                }
            
            if status["status"] == "in_progress" or status["status"] == "queued":
                time.sleep(CHECK_INTERVAL)
                continue
            
            # Unknown or failed status
            return {
                "status": status["status"],
                "conclusion": status.get("conclusion"),
                "run_id": run_id,
                "wait_time": int(time.time() - start_time)
            }
        
        # Timeout
        return {
            "status": "timeout",
            "conclusion": None,
            "run_id": run_id,
            "wait_time": timeout
        }
    
    def verify_levels_in_game(self, level_files: list) -> Dict:
        """Verify level files exist in game repository"""
        results = {"verified": [], "missing": []}
        
        for level_file in level_files:
            try:
                result = subprocess.run(
                    ["gh", "api", f"repos/{self.repo}/contents/Assets/StreamingAssets/Levels/{level_file}"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if result.returncode == 0:
                    results["verified"].append(level_file)
                else:
                    results["missing"].append(level_file)
            except Exception:
                results["missing"].append(level_file)
        
        return results


