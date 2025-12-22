#!/bin/bash
# Import Unity Build Orchestrator via CLI
# This script will help you get an API key and import the workflow

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PI_N8N_URL="http://192.168.1.226:5678"
# Use the file from Desktop/n8n-workflows-to-import (the correct 13-node version)
DESKTOP_FILE="${HOME}/Desktop/n8n-workflows-to-import/n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"
LOCAL_FILE="n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"

# Prefer Desktop file, fallback to local file
if [ -f "$DESKTOP_FILE" ]; then
    WORKFLOW_FILE="$DESKTOP_FILE"
    echo -e "${GREEN}✅ Using workflow from Desktop/n8n-workflows-to-import${NC}"
elif [ -f "$LOCAL_FILE" ]; then
    WORKFLOW_FILE="$LOCAL_FILE"
    echo -e "${YELLOW}⚠️  Using local workflow file (Desktop file not found)${NC}"
else
    echo -e "${RED}❌ Workflow file not found in either location:${NC}"
    echo "   Desktop: $DESKTOP_FILE"
    echo "   Local: $LOCAL_FILE"
    exit 1
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 Import Unity Build Orchestrator via CLI${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Verify workflow file has 13 nodes before proceeding
echo -e "${YELLOW}Verifying workflow file...${NC}"
NODE_COUNT=$(python3 -c "import json, os; path=os.path.expanduser('$WORKFLOW_FILE'); w=json.load(open(path)); nodes=w.get('nodes', []); print(len(nodes))" 2>/dev/null || echo "0")
if [ "$NODE_COUNT" != "13" ]; then
    echo -e "${RED}❌ ERROR: Workflow has $NODE_COUNT nodes, expected 13!${NC}"
    echo "   This is the wrong workflow file."
    exit 1
fi
echo -e "${GREEN}✅ Workflow file verified: $WORKFLOW_FILE (13 nodes)${NC}"
echo ""

# Check for API key (but don't let it override WORKFLOW_FILE)
if [ -f .n8n-env.pi ]; then
    # Save WORKFLOW_FILE before sourcing
    SAVED_WORKFLOW_FILE="$WORKFLOW_FILE"
    source .n8n-env.pi 2>/dev/null
    # Restore WORKFLOW_FILE after sourcing
    WORKFLOW_FILE="$SAVED_WORKFLOW_FILE"
fi

# Try to import if API key exists
if [ -n "$N8N_API_KEY" ] && [ "$N8N_API_KEY" != "" ]; then
    echo -e "${GREEN}✅ API key found - importing via CLI...${NC}"
    echo ""
    
    # Clean workflow for API (remove metadata properties n8n API doesn't accept)
    # Use a unique temp file to avoid conflicts
    CLEANED_FILE="/tmp/n8n-workflow-import-$$-$(date +%s).json"
    echo -e "${YELLOW}Cleaning workflow for API import...${NC}"
    if python3 scripts/clean-workflow-for-api.py "$WORKFLOW_FILE" "$CLEANED_FILE" 2>/dev/null; then
        echo -e "${GREEN}✅ Workflow cleaned${NC}"
        WORKFLOW_FILE_TO_IMPORT="$CLEANED_FILE"
    else
        echo -e "${YELLOW}⚠️  Could not clean workflow, using original${NC}"
        WORKFLOW_FILE_TO_IMPORT="$WORKFLOW_FILE"
        CLEANED_FILE=""  # No cleanup needed
    fi
    echo ""
    
    # Verify the cleaned file has 13 nodes before importing
    NODE_COUNT=$(python3 -c "import json; w=json.load(open('$WORKFLOW_FILE_TO_IMPORT')); nodes=w.get('nodes', []); print(len(nodes))" 2>/dev/null || echo "0")
    echo -e "${YELLOW}Verifying workflow has 13 nodes...${NC}"
    if [ "$NODE_COUNT" != "13" ]; then
        echo -e "${RED}❌ ERROR: Workflow has $NODE_COUNT nodes, expected 13!${NC}"
        echo "   This is the wrong workflow file. Please check the file."
        [ -n "$CLEANED_FILE" ] && [ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
        exit 1
    fi
    echo -e "${GREEN}✅ Verified: Workflow has 13 nodes${NC}"
    echo ""
    
    RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
      -H "X-N8N-API-KEY: $N8N_API_KEY" \
      -H "Content-Type: application/json" \
      -d @"$WORKFLOW_FILE_TO_IMPORT")
    
    HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
    BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')
    
    if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
        echo -e "${GREEN}✅ SUCCESS! Workflow imported via CLI${NC}"
        echo ""
        
        # Verify the imported workflow has 13 nodes
        IMPORTED_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
        if [ -n "$IMPORTED_ID" ]; then
            echo -e "${YELLOW}Verifying imported workflow...${NC}"
            VERIFY_RESPONSE=$(curl -s -X GET "${PI_N8N_URL}/api/v1/workflows/$IMPORTED_ID" \
              -H "X-N8N-API-KEY: $N8N_API_KEY" \
              -H "Content-Type: application/json" 2>/dev/null)
            IMPORTED_NODES=$(echo "$VERIFY_RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('nodes', [])))" 2>/dev/null || echo "?")
            if [ "$IMPORTED_NODES" = "13" ]; then
                echo -e "${GREEN}✅ Verified: Imported workflow has 13 nodes${NC}"
            else
                echo -e "${RED}⚠️  WARNING: Imported workflow has $IMPORTED_NODES nodes (expected 13)${NC}"
                echo "   You may need to delete this workflow and try again."
            fi
            echo ""
        fi
        
        echo "Response:"
        echo "$BODY" | python3 -m json.tool 2>/dev/null | head -30 || echo "$BODY" | head -15
        echo ""
        echo -e "${YELLOW}📝 Next steps:${NC}"
        echo "1. Open n8n: $PI_N8N_URL"
        echo "2. Find the imported workflow (should have 13 nodes)"
        echo "3. If you see a 23-node workflow, DELETE it first"
        echo "4. Activate the 13-node workflow (toggle switch)"
        echo "5. Configure credentials if needed"
        
        # Clean up temp file
        [ -n "$CLEANED_FILE" ] && [ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
        exit 0
    else
        echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
        echo ""
        echo "Response:"
        echo "$BODY" | head -10
        echo ""
        echo -e "${YELLOW}💡 Troubleshooting:${NC}"
        echo "- Check if API key is valid"
        echo "- Verify n8n is running: curl $PI_N8N_URL/healthz"
        echo "- Try cleaning workflow: python3 scripts/clean-workflow-for-api.py $WORKFLOW_FILE"
        
        # Clean up temp file
        [ -n "$CLEANED_FILE" ] && [ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠️  No API key found${NC}"
    echo ""
    echo -e "${BLUE}📋 To import via CLI, you need an API key:${NC}"
    echo ""
    echo "Step 1: Get API Key"
    echo "  1. Open Pi n8n: $PI_N8N_URL"
    echo "  2. Click 'Settings' (gear icon)"
    echo "  3. Click 'API' in left sidebar"
    echo "  4. Click 'Create API Key'"
    echo "  5. Copy the API key"
    echo ""
    echo "Step 2: Add API Key to .n8n-env.pi"
    echo "  Run this command (replace YOUR_KEY with your actual key):"
    echo ""
    echo -e "${GREEN}  echo \"export N8N_API_KEY='YOUR_KEY'\" >> .n8n-env.pi${NC}"
    echo ""
    echo "Step 3: Run this script again"
    echo -e "${GREEN}  ./scripts/import-orchestrator-cli.sh${NC}"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}💡 Alternative: Import via UI${NC}"
    echo ""
    echo "If you prefer UI import:"
    echo "1. Open Pi n8n: $PI_N8N_URL"
    echo "2. Workflows → Import from File"
    echo "3. Select: $WORKFLOW_FILE"
    echo "4. Click Import"
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    exit 1
fi

