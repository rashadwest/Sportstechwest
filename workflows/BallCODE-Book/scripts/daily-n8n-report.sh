#!/bin/bash
# Daily n8n Workflow Report
# Shows yesterday's executions and today's recommended actions

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 BallCODE n8n Daily Report${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Get current date
TODAY=$(date +%Y-%m-%d)
YESTERDAY=$(date -v-1d +%Y-%m-%d 2>/dev/null || date -d "yesterday" +%Y-%m-%d)

echo -e "${CYAN}Report Date: ${TODAY}${NC}"
echo -e "${CYAN}Yesterday: ${YESTERDAY}${NC}"
echo ""

# Check workflow status
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📋 WORKFLOW STATUS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Quick status check for each workflow
check_workflow() {
    local name=$1
    local webhook=$2
    local test_data=$3
    
    RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}${webhook}" \
      -H "Content-Type: application/json" \
      -d "$test_data" 2>&1)
    
    HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2 || echo "000")
    
    if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
        echo -e "  ${GREEN}✅ ${name}: WORKING${NC}"
        return 0
    elif [ "$HTTP_CODE" = "404" ]; then
        echo -e "  ${RED}❌ ${name}: NOT FOUND${NC}"
        return 1
    elif [ "$HTTP_CODE" = "000" ]; then
        echo -e "  ${YELLOW}⚠️  ${name}: NOT ACTIVE${NC}"
        return 2
    else
        echo -e "  ${RED}❌ ${name}: ERROR (HTTP $HTTP_CODE)${NC}"
        return 1
    fi
}

echo -e "${YELLOW}1. Unity Build Orchestrator${NC}"
check_workflow "Unity Build Orchestrator" "/webhook/unity-build" '{"request": "Status check", "branch": "main"}'
ORCHESTRATOR_STATUS=$?

echo ""
echo -e "${YELLOW}2. Full Integration Workflow${NC}"
check_workflow "Full Integration" "/webhook/ballcode-dev" '{"prompt": "Status check", "mode": "quick"}'
FULL_INTEGRATION_STATUS=$?

echo ""
echo -e "${YELLOW}3. Screenshot to Fix Workflow${NC}"
check_workflow "Screenshot Fix" "/webhook/screenshot-fix" '{"screenshotUrl": "https://example.com/test.png", "context": "Status check"}'
SCREENSHOT_STATUS=$?

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📝 TODAY'S RECOMMENDED ACTIONS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

ACTION_COUNT=0

if [ $ORCHESTRATOR_STATUS -ne 0 ]; then
    ACTION_COUNT=$((ACTION_COUNT + 1))
    echo -e "${RED}[ ] ${ACTION_COUNT}. Fix Unity Build Orchestrator (Priority: HIGH)${NC}"
    echo -e "   ${YELLOW}   Run: ./scripts/diagnose-orchestrator.sh${NC}"
    echo -e "   ${YELLOW}   Check: n8n UI for workflow status${NC}"
    echo ""
fi

if [ $FULL_INTEGRATION_STATUS -ne 0 ]; then
    ACTION_COUNT=$((ACTION_COUNT + 1))
    echo -e "${YELLOW}[ ] ${ACTION_COUNT}. Verify Full Integration workflow${NC}"
    echo -e "   ${CYAN}   Check: OpenAI credentials${NC}"
    echo -e "   ${CYAN}   Check: WORKFLOW_PATH environment variable${NC}"
    echo ""
fi

if [ $SCREENSHOT_STATUS -ne 0 ]; then
    ACTION_COUNT=$((ACTION_COUNT + 1))
    echo -e "${YELLOW}[ ] ${ACTION_COUNT}. Verify Screenshot Fix workflow${NC}"
    echo -e "   ${CYAN}   Test: ./scripts/test-screenshot-fix.sh${NC}"
    echo ""
fi

if [ $ACTION_COUNT -eq 0 ]; then
    echo -e "${GREEN}✅ All workflows are working!${NC}"
    echo ""
    echo -e "${CYAN}💡 Optional actions:${NC}"
    echo "  - Test Full Integration with a new prompt"
    echo "  - Review yesterday's workflow executions in n8n UI"
    echo ""
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}💡 QUICK COMMANDS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${CYAN}Check status:${NC} ./scripts/check-n8n-status.sh"
echo -e "${CYAN}Diagnose orchestrator:${NC} ./scripts/diagnose-orchestrator.sh"
echo -e "${CYAN}Test all webhooks:${NC} ./scripts/test-all-webhooks.sh"
echo -e "${CYAN}Full reference:${NC} BALLCODE-N8N-COMMAND-REFERENCE.md"
echo ""


