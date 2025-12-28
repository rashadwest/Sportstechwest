#!/bin/bash
# Import Unity Build Orchestrator Workflow via n8n API
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuration
N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"
N8N_API_KEY="${N8N_API_KEY:-}"
WORKFLOW_FILE="${1:-../n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json}"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📥 Import Unity Build Orchestrator Workflow${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if workflow file exists
if [ ! -f "$WORKFLOW_FILE" ]; then
    echo -e "${RED}❌ Workflow file not found: $WORKFLOW_FILE${NC}"
    exit 1
fi

echo -e "${YELLOW}📄 Workflow file: $WORKFLOW_FILE${NC}"
echo -e "${YELLOW}🌐 n8n URL: $N8N_URL${NC}"
echo ""

# Check if API key is set
if [ -z "$N8N_API_KEY" ]; then
    echo -e "${YELLOW}⚠️  N8N_API_KEY not set. Trying without authentication...${NC}"
    echo -e "${YELLOW}   (If this fails, set N8N_API_KEY environment variable)${NC}"
    echo ""
    AUTH_HEADER=""
else
    AUTH_HEADER="-H \"X-N8N-API-KEY: $N8N_API_KEY\""
fi

# Method 1: Try n8n CLI if available
if command -v n8n &> /dev/null; then
    echo -e "${BLUE}Method 1: Using n8n CLI...${NC}"
    n8n import:workflow --input="$WORKFLOW_FILE" --host="$N8N_URL" && {
        echo -e "${GREEN}✅ Workflow imported via CLI${NC}"
        exit 0
    } || echo -e "${YELLOW}⚠️  CLI method failed, trying API...${NC}"
    echo ""
fi

# Method 2: Use n8n API
echo -e "${BLUE}Method 2: Using n8n API...${NC}"

# Read workflow JSON
WORKFLOW_JSON=$(cat "$WORKFLOW_FILE")

# Prepare payload (n8n expects workflow in 'workflow' field)
PAYLOAD=$(cat <<EOF
{
  "name": "$(echo "$WORKFLOW_JSON" | jq -r '.name // "Unity Build Orchestrator"')",
  "nodes": $(echo "$WORKFLOW_JSON" | jq -c '.nodes'),
  "connections": $(echo "$WORKFLOW_JSON" | jq -c '.connections'),
  "settings": $(echo "$WORKFLOW_JSON" | jq -c '.settings // {}'),
  "staticData": $(echo "$WORKFLOW_JSON" | jq -c '.staticData // null'),
  "tags": $(echo "$WORKFLOW_JSON" | jq -c '.tags // []')
}
EOF
)

# Import workflow
echo -e "${YELLOW}Uploading workflow to n8n...${NC}"

if [ -z "$N8N_API_KEY" ]; then
    RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST \
        "${N8N_URL}/api/v1/workflows" \
        -H "Content-Type: application/json" \
        -d "$PAYLOAD" 2>&1)
else
    RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST \
        "${N8N_URL}/api/v1/workflows" \
        -H "Content-Type: application/json" \
        -H "X-N8N-API-KEY: $N8N_API_KEY" \
        -d "$PAYLOAD" 2>&1)
fi

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Workflow imported successfully!${NC}"
    echo ""
    echo -e "${BLUE}Workflow ID:${NC}"
    echo "$BODY" | jq -r '.id // .data.id // "N/A"' 2>/dev/null || echo "Check n8n UI"
    echo ""
    echo -e "${YELLOW}⚠️  IMPORTANT: Activate the workflow in n8n UI:${NC}"
    echo -e "   1. Go to: ${N8N_URL}"
    echo -e "   2. Find: Unity Build Orchestrator"
    echo -e "   3. Click 'Active' toggle (top-right)"
    echo ""
else
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo ""
    echo -e "${YELLOW}Response:${NC}"
    echo "$BODY" | head -20
    echo ""
    echo -e "${YELLOW}💡 Try:${NC}"
    echo -e "   1. Check n8n is running: curl ${N8N_URL}/healthz"
    echo -e "   2. Set N8N_API_KEY if authentication required"
    echo -e "   3. Import manually via n8n UI"
    exit 1
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Import Complete${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"


