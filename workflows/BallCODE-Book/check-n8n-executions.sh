#!/bin/bash
# Check n8n Workflow Execution History
# Verifies if workflow has been running and shows recent executions

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check if N8N_URL was passed as environment variable (don't override)
if [ -z "$N8N_URL" ]; then
  # Load environment variables from file if not set
  if [ -f .n8n-env ]; then
    source .n8n-env
  fi
fi

# Default n8n URL (use environment variable if set, otherwise default)
N8N_URL="${N8N_URL:-http://localhost:5678}"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🔍 Checking n8n Workflow Execution History${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if n8n is accessible
echo -e "${YELLOW}📡 Checking n8n connection...${NC}"
if curl -s -f "${N8N_URL}/healthz" > /dev/null 2>&1; then
  echo -e "${GREEN}✅ n8n is accessible at: ${N8N_URL}${NC}"
else
  echo -e "${RED}❌ Cannot connect to n8n at: ${N8N_URL}${NC}"
  echo ""
  echo "If n8n is on a remote server (Raspberry Pi), set N8N_URL:"
  echo "  export N8N_URL=http://your-pi-ip:5678"
  echo "  Or create .n8n-env file with: N8N_URL=http://your-pi-ip:5678"
  exit 1
fi

echo ""

# Get list of workflows
echo -e "${YELLOW}📋 Getting list of workflows...${NC}"
WORKFLOWS=$(curl -s "${N8N_URL}/api/v1/workflows" \
  ${N8N_API_KEY:+-H "X-N8N-API-KEY: $N8N_API_KEY"} \
  ${N8N_BASIC_AUTH:+-u "$N8N_BASIC_AUTH"} 2>/dev/null || echo "[]")

if [ "$WORKFLOWS" = "[]" ] || [ -z "$WORKFLOWS" ]; then
  echo -e "${YELLOW}⚠️  No workflows found or API access denied${NC}"
  echo ""
  echo "To check executions manually:"
  echo "  1. Open n8n UI: ${N8N_URL}"
  echo "  2. Click 'Executions' tab at the top"
  echo "  3. See all workflow runs there"
  exit 0
fi

# Find Unity automation workflow
UNITY_WORKFLOW_ID=$(echo "$WORKFLOWS" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for wf in data.get('data', []):
    if 'unity' in wf.get('name', '').lower() or 'automation' in wf.get('name', '').lower():
        print(wf.get('id', ''))
        print(wf.get('name', ''))
        break
" 2>/dev/null | head -1)

if [ -z "$UNITY_WORKFLOW_ID" ]; then
  echo -e "${YELLOW}⚠️  Unity automation workflow not found${NC}"
  echo ""
  echo "Available workflows:"
  echo "$WORKFLOWS" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for wf in data.get('data', []):
    print(f\"  - {wf.get('name', 'Unknown')} (ID: {wf.get('id', 'N/A')})\")
" 2>/dev/null || echo "  (Could not parse workflow list)"
  exit 0
fi

UNITY_WORKFLOW_NAME=$(echo "$WORKFLOWS" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for wf in data.get('data', []):
    if 'unity' in wf.get('name', '').lower() or 'automation' in wf.get('name', '').lower():
        print(wf.get('name', ''))
        break
" 2>/dev/null)

echo -e "${GREEN}✅ Found workflow: ${UNITY_WORKFLOW_NAME}${NC}"
echo -e "   Workflow ID: ${UNITY_WORKFLOW_ID}"
echo ""

# Get executions for this workflow
echo -e "${YELLOW}📊 Getting execution history...${NC}"
EXECUTIONS=$(curl -s "${N8N_URL}/api/v1/executions?workflowId=${UNITY_WORKFLOW_ID}&limit=10" \
  ${N8N_API_KEY:+-H "X-N8N-API-KEY: $N8N_API_KEY"} \
  ${N8N_BASIC_AUTH:+-u "$N8N_BASIC_AUTH"} 2>/dev/null || echo "{}")

# Parse and display executions
echo "$EXECUTIONS" | python3 -c "
import sys, json
from datetime import datetime

try:
    data = json.load(sys.stdin)
    executions = data.get('data', [])
    
    if not executions:
        print('❌ No executions found')
        print('')
        print('This means:')
        print('  - Workflow has not run yet')
        print('  - OR workflow is not active')
        print('  - OR schedule trigger has not fired')
        print('')
        print('To manually trigger:')
        print('  1. Open n8n UI')
        print('  2. Open the workflow')
        print('  3. Click \"Execute Workflow\" button')
        sys.exit(0)
    
    print(f'✅ Found {len(executions)} recent execution(s)')
    print('')
    print('Recent Executions:')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    
    for i, exec in enumerate(executions, 1):
        exec_id = exec.get('id', 'N/A')
        status = exec.get('finished', False)
        mode = exec.get('mode', 'unknown')
        started_at = exec.get('startedAt', '')
        stopped_at = exec.get('stoppedAt', '')
        
        # Parse timestamps
        try:
            if started_at:
                start_dt = datetime.fromisoformat(started_at.replace('Z', '+00:00'))
                start_str = start_dt.strftime('%Y-%m-%d %H:%M:%S')
            else:
                start_str = 'N/A'
            
            if stopped_at:
                stop_dt = datetime.fromisoformat(stopped_at.replace('Z', '+00:00'))
                stop_str = stop_dt.strftime('%Y-%m-%d %H:%M:%S')
            else:
                stop_str = 'Still running'
        except:
            start_str = started_at
            stop_str = stopped_at
        
        # Status indicator
        if status:
            status_icon = '✅'
            status_text = 'Completed'
        else:
            status_icon = '⏳'
            status_text = 'Running'
        
        print(f'{status_icon} Execution #{i}')
        print(f'   ID: {exec_id}')
        print(f'   Status: {status_text}')
        print(f'   Started: {start_str}')
        print(f'   Finished: {stop_str}')
        print(f'   Mode: {mode}')
        print('')
    
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('')
    print('To see more details:')
    print('  1. Open n8n UI')
    print('  2. Click \"Executions\" tab')
    print('  3. Click on any execution to see details')
    
except Exception as e:
    print(f'❌ Error parsing executions: {e}')
    print('')
    print('To check manually:')
    print('  1. Open n8n UI')
    print('  2. Click \"Executions\" tab')
" 2>/dev/null || {
  echo -e "${YELLOW}⚠️  Could not parse execution data${NC}"
  echo ""
  echo "To check manually:"
  echo "  1. Open n8n UI: ${N8N_URL}"
  echo "  2. Click 'Executions' tab at the top"
  echo "  3. Filter by your workflow name"
}

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}✅ Check Complete${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"


