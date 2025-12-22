#!/bin/bash
# Test OpenAI API Key - Verify Credentials Work

# Copyright © 2025 Rashad West. All Rights Reserved.

echo "🔍 Testing OpenAI API Key..."
echo ""

# Get API key from user
read -p "Enter your OpenAI API key (sk-proj-...): " API_KEY

if [ -z "$API_KEY" ]; then
    echo "❌ No API key provided"
    exit 1
fi

echo ""
echo "Testing API key..."
echo ""

# Test 1: List models (simple test)
echo "Test 1: List available models..."
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  https://api.openai.com/v1/models)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

echo "HTTP Status: $HTTP_CODE"
echo ""

if [ "$HTTP_CODE" = "200" ]; then
    echo "✅ API Key is VALID and working!"
    echo ""
    echo "Available models (first 3):"
    echo "$BODY" | python3 -m json.tool 2>/dev/null | grep -A 2 '"id"' | head -10 || echo "$BODY" | head -20
elif [ "$HTTP_CODE" = "401" ]; then
    echo "❌ API Key is INVALID or expired"
    echo ""
    echo "Check:"
    echo "1. Key starts with 'sk-proj-' or 'sk-'"
    echo "2. Key is not expired"
    echo "3. Key has proper permissions"
    echo ""
    echo "Get new key: https://platform.openai.com/api-keys"
elif [ "$HTTP_CODE" = "429" ]; then
    echo "⚠️  API Key is VALID but rate limited"
    echo ""
    echo "Your key works, but you're hitting rate limits."
    echo "Wait 5 minutes and try again."
    echo ""
    echo "Response:"
    echo "$BODY" | head -10
else
    echo "⚠️  Unexpected response: HTTP $HTTP_CODE"
    echo ""
    echo "Response:"
    echo "$BODY" | head -20
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Test 2: Check account status
echo "Test 2: Check account usage..."
echo "Visit: https://platform.openai.com/usage"
echo ""

# Test 3: Check rate limits
echo "Test 3: Check rate limits..."
echo "Visit: https://platform.openai.com/account/limits"
echo ""

echo "✅ Test complete!"

