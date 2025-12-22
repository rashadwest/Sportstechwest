#!/bin/bash
# Quick Import: Unity Build Orchestrator
# Usage: ./IMPORT-ORCHESTRATOR-NOW.sh [API_KEY]

# Copyright © 2025 Rashad West. All Rights Reserved.

cd "$(dirname "$0")" || exit 1

PI_N8N_URL="http://192.168.1.226:5678"
WORKFLOW_FILE="n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json"

# Try to get API key from environment or argument
if [ -n "$1" ]; then
    API_KEY="$1"
elif [ -f .n8n-env.pi ]; then
    source .n8n-env.pi 2>/dev/null
    API_KEY="$N8N_API_KEY"
else
    API_KEY=""
fi

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📥 Import Unity Build Orchestrator${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ ! -f "$WORKFLOW_FILE" ]; then
    echo -e "${RED}❌ Workflow file not found: $WORKFLOW_FILE${NC}"
    exit 1
fi

if [ -z "$API_KEY" ]; then
    echo -e "${YELLOW}⚠️  No API key found${NC}"
    echo ""
    echo -e "${BLUE}Option 1: Get API Key and Run Again${NC}"
    echo "1. Open: $PI_N8N_URL"
    echo "2. Settings → API → Create API Key"
    echo "3. Copy the key"
    echo "4. Run: ./IMPORT-ORCHESTRATOR-NOW.sh YOUR_API_KEY"
    echo ""
    echo -e "${BLUE}Option 2: Import via UI (No API Key Needed)${NC}"
    echo "1. Open: $PI_N8N_URL"
    echo "2. Click 'Workflows' → 'Import from File'"
    echo "3. Select: $WORKFLOW_FILE"
    echo "4. Click 'Import'"
    echo "5. Activate the workflow (toggle ON)"
    echo ""
    exit 1
fi

echo -e "${YELLOW}📄 File: $WORKFLOW_FILE${NC}"
echo -e "${YELLOW}🌐 n8n: $PI_N8N_URL${NC}"
echo ""

# Clean workflow JSON (remove metadata n8n API doesn't accept)
CLEANED_FILE="/tmp/n8n-orchestrator-import-$$.json"
python3 << 'PYTHON_SCRIPT' > "$CLEANED_FILE"
import json
import sys

try:
    with open('n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json', 'r') as f:
        workflow = json.load(f)
    
    # Remove metadata properties n8n API doesn't accept
    cleaned = {
        "name": workflow.get("name", "Unity Build Orchestrator"),
        "nodes": workflow.get("nodes", []),
        "connections": workflow.get("connections", {}),
        "settings": workflow.get("settings", {}),
        "staticData": workflow.get("staticData"),
        "tags": workflow.get("tags", [])
    }
    
    print(json.dumps(cleaned))
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
PYTHON_SCRIPT

if [ $? -ne 0 ] || [ ! -s "$CLEANED_FILE" ]; then
    echo -e "${RED}❌ Failed to clean workflow JSON${NC}"
    rm -f "$CLEANED_FILE"
    exit 1
fi

echo -e "${BLUE}📤 Importing workflow...${NC}"

RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$CLEANED_FILE")

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

rm -f "$CLEANED_FILE"

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ SUCCESS! Workflow imported${NC}"
    echo ""
    
    WORKFLOW_ID=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null || echo "")
    
    if [ -n "$WORKFLOW_ID" ]; then
        echo -e "${BLUE}Workflow ID: $WORKFLOW_ID${NC}"
        echo ""
        
        # Try to activate it
        echo -e "${YELLOW}🔄 Attempting to activate workflow...${NC}"
        ACTIVATE_RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X POST "${PI_N8N_URL}/api/v1/workflows/$WORKFLOW_ID/activate" \
          -H "X-N8N-API-KEY: $API_KEY" \
          -H "Content-Type: application/json" \
          -d '{"active": true}' 2>/dev/null)
        
        ACTIVATE_CODE=$(echo "$ACTIVATE_RESPONSE" | grep "HTTP_CODE" | cut -d: -f2)
        if [ "$ACTIVATE_CODE" = "200" ]; then
            echo -e "${GREEN}✅ Workflow activated!${NC}"
        else
            echo -e "${YELLOW}⚠️  Could not activate via API (HTTP $ACTIVATE_CODE)${NC}"
            echo -e "${YELLOW}   Activate manually in n8n UI${NC}"
        fi
    fi
    
    echo ""
    echo -e "${BLUE}📝 Next Steps:${NC}"
    echo "1. Open: $PI_N8N_URL"
    echo "2. Find: 'AIMCODE (Demis) - Unity Build Orchestrator'"
    echo "3. Verify it's active (toggle should be ON)"
    echo "4. Configure credentials (GitHub Actions Token, Netlify API Token)"
    echo "5. Test: curl -X POST $PI_N8N_URL/webhook/unity-build -H 'Content-Type: application/json' -d '{\"request\":\"Test\",\"branch\":\"main\"}'"
    echo ""
else
    echo -e "${RED}❌ Import failed (HTTP $HTTP_CODE)${NC}"
    echo ""
    echo "Response:"
    echo "$BODY" | head -10
    echo ""
    echo -e "${YELLOW}💡 Troubleshooting:${NC}"
    echo "- Check API key is valid"
    echo "- Check n8n is running: curl $PI_N8N_URL/healthz"
    echo "- Try importing via UI instead"
    exit 1
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
