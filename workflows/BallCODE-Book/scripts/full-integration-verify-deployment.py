#!/usr/bin/env python3
"""
Full Integration: Deployment Status Verification
Verifies that deployments succeeded after Full Integration execution.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))
from modules.build_tracker import BuildTracker
from modules.status_reporter import StatusReporter

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent

def verify_deployment_status(verification_data_json: str) -> dict:
    """Verify deployment status for website, game, and curriculum."""
    try:
        # Parse verification data
        if isinstance(verification_data_json, str):
            try:
                verification_data = json.loads(verification_data_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', verification_data_json)
                if json_match:
                    verification_data = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            verification_data = verification_data_json
        
        results = {
            "status": "success",
            "website_deployment": {},
            "game_deployment": {},
            "curriculum_update": {},
            "errors": []
        }
        
        # Initialize trackers
        build_tracker = BuildTracker()
        status_reporter = StatusReporter()
        
        # Verify website deployment (if website updates were made)
        if verification_data.get("website_updated", False):
            try:
                # Check Netlify deployment status
                # Use garvis-deploy.py status or check directly
                netlify_status = check_netlify_deployment()
                results["website_deployment"] = {
                    "status": netlify_status.get("status", "unknown"),
                    "url": netlify_status.get("url", ""),
                    "deployed_at": netlify_status.get("deployed_at", "")
                }
            except Exception as e:
                results["errors"].append(f"Website deployment verification failed: {str(e)}")
                results["website_deployment"] = {"status": "error", "error": str(e)}
        
        # Verify game deployment (if game updates were made)
        if verification_data.get("game_updated", False):
            try:
                # Check GitHub Actions build status
                build_status = build_tracker.get_latest_build_status()
                results["game_deployment"] = {
                    "status": build_status.get("status", "unknown"),
                    "build_id": build_status.get("id", ""),
                    "completed_at": build_status.get("completed_at", ""),
                    "netlify_url": build_status.get("netlify_url", "")
                }
            except Exception as e:
                results["errors"].append(f"Game deployment verification failed: {str(e)}")
                results["game_deployment"] = {"status": "error", "error": str(e)}
        
        # Verify curriculum update (if curriculum updates were made)
        if verification_data.get("curriculum_updated", False):
            try:
                # Check if schema file was updated
                schema_path = PROJECT_ROOT / "CURRICULUM-DATA-EXAMPLE.json"
                if schema_path.exists():
                    stat = schema_path.stat()
                    results["curriculum_update"] = {
                        "status": "success",
                        "file_exists": True,
                        "last_modified": time.ctime(stat.st_mtime),
                        "file_size": stat.st_size
                    }
                else:
                    results["curriculum_update"] = {
                        "status": "error",
                        "file_exists": False
                    }
            except Exception as e:
                results["errors"].append(f"Curriculum update verification failed: {str(e)}")
                results["curriculum_update"] = {"status": "error", "error": str(e)}
        
        # Determine overall status
        all_success = (
            results["website_deployment"].get("status") in ["success", "deployed", None] or not verification_data.get("website_updated", False)
        ) and (
            results["game_deployment"].get("status") in ["success", "completed", None] or not verification_data.get("game_updated", False)
        ) and (
            results["curriculum_update"].get("status") in ["success", None] or not verification_data.get("curriculum_updated", False)
        )
        
        if results["errors"]:
            results["status"] = "partial" if all_success else "error"
        else:
            results["status"] = "success" if all_success else "partial"
        
        results["summary"] = {
            "website_verified": bool(results["website_deployment"].get("status")),
            "game_verified": bool(results["game_deployment"].get("status")),
            "curriculum_verified": bool(results["curriculum_update"].get("status")),
            "errors_count": len(results["errors"])
        }
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "website_deployment": {},
            "game_deployment": {},
            "curriculum_update": {},
            "errors": [str(e)]
        }

def check_netlify_deployment() -> dict:
    """Check Netlify deployment status."""
    # Try to get status from garvis-deploy.py or check directly
    # For now, return placeholder - can be enhanced with Netlify API
    return {
        "status": "unknown",
        "url": "https://ballcode.co",
        "deployed_at": ""
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
    
    result = verify_deployment_status(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)

