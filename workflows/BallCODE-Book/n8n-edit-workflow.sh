#!/bin/bash
# n8n Terminal Workflow Editor
# Export → Edit → Import workflow using n8n CLI

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

WORKFLOW_ID="$1"
EDITOR="${EDITOR:-${VISUAL:-nano}}"
TEMP_DIR="/tmp/n8n-edit-$$"
WORKFLOW_FILE=""

# Check if workflow ID provided
if [ -z "$WORKFLOW_ID" ]; then
    echo -e "${RED}❌ Error: Workflow ID required${NC}"
    echo ""
    echo "Usage: $0 <workflow-id> [editor]"
    echo ""
    echo "Examples:"
    echo "  $0 abc123              # Edit with default editor (nano)"
    echo "  $0 abc123 vim          # Edit with vim"
    echo "  $0 abc123 code         # Edit with VS Code"
    echo ""
    echo "To get workflow IDs, run:"
    echo "  n8n export:workflow --all --output=/tmp/all-workflows/"
    exit 1
fi

# Use custom editor if provided
if [ -n "$2" ]; then
    EDITOR="$2"
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📝 n8n Terminal Workflow Editor${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Workflow ID: ${YELLOW}$WORKFLOW_ID${NC}"
echo "Editor: ${YELLOW}$EDITOR${NC}"
echo ""

# Create temp directory
mkdir -p "$TEMP_DIR"
trap "rm -rf $TEMP_DIR" EXIT

# Export workflow
echo -e "${YELLOW}📥 Exporting workflow...${NC}"
if n8n export:workflow --id="$WORKFLOW_ID" --output="$TEMP_DIR/workflow.json" --pretty 2>/dev/null; then
    WORKFLOW_FILE="$TEMP_DIR/workflow.json"
    echo -e "${GREEN}✅ Workflow exported${NC}"
else
    echo -e "${RED}❌ Failed to export workflow${NC}"
    echo "   Make sure n8n is running and the workflow ID is correct"
    exit 1
fi

# Show workflow info
echo ""
echo -e "${YELLOW}📊 Workflow Information:${NC}"
python3 -c "
import json
with open('$WORKFLOW_FILE') as f:
    wf = json.load(f)
print(f\"  Name: {wf.get('name', 'N/A')}\")
print(f\"  Nodes: {len(wf.get('nodes', []))}\")
print(f\"  Active: {wf.get('active', False)}\")
" 2>/dev/null || echo "  (Could not parse workflow info)"

# Backup original
BACKUP_FILE="workflow-${WORKFLOW_ID}-backup-$(date +%Y%m%d-%H%M%S).json"
cp "$WORKFLOW_FILE" "$BACKUP_FILE"
echo ""
echo -e "${GREEN}💾 Backup saved: $BACKUP_FILE${NC}"

# Edit workflow
echo ""
echo -e "${YELLOW}✏️  Opening in editor ($EDITOR)...${NC}"
echo "   Make your changes and save the file"
echo ""

if $EDITOR "$WORKFLOW_FILE"; then
    echo ""
    echo -e "${YELLOW}🔍 Validating JSON...${NC}"
    
    # Validate JSON
    if python3 -m json.tool "$WORKFLOW_FILE" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ JSON is valid${NC}"
    else
        echo -e "${RED}❌ Invalid JSON!${NC}"
        echo "   Please fix JSON errors before importing"
        read -p "   Open editor again? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            $EDITOR "$WORKFLOW_FILE"
        else
            exit 1
        fi
    fi
    
    # Ask to import
    echo ""
    read -p "Import workflow back to n8n? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo ""
        echo -e "${YELLOW}📤 Importing workflow...${NC}"
        if n8n import:workflow --input="$WORKFLOW_FILE" 2>/dev/null; then
            echo -e "${GREEN}✅ Workflow imported successfully!${NC}"
        else
            echo -e "${RED}❌ Failed to import workflow${NC}"
            echo "   Check n8n logs for details"
            exit 1
        fi
    else
        echo ""
        echo -e "${YELLOW}⚠️  Workflow not imported${NC}"
        echo "   Edited file saved at: $WORKFLOW_FILE"
        echo "   You can import it later with:"
        echo "   ${YELLOW}n8n import:workflow --input=$WORKFLOW_FILE${NC}"
    fi
else
    echo ""
    echo -e "${RED}❌ Editor exited with error${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Complete!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"




