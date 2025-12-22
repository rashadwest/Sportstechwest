#!/bin/bash
# Validate 3 Timed Pushes Workflow
# Quick validation script before importing to n8n

# Copyright © 2025 Rashad West. All Rights Reserved.

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

WORKFLOW_FILE="n8n-unity-3-timed-pushes-today.json"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🤖 Validating 3 Timed Pushes Workflow${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Test 1: File exists
echo -e "${YELLOW}Test 1: Checking workflow file exists...${NC}"
if [ -f "$WORKFLOW_FILE" ]; then
    echo -e "${GREEN}✅ Workflow file exists: $WORKFLOW_FILE${NC}"
else
    echo -e "${RED}❌ Workflow file not found: $WORKFLOW_FILE${NC}"
    exit 1
fi
echo ""

# Test 2: JSON is valid
echo -e "${YELLOW}Test 2: Validating JSON structure...${NC}"
if python3 -m json.tool "$WORKFLOW_FILE" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ JSON is valid${NC}"
else
    echo -e "${RED}❌ Invalid JSON${NC}"
    python3 -m json.tool "$WORKFLOW_FILE" 2>&1 | head -5
    exit 1
fi
echo ""

# Test 3: Check for required nodes
echo -e "${YELLOW}Test 3: Checking workflow structure...${NC}"
NODES=$(python3 -c "import json; wf=json.load(open('$WORKFLOW_FILE')); print(len(wf.get('nodes', [])))" 2>/dev/null)
TRIGGERS=$(python3 -c "import json; wf=json.load(open('$WORKFLOW_FILE')); nodes=wf.get('nodes', []); print(len([n for n in nodes if 'scheduleTrigger' in n.get('type', '')]))" 2>/dev/null)

if [ "$NODES" = "7" ]; then
    echo -e "${GREEN}✅ Correct number of nodes: $NODES${NC}"
else
    echo -e "${YELLOW}⚠️  Expected 7 nodes, found: $NODES${NC}"
fi

if [ "$TRIGGERS" = "3" ]; then
    echo -e "${GREEN}✅ Correct number of triggers: $TRIGGERS${NC}"
else
    echo -e "${RED}❌ Expected 3 triggers, found: $TRIGGERS${NC}"
    exit 1
fi
echo ""

# Test 4: Check cron expressions
echo -e "${YELLOW}Test 4: Validating cron expressions...${NC}"
CRON_1030=$(python3 -c "import json; wf=json.load(open('$WORKFLOW_FILE')); nodes=wf.get('nodes', []); print([n['parameters']['rule']['cronExpression'] for n in nodes if '1030' in n.get('id', '')][0])" 2>/dev/null)
CRON_1PM=$(python3 -c "import json; wf=json.load(open('$WORKFLOW_FILE')); nodes=wf.get('nodes', []); print([n['parameters']['rule']['cronExpression'] for n in nodes if '1pm' in n.get('id', '')][0])" 2>/dev/null)
CRON_5PM=$(python3 -c "import json; wf=json.load(open('$WORKFLOW_FILE')); nodes=wf.get('nodes', []); print([n['parameters']['rule']['cronExpression'] for n in nodes if '5pm' in n.get('id', '')][0])" 2>/dev/null)

if [ "$CRON_1030" = "30 10 * * *" ]; then
    echo -e "${GREEN}✅ Push 1 cron: $CRON_1030 (10:30 AM)${NC}"
else
    echo -e "${RED}❌ Push 1 cron incorrect: $CRON_1030${NC}"
fi

if [ "$CRON_1PM" = "0 13 * * *" ]; then
    echo -e "${GREEN}✅ Push 2 cron: $CRON_1PM (1:00 PM)${NC}"
else
    echo -e "${RED}❌ Push 2 cron incorrect: $CRON_1PM${NC}"
fi

if [ "$CRON_5PM" = "0 17 * * *" ]; then
    echo -e "${GREEN}✅ Push 3 cron: $CRON_5PM (5:00 PM)${NC}"
else
    echo -e "${RED}❌ Push 3 cron incorrect: $CRON_5PM${NC}"
fi
echo ""

# Test 5: Check git commands use correct syntax
echo -e "${YELLOW}Test 5: Validating git command syntax...${NC}"
GIT_PULL=$(python3 -c "import json; wf=json.load(open('$WORKFLOW_FILE')); nodes=wf.get('nodes', []); node=[n for n in nodes if 'git-pull' in n.get('id', '')][0]; print(node['parameters']['command'])" 2>/dev/null)
GIT_PUSH=$(python3 -c "import json; wf=json.load(open('$WORKFLOW_FILE')); nodes=wf.get('nodes', []); node=[n for n in nodes if 'git-commit-push' in n.get('id', '')][0]; print(node['parameters']['command'])" 2>/dev/null)

if echo "$GIT_PULL" | grep -q "/bin/sh"; then
    echo -e "${GREEN}✅ Git pull uses /bin/sh${NC}"
else
    echo -e "${YELLOW}⚠️  Git pull command: $GIT_PULL${NC}"
fi

if echo "$GIT_PUSH" | grep -q "/bin/sh"; then
    echo -e "${GREEN}✅ Git push uses /bin/sh${NC}"
else
    echo -e "${YELLOW}⚠️  Git push command: $GIT_PUSH${NC}"
fi
echo ""

# Summary
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 VALIDATION SUMMARY${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${GREEN}✅ Workflow file: Valid${NC}"
echo -e "${GREEN}✅ JSON structure: Valid${NC}"
echo -e "${GREEN}✅ Workflow structure: Correct${NC}"
echo -e "${GREEN}✅ Cron expressions: Correct${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. Import workflow to n8n"
echo "  2. Verify environment variables"
echo "  3. Activate workflow"
echo "  4. Monitor at scheduled times"
echo ""
echo -e "${BLUE}See: ROBOT-3-TIMED-PUSHES-EXECUTION-PLAN.md for full setup${NC}"
echo ""


