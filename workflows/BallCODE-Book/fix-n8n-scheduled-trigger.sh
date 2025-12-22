#!/bin/bash
# Fix n8n Scheduled Trigger Warnings
# Adds missing triggerAtMinute parameter and timezone setting

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Load environment
if [ -z "$N8N_URL" ]; then
  if [ -f .n8n-env ]; then
    source .n8n-env
  fi
fi

N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🔧 Fixing n8n Scheduled Trigger Warnings${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check connection
echo -e "${YELLOW}📡 Checking n8n connection...${NC}"
if ! curl -s -f "${N8N_URL}/healthz" > /dev/null 2>&1; then
  echo -e "${RED}❌ Cannot connect to n8n at: ${N8N_URL}${NC}"
  exit 1
fi
echo -e "${GREEN}✅ n8n is accessible${NC}"
echo ""

# Get workflow ID
echo -e "${YELLOW}📋 Finding Unity workflow...${NC}"
WORKFLOW_FILE="n8n-unity-automation-workflow-FINAL-WORKING.json"

if [ ! -f "$WORKFLOW_FILE" ]; then
  echo -e "${RED}❌ Workflow file not found: $WORKFLOW_FILE${NC}"
  exit 1
fi

# Get workflow ID from n8n
WORKFLOW_ID=$(curl -s "${N8N_URL}/api/v1/workflows" \
  ${N8N_API_KEY:+-H "X-N8N-API-KEY: $N8N_API_KEY"} \
  ${N8N_BASIC_AUTH:+-u "$N8N_BASIC_AUTH"} 2>/dev/null | \
  python3 -c "
import sys, json
data = json.load(sys.stdin)
for wf in data.get('data', []):
    if 'unity' in wf.get('name', '').lower() or 'ballcode' in wf.get('name', '').lower():
        print(wf.get('id', ''))
        break
" 2>/dev/null)

if [ -z "$WORKFLOW_ID" ]; then
  echo -e "${YELLOW}⚠️  Workflow not found in n8n. Will create new workflow.${NC}"
  CREATE_NEW=true
else
  echo -e "${GREEN}✅ Found workflow ID: ${WORKFLOW_ID}${NC}"
  CREATE_NEW=false
fi
echo ""

# Validate JSON
echo -e "${YELLOW}📋 Validating workflow JSON...${NC}"
if ! python3 -m json.tool "$WORKFLOW_FILE" > /dev/null 2>&1; then
  echo -e "${RED}❌ Invalid JSON in workflow file${NC}"
  exit 1
fi
echo -e "${GREEN}✅ JSON is valid${NC}"
echo ""

# Deploy workflow
if [ "$CREATE_NEW" = true ]; then
  echo -e "${YELLOW}🚀 Creating new workflow...${NC}"
  RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "${N8N_URL}/api/v1/workflows" \
    ${N8N_API_KEY:+-H "X-N8N-API-KEY: $N8N_API_KEY"} \
    ${N8N_BASIC_AUTH:+-u "$N8N_BASIC_AUTH"} \
    -H "Content-Type: application/json" \
    -d @"$WORKFLOW_FILE" 2>/dev/null)
else
  echo -e "${YELLOW}🔄 Updating existing workflow...${NC}"
  RESPONSE=$(curl -s -w "\n%{http_code}" -X PUT "${N8N_URL}/api/v1/workflows/${WORKFLOW_ID}" \
    ${N8N_API_KEY:+-H "X-N8N-API-KEY: $N8N_API_KEY"} \
    ${N8N_BASIC_AUTH:+-u "$N8N_BASIC_AUTH"} \
    -H "Content-Type: application/json" \
    -d @"$WORKFLOW_FILE" 2>/dev/null)
fi

HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
BODY=$(echo "$RESPONSE" | sed '$d')

if [ "$HTTP_CODE" -eq 200 ] || [ "$HTTP_CODE" -eq 201 ]; then
  echo -e "${GREEN}✅ Workflow ${CREATE_NEW:+created}${CREATE_NEW:-updated} successfully!${NC}"
  echo ""
  echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo -e "${GREEN}✅ Fix Applied!${NC}"
  echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo ""
  echo "Fixes applied:"
  echo "  ✅ Added triggerAtMinute: 0 (runs at top of hour)"
  echo "  ✅ Added timezone: America/New_York"
  echo ""
  echo "Next steps:"
  echo "  1. Open n8n UI: ${N8N_URL}"
  echo "  2. Open your workflow"
  echo "  3. Check 'Scheduled Trigger' node - warnings should be gone"
  echo "  4. Verify workflow is Active (toggle ON)"
  echo ""
else
  echo -e "${RED}❌ Error ${CREATE_NEW:+creating}${CREATE_NEW:-updating} workflow (HTTP $HTTP_CODE)${NC}"
  echo "$BODY" | python3 -m json.tool 2>/dev/null || echo "$BODY"
  echo ""
  echo "If API access is denied, you can:"
  echo "  1. Open n8n UI: ${N8N_URL}"
  echo "  2. Import the fixed workflow file manually"
  echo "  3. Or edit the Scheduled Trigger node and add:"
  echo "     - Trigger at Minute: 0"
  echo "     - Timezone: America/New_York (in workflow settings)"
  exit 1
fi


