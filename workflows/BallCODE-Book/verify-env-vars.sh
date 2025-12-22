#!/bin/bash

# Verify Environment Variables in Unity Build Workflow
# Tests if required env vars are accessible

N8N_URL="${N8N_BASE_URL:-http://192.168.1.226:5678}"
WEBHOOK_PATH="/webhook/unity-build"

echo "============================================================"
echo "Verifying Environment Variables"
echo "============================================================"
echo ""

# Test the webhook and check for env var errors
echo "Sending test request to check environment variables..."
echo ""

RESPONSE=$(curl -s -X POST "$N8N_URL$WEBHOOK_PATH" \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Env var check",
    "branch": "main"
  }')

echo "Response:"
echo "$RESPONSE" | jq '.' 2>/dev/null || echo "$RESPONSE"
echo ""

# Check for missing env var errors
if echo "$RESPONSE" | grep -q "Missing required env var"; then
  echo "❌ Environment Variables Missing!"
  echo ""
  MISSING=$(echo "$RESPONSE" | jq -r '.error' 2>/dev/null || echo "$RESPONSE" | grep -oP 'Missing required env var\(s\): \K[^"]*')
  echo "Missing variables: $MISSING"
  echo ""
  echo "Required variables:"
  echo "  - GITHUB_REPO_OWNER"
  echo "  - GITHUB_REPO_NAME"
  echo "  - GITHUB_WORKFLOW_FILE"
  echo "  - NETLIFY_SITE_ID (can be placeholder)"
  echo ""
  echo "Fix: Run robot-hardcode-env-vars.py to set them"
elif echo "$RESPONSE" | grep -q '"status":"fail"'; then
  echo "⚠️  Workflow failed (check error message above)"
elif echo "$RESPONSE" | grep -q '"status":"skipped"'; then
  echo "ℹ️  Workflow was skipped (likely locked)"
  echo "This is OK - it means env vars are set correctly"
  echo "Check the message for skip reason"
elif echo "$RESPONSE" | grep -q '"status":"ok"'; then
  echo "✅ Environment Variables are set correctly!"
  echo "✅ Workflow executed successfully!"
else
  echo "⚠️  Could not determine status"
  echo "Check n8n UI for execution details"
fi

echo ""
echo "============================================================"

