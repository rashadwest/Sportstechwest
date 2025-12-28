#!/bin/bash
# Delete All Orchestrator Workflows and Re-import Clean Version
# Fixes "Could not find workflow" + "Could not find property option" errors

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

PI_N8N_URL="http://192.168.1.226:5678"
WORKFLOW_FILE="n8n-unity-build-orchestrator-CLEANED-UI-IMPORT.json"

if [ -f .n8n-env.pi ]; then
    source .n8n-env.pi 2>/dev/null
fi

if [ -z "$N8N_API_KEY" ]; then
    echo -e "${RED}❌ N8N_API_KEY not set${NC}"
    exit 1
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🗑️  Delete All Orchestrator Workflows & Re-import${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${CYAN}Step 1: Finding all orchestrator workflows...${NC}"
WORKFLOWS_JSON=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows" -H "X-N8N-API-KEY: $N8N_API_KEY")

ORCHESTRATOR_IDS=$(echo "$WORKFLOWS_JSON" | python3 -c "
import sys, json
data = json.load(sys.stdin)
workflows = [w for w in data.get('data', []) if 'orchestrator' in w.get('name', '').lower() and '13 nodes' in w.get('name', '')]
ids = [w.get('id') for w in workflows]
print('\n'.join(ids))
" 2>/dev/null)

COUNT=$(echo "$ORCHESTRATOR_IDS" | grep -v '^$' | wc -l | tr -d ' ')

if [ "$COUNT" -gt 0 ]; then
    echo -e "${YELLOW}Found $COUNT orchestrator workflows to delete${NC}"
    echo ""
    
    echo -e "${CYAN}Step 2: Deleting all orchestrator workflows...${NC}"
    DELETED=0
    for ID in $ORCHESTRATOR_IDS; do
        if [ -n "$ID" ]; then
            HTTP_CODE=$(curl -s -w "%{http_code}" -o /dev/null -X DELETE "${PI_N8N_URL}/api/v1/workflows/$ID" -H "X-N8N-API-KEY: $N8N_API_KEY")
            if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "204" ]; then
                echo -e "  ${GREEN}✅ Deleted: $ID${NC}"
                DELETED=$((DELETED + 1))
            fi
        fi
    done
    echo -e "${GREEN}Deleted $DELETED workflows${NC}"
    echo ""
fi

echo -e "${CYAN}Step 3: Creating cleaned workflow...${NC}"
if [ ! -f "$WORKFLOW_FILE" ]; then
    python3 scripts/clean-workflow-for-api.py \
      n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json \
      "$WORKFLOW_FILE" 2>&1
fi

echo -e "${CYAN}Step 4: Importing clean workflow...${NC}"
IMPORT_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$WORKFLOW_FILE" 2>&1)

HTTP_CODE=$(echo "$IMPORT_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2 || echo "000")
BODY=$(echo "$IMPORT_RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    NEW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
    echo -e "${GREEN}✅ SUCCESS! Workflow imported${NC}"
    echo "   ID: $NEW_ID"
    echo ""
    echo -e "${CYAN}Next: Open n8n UI and try to load the workflow${NC}"
    echo "   URL: $PI_N8N_URL"
else
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo "$BODY" | head -5
fi


