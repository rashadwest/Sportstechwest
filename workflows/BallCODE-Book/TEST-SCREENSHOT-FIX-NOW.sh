#!/bin/bash
# Quick Test: Screenshot-to-Fix Webhook
# Tests the webhook with sample data

# Copyright © 2025 Rashad West. All Rights Reserved.

N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"

echo "🧪 Testing Screenshot-to-Fix Webhook..."
echo "URL: ${N8N_URL}/webhook-test/screenshot-fix"
echo ""

# Test with placeholder image URL
curl -X POST "${N8N_URL}/webhook-test/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://via.placeholder.com/800x600.png?text=Test+Error+Screenshot",
    "context": "Test error - n8n workflow import issue"
  }' | python3 -m json.tool

echo ""
echo "✅ Test complete!"

