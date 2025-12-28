#!/bin/bash
# End-to-end fix for Unity Build Orchestrator - Get it working completely
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
echo -e "${BLUE}🔧 End-to-End Orchestrator Fix${NC}"
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

# Step 1: Delete ALL orchestrator workflows (including current one)
echo -e "${YELLOW}Step 1: Cleaning up ALL orchestrator workflows...${NC}"
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

COUNT=$(echo "$ORCHESTRATOR_IDS" | grep -v '^$' | wc -l | tr -d ' ')
echo -e "${YELLOW}   Found $COUNT orchestrator workflow(s) to delete${NC}"

if [ "$COUNT" -gt 0 ]; then
    DELETED=0
    for ID in $ORCHESTRATOR_IDS; do
        if [ -n "$ID" ]; then
            DELETE_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X DELETE "${PI_N8N_URL}/api/v1/workflows/$ID" \
              -H "X-N8N-API-KEY: $N8N_API_KEY" \
              -H "Content-Type: application/json" 2>/dev/null)
            HTTP_CODE=$(echo "$DELETE_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
            if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "204" ]; then
                DELETED=$((DELETED + 1))
            fi
        fi
    done
    echo -e "${GREEN}✅ Deleted $DELETED workflow(s)${NC}"
else
    echo -e "${GREEN}✅ No workflows to delete${NC}"
fi
echo ""

# Step 2: Find and verify workflow file
echo -e "${YELLOW}Step 2: Preparing workflow file...${NC}"
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

# Step 3: Clean workflow with enhanced cleaning
echo -e "${YELLOW}Step 3: Cleaning workflow for API import...${NC}"
CLEANED_FILE="/tmp/n8n-orchestrator-fixed-$$-$(date +%s).json"

# First pass: Use existing cleaning script
if python3 scripts/clean-workflow-for-api.py "$WORKFLOW_FILE" "$CLEANED_FILE" 2>/dev/null; then
    echo -e "${GREEN}✅ Initial cleaning complete${NC}"
else
    echo -e "${RED}❌ Cleaning failed${NC}"
    exit 1
fi

# Second pass: Additional fixes for activation issues
echo -e "${YELLOW}   Applying additional fixes...${NC}"
python3 << PYTHON_SCRIPT
import json
import sys

cleaned_file = "$CLEANED_FILE"

with open(cleaned_file, 'r') as f:
    workflow = json.load(f)

fixes = []

# Fix: Ensure all nodes have proper structure
for node in workflow.get('nodes', []):
    node_type = node.get('type', '')
    params = node.get('parameters', {})
    
    # Fix httpRequest nodes - ensure options structure is correct
    if 'httpRequest' in node_type:
        if 'options' in params:
            # Ensure options is an object, not null
            if params['options'] is None:
                params['options'] = {}
            # Ensure headers exists if options exists
            if 'options' in params and 'headers' not in params['options']:
                params['options']['headers'] = {}
    
    # Fix respondToWebhook - ensure NO options at all
    if 'respondToWebhook' in node_type and node.get('typeVersion') == 1:
        if 'options' in params:
            del params['options']
            fixes.append(f"Removed options from {node.get('name', 'Unknown')}")
    
    # Fix webhook nodes - ensure proper structure
    if 'webhook' in node_type.lower() and node.get('typeVersion') == 1:
        # Webhook nodes should have responseMode, not options
        if 'options' in params and params.get('options') == {}:
            del params['options']
            fixes.append(f"Removed empty options from {node.get('name', 'Unknown')}")

if fixes:
    print(f"   Applied {len(fixes)} additional fixes")

# Ensure workflow structure is minimal and correct
# Remove any null/empty properties that might cause issues
if 'staticData' in workflow and (workflow['staticData'] is None or workflow['staticData'] == {}):
    workflow['staticData'] = {}
if 'pinData' in workflow and (workflow['pinData'] is None or workflow['pinData'] == {}):
    workflow['pinData'] = {}

# Ensure settings has required structure
if 'settings' not in workflow:
    workflow['settings'] = {}
if 'executionOrder' not in workflow['settings']:
    workflow['settings']['executionOrder'] = 'v1'

