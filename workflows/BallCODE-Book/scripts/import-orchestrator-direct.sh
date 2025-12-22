#!/bin/bash
# Direct CLI import of Unity Build Orchestrator
# Usage: ./scripts/import-orchestrator-direct.sh YOUR_API_KEY

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

PI_N8N_URL="http://192.168.1.226:5678"
WORKFLOW_FILE="n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE-IMPORTABLE.json"
API_KEY="$1"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

if [ -z "$API_KEY" ]; then
    echo -e "${YELLOW}⚠️  API key required${NC}"
    echo ""
    echo "Usage: ./scripts/import-orchestrator-direct.sh YOUR_API_KEY"
    echo ""
    echo "To get API key:"
    echo "1. Open: $PI_N8N_URL"
    echo "2. Settings → API → Create API Key"
    echo "3. Copy the key"
    echo "4. Run: ./scripts/import-orchestrator-direct.sh YOUR_KEY"
    exit 1
fi

if [ ! -f "$WORKFLOW_FILE" ]; then
    echo -e "${RED}❌ Workflow file not found: $WORKFLOW_FILE${NC}"
    exit 1
fi

echo -e "${BLUE}🚀 Importing Unity Build Orchestrator via CLI...${NC}"
echo ""

RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$WORKFLOW_FILE")

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ SUCCESS! Workflow imported via CLI${NC}"
    echo ""
    echo "Response:"
    echo "$BODY" | python3 -m json.tool 2>/dev/null | head -30 || echo "$BODY" | head -15
    echo ""
    echo -e "${YELLOW}📝 Next steps:${NC}"
    echo "1. Open n8n: $PI_N8N_URL"
    echo "2. Find the imported workflow: 'AIMCODE (Demis) - Unity Build Orchestrator (13 nodes, MAC GUARDED)'"
    echo "3. Activate it (toggle switch)"
    echo "4. Configure credentials (GitHub Actions Token, Netlify API Token)"
else
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo ""
    echo "Response:"
    echo "$BODY" | head -10
    echo ""
    if [ "$HTTP_CODE" = "401" ]; then
        echo -e "${YELLOW}💡 Authentication failed - check your API key${NC}"
    elif [ "$HTTP_CODE" = "400" ]; then
        echo -e "${YELLOW}💡 Bad request - check workflow file format${NC}"
    fi
    exit 1
fi


