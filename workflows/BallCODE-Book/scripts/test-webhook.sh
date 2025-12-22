#!/bin/bash
# Test Single Webhook - Quick Terminal Test
# Usage: ./test-webhook.sh <webhook-name> [n8n-url]

# Copyright © 2025 Rashad West. All Rights Reserved.

WEBHOOK_NAME="$1"
N8N_URL="${2:-${N8N_URL:-http://localhost:5678}}"

if [ -z "$WEBHOOK_NAME" ]; then
    echo "Usage: ./test-webhook.sh <webhook-name> [n8n-url]"
    echo ""
    echo "Available webhooks:"
    echo "  - unity-build"
    echo "  - ballcode-dev"
    echo "  - screenshot-fix"
    exit 1
fi

# Test data for each webhook
case "$WEBHOOK_NAME" in
    "unity-build")
        DATA='{"request": "Test build", "branch": "main"}'
        ;;
    "ballcode-dev")
        DATA='{"prompt": "Test AI analysis", "mode": "quick"}'
        ;;
    "screenshot-fix")
        DATA='{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}'
        ;;
    *)
        echo "Unknown webhook: $WEBHOOK_NAME"
        exit 1
        ;;
esac

echo "Testing webhook: $WEBHOOK_NAME"
echo "URL: ${N8N_URL}/webhook/${WEBHOOK_NAME}"
echo ""

RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/${WEBHOOK_NAME}" \
  -H "Content-Type: application/json" \
  -d "$DATA")

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

echo "HTTP Status: $HTTP_CODE"
echo "Response:"
echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"


