#!/usr/bin/env python3
"""
n8n Workflow Debugger
Automatically diagnoses and fixes issues for all 4 active workflows
Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
import requests
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class WorkflowConfig:
    """Workflow configuration"""
    name: str
    webhook_path: str
    test_payload: dict
    expected_response_keys: List[str]
    critical_nodes: List[str]

# Define all 4 active workflows
WORKFLOWS = [
    WorkflowConfig(
        name="Unity Build Orchestrator",
        webhook_path="/unity-build",
        test_payload={"request": "Test build", "branch": "main"},
        expected_response_keys=["status", "request"],
        critical_nodes=["Webhook", "GitHub API", "Netlify API"]
    ),
    WorkflowConfig(
        name="Full Integration Workflow",
        webhook_path="/ballcode-dev",
        test_payload={"prompt": "Test integration", "mode": "quick"},
        expected_response_keys=["status", "actionPlan"],
        critical_nodes=["Webhook", "OpenAI", "Code Execution"]
    ),
    WorkflowConfig(
        name="Screenshot Fix Workflow",
        webhook_path="/screenshot-fix",
        test_payload={"screenshotUrl": "test", "context": "Test error"},
        expected_response_keys=["status", "analysis"],
        critical_nodes=["Webhook", "GPT-4 Vision", "Code Fix"]
    ),
    WorkflowConfig(
        name="Book Content Update Workflow",
        webhook_path="/book-content-update",
        test_payload={"bookId": "book1", "action": "test"},
        expected_response_keys=["status"],
        critical_nodes=["Webhook", "Content Update"]
    ),
]

class WorkflowDebugger:
    """Debugger for n8n workflows"""
    
    def __init__(self, n8n_url: str = "http://192.168.1.226:5678", use_test: bool = True):
        self.n8n_url = n8n_url.rstrip('/')
        self.webhook_prefix = "/webhook-test" if use_test else "/webhook"
        self.results = []
    
    def check_n8n_health(self) -> Tuple[bool, str]:
        """Check if n8n is running"""
        try:
            response = requests.get(f"{self.n8n_url}/healthz", timeout=5)
            if response.status_code == 200:
                return True, "n8n is running"
            return False, f"n8n health check returned {response.status_code}"
        except requests.exceptions.RequestException as e:
            return False, f"Cannot connect to n8n: {e}"
    
    def test_webhook(self, workflow: WorkflowConfig) -> Dict:
        """Test a single workflow webhook"""
        url = f"{self.n8n_url}{self.webhook_prefix}{workflow.webhook_path}"
        
        try:
            response = requests.post(
                url,
                json=workflow.test_payload,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            result = {
                "workflow": workflow.name,
                "webhook_path": workflow.webhook_path,
                "status_code": response.status_code,
                "success": response.status_code in [200, 201],
                "response": response.text[:500] if response.text else "",
                "error": None
            }
            
            # Check for expected response keys
            if result["success"]:
                try:
                    response_json = response.json()
                    missing_keys = [key for key in workflow.expected_response_keys 
                                  if key not in response_json]
                    if missing_keys:
                        result["warning"] = f"Missing expected keys: {missing_keys}"
                except:
                    pass
            
            return result
            
        except requests.exceptions.RequestException as e:
            return {
                "workflow": workflow.name,
                "webhook_path": workflow.webhook_path,
                "status_code": None,
                "success": False,
                "response": "",
                "error": str(e)
            }
    
    def diagnose_issue(self, result: Dict) -> List[str]:
        """Diagnose issues from test result"""
        issues = []
        
        if result["status_code"] == 404:
            issues.append("❌ Workflow not found - Check if workflow is ACTIVE in n8n UI")
            issues.append("   → Verify webhook path is correct")
            issues.append("   → Check workflow name matches webhook path")
        
        elif result["status_code"] == 500:
            issues.append("❌ Workflow execution error - Check n8n execution logs")
            issues.append("   → Look for node errors in execution details")
            issues.append("   → Verify credentials are configured")
            issues.append("   → Check environment variables")
        
        elif result["status_code"] is None:
            issues.append("❌ Cannot connect to n8n")
            issues.append("   → Check if n8n is running: curl -s http://192.168.1.226:5678/healthz")
            issues.append("   → Verify network connectivity")
        
        elif not result["success"]:
            issues.append(f"⚠️  Unexpected status code: {result['status_code']}")
            issues.append("   → Check n8n execution logs for details")
        
        if "warning" in result:
            issues.append(f"⚠️  {result['warning']}")
        
        return issues
    
    def suggest_fix(self, result: Dict, workflow: WorkflowConfig) -> List[str]:
        """Suggest fixes for issues"""
        fixes = []
        
        if result["status_code"] == 404:
            fixes.append("1. Open n8n UI: http://192.168.1.226:5678")
            fixes.append("2. Find workflow: " + workflow.name)
            fixes.append("3. Toggle 'Active' to ON (green)")
            fixes.append("4. Verify webhook path matches: " + workflow.webhook_path)
        
        elif result["status_code"] == 500:
            fixes.append("1. Check n8n Executions tab for error details")
            fixes.append("2. Verify all credentials are configured:")
            fixes.append("   - GitHub API token")
            fixes.append("   - OpenAI API key")
            fixes.append("   - Netlify API token")
            fixes.append("3. Check environment variables are set")
            fixes.append("4. Review workflow node configurations")
        
        elif result["status_code"] is None:
            fixes.append("1. Start n8n: Check if service is running")
            fixes.append("2. Verify Pi is accessible: ping 192.168.1.226")
            fixes.append("3. Check n8n logs for startup errors")
        
        return fixes
    
    def debug_all(self) -> Dict:
        """Debug all workflows"""
        print("🔍 n8n Workflow Debugger")
        print("=" * 50)
        print(f"n8n URL: {self.n8n_url}")
        print(f"Webhook prefix: {self.webhook_prefix}")
        print()
        
        # Check n8n health
        print("1️⃣ Checking n8n health...")
        health_ok, health_msg = self.check_n8n_health()
        if health_ok:
            print(f"   ✅ {health_msg}\n")
        else:
            print(f"   ❌ {health_msg}\n")
            return {"error": health_msg}
        
        # Test each workflow
        all_results = []
        for workflow in WORKFLOWS:
            print(f"2️⃣ Testing {workflow.name}...")
            result = self.test_webhook(workflow)
            all_results.append(result)
            
            if result["success"]:
                print(f"   ✅ PASS - HTTP {result['status_code']}")
            else:
                print(f"   ❌ FAIL - HTTP {result.get('status_code', 'N/A')}")
                if result.get("error"):
                    print(f"   Error: {result['error']}")
            print()
        
        # Diagnose issues
        print("3️⃣ Diagnosing issues...")
        print()
        for result in all_results:
            if not result["success"]:
                print(f"🔍 {result['workflow']}:")
                issues = self.diagnose_issue(result)
                for issue in issues:
                    print(f"   {issue}")
                
                fixes = self.suggest_fix(result, next(w for w in WORKFLOWS if w.name == result["workflow"]))
                if fixes:
                    print("   💡 Suggested fixes:")
                    for fix in fixes:
                        print(f"      {fix}")
                print()
        
        # Summary
        passed = sum(1 for r in all_results if r["success"])
        failed = len(all_results) - passed
        
        print("=" * 50)
        print(f"📊 Summary: {passed} passed, {failed} failed")
        print()
        
        if failed == 0:
            print("✅ All workflows are working correctly!")
        else:
            print(f"⚠️  {failed} workflow(s) need attention")
            print("   Review the diagnostics above for fixes")
        
        return {
            "health": health_ok,
            "results": all_results,
            "passed": passed,
            "failed": failed
        }

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Debug n8n workflows")
    parser.add_argument("--url", default="http://192.168.1.226:5678", help="n8n URL")
    parser.add_argument("--production", action="store_true", help="Use production webhooks")
    
    args = parser.parse_args()
    
    debugger = WorkflowDebugger(
        n8n_url=args.url,
        use_test=not args.production
    )
    
    results = debugger.debug_all()
    
    if results.get("error"):
        sys.exit(1)
    
    if results.get("failed", 0) > 0:
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    main()

