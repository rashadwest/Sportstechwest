#!/bin/bash
# Test Screenshot-to-Fix Webhook
# Usage: bash TEST-SCREENSHOT-FIX-WEBHOOK.sh [image-url] [context]

N8N_URL="http://192.168.1.226:5678"
SCREENSHOT_URL="${1:-https://via.placeholder.com/800x600.png}"
CONTEXT="${2:-Test screenshot for debugging}"

echo "🧪 Testing Screenshot-to-Fix Webhook"
echo ""
echo "📡 URL: ${N8N_URL}/webhook/screenshot-fix"
echo "🖼️  Image: ${SCREENSHOT_URL}"
echo "📝 Context: ${CONTEXT}"
echo ""

response=$(curl -s -X POST "${N8N_URL}/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d "{\"screenshotUrl\": \"${SCREENSHOT_URL}\", \"context\": \"${CONTEXT}\"}" \
  -w "\nHTTP_CODE:%{http_code}")

http_code=$(echo "$response" | grep "HTTP_CODE:" | cut -d: -f2)
body=$(echo "$response" | sed '/HTTP_CODE:/d')

echo "Response:"
echo "$body"
echo ""
echo "Status Code: $http_code"
echo ""

if [ "$http_code" = "200" ]; then
    echo "✅ Webhook triggered successfully!"
    echo "   → Check n8n Executions tab for execution status"
    echo "   → Look for new execution (should succeed with real image URL)"
else
    echo "❌ Webhook returned error: $http_code"
    echo "   → Check n8n Executions tab for error details"
fi

echo ""
echo "💡 To test with your own image:"
echo "   bash TEST-SCREENSHOT-FIX-WEBHOOK.sh 'https://your-image-url.com/image.png' 'Your context'"

