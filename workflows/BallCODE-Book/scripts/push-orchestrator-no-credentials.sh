#!/bin/bash
# Push Orchestrator Workflow WITHOUT Credentials
# Fixes workflow that shows for a second then reverts to blank

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

PI_N8N_URL="http://192.168.1.226:5678"
SOURCE_FILE="n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"
NO_CREDS_FILE="n8n-unity-build-orchestrator-NO-CREDENTIALS.json"

if [ -f .n8n-env.pi ]; then
    source .n8n-env.pi 2>/dev/null
fi

if [ -z "$N8N_API_KEY" ]; then
    echo -e "${RED}❌ N8N_API_KEY not set${NC}"
    exit 1
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 Push Orchestrator (No Credentials) - Fixes UI Revert${NC}"
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

# Step 2: Create workflow without credentials
echo -e "${CYAN}Step 2: Creating workflow WITHOUT credentials...${NC}"
if [ ! -f "$SOURCE_FILE" ]; then
    echo -e "${RED}❌ Source file not found: $SOURCE_FILE${NC}"
    exit 1
fi

python3 -c "
import json

with open('$SOURCE_FILE', 'r') as f:
    wf = json.load(f)

# Remove credentials from all nodes
for node in wf.get('nodes', []):
    if 'credentials' in node:
        del node['credentials']

# Create minimal structure
cleaned = {
    'name': wf.get('name'),
    'nodes': wf.get('nodes', []),
    'connections': wf.get('connections', {}),
    'settings': {
        'executionOrder': wf.get('settings', {}).get('executionOrder', 'v1'),
        'timezone': wf.get('settings', {}).get('timezone', 'America/New_York')
    }
}

with open('$NO_CREDS_FILE', 'w') as f:
    json.dump(cleaned, f, indent=2)

print('✅ Created workflow without credentials')
print(f\"   Nodes: {len(cleaned['nodes'])}\")
" 2>&1

if [ ! -f "$NO_CREDS_FILE" ]; then
    echo -e "${RED}❌ Failed to create workflow without credentials${NC}"
    exit 1
fi

# Verify it has 13 nodes
NODE_COUNT=$(python3 -c "import json; w=json.load(open('$NO_CREDS_FILE')); print(len(w.get('nodes', [])))" 2>/dev/null || echo "0")
if [ "$NODE_COUNT" != "13" ]; then
    echo -e "${RED}❌ ERROR: Workflow has $NODE_COUNT nodes (expected 13)${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Workflow ready (13 nodes, no credentials)${NC}"
echo ""

# Step 3: Import via API
echo -e "${CYAN}Step 3: Importing workflow via API...${NC}"
IMPORT_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$NO_CREDS_FILE" 2>&1)

HTTP_CODE=$(echo "$IMPORT_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2 || echo "000")
BODY=$(echo "$IMPORT_RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    NEW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
    NEW_NAME=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('name', ''))" 2>/dev/null || echo "")
    
    echo -e "${GREEN}✅ SUCCESS! Workflow imported${NC}"
    echo "   ID: $NEW_ID"
    echo "   Name: $NEW_NAME"
    echo ""
    
    # Verify
    VERIFY_RESPONSE=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows/$NEW_ID" -H "X-N8N-API-KEY: $N8N_API_KEY" 2>/dev/null)
    IMPORTED_NODES=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('nodes', [])))" 2>/dev/null || echo "?")
    
    if [ "$IMPORTED_NODES" = "13" ]; then
        echo -e "${GREEN}✅ Verified: 13 nodes imported${NC}"
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
    echo "   - Should load now (no credentials to validate)"
    echo "   - If still blank → Check browser console (F12)"
    echo ""
    echo -e "${YELLOW}4. Add credentials manually:${NC}"
    echo "   - Open each HTTP Request node"
    echo "   - Select credentials:"
    echo "     • Dispatch GitHub Build → GitHub Actions Token"
    echo "     • Check Latest GitHub Run → GitHub Actions Token"
    echo "     • Check Latest Netlify Deploy → Netlify API Token"
    echo "   - Save each node"
    echo ""
    
else
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo "$BODY" | head -5
    exit 1
fi

echo ""
echo -e "${GREEN}✅ Process complete!${NC}"
echo ""


