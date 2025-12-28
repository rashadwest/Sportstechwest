#!/bin/bash
# Test Screenshot to Fix Workflow
# Interactive test script for screenshot fix workflow

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
echo -e "${BLUE}📸 Screenshot to Fix Workflow - Test${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Get screenshot URL
echo -e "${CYAN}Enter screenshot URL (must be publicly accessible):${NC}"
read -p "Screenshot URL: " SCREENSHOT_URL

if [ -z "$SCREENSHOT_URL" ]; then
    echo -e "${RED}❌ Screenshot URL is required${NC}"
    exit 1
fi

# Get context
echo ""
echo -e "${CYAN}Enter context/description:${NC}"
read -p "Context: " CONTEXT

if [ -z "$CONTEXT" ]; then
    CONTEXT="Test screenshot fix"
fi

# Optional fields
echo ""
echo -e "${CYAN}Optional fields (press Enter to skip):${NC}"
read -p "Error Type (e.g., build_failure, runtime_error): " ERROR_TYPE
read -p "System (e.g., unity, n8n, website): " SYSTEM
read -p "Urgency (low, medium, high): " URGENCY

# Build request JSON
REQUEST_JSON="{"
REQUEST_JSON+="\"screenshotUrl\": \"${SCREENSHOT_URL}\","
REQUEST_JSON+="\"context\": \"${CONTEXT}\""

if [ -n "$ERROR_TYPE" ]; then
    REQUEST_JSON+=",\"errorType\": \"${ERROR_TYPE}\""
fi

if [ -n "$SYSTEM" ]; then
    REQUEST_JSON+=",\"system\": \"${SYSTEM}\""
fi

if [ -n "$URGENCY" ]; then
    REQUEST_JSON+=",\"urgency\": \"${URGENCY}\""
fi

REQUEST_JSON+="}"

echo ""
echo -e "${CYAN}Sending request to: ${N8N_URL}/webhook/screenshot-fix${NC}"
echo ""

# Send request
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${N8N_URL}/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d "$REQUEST_JSON" 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2 || echo "000")
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📋 RESPONSE${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ Status: SUCCESS (HTTP $HTTP_CODE)${NC}"
    echo ""
    
    # Try to parse JSON response
    if command -v jq > /dev/null 2>&1; then
        echo "$BODY" | jq '.'
    else
        echo "$BODY"
    fi
    
    # Save response to file
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    OUTPUT_FILE="screenshot-fix-test-${TIMESTAMP}.json"
    echo "$BODY" > "$OUTPUT_FILE"
    echo ""
    echo -e "${CYAN}💾 Response saved to: ${OUTPUT_FILE}${NC}"
    
elif [ "$HTTP_CODE" = "404" ]; then
    echo -e "${RED}❌ Status: NOT FOUND (HTTP 404)${NC}"
    echo -e "${YELLOW}💡 Workflow may not be imported or webhook path is wrong${NC}"
    echo ""
    echo "Response: $BODY"
    
elif [ "$HTTP_CODE" = "000" ]; then
    echo -e "${RED}❌ Status: NO RESPONSE${NC}"
    echo -e "${YELLOW}💡 Workflow may not be active${NC}"
    echo -e "${YELLOW}💡 Check n8n UI: Toggle workflow to active${NC}"
    echo ""
    echo "Response: $BODY"
    
else
    echo -e "${RED}❌ Status: ERROR (HTTP $HTTP_CODE)${NC}"
    echo ""
    echo "Response: $BODY"
fi

echo ""
echo -e "${CYAN}💡 Next Steps:${NC}"
echo "  - Review error identification"
echo "  - Check if fix was applied"
echo "  - Verify files were modified (if fix applied)"
echo "  - Check n8n execution logs for details"
echo ""


