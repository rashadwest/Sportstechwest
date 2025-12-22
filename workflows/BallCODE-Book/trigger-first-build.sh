#!/bin/bash

# Trigger First Build - n8n Unity Automation Workflow
# This script triggers your workflow via webhook

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Triggering First Build${NC}"
echo ""

# n8n URL (Raspberry Pi)
N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"
WEBHOOK_PATH="unity-dev"
WEBHOOK_URL="${N8N_URL}/webhook/${WEBHOOK_PATH}"

echo -e "${BLUE}Webhook URL: ${WEBHOOK_URL}${NC}"
echo ""

# Request message
REQUEST_MESSAGE="${1:-First build - Initial deployment}"

echo -e "${YELLOW}Sending request: ${REQUEST_MESSAGE}${NC}"
echo ""

# Send POST request to webhook
RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "${WEBHOOK_URL}" \
  -H "Content-Type: application/json" \
  -d "{\"request\": \"${REQUEST_MESSAGE}\"}")

# Extract HTTP status code (last line)
HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
BODY=$(echo "$RESPONSE" | sed '$d')

echo -e "${BLUE}Response Status: ${HTTP_CODE}${NC}"
echo ""

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Workflow triggered successfully!${NC}"
    echo ""
    echo -e "${BLUE}Response:${NC}"
    echo "$BODY" | jq '.' 2>/dev/null || echo "$BODY"
    echo ""
    echo -e "${YELLOW}📊 Check workflow execution in n8n:${NC}"
    echo -e "   ${N8N_URL}/executions"
    echo ""
    echo -e "${GREEN}✅ Build process started!${NC}"
    echo -e "${YELLOW}   The workflow will:${NC}"
    echo "   1. Analyze the request"
    echo "   2. Check if Unity edits needed"
    echo "   3. Pull latest code"
    echo "   4. Commit & push changes"
    echo "   5. Trigger GitHub Actions build"
    echo "   6. Wait for build completion"
    echo "   7. Deploy to Netlify"
    echo ""
else
    echo -e "${RED}❌ Failed to trigger workflow${NC}"
    echo ""
    echo -e "${YELLOW}Response:${NC}"
    echo "$BODY"
    echo ""
    echo -e "${YELLOW}Troubleshooting:${NC}"
    echo "1. Check if n8n is running: curl ${N8N_URL}/healthz"
    echo "2. Check if workflow is active in n8n UI"
    echo "3. Verify webhook path is correct: ${WEBHOOK_PATH}"
    echo "4. Try manual trigger in n8n UI instead"
    exit 1
fi


