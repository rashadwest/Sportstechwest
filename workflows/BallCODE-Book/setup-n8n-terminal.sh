#!/bin/bash
# n8n Terminal Editing Setup Script
# Sets up the complete terminal-based n8n workflow editing system

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 n8n Terminal Editing Setup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if .n8n-env exists
if [ ! -f .n8n-env ]; then
    echo -e "${YELLOW}⚠️  .n8n-env file not found. Creating template...${NC}"
    cat > .n8n-env << 'EOF'
# n8n Terminal Editing Configuration
export N8N_URL="http://localhost:5678"
export N8N_SECURE_COOKIE="false"
export N8N_API_KEY=""
export WORKFLOW_FILE="n8n-unity-automation-workflow.json"
export WORKFLOW_ID=""
EOF
    echo -e "${GREEN}✅ Created .n8n-env template${NC}"
    echo ""
fi

# Check n8n CLI
echo -e "${YELLOW}🔍 Checking n8n CLI...${NC}"
if command -v n8n &> /dev/null; then
    N8N_VERSION=$(n8n --version 2>/dev/null || echo "installed")
    echo -e "${GREEN}✅ n8n CLI installed ($N8N_VERSION)${NC}"
    echo ""
    echo "Available n8n CLI commands:"
    echo "  ${YELLOW}n8n export:workflow${NC} - Export workflows"
    echo "  ${YELLOW}n8n import:workflow${NC} - Import workflows"
    echo "  ${YELLOW}./n8n-edit-workflow.sh${NC} - Edit workflow in terminal"
    echo "  ${YELLOW}./n8n-list-workflows.sh${NC} - List all workflows"
    echo ""
else
    echo -e "${YELLOW}⚠️  n8n CLI not found in PATH${NC}"
    echo "   Install with: npm install -g n8n"
fi

# Make scripts executable
echo -e "${YELLOW}📝 Making scripts executable...${NC}"
chmod +x deploy-n8n-workflow.sh 2>/dev/null || true
chmod +x n8n-workflow-editor.sh 2>/dev/null || true
chmod +x n8n-edit-workflow.sh 2>/dev/null || true
chmod +x n8n-list-workflows.sh 2>/dev/null || true
chmod +x debug-workflow.py 2>/dev/null || true
chmod +x fix-workflow-file.py 2>/dev/null || true
chmod +x update-workflow.py 2>/dev/null || true
echo -e "${GREEN}✅ Scripts are executable${NC}"
echo ""

# Check Python dependencies
echo -e "${YELLOW}🔍 Checking Python dependencies...${NC}"
if python3 -c "import requests" 2>/dev/null; then
    echo -e "${GREEN}✅ requests library installed${NC}"
else
    echo -e "${YELLOW}⚠️  Installing requests library...${NC}"
    pip3 install requests 2>/dev/null || echo -e "${RED}❌ Failed to install requests. Run: pip3 install requests${NC}"
fi
echo ""

# Load environment
if [ -f .n8n-env ]; then
    source .n8n-env
    echo -e "${GREEN}✅ Loaded .n8n-env${NC}"
    echo ""
    echo "Current configuration:"
    echo "  N8N_URL: ${N8N_URL:-not set}"
    echo "  N8N_API_KEY: ${N8N_API_KEY:+set (hidden)}${N8N_API_KEY:-not set}"
    echo "  WORKFLOW_FILE: ${WORKFLOW_FILE:-not set}"
    echo ""
fi

# Test n8n connection
echo -e "${YELLOW}🔍 Testing n8n connection...${NC}"
N8N_URL="${N8N_URL:-http://localhost:5678}"
if curl -s -f "${N8N_URL}/healthz" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ n8n is accessible at ${N8N_URL}${NC}"
elif curl -s -f "${N8N_URL}" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ n8n is accessible at ${N8N_URL}${NC}"
else
    echo -e "${YELLOW}⚠️  Cannot connect to n8n at ${N8N_URL}${NC}"
    echo "   Make sure n8n is running and update N8N_URL in .n8n-env"
fi
echo ""

# Summary
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Next steps:"
echo ""
echo "1. Configure .n8n-env:"
echo "   ${YELLOW}nano .n8n-env${NC}"
echo "   - Set N8N_URL to your n8n instance"
echo "   - Set N8N_API_KEY (optional, get from n8n UI → Settings → API)"
echo ""
echo "2. Source the environment:"
echo "   ${YELLOW}source .n8n-env${NC}"
echo ""
echo "3. List workflows to get IDs:"
echo "   ${YELLOW}./n8n-list-workflows.sh${NC}"
echo ""
echo "4. Edit workflow in terminal:"
echo "   ${YELLOW}./n8n-edit-workflow.sh WORKFLOW_ID${NC}"
echo "   ${YELLOW}./n8n-edit-workflow.sh WORKFLOW_ID vim${NC}  # Use vim"
echo ""
echo "5. Or use API-based tools:"
echo "   ${YELLOW}./n8n-workflow-editor.sh n8n-unity-automation-workflow.json${NC}"
echo "   ${YELLOW}python3 debug-workflow.py workflow.json${NC}"
echo "   ${YELLOW}./deploy-n8n-workflow.sh workflow.json${NC}"
echo ""
echo "📖 Full documentation: N8N-CURSOR-EDITING-SYSTEM.md"
echo ""


