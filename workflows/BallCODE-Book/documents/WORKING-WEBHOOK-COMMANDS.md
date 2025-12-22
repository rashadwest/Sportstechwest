# ✅ Working Webhook Commands - Use These

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Pi n8n URL:** `http://192.168.1.226:5678`

---

## 🚀 QUICK COMMANDS (USE TEST URLs - They Always Work)

### 1. Unity Build Orchestrator

```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build from terminal", "branch": "main"}'
```

**One-liner:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/unity-build" -H "Content-Type: application/json" -d '{"request": "Test build", "branch": "main"}'
```

---

### 2. BallCODE Full Integration - AI Analysis (Simplified)

```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test AI analysis from terminal", "mode": "quick"}'
```

**One-liner:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/ballcode-dev" -H "Content-Type: application/json" -d '{"prompt": "Test AI analysis", "mode": "quick"}'
```

---

### 3. Screenshot-to-Fix Automation

```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test-error.png", "context": "Terminal test - n8n workflow error"}'
```

**One-liner:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook-test/screenshot-fix" -H "Content-Type: application/json" -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}'
```

---

## 📋 ALL 3 COMMANDS IN ONE PLACE

```bash
# 1. Unity Build
curl -X POST "http://192.168.1.226:5678/webhook-test/unity-build" -H "Content-Type: application/json" -d '{"request": "Test build", "branch": "main"}'

# 2. Full Integration
curl -X POST "http://192.168.1.226:5678/webhook-test/ballcode-dev" -H "Content-Type: application/json" -d '{"prompt": "Test AI analysis", "mode": "quick"}'

# 3. Screenshot Fix
curl -X POST "http://192.168.1.226:5678/webhook-test/screenshot-fix" -H "Content-Type: application/json" -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}'
```

---

## 🔑 KEY DIFFERENCE

**Test URLs (`/webhook-test/`):**
- ✅ Work even when workflows are inactive
- ✅ Show execution on canvas
- ✅ Best for testing

**Production URLs (`/webhook/`):**
- ❌ Require workflows to be active
- ❌ Don't show on canvas (only in executions list)
- ⚠️ Use only when workflow is confirmed active

---

## 🎯 WORKFLOW NAME → WEBHOOK PATH MAPPING

| Workflow Name | Test URL | Production URL |
|--------------|----------|----------------|
| BallCODE Orchestrator (WORKING CLONE) | `/webhook-test/unity-build` | `/webhook/unity-build` |
| BallCODE Full Integration - AI Analysis (Simplified) | `/webhook-test/ballcode-dev` | `/webhook/ballcode-dev` |
| Screenshot-to-Fix Automation | `/webhook-test/screenshot-fix` | `/webhook/screenshot-fix` |

---

## ✅ EXPECTED RESPONSES

**Success (200/201):**
- JSON response with workflow execution results
- Check n8n "Executions" tab to see workflow run
- For test URLs: You'll see execution on canvas

**Error (404):**
- Wrong webhook path
- n8n not running on Pi
- Check: `curl -s http://192.168.1.226:5678/healthz`

**Error (500):**
- Workflow execution error
- Check n8n execution logs for details

---

## 🧪 TEST ALL AT ONCE

```bash
#!/bin/bash
N8N_URL="http://192.168.1.226:5678"

echo "1️⃣ Unity Build..."
curl -s -X POST "${N8N_URL}/webhook-test/unity-build" -H "Content-Type: application/json" -d '{"request":"Test","branch":"main"}' | head -c 100 && echo " ✅"

echo "2️⃣ Full Integration..."
curl -s -X POST "${N8N_URL}/webhook-test/ballcode-dev" -H "Content-Type: application/json" -d '{"prompt":"Test","mode":"quick"}' | head -c 100 && echo " ✅"

echo "3️⃣ Screenshot Fix..."
curl -s -X POST "${N8N_URL}/webhook-test/screenshot-fix" -H "Content-Type: application/json" -d '{"screenshotUrl":"test","context":"test"}' | head -c 100 && echo " ✅"

echo "✅ All webhooks tested"
```

---

**Version:** 1.0  
**Created:** December 16, 2025  
**Status:** ✅ These are the working commands from previous documentation


