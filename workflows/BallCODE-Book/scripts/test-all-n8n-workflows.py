#!/usr/bin/env python3
"""
Test All n8n Workflows
Comprehensive testing script to verify all workflows work

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import requests
import json
import sys
from pathlib import Path
from datetime import datetime

# n8n Configuration
N8N_URL = "http://192.168.1.226:5678"

# Workflow webhooks to test
WORKFLOWS = {
    "unity-build": {
        "name": "Unity Build Orchestrator",
        "webhook": "/webhook/unity-build",
        "test_payload": {
            "request": "Test build - diagnostic",
            "branch": "main"
        }
    },
    "full-integration": {
        "name": "Full Integration - AI Analysis",
        "webhook": "/webhook/ballcode-dev",
        "test_payload": {
            "prompt": "Test integration - verify all systems connected"
        }
    },
    "screenshot-fix": {
        "name": "Screenshot-to-Fix Automation",
        "webhook": "/webhook/screenshot-fix",
        "test_payload": {
            "screenshotUrl": "https://via.placeholder.com/800x600.png",
            "context": "Test screenshot for diagnostic purposes"
        }
    }
}

def test_webhook(webhook_path: str, payload: dict, workflow_name: str) -> dict:
    """Test a single webhook endpoint."""
    url = f"{N8N_URL}{webhook_path}"
    
    print(f"\n🧪 Testing: {workflow_name}")
    print(f"   URL: {url}")
    print(f"   Payload: {json.dumps(payload, indent=2)}")
    
    try:
        response = requests.post(
            url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=60
        )
        
        result = {
            "success": response.status_code == 200,
            "status_code": response.status_code,
            "response": response.text[:500] if response.text else "No response",
            "headers": dict(response.headers)
        }
        
        if response.status_code == 200:
            print(f"   ✅ Status: {response.status_code} - Success!")
            try:
                json_response = response.json()
                print(f"   Response: {json.dumps(json_response, indent=2)[:200]}")
            except:
                print(f"   Response: {response.text[:200]}")
        else:
            print(f"   ❌ Status: {response.status_code} - Failed!")
            print(f"   Response: {response.text[:200]}")
        
        return result
        
    except requests.exceptions.ConnectionError:
        print(f"   ❌ Connection Error: Cannot connect to {N8N_URL}")
        return {
            "success": False,
            "error": "Connection failed",
            "message": f"Cannot connect to n8n at {N8N_URL}"
        }
    except requests.exceptions.Timeout:
        print(f"   ⏱️ Timeout: Request took longer than 60 seconds")
        return {
            "success": False,
            "error": "Timeout",
            "message": "Workflow may still be running"
        }
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "message": f"Unexpected error: {e}"
        }

def check_n8n_health() -> bool:
    """Check if n8n is accessible."""
    try:
        response = requests.get(f"{N8N_URL}/healthz", timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    """Main testing function."""
    print("=" * 70)
    print("🧪 n8n Workflow Testing Suite")
    print("=" * 70)
    print(f"\n📡 Testing n8n at: {N8N_URL}")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check n8n is accessible
    print("\n🔍 Checking n8n connectivity...")
    if not check_n8n_health():
        print(f"❌ Cannot connect to n8n at {N8N_URL}")
        print("\n💡 Troubleshooting:")
        print("   1. Check n8n is running on the Pi")
        print("   2. Check network connectivity")
        print("   3. Verify URL is correct")
        return False
    
    print("✅ n8n is accessible!")
    
    # Test each workflow
    results = {}
    
    for workflow_id, workflow_info in WORKFLOWS.items():
        result = test_webhook(
            workflow_info["webhook"],
            workflow_info["test_payload"],
            workflow_info["name"]
        )
        results[workflow_id] = result
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 Test Results Summary")
    print("=" * 70)
    
    total = len(results)
    successful = sum(1 for r in results.values() if r.get("success"))
    failed = total - successful
    
    print(f"\nTotal Workflows Tested: {total}")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"Success Rate: {(successful/total*100):.1f}%")
    
    print("\n📋 Detailed Results:")
    for workflow_id, result in results.items():
        workflow_name = WORKFLOWS[workflow_id]["name"]
        status = "✅" if result.get("success") else "❌"
        print(f"  {status} {workflow_name}")
        if not result.get("success"):
            error = result.get("error") or result.get("message", "Unknown error")
            print(f"     Error: {error}")
    
    # Save results
    results_file = Path(__file__).parent.parent / "n8n-test-results.json"
    with open(results_file, 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "n8n_url": N8N_URL,
            "results": results,
            "summary": {
                "total": total,
                "successful": successful,
                "failed": failed,
                "success_rate": (successful/total*100) if total > 0 else 0
            }
        }, f, indent=2)
    
    print(f"\n💾 Results saved to: {results_file}")
    
    # Recommendations
    if failed > 0:
        print("\n🔧 Next Steps:")
        print("   1. Check n8n Executions tab for error details")
        print("   2. Review workflow configurations")
        print("   3. Check environment variables and credentials")
        print("   4. See FIX-WORKFLOW-ERRORS.md for detailed fixes")
    
    return successful == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)


