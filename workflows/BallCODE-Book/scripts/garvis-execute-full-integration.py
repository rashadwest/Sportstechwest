#!/usr/bin/env python3
"""
Garvis: Execute Full Integration Seamlessly
Calls Full Integration workflow, extracts updates, and executes all scripts automatically.

Part of Garvis System - Seamless automation without human intervention.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys
import json
import subprocess
import requests
from pathlib import Path
from typing import Dict, Optional, Any
from datetime import datetime

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

# Configuration
N8N_URL = "http://192.168.1.226:5678"
WEBHOOK_PATH = "/webhook/ballcode-dev"
TIMEOUT = 300  # 5 minutes

# Colors for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*60}{NC}")
    print(f"{BLUE}{text:^60}{NC}")
    print(f"{BLUE}{'='*60}{NC}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{NC}")

def print_error(text):
    print(f"{RED}❌ {text}{NC}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{NC}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{NC}")

def call_full_integration_workflow(prompt: str, mode: str = "quick", session_id: Optional[str] = None) -> Dict:
    """Call Full Integration workflow and get plan."""
    try:
        if not session_id:
            session_id = f"garvis-{datetime.now().timestamp()}"
        
        payload = {
            "prompt": prompt,
            "mode": mode,
            "sessionId": session_id
        }
        
        print_info(f"Calling Full Integration workflow...")
        print_info(f"Prompt: {prompt[:100]}...")
        
        response = requests.post(
            f"{N8N_URL}{WEBHOOK_PATH}",
            json=payload,
            timeout=TIMEOUT
        )
        
        if response.status_code != 200:
            return {
                "status": "error",
                "error": f"Workflow returned status {response.status_code}",
                "response": response.text
            }
        
        result = response.json()
        return {
            "status": "success",
            "session_id": session_id,
            "workflow_response": result
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__
        }

def extract_updates_from_response(workflow_response: Dict) -> Dict:
    """Extract system updates from workflow response."""
    try:
        updates = {
            "game": None,
            "curriculum": None,
            "book": None,
            "website": None
        }
        
        # Try to extract from workflow response
        # The response structure may vary, so we'll try multiple paths
        if "gameUpdates" in workflow_response:
            updates["game"] = workflow_response["gameUpdates"]
        elif "game_updates" in workflow_response:
            updates["game"] = workflow_response["game_updates"]
        
        if "curriculumUpdates" in workflow_response:
            updates["curriculum"] = workflow_response["curriculumUpdates"]
        elif "curriculum_updates" in workflow_response:
            updates["curriculum"] = workflow_response["curriculum_updates"]
        
        if "bookUpdates" in workflow_response:
            updates["book"] = workflow_response["bookUpdates"]
        elif "book_updates" in workflow_response:
            updates["book"] = workflow_response["book_updates"]
        
        if "websiteUpdates" in workflow_response:
            updates["website"] = workflow_response["websiteUpdates"]
        elif "website_updates" in workflow_response:
            updates["website"] = workflow_response["website_updates"]
        
        # If no direct updates, try to parse from actionPlan or other fields
        if not any(updates.values()):
            # Check if we need to parse AI responses
            # This would require parsing the workflow's internal structure
            # For now, we'll use what's available in the response
            pass
        
        return {
            "status": "success",
            "updates": updates,
            "has_updates": any(updates.values())
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "updates": {}
        }

def execute_script(script_name: str, input_data: str) -> Dict:
    """Execute a Full Integration script with input data."""
    try:
        script_path = SCRIPTS_DIR / script_name
        
        if not script_path.exists():
            return {
                "status": "error",
                "error": f"Script not found: {script_path}"
            }
        
        print_info(f"Executing: {script_name}")
        
        process = subprocess.run(
            [sys.executable, str(script_path)],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=300,
            encoding='utf-8'
        )
        
        if process.returncode != 0:
            return {
                "status": "error",
                "error": process.stderr,
                "stdout": process.stdout,
                "exit_code": process.returncode
            }
        
        # Try to parse JSON output
        try:
            result = json.loads(process.stdout)
        except json.JSONDecodeError:
            # If not JSON, return as text
            result = {
                "status": "success",
                "output": process.stdout
            }
        
        return result
        
    except subprocess.TimeoutExpired:
        return {
            "status": "error",
            "error": "Script execution timeout"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__
        }

def execute_full_integration(prompt: str, mode: str = "quick", auto_execute: bool = True) -> Dict:
    """Execute Full Integration seamlessly - call workflow and execute scripts."""
    print_header("🚀 GARVIS: Full Integration Execution")
    
    results = {
        "status": "success",
        "session_id": None,
        "workflow_result": None,
        "script_results": {},
        "errors": []
    }
    
    # Step 1: Call Full Integration workflow
    print_info("Step 1: Calling Full Integration workflow...")
    workflow_result = call_full_integration_workflow(prompt, mode)
    
    if workflow_result["status"] != "success":
        print_error(f"Workflow call failed: {workflow_result.get('error')}")
        return {
            "status": "error",
            "error": workflow_result.get("error"),
            "workflow_result": workflow_result
        }
    
    results["session_id"] = workflow_result.get("session_id")
    results["workflow_result"] = workflow_result.get("workflow_response")
    
    print_success("Workflow executed successfully")
    
    # Step 2: Extract updates
    print_info("Step 2: Extracting updates from workflow response...")
    updates_result = extract_updates_from_response(workflow_result["workflow_response"])
    
    if updates_result["status"] != "success":
        print_warning(f"Could not extract updates: {updates_result.get('error')}")
        print_info("Workflow completed, but no updates to execute")
        return results
    
    updates = updates_result["updates"]
    
    if not updates_result["has_updates"]:
        print_info("No updates found in workflow response")
        print_info("Workflow may have generated a plan but no executable updates")
        return results
    
    # Step 3: Execute scripts if auto_execute is enabled
    if not auto_execute:
        print_info("Auto-execute disabled - updates extracted but not executed")
        results["updates"] = updates
        return results
    
    print_info("Step 3: Executing scripts automatically...")
    
    # Execute game script
    if updates["game"]:
        print_info("Executing game updates...")
        game_input = json.dumps(updates["game"])
        game_result = execute_script("full-integration-apply-game.py", game_input)
        results["script_results"]["game"] = game_result
        if game_result["status"] == "success":
            print_success("Game updates applied")
        else:
            print_error(f"Game updates failed: {game_result.get('error')}")
            results["errors"].append(f"Game: {game_result.get('error')}")
    
    # Execute curriculum script
    if updates["curriculum"]:
        print_info("Executing curriculum updates...")
        curriculum_input = json.dumps(updates["curriculum"])
        curriculum_result = execute_script("full-integration-apply-curriculum.py", curriculum_input)
        results["script_results"]["curriculum"] = curriculum_result
        if curriculum_result["status"] == "success":
            print_success("Curriculum updates applied")
        else:
            print_error(f"Curriculum updates failed: {curriculum_result.get('error')}")
            results["errors"].append(f"Curriculum: {curriculum_result.get('error')}")
    
    # Execute book script
    if updates["book"]:
        print_info("Executing book updates...")
        book_input = json.dumps(updates["book"])
        book_result = execute_script("full-integration-apply-book.py", book_input)
        results["script_results"]["book"] = book_result
        if book_result["status"] == "success":
            print_success("Book updates applied")
        else:
            print_error(f"Book updates failed: {book_result.get('error')}")
            results["errors"].append(f"Book: {book_result.get('error')}")
    
    # Execute website script
    if updates["website"]:
        print_info("Executing website updates...")
        website_input = json.dumps(updates["website"])
        website_result = execute_script("full-integration-apply-website.py", website_input)
        results["script_results"]["website"] = website_result
        if website_result["status"] == "success":
            print_success("Website updates applied")
        else:
            print_error(f"Website updates failed: {website_result.get('error')}")
            results["errors"].append(f"Website: {website_result.get('error')}")
    
    # Determine overall status
    if results["errors"]:
        results["status"] = "partial" if results["script_results"] else "error"
    else:
        results["status"] = "success"
    
    # Print summary
    print_header("📊 EXECUTION SUMMARY")
    
    if results["status"] == "success":
        print_success("All systems updated successfully!")
    elif results["status"] == "partial":
        print_warning("Some systems updated, some failed")
    else:
        print_error("Execution failed")
    
    print_info(f"Session ID: {results['session_id']}")
    print_info(f"Scripts executed: {len(results['script_results'])}")
    if results["errors"]:
        print_error(f"Errors: {len(results['errors'])}")
        for error in results["errors"]:
            print_error(f"  - {error}")
    
    return results

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Garvis: Execute Full Integration seamlessly",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Execute with prompt
  python3 scripts/garvis-execute-full-integration.py "Update Book 1"
  
  # Execute with quick mode
  python3 scripts/garvis-execute-full-integration.py "Update Book 1" --mode quick
  
  # Extract updates only (don't execute)
  python3 scripts/garvis-execute-full-integration.py "Update Book 1" --no-execute
        """
    )
    
    parser.add_argument("prompt", help="Development prompt for Full Integration")
    parser.add_argument("--mode", default="quick", choices=["quick", "full"],
                       help="Unified prompting mode (default: quick)")
    parser.add_argument("--no-execute", action="store_true",
                       help="Extract updates but don't execute scripts")
    parser.add_argument("--session-id", help="Custom session ID")
    
    args = parser.parse_args()
    
    result = execute_full_integration(
        prompt=args.prompt,
        mode=args.mode,
        auto_execute=not args.no_execute
    )
    
    # Exit with error code if failed
    if result["status"] == "error":
        sys.exit(1)
    elif result["status"] == "partial":
        sys.exit(2)


