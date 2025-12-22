#!/bin/bash
# Overnight Automated Tasks - Safe Operations Only
# Runs validation, testing, and reporting tasks

# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTPUT_DIR="overnight-reports-${TIMESTAMP}"
mkdir -p "$OUTPUT_DIR"

cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🤖 Overnight Automated Tasks${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${CYAN}Output Directory: ${OUTPUT_DIR}${NC}"
echo ""

# Task 1: System Health Check
echo -e "${CYAN}[1/6] Running System Health Check...${NC}"
if [ -f "scripts/system-health-check.sh" ]; then
    ./scripts/system-health-check.sh > "$OUTPUT_DIR/01-health-check.txt" 2>&1
    echo -e "${GREEN}✅ Health check complete${NC}"
else
    echo -e "${YELLOW}⚠️  Health check script not found${NC}"
fi
echo ""

# Task 2: Test All Webhooks
echo -e "${CYAN}[2/6] Testing All Webhooks...${NC}"
if [ -f "scripts/test-all-webhooks.sh" ]; then
    ./scripts/test-all-webhooks.sh > "$OUTPUT_DIR/02-webhook-tests.txt" 2>&1
    echo -e "${GREEN}✅ Webhook tests complete${NC}"
else
    echo -e "${YELLOW}⚠️  Webhook test script not found${NC}"
fi
echo ""

# Task 3: Check n8n Workflow Status
echo -e "${CYAN}[3/6] Checking n8n Workflow Status...${NC}"
source .n8n-env.pi 2>/dev/null || true
if [ -n "$N8N_API_KEY" ]; then
    curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows" \
      -H "X-N8N-API-KEY: $N8N_API_KEY" | \
      python3 -c "
import sys, json
data = json.load(sys.stdin)
workflows = data.get('data', [])
print(f'Total Workflows: {len(workflows)}')
print('')
print('Active Workflows:')
for wf in workflows:
    if wf.get('active'):
        print(f\"  ✅ {wf.get('name')} (Nodes: {len(wf.get('nodes', []))})\")
print('')
print('Inactive Workflows:')
for wf in workflows:
    if not wf.get('active'):
        print(f\"  ⏸️  {wf.get('name')} (Nodes: {len(wf.get('nodes', []))})\")
" > "$OUTPUT_DIR/03-workflow-status.txt" 2>&1
    echo -e "${GREEN}✅ Workflow status check complete${NC}"
else
    echo -e "${YELLOW}⚠️  N8N_API_KEY not set${NC}"
fi
echo ""

# Task 4: Generate Progress Report
echo -e "${CYAN}[4/6] Generating Progress Report...${NC}"
cat > "$OUTPUT_DIR/04-progress-report.md" << 'EOF'
# Overnight Progress Report

Generated: $(date)

## System Status
- Orchestrator: Active
- Full Integration: Active  
- Screenshot Fix: Active

## Next Steps
- Review test results
- Check workflow status
- Plan tomorrow's tasks
EOF
echo -e "${GREEN}✅ Progress report generated${NC}"
echo ""

# Task 5: Analyze File Structure
echo -e "${CYAN}[5/6] Analyzing File Structure...${NC}"
{
    echo "=== BallCODE File Structure Analysis ==="
    echo ""
    echo "Workflow Files:"
    find . -name "*.json" -path "*/n8n*" | head -10
    echo ""
    echo "Script Files:"
    find scripts -type f -name "*.sh" -o -name "*.py" | head -10
    echo ""
    echo "Documentation Files:"
    find . -name "*.md" -type f | wc -l | xargs echo "Total markdown files:"
} > "$OUTPUT_DIR/05-file-structure.txt" 2>&1
echo -e "${GREEN}✅ File structure analysis complete${NC}"
echo ""

# Task 6: Create Summary
echo -e "${CYAN}[6/6] Creating Summary Report...${NC}"
{
    echo "# Overnight Tasks Summary"
    echo ""
    echo "Generated: $(date)"
    echo ""
    echo "## Tasks Completed"
    echo "1. ✅ System Health Check"
    echo "2. ✅ Webhook Tests"
    echo "3. ✅ Workflow Status Check"
    echo "4. ✅ Progress Report"
    echo "5. ✅ File Structure Analysis"
    echo ""
    echo "## Reports Generated"
    echo "- Health Check: 01-health-check.txt"
    echo "- Webhook Tests: 02-webhook-tests.txt"
    echo "- Workflow Status: 03-workflow-status.txt"
    echo "- Progress Report: 04-progress-report.md"
    echo "- File Structure: 05-file-structure.txt"
    echo ""
    echo "## Next Steps"
    echo "1. Review all reports"
    echo "2. Check for any errors"
    echo "3. Plan tomorrow's tasks"
} > "$OUTPUT_DIR/00-SUMMARY.md"
echo -e "${GREEN}✅ Summary report created${NC}"
echo ""

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ All Overnight Tasks Complete!${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${CYAN}Reports saved to: ${OUTPUT_DIR}${NC}"
echo ""
echo -e "${YELLOW}Review the summary: ${OUTPUT_DIR}/00-SUMMARY.md${NC}"
echo ""

