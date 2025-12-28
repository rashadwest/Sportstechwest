#!/bin/bash
# Test All n8n Workflows - End-to-End Testing Script
# Checks current state, dependencies, and tests each workflow

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
N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"  # Default to Pi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🧪 n8n Workflows - End-to-End Test${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Test n8n connection
echo -e "${CYAN}📡 Testing n8n connection...${NC}"
if curl -s -f "${N8N_URL}/healthz" > /dev/null 2>&1 || curl -s -f "${N8N_URL}" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ n8n is accessible at ${N8N_URL}${NC}"
else
    echo -e "${RED}❌ Cannot connect to n8n at ${N8N_URL}${NC}"
    echo "   Make sure n8n is running"
    exit 1
fi
echo ""

# Check Python scripts
echo -e "${CYAN}🐍 Checking Python scripts...${NC}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKFLOW_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ -f "$WORKFLOW_DIR/scripts/n8n-update-schema.py" ]; then
    echo -e "${GREEN}✅ n8n-update-schema.py exists${NC}"
else
    echo -e "${RED}❌ n8n-update-schema.py missing${NC}"
fi

if [ -f "$WORKFLOW_DIR/screenshot_fix_processor.py" ]; then
    echo -e "${GREEN}✅ screenshot_fix_processor.py exists${NC}"
else
    echo -e "${RED}❌ screenshot_fix_processor.py missing${NC}"
fi
echo ""

# Test Workflow 1: Unity Build Orchestrator
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}1. Testing Unity Build Orchestrator${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}Webhook: /webhook/unity-build${NC}"
RESPONSE=$(curl -s --max-time 30 -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{
    "request": "End-to-end test from terminal",
    "branch": "main"
  }' 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Unity Build webhook working (HTTP $HTTP_CODE)${NC}"
    echo "Response preview: $(echo "$BODY" | head -c 200)..."
else
    echo -e "${RED}❌ Unity Build webhook failed (HTTP $HTTP_CODE)${NC}"
    if [ -n "$BODY" ]; then
        echo "Response: $BODY" | head -c 500
    fi
fi
echo ""

# Test Workflow 2: Full Integration
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}2. Testing Full Integration Workflow${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}Webhook: /webhook/ballcode-dev${NC}"
echo -e "${YELLOW}⏳ This workflow uses AI and may take 30-60 seconds...${NC}"
RESPONSE=$(curl -s --max-time 60 -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Test AI analysis from end-to-end test",
    "mode": "quick"
  }' 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ -z "$HTTP_CODE" ] || [ "$HTTP_CODE" = "000" ]; then
    echo -e "${RED}❌ Full Integration webhook timed out or connection failed${NC}"
    echo -e "${YELLOW}   This workflow uses AI (OpenAI) which can take 30-60+ seconds${NC}"
    echo -e "${YELLOW}   The workflow may not be imported, or it's still processing${NC}"
elif [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Full Integration webhook working (HTTP $HTTP_CODE)${NC}"
    echo "Response preview: $(echo "$BODY" | head -c 200)..."
elif [ "$HTTP_CODE" = "404" ]; then
    echo -e "${YELLOW}⚠️  Full Integration webhook not found (404) - Workflow not imported${NC}"
else
    echo -e "${RED}❌ Full Integration webhook failed (HTTP $HTTP_CODE)${NC}"
    if [ -n "$BODY" ]; then
        echo "Response: $BODY" | head -c 500
    fi
fi
echo ""

# Test Workflow 3: Screenshot to Fix
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}3. Testing Screenshot to Fix Workflow${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}Webhook: /webhook/screenshot-fix${NC}"
echo -e "${YELLOW}⏳ This workflow uses AI Vision and may take 30-60 seconds...${NC}"
RESPONSE=$(curl -s --max-time 60 -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/test-error.png",
    "context": "End-to-end test - n8n workflow error"
  }' 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Screenshot Fix webhook working (HTTP $HTTP_CODE)${NC}"
    echo "Response preview: $(echo "$BODY" | head -c 200)..."
elif [ "$HTTP_CODE" = "404" ]; then
    echo -e "${YELLOW}⚠️  Screenshot Fix webhook not found (404) - Workflow not imported${NC}"
else
    echo -e "${RED}❌ Screenshot Fix webhook failed (HTTP $HTTP_CODE)${NC}"
    if [ -n "$BODY" ]; then
        echo "Response: $BODY" | head -c 500
    fi
