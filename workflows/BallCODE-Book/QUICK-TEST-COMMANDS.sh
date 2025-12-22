#!/bin/bash
# Quick Test Commands for Orchestrator Workflows
# Copy individual commands as needed

cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env.pi 2>/dev/null

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🧪 ORCHESTRATOR TESTING COMMANDS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 1. Check All Orchestrators
echo "1️⃣  CHECK ALL ORCHESTRATORS:"
echo "curl -s -X GET \"http://192.168.1.226:5678/api/v1/workflows\" \\"
echo "  -H \"X-N8N-API-KEY: \$N8N_API_KEY\" | \\"
echo "  python3 -c \""
echo "import sys, json"
echo "data = json.load(sys.stdin)"
echo "workflows = [w for w in data.get('data', []) if 'orchestrator' in w.get('name', '').lower()]"
echo "for wf in workflows:"
echo "    print(f\"  {'✅' if wf.get('active') else '⏸️ '} {wf.get('name')} (Nodes: {len(wf.get('nodes', []))})\")"
echo "\""
echo ""

# 2. Test Webhook
echo "2️⃣  TEST WEBHOOK:"
echo "curl -X POST http://192.168.1.226:5678/webhook/unity-build \\"
echo "  -H \"Content-Type: application/json\" \\"
echo "  -d '{\"request\": \"Test build\", \"branch\": \"main\"}' | python3 -m json.tool"
echo ""

# 3. Push Fixed V3
echo "3️⃣  PUSH FIXED V3 (Recommended):"
echo "./scripts/push-orchestrator-fixed-v3.sh"
echo ""

# 4. Check Status
echo "4️⃣  CHECK N8N STATUS:"
echo "./scripts/check-n8n-status.sh"
echo ""

# 5. Direct URLs
echo "5️⃣  DIRECT URLS:"
echo "13-Node: http://192.168.1.226:5678/workflow/B6LMAEu5Q2XjdbF6"
echo "4-Node:   http://192.168.1.226:5678/workflow/nqVXVSixEuJrxkr4"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

