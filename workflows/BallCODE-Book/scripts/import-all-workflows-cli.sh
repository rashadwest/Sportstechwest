#!/bin/bash
# Import All n8n Workflows via CLI with Permanent Fix Applied
# Applies the "Could not find property option" fix to all workflows automatically

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

PI_N8N_URL="http://192.168.1.226:5678"
WORKFLOWS_DIR="${HOME}/Desktop/n8n-workflows-to-import"
# Also check local directory for Phase 2 workflows
LOCAL_WORKFLOWS_DIR="."

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 Import All n8n Workflows via CLI (With Permanent Fix)${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if workflows directory exists
if [ ! -d "$WORKFLOWS_DIR" ]; then
    echo -e "${RED}❌ Workflows directory not found: $WORKFLOWS_DIR${NC}"
    exit 1
fi

# Check for API key
if [ -f .n8n-env.pi ]; then
    # Save WORKFLOW_FILE before sourcing (prevent override)
    SAVED_WORKFLOW_FILE="${WORKFLOW_FILE:-}"
    source .n8n-env.pi 2>/dev/null
    WORKFLOW_FILE="${SAVED_WORKFLOW_FILE}"
fi

if [ -z "$N8N_API_KEY" ] || [ "$N8N_API_KEY" = "" ]; then
    echo -e "${RED}❌ API key not found${NC}"
    echo ""
    echo "Run: ./scripts/setup-pi-api-key.sh"
    exit 1
fi

echo -e "${GREEN}✅ API key found${NC}"
echo ""

# Find all workflow JSON files (Desktop folder + local Phase 2 workflows)
WORKFLOW_FILES=($(find "$WORKFLOWS_DIR" -name "*.json" -type f 2>/dev/null | grep -v ".DS_Store" | sort))
# Add Phase 2 workflows from local directory if they exist
PHASE2_WORKFLOWS=(
    "n8n-book-content-update-workflow.json"
    "n8n-curriculum-sync-workflow.json"
    "n8n-game-exercise-integration-workflow.json"
)
for wf in "${PHASE2_WORKFLOWS[@]}"; do
    if [ -f "$LOCAL_WORKFLOWS_DIR/$wf" ]; then
        # Use absolute path
        WORKFLOW_FILES+=("$(pwd)/$wf")
    fi
done

if [ ${#WORKFLOW_FILES[@]} -eq 0 ]; then
    echo -e "${RED}❌ No workflow files found in $WORKFLOWS_DIR${NC}"
    exit 1
fi

echo -e "${CYAN}Found ${#WORKFLOW_FILES[@]} workflow file(s):${NC}"
for file in "${WORKFLOW_FILES[@]}"; do
    echo "  - $(basename "$file")"
done
echo ""

# Import each workflow
SUCCESS_COUNT=0
FAILED_COUNT=0
FAILED_FILES=()

for workflow_file in "${WORKFLOW_FILES[@]}"; do
    filename=$(basename "$workflow_file")
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}Processing: $filename${NC}"
    echo ""
    
    # Verify workflow file has nodes
    NODE_COUNT=$(python3 -c "import json, os; path=os.path.expanduser('$workflow_file'); w=json.load(open(path)); nodes=w.get('nodes', []); print(len(nodes))" 2>/dev/null || echo "0")
    
    if [ "$NODE_COUNT" = "0" ]; then
        echo -e "${RED}❌ Invalid workflow file (no nodes found)${NC}"
        FAILED_COUNT=$((FAILED_COUNT + 1))
        FAILED_FILES+=("$filename (invalid)")
        echo ""
        continue
    fi
    
    echo -e "${GREEN}✅ Workflow has $NODE_COUNT nodes${NC}"
    
    # Clean workflow (apply permanent fix)
    CLEANED_FILE="/tmp/n8n-workflow-import-$$-$(basename "$workflow_file" .json)-$(date +%s).json"
    echo -e "${YELLOW}Applying permanent fix (removing problematic options)...${NC}"
    
    if python3 scripts/clean-workflow-for-api.py "$workflow_file" "$CLEANED_FILE" 2>&1 | grep -q "Fixed"; then
        echo -e "${GREEN}✅ Fixes applied${NC}"
    else
        echo -e "${GREEN}✅ Workflow cleaned${NC}"
    fi
    
    # Verify cleaned file
    CLEANED_NODES=$(python3 -c "import json; w=json.load(open('$CLEANED_FILE')); print(len(w.get('nodes', [])))" 2>/dev/null || echo "0")
    
    if [ "$CLEANED_NODES" != "$NODE_COUNT" ]; then
        echo -e "${RED}❌ Node count mismatch after cleaning ($CLEANED_NODES vs $NODE_COUNT)${NC}"
        FAILED_COUNT=$((FAILED_COUNT + 1))
        FAILED_FILES+=("$filename (node count mismatch)")
        [ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
        echo ""
        continue
    fi
    
    # Import via API
    echo -e "${YELLOW}Importing via CLI...${NC}"
    RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
      -H "X-N8N-API-KEY: $N8N_API_KEY" \
      -H "Content-Type: application/json" \
      -d @"$CLEANED_FILE" 2>&1)
    
    HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2 || echo "000")
    BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')
    
    if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
        WORKFLOW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
        WORKFLOW_NAME=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('name', ''))" 2>/dev/null || echo "")
        
        echo -e "${GREEN}✅ SUCCESS! Workflow imported${NC}"
        echo "   ID: $WORKFLOW_ID"
        echo "   Name: $WORKFLOW_NAME"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    else
        echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
        echo "   Response: $(echo "$BODY" | head -3 | tr '\n' ' ')"
        FAILED_COUNT=$((FAILED_COUNT + 1))
        FAILED_FILES+=("$filename (HTTP $HTTP_CODE)")
    fi
    
    # Clean up temp file
    [ -f "$CLEANED_FILE" ] && rm -f "$CLEANED_FILE"
    echo ""
done

# Summary
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}📊 Import Summary${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${GREEN}✅ Successful: $SUCCESS_COUNT${NC}"
echo -e "${RED}❌ Failed: $FAILED_COUNT${NC}"
echo ""

if [ ${#FAILED_FILES[@]} -gt 0 ]; then
    echo -e "${YELLOW}Failed workflows:${NC}"
    for failed in "${FAILED_FILES[@]}"; do
        echo "  - $failed"
    done
    echo ""
fi

if [ $SUCCESS_COUNT -gt 0 ]; then
    echo -e "${GREEN}✅ Next steps:${NC}"
    echo "1. Open n8n: $PI_N8N_URL"
    echo "2. Find imported workflows"
    echo "3. Activate each workflow (toggle switch)"
    echo "4. Configure credentials if needed"
    echo ""
fi

if [ $FAILED_COUNT -eq 0 ]; then
    echo -e "${GREEN}🎉 All workflows imported successfully!${NC}"
    exit 0
else
    exit 1
fi


