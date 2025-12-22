#!/bin/bash
# Import Unity Build Orchestrator - Fixed version
# Usage: ./scripts/import-orchestrator-now.sh YOUR_API_KEY

PI_N8N_URL="http://192.168.1.226:5678"
WORKFLOW_FILE="n8n-unity-build-orchestrator-SINGLE.json"
API_KEY="$1"

if [ -z "$API_KEY" ]; then
    echo "❌ API key required"
    echo ""
    echo "Usage: ./scripts/import-orchestrator-now.sh YOUR_API_KEY"
    echo ""
    echo "Get API key from: $PI_N8N_URL → Settings → API → Create API Key"
    exit 1
fi

if [ ! -f "$WORKFLOW_FILE" ]; then
    echo "❌ Workflow file not found: $WORKFLOW_FILE"
    exit 1
fi

echo "🚀 Importing Unity Build Orchestrator..."
echo ""

RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$WORKFLOW_FILE")

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo "✅ SUCCESS! Workflow imported"
    echo ""
    echo "$BODY" | python3 -m json.tool 2>/dev/null | head -20 || echo "$BODY" | head -10
    echo ""
    echo "Next: Open $PI_N8N_URL and activate the workflow"
else
    echo "❌ Import failed (HTTP $HTTP_CODE)"
    echo "$BODY" | head -5
    exit 1
fi
