#!/bin/bash
# Full System Audit
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

echo "🔍 BallCODE System Audit"
echo "========================"
echo "Date: $(date)"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PASSED=0
FAILED=0
WARNINGS=0

check() {
    local name=$1
    local command=$2
    
    echo -n "Checking $name... "
    if eval "$command" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ PASS${NC}"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}❌ FAIL${NC}"
        ((FAILED++))
        return 1
    fi
}

warn() {
    local name=$1
    local message=$2
    echo -e "${YELLOW}⚠️  $name: $message${NC}"
    ((WARNINGS++))
}

echo "1️⃣ Repository Status"
echo "-------------------"
if [ -d .git ]; then
    check "Git repository exists" "test -d .git"
    check "On main branch" "[ \$(git branch --show-current) = 'main' ]"
    check "No uncommitted changes" "git diff --quiet HEAD"
else
    warn "Git repository" "Not in git repository (may be in parent directory)"
fi

echo ""
echo "2️⃣ Level Files"
echo "-------------"
check "Book 1 level exists" "test -f Unity-Scripts/Levels/book1_foundation_block.json"
check "Book 2 level exists" "test -f Unity-Scripts/Levels/book2_decision_crossover.json"
check "Book 3 level exists" "test -f Unity-Scripts/Levels/book3_pattern_loop.json"

# Validate JSON
for file in Unity-Scripts/Levels/book*.json; do
    if [ -f "$file" ]; then
        if python3 -m json.tool "$file" > /dev/null 2>&1; then
            echo -e "   ${GREEN}✅ $(basename $file) - Valid JSON${NC}"
        else
            echo -e "   ${RED}❌ $(basename $file) - Invalid JSON${NC}"
            ((FAILED++))
        fi
    fi
done

echo ""
echo "3️⃣ Website Files"
echo "---------------"
check "Homepage exists" "test -f BallCode/index.html"
check "CSS file exists" "test -f BallCode/css/style.css"
check "Assets directory exists" "test -d BallCode/assets"

echo ""
echo "4️⃣ Documentation"
echo "---------------"
check "Level push documentation exists" "test -f documents/LEVEL-PUSH-SYSTEM-AUTOMATION.md"
check "Daily workflow exists" "test -f documents/DAILY-WORKFLOW-2025-12-22.md"

echo ""
echo "5️⃣ Scripts"
echo "---------"
check "Test script exists" "test -f scripts/test-all-4-workflows.sh"
check "Debugger script exists" "test -f scripts/n8n-workflow-debugger.py"
check "Scripts are executable" "[ -x scripts/test-all-4-workflows.sh ]"

echo ""
echo "6️⃣ n8n Workflows"
echo "---------------"
N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"
if curl -s -f "${N8N_URL}/healthz" > /dev/null 2>&1; then
    echo -e "   ${GREEN}✅ n8n is accessible${NC}"
    ((PASSED++))
else
    echo -e "   ${YELLOW}⚠️  n8n not accessible (may be offline)${NC}"
    ((WARNINGS++))
fi

echo ""
echo "7️⃣ Git Status"
echo "------------"
if [ -n "$(git status --porcelain)" ]; then
    warn "Uncommitted changes" "Some files are not committed"
    git status --short | head -5
else
    echo -e "   ${GREEN}✅ Working directory clean${NC}"
    ((PASSED++))
fi

echo ""
echo "========================"
echo "📊 Audit Summary"
echo "========================"
echo -e "${GREEN}✅ Passed: $PASSED${NC}"
echo -e "${RED}❌ Failed: $FAILED${NC}"
echo -e "${YELLOW}⚠️  Warnings: $WARNINGS${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ System audit passed!${NC}"
    exit 0
else
    echo -e "${RED}❌ System audit found issues${NC}"
    exit 1
fi

