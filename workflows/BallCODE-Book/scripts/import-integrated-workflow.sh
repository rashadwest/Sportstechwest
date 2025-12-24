#!/bin/bash
# Import integrated Full Integration workflow to n8n

N8N_URL="${N8N_BASE_URL:-http://192.168.1.226:5678}"
WORKFLOW_FILE="n8n-ballcode-full-integration-workflow-INTEGRATED.json"
WORKFLOW_NAME="BallCODE Full Integration - AI Development Workflow (INTEGRATED)"

echo "🚀 Importing integrated Full Integration workflow to n8n..."
echo "📍 n8n URL: $N8N_URL"
echo "📁 Workflow file: $WORKFLOW_FILE"

# Check if file exists
if [ ! -f "$WORKFLOW_FILE" ]; then
    echo "❌ Error: Workflow file not found: $WORKFLOW_FILE"
    exit 1
fi

# Import workflow via n8n API
echo "📤 Uploading workflow to n8n..."

RESPONSE=$(curl -s -X POST "$N8N_URL/api/v1/workflows" \
    -H "Content-Type: application/json" \
    -d @"$WORKFLOW_FILE")

# Check if import was successful
if echo "$RESPONSE" | grep -q '"id"'; then
    WORKFLOW_ID=$(echo "$RESPONSE" | grep -o '"id":"[^"]*' | head -1 | cut -d'"' -f4)
    echo "✅ Workflow imported successfully!"
    echo "🆔 Workflow ID: $WORKFLOW_ID"
    echo "🔗 View in n8n: $N8N_URL/workflow/$WORKFLOW_ID"
    echo ""
    echo "📋 Next steps:"
    echo "1. Activate the workflow in n8n UI"
    echo "2. Test with: curl -X POST $N8N_URL/webhook/ballcode-dev -d '{\"prompt\": \"Test Full Integration\"}'"
    echo "3. Monitor execution in n8n UI"
else
    echo "❌ Error importing workflow:"
    echo "$RESPONSE"
    exit 1
fi

