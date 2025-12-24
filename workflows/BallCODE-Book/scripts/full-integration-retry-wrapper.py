#!/usr/bin/env python3
"""
Full Integration: Retry Wrapper
Wraps script execution with retry logic for transient failures.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import subprocess
import time
from pathlib import Path
from typing import Dict, Optional

# Configuration
MAX_RETRIES = 3
INITIAL_BACKOFF = 1  # seconds
MAX_BACKOFF = 60  # seconds
BACKOFF_MULTIPLIER = 2

def is_transient_error(error_output: str) -> bool:
    """Determine if error is transient (retryable) or permanent."""
    transient_indicators = [
        "network",
        "timeout",
        "connection",
        "rate limit",
        "temporary",
        "503",
        "502",
        "504",
        "429"  # Too Many Requests
    ]
    
    error_lower = error_output.lower()
    return any(indicator in error_lower for indicator in transient_indicators)

def execute_with_retry(script_path: str, input_data: str, max_retries: int = MAX_RETRIES) -> dict:
    """Execute script with retry logic."""
    results = {
        "status": "error",
        "attempts": [],
        "final_result": None,
        "retries_used": 0
    }
    
    backoff = INITIAL_BACKOFF
    
    for attempt in range(1, max_retries + 1):
        try:
            # Execute script
            process = subprocess.run(
                [sys.executable, script_path],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
                encoding='utf-8'
            )
            
            attempt_result = {
                "attempt": attempt,
                "exit_code": process.returncode,
                "stdout": process.stdout,
                "stderr": process.stderr,
                "success": process.returncode == 0
            }
            
            results["attempts"].append(attempt_result)
            
            # If successful, return result
            if process.returncode == 0:
                try:
                    result_json = json.loads(process.stdout)
                    results["status"] = "success"
                    results["final_result"] = result_json
                    results["retries_used"] = attempt - 1
                    return results
                except json.JSONDecodeError:
                    # Not JSON, but exit code was 0
                    results["status"] = "success"
                    results["final_result"] = {"output": process.stdout}
                    results["retries_used"] = attempt - 1
                    return results
            
            # Check if error is transient
            if not is_transient_error(process.stderr + process.stdout):
                # Permanent error - don't retry
                results["status"] = "error"
                results["final_result"] = {
                    "error": "Permanent error - not retrying",
                    "stderr": process.stderr,
                    "stdout": process.stdout
                }
                results["retries_used"] = attempt - 1
                return results
            
            # Transient error - retry with backoff
            if attempt < max_retries:
                time.sleep(backoff)
                backoff = min(backoff * BACKOFF_MULTIPLIER, MAX_BACKOFF)
            else:
                # Last attempt failed
                results["status"] = "error"
                results["final_result"] = {
                    "error": "Max retries exceeded",
                    "stderr": process.stderr,
                    "stdout": process.stdout
                }
                results["retries_used"] = max_retries - 1
                return results
                
        except subprocess.TimeoutExpired:
            attempt_result = {
                "attempt": attempt,
                "exit_code": -1,
                "error": "Timeout expired",
                "success": False
            }
            results["attempts"].append(attempt_result)
            
            if attempt < max_retries:
                time.sleep(backoff)
                backoff = min(backoff * BACKOFF_MULTIPLIER, MAX_BACKOFF)
            else:
                results["status"] = "error"
                results["final_result"] = {"error": "Timeout after max retries"}
                results["retries_used"] = max_retries - 1
                return results
                
        except Exception as e:
            attempt_result = {
                "attempt": attempt,
                "exit_code": -1,
                "error": str(e),
                "success": False
            }
            results["attempts"].append(attempt_result)
            
            if attempt < max_retries:
                time.sleep(backoff)
                backoff = min(backoff * BACKOFF_MULTIPLIER, MAX_BACKOFF)
            else:
                results["status"] = "error"
                results["final_result"] = {"error": str(e)}
                results["retries_used"] = max_retries - 1
                return results
    
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: full-integration-retry-wrapper.py <script_path> [input_json]")
        sys.exit(1)
    
    script_path = Path(sys.argv[1])
    if not script_path.exists():
        print(json.dumps({
            "status": "error",
            "error": f"Script not found: {script_path}"
        }, indent=2))
        sys.exit(1)
    
    # Get input data
    if len(sys.argv) > 2:
        input_data = sys.argv[2]
    else:
        input_data = sys.stdin.read()
    
    result = execute_with_retry(str(script_path), input_data)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)