fi
echo ""

# Test Workflow 4: Book Content Update
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}4. Testing Book Content Update Workflow${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}Webhook: /webhook/book-content-update${NC}"
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{
    "bookId": 1,
    "content": {
      "title": "Test Book",
      "slug": "test-book",
      "concepts": {"python": "Sequences"},
      "basketball": {"skill": "Pound Dribble"},
      "curriculum": {"gradeLevels": ["3-5"]}
    },
    "updateType": "modify"
  }' 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ -z "$HTTP_CODE" ] || [ "$HTTP_CODE" = "000" ]; then
    echo -e "${RED}❌ Book Content Update webhook timed out or connection failed${NC}"
    echo -e "${YELLOW}   This workflow uses AI which can take 30-60+ seconds${NC}"
    echo -e "${YELLOW}   The workflow may not be imported, or it's still processing${NC}"
elif [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Book Content Update webhook working (HTTP $HTTP_CODE)${NC}"
    echo "Response preview: $(echo "$BODY" | head -c 200)..."
elif [ "$HTTP_CODE" = "404" ]; then
    echo -e "${YELLOW}⚠️  Book Content Update webhook not found (404) - Workflow not imported${NC}"
else
    echo -e "${RED}❌ Book Content Update webhook failed (HTTP $HTTP_CODE)${NC}"
    if [ -n "$BODY" ]; then
        echo "Response: $BODY" | head -c 500
    fi
fi
echo ""

# Test Workflow 5: Curriculum Sync
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}5. Testing Curriculum Sync Workflow${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}Webhook: /webhook/curriculum-sync${NC}"
echo -e "${YELLOW}⏳ This workflow uses AI and may take 30-60 seconds...${NC}"
RESPONSE=$(curl -s --max-time 60 -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{
    "changeType": "newObjective",
    "learningObjective": {
      "objective": "Test objective",
      "gradeLevels": ["3-5"]
    }
  }' 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Curriculum Sync webhook working (HTTP $HTTP_CODE)${NC}"
    echo "Response preview: $(echo "$BODY" | head -c 200)..."
elif [ "$HTTP_CODE" = "404" ]; then
    echo -e "${YELLOW}⚠️  Curriculum Sync webhook not found (404) - Workflow not imported${NC}"
else
    echo -e "${RED}❌ Curriculum Sync webhook failed (HTTP $HTTP_CODE)${NC}"
    if [ -n "$BODY" ]; then
        echo "Response: $BODY" | head -c 500
    fi
fi
echo ""

# Test Workflow 6: Game Exercise Integration
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}6. Testing Game Exercise Integration Workflow${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}Webhook: /webhook/game-exercise-integration${NC}"
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{
    "exerciseType": "new",
    "exerciseData": {
      "exerciseId": "test-exercise-1",
      "bookId": 1,
      "difficulty": "beginner",
      "concept": "Sequences"
    }
  }' 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ -z "$HTTP_CODE" ] || [ "$HTTP_CODE" = "000" ]; then
    echo -e "${RED}❌ Game Exercise Integration webhook timed out or connection failed${NC}"
    echo -e "${YELLOW}   This workflow uses AI which can take 30-60+ seconds${NC}"
    echo -e "${YELLOW}   The workflow may not be imported, or it's still processing${NC}"
elif [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Game Exercise Integration webhook working (HTTP $HTTP_CODE)${NC}"
    echo "Response preview: $(echo "$BODY" | head -c 200)..."
elif [ "$HTTP_CODE" = "404" ]; then
    echo -e "${YELLOW}⚠️  Game Exercise Integration webhook not found (404) - Workflow not imported${NC}"
else
    echo -e "${RED}❌ Game Exercise Integration webhook failed (HTTP $HTTP_CODE)${NC}"
    if [ -n "$BODY" ]; then
        echo "Response: $BODY" | head -c 500
    fi
fi
echo ""

# Summary
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 Test Summary${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Next steps:"
echo "1. Review test results above"
echo "2. Import missing workflows (404 errors)"
echo "3. Configure environment variables and credentials"
echo "4. Recreate Game Exercise Integration workflow (file is empty)"
echo "5. Run this test again to verify all workflows"
echo ""
echo -e "${CYAN}📖 See N8N-WORKFLOWS-END-TO-END-ANALYSIS.md for detailed analysis${NC}"
echo ""


