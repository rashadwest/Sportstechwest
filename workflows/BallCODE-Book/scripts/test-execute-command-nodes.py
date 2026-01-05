#!/usr/bin/env python3
"""
Test Execute Command Nodes in Full Integration Workflow
Verifies that scripts actually execute, not just generate JSON.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import subprocess
import requests
import time
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

def test_script_execution_directly():
    """Test that scripts can be executed directly (simulating Execute Command node)."""
    print("🧪 Testing Script Execution (Direct - Simulating Execute Command Node)\n")
    
    results = {
        "status": "success",
        "tests": [],
        "timestamp": datetime.now().isoformat()
    }
    
    # Test each script with a simple input
    scripts = [
        ("full-integration-apply-game.py", '{"unityScripts": [], "levelFiles": []}'),
        ("full-integration-apply-curriculum.py", '{"curriculumUpdates": []}'),
        ("full-integration-apply-book.py", '{"bookUpdates": []}'),
        ("full-integration-apply-website.py", '{"htmlFiles": [], "cssUpdates": []}')
    ]
    
    for script_name, test_input in scripts:
        script_path = SCRIPTS_DIR / script_name
        
        if not script_path.exists():
            results["tests"].append({
                "script": script_name,
                "status": "error",
                "error": "Script not found"
            })
            continue
        
        try:
            # Simulate Execute Command node: python3 script.py < input
            process = subprocess.run(
                [sys.executable, str(script_path)],
                input=test_input,
                capture_output=True,
                text=True,
                timeout=30,
                encoding='utf-8'
            )
            
            # Check if script executed and returned JSON
            try:
                output = json.loads(process.stdout)
                executed = output.get("status") in ["success", "partial", "error"]
                
                results["tests"].append({
                    "script": script_name,
                    "status": "success" if executed else "error",
                    "exit_code": process.returncode,
                    "output_status": output.get("status"),
                    "executed": executed,
                    "has_output": bool(output)
                })
            except json.JSONDecodeError:
                results["tests"].append({
                    "script": script_name,
                    "status": "error",
                    "error": "Output is not valid JSON",
                    "raw_output": process.stdout[:200]
                })
                
        except subprocess.TimeoutExpired:
            results["tests"].append({
                "script": script_name,
                "status": "error",
                "error": "Script execution timeout"
            })
        except Exception as e:
            results["tests"].append({
                "script": script_name,
                "status": "error",
                "error": str(e)
            })
    
    # Summary
    passed = sum(1 for t in results["tests"] if t.get("status") == "success")
    total = len(results["tests"])
    
    print(f"✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}\n")
    
    for test in results["tests"]:
        status_icon = "✅" if test.get("status") == "success" else "❌"
        print(f"{status_icon} {test['script']}: {test.get('status', 'unknown')}")
        if test.get("executed"):
            print(f"   → Script executed, output status: {test.get('output_status')}")
        if test.get("error"):
            print(f"   → Error: {test['error']}")
    
    results["summary"] = {
        "passed": passed,
        "total": total,
        "all_passed": passed == total
    }
    
    return results

def test_n8n_workflow_execution():
    """Test n8n workflow execution and check if Execute Command nodes ran."""
    print("\n🧪 Testing n8n Workflow Execution\n")
    
    n8n_url = "http://192.168.1.226:5678"
    webhook_path = "/webhook/ballcode-dev"
    
    test_prompt = {
        "prompt": "Test script execution: Create a simple test file",
        "mode": "quick",
        "sessionId": f"test-execution-{int(time.time())}"
    }
    
    print(f"📍 n8n URL: {n8n_url}")
    print(f"🔗 Webhook: {webhook_path}")
    print(f"📤 Sending test request...\n")
    
    try:
        response = requests.post(
            f"{n8n_url}{webhook_path}",
            json=test_prompt,
            timeout=300
        )
        
        result = {
            "status": "success" if response.status_code == 200 else "error",
            "http_code": response.status_code,
            "response_time": response.elapsed.total_seconds()
        }
        
        if response.status_code == 200:
            try:
                response_data = response.json()
                result["response_data"] = response_data
                
                # Check if response indicates script execution
                has_action_plan = bool(response_data.get("actionPlan"))
                has_script_results = bool(response_data.get("scriptResults"))
                has_updates = bool(response_data.get("updates"))
                
                result["execution_indicators"] = {
                    "has_action_plan": has_action_plan,
                    "has_script_results": has_script_results,
                    "has_updates": has_updates,
                    "scripts_executed": has_script_results or has_updates
                }
                
                print(f"✅ Workflow executed (HTTP {response.status_code})")
                print(f"⏱️  Response time: {result['response_time']:.2f}s")
                print(f"\n📊 Execution Indicators:")
                print(f"   - Has action plan: {has_action_plan}")
                print(f"   - Has script results: {has_script_results}")
                print(f"   - Has updates: {has_updates}")
                print(f"   - Scripts executed: {result['execution_indicators']['scripts_executed']}")
                
                if not result["execution_indicators"]["scripts_executed"]:
                    print("\n⚠️  WARNING: Response doesn't indicate script execution!")
                    print("   The workflow may be generating plans but not executing scripts.")
                    print("   Check n8n executions for Execute Command node logs:")
                    print(f"   {n8n_url}/executions")
                
            except json.JSONDecodeError:
                result["error"] = "Response is not valid JSON"
                result["raw_response"] = response.text[:500]
        else:
            result["error"] = f"HTTP {response.status_code}"
            result["response_text"] = response.text[:500]
            print(f"❌ Workflow execution failed (HTTP {response.status_code})")
        
        return result
        
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "error": str(e)
        }

def main():
    """Run all tests."""
    print("=" * 60)
    print("🧪 TESTING EXECUTE COMMAND NODES")
    print("=" * 60)
    print()
    
    # Test 1: Direct script execution
    direct_results = test_script_execution_directly()
    
    # Test 2: n8n workflow execution
    workflow_results = test_n8n_workflow_execution()
    
    # Final summary
    print("\n" + "=" * 60)
    print("📊 FINAL SUMMARY")
    print("=" * 60)
    
    print("\n1️⃣ Direct Script Execution:")
    if direct_results["summary"]["all_passed"]:
        print("   ✅ All scripts execute correctly")
    else:
        print(f"   ⚠️  {direct_results['summary']['passed']}/{direct_results['summary']['total']} scripts passed")
    
    print("\n2️⃣ n8n Workflow Execution:")
    if workflow_results.get("status") == "success":
        if workflow_results.get("execution_indicators", {}).get("scripts_executed"):
            print("   ✅ Workflow executed and scripts ran")
        else:
            print("   ⚠️  Workflow executed but scripts may not have run")
            print("   → Check n8n executions for Execute Command node logs")
    else:
        print(f"   ❌ Workflow execution failed: {workflow_results.get('error')}")
    
    print("\n📋 Next Steps:")
    print("   1. Check n8n executions: http://192.168.1.226:5678/executions")
    print("   2. Verify Execute Command nodes appear in execution logs")
    print("   3. Check if scripts actually modified files")
    
    # Exit code
    if direct_results["summary"]["all_passed"] and workflow_results.get("status") == "success":
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())

