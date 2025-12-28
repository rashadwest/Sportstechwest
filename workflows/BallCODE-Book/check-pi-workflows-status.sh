#!/bin/bash
# Check Pi n8n Workflow Status
# Verifies which workflows are imported and active

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
echo -e "${BLUE}🔍 Checking Pi n8n Workflow Status${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check connection
echo -e "${YELLOW}📡 Checking Pi n8n connection...${NC}"
if curl -s -f "${PI_N8N_URL}/healthz" > /dev/null 2>&1 || curl -s -f "${PI_N8N_URL}" > /dev/null 2>&1; then
  echo -e "${GREEN}✅ Pi n8n is accessible${NC}"
else
  echo -e "${RED}❌ Cannot connect to Pi n8n${NC}"
  exit 1
fi
echo ""

# Expected workflows
EXPECTED_WORKFLOWS=(
  "BallCODE Full Integration"
  "Book Content Update"
  "Curriculum Schema Sync"
  "Game Exercise Integration"
  "Screenshot to Fix"
)

echo -e "${YELLOW}📋 Checking workflow status...${NC}"
echo ""

# Try to get workflows via API (may require auth)
WORKFLOWS_JSON=$(curl -s "${PI_N8N_URL}/api/v1/workflows" 2>/dev/null || echo "[]")

if [ "$WORKFLOWS_JSON" = "[]" ] || [ -z "$WORKFLOWS_JSON" ]; then
  echo -e "${YELLOW}⚠️  Cannot access workflows via API (may require authentication)${NC}"
  echo ""
  echo -e "${BLUE}📝 Manual Check Required:${NC}"
  echo ""
  echo "1. Open Pi n8n UI: ${PI_N8N_URL}"
  echo "2. Click 'Workflows' in left sidebar"
  echo "3. Check if these workflows exist:"
  for workflow in "${EXPECTED_WORKFLOWS[@]}"; do
    echo "   - ${workflow}"
  done
  echo ""
  echo "4. For each workflow:"
  echo "   - Open the workflow"
  echo "   - Check if toggle switch is 'Active' (green/blue)"
  echo "   - If 'Inactive', toggle it to 'Active'"
  echo ""
else
  # Parse workflows
  echo -e "${BLUE}Found Workflows:${NC}"
  echo ""
  
  for workflow in "${EXPECTED_WORKFLOWS[@]}"; do
    WORKFLOW_INFO=$(echo "$WORKFLOWS_JSON" | python3 -c "
import json, sys
try:
    workflows = json.load(sys.stdin)
    for wf in workflows:
        if '$workflow' in wf.get('name', ''):
            print(f\"{wf.get('id', 'unknown')}|{wf.get('name', 'Unknown')}|{wf.get('active', False)}\")
            break
except:
    pass
" 2>/dev/null)
    
    if [ -n "$WORKFLOW_INFO" ]; then
      IFS='|' read -r wf_id wf_name wf_active <<< "$WORKFLOW_INFO"
      if [ "$wf_active" = "True" ] || [ "$wf_active" = "true" ]; then
        echo -e "  ${GREEN}✅${NC} ${wf_name} (Active)"
      else
        echo -e "  ${YELLOW}⏸️${NC} ${wf_name} (Inactive - needs activation)"
      fi
    else
      echo -e "  ${RED}❌${NC} ${workflow} (Not found - needs import)"
    fi
  done
  echo ""
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📋 Next Steps${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "If workflows are missing:"
echo "  1. Import via n8n UI: ${PI_N8N_URL}"
echo "  2. Workflows → Import from File"
echo "  3. Import workflow JSON files from project directory"
echo ""
echo "If workflows exist but are inactive:"
echo "  1. Open each workflow in n8n UI"
echo "  2. Toggle 'Inactive' → 'Active' (top-right switch)"
echo "  3. Switch should turn green/blue when active"
echo ""
echo "After activation, test with:"
echo "  curl -X POST \"${PI_N8N_URL}/webhook/book-content-update\" \\"
echo "    -H \"Content-Type: application/json\" \\"
echo "    -d '{\"bookId\": 1, \"content\": {\"title\": \"Test\"}, \"updateType\": \"modify\"}'"
echo ""



