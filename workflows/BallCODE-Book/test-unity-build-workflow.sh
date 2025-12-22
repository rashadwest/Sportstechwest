#!/bin/bash

# Test Unity Build Workflow
# Tests the n8n Unity Build Orchestrator workflow

set -e

N8N_URL="${N8N_BASE_URL:-http://192.168.1.226:5678}"
WEBHOOK_PATH="/webhook/unity-build"

echo "============================================================"
echo "Testing Unity Build Workflow"
echo "============================================================"
echo ""
echo "n8n URL: $N8N_URL"
echo "Webhook: $WEBHOOK_PATH"
echo ""

# Test 1: Basic webhook call
echo "Test 1: Basic webhook call..."
echo "Sending POST request to trigger workflow..."
echo ""

RESPONSE=$(curl -s -w "\nHTTP_STATUS:%{http_code}" -X POST "$N8N_URL$WEBHOOK_PATH" \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Test build from script",
    "branch": "main",
    "triggerType": "test"
  }')

HTTP_STATUS=$(echo "$RESPONSE" | grep "HTTP_STATUS" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_STATUS/d')

echo "HTTP Status: $HTTP_STATUS"
echo ""
echo "Response:"
echo "$BODY" | jq '.' 2>/dev/null || echo "$BODY"
echo ""

if [ "$HTTP_STATUS" = "200" ]; then
  echo "✅ Webhook call succeeded!"
  
  # Check response for errors
  if echo "$BODY" | grep -q '"status":"fail"'; then
    echo "⚠️  Workflow executed but reported an error"
    echo "Check the response above for details"
  elif echo "$BODY" | grep -q '"status":"skipped"'; then
    echo "ℹ️  Workflow was skipped (check skipReason in response)"
  elif echo "$BODY" | grep -q '"status":"ok"'; then
    echo "✅ Workflow executed successfully!"
  fi
else
  echo "❌ Webhook call failed with status $HTTP_STATUS"
  echo "Check n8n workflow is active and webhook path is correct"
fi

echo ""
echo "============================================================"
echo "Next Steps:"
echo "1. Check n8n UI for execution details"
echo "2. Look for any credential errors"
echo "3. Verify GitHub Actions was triggered"
echo "4. Check Netlify deployment status"
echo "============================================================"

