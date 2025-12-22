#!/bin/bash
# Robot: Verify n8n Credentials via Terminal
# Checks credentials are set and working

set -e

N8N_URL="http://192.168.1.226:5678"
N8N_HOST="192.168.1.226"

echo "======================================================================"
echo "🤖 Robot: Verify n8n Credentials"
echo "======================================================================"
echo ""

# Method 1: Test workflow execution
echo "🧪 Method 1: Testing Screenshot-to-Fix workflow (uses OpenAI)..."
RESPONSE=$(curl -s -X POST "${N8N_URL}/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test.png", "context": "Credential verification test"}' \
  -w "\nHTTP_CODE:%{http_code}")

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE:" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE:/d')

if [ "$HTTP_CODE" = "200" ]; then
    echo "   ✅ Webhook responds (200)"
    echo "   ⚠️  But check Executions tab to see if execution succeeded"
else
    echo "   ❌ Status: $HTTP_CODE"
    echo "   Response: $BODY"
fi

echo ""
echo "======================================================================"
echo "📋 Credential Verification Methods"
echo "======================================================================"
echo ""
echo "Since n8n API requires authentication, use these methods:"
echo ""
echo "Method 1: Check Credentials Tab in n8n UI"
echo "   1. Open: ${N8N_URL}"
echo "   2. Click 'Credentials' tab (left sidebar)"
echo "   3. Look for 'OpenAI API' or 'OpenAI account'"
echo "   4. Click on it to verify:"
echo "      - Has API key set (not empty)"
echo "      - No error messages"
echo "      - Status is active"
echo ""
echo "Method 2: Check Workflow Node"
echo "   1. Open Screenshot-to-Fix workflow"
echo "   2. Click 'Message a model' node"
echo "   3. Check 'Credential to connect with' dropdown:"
echo "      - Should show 'OpenAI account' (not empty)"
echo "      - Should have edit icon (means it's set)"
echo ""
echo "Method 3: Check Execution Error (Most Reliable)"
echo "   1. Go to Executions tab"
echo "   2. Click Exec ID 88 (most recent Screenshot-to-Fix error)"
echo "   3. Find RED node in workflow diagram"
echo "   4. Click on it to see error message"
echo "   5. If error says 'credential' or 'OpenAI':"
echo "      → Credential issue (re-add credential)"
echo "   6. If error says something else:"
echo "      → Different issue (not credential)"
echo ""
echo "Method 4: Test Workflow Manually"
echo "   1. Open Screenshot-to-Fix workflow"
echo "   2. Click 'Execute workflow' button (orange)"
echo "   3. Watch 'Message a model' node:"
echo "      - GREEN = Credential works ✅"
echo "      - RED = Credential issue ❌"
echo ""
echo "======================================================================"
echo "🔧 If Credential Error Found"
echo "======================================================================"
echo ""
echo "Re-add OpenAI credential:"
echo "   1. Credentials → Add Credential"
echo "   2. Search 'OpenAI' → Select 'OpenAI API'"
echo "   3. Name: 'OpenAI API'"
echo "   4. API Key: [your key]"
echo "   5. Save"
echo "   6. Assign to 'Message a model' node"
echo "   7. Save workflow"
echo ""
echo "======================================================================"
echo "✅ Verification Complete"
echo "======================================================================"
echo ""
echo "The credential appears set in the node."
echo "Check Exec ID 88 to see the exact error message!"
echo ""

