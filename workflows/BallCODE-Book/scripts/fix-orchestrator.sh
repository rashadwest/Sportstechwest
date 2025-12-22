#!/bin/bash
# Fix Unity Build Orchestrator - Clean up duplicates and get ONE working
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PI_N8N_URL="http://192.168.1.226:5678"
DESKTOP_FILE="${HOME}/Desktop/n8n-workflows-to-import/n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"
LOCAL_FILE="n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🔧 Fix Unity Build Orchestrator${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Load API key
if [ -f .n8n-env.pi ]; then
    source .n8n-env.pi 2>/dev/null
fi

if [ -z "$N8N_API_KEY" ] || [ "$N8N_API_KEY" = "" ]; then
    echo -e "${RED}❌ No API key found. Please run: ./scripts/setup-pi-api-key.sh${NC}"
    exit 1
fi

echo -e "${GREEN}✅ API key found${NC}"
echo ""

# Step 1: Find and delete all duplicate orchestrators
echo -e "${YELLOW}Step 1: Cleaning up duplicate workflows...${NC}"
WORKFLOWS=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json")

ORCHESTRATOR_IDS=$(echo "$WORKFLOWS" | python3 -c "
import sys, json
data = json.load(sys.stdin)
workflows = [w for w in data.get('data', []) if 'Unity Build Orchestrator' in w.get('name', '') and '13 nodes' in w.get('name', '')]
for w in workflows:
    print(w.get('id'))
" 2>/dev/null)

COUNT=$(echo "$ORCHESTRATOR_IDS" | wc -l | tr -d ' ')
echo -e "${YELLOW}   Found $COUNT duplicate orchestrator(s)${NC}"

if [ "$COUNT" -gt 0 ]; then
    DELETED=0
    for ID in $ORCHESTRATOR_IDS; do
        if [ -n "$ID" ]; then
            echo -e "${YELLOW}   Deleting duplicate: $ID${NC}"
            DELETE_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X DELETE "${PI_N8N_URL}/api/v1/workflows/$ID" \
              -H "X-N8N-API-KEY: $N8N_API_KEY" \
              -H "Content-Type: application/json" 2>/dev/null)
            HTTP_CODE=$(echo "$DELETE_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
            if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "204" ]; then
                DELETED=$((DELETED + 1))
            fi
        fi
    done
    echo -e "${GREEN}✅ Deleted $DELETED duplicate workflow(s)${NC}"
else
    echo -e "${GREEN}✅ No duplicates found${NC}"
fi
echo ""

# Step 2: Import fresh orchestrator
echo -e "${YELLOW}Step 2: Importing fresh orchestrator...${NC}"

# Find workflow file
if [ -f "$DESKTOP_FILE" ]; then
    WORKFLOW_FILE="$DESKTOP_FILE"
    echo -e "${GREEN}✅ Using workflow from Desktop${NC}"
elif [ -f "$LOCAL_FILE" ]; then
    WORKFLOW_FILE="$LOCAL_FILE"
    echo -e "${YELLOW}⚠️  Using local workflow file${NC}"
else
    echo -e "${RED}❌ Workflow file not found${NC}"
    exit 1
fi

# Verify it has 13 nodes
NODE_COUNT=$(python3 -c "import json, os; w=json.load(open('$WORKFLOW_FILE')); print(len(w.get('nodes', [])))" 2>/dev/null || echo "0")
if [ "$NODE_COUNT" != "13" ]; then
    echo -e "${RED}❌ ERROR: Workflow has $NODE_COUNT nodes, expected 13!${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Verified: Workflow has 13 nodes${NC}"

# Clean workflow for API
CLEANED_FILE="/tmp/n8n-orchestrator-import-$$-$(date +%s).json"
if python3 scripts/clean-workflow-for-api.py "$WORKFLOW_FILE" "$CLEANED_FILE" 2>/dev/null; then
    WORKFLOW_FILE_TO_IMPORT="$CLEANED_FILE"
    echo -e "${GREEN}✅ Workflow cleaned for API${NC}"
else
    WORKFLOW_FILE_TO_IMPORT="$WORKFLOW_FILE"
    CLEANED_FILE=""
fi

# Import workflow
IMPORT_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$WORKFLOW_FILE_TO_IMPORT")

HTTP_CODE=$(echo "$IMPORT_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$IMPORT_RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" != "200" ] && [ "$HTTP_CODE" != "201" ]; then
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo "$BODY" | head -5
    [ -n "$CLEANED_FILE" ] && [ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
    exit 1
fi

WORKFLOW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
if [ -z "$WORKFLOW_ID" ]; then
    echo -e "${RED}❌ Could not get workflow ID from response${NC}"
    [ -n "$CLEANED_FILE" ] && [ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
    exit 1
fi

echo -e "${GREEN}✅ Workflow imported (ID: $WORKFLOW_ID)${NC}"
[ -n "$CLEANED_FILE" ] && [ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
echo ""

# Step 3: Unarchive workflow
echo -e "${YELLOW}Step 3: Unarchiving workflow...${NC}"
UNARCHIVE_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID/activate" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"active": false}' 2>/dev/null)

# Actually unarchive by updating workflow
UNARCHIVE_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X PATCH "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"isArchived": false}' 2>/dev/null)

HTTP_CODE=$(echo "$UNARCHIVE_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ Workflow unarchived${NC}"
else
    echo -e "${YELLOW}⚠️  Could not unarchive via API (HTTP $HTTP_CODE)${NC}"
    echo -e "${YELLOW}   You may need to unarchive manually in n8n UI${NC}"
fi
echo ""

# Step 4: Verify final status
echo -e "${YELLOW}Step 4: Verifying workflow status...${NC}"
VERIFY_RESPONSE=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" 2>/dev/null)

NODE_COUNT=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('nodes', [])))" 2>/dev/null || echo "?")
IS_ARCHIVED=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('isArchived', False))" 2>/dev/null || echo "?")
IS_ACTIVE=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('active', False))" 2>/dev/null || echo "?")
WORKFLOW_NAME=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('name', 'Unknown'))" 2>/dev/null || echo "Unknown")

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Orchestrator Status:${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "  Name: $WORKFLOW_NAME"
echo "  ID: $WORKFLOW_ID"
echo "  Nodes: $NODE_COUNT"
echo "  Archived: $IS_ARCHIVED"
echo "  Active: $IS_ACTIVE"
echo ""

if [ "$NODE_COUNT" = "13" ] && [ "$IS_ARCHIVED" = "False" ]; then
    echo -e "${GREEN}✅ SUCCESS! Orchestrator is ready${NC}"
    echo ""
    echo -e "${YELLOW}📝 Next steps:${NC}"
    echo "1. Open n8n: $PI_N8N_URL"
    echo "2. Find workflow: $WORKFLOW_NAME"
    echo "3. Activate it (toggle switch in top bar)"
    echo "4. Configure credentials if needed"
    echo ""
    echo -e "${GREEN}🎉 Orchestrator is working!${NC}"
else
    echo -e "${YELLOW}⚠️  Workflow needs attention:${NC}"
    if [ "$IS_ARCHIVED" != "False" ]; then
        echo "   - Still archived (unarchive manually in n8n UI)"
    fi
    if [ "$NODE_COUNT" != "13" ]; then
        echo "   - Has $NODE_COUNT nodes (expected 13)"
    fi
    echo ""
    echo "Open n8n: $PI_N8N_URL"
    echo "Workflow ID: $WORKFLOW_ID"
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

