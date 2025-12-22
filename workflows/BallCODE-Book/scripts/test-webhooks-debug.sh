#!/bin/bash
# Test All Webhooks with Full Debugging
# Shows detailed responses and errors

# Copyright © 2025 Rashad West. All Rights Reserved.

PI_URL="http://192.168.1.226:5678"

echo "🧪 Testing All Webhooks on Pi with Full Debugging"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Test 1: Screenshot Fix
echo "1️⃣  Screenshot Fix Webhook"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "URL: ${PI_URL}/webhook/screenshot-fix"
echo ""
RESPONSE=$(curl -s -w "\nHTTP_STATUS:%{http_code}\nTIME:%{time_total}" -X POST "${PI_URL}/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}')

HTTP_STATUS=$(echo "$RESPONSE" | grep "HTTP_STATUS" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_STATUS/d' | sed '/TIME/d')

echo "HTTP Status: $HTTP_STATUS"
echo "Response Body:"
echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Test 2: Full Integration
echo "2️⃣  Full Integration Webhook"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "URL: ${PI_URL}/webhook/ballcode-dev"
echo ""
RESPONSE=$(curl -s -w "\nHTTP_STATUS:%{http_code}\nTIME:%{time_total}" -X POST "${PI_URL}/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test AI analysis", "mode": "quick"}')

HTTP_STATUS=$(echo "$RESPONSE" | grep "HTTP_STATUS" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_STATUS/d' | sed '/TIME/d')

echo "HTTP Status: $HTTP_STATUS"
echo "Response Body:"
echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Test 3: Unity Build
echo "3️⃣  Unity Build Webhook"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "URL: ${PI_URL}/webhook/unity-build"
echo ""
RESPONSE=$(curl -s -w "\nHTTP_STATUS:%{http_code}\nTIME:%{time_total}" -X POST "${PI_URL}/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}')

HTTP_STATUS=$(echo "$RESPONSE" | grep "HTTP_STATUS" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_STATUS/d' | sed '/TIME/d')

echo "HTTP Status: $HTTP_STATUS"
echo "Response Body:"
echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Testing Complete"
echo ""
echo "📋 Summary:"
echo "  - Check HTTP status codes (200/201 = success, 404 = not found, 500 = error)"
echo "  - Check response bodies for error messages"
echo "  - If 404: Webhook not registered (workflow not active or path mismatch)"
echo "  - If 500: Workflow execution error (check n8n Executions tab)"
echo "  - If empty: Workflow running but no response (check Respond node)"


