#!/bin/bash
# Import n8n workflow to Pi - Handles API key or uses UI instructions
# Usage: ./scripts/import-workflow-to-pi.sh <workflow.json>

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

WORKFLOW_FILE="$1"
PI_N8N_URL="http://192.168.1.226:5678"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

if [ -z "$WORKFLOW_FILE" ]; then
    echo -e "${RED}❌ Error: Workflow file required${NC}"
    echo "Usage: ./scripts/import-workflow-to-pi.sh <workflow.json>"
    exit 1
fi

if [ ! -f "$WORKFLOW_FILE" ]; then
    echo -e "${RED}❌ Error: File not found: $WORKFLOW_FILE${NC}"
    exit 1
fi

echo -e "${BLUE}🚀 Importing workflow to Pi n8n...${NC}"
echo ""

# Check for API key
if [ -f .n8n-env ]; then
    source .n8n-env 2>/dev/null
fi

# Try API import if key is available
if [ -n "$N8N_API_KEY" ] && [ "$N8N_API_KEY" != "" ]; then
    echo -e "${GREEN}✅ API key found - attempting API import...${NC}"
    echo ""
    
    RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
      -H "X-N8N-API-KEY: $N8N_API_KEY" \
      -H "Content-Type: application/json" \
      -d @"$WORKFLOW_FILE")
    
    HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
    BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')
    
    if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
        echo -e "${GREEN}✅ Workflow imported successfully via API!${NC}"
        echo ""
        echo "Response:"
        echo "$BODY" | python3 -m json.tool 2>/dev/null | head -30 || echo "$BODY" | head -30
        echo ""
        echo -e "${GREEN}Next steps:${NC}"
        echo "1. Open n8n: $PI_N8N_URL"
        echo "2. Find the imported workflow"
        echo "3. Activate it (toggle switch)"
        exit 0
    else
        echo -e "${YELLOW}⚠️  API import failed (HTTP $HTTP_CODE)${NC}"
        echo "Response: $BODY" | head -5
        echo ""
        echo "Falling back to UI import instructions..."
        echo ""
    fi
else
    echo -e "${YELLOW}⚠️  No API key configured${NC}"
    echo ""
fi

# Provide UI import instructions
echo -e "${BLUE}📋 UI Import Instructions (No API Key Needed):${NC}"
echo ""
echo "1. Open Pi n8n in browser:"
echo "   $PI_N8N_URL"
echo ""
echo "2. Click 'Workflows' in left sidebar"
echo ""
echo "3. Click 'Import from File' button (top right)"
echo ""
echo "4. Select this file:"
echo "   $(realpath "$WORKFLOW_FILE")"
echo ""
echo "5. Click 'Import'"
echo ""
echo "6. After import, activate the workflow:"
echo "   - Open the workflow"
echo "   - Toggle 'Active' switch ON (top-right)"
echo ""
echo -e "${GREEN}✅ Workflow file is ready for import!${NC}"
echo ""


