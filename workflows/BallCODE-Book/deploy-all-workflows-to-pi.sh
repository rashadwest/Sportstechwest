#!/bin/bash
# Deploy All BallCODE Workflows to Pi n8n Instance
# Automated deployment script for all Phase 1 and Phase 2 workflows

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🤖 Automated Workflow Deployment to Pi n8n${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Pi n8n configuration
PI_N8N_URL="http://192.168.1.226:5678"
PROJECT_DIR="/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"

# Change to project directory
cd "$PROJECT_DIR" || {
  echo -e "${RED}❌ Error: Cannot access project directory: $PROJECT_DIR${NC}"
  exit 1
}

# Load environment variables if available
if [ -f .n8n-env.pi ]; then
  source .n8n-env.pi
  echo -e "${GREEN}✅ Loaded Pi environment configuration${NC}"
fi

# Use API key if available, otherwise proceed without it
N8N_API_KEY="${N8N_API_KEY:-}"

# Check if Pi n8n is accessible
echo -e "${YELLOW}🔍 Checking Pi n8n connection...${NC}"
if curl -s -f "${PI_N8N_URL}/healthz" > /dev/null 2>&1 || curl -s -f "${PI_N8N_URL}" > /dev/null 2>&1; then
  echo -e "${GREEN}✅ Pi n8n is accessible at ${PI_N8N_URL}${NC}"
else
  echo -e "${RED}❌ Cannot connect to Pi n8n at ${PI_N8N_URL}${NC}"
  echo "   Make sure n8n is running on the Pi"
  exit 1
fi
echo ""

# Workflows to deploy
WORKFLOWS=(
  "n8n-ballcode-full-integration-workflow.json:Phase 1 - Full Integration"
  "n8n-screenshot-to-fix-workflow.json:Phase 1 - Screenshot to Fix"
  "n8n-book-content-update-workflow.json:Phase 2 - Book Content Update"
  "n8n-curriculum-sync-workflow.json:Phase 2 - Curriculum Sync"
  "n8n-game-exercise-integration-workflow.json:Phase 2 - Game Exercise Integration"
)

# Function to deploy a workflow
deploy_workflow() {
  local workflow_file="$1"
  local workflow_name="$2"
  
  echo -e "${YELLOW}📦 Deploying: ${workflow_name}${NC}"
  echo "   File: ${workflow_file}"
  
  # Check if file exists
  if [ ! -f "$workflow_file" ]; then
    echo -e "${RED}   ❌ File not found: ${workflow_file}${NC}"
    return 1
  fi
  
  # Validate JSON
  if ! python3 -m json.tool "$workflow_file" > /dev/null 2>&1; then
    echo -e "${RED}   ❌ Invalid JSON in ${workflow_file}${NC}"
    return 1
  fi
  
  # Deploy via API
  if [ -n "$N8N_API_KEY" ]; then
    # With API key
    RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
      -H "X-N8N-API-KEY: ${N8N_API_KEY}" \
      -H "Content-Type: application/json" \
      -d @"${workflow_file}" 2>&1)
  else
    # Without API key (may require authentication)
    RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
      -H "Content-Type: application/json" \
      -d @"${workflow_file}" 2>&1)
  fi
  
  HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
  BODY=$(echo "$RESPONSE" | sed '$d')
  
  if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    WORKFLOW_ID=$(echo "$BODY" | python3 -c "import json, sys; print(json.load(sys.stdin).get('id', 'unknown'))" 2>/dev/null || echo "unknown")
    echo -e "${GREEN}   ✅ Deployed successfully (ID: ${WORKFLOW_ID})${NC}"
    
    # Try to activate workflow
    if [ -n "$N8N_API_KEY" ] && [ "$WORKFLOW_ID" != "unknown" ]; then
      ACTIVATE_RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows/${WORKFLOW_ID}/activate" \
        -H "X-N8N-API-KEY: ${N8N_API_KEY}" 2>&1)
      ACTIVATE_CODE=$(echo "$ACTIVATE_RESPONSE" | tail -n1)
      
      if [ "$ACTIVATE_CODE" = "200" ]; then
        echo -e "${GREEN}   ✅ Activated successfully${NC}"
      else
        echo -e "${YELLOW}   ⚠️  Deployed but not activated (activate manually in n8n UI)${NC}"
      fi
    else
      echo -e "${YELLOW}   ⚠️  Deployed but not activated (activate manually in n8n UI)${NC}"
    fi
    
    return 0
  else
    echo -e "${RED}   ❌ Deployment failed (HTTP ${HTTP_CODE})${NC}"
    echo "   Response: ${BODY}"
    return 1
  fi
}

# Deploy all workflows
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📤 Deploying Workflows to Pi n8n${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

SUCCESS_COUNT=0
FAIL_COUNT=0

for workflow_entry in "${WORKFLOWS[@]}"; do
  IFS=':' read -r workflow_file workflow_name <<< "$workflow_entry"
  
  if deploy_workflow "$workflow_file" "$workflow_name"; then
    ((SUCCESS_COUNT++))
  else
    ((FAIL_COUNT++))
  fi
  echo ""
done

# Summary
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 Deployment Summary${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "✅ Successful: ${GREEN}${SUCCESS_COUNT}${NC}"
echo -e "❌ Failed: ${RED}${FAIL_COUNT}${NC}"
echo ""

if [ $FAIL_COUNT -eq 0 ]; then
  echo -e "${GREEN}🎉 All workflows deployed successfully!${NC}"
  echo ""
  echo "Next steps:"
  echo "1. Open Pi n8n UI: ${PI_N8N_URL}"
  echo "2. Verify all workflows are imported"
  echo "3. Activate workflows (toggle switch in top-right)"
  echo "4. Test workflows using the execute commands"
  echo ""
  echo "Test commands:"
  echo "  curl -X POST \"${PI_N8N_URL}/webhook/book-content-update\" \\"
  echo "    -H \"Content-Type: application/json\" \\"
  echo "    -d '{\"bookId\": 1, \"content\": {\"title\": \"Test\"}, \"updateType\": \"modify\"}'"
else
  echo -e "${YELLOW}⚠️  Some workflows failed to deploy${NC}"
  echo "   Check the errors above and try again"
  echo "   You may need to import manually via n8n UI"
fi
echo ""



