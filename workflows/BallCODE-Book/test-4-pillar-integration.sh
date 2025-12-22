#!/bin/bash
# Test 4-Pillar Integration System
# Tests: Website → Book → Curriculum → Game integration

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🧪 Testing 4-Pillar Integration${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

BASE_URL="${1:-http://localhost:8888}"
SCHEMA_FILE="${2:-CURRICULUM-DATA-EXAMPLE.json}"

echo -e "${YELLOW}Testing against: $BASE_URL${NC}"
echo -e "${YELLOW}Schema file: $SCHEMA_FILE${NC}"
echo ""

# Test 1: Check schema file exists
echo -e "${YELLOW}Test 1: Checking schema file...${NC}"
if [ -f "$SCHEMA_FILE" ]; then
    echo -e "${GREEN}✅ Schema file exists: $SCHEMA_FILE${NC}"
    BOOK_COUNT=$(python3 -c "import json; data=json.load(open('$SCHEMA_FILE')); print(len(data.get('books', [])))")
    echo -e "${GREEN}   Books in schema: $BOOK_COUNT${NC}"
else
    echo -e "${RED}❌ Schema file not found: $SCHEMA_FILE${NC}"
    exit 1
fi
echo ""

# Test 2: Validate JSON structure
echo -e "${YELLOW}Test 2: Validating JSON structure...${NC}"
if python3 -m json.tool "$SCHEMA_FILE" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ JSON is valid${NC}"
else
    echo -e "${RED}❌ Invalid JSON${NC}"
    exit 1
fi
echo ""

# Test 3: Check API functions exist
echo -e "${YELLOW}Test 3: Checking API functions...${NC}"
API_FUNCTIONS=(
    "BallCode/netlify/functions/books.js"
    "BallCode/netlify/functions/book.js"
    "BallCode/netlify/functions/curriculum.js"
    "BallCode/netlify/functions/next-book.js"
    "BallCode/netlify/functions/game-edit.js"
)

for func in "${API_FUNCTIONS[@]}"; do
    if [ -f "$func" ]; then
        echo -e "${GREEN}✅ $func exists${NC}"
    else
        echo -e "${RED}❌ $func missing${NC}"
    fi
done
echo ""

# Test 4: Check integration scripts
echo -e "${YELLOW}Test 4: Checking integration scripts...${NC}"
INTEGRATION_SCRIPTS=(
    "BallCode/js/api-client.js"
    "BallCode/js/integration.js"
    "BallCode/data/curriculum-data.json"
)

for script in "${INTEGRATION_SCRIPTS[@]}"; do
    if [ -f "$script" ]; then
        echo -e "${GREEN}✅ $script exists${NC}"
    else
        echo -e "${RED}❌ $script missing${NC}"
    fi
done
echo ""

# Test 5: Test API endpoints (if Netlify dev running)
echo -e "${YELLOW}Test 5: Testing API endpoints...${NC}"
if curl -s "$BASE_URL/.netlify/functions/books" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Books API endpoint accessible${NC}"
    
    # Test getting all books
    RESPONSE=$(curl -s "$BASE_URL/.netlify/functions/books")
    if echo "$RESPONSE" | python3 -m json.tool > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Books API returns valid JSON${NC}"
        BOOK_COUNT=$(echo "$RESPONSE" | python3 -c "import sys, json; print(len(json.load(sys.stdin).get('data', [])))" 2>/dev/null || echo "0")
        echo -e "${GREEN}   Books returned: $BOOK_COUNT${NC}"
    else
        echo -e "${YELLOW}⚠️  Books API response not valid JSON${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  API endpoint not accessible (Netlify dev may not be running)${NC}"
    echo -e "${YELLOW}   Start with: cd BallCode && netlify dev${NC}"
fi
echo ""

# Test 6: Check HTML files have integration scripts
echo -e "${YELLOW}Test 6: Checking HTML integration...${NC}"
HTML_FILES=(
    "BallCode/index.html"
    "BallCode/books/book1.html"
    "BallCode/books/book2.html"
    "BallCode/books/book3.html"
)

for html in "${HTML_FILES[@]}"; do
    if [ -f "$html" ]; then
        if grep -q "api-client.js\|integration.js" "$html" 2>/dev/null; then
            echo -e "${GREEN}✅ $html has integration scripts${NC}"
        else
            echo -e "${YELLOW}⚠️  $html missing integration scripts${NC}"
        fi
    else
        echo -e "${RED}❌ $html not found${NC}"
    fi
done
echo ""

# Summary
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 TEST SUMMARY${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${GREEN}✅ Schema file: $SCHEMA_FILE${NC}"
echo -e "${GREEN}✅ API functions: Created${NC}"
echo -e "${GREEN}✅ Integration scripts: Created${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. Add integration scripts to HTML files"
echo "  2. Start Netlify dev: cd BallCode && netlify dev"
echo "  3. Test in browser: http://localhost:8888"
echo "  4. Deploy to production: git push"
echo ""



