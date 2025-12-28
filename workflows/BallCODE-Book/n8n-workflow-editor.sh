#!/bin/bash
# n8n Workflow Editor - Cursor Integration
# Complete workflow management system for editing n8n workflows in Cursor

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

WORKFLOW_FILE="${1:-n8n-unity-automation-workflow.json}"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 n8n Workflow Editor - Cursor Integration${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if workflow file exists
if [ ! -f "$WORKFLOW_FILE" ]; then
    echo -e "${RED}❌ Error: Workflow file not found: $WORKFLOW_FILE${NC}"
    exit 1
fi

# Menu
echo "Select an action:"
echo ""
echo "  1) Debug workflow (check for issues)"
echo "  2) Fix workflow (auto-fix common issues)"
echo "  3) Validate JSON"
echo "  4) Deploy to n8n (create/update)"
echo "  5) Export from n8n (download current)"
echo "  6) Compare workflows (diff)"
echo "  7) Show workflow info"
echo "  8) Full workflow check (debug + fix + validate)"
echo ""
read -p "Enter choice [1-8]: " choice

case $choice in
    1)
        echo -e "${YELLOW}🔍 Debugging workflow...${NC}"
        python3 debug-workflow.py "$WORKFLOW_FILE"
        ;;
    2)
        echo -e "${YELLOW}🔧 Fixing workflow...${NC}"
        python3 fix-workflow-file.py "$WORKFLOW_FILE" "${WORKFLOW_FILE}.fixed"
        echo ""
        read -p "Apply fixes to original file? (y/n) " apply
        if [[ $apply =~ ^[Yy]$ ]]; then
            mv "${WORKFLOW_FILE}.fixed" "$WORKFLOW_FILE"
            echo -e "${GREEN}✅ Fixes applied!${NC}"
        fi
        ;;
    3)
        echo -e "${YELLOW}📋 Validating JSON...${NC}"
        if python3 -m json.tool "$WORKFLOW_FILE" > /dev/null; then
            echo -e "${GREEN}✅ JSON is valid!${NC}"
        else
            echo -e "${RED}❌ Invalid JSON!${NC}"
            exit 1
        fi
        ;;
    4)
        echo -e "${YELLOW}🚀 Deploying workflow...${NC}"
        read -p "Workflow ID (leave empty for new workflow): " workflow_id
        if [ -z "$workflow_id" ]; then
            ./deploy-n8n-workflow.sh "$WORKFLOW_FILE"
        else
            ./deploy-n8n-workflow.sh "$WORKFLOW_FILE" "$workflow_id"
        fi
        ;;
    5)
        echo -e "${YELLOW}📥 Exporting workflow from n8n...${NC}"
        read -p "Workflow ID: " workflow_id
        if [ -z "$workflow_id" ]; then
            echo -e "${RED}❌ Workflow ID required${NC}"
            exit 1
        fi
        
        source .n8n-env 2>/dev/null || true
        N8N_URL="${N8N_URL:-http://localhost:5678}"
        
        curl -s -X GET "$N8N_URL/api/v1/workflows/$workflow_id" \
            ${N8N_API_KEY:+-H "X-N8N-API-KEY: $N8N_API_KEY"} \
            | python3 -m json.tool > "${WORKFLOW_FILE}.exported"
        
        echo -e "${GREEN}✅ Workflow exported to: ${WORKFLOW_FILE}.exported${NC}"
        ;;
    6)
        echo -e "${YELLOW}🔍 Comparing workflows...${NC}"
        read -p "Second workflow file: " file2
        if [ ! -f "$file2" ]; then
            echo -e "${RED}❌ File not found: $file2${NC}"
            exit 1
        fi
        diff -u "$WORKFLOW_FILE" "$file2" || true
        ;;
    7)
        echo -e "${YELLOW}📊 Workflow Information:${NC}"
        echo ""
        python3 -c "
import json
import sys
with open('$WORKFLOW_FILE') as f:
    wf = json.load(f)
print(f\"Name: {wf.get('name', 'N/A')}\")
print(f\"Nodes: {len(wf.get('nodes', []))}\")
print(f\"Connections: {len(wf.get('connections', {}))}\")
print()
print('Node List:')
for i, node in enumerate(wf.get('nodes', []), 1):
    print(f\"  {i}. {node.get('name', 'Unknown')} ({node.get('type', 'N/A')})\")
"
        ;;
    8)
        echo -e "${YELLOW}🔍 Running full workflow check...${NC}"
        echo ""
        echo "Step 1: Validating JSON..."
        python3 -m json.tool "$WORKFLOW_FILE" > /dev/null && echo -e "${GREEN}✅ JSON valid${NC}" || { echo -e "${RED}❌ JSON invalid${NC}"; exit 1; }
        echo ""
        echo "Step 2: Debugging workflow..."
        python3 debug-workflow.py "$WORKFLOW_FILE"
        echo ""
        echo "Step 3: Fixing issues..."
        python3 fix-workflow-file.py "$WORKFLOW_FILE" "${WORKFLOW_FILE}.fixed"
        if [ -f "${WORKFLOW_FILE}.fixed" ]; then
            echo ""
            read -p "Apply fixes? (y/n) " apply
            if [[ $apply =~ ^[Yy]$ ]]; then
                mv "${WORKFLOW_FILE}.fixed" "$WORKFLOW_FILE"
                echo -e "${GREEN}✅ All checks complete and fixes applied!${NC}"
            fi
        fi
        ;;
    *)
        echo -e "${RED}❌ Invalid choice${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Complete!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"




