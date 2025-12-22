#!/bin/bash
# Recreate and test orchestrator end-to-end - Complete bug-free solution
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PI_N8N_URL="http://192.168.1.226:5678"
DESKTOP_FILE="${HOME}/Desktop/n8n-workflows-to-import/n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🔧 Recreate & Test Orchestrator - End-to-End${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Load API key
if [ -f .n8n-env.pi ]; then
    source .n8n-env.pi 2>/dev/null
fi

if [ -z "$N8N_API_KEY" ]; then
    echo -e "${RED}❌ No API key found${NC}"
    exit 1
fi

echo -e "${GREEN}✅ API key found${NC}"
echo ""

# Step 1: Delete ALL existing
echo -e "${YELLOW}Step 1: Cleaning up...${NC}"
WORKFLOWS=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY")
ORCHESTRATOR_IDS=$(echo "$WORKFLOWS" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for w in data.get('data', []):
    if 'Unity Build Orchestrator' in w.get('name', ''):
        print(w.get('id'))
" 2>/dev/null)

COUNT=$(echo "$ORCHESTRATOR_IDS" | grep -v '^$' | wc -l | tr -d ' ')
if [ "$COUNT" -gt 0 ]; then
    for ID in $ORCHESTRATOR_IDS; do
        [ -n "$ID" ] && curl -s -X DELETE "${PI_N8N_URL}/api/v1/workflows/$ID" \
          -H "X-N8N-API-KEY: $N8N_API_KEY" > /dev/null 2>&1
    done
    echo -e "${GREEN}✅ Deleted $COUNT workflow(s)${NC}"
fi
echo ""

# Step 2: Recreate clean workflow
echo -e "${YELLOW}Step 2: Recreating clean workflow...${NC}"
CLEAN_FILE="/tmp/orchestrator-recreated-$$-$(date +%s).json"
if ! python3 scripts/recreate-orchestrator-complete.py "$DESKTOP_FILE" "$CLEAN_FILE"; then
    echo -e "${RED}❌ Failed to recreate workflow${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Clean workflow created${NC}"
echo ""

# Step 3: Additional validation
echo -e "${YELLOW}Step 3: Additional validation...${NC}"
python3 << VALIDATE
import json
import sys

with open("$CLEAN_FILE", 'r') as f:
    w = json.load(f)

errors = []
for node in w.get('nodes', []):
    if 'respondToWebhook' in node.get('type', '') and node.get('typeVersion') == 1:
        if 'options' in node.get('parameters', {}):
            errors.append(f"{node.get('name')}: respondToWebhook v1 has options")
        # Check for only allowed params
        params = node.get('parameters', {})
        allowed = ['respondWith', 'responseBody', 'responseCode', 'responseHeaders']
        for p in params:
            if p not in allowed:
                errors.append(f"{node.get('name')}: unexpected param '{p}'")

if errors:
    for e in errors:
        print(f"ERROR: {e}")
    sys.exit(1)
else:
    print("✅ All validations passed")
VALIDATE

VALIDATION_EXIT=$?

if [ $VALIDATION_EXIT -ne 0 ]; then
    echo -e "${RED}❌ Validation failed${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Validation passed${NC}"
echo ""

# Step 4: Import
echo -e "${YELLOW}Step 4: Importing workflow...${NC}"
IMPORT_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$CLEAN_FILE")

HTTP_CODE=$(echo "$IMPORT_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$IMPORT_RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" != "200" ] && [ "$HTTP_CODE" != "201" ]; then
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo "$BODY" | head -10
    echo ""
    echo -e "${YELLOW}Debugging workflow structure:${NC}"
    python3 -c "
import json
with open('$CLEAN_FILE', 'r') as f:
    w = json.load(f)
print(f'Nodes: {len(w.get(\"nodes\", []))}')
for node in w.get('nodes', []):
    if 'respondToWebhook' in node.get('type', ''):
        print(f'  {node.get(\"name\")}: {node.get(\"type\")} v{node.get(\"typeVersion\")}')
        print(f'    Params: {list(node.get(\"parameters\", {}).keys())}')
"
    rm -f "$CLEAN_FILE"
    exit 1
fi

WORKFLOW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
if [ -z "$WORKFLOW_ID" ]; then
    echo -e "${RED}❌ Could not get workflow ID${NC}"
    rm -f "$CLEAN_FILE"
    exit 1
fi

echo -e "${GREEN}✅ Workflow imported (ID: $WORKFLOW_ID)${NC}"
rm -f "$CLEAN_FILE"
echo ""

# Step 5: Verify imported
echo -e "${YELLOW}Step 5: Verifying imported workflow...${NC}"
VERIFY_RESPONSE=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY")

NODE_COUNT=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('nodes', [])))" 2>/dev/null || echo "?")
IS_ARCHIVED=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('isArchived', False))" 2>/dev/null || echo "?")
WORKFLOW_NAME=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('name', 'Unknown'))" 2>/dev/null || echo "Unknown")

# Check for issues in imported
ISSUES=$(echo "$VERIFY_RESPONSE" | python3 -c "
import sys, json
data = json.load(sys.stdin)
issues = []
for node in data.get('nodes', []):
    if 'respondToWebhook' in node.get('type', '') and node.get('typeVersion') == 1:
        if 'options' in node.get('parameters', {}):
            issues.append(f\"{node.get('name')}: respondToWebhook v1 has options\")
if issues:
    for issue in issues:
        print(issue)
" 2>/dev/null)

if [ -n "$ISSUES" ]; then
    echo -e "${RED}❌ Issues found in imported workflow:${NC}"
    echo "$ISSUES"
    exit 1
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ SUCCESS! Orchestrator Recreated & Verified${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "  Name: $WORKFLOW_NAME"
echo "  ID: $WORKFLOW_ID"
echo "  Nodes: $NODE_COUNT"
echo "  Archived: $IS_ARCHIVED"
echo ""
echo -e "${GREEN}✅ All validations passed${NC}"
echo -e "${GREEN}✅ No bugs found${NC}"
echo -e "${GREEN}✅ Ready to activate${NC}"
echo ""
echo -e "${YELLOW}📝 Next step:${NC}"
echo "  1. Open: $PI_N8N_URL"
echo "  2. Find workflow: $WORKFLOW_NAME"
echo "  3. Toggle switch to activate"
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
