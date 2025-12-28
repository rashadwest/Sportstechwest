#!/bin/bash

# Check Unity Build Workflow Status
# Checks if workflow is locked and shows current status

N8N_URL="${N8N_BASE_URL:-http://192.168.1.226:5678}"
WEBHOOK_PATH="/webhook/unity-build"

echo "============================================================"
echo "Checking Unity Build Workflow Status"
echo "============================================================"
echo ""

# Test the webhook
echo "Sending test request..."
RESPONSE=$(curl -s -X POST "$N8N_URL$WEBHOOK_PATH" \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Status check",
    "branch": "main"
  }')

echo ""
echo "Response:"
echo "$RESPONSE" | jq '.' 2>/dev/null || echo "$RESPONSE"
echo ""

# Parse status
STATUS=$(echo "$RESPONSE" | jq -r '.status' 2>/dev/null || echo "unknown")
MESSAGE=$(echo "$RESPONSE" | jq -r '.message' 2>/dev/null || echo "")

echo "Status: $STATUS"
echo ""

if [ "$STATUS" = "skipped" ]; then
  if echo "$MESSAGE" | grep -q "Locked"; then
    LOCK_UNTIL=$(echo "$MESSAGE" | grep -oP 'until \K[^ ]+' || echo "unknown")
    echo "⚠️  Workflow is LOCKED"
    echo "Lock expires at: $LOCK_UNTIL"
    echo ""
    echo "This means a build is currently running or recently completed."
    echo "Check n8n UI for execution details."
    echo ""
    echo "Next steps:"
    echo "1. Go to n8n UI → Executions"
    echo "2. Look for recent execution"
    echo "3. Wait for it to complete"
    echo "4. Try again after lock clears"
  else
    echo "⚠️  Workflow was skipped"
    echo "Reason: $MESSAGE"
  fi
elif [ "$STATUS" = "ok" ]; then
  echo "✅ Workflow executed successfully!"
  echo ""
  GITHUB_STATUS=$(echo "$RESPONSE" | jq -r '.github.status' 2>/dev/null || echo "unknown")
  NETLIFY_STATE=$(echo "$RESPONSE" | jq -r '.netlify.state' 2>/dev/null || echo "unknown")
  echo "GitHub Status: $GITHUB_STATUS"
  echo "Netlify State: $NETLIFY_STATE"
elif [ "$STATUS" = "fail" ]; then
  echo "❌ Workflow failed"
  ERROR=$(echo "$RESPONSE" | jq -r '.error' 2>/dev/null || echo "unknown")
  echo "Error: $ERROR"
else
  echo "ℹ️  Status: $STATUS"
  echo "Message: $MESSAGE"
fi

echo ""
echo "============================================================"


