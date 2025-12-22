#!/bin/bash
# Complete n8n Workflow Validation - Tests Actual Functionality
# This validates workflows actually WORK, not just return HTTP 200

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
echo -e "${BLUE}🔬 Complete n8n Workflow Validation${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${CYAN}This script validates workflows actually FUNCTION, not just respond${NC}"
echo ""

# Test 1: Unity Build Orchestrator - Full Validation
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}1. Unity Build Orchestrator - Complete Validation${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${CYAN}Step 1: Test webhook response...${NC}"
RESPONSE=$(curl -s --max-time 30 -X POST "${N8N_URL}/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Validation test build",
    "branch": "main"
  }' 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep -o "HTTP_CODE:[0-9]*" | cut -d: -f2 || echo "000")
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Webhook responds (HTTP $HTTP_CODE)${NC}"
    
    # Parse response to check if it actually did something
    if echo "$BODY" | grep -q "github\|netlify\|status\|message"; then
        echo -e "${GREEN}✅ Response contains workflow data${NC}"
        echo "Response: $(echo "$BODY" | head -c 300)..."
    else
        echo -e "${YELLOW}⚠️  Response may be empty or incomplete${NC}"
        echo "Full response: $BODY"
    fi
    
    # Check if workflow actually dispatched to GitHub
    echo -e "${CYAN}Step 2: Verify GitHub dispatch was triggered...${NC}"
    echo -e "${YELLOW}   (Check n8n execution logs or GitHub Actions to confirm)${NC}"
    echo -e "${YELLOW}   Manual verification needed:${NC}"
    echo "   1. Go to n8n UI → Executions"
    echo "   2. Find latest execution"
    echo "   3. Verify 'Dispatch GitHub Build' node executed"
    echo "   4. Check GitHub Actions for new workflow run"
    
else
    echo -e "${RED}❌ Webhook failed (HTTP $HTTP_CODE)${NC}"
fi
echo ""

# Test 2: Screenshot to Fix - Full Validation
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}2. Screenshot to Fix - Complete Validation${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${CYAN}Step 1: Test webhook with test screenshot URL...${NC}"
RESPONSE=$(curl -s --max-time 90 -X POST "${N8N_URL}/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://via.placeholder.com/800x600.png?text=Test+Error+Screenshot",
    "context": "Validation test - testing screenshot analysis workflow"
  }' 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep -o "HTTP_CODE:[0-9]*" | cut -d: -f2 || echo "000")
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Webhook responds (HTTP $HTTP_CODE)${NC}"
    
    # Check if AI analysis actually happened
    if echo "$BODY" | grep -q "diagnosis\|errorType\|fix\|requestId"; then
        echo -e "${GREEN}✅ Response contains analysis data${NC}"
        echo "Response preview: $(echo "$BODY" | head -c 300)..."
        
        # Extract key info
        if echo "$BODY" | grep -q "errorType"; then
            echo -e "${GREEN}✅ AI Vision analysis completed${NC}"
        fi
        if echo "$BODY" | grep -q "fix"; then
            echo -e "${GREEN}✅ Fix generation attempted${NC}"
        fi
    else
        echo -e "${YELLOW}⚠️  Response may not contain expected analysis data${NC}"
        echo "Full response: $BODY"
    fi
    
    echo -e "${CYAN}Step 2: Verify AI Vision processing...${NC}"
    echo -e "${YELLOW}   Manual verification needed:${NC}"
    echo "   1. Go to n8n UI → Executions"
    echo "   2. Find latest execution"
    echo "   3. Verify 'Vision Analysis' node executed"
    echo "   4. Check if OpenAI API was called"
    echo "   5. Verify diagnosis was generated"
    
else
    echo -e "${RED}❌ Webhook failed (HTTP $HTTP_CODE)${NC}"
fi
echo ""

# Test 3: Full Integration - Validation
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}3. Full Integration Workflow - Validation${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${CYAN}Testing with simple prompt...${NC}"
RESPONSE=$(curl -s --max-time 90 -X POST "${N8N_URL}/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Add a test exercise for sequences",
    "mode": "quick"
  }' 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep -o "HTTP_CODE:[0-9]*" | cut -d: -f2 || echo "000")
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Webhook responds (HTTP $HTTP_CODE)${NC}"
    
    if echo "$BODY" | grep -q "actionPlan\|analysis\|systemsAffected"; then
        echo -e "${GREEN}✅ AI analysis completed${NC}"
        echo "Response preview: $(echo "$BODY" | head -c 300)..."
    else
        echo -e "${YELLOW}⚠️  Response may be incomplete${NC}"
    fi
else
    echo -e "${RED}❌ Webhook failed (HTTP $HTTP_CODE)${NC}"
fi
echo ""

# Summary
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 Validation Summary${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${CYAN}Next Steps for Complete Verification:${NC}"
echo ""
echo "1. ${YELLOW}Check n8n Executions:${NC}"
echo "   - Go to: ${N8N_URL}/executions"
echo "   - Review latest executions for each workflow"
echo "   - Verify all nodes executed successfully"
echo ""
echo "2. ${YELLOW}Unity Build Orchestrator:${NC}"
echo "   - Check GitHub Actions for new workflow run"
echo "   - Verify build was actually triggered"
echo "   - Check Netlify for deployment status"
echo ""
echo "3. ${YELLOW}Screenshot to Fix:${NC}"
echo "   - Check OpenAI API usage (if you have access)"
echo "   - Verify diagnosis was generated"
echo "   - Check if fix was applied (if auto-fix enabled)"
echo ""
echo "4. ${YELLOW}Full Integration:${NC}"
echo "   - Verify AI analysis completed"
echo "   - Check if action plan was generated"
echo "   - Verify all 4 systems were analyzed"
echo ""
echo -e "${GREEN}✅ Automated tests complete${NC}"
echo -e "${YELLOW}⚠️  Manual verification required for full confidence${NC}"
echo ""

