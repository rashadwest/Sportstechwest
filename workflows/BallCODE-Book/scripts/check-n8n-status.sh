#!/bin/bash
# Check n8n Workflow Status - Quick Status Report
# Shows which workflows are imported, active, and working

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Get n8n URL from environment or use default
N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"
N8N_API_KEY="${N8N_API_KEY:-}"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 BallCODE n8n Workflow Status Check${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if n8n is accessible
echo -e "${CYAN}Checking n8n instance at: ${N8N_URL}${NC}"
if ! curl -s -f "${N8N_URL}/healthz" > /dev/null 2>&1; then
    echo -e "${RED}❌ n8n instance not accessible at ${N8N_URL}${NC}"
    echo -e "${YELLOW}💡 Check if n8n is running and URL is correct${NC}"
    exit 1
fi
echo -e "${GREEN}✅ n8n instance is accessible${NC}"
echo ""

# Get workflows via API (if API key provided) or webhook test
if [ -n "$N8N_API_KEY" ]; then
    echo -e "${CYAN}Fetching workflows via API...${NC}"
    WORKFLOWS=$(curl -s -H "X-N8N-API-KEY: ${N8N_API_KEY}" "${N8N_URL}/api/v1/workflows" 2>/dev/null || echo "[]")
else
    echo -e "${YELLOW}⚠️  No API key provided - testing webhooks directly${NC}"
    WORKFLOWS="[]"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🎯 CRITICAL WORKFLOWS STATUS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Test each critical workflow
test_webhook() {
    local name=$1
    local webhook=$2
    local test_data=$3
    
    echo -e "${CYAN}Testing: ${name}${NC}"
    RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}${webhook}" \
      -H "Content-Type: application/json" \
      -d "$test_data" 2>&1)
    
    HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2 || echo "000")
    BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d' | head -c 200)
    
    if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
        echo -e "  ${GREEN}✅ Status: WORKING (HTTP $HTTP_CODE)${NC}"
        return 0
    elif [ "$HTTP_CODE" = "404" ]; then
        echo -e "  ${RED}❌ Status: NOT FOUND (Webhook doesn't exist)${NC}"
        return 1
    elif [ "$HTTP_CODE" = "000" ]; then
        echo -e "  ${YELLOW}⚠️  Status: NO RESPONSE (Workflow may not be active)${NC}"
        return 2
    else
        echo -e "  ${RED}❌ Status: ERROR (HTTP $HTTP_CODE)${NC}"
        echo -e "  ${YELLOW}Response: ${BODY}${NC}"
        return 1
    fi
}

# Test Unity Build Orchestrator
echo -e "${YELLOW}1. Unity Build Orchestrator${NC}"
test_webhook "Unity Build Orchestrator" "/webhook/unity-build" '{"request": "Status check", "branch": "main"}'
ORCHESTRATOR_STATUS=$?
echo ""

# Test Full Integration
echo -e "${YELLOW}2. Full Integration Workflow${NC}"
test_webhook "Full Integration" "/webhook/ballcode-dev" '{"prompt": "Status check", "mode": "quick"}'
FULL_INTEGRATION_STATUS=$?
echo ""

# Test Screenshot Fix
echo -e "${YELLOW}3. Screenshot to Fix Workflow${NC}"
test_webhook "Screenshot Fix" "/webhook/screenshot-fix" '{"screenshotUrl": "https://example.com/test.png", "context": "Status check"}'
SCREENSHOT_STATUS=$?
echo ""

# Summary
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📋 SUMMARY${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ $ORCHESTRATOR_STATUS -eq 0 ]; then
    echo -e "${GREEN}✅ Unity Build Orchestrator: WORKING${NC}"
elif [ $ORCHESTRATOR_STATUS -eq 2 ]; then
    echo -e "${YELLOW}⚠️  Unity Build Orchestrator: NOT ACTIVE (needs activation)${NC}"
else
    echo -e "${RED}❌ Unity Build Orchestrator: NOT WORKING${NC}"
fi

if [ $FULL_INTEGRATION_STATUS -eq 0 ]; then
    echo -e "${GREEN}✅ Full Integration: WORKING${NC}"
elif [ $FULL_INTEGRATION_STATUS -eq 2 ]; then
    echo -e "${YELLOW}⚠️  Full Integration: NOT ACTIVE (needs activation)${NC}"
else
    echo -e "${RED}❌ Full Integration: NOT WORKING${NC}"
fi

if [ $SCREENSHOT_STATUS -eq 0 ]; then
    echo -e "${GREEN}✅ Screenshot Fix: WORKING${NC}"
elif [ $SCREENSHOT_STATUS -eq 2 ]; then
    echo -e "${YELLOW}⚠️  Screenshot Fix: NOT ACTIVE (needs activation)${NC}"
else
    echo -e "${RED}❌ Screenshot Fix: NOT WORKING${NC}"
fi

echo ""
echo -e "${CYAN}💡 Next Steps:${NC}"
echo "  - If workflow shows NOT ACTIVE: Activate it in n8n UI"
echo "  - If workflow shows NOT WORKING: Run diagnostic script"
echo "  - For detailed diagnostics: ./scripts/diagnose-orchestrator.sh"
echo ""

