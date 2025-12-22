#!/bin/bash
# Test Only the Two Fixed Webhooks (Screenshot Fix & Full Integration)
# Excludes Unity Build Orchestrator

# Copyright © 2025 Rashad West. All Rights Reserved.

PI_URL="http://192.168.1.226:5678"

echo "🧪 Testing Fixed Webhooks (Screenshot Fix & Full Integration)"
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
if [ "$HTTP_STATUS" = "200" ]; then
    echo "✅ Status: OK"
else
    echo "❌ Status: Error"
fi
echo ""
echo "Response Body:"
if [ -z "$BODY" ]; then
    echo "  (Empty response)"
else
    echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
fi
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
if [ "$HTTP_STATUS" = "200" ]; then
    echo "✅ Status: OK"
else
    echo "❌ Status: Error"
fi
echo ""
echo "Response Body:"
if [ -z "$BODY" ]; then
    echo "  (Empty response)"
else
    echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
fi
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Testing Complete"
echo ""
echo "📋 Next Steps:"
echo "  - If you see empty responses, check n8n Executions tab"
echo "  - Look for red nodes (errors)"
echo "  - Most likely: OpenAI credentials need to be configured"


