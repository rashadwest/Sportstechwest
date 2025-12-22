# 🧪 Orchestrator Workflow - Testing Commands Reference

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Quick Reference:** All commands to test and verify orchestrator workflows

---

## 📋 QUICK STATUS CHECK

### **Check All Orchestrator Workflows**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env.pi 2>/dev/null
curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  python3 -c "
import sys, json
data = json.load(sys.stdin)
workflows = [w for w in data.get('data', []) if 'orchestrator' in w.get('name', '').lower()]
print(f'Found {len(workflows)} orchestrator workflows:')
for wf in workflows:
    print(f\"  {'✅' if wf.get('active') else '⏸️ '} {wf.get('name')} (ID: {wf.get('id')}, Nodes: {len(wf.get('nodes', []))})\")
"
```

### **Check Specific Workflow by ID**
```bash
# Replace WORKFLOW_ID with actual ID (e.g., B6LMAEu5Q2XjdbF6)
WORKFLOW_ID="B6LMAEu5Q2XjdbF6"
source .n8n-env.pi 2>/dev/null
curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  python3 -c "
import sys, json
wf = json.load(sys.stdin)
print(f\"Name: {wf.get('name')}\")
print(f\"ID: {wf.get('id')}\")
print(f\"Active: {wf.get('active')}\")
print(f\"Nodes: {len(wf.get('nodes', []))}\")
"
```

---

## 🚀 PUSH/IMPORT COMMANDS

### **Push 13-Node Orchestrator (Fixed V3 - Recommended)**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/push-orchestrator-fixed-v3.sh
```

### **Push 13-Node Orchestrator (No Credentials)**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/push-orchestrator-no-credentials.sh
```

### **Push 13-Node Orchestrator (V2 - Old)**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/push-orchestrator-cli-v2.sh
```

---

## 🧪 WEBHOOK TESTING

### **Test 13-Node Orchestrator Webhook**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Test build from command line",
    "branch": "main"
  }' | python3 -m json.tool
```

### **Test 4-Node Minimal Orchestrator Webhook**
```bash
# First, get the webhook path from the workflow
# Then test it (usually same path: /webhook/unity-build)
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Test minimal orchestrator",
    "branch": "main"
  }' | python3 -m json.tool
```

### **Test All Webhooks (Comprehensive)**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/test-all-webhooks.sh
```

---

## 🔍 DIAGNOSTIC COMMANDS

### **Check n8n Status**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/check-n8n-status.sh
```

### **Diagnose Orchestrator Issues**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/diagnose-orchestrator.sh
```

### **Daily n8n Report**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/daily-n8n-report.sh
```

---

## 🗑️ CLEANUP COMMANDS

### **Delete All 13-Node Orchestrators**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env.pi 2>/dev/null
curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  python3 -c "
import sys, json
data = json.load(sys.stdin)
workflows = [w for w in data.get('data', []) if 'orchestrator' in w.get('name', '').lower() and '13 nodes' in w.get('name', '')]
ids = [w.get('id') for w in workflows]
for wf_id in ids:
    print(f\"Deleting: {wf_id}\")
    import subprocess
    subprocess.run(['curl', '-s', '-X', 'DELETE', f'http://192.168.1.226:5678/api/v1/workflows/{wf_id}', '-H', f'X-N8N-API-KEY: {sys.argv[1]}'], env={'N8N_API_KEY': sys.argv[1]})
" "$N8N_API_KEY"
```

### **Delete Specific Workflow by ID**
```bash
WORKFLOW_ID="B6LMAEu5Q2XjdbF6"  # Replace with actual ID
source .n8n-env.pi 2>/dev/null
curl -X DELETE "http://192.168.1.226:5678/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"
```

---

## 🔧 WORKFLOW FIXING COMMANDS

### **Fix Workflow Options (V3)**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 scripts/fix-options-error-v3.py \
  n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json \
  n8n-unity-build-orchestrator-FIXED-V3.json
```

### **Clean Workflow for API (V2)**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 scripts/clean-workflow-for-api-v2.py \
  n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json \
  n8n-unity-build-orchestrator-API-READY-V2.json
```

### **Diagnose Workflow Issues**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 scripts/diagnose-workflow-issues.py \
  n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json
```

---

## 📊 COMPARISON COMMANDS

### **Compare 4-Node vs 13-Node**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env.pi 2>/dev/null

# Get 4-node
curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows/nqVXVSixEuJrxkr4" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" > /tmp/4node.json

# Get 13-node
curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows/B6LMAEu5Q2XjdbF6" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" > /tmp/13node.json

# Compare
python3 -c "
import json
with open('/tmp/4node.json') as f:
    wf4 = json.load(f)
with open('/tmp/13node.json') as f:
    wf13 = json.load(f)
print(f\"4-node: {len(wf4.get('nodes', []))} nodes, Active: {wf4.get('active')}\")
print(f\"13-node: {len(wf13.get('nodes', []))} nodes, Active: {wf13.get('active')}\")
"
```

---

## 🎯 QUICK TEST SEQUENCE

### **Full Test Sequence (Copy & Paste)**
```bash
# 1. Check status
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env.pi 2>/dev/null
echo "=== Checking Orchestrator Workflows ==="
curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  python3 -c "
import sys, json
data = json.load(sys.stdin)
workflows = [w for w in data.get('data', []) if 'orchestrator' in w.get('name', '').lower()]
for wf in workflows:
    print(f\"  {'✅' if wf.get('active') else '⏸️ '} {wf.get('name')} (Nodes: {len(wf.get('nodes', []))})\")
"

# 2. Test webhook (if active)
echo ""
echo "=== Testing Webhook ==="
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test", "branch": "main"}' | python3 -m json.tool

# 3. Check n8n status
echo ""
echo "=== n8n Status ==="
./scripts/check-n8n-status.sh
```

---

## 🔗 DIRECT URLS

### **13-Node Orchestrator (New)**
```
http://192.168.1.226:5678/workflow/B6LMAEu5Q2XjdbF6
```

### **4-Node Minimal Orchestrator**
```
http://192.168.1.226:5678/workflow/nqVXVSixEuJrxkr4
```

### **n8n Home**
```
http://192.168.1.226:5678
```

---

## 📝 NOTES

### **Current Workflow IDs:**
- **13-Node:** `B6LMAEu5Q2XjdbF6` (Inactive)
- **4-Node:** `nqVXVSixEuJrxkr4` (Active)

### **Environment Setup:**
```bash
# Load n8n credentials
source .n8n-env.pi 2>/dev/null

# Verify API key is set
echo "API Key: ${N8N_API_KEY:0:10}..."
```

### **Common Issues:**
- **"Could not find property option"** → Use `push-orchestrator-fixed-v3.sh`
- **Workflow not visible in UI** → Try direct URL or hard refresh browser
- **Webhook 404** → Workflow not active, activate it first

---

**Last Updated:** January 2025  
**Status:** Ready for testing

