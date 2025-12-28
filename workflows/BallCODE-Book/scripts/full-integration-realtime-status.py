#!/usr/bin/env python3
"""
Full Integration: Real-time Status Updates
Provides real-time status updates via WebSocket or polling.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent

def get_realtime_status(session_id: str) -> dict:
    """Get real-time status for a session."""
    try:
        results = {
            "status": "success",
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "current_step": "",
            "progress": 0,
            "status_message": "",
            "errors": []
        }
        
        # Load status from garvis_status.json
        status_file = PROJECT_ROOT / "garvis_status.json"
        if status_file.exists():
            with open(status_file, 'r', encoding='utf-8') as f:
                status_data = json.load(f)
            
            # Find session status
            session_status = status_data.get("sessions", {}).get(session_id, {})
            
            if session_status:
                results["current_step"] = session_status.get("current_step", "")
                results["progress"] = session_status.get("progress", 0)
                results["status_message"] = session_status.get("status_message", "")
                results["last_updated"] = session_status.get("last_updated", "")
            else:
                results["status_message"] = "Session not found"
        else:
            results["status_message"] = "Status file not found"
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "errors": [str(e)]
        }

def update_realtime_status(session_id: str, status_data_json: str) -> dict:
    """Update real-time status for a session."""
    try:
        # Parse status data
        if isinstance(status_data_json, str):
            try:
                status_data = json.loads(status_data_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', status_data_json)
                if json_match:
                    status_data = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            status_data = status_data_json
        
        # Load existing status
        status_file = PROJECT_ROOT / "garvis_status.json"
        if status_file.exists():
            with open(status_file, 'r', encoding='utf-8') as f:
                all_status = json.load(f)
        else:
            all_status = {"sessions": {}}
        
        # Update session status
        if "sessions" not in all_status:
            all_status["sessions"] = {}
        
        all_status["sessions"][session_id] = {
            "current_step": status_data.get("current_step", ""),
            "progress": status_data.get("progress", 0),
            "status_message": status_data.get("status_message", ""),
            "last_updated": datetime.now().isoformat()
        }
        
        # Save updated status
        status_file.write_text(json.dumps(all_status, indent=2), encoding='utf-8')
        
        return {
            "status": "success",
            "session_id": session_id,
            "updated": True
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "updated": False,
            "errors": [str(e)]
        }

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Real-time Status Updates")
    parser.add_argument("--get", help="Get status for session ID")
    parser.add_argument("--update", help="Update status for session ID")
    parser.add_argument("--data", help="Status data (JSON)")
    
    args = parser.parse_args()
    
    if args.get:
        result = get_realtime_status(args.get)
        print(json.dumps(result, indent=2))
    
    elif args.update:
        if not args.data:
            print(json.dumps({"status": "error", "error": "Status data required for update"}, indent=2))
            sys.exit(1)
        
        result = update_realtime_status(args.update, args.data)
        print(json.dumps(result, indent=2))
    
    else:
        print("Usage: --get <session_id> or --update <session_id> --data <json>")
        sys.exit(1)
    
    if result.get("status") == "error":
        sys.exit(1)