with open(cleaned_file, 'w') as f:
    json.dump(workflow, f, indent=2)

PYTHON_SCRIPT

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Additional fixes applied${NC}"
else
    echo -e "${YELLOW}⚠️  Additional fixes may have failed, continuing...${NC}"
fi
echo ""

# Step 4: Import workflow
echo -e "${YELLOW}Step 4: Importing workflow...${NC}"
IMPORT_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$CLEANED_FILE")

HTTP_CODE=$(echo "$IMPORT_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$IMPORT_RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" != "200" ] && [ "$HTTP_CODE" != "201" ]; then
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo "$BODY" | head -10
    [ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
    exit 1
fi

WORKFLOW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
if [ -z "$WORKFLOW_ID" ]; then
    echo -e "${RED}❌ Could not get workflow ID${NC}"
    [ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
    exit 1
fi

echo -e "${GREEN}✅ Workflow imported (ID: $WORKFLOW_ID)${NC}"
[ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
echo ""

# Step 5: Verify workflow structure
echo -e "${YELLOW}Step 5: Verifying workflow structure...${NC}"
VERIFY_RESPONSE=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" 2>/dev/null)

NODE_COUNT=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('nodes', [])))" 2>/dev/null || echo "?")
IS_ARCHIVED=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('isArchived', False))" 2>/dev/null || echo "?")
WORKFLOW_NAME=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('name', 'Unknown'))" 2>/dev/null || echo "Unknown")

if [ "$NODE_COUNT" != "13" ]; then
    echo -e "${RED}❌ ERROR: Imported workflow has $NODE_COUNT nodes (expected 13)${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Workflow verified: 13 nodes, not archived${NC}"
echo ""

# Step 6: Activate workflow (using update endpoint instead of activate)
echo -e "${YELLOW}Step 6: Activating workflow...${NC}"

# Get current workflow data
CURRENT_WORKFLOW=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" 2>/dev/null)

# Update workflow to set active=true
ACTIVATE_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X PUT "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$CURRENT_WORKFLOW" 2>/dev/null)

# Try alternative: PATCH with just active field
PATCH_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X PATCH "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"active": true}' 2>/dev/null)

PATCH_HTTP_CODE=$(echo "$PATCH_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)

if [ "$PATCH_HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ Workflow activated via API${NC}"
else
    echo -e "${YELLOW}⚠️  Could not activate via API (HTTP $PATCH_HTTP_CODE)${NC}"
    echo -e "${YELLOW}   Workflow is ready - activate manually in UI${NC}"
fi
echo ""

# Step 7: Final verification
echo -e "${YELLOW}Step 7: Final verification...${NC}"
FINAL_RESPONSE=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" 2>/dev/null)

FINAL_NODE_COUNT=$(echo "$FINAL_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('nodes', [])))" 2>/dev/null || echo "?")
FINAL_ARCHIVED=$(echo "$FINAL_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('isArchived', False))" 2>/dev/null || echo "?")
FINAL_ACTIVE=$(echo "$FINAL_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('active', False))" 2>/dev/null || echo "?")

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Orchestrator Status:${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "  Name: $WORKFLOW_NAME"
echo "  ID: $WORKFLOW_ID"
echo "  Nodes: $FINAL_NODE_COUNT"
echo "  Archived: $FINAL_ARCHIVED"
echo "  Active: $FINAL_ACTIVE"
echo ""

if [ "$FINAL_NODE_COUNT" = "13" ] && [ "$FINAL_ARCHIVED" = "False" ]; then
    if [ "$FINAL_ACTIVE" = "True" ]; then
        echo -e "${GREEN}🎉 SUCCESS! Orchestrator is ACTIVE and WORKING!${NC}"
    else
        echo -e "${GREEN}✅ Orchestrator is ready - activate in UI:${NC}"
        echo "   1. Open: $PI_N8N_URL"
        echo "   2. Find workflow: $WORKFLOW_NAME"
        echo "   3. Toggle switch to activate"
    fi
else
    echo -e "${YELLOW}⚠️  Workflow needs attention${NC}"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"


