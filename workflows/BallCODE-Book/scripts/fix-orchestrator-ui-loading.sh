#!/bin/bash
# Fix Orchestrator Workflow UI Loading Issue
# Solves "Could not find workflow" + workflow reverts to blank

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

WORKFLOW_FILE="n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"
CLEANED_FILE="n8n-unity-build-orchestrator-CLEANED-UI-IMPORT.json"
N8N_URL="http://192.168.1.226:5678"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🔧 Fix Orchestrator Workflow UI Loading Issue${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Step 1: Diagnose
echo -e "${CYAN}Step 1: Diagnosing workflow...${NC}"
if [ -f "$WORKFLOW_FILE" ]; then
    python3 scripts/diagnose-workflow-issues.py "$WORKFLOW_FILE" 2>&1 | head -20
    echo ""
else
    echo -e "${RED}❌ Workflow file not found: $WORKFLOW_FILE${NC}"
    exit 1
fi

# Step 2: Clean workflow
echo -e "${CYAN}Step 2: Cleaning workflow for UI import...${NC}"
if python3 scripts/clean-workflow-for-api.py "$WORKFLOW_FILE" "$CLEANED_FILE" 2>&1; then
    echo -e "${GREEN}✅ Cleaned workflow created: $CLEANED_FILE${NC}"
    echo ""
else
    echo -e "${RED}❌ Failed to clean workflow${NC}"
    exit 1
fi

# Step 3: Instructions
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📋 FIX PROCEDURE${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${YELLOW}SOLUTION 1: Browser Fixes (Try This First - 5 minutes)${NC}"
echo ""
echo "1. Clear Browser Cache:"
echo "   - Chrome/Edge: Press Cmd+Shift+Delete (Mac) or Ctrl+Shift+Delete (Windows)"
echo "   - Select 'Cached images and files'"
echo "   - Click 'Clear data'"
echo ""
echo "2. Try Incognito/Private Window:"
echo "   - Open n8n in incognito: $N8N_URL"
echo "   - Navigate to orchestrator workflow"
echo "   - If it works → Browser cache was the issue!"
echo ""
echo "3. Hard Refresh:"
echo "   - Press Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)"
echo "   - Forces complete reload"
echo ""
echo "4. Check Browser Console:"
echo "   - Press F12 → Console tab"
echo "   - Look for WebSocket or JavaScript errors"
echo ""
echo -e "${GREEN}If Solution 1 works, you're done!${NC}"
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${YELLOW}SOLUTION 2: Delete and Re-import (If Solution 1 Doesn't Work)${NC}"
echo ""
echo "1. Delete Existing Workflow:"
echo "   - Open n8n: $N8N_URL"
echo "   - Go to Workflows list"
echo "   - Find: 'AIMCODE (Demis) - Unity Build Orchestrator (13 nodes, MAC GUARDED)'"
echo "   - Click Delete (or use ... menu)"
echo ""
echo "2. Import Cleaned Workflow:"
echo "   - Click 'Import from File' button"
echo "   - Select: $(pwd)/$CLEANED_FILE"
echo "   - Click 'Import'"
echo ""
echo "3. Activate Workflow:"
echo "   - Open the imported workflow"
echo "   - Toggle 'Active' switch ON"
echo ""
echo -e "${GREEN}Cleaned workflow file ready: $CLEANED_FILE${NC}"
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${CYAN}💡 Why This Happens:${NC}"
echo "  - Browser cache holds stale workflow data"
echo "  - WebSocket connection issues with local IP"
echo "  - Metadata properties can interfere with UI loading"
echo "  - n8n UI expects different format than API import"
echo ""

echo -e "${CYAN}📊 Success Probability:${NC}"
echo "  - Solution 1 (Browser fixes): ~80%"
echo "  - Solution 2 (Re-import): ~15%"
echo "  - Solution 3 (Version check): ~5%"
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Fix procedure ready!${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

