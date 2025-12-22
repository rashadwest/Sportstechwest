#!/bin/bash

# Trigger n8n Webhook for Unity Build
# Usage: ./scripts/trigger-webhook.sh [request message]

REQUEST="${1:-Test build trigger from terminal}"

echo "🚀 Triggering n8n Webhook..."
echo "Request: $REQUEST"
echo ""

# Use Pi n8n instance
N8N_URL="http://192.168.1.226:5678"
if curl -s "${N8N_URL}/healthz" > /dev/null 2>&1; then
    echo "📍 Using: Raspberry Pi (192.168.1.226)"
else
    echo "❌ Pi n8n not accessible at ${N8N_URL}"
    exit 1
fi

echo ""
echo "📤 Sending webhook request..."
echo ""

# Try production URL first, fallback to test URL
RESPONSE=$(curl -s -X POST "${N8N_URL}/webhook/unity-build" \
  -H 'Content-Type: application/json' \
  -d "{\"request\": \"$REQUEST\"}")

# If production URL fails, try test URL
if echo "$RESPONSE" | grep -q "not registered"; then
    echo "⚠️  Production webhook not registered, trying test URL..."
    RESPONSE=$(curl -s -X POST "${N8N_URL}/webhook-test/unity-build" \
      -H 'Content-Type: application/json' \
      -d "{\"request\": \"$REQUEST\"}")
fi

# Check if response contains error
if echo "$RESPONSE" | grep -q "not registered"; then
    echo "❌ ERROR: Webhook not registered"
    echo ""
    echo "⚠️  The workflow must be ACTIVE for the production webhook to work!"
    echo ""
    echo "To fix:"
    echo "1. Open n8n: $N8N_URL"
    echo "2. Find workflow: 'AIMCODE (Demis) - Unity Build Orchestrator'"
    echo "3. Click the 'Active' toggle (top-right) to turn it ON"
    echo "4. Then run this script again"
    echo ""
    exit 1
elif echo "$RESPONSE" | grep -q "\"code\""; then
    echo "❌ Error response:"
    echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
    exit 1
elif echo "$RESPONSE" | grep -q "Workflow was started"; then
    echo "✅ Webhook triggered successfully! (using test URL)"
    echo ""
    echo "Response:"
    echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
    echo ""
    echo "💡 Check n8n Executions tab to see the workflow run"
    echo "   $N8N_URL"
    echo ""
    echo "⚠️  Note: Using test URL. Activate workflow for production URL."
else
    echo "✅ Webhook triggered successfully!"
    echo ""
    echo "Response:"
    echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
    echo ""
    echo "💡 Check n8n Executions tab to see the workflow run"
    echo "   $N8N_URL"
fi

