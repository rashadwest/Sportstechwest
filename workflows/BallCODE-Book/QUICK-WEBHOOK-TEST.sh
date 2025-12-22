#!/bin/bash
# Quick Webhook Test Script
# Tests orchestrator webhook and shows status

cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env.pi 2>/dev/null

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🧪 ORCHESTRATOR WEBHOOK TEST"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check workflow status
echo "1️⃣  Checking workflow status..."
WORKFLOW_STATUS=$(curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  python3 -c "
import sys, json
data = json.load(sys.stdin)
workflows = [w for w in data.get('data', []) if 'orchestrator' in w.get('name', '').lower() and '13 nodes' in w.get('name', '')]
if workflows:
    wf = workflows[0]
    print(f\"{'ACTIVE' if wf.get('active') else 'INACTIVE'}\")
else:
    print('NOT_FOUND')
" 2>/dev/null)

if [ "$WORKFLOW_STATUS" = "INACTIVE" ]; then
    echo "   ⚠️  Workflow is INACTIVE"
    echo "   → Activate it in n8n UI first!"
    echo ""
    exit 1
elif [ "$WORKFLOW_STATUS" = "ACTIVE" ]; then
    echo "   ✅ Workflow is ACTIVE"
else
    echo "   ❌ Workflow not found"
    exit 1
fi

echo ""

# Test webhook
echo "2️⃣  Testing webhook..."
RESPONSE=$(curl -s -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}' \
  -w "\nHTTP_CODE:%{http_code}")

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

echo "   HTTP Code: $HTTP_CODE"
echo ""

if [ "$HTTP_CODE" = "200" ]; then
    if [ -z "$BODY" ] || [ "$BODY" = "{}" ] || [ "$BODY" = "" ]; then
        echo "   ⚠️  Empty response (workflow may have errors)"
        echo "   → Check n8n Executions tab for details"
    else
        echo "   ✅ Response received:"
        echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
    fi
else
    echo "   ❌ Error: HTTP $HTTP_CODE"
    echo "   Response: $BODY"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

