# 🧪 Webhook Testing Commands - Quick Reference

**Copyright © 2025 Rashad West. All Rights Reserved.**

**All commands for testing n8n webhooks**

---

## 🎯 ORCHESTRATOR WEBHOOK

### **Basic Test**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

### **Pretty Print JSON Response**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}' | python3 -m json.tool
```

### **With Custom Request Message**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Build Unity game for production", "branch": "main"}'
```

### **With Different Branch**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "develop"}'
```

### **Verbose Output (See Headers)**
```bash
curl -v -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

### **Save Response to File**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}' \
  -o webhook-response.json
```

---

## 🔍 DIAGNOSTIC COMMANDS

### **Check if Webhook is Active**
```bash
curl -I http://192.168.1.226:5678/webhook/unity-build
```

### **Test with GET (Should Fail)**
```bash
curl http://192.168.1.226:5678/webhook/unity-build
```

### **Check Workflow Status**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env.pi 2>/dev/null
curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  python3 -c "
import sys, json
data = json.load(sys.stdin)
workflows = [w for w in data.get('data', []) if 'orchestrator' in w.get('name', '').lower()]
for wf in workflows:
    print(f\"  {'✅' if wf.get('active') else '⏸️ '} {wf.get('name')} (Active: {wf.get('active')})\")
"
```

---

## 📋 FULL INTEGRATION WEBHOOK

### **Test Full Integration Workflow**
```bash
curl -X POST http://192.168.1.226:5678/webhook/full-integration \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Update the game with new features",
    "priority": "high"
  }' | python3 -m json.tool
```

---

## 📸 SCREENSHOT TO FIX WEBHOOK

### **Test Screenshot to Fix Workflow**
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshot_url": "https://example.com/screenshot.png",
    "context": "Button not working on mobile"
  }' | python3 -m json.tool
```

---

## 🧪 TEST ALL WEBHOOKS

### **Run Comprehensive Test Script**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/test-all-webhooks.sh
```

---

## ⚠️ TROUBLESHOOTING

### **Error: "Expecting value: line 1 column 1 (char 0)"**
**Meaning:** Empty response or not JSON

**Possible Causes:**
1. Workflow not active (check toggle switch)
2. Webhook path incorrect
3. Workflow error (check n8n executions)

**Fix:**
```bash
# Check if workflow is active
curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  python3 -c "import sys, json; data=json.load(sys.stdin); workflows=[w for w in data.get('data', []) if 'orchestrator' in w.get('name', '').lower()]; print('Active:', workflows[0].get('active') if workflows else 'Not found')"
```

### **Error: 404 Not Found**
**Meaning:** Webhook doesn't exist

**Fix:**
- Activate the workflow in n8n UI
- Check webhook path is correct: `/webhook/unity-build`

### **Error: 500 Internal Server Error**
**Meaning:** Workflow execution failed

**Fix:**
- Check n8n executions tab for error details
- Verify credentials are set correctly
- Check environment variables

---

## 📝 QUICK COPY-PASTE COMMANDS

### **Morning Test (Copy All)**
```bash
# Test Orchestrator
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Morning test build", "branch": "main"}' | python3 -m json.tool

# Check Status
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env.pi 2>/dev/null
curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  python3 -c "import sys, json; data=json.load(sys.stdin); workflows=[w for w in data.get('data', []) if 'orchestrator' in w.get('name', '').lower()]; [print(f\"  {'✅' if wf.get('active') else '⏸️ '} {wf.get('name')}\") for wf in workflows]"
```

---

## 🔗 WEBHOOK URLS

- **Orchestrator:** `http://192.168.1.226:5678/webhook/unity-build`
- **Full Integration:** `http://192.168.1.226:5678/webhook/full-integration`
- **Screenshot to Fix:** `http://192.168.1.226:5678/webhook/screenshot-fix`

---

**Last Updated:** January 2025  
**Status:** Ready for testing

