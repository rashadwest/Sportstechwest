#!/bin/bash
# Push Orchestrator Workflow via CLI - V2 (Based on Successful Imports)
# Uses research-based cleaning and proven import method

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

PI_N8N_URL="http://192.168.1.226:5678"
SOURCE_FILE="n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"
CLEANED_FILE="n8n-unity-build-orchestrator-API-READY-V2.json"

if [ -f .n8n-env.pi ]; then
    source .n8n-env.pi 2>/dev/null
fi

if [ -z "$N8N_API_KEY" ]; then
    echo -e "${RED}❌ N8N_API_KEY not set${NC}"
    exit 1
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 Push Orchestrator Workflow via CLI - V2${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Step 1: Delete existing orchestrators
echo -e "${CYAN}Step 1: Cleaning up existing orchestrator workflows...${NC}"
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
    DELETED=0
    for ID in $ORCHESTRATOR_IDS; do
        if [ -n "$ID" ]; then
            HTTP_CODE=$(curl -s -w "%{http_code}" -o /dev/null -X DELETE "${PI_N8N_URL}/api/v1/workflows/$ID" -H "X-N8N-API-KEY: $N8N_API_KEY")
            if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "204" ]; then
                DELETED=$((DELETED + 1))
            fi
        fi
    done
    echo -e "${GREEN}✅ Deleted $DELETED workflows${NC}"
    echo ""
fi

# Step 2: Clean workflow using V2 cleaner
echo -e "${CYAN}Step 2: Cleaning workflow for API import (V2)...${NC}"
if [ ! -f "$SOURCE_FILE" ]; then
    echo -e "${RED}❌ Source file not found: $SOURCE_FILE${NC}"
    exit 1
fi

python3 scripts/clean-workflow-for-api-v2.py "$SOURCE_FILE" "$CLEANED_FILE" 2>&1

if [ ! -f "$CLEANED_FILE" ]; then
    echo -e "${RED}❌ Failed to create cleaned workflow${NC}"
    exit 1
fi

# Verify cleaned file has 13 nodes
NODE_COUNT=$(python3 -c "import json; w=json.load(open('$CLEANED_FILE')); print(len(w.get('nodes', [])))" 2>/dev/null || echo "0")
if [ "$NODE_COUNT" != "13" ]; then
    echo -e "${RED}❌ ERROR: Cleaned workflow has $NODE_COUNT nodes (expected 13)${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Cleaned workflow ready (13 nodes)${NC}"
echo ""

# Step 3: Import via API
echo -e "${CYAN}Step 3: Importing workflow via API...${NC}"
IMPORT_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$CLEANED_FILE" 2>&1)

HTTP_CODE=$(echo "$IMPORT_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2 || echo "000")
BODY=$(echo "$IMPORT_RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    NEW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
    NEW_NAME=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('name', ''))" 2>/dev/null || echo "")
    
    echo -e "${GREEN}✅ SUCCESS! Workflow imported${NC}"
    echo "   ID: $NEW_ID"
    echo "   Name: $NEW_NAME"
    echo ""
    
    # Verify imported workflow
    VERIFY_RESPONSE=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows/$NEW_ID" -H "X-N8N-API-KEY: $N8N_API_KEY" 2>/dev/null)
    IMPORTED_NODES=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('nodes', [])))" 2>/dev/null || echo "?")
    
    if [ "$IMPORTED_NODES" = "13" ]; then
        echo -e "${GREEN}✅ Verified: Imported workflow has 13 nodes${NC}"
    else
        echo -e "${YELLOW}⚠️  Warning: Imported workflow has $IMPORTED_NODES nodes${NC}"
    fi
    echo ""
    
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}📋 NEXT STEPS${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${CYAN}1. Open n8n UI:${NC} $PI_N8N_URL"
    echo ""
    echo -e "${CYAN}2. Find workflow:${NC} $NEW_NAME"
    echo ""
    echo -e "${CYAN}3. Click to open it${NC}"
    echo "   - If it loads → Problem solved!"
    echo "   - If blank → Try hard refresh (Cmd+Shift+R)"
    echo ""
    echo -e "${CYAN}4. Activate workflow:${NC}"
    echo "   - Toggle 'Active' switch ON"
    echo ""
    
else
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo ""
    echo "Response:"
    echo "$BODY" | head -10
    echo ""
    echo -e "${YELLOW}💡 If API import fails, try UI import:${NC}"
    echo "   1. Open n8n: $PI_N8N_URL"
    echo "   2. Workflows → Import from File"
    echo "   3. Select: $(pwd)/$CLEANED_FILE"
    exit 1
fi

echo ""
echo -e "${GREEN}✅ Process complete!${NC}"
echo ""

