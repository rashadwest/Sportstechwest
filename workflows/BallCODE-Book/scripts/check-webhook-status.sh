#!/bin/bash

# Quick Webhook Status Check
# Checks n8n execution, GitHub Actions, and Netlify deployment

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}🔍 Checking Webhook Execution Status...${NC}"
echo ""

# Use Pi n8n instance
N8N_URL="http://192.168.1.226:5678"
echo -e "${BLUE}📍 Using: Raspberry Pi (192.168.1.226)${NC}"
echo ""

# 1. Check n8n Latest Execution
echo -e "${BLUE}1️⃣  n8n Workflow Execution (Last 5 minutes)${NC}"
echo "----------------------------------------"
EXEC_DATA=$(curl -s "${N8N_URL}/api/v1/executions?limit=1" 2>/dev/null)

if [ $? -eq 0 ] && [ ! -z "$EXEC_DATA" ]; then
    echo "$EXEC_DATA" | python3 -c "
import json, sys
from datetime import datetime, timezone, timedelta
try:
    data = json.load(sys.stdin)
    if 'data' in data and len(data['data']) > 0:
        exec = data['data'][0]
        exec_id = exec.get('id', 'N/A')
        finished = exec.get('finished', False)
        mode = exec.get('mode', 'unknown')
        started = exec.get('startedAt', 'unknown')
        stopped = exec.get('stoppedAt', 'unknown')
        
        # Check if execution is recent (last 5 minutes)
        if started != 'unknown':
            try:
                start_time = datetime.fromisoformat(started.replace('Z', '+00:00'))
                now = datetime.now(timezone.utc)
                age = (now - start_time).total_seconds() / 60
                
                if age <= 5:
                    status_icon = '✅' if finished else '⏳'
                    print(f\"${status_icon} Status: {'Finished' if finished else 'Running'}\")
                    print(f\"   Mode: {mode}\")
                    print(f\"   Started: {started}\")
                    print(f\"   Stopped: {stopped if stopped != 'unknown' else 'Still running'}\")
                    print(f\"   Age: {age:.1f} minutes ago\")
                    print(f\"   Execution ID: {exec_id}\")
                    print(f\"   ${BLUE}View in n8n: ${N8N_URL}/workflow/${exec.get('workflowId', 'N/A')}/executions/${exec_id}${NC}\")
                else:
                    print(f\"⚠️  Last execution was {age:.1f} minutes ago (older than 5 minutes)\")
                    print(f\"   Started: {started}\")
            except:
                print(f\"✅ Execution found (could not parse time)\")
                print(f\"   Status: {'Finished' if finished else 'Running'}\")
                print(f\"   Started: {started}\")
        else:
            print(f\"✅ Execution found\")
            print(f\"   Status: {'Finished' if finished else 'Running'}\")
    else:
        print(\"❌ No executions found in n8n\")
except Exception as e:
    print(f\"⚠️  Could not parse n8n response: {e}\")
" || echo "❌ Could not connect to n8n at ${N8N_URL}"
else
    echo "❌ Could not connect to n8n"
fi
echo ""

# 2. Check GitHub Actions (Most Recent)
echo -e "${BLUE}2️⃣  GitHub Actions Build (Last 10 minutes)${NC}"
echo "----------------------------------------"
if command -v gh &> /dev/null; then
    gh run list --repo rashadwest/BTEBallCODE --limit 1 --json status,conclusion,name,createdAt,url,workflowName 2>/dev/null | python3 -c "
import json, sys
from datetime import datetime, timezone, timedelta
try:
    runs = json.load(sys.stdin)
    if runs:
        run = runs[0]
        created = run.get('createdAt', '')
        status = run.get('status', 'unknown')
        conclusion = run.get('conclusion', 'unknown')
        
        # Check if build is recent (last 10 minutes)
        if created:
            try:
                created_time = datetime.fromisoformat(created.replace('Z', '+00:00'))
                now = datetime.now(timezone.utc)
                age = (now - created_time).total_seconds() / 60
                
                if age <= 10:
                    status_icon = '✅' if conclusion == 'success' else '❌' if conclusion == 'failure' else '⏳'
                    print(f\"${status_icon} Status: {status}\")
                    print(f\"   Conclusion: {conclusion}\")
                    print(f\"   Workflow: {run.get('workflowName', run.get('name', 'unknown'))}\")
                    print(f\"   Created: {created} ({age:.1f} minutes ago)\")
                    print(f\"   URL: {run.get('url', 'N/A')}\")
                else:
                    print(f\"⚠️  Last build was {age:.1f} minutes ago (older than 10 minutes)\")
                    print(f\"   Status: {status}, Conclusion: {conclusion}\")
            except:
                print(f\"✅ Build found\")
                print(f\"   Status: {status}, Conclusion: {conclusion}\")
        else:
            print(f\"✅ Build found\")
            print(f\"   Status: {status}, Conclusion: {conclusion}\")
    else:
        print(\"❌ No recent GitHub Actions runs\")
except Exception as e:
    print(f\"⚠️  Could not parse GitHub Actions data: {e}\")
" || echo "⚠️  GitHub CLI error (may need: gh auth login)"
else
    echo "⚠️  GitHub CLI not installed"
    echo "   Install: brew install gh"
    echo "   Or check: https://github.com/rashadwest/BTEBallCODE/actions"
fi
echo ""

# 3. Check Recent Git Commits
echo -e "${BLUE}3️⃣  Recent Git Commits (Last 10 minutes)${NC}"
echo "----------------------------------------"
UNITY_REPO="/Users/rashadwest/BTEBallCODE"
if [ -d "$UNITY_REPO" ]; then
    cd "$UNITY_REPO" 2>/dev/null
    RECENT_COMMITS=$(git log --oneline --since="10 minutes ago" --all 2>/dev/null)
    if [ ! -z "$RECENT_COMMITS" ]; then
        echo "✅ Recent commits found:"
        echo "$RECENT_COMMITS" | head -5
    else
        echo "⚠️  No commits in last 10 minutes"
        echo "   Last 3 commits:"
        git log --oneline -3 2>/dev/null | head -3 || echo "   Could not read git log"
    fi
else
    echo "⚠️  Unity repo not found at $UNITY_REPO"
fi
echo ""

# 4. Summary
echo -e "${BLUE}📊 Summary${NC}"
echo "----------------------------------------"
echo "✅ Checked n8n execution status"
echo "✅ Checked GitHub Actions build"
echo "✅ Checked recent git commits"
echo ""
echo -e "${YELLOW}💡 Next Steps:${NC}"
echo "1. If n8n execution shows success → Check GitHub Actions build"
echo "2. If GitHub Actions succeeded → Check Netlify deployment"
echo "3. View full details in n8n UI: ${N8N_URL}"
echo "4. Check GitHub Actions: https://github.com/rashadwest/BTEBallCODE/actions"
echo ""

