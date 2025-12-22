#!/bin/bash

# End-to-End Test: Garvis → Unity Build → GitHub Actions → Netlify
# Tests the complete integration flow

set -e

N8N_URL="${N8N_BASE_URL:-http://192.168.1.226:5678}"

echo "============================================================"
echo "End-to-End Integration Test"
echo "============================================================"
echo ""
echo "Testing: Garvis → Unity Build → GitHub Actions → Netlify"
echo "n8n URL: $N8N_URL"
echo ""

# Test 1: Garvis Orchestrator
echo "Test 1: Garvis Orchestrator Webhook"
echo "-----------------------------------"
echo "Sending request to /webhook/garvis..."
echo ""

GARVIS_RESPONSE=$(curl -s -w "\nHTTP_STATUS:%{http_code}" -X POST "$N8N_URL/webhook/garvis" \
  -H "Content-Type: application/json" \
  -d '{
    "one_thing": "Build Unity game for testing",
    "tasks": ["build unity game"],
    "context": "End-to-end integration test",
    "job_id": "e2e-test-'$(date +%s)'"
  }')

GARVIS_HTTP=$(echo "$GARVIS_RESPONSE" | grep "HTTP_STATUS" | cut -d: -f2)
GARVIS_BODY=$(echo "$GARVIS_RESPONSE" | sed '/HTTP_STATUS/d')

echo "HTTP Status: $GARVIS_HTTP"
if [ "$GARVIS_HTTP" = "200" ]; then
  echo "✅ Garvis Orchestrator is responding"
  echo "Response:"
  echo "$GARVIS_BODY" | jq '.' 2>/dev/null || echo "$GARVIS_BODY"
else
  echo "⚠️  Garvis Orchestrator response: $GARVIS_HTTP"
  echo "Response: $GARVIS_BODY"
  echo ""
  echo "Note: If 404, workflow may not be active. Check n8n UI."
fi

echo ""
echo ""

# Test 2: Unity Build Webhook (direct)
echo "Test 2: Unity Build Webhook (Direct)"
echo "--------------------------------------"
echo "Sending request to /webhook/unity-build..."
echo ""

UNITY_RESPONSE=$(curl -s -w "\nHTTP_STATUS:%{http_code}" -X POST "$N8N_URL/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{
    "request": "End-to-end test build",
    "branch": "main"
  }')

UNITY_HTTP=$(echo "$UNITY_RESPONSE" | grep "HTTP_STATUS" | cut -d: -f2)
UNITY_BODY=$(echo "$UNITY_RESPONSE" | sed '/HTTP_STATUS/d')

echo "HTTP Status: $UNITY_HTTP"
if [ "$UNITY_HTTP" = "200" ]; then
  echo "✅ Unity Build webhook is responding"
  
  # Parse response
  STATUS=$(echo "$UNITY_BODY" | jq -r '.status' 2>/dev/null || echo "unknown")
  MESSAGE=$(echo "$UNITY_BODY" | jq -r '.message' 2>/dev/null || echo "")
  
  echo "Status: $STATUS"
  echo "Message: $MESSAGE"
  echo ""
  
  if [ "$STATUS" = "ok" ]; then
    echo "✅ Build dispatched successfully!"
    GITHUB_STATUS=$(echo "$UNITY_BODY" | jq -r '.github.status' 2>/dev/null || echo "unknown")
    NETLIFY_STATE=$(echo "$UNITY_BODY" | jq -r '.netlify.state' 2>/dev/null || echo "unknown")
    echo "GitHub Status: $GITHUB_STATUS"
    echo "Netlify State: $NETLIFY_STATE"
  elif [ "$STATUS" = "skipped" ]; then
    if echo "$MESSAGE" | grep -q "Locked"; then
      echo "ℹ️  Workflow is locked (previous build running)"
      echo "This is normal - check n8n UI for execution status"
    else
      echo "ℹ️  Workflow was skipped: $MESSAGE"
    fi
  elif [ "$STATUS" = "fail" ]; then
    ERROR=$(echo "$UNITY_BODY" | jq -r '.error' 2>/dev/null || echo "unknown")
    echo "❌ Build failed: $ERROR"
  fi
  
  echo ""
  echo "Full response:"
  echo "$UNITY_BODY" | jq '.' 2>/dev/null || echo "$UNITY_BODY"
else
  echo "❌ Unity Build webhook error: $UNITY_HTTP"
  echo "Response: $UNITY_BODY"
fi

echo ""
echo ""

# Test 3: Check GitHub Actions (if we can)
echo "Test 3: GitHub Actions Status"
echo "-----------------------------"
echo "Note: This requires checking GitHub API or web interface"
echo "Go to: https://github.com/rashadwest/BTEBallCODE/actions"
echo "Look for recent workflow runs triggered by the test above"
echo ""

# Test 4: Summary
echo "============================================================"
echo "Test Summary"
echo "============================================================"
echo ""
echo "✅ Garvis Orchestrator: $([ "$GARVIS_HTTP" = "200" ] && echo "Working" || echo "Check Status")"
echo "✅ Unity Build Webhook: $([ "$UNITY_HTTP" = "200" ] && echo "Working" || echo "Check Status")"
echo ""
echo "Next Steps:"
echo "1. Check n8n UI for execution details"
echo "2. Check GitHub Actions for build status"
echo "3. Check Netlify for deployment (when site is transferred)"
echo "4. Verify credentials worked (no errors in n8n execution)"
echo ""
echo "============================================================"

