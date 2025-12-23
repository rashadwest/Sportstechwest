#!/bin/bash
# Import Fixed Garvis Orchestrator Workflow to n8n
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

PI_N8N_URL="http://192.168.1.226:5678"
SOURCE_FILE="n8n-garvis-orchestrator-workflow.json"
CLEANED_FILE="n8n-garvis-orchestrator-workflow-API-READY.json"
WORKFLOW_FILE="$CLEANED_FILE"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

# Load API key from .n8n-env.pi if exists
if [ -f .n8n-env.pi ]; then
    source .n8n-env.pi 2>/dev/null
fi

if [ -z "$N8N_API_KEY" ]; then
    echo -e "${RED}❌ N8N_API_KEY not set${NC}"
    echo ""
    echo "To get API key:"
    echo "1. Open: $PI_N8N_URL"
    echo "2. Settings → API → Create API Key"
    echo "3. Add to .n8n-env.pi: export N8N_API_KEY='your_key'"
    exit 1
fi

if [ ! -f "$SOURCE_FILE" ]; then
    echo -e "${RED}❌ Source workflow file not found: $SOURCE_FILE${NC}"
    exit 1
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 Importing Fixed Garvis Orchestrator Workflow${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Step 0: Clean workflow for API
echo -e "${BLUE}Step 0: Cleaning workflow for API import...${NC}"
if [ -f "scripts/clean-workflow-for-api-v2.py" ]; then
    python3 scripts/clean-workflow-for-api-v2.py "$SOURCE_FILE" "$CLEANED_FILE" 2>/dev/null
    if [ $? -eq 0 ] && [ -f "$CLEANED_FILE" ]; then
        echo -e "${GREEN}✅ Workflow cleaned${NC}"
    else
        echo -e "${YELLOW}⚠️  Clean script not available, using source file${NC}"
        WORKFLOW_FILE="$SOURCE_FILE"
    fi
else
    echo -e "${YELLOW}⚠️  Clean script not found, using source file${NC}"
    WORKFLOW_FILE="$SOURCE_FILE"
fi

# Step 1: Find existing workflow
echo -e "${BLUE}Step 1: Checking for existing workflow...${NC}"
WORKFLOWS_JSON=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows" -H "X-N8N-API-KEY: $N8N_API_KEY")

EXISTING_ID=$(echo "$WORKFLOWS_JSON" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    workflows = data.get('data', [])
    for w in workflows:
        if 'garvis' in w.get('name', '').lower() and 'orchestrator' in w.get('name', '').lower():
            print(w.get('id'))
            break
except:
    pass
" 2>/dev/null)

if [ -n "$EXISTING_ID" ]; then
    echo -e "${YELLOW}Found existing workflow (ID: $EXISTING_ID)${NC}"
    echo -e "${BLUE}Step 2: Updating existing workflow...${NC}"
    
    # Update existing workflow
    RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X PUT "${PI_N8N_URL}/api/v1/workflows/$EXISTING_ID" \
      -H "X-N8N-API-KEY: $N8N_API_KEY" \
      -H "Content-Type: application/json" \
      -d @"$WORKFLOW_FILE")
else
    echo -e "${BLUE}Step 2: Creating new workflow...${NC}"
    
    # Create new workflow
    RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
      -H "X-N8N-API-KEY: $N8N_API_KEY" \
      -H "Content-Type: application/json" \
      -d @"$WORKFLOW_FILE")
fi

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ SUCCESS! Workflow imported/updated${NC}"
    echo ""
    
    # Extract workflow ID
    WORKFLOW_ID=$(echo "$BODY" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data.get('id', ''))
except:
    pass
" 2>/dev/null)
    
    if [ -n "$WORKFLOW_ID" ]; then
        echo -e "${GREEN}Workflow ID: $WORKFLOW_ID${NC}"
    fi
    
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo "1. Open: $PI_N8N_URL"
    echo "2. Find: 'Garvis Orchestrator - BallCODE Fully Integrated System'"
    echo "3. Activate workflow (toggle ON)"
    echo "4. Test with: curl -X POST \"$PI_N8N_URL/webhook/garvis\" -H \"Content-Type: application/json\" -d '{\"one_thing\": \"test\", \"tasks\": [\"test\"]}'"
else
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo "$BODY" | head -10
    exit 1
fi

