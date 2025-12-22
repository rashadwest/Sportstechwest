#!/bin/bash
# Setup n8n API Key for Pi - Interactive Guide
# This script helps you get and configure the API key for CLI access

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

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🔑 n8n API Key Setup for Pi CLI Access${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Step 1: Check if n8n is accessible
echo -e "${YELLOW}Step 1: Checking Pi n8n connection...${NC}"
if curl -s -f "${PI_N8N_URL}/healthz" > /dev/null 2>&1 || curl -s -f "${PI_N8N_URL}" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Pi n8n is accessible at ${PI_N8N_URL}${NC}"
else
    echo -e "${RED}❌ Cannot connect to Pi n8n at ${PI_N8N_URL}${NC}"
    echo ""
    echo "Please check:"
    echo "  1. Pi is powered on and connected to network"
    echo "  2. n8n is running on the Pi"
    echo "  3. IP address is correct: 192.168.1.226"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi
echo ""

# Step 2: Instructions to get API key
echo -e "${YELLOW}Step 2: Get API Key from n8n UI${NC}"
echo ""
echo -e "${CYAN}Follow these steps:${NC}"
echo ""
echo "1. Open Pi n8n in your browser:"
echo -e "   ${GREEN}${PI_N8N_URL}${NC}"
echo ""
echo "2. Click 'Settings' (gear icon, usually top-right or left sidebar)"
echo ""
echo "3. Click 'API' in the left sidebar"
echo ""
echo "4. Click 'Create API Key' button"
echo ""
echo "5. Copy the API key (it will look like: n8n_api_xxxxxxxxxxxxx)"
echo "   ${YELLOW}⚠️  IMPORTANT: Copy it immediately - you won't see it again!${NC}"
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Step 3: Get API key from user
read -p "Paste your API key here: " API_KEY
echo ""

if [ -z "$API_KEY" ]; then
    echo -e "${RED}❌ No API key provided. Exiting.${NC}"
    exit 1
fi

# Step 4: Test the API key
echo -e "${YELLOW}Step 3: Testing API key...${NC}"
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X GET "${PI_N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: ${API_KEY}" \
  -H "Content-Type: application/json" 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2 || echo "000")
BODY=$(echo "$RESPONSE" | sed '/HTTP_CODE/d')

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo -e "${GREEN}✅ API key is valid!${NC}"
    WORKFLOW_COUNT=$(echo "$BODY" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data.get('data', [])))" 2>/dev/null || echo "?")
    echo -e "${GREEN}   Found ${WORKFLOW_COUNT} workflow(s)${NC}"
elif [ "$HTTP_CODE" = "401" ] || [ "$HTTP_CODE" = "403" ]; then
    echo -e "${RED}❌ API key is invalid or unauthorized (HTTP $HTTP_CODE)${NC}"
    echo ""
    echo "Please check:"
    echo "  1. You copied the entire API key"
    echo "  2. The API key was created in the Pi n8n instance"
    echo "  3. Try creating a new API key"
    exit 1
else
    echo -e "${YELLOW}⚠️  Unexpected response (HTTP $HTTP_CODE)${NC}"
    echo "Response: $BODY" | head -5
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi
echo ""

# Step 5: Update .n8n-env.pi file
echo -e "${YELLOW}Step 4: Saving API key to .n8n-env.pi...${NC}"

# Create .n8n-env.pi if it doesn't exist
if [ ! -f .n8n-env.pi ]; then
    cat > .n8n-env.pi << 'EOF'
# n8n Terminal Editing Configuration (Raspberry Pi / LAN)
# ✅ DEFAULT: All workflows use Pi n8n for production
export N8N_URL="http://192.168.1.226:5678"
# Pi is usually accessed over HTTP on LAN; disable secure cookie to avoid the warning banner.
export N8N_SECURE_COOKIE="false"
export N8N_API_KEY=""
export WORKFLOW_FILE="n8n-unity-automation-workflow.json"
export WORKFLOW_ID=""
EOF
    echo -e "${GREEN}✅ Created .n8n-env.pi template${NC}"
fi

# Update API key in .n8n-env.pi
if grep -q "export N8N_API_KEY=" .n8n-env.pi; then
    # Update existing line
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        sed -i '' "s|export N8N_API_KEY=.*|export N8N_API_KEY=\"${API_KEY}\"|" .n8n-env.pi
    else
        # Linux
        sed -i "s|export N8N_API_KEY=.*|export N8N_API_KEY=\"${API_KEY}\"|" .n8n-env.pi
    fi
else
    # Add new line
    echo "export N8N_API_KEY=\"${API_KEY}\"" >> .n8n-env.pi
fi

# Also update N8N_URL to point to Pi
if grep -q "export N8N_URL=" .n8n-env.pi; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s|export N8N_URL=.*|export N8N_URL=\"${PI_N8N_URL}\"|" .n8n-env.pi
    else
        sed -i "s|export N8N_URL=.*|export N8N_URL=\"${PI_N8N_URL}\"|" .n8n-env.pi
    fi
fi

echo -e "${GREEN}✅ API key saved to .n8n-env.pi${NC}"
echo ""

# Step 6: Update .n8n-env (active profile)
echo -e "${YELLOW}Step 5: Updating active .n8n-env profile...${NC}"
read -p "Update .n8n-env to use Pi configuration? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    cp .n8n-env.pi .n8n-env
    echo -e "${GREEN}✅ .n8n-env updated to use Pi configuration${NC}"
else
    echo -e "${YELLOW}⚠️  .n8n-env not updated. Use: ./setup-n8n-terminal.sh pi${NC}"
fi
echo ""

# Step 7: Test CLI access
echo -e "${YELLOW}Step 6: Testing CLI access...${NC}"
source .n8n-env.pi 2>/dev/null || true
export N8N_API_KEY="${API_KEY}"
export N8N_URL="${PI_N8N_URL}"

# Test with a simple API call
RESPONSE=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X GET "${N8N_URL}/api/v1/workflows" \
  -H "X-N8N-API-KEY: ${N8N_API_KEY}" \
  -H "Content-Type: application/json" 2>&1)

HTTP_CODE=$(echo "$RESPONSE" | grep "HTTP_CODE" | cut -d: -f2 || echo "000")

if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ CLI access working!${NC}"
else
    echo -e "${YELLOW}⚠️  CLI test returned HTTP $HTTP_CODE${NC}"
fi
echo ""

# Summary
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ API Key Setup Complete!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${CYAN}📋 Next Steps:${NC}"
echo ""
echo "1. Source the environment:"
echo -e "   ${GREEN}source .n8n-env.pi${NC}"
echo "   Or activate the Pi profile:"
echo -e "   ${GREEN}./setup-n8n-terminal.sh pi${NC}"
echo ""
echo "2. Test CLI import:"
echo -e "   ${GREEN}./scripts/import-orchestrator-cli.sh${NC}"
echo ""
echo "3. Deploy workflows:"
echo -e "   ${GREEN}./deploy-n8n-workflow.sh workflow.json${NC}"
echo ""
echo "4. List workflows:"
echo -e "   ${GREEN}./n8n-list-workflows.sh${NC}"
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

