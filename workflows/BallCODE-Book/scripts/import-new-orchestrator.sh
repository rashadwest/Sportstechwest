#!/bin/bash
# Import New Unity Build Orchestrator Workflow
# Brand new workflow from scratch - avoids all known issues

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

WORKFLOW_FILE="n8n-unity-build-orchestrator-NEW-FROM-SCRATCH.json"
N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 Import New Unity Build Orchestrator${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if workflow file exists
if [ ! -f "$WORKFLOW_FILE" ]; then
    echo -e "${RED}❌ Workflow file not found: $WORKFLOW_FILE${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Found workflow file: $WORKFLOW_FILE${NC}"

# Verify JSON structure
echo -e "${YELLOW}🔍 Verifying JSON structure...${NC}"
if ! python3 -m json.tool "$WORKFLOW_FILE" > /dev/null 2>&1; then
    echo -e "${RED}❌ Invalid JSON structure${NC}"
    exit 1
fi

# Count nodes
NODE_COUNT=$(python3 -c "import json; w=json.load(open('$WORKFLOW_FILE')); print(len(w.get('nodes', [])))")
echo -e "${GREEN}✅ JSON valid - $NODE_COUNT nodes${NC}"

# Check for problematic patterns
echo -e "${YELLOW}🔍 Checking for known issues...${NC}"

# Check for empty options
EMPTY_OPTIONS=$(python3 -c "
import json
w = json.load(open('$WORKFLOW_FILE'))
issues = []
for node in w.get('nodes', []):
    params = node.get('parameters', {})
    if 'options' in params:
        if params['options'] == {} or params['options'] is None:
            issues.append(node.get('name', 'Unknown'))
if issues:
    print(','.join(issues))
else:
    print('NONE')
")

if [ "$EMPTY_OPTIONS" != "NONE" ]; then
    echo -e "${YELLOW}⚠️  Found empty options in: $EMPTY_OPTIONS${NC}"
else
    echo -e "${GREEN}✅ No empty options found${NC}"
fi

# Check respondToWebhook nodes
RESPOND_ISSUES=$(python3 -c "
import json
w = json.load(open('$WORKFLOW_FILE'))
issues = []
for node in w.get('nodes', []):
    if 'respondToWebhook' in node.get('type', '') and node.get('typeVersion') == 1:
        params = node.get('parameters', {})
        if 'options' in params:
            issues.append(node.get('name', 'Unknown'))
if issues:
    print(','.join(issues))
else:
    print('NONE')
")

if [ "$RESPOND_ISSUES" != "NONE" ]; then
    echo -e "${RED}❌ respondToWebhook nodes with options: $RESPOND_ISSUES${NC}"
    exit 1
else
    echo -e "${GREEN}✅ respondToWebhook nodes are clean${NC}"
fi

echo ""
echo -e "${BLUE}📤 Importing workflow...${NC}"

# Check if API key is available
if [ -z "$N8N_API_KEY" ]; then
    echo -e "${YELLOW}⚠️  N8N_API_KEY not set - using UI import method${NC}"
    echo ""
    echo "To import via UI:"
    echo "1. Open: $N8N_URL"
    echo "2. Click 'Workflows' → 'Import from File'"
    echo "3. Select: $WORKFLOW_FILE"
    echo "4. Click 'Import'"
    echo ""
    echo "Or set N8N_API_KEY and run this script again for API import."
    exit 0
fi

# Import via API
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: ${N8N_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @"$WORKFLOW_FILE")

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "201" ] || [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ Workflow imported successfully!${NC}"
    echo ""
    
    # Extract workflow ID
    WORKFLOW_ID=$(echo "$BODY" | python3 -c "import json, sys; print(json.load(sys.stdin).get('id', ''))" 2>/dev/null || echo "")
    
    if [ -n "$WORKFLOW_ID" ]; then
        echo -e "${GREEN}Workflow ID: $WORKFLOW_ID${NC}"
        echo ""
        echo "Next steps:"
        echo "1. Open workflow in n8n UI: ${N8N_URL}/workflow/$WORKFLOW_ID"
        echo "2. Activate the workflow (toggle switch top-right)"
        echo "3. Test webhook:"
        echo "   curl -X POST ${N8N_URL}/webhook/unity-build \\"
        echo "     -H 'Content-Type: application/json' \\"
        echo "     -d '{\"request\": \"Test build\", \"branch\": \"main\"}'"
    fi
else
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo "Response: $BODY"
    echo ""
    echo "Try importing via UI instead:"
    echo "1. Open: $N8N_URL"
    echo "2. Click 'Workflows' → 'Import from File'"
    echo "3. Select: $WORKFLOW_FILE"
    exit 1
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Import Complete${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

