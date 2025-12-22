# All Webhook Terminal Commands - Pi n8n
## Complete Reference for Testing

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 15, 2025  
**n8n URL:** `http://192.168.1.226:5678` (Raspberry Pi)  
**Status:** ✅ Ready for Testing

---

## 🎯 WORKFLOW: Unity Build Orchestrator

### **Webhook Path:** `unity-build`

#### **1. Production URL (Workflow Must Be Active):**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Test build trigger", "branch": "main"}'
```

#### **2. Test URL (Always Works - Recommended for Testing):**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Test build trigger", "branch": "main"}'
```

#### **3. With Full Payload:**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{
    "request": "Fully integrated system test - verifying end-to-end",
    "branch": "main"
  }'
```

#### **4. Pretty Print Response:**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Test build", "branch": "main"}' | python3 -m json.tool
```

#### **5. Verbose Output (See Headers):**
```bash
curl -v -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Test build", "branch": "main"}'
```

#### **6. Save Response to File:**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Test build", "branch": "main"}' \
  -o webhook-response.json && cat webhook-response.json | python3 -m json.tool
```

---

## 🔍 VERIFICATION COMMANDS

### **Check n8n is Running:**
```bash
curl -s http://192.168.1.226:5678/healthz && echo "✅ Pi n8n is running"
```

### **Check Workflow Status:**
```bash
curl -s "http://192.168.1.226:5678/api/v1/workflows" | python3 -c "import json, sys; data = json.load(sys.stdin); workflows = [w for w in data.get('data', []) if 'orchestrator' in w.get('name', '').lower()]; print('Orchestrator workflows:'); [print(f\"  - {w.get('name')} | Active: {w.get('active')}\") for w in workflows]"
```

### **Check Latest Execution:**
```bash
curl -s "http://192.168.1.226:5678/api/v1/executions?limit=1" | python3 -m json.tool | head -30
```

### **Check GitHub Actions Build:**
```bash
gh run list --repo rashadwest/BTEBallCODE --limit 1
```

### **Check Netlify Deployment:**
```bash
# Requires Netlify CLI or check dashboard
open https://app.netlify.com
```

---

## 🧪 TESTING SCRIPTS

### **Test All Webhooks (Automated):**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/test-all-webhooks.sh
# Select option 1 for Pi when prompted
```

### **Quick Test Script:**
```bash
#!/bin/bash
# Quick test for Unity Build Orchestrator
echo "Testing Unity Build Orchestrator webhook..."
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Quick test", "branch": "main"}' | python3 -m json.tool
```

---

## 📋 COMMON TEST SCENARIOS

### **Scenario 1: Basic Build Trigger**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Trigger build", "branch": "main"}'
```

### **Scenario 2: Custom Branch**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Build for feature branch", "branch": "feature/new-level"}'
```

### **Scenario 3: Full Integration Test**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{
    "request": "End-to-end integration test - verify all systems",
    "branch": "main"
  }' | python3 -m json.tool
```

---

## ⚠️ TROUBLESHOOTING

### **If You Get 404 Error:**
```bash
# Workflow not active - use test URL instead
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Test", "branch": "main"}'
```

### **If You Get Connection Error:**
```bash
# Check if Pi n8n is running
curl -v http://192.168.1.226:5678/healthz

# Check if Pi is accessible
ping -c 3 192.168.1.226
```

### **If You Get JSON Error:**
```bash
# Validate JSON payload
echo '{"request": "Test", "branch": "main"}' | python3 -m json.tool
```

---

## 🎯 QUICK REFERENCE

| Action | Command |
|--------|---------|
| **Test Webhook** | `curl -X POST http://192.168.1.226:5678/webhook-test/unity-build -H 'Content-Type: application/json' -d '{"request": "Test", "branch": "main"}'` |
| **Check n8n Status** | `curl -s http://192.168.1.226:5678/healthz` |
| **Check Executions** | `curl -s "http://192.168.1.226:5678/api/v1/executions?limit=1" \| python3 -m json.tool` |
| **Check GitHub Builds** | `gh run list --repo rashadwest/BTEBallCODE --limit 1` |

---

## ✅ EXPECTED SUCCESS RESPONSE

```json
{
  "status": "ok",
  "request": "Test build trigger",
  "triggerType": "webhook",
  "isWebhook": true,
  "branch": "main",
  "timestamp": "2025-12-15T10:40:08.000Z",
  "instanceRole": "prod",
  "github": {
    "ok": true,
    "status": "completed",
    "conclusion": "success",
    "url": "https://github.com/rashadwest/BTEBallCODE/actions/runs/..."
  },
  "netlify": {
    "ok": true,
    "state": "ready",
    "deployUrl": "https://..."
  },
  "siteUrl": "https://ballcode-game.netlify.app",
  "message": "Build dispatched. GH=completed/success NF=ready"
}
```

---

**Version:** 1.0  
**Created:** December 15, 2025  
**Status:** ✅ Complete - Ready for Testing


