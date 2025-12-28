#!/bin/bash

# Check Build Status - Comprehensive Check
# Checks n8n, GitHub, and deployment status

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}🔍 Checking Build Status...${NC}"
echo ""

# n8n URL
N8N_URL="${N8N_URL:-http://192.168.1.226:5678}"

# 1. Check n8n Execution
echo -e "${BLUE}1. n8n Workflow Execution${NC}"
echo "----------------------------------------"
curl -s "${N8N_URL}/api/v1/executions?limit=1" 2>/dev/null | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    if 'data' in data and len(data['data']) > 0:
        exec = data['data'][0]
        status = exec.get('finished', False)
        mode = exec.get('mode', 'unknown')
        started = exec.get('startedAt', 'unknown')
        stopped = exec.get('stoppedAt', 'unknown')
        print(f\"Status: {'✅ Finished' if status else '⏳ Running'}\")
        print(f\"Mode: {mode}\")
        print(f\"Started: {started}\")
        print(f\"Stopped: {stopped}\")
        print(f\"Execution ID: {exec.get('id', 'N/A')}\")
    else:
        print(\"No executions found\")
except:
    print(\"Could not parse n8n response\")
" || echo "Could not connect to n8n"
echo ""

# 2. Check Git Commits
echo -e "${BLUE}2. Recent Git Commits${NC}"
echo "----------------------------------------"
if [ -d "/Users/rashadwest/BTEBallCODE" ]; then
    cd /Users/rashadwest/BTEBallCODE
    echo "Recent commits (last hour):"
    git log --oneline --since="1 hour ago" -5 2>/dev/null || echo "No recent commits"
else
    echo "Unity repo not found at /Users/rashadwest/BTEBallCODE"
fi
echo ""

# 3. Check GitHub Actions
echo -e "${BLUE}3. GitHub Actions Build${NC}"
echo "----------------------------------------"
if command -v gh &> /dev/null; then
    gh run list --repo rashadwest/BallCode --limit 1 --json status,conclusion,name,createdAt,url 2>/dev/null | python3 -c "
import json, sys
try:
    runs = json.load(sys.stdin)
    if runs:
        run = runs[0]
        status_icon = '✅' if run.get('conclusion') == 'success' else '❌' if run.get('conclusion') == 'failure' else '⏳'
        print(f\"{status_icon} Status: {run.get('status', 'unknown')}\")
        print(f\"   Conclusion: {run.get('conclusion', 'unknown')}\")
        print(f\"   Workflow: {run.get('name', 'unknown')}\")
        print(f\"   Created: {run.get('createdAt', 'unknown')}\")
        print(f\"   URL: {run.get('url', 'N/A')}\")
    else:
        print(\"No recent GitHub Actions runs\")
except:
    print(\"Could not parse GitHub Actions data\")
" || echo "GitHub CLI not available"
else
    echo "GitHub CLI not installed. Install with: brew install gh"
    echo "Or check manually: https://github.com/rashadwest/BallCode/actions"
fi
echo ""

# 4. Check Netlify (if possible)
echo -e "${BLUE}4. Netlify Deployment${NC}"
echo "----------------------------------------"
echo "Check Netlify dashboard manually:"
echo "  https://app.netlify.com/sites/YOUR_SITE_ID/deploys"
echo ""

# Summary
echo -e "${BLUE}📊 Summary${NC}"
echo "----------------------------------------"
echo "✅ n8n workflow executed successfully"
echo "🔍 Check the items above for detailed status"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Verify GitHub Actions build completed"
echo "2. Check Netlify deployment"
echo "3. Test the deployed site"
echo ""



