#!/usr/bin/env python3
"""
Full Integration: End-to-End Integration Testing
Tests the complete Full Integration workflow end-to-end.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import subprocess
import requests
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent

def test_end_to_end_integration(test_config_json: str) -> dict:
    """Test Full Integration workflow end-to-end."""
    try:
        # Parse test config
        if isinstance(test_config_json, str):
            try:
                config = json.loads(test_config_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', test_config_json)
                if json_match:
                    config = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            config = test_config_json
        
        results = {
            "status": "success",
            "test_name": config.get("test_name", "End-to-End Integration Test"),
            "timestamp": datetime.now().isoformat(),
            "tests_run": [],
            "tests_passed": 0,
            "tests_failed": 0,
            "errors": []
        }
        
        # Test 1: Test Full Integration webhook
        test_webhook = config.get("test_webhook", True)
        if test_webhook:
            try:
                n8n_url = config.get("n8n_url", "http://192.168.1.226:5678")
                webhook_path = config.get("webhook_path", "/webhook/ballcode-dev")
                
                test_prompt = config.get("test_prompt", {
                    "prompt": "Test Full Integration end-to-end",
                    "mode": "quick"
                })
                
                response = requests.post(
                    f"{n8n_url}{webhook_path}",
                    json=test_prompt,
                    timeout=300
                )
                
                webhook_test = {
                    "name": "Full Integration Webhook",
                    "status": "passed" if response.status_code == 200 else "failed",
                    "status_code": response.status_code,
                    "response_time": response.elapsed.total_seconds()
                }
                
                results["tests_run"].append(webhook_test)
                if webhook_test["status"] == "passed":
                    results["tests_passed"] += 1
                else:
                    results["tests_failed"] += 1
                    results["errors"].append(f"Webhook test failed: {response.status_code}")
                    
            except Exception as e:
                results["tests_run"].append({
                    "name": "Full Integration Webhook",
                    "status": "failed",
                    "error": str(e)
                })
                results["tests_failed"] += 1
                results["errors"].append(f"Webhook test error: {str(e)}")
        
        # Test 2: Test script execution
        test_scripts = config.get("test_scripts", True)
        if test_scripts:
            scripts_to_test = [
                "full-integration-apply-game.py",
                "full-integration-apply-curriculum.py",
                "full-integration-apply-book.py",
                "full-integration-apply-website.py"
            ]
            
            for script_name in scripts_to_test:
                try:
                    script_path = PROJECT_ROOT / "scripts" / script_name
                    if not script_path.exists():
                        results["tests_run"].append({
                            "name": f"Script: {script_name}",
                            "status": "failed",
                            "error": "Script not found"
                        })
                        results["tests_failed"] += 1
                        continue
                    
                    # Test with empty input
                    result = subprocess.run(
                        [sys.executable, str(script_path)],
                        input='{}',
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    
                    script_test = {
                        "name": f"Script: {script_name}",
                        "status": "passed" if result.returncode == 0 else "failed",
                        "exit_code": result.returncode
                    }
                    
                    results["tests_run"].append(script_test)
                    if script_test["status"] == "passed":
                        results["tests_passed"] += 1
                    else:
                        results["tests_failed"] += 1
                        results["errors"].append(f"{script_name} failed: {result.stderr}")
                        
                except Exception as e:
                    results["tests_run"].append({
                        "name": f"Script: {script_name}",
                        "status": "failed",
                        "error": str(e)
                    })
                    results["tests_failed"] += 1
                    results["errors"].append(f"{script_name} error: {str(e)}")
        
        # Test 3: Test system integration
        test_integration = config.get("test_integration", True)
        if test_integration:
            # Test game → curriculum → book → website flow
            integration_tests = [
                {"system": "game", "file": "Unity-Scripts/Levels/book1_foundation_block.json"},
                {"system": "curriculum", "file": "CURRICULUM-DATA-EXAMPLE.json"},
                {"system": "book", "file": "My Books"},
                {"system": "website", "file": "BallCode/index.html"}
            ]
            
            for test in integration_tests:
                try:
                    file_path = PROJECT_ROOT / test["file"]
                    exists = file_path.exists()
                    
                    integration_test = {
                        "name": f"Integration: {test['system']}",
                        "status": "passed" if exists else "failed",
                        "file_exists": exists
                    }
                    
                    results["tests_run"].append(integration_test)
                    if integration_test["status"] == "passed":
                        results["tests_passed"] += 1
                    else:
                        results["tests_failed"] += 1
                        results["errors"].append(f"{test['system']} file not found: {test['file']}")
                        
                except Exception as e:
                    results["tests_run"].append({
                        "name": f"Integration: {test['system']}",
                        "status": "failed",
                        "error": str(e)
                    })
                    results["tests_failed"] += 1
        
        # Determine overall status
        if results["tests_failed"] > 0:
            results["status"] = "partial" if results["tests_passed"] > 0 else "failed"
        else:
            results["status"] = "success"
        
        results["summary"] = {
            "total_tests": len(results["tests_run"]),
            "passed": results["tests_passed"],
            "failed": results["tests_failed"],
            "pass_rate": f"{(results['tests_passed'] / len(results['tests_run']) * 100):.1f}%" if results["tests_run"] else "0%"
        }
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "tests_run": [],
            "tests_passed": 0,
            "tests_failed": 0,
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
        # Default test config
        input_json = json.dumps({
            "test_name": "Full Integration End-to-End Test",
            "test_webhook": True,
            "test_scripts": True,
            "test_integration": True,
            "n8n_url": "http://192.168.1.226:5678",
            "webhook_path": "/webhook/ballcode-dev",
            "test_prompt": {
                "prompt": "Test Full Integration end-to-end",
                "mode": "quick"
            }
        })
    
    result = test_end_to_end_integration(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") in ["error", "failed"]:
        sys.exit(1)


