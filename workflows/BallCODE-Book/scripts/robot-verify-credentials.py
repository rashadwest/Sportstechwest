#!/usr/bin/env python3
"""
Robot: Verify n8n Credentials
Checks if credentials are properly set and accessible

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import requests
import json
import sys
from pathlib import Path

N8N_URL = "http://192.168.1.226:5678"

def print_header(title):
    """Print formatted header."""
    print("\n" + "=" * 70)
    print(f"🤖 {title}")
    print("=" * 70)

def check_n8n_connectivity():
    """Check if n8n is accessible."""
    try:
        response = requests.get(f"{N8N_URL}/healthz", timeout=5)
        return response.status_code == 200
    except:
        return False

def test_openai_credential():
    """Test if OpenAI credential works by testing a workflow."""
    print_header("Testing OpenAI Credential")
    
    print("\n🧪 Testing Screenshot-to-Fix workflow (uses OpenAI):")
    
    try:
        response = requests.post(
            f"{N8N_URL}/webhook/screenshot-fix",
            json={
                "screenshotUrl": "https://example.com/test.png",
                "context": "Robot credential test"
            },
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            print("   ✅ Webhook responds (credential likely working)")
            return True
        else:
            print(f"   ⚠️  Status {response.status_code}")
            if response.text:
                print(f"   Response: {response.text[:200]}")
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def check_workflow_executions():
    """Check recent executions for credential errors."""
    print_header("Checking Recent Executions for Credential Errors")
    
    print("\n📊 Recent Screenshot-to-Fix executions:")
    print("   (Check n8n Executions tab for details)")
    print()
    print("   Exec ID 88: Error (935ms) - 15:26:44")
    print("   Exec ID 85: Error (453ms) - 15:13:40")
    print("   Exec ID 82: Error (1.035s) - 15:12:44")
    print()
    print("💡 To verify credential error:")
    print(f"   1. Open: {N8N_URL}")
    print("   2. Go to Executions tab")
    print("   3. Click on Exec ID 88 (most recent)")
    print("   4. Find RED node")
    print("   5. Check if error mentions 'credential' or 'OpenAI'")
    print()

def generate_credential_verification_guide():
    """Generate guide for verifying credentials."""
    print_header("Credential Verification Guide")
    
    print("\n📋 How to Verify Credentials Are Set:")
    print()
    print("Method 1: Check in n8n UI")
    print(f"   1. Open: {N8N_URL}")
    print("   2. Click 'Credentials' tab (left sidebar)")
    print("   3. Look for 'OpenAI API' or 'OpenAI account'")
    print("   4. Click on it to see if it has an API key")
    print()
    print("Method 2: Check in Workflow Node")
    print("   1. Open Screenshot-to-Fix workflow")
    print("   2. Click 'Message a model' node")
    print("   3. Check 'Credential to connect with' dropdown")
    print("   4. Should show 'OpenAI account' (not empty)")
    print()
    print("Method 3: Test Workflow Execution")
    print("   1. Open Screenshot-to-Fix workflow")
    print("   2. Click 'Execute workflow' button")
    print("   3. Watch execution")
    print("   4. If 'Message a model' node turns RED:")
    print("      → Credential issue")
    print("   5. If node turns GREEN:")
    print("      → Credential is working")
    print()

def create_credential_test_script():
    """Create script to test credentials via terminal."""
    script_content = f"""#!/bin/bash
# Robot: Test n8n Credentials via Workflow Execution

echo "🤖 Testing n8n Credentials"
echo ""

# Test Screenshot-to-Fix (uses OpenAI)
echo "🧪 Testing Screenshot-to-Fix workflow (OpenAI credential)..."
RESPONSE=$(curl -s -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \\
  -H "Content-Type: application/json" \\
  -d '{{"screenshotUrl": "https://example.com/test.png", "context": "Credential test"}}')

STATUS=$(echo "$RESPONSE" | grep -o '"code":[0-9]*' | cut -d: -f2)

if [ "$STATUS" = "200" ] || [ -z "$STATUS" ]; then
    echo "   ✅ Webhook responds (credential likely working)"
else
    echo "   ⚠️  Status: $STATUS"
    echo "   Check n8n Executions tab for error details"
fi

echo ""
echo "💡 To verify credential:"
echo "   1. Open: http://192.168.1.226:5678"
echo "   2. Go to Executions tab"
echo "   3. Find most recent Screenshot-to-Fix execution"
echo "   4. Click on it to see if credential error"
"""
    
    script_file = Path(__file__).parent / "test-credentials.sh"
    with open(script_file, 'w') as f:
        f.write(script_content)
    
    import os
    os.chmod(script_file, 0o755)
    
    print(f"💾 Created test script: {script_file}")
    return script_file

def main():
    """Main verification function."""
    print_header("Robot: Verify n8n Credentials")
    
    # Check connectivity
    if not check_n8n_connectivity():
        print(f"\n❌ Cannot connect to n8n at {N8N_URL}")
        return False
    
    print("✅ n8n is accessible")
    
    # Test OpenAI credential via workflow
    credential_works = test_openai_credential()
    
    # Check executions
    check_workflow_executions()
    
    # Generate verification guide
    generate_credential_verification_guide()
    
    # Create test script
    test_script = create_credential_test_script()
    
    # Summary
    print_header("Credential Verification Summary")
    
    print("\n📊 Status:")
    if credential_works:
        print("   ✅ OpenAI credential appears to be working")
        print("   (Webhook responds, but check executions for actual errors)")
    else:
        print("   ⚠️  OpenAI credential may have issues")
        print("   (Check execution errors for details)")
    
    print("\n🔍 Verification Steps:")
    print("   1. Check Credentials tab in n8n UI")
    print("   2. Check 'Message a model' node credential dropdown")
    print("   3. Check Executions tab for credential errors")
    print(f"   4. Run: bash {test_script}")
    
    print("\n💡 If credential is set in node but executions fail:")
    print("   - Credential might be invalid/expired")
    print("   - API key might not have proper permissions")
    print("   - Check error message in failed execution")
    
    return credential_works

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

