#!/bin/bash
# Push All 5 AIMCODE Solutions via CLI - Test Each One
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuration
PI_N8N_URL="http://192.168.1.226:5678"

# Load API key
if [ -f ../.n8n-env.pi ]; then
    source ../.n8n-env.pi 2>/dev/null
fi

if [ -z "$N8N_API_KEY" ]; then
    echo -e "${RED}❌ N8N_API_KEY not set${NC}"
    echo "Set it in .n8n-env.pi or export N8N_API_KEY=your_key"
    exit 1
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 Pushing All 5 AIMCODE Solutions${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Function to push a solution
push_solution() {
    local solution_num=$1
    local solution_file=$2
    local solution_name=$3
    
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}Solution $solution_num: $solution_name${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    if [ ! -f "$solution_file" ]; then
        echo -e "${RED}❌ File not found: $solution_file${NC}"
        return 1
    fi
    
    echo -e "${BLUE}📤 Pushing to n8n...${NC}"
    
    RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
      -H "X-N8N-API-KEY: $N8N_API_KEY" \
      -H "Content-Type: application/json" \
      -d @"$solution_file")
    
    HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
    BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')
    
    if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
        WORKFLOW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
        WORKFLOW_NAME=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('name', ''))" 2>/dev/null || echo "")
        
        echo -e "${GREEN}✅ SUCCESS! Solution $solution_num imported${NC}"
        echo -e "${GREEN}   Workflow ID: $WORKFLOW_ID${NC}"
        echo -e "${GREEN}   Name: $WORKFLOW_NAME${NC}"
        echo ""
        echo -e "${YELLOW}📝 Test it:${NC}"
        echo "   curl -X POST ${PI_N8N_URL}/webhook/unity-build -H 'Content-Type: application/json' -d '{\"request\":\"Test\",\"branch\":\"main\"}'"
        echo ""
        echo -e "${YELLOW}⚠️  Remember to activate it in n8n UI${NC}"
        echo ""
        return 0
    else
        echo -e "${RED}❌ FAILED (HTTP $HTTP_CODE)${NC}"
        echo ""
        echo "Response:"
        echo "$BODY" | head -10
        echo ""
        return 1
    fi
}

# Push all 5 solutions
cd "$(dirname "$0")/.." || exit 1

echo -e "${BLUE}Starting to push all 5 solutions...${NC}"
echo ""

# Solution 1: Remove all empty options
push_solution 1 "/tmp/orchestrator-solution-1.json" "Remove All Empty Options"
SOLUTION1_RESULT=$?

echo ""
sleep 2

# Solution 2: Fix respondToWebhook
push_solution 2 "/tmp/orchestrator-solution-2.json" "Fix respondToWebhook Specifically"
SOLUTION2_RESULT=$?

echo ""
sleep 2

# Solution 3: Ultra-minimal
push_solution 3 "/tmp/orchestrator-solution-3.json" "Ultra-Minimal Structure"
SOLUTION3_RESULT=$?

echo ""
sleep 2

# Solution 4: Direct headers
push_solution 4 "/tmp/orchestrator-solution-4.json" "Direct Headers (No options.headers)"
SOLUTION4_RESULT=$?

echo ""
sleep 2

# Solution 5: Rebuild minimal
push_solution 5 "/tmp/orchestrator-solution-5.json" "Rebuild Minimal (4 Nodes)"
SOLUTION5_RESULT=$?

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 RESULTS SUMMARY${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

SUCCESS_COUNT=0
[ "$SOLUTION1_RESULT" = "0" ] && SUCCESS_COUNT=$((SUCCESS_COUNT + 1)) && echo -e "${GREEN}✅ Solution 1: SUCCESS${NC}" || echo -e "${RED}❌ Solution 1: FAILED${NC}"
[ "$SOLUTION2_RESULT" = "0" ] && SUCCESS_COUNT=$((SUCCESS_COUNT + 1)) && echo -e "${GREEN}✅ Solution 2: SUCCESS${NC}" || echo -e "${RED}❌ Solution 2: FAILED${NC}"
[ "$SOLUTION3_RESULT" = "0" ] && SUCCESS_COUNT=$((SUCCESS_COUNT + 1)) && echo -e "${GREEN}✅ Solution 3: SUCCESS${NC}" || echo -e "${RED}❌ Solution 3: FAILED${NC}"
[ "$SOLUTION4_RESULT" = "0" ] && SUCCESS_COUNT=$((SUCCESS_COUNT + 1)) && echo -e "${GREEN}✅ Solution 4: SUCCESS${NC}" || echo -e "${RED}❌ Solution 4: FAILED${NC}"
[ "$SOLUTION5_RESULT" = "0" ] && SUCCESS_COUNT=$((SUCCESS_COUNT + 1)) && echo -e "${GREEN}✅ Solution 5: SUCCESS${NC}" || echo -e "${RED}❌ Solution 5: FAILED${NC}"

echo ""
echo -e "${BLUE}Total Success: $SUCCESS_COUNT / 5${NC}"
echo ""
echo -e "${YELLOW}📝 Next Steps:${NC}"
echo "1. Check n8n UI: $PI_N8N_URL"
echo "2. Find the imported workflows"
echo "3. Activate each one (toggle ON)"
echo "4. Test each webhook"
echo "5. See which one works!"
echo ""

