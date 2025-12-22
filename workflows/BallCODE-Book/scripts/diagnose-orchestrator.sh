#!/bin/bash
# Diagnose Unity Build Orchestrator Issues
# Comprehensive diagnostic for orchestrator workflow problems

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
echo -e "${BLUE}🔍 Unity Build Orchestrator Diagnostic${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Step 1: Check n8n accessibility
echo -e "${CYAN}Step 1: Checking n8n instance...${NC}"
if ! curl -s -f "${N8N_URL}/healthz" > /dev/null 2>&1; then
    echo -e "${RED}❌ n8n not accessible at ${N8N_URL}${NC}"
    echo -e "${YELLOW}💡 Check if n8n is running${NC}"
    exit 1
fi
echo -e "${GREEN}✅ n8n is accessible${NC}"
echo ""

# Step 2: Test webhook endpoint
echo -e "${CYAN}Step 2: Testing webhook endpoint...${NC}"
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Diagnostic test", "branch": "main"}' 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2 || echo "000")
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Webhook responds (HTTP $HTTP_CODE)${NC}"
    echo -e "${CYAN}Response: ${BODY:0:200}${NC}"
elif [ "$HTTP_CODE" = "404" ]; then
    echo -e "${RED}❌ Webhook not found (404)${NC}"
    echo -e "${YELLOW}💡 Workflow may not be imported or webhook path is wrong${NC}"
    echo -e "${YELLOW}💡 Check n8n UI: Is workflow imported? Is it active?${NC}"
elif [ "$HTTP_CODE" = "000" ]; then
    echo -e "${RED}❌ No response from webhook${NC}"
    echo -e "${YELLOW}💡 Workflow may not be active${NC}"
    echo -e "${YELLOW}💡 Check n8n UI: Toggle workflow to active${NC}"
else
    echo -e "${RED}❌ Webhook error (HTTP $HTTP_CODE)${NC}"
    echo -e "${YELLOW}Response: ${BODY:0:500}${NC}"
fi
echo ""

# Step 3: Check environment variables (if we can access n8n API)
echo -e "${CYAN}Step 3: Checking required environment variables...${NC}"
echo -e "${YELLOW}Required variables:${NC}"
echo "  - GITHUB_REPO_OWNER"
echo "  - GITHUB_REPO_NAME"
echo "  - GITHUB_WORKFLOW_FILE"
echo "  - NETLIFY_SITE_ID"
echo "  - NETLIFY_SITE_NAME"
echo "  - N8N_INSTANCE_ROLE"
echo -e "${YELLOW}💡 Check these in n8n Settings → Environment Variables${NC}"
echo ""

# Step 4: Check credentials
echo -e "${CYAN}Step 4: Checking required credentials...${NC}"
echo -e "${YELLOW}Required credentials:${NC}"
echo "  - github-actions-token (HTTP Header Auth)"
echo "  - netlify-api-token (HTTP Header Auth)"
echo -e "${YELLOW}💡 Check these in n8n Settings → Credentials${NC}"
echo ""

# Step 5: Check workflow file
echo -e "${CYAN}Step 5: Checking workflow file...${NC}"
WORKFLOW_FILE="n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"
if [ -f "$WORKFLOW_FILE" ]; then
    echo -e "${GREEN}✅ Workflow file exists: ${WORKFLOW_FILE}${NC}"
    
    # Check if JSON is valid
    if python3 -m json.tool "$WORKFLOW_FILE" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Workflow JSON is valid${NC}"
    else
        echo -e "${RED}❌ Workflow JSON is invalid${NC}"
        echo -e "${YELLOW}💡 Try using cleaned version: n8n-unity-build-orchestrator-CLEANED-FOR-IMPORT.json${NC}"
    fi
else
    echo -e "${RED}❌ Workflow file not found: ${WORKFLOW_FILE}${NC}"
    echo -e "${YELLOW}💡 Check if file exists in current directory${NC}"
fi
echo ""

# Step 6: Recommendations
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}💡 RECOMMENDATIONS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ "$HTTP_CODE" = "404" ] || [ "$HTTP_CODE" = "000" ]; then
    echo -e "${YELLOW}1. Import/Re-import workflow:${NC}"
    echo "   - Go to n8n UI → Workflows → Import from File"
    echo "   - Select: n8n-unity-build-orchestrator-CLEANED-FOR-IMPORT.json"
    echo "   - Or try: n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"
    echo ""
    echo -e "${YELLOW}2. Activate workflow:${NC}"
    echo "   - Open workflow in n8n UI"
    echo "   - Toggle 'Active' switch to ON"
    echo ""
fi

echo -e "${YELLOW}3. Verify environment variables:${NC}"
echo "   - n8n Settings → Environment Variables"
echo "   - Ensure all required variables are set"
echo ""

echo -e "${YELLOW}4. Verify credentials:${NC}"
echo "   - n8n Settings → Credentials"
echo "   - Ensure github-actions-token and netlify-api-token exist"
echo ""

echo -e "${YELLOW}5. Check n8n logs:${NC}"
echo "   - n8n UI → Executions"
echo "   - Look for error messages"
echo ""

echo -e "${YELLOW}6. Try alternative workflow file:${NC}"
echo "   - n8n-unity-build-orchestrator-CLEANED-FOR-IMPORT.json"
echo "   - n8n-unity-build-orchestrator-NEW-FROM-SCRATCH.json"
echo ""

echo -e "${CYAN}For more help, see: BALLCODE-N8N-COMMAND-REFERENCE.md${NC}"
echo ""

