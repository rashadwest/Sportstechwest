#!/usr/bin/env python3
"""
Check n8n Execution Errors
Helps identify what went wrong in failed executions

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys

def main():
    """Guide user to check execution errors manually."""
    print("=" * 70)
    print("🔍 How to Check Execution Errors in n8n")
    print("=" * 70)
    print()
    print("Since n8n API requires authentication, we'll check manually:")
    print()
    print("📋 Step-by-Step Instructions:")
    print()
    print("1. Open n8n UI:")
    print("   http://192.168.1.226:5678")
    print()
    print("2. Click 'Executions' tab (top navigation)")
    print()
    print("3. Find these failed executions:")
    print("   - Exec ID 74: Screenshot-to-Fix (14:02:57)")
    print("   - Exec ID 73: Unity Build Orchestrator (14:02:56)")
    print()
    print("4. Click on Exec ID 73 (Unity Build Orchestrator):")
    print("   - Look for RED nodes (failed)")
    print("   - Click on the red node")
    print("   - Read the error message")
    print("   - Copy the error text")
    print()
    print("5. Click on Exec ID 74 (Screenshot-to-Fix):")
    print("   - Look for RED nodes (failed)")
    print("   - Click on the red node")
    print("   - Read the error message")
    print("   - Copy the error text")
    print()
    print("6. Common errors you might see:")
    print()
    print("   ❌ 'environment variable is not set'")
    print("      → Fix: Add env vars in Settings → Environment Variables")
    print()
    print("   ❌ 'Credential not found' or 'OpenAI API key missing'")
    print("      → Fix: Add OpenAI credential in Credentials")
    print()
    print("   ❌ 'Cannot read property of undefined'")
    print("      → Fix: Check Code node for null/undefined access")
    print()
    print("   ❌ 'TypeError' or 'ReferenceError'")
    print("      → Fix: Fix variable references in Code node")
    print()
    print("=" * 70)
    print("💡 Once you have the error messages, we can fix them quickly!")
    print("=" * 70)

if __name__ == "__main__":
    main()


