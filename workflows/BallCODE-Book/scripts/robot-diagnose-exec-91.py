#!/usr/bin/env python3
"""
Robot: Diagnose Exec ID 91 Error
Checks the specific error in Screenshot-to-Fix execution 91

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

def check_execution_details():
    """Provide steps to check Exec ID 91 error."""
    print_header("Diagnosing Exec ID 91 Error")
    
    print("\n📊 Execution Details:")
    print("   Workflow: Screenshot-to-Fix Automation")
    print("   Exec ID: 91 (Retry of 90)")
    print("   Status: Error")
    print("   Started: Dec 17, 15:46:46")
    print("   Run Time: 416ms")
    print()
    
    print("🔍 To See Exact Error:")
    print(f"   1. Open: {N8N_URL}")
    print("   2. Click 'Executions' tab")
    print("   3. Click on Exec ID 91")
    print("   4. Find RED node in workflow diagram")
    print("   5. Click on the red node")
    print("   6. Read the error message")
    print()
    
    print("💡 Common Errors for Screenshot-to-Fix:")
    print("   ❌ 'Credential not found' → Credential not set")
    print("   ❌ 'OpenAI API key invalid' → Wrong/expired API key")
    print("   ❌ 'Authentication failed' → Credential issue")
    print("   ❌ 'Input data missing' → Webhook data format issue")
    print("   ❌ 'Parse error' → Input parsing issue")
    print("   ❌ 'Model not found' → GPT-5.2-PRO not available")
    print("   ❌ 'Rate limit exceeded' → API rate limit")
    print()

def test_webhook_with_detailed_logging():
    """Test webhook and provide detailed analysis."""
    print_header("Testing Screenshot-to-Fix Webhook")
    
    print("\n🧪 Sending test request...")
    
    test_payload = {
        "screenshotUrl": "https://example.com/test.png",
        "context": "Robot diagnostic test for Exec ID 91"
    }
    
    try:
        response = requests.post(
            f"{N8N_URL}/webhook/screenshot-fix",
            json=test_payload,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text[:300]}")
        print()
        
        if response.status_code == 200:
            print("   ✅ Webhook accepts request")
            print("   ⚠️  But execution may still fail internally")
            print("   → Check Executions tab for new execution")
            print("   → See if it succeeds or fails")
        else:
            print(f"   ❌ Webhook returned error: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")

def generate_fix_guide():
    """Generate fix guide based on common errors."""
    print_header("Fix Guide for Screenshot-to-Fix Errors")
    
    print("\n🔧 Based on Error Type:")
    print()
    
    print("1. If Error: 'Credential not found' or 'OpenAI API key invalid'")
    print("   Fix:")
    print("   a. Go to Credentials → Add Credential")
    print("   b. Select 'OpenAI API'")
    print("   c. Enter valid API key")
    print("   d. Save")
    print("   e. Assign to 'Message a model' node")
    print("   f. Save workflow")
    print()
    
    print("2. If Error: 'Input data missing' or 'Parse error'")
    print("   Fix:")
    print("   a. Check webhook input format")
    print("   b. Ensure 'screenshotUrl' is provided")
    print("   c. Check 'Normalize Screenshot Input' node")
    print()
    
    print("3. If Error: 'Model not found' or 'GPT-5.2-PRO not available'")
    print("   Fix:")
    print("   a. Check if GPT-5.2-PRO is available in your OpenAI account")
    print("   b. Try GPT-4 or GPT-4-turbo instead")
    print("   c. Update model in 'Message a model' node")
    print()
    
    print("4. If Error: 'Rate limit exceeded'")
    print("   Fix:")
    print("   a. Wait a few minutes")
    print("   b. Check OpenAI usage limits")
    print("   c. Upgrade OpenAI plan if needed")
    print()

def create_error_check_script():
    """Create script to help check error."""
    script_content = f"""#!/bin/bash
# Robot: Check Exec ID 91 Error Details

echo "🤖 Checking Exec ID 91 Error"
echo ""
echo "Since n8n API requires authentication, check manually:"
echo ""
echo "1. Open: {N8N_URL}"
echo "2. Click 'Executions' tab"
echo "3. Click Exec ID 91"
echo "4. Find RED node"
echo "5. Click on it"
echo "6. Copy the error message"
echo ""
echo "Then share the error message to get specific fix!"
"""
    
    script_file = Path(__file__).parent / "check-exec-91-error.sh"
    with open(script_file, 'w') as f:
        f.write(script_content)
    
    import os
    os.chmod(script_file, 0o755)
    
    return script_file

def main():
    """Main diagnostic function."""
    print_header("Robot: Diagnose Exec ID 91 Error")
    
    # Check execution details
    check_execution_details()
    
    # Test webhook
    test_webhook_with_detailed_logging()
    
    # Generate fix guide
    generate_fix_guide()
    
    # Create check script
    check_script = create_error_check_script()
    
    # Summary
    print_header("Next Steps")
    
    print("\n📋 Action Required:")
    print("   1. Click Exec ID 91 in n8n Executions tab")
    print("   2. Find the RED node")
    print("   3. Click on it to see error message")
    print("   4. Share the exact error message")
    print("   5. I'll provide the specific fix")
    print()
    
    print("💡 The credential is set, so error is likely:")
    print("   - Invalid/expired API key")
    print("   - Input data format issue")
    print("   - Model availability issue")
    print("   - Rate limit")
    print()
    
    print(f"📝 Check script created: {check_script}")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

