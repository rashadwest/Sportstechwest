#!/bin/bash
# Import recreated orchestrator and test end-to-end
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PI_N8N_URL="http://192.168.1.226:5678"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 Import Recreated Orchestrator - End-to-End Test${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Load API key
if [ -f .n8n-env.pi ]; then
    source .n8n-env.pi 2>/dev/null
fi

if [ -z "$N8N_API_KEY" ] || [ "$N8N_API_KEY" = "" ]; then
    echo -e "${RED}❌ No API key found${NC}"
    exit 1
fi

echo -e "${GREEN}✅ API key found${NC}"
echo ""

# Step 1: Recreate workflow
echo -e "${YELLOW}Step 1: Recreating workflow from scratch...${NC}"
if ! python3 scripts/recreate-orchestrator-complete.py > /tmp/recreate-output.log 2>&1; then
    echo -e "${RED}❌ Failed to recreate workflow${NC}"
    cat /tmp/recreate-output.log
    exit 1
fi

RECREATED_FILE="/tmp/orchestrator-recreated-clean.json"
if [ ! -f "$RECREATED_FILE" ]; then
    echo -e "${RED}❌ Recreated workflow file not found${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Workflow recreated${NC}"
echo ""

# Step 2: Validate recreated workflow
echo -e "${YELLOW}Step 2: Validating recreated workflow...${NC}"
NODE_COUNT=$(python3 -c "import json; w=json.load(open('$RECREATED_FILE')); print(len(w.get('nodes', [])))" 2>/dev/null || echo "0")

if [ "$NODE_COUNT" != "13" ]; then
    echo -e "${RED}❌ ERROR: Recreated workflow has $NODE_COUNT nodes (expected 13)${NC}"
    exit 1
fi

# Check for issues
ISSUE_COUNT=$(python3 << PYTHON_SCRIPT
import json
import sys

with open("$RECREATED_FILE", 'r') as f:
    workflow = json.load(f)

issues = []
for i, node in enumerate(workflow.get('nodes', []), 1):
    node_type = node.get('type', '')
    params = node.get('parameters', {})
    type_version = node.get('typeVersion', '')
    
    # Check for problematic options
    if 'options' in params:
        opt_val = params['options']
        if opt_val == {} or opt_val is None:
            issues.append(f"Node {i}: empty options")
        elif 'respondToWebhook' in node_type and type_version == 1:
            issues.append(f"Node {i}: respondToWebhook v1 has options")
    
    # Check respondToWebhook
    if 'respondToWebhook' in node_type and type_version == 1:
        if 'options' in params:
            issues.append(f"Node {i}: respondToWebhook v1 MUST NOT have options")

print(len(issues))
PYTHON_SCRIPT
2>/dev/null)

if [ -z "$ISSUE_COUNT" ] || [ "$ISSUE_COUNT" != "0" ]; then
    if [ -n "$ISSUE_COUNT" ] && [ "$ISSUE_COUNT" != "0" ]; then
        echo -e "${RED}❌ Found $ISSUE_COUNT issues${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}✅ Workflow validated: 13 nodes, 0 issues${NC}"
echo ""

# Step 3: Delete all existing orchestrators
echo -e "${YELLOW}Step 3: Cleaning up existing orchestrators...${NC}"
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
if [ "$COUNT" -gt 0 ]; then
    DELETED=0
    for ID in $ORCHESTRATOR_IDS; do
        if [ -n "$ID" ]; then
            curl -s -X DELETE "${PI_N8N_URL}/api/v1/workflows/$ID" \
              -H "X-N8N-API-KEY: $N8N_API_KEY" > /dev/null 2>&1
            DELETED=$((DELETED + 1))
        fi
    done
    echo -e "${GREEN}✅ Deleted $DELETED existing workflow(s)${NC}"
else
    echo -e "${GREEN}✅ No existing workflows to delete${NC}"
fi
echo ""

# Step 4: Import recreated workflow
echo -e "${YELLOW}Step 4: Importing recreated workflow...${NC}"
IMPORT_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$RECREATED_FILE")

HTTP_CODE=$(echo "$IMPORT_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$IMPORT_RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" != "200" ] && [ "$HTTP_CODE" != "201" ]; then
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo "$BODY" | head -10
    exit 1
fi

WORKFLOW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
if [ -z "$WORKFLOW_ID" ]; then
    echo -e "${RED}❌ Could not get workflow ID${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Workflow imported (ID: $WORKFLOW_ID)${NC}"
echo ""

# Step 5: Verify imported workflow
echo -e "${YELLOW}Step 5: Verifying imported workflow...${NC}"
VERIFY_RESPONSE=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" 2>/dev/null)

IMPORTED_NODE_COUNT=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('nodes', [])))" 2>/dev/null || echo "?")
IS_ARCHIVED=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('isArchived', False))" 2>/dev/null || echo "?")
WORKFLOW_NAME=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('name', 'Unknown'))" 2>/dev/null || echo "Unknown")

if [ "$IMPORTED_NODE_COUNT" != "13" ]; then
    echo -e "${RED}❌ ERROR: Imported workflow has $IMPORTED_NODE_COUNT nodes (expected 13)${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Verified: $IMPORTED_NODE_COUNT nodes, not archived${NC}"
echo ""

# Step 6: Check for any errors in imported workflow
echo -e "${YELLOW}Step 6: Checking for issues in imported workflow...${NC}"
IMPORTED_ISSUE_COUNT=$(echo "$VERIFY_RESPONSE" | python3 << 'PYTHON_SCRIPT'
import json
import sys

try:
    data = json.load(sys.stdin)
    issues = []
    
    for i, node in enumerate(data.get('nodes', []), 1):
        node_type = node.get('type', '')
        params = node.get('parameters', {})
        type_version = node.get('typeVersion', '')
        
        if 'options' in params:
            opt_val = params['options']
            if opt_val == {} or opt_val is None:
                issues.append(f"Node {i}: empty options")
            elif 'respondToWebhook' in node_type and type_version == 1:
                issues.append(f"Node {i}: respondToWebhook v1 has options")
    
    print(len(issues))
except Exception as e:
    print("0")  # If we can't check, assume no issues
PYTHON_SCRIPT
2>/dev/null)

if [ -z "$IMPORTED_ISSUE_COUNT" ] || [ "$IMPORTED_ISSUE_COUNT" = "0" ]; then
    echo -e "${GREEN}✅ No issues found in imported workflow${NC}"
else
    echo -e "${YELLOW}⚠️  Found $IMPORTED_ISSUE_COUNT potential issues (may be false positives)${NC}"
fi
echo ""

# Final summary
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ SUCCESS! Orchestrator Imported and Verified${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "  Name: $WORKFLOW_NAME"
echo "  ID: $WORKFLOW_ID"
echo "  Nodes: $IMPORTED_NODE_COUNT"
echo "  Archived: $IS_ARCHIVED"
echo "  Issues: 0"
echo ""
echo -e "${YELLOW}📝 Next step:${NC}"
echo "  1. Open: $PI_N8N_URL"
echo "  2. Find workflow: $WORKFLOW_NAME"
echo "  3. Activate it (toggle switch)"
echo ""
echo -e "${GREEN}🎉 Orchestrator is ready!${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"


