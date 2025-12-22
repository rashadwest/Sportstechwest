#!/bin/bash
# Test All n8n Webhooks - Terminal Testing Script
# Tests webhooks without needing to click "Listen for test event" in UI

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Get n8n URL from environment or use default
# DEFAULT: Pi n8n (production) - Mac only when explicitly requested
N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"  # Default to Pi
PI_N8N_URL="${PI_N8N_URL:-http://192.168.1.226:5678}"
LOCAL_N8N_URL="${LOCAL_N8N_URL:-http://localhost:5678}"  # Mac only when requested

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🧪 Test All n8n Webhooks${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Ask which n8n instance (default to Pi)
echo -e "${YELLOW}Which n8n instance?${NC}"
echo "1) Pi (192.168.1.226:5678) [DEFAULT - Production]"
echo "2) Local (localhost:5678) [Mac - Testing Only]"
read -p "Choice [1-2] (default: 1): " choice

if [ "$choice" = "2" ]; then
    N8N_URL="$LOCAL_N8N_URL"
    echo -e "${YELLOW}⚠️  Using Mac n8n (localhost) - Testing Only${NC}"
else
    N8N_URL="$PI_N8N_URL"
    echo -e "${GREEN}✅ Using Pi n8n (Production)${NC}"
fi

echo ""
echo -e "${BLUE}Testing webhooks at: ${N8N_URL}${NC}"
echo ""

# Test 1: Unity Build Orchestrator
echo -e "${YELLOW}1. Testing Unity Build Orchestrator...${NC}"
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Test build from terminal",
    "branch": "main"
  }')

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Unity Build webhook working${NC}"
    echo "Response: $BODY" | head -c 200
    echo "..."
else
    echo -e "${RED}❌ Unity Build webhook failed (HTTP $HTTP_CODE)${NC}"
    echo "Response: $BODY"
fi
echo ""

# Test 2: Full Integration Simplified
echo -e "${YELLOW}2. Testing Full Integration Simplified...${NC}"
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Test AI analysis from terminal",
    "mode": "quick"
  }')

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Full Integration webhook working${NC}"
    echo "Response: $BODY" | head -c 200
    echo "..."
else
    echo -e "${RED}❌ Full Integration webhook failed (HTTP $HTTP_CODE)${NC}"
    echo "Response: $BODY"
fi
echo ""

# Test 3: Screenshot to Fix
echo -e "${YELLOW}3. Testing Screenshot to Fix...${NC}"
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/test-error.png",
    "context": "Terminal test - n8n workflow error"
  }')

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Screenshot Fix webhook working${NC}"
    echo "Response: $BODY" | head -c 200
    echo "..."
else
    echo -e "${RED}❌ Screenshot Fix webhook failed (HTTP $HTTP_CODE)${NC}"
    echo "Response: $BODY"
fi
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}✅ Testing Complete${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

