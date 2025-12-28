#!/usr/bin/env python3
"""
Full Integration: File Update Verification
Verifies that files were actually updated after Full Integration execution.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent

def verify_file_updates(verification_data_json: str) -> dict:
    """Verify that files were actually updated."""
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
            "files_verified": [],
            "files_missing": [],
            "files_changed": [],
            "files_unchanged": [],
            "errors": []
        }
        
        # Get files to verify
        files_to_verify = verification_data.get('files', [])
        expected_content = verification_data.get('expected_content', {})
        before_state = verification_data.get('before_state', {})
        
        for file_path_str in files_to_verify:
            try:
                file_path = PROJECT_ROOT / file_path_str
                
                # Check if file exists
                if not file_path.exists():
                    results["files_missing"].append(file_path_str)
                    continue
                
                # Get file stats
                stat = file_path.stat()
                file_size = stat.st_size
                file_mtime = datetime.fromtimestamp(stat.st_mtime)
                
                # Check if file was modified (if before_state provided)
                if file_path_str in before_state:
                    before_mtime = datetime.fromtimestamp(before_state[file_path_str].get('mtime', 0))
                    if file_mtime > before_mtime:
                        results["files_changed"].append({
                            "file": file_path_str,
                            "size": file_size,
                            "modified": file_mtime.isoformat()
                        })
                    else:
                        results["files_unchanged"].append(file_path_str)
                else:
                    # Just verify existence
                    results["files_verified"].append({
                        "file": file_path_str,
                        "size": file_size,
                        "exists": True
                    })
                
                # Verify content if expected_content provided
                if file_path_str in expected_content:
                    actual_content = file_path.read_text(encoding='utf-8')
                    expected = expected_content[file_path_str]
                    
                    if isinstance(expected, str):
                        if expected in actual_content:
                            results["files_verified"].append({
                                "file": file_path_str,
                                "content_match": True
                            })
                        else:
                            results["errors"].append(f"Content mismatch in {file_path_str}")
                    elif isinstance(expected, dict):
                        # Check for specific content patterns
                        for key, value in expected.items():
                            if key in actual_content and str(value) in actual_content:
                                continue
                            else:
                                results["errors"].append(f"Content pattern '{key}' not found in {file_path_str}")
                
            except Exception as e:
                results["errors"].append(f"Error verifying {file_path_str}: {str(e)}")
        
        # Determine overall status
        if results["files_missing"] or results["errors"]:
            results["status"] = "error" if not results["files_verified"] else "partial"
        elif results["files_unchanged"]:
            results["status"] = "warning"
        else:
            results["status"] = "success"
        
        results["summary"] = {
            "total_files": len(files_to_verify),
            "verified": len(results["files_verified"]),
            "missing": len(results["files_missing"]),
            "changed": len(results["files_changed"]),
            "unchanged": len(results["files_unchanged"]),
            "errors": len(results["errors"])
        }
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "files_verified": [],
            "files_missing": [],
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
    
    result = verify_file_updates(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)


