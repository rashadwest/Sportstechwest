#!/bin/bash
# Test All 4 Active n8n Workflows
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"
USE_TEST="${USE_TEST:-true}"

if [ "$USE_TEST" = "true" ]; then
    WEBHOOK_PREFIX="/webhook-test"
else
    WEBHOOK_PREFIX="/webhook"
fi

echo "🧪 Testing All 4 Active n8n Workflows"
echo "======================================"
echo "n8n URL: $N8N_URL"
echo "Using: $WEBHOOK_PREFIX"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test results
PASSED=0
FAILED=0

test_webhook() {
    local name=$1
    local path=$2
    local payload=$3
    
    echo -n "Testing $name... "
    
    response=$(curl -s -w "\n%{http_code}" -X POST "${N8N_URL}${WEBHOOK_PREFIX}${path}" \
        -H "Content-Type: application/json" \
        -d "$payload" 2>&1)
    
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | sed '$d')
    
    if [ "$http_code" = "200" ] || [ "$http_code" = "201" ]; then
        echo -e "${GREEN}✅ PASS${NC} (HTTP $http_code)"
        echo "$body" | head -c 100
        echo "..."
        ((PASSED++))
        return 0
    elif [ "$http_code" = "404" ]; then
        echo -e "${YELLOW}⚠️  NOT FOUND${NC} (HTTP $http_code) - Workflow may not be active or webhook path incorrect"
        echo "$body"
        ((FAILED++))
        return 1
    else
        echo -e "${RED}❌ FAIL${NC} (HTTP $http_code)"
        echo "$body" | head -c 200
        echo ""
        ((FAILED++))
        return 1
    fi
}

echo "1️⃣ Unity Build Orchestrator"
test_webhook "Unity Build Orchestrator" "/unity-build" '{"request":"Test build","branch":"main"}'

echo ""
echo "2️⃣ Full Integration Workflow"
test_webhook "Full Integration" "/ballcode-dev" '{"prompt":"Test integration","mode":"quick"}'

echo ""
echo "3️⃣ Screenshot Fix Workflow"
test_webhook "Screenshot Fix" "/screenshot-fix" '{"screenshotUrl":"test","context":"Test error"}'

echo ""
echo "4️⃣ Book Content Update Workflow"
test_webhook "Book Content Update" "/book-content-update" '{"bookId":"book1","action":"test"}'

echo ""
echo "======================================"
echo "Results: ${GREEN}$PASSED passed${NC}, ${RED}$FAILED failed${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ All workflows tested successfully!${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️  Some workflows need attention${NC}"
    echo ""
    echo "Troubleshooting:"
    echo "1. Check if workflows are ACTIVE in n8n UI"
    echo "2. Verify webhook paths are correct"
    echo "3. Check n8n execution logs for errors"
    echo "4. Ensure n8n is running: curl -s $N8N_URL/healthz"
    exit 1
fi


