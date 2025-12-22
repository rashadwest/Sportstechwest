#!/bin/bash

# Deploy to Netlify via n8n Webhook
# Copyright © 2025 Rashad West. All Rights Reserved.

# Usage: ./deploy-via-n8n.sh [commit message]

N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"
COMMIT_MSG="${1:-Deploy to Netlify: $(date +'%Y-%m-%d %H:%M:%S')}"

echo "🚀 Deploying via n8n..."
echo "📝 Commit message: $COMMIT_MSG"
echo ""

RESPONSE=$(curl -s -X POST "$N8N_URL/webhook/deploy-netlify" \
  -H "Content-Type: application/json" \
  -d "{\"commitMessage\": \"$COMMIT_MSG\"}")

if echo "$RESPONSE" | grep -q "success"; then
    echo "✅ Deployment triggered successfully!"
    echo ""
    echo "📊 Response:"
    echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
    echo ""
    echo "⏳ Netlify will deploy in 1-3 minutes"
    echo "🌐 Check: https://ballcode.co"
else
    echo "❌ Deployment failed"
    echo "Response: $RESPONSE"
    exit 1
fi

