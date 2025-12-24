#!/bin/bash
# Test Full Integration workflow end-to-end

N8N_URL="${N8N_BASE_URL:-http://192.168.1.226:5678}"
WEBHOOK_PATH="/webhook/ballcode-dev"

echo "🧪 Testing Full Integration workflow end-to-end..."
echo "📍 n8n URL: $N8N_URL"
echo "🔗 Webhook: $WEBHOOK_PATH"

# Test prompt
TEST_PROMPT='{
  "prompt": "Test Full Integration: Update Book 1 with a new exercise button",
  "mode": "quick",
  "sessionId": "test-'$(date +%s)'"
}'

echo ""
echo "📤 Sending test request..."
echo "Prompt: Test Full Integration: Update Book 1 with a new exercise button"
echo ""

RESPONSE=$(curl -s -X POST "$N8N_URL$WEBHOOK_PATH" \
    -H "Content-Type: application/json" \
    -d "$TEST_PROMPT" \
    -w "\nHTTP_CODE:%{http_code}")

HTTP_CODE=$(echo "$RESPONSE" | grep -o "HTTP_CODE:[0-9]*" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed 's/HTTP_CODE:[0-9]*$//')

echo "📥 Response:"
echo "HTTP Status: $HTTP_CODE"
echo ""

if [ "$HTTP_CODE" = "200" ]; then
    echo "✅ Workflow executed successfully!"
    echo ""
    echo "Response body:"
    echo "$BODY" | jq '.' 2>/dev/null || echo "$BODY"
    echo ""
    echo "📋 Check n8n executions for detailed logs:"
    echo "   $N8N_URL/executions"
else
    echo "❌ Workflow execution failed!"
    echo "HTTP Status: $HTTP_CODE"
    echo "Response:"
    echo "$BODY"
    exit 1
fi

