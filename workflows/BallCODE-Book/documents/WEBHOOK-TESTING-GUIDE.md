# 🧪 Webhook Testing Guide - Terminal Commands

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Purpose:** Test webhooks via terminal (no UI clicking needed)

---

## 🚀 QUICK TEST COMMANDS

### Test All Webhooks at Once:

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/test-all-webhooks.sh
```

**What it does:**
- Tests all 3 webhooks automatically
- Shows HTTP status codes
- Shows response previews
- Works for localhost or Pi

---

### Test Single Webhook:

```bash
# Test Unity Build
./scripts/test-webhook.sh unity-build

# Test Full Integration
./scripts/test-webhook.sh ballcode-dev

# Test Screenshot Fix
./scripts/test-webhook.sh screenshot-fix

# Test on Pi
./scripts/test-webhook.sh unity-build http://192.168.1.226:5678
```

---

## 📋 MANUAL TEST COMMANDS

### Test Unity Build Orchestrator:

```bash
curl -X POST "http://localhost:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

### Test Full Integration Simplified:

```bash
curl -X POST "http://localhost:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test AI analysis", "mode": "quick"}'
```

### Test Screenshot to Fix:

```bash
curl -X POST "http://localhost:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}'
```

---

## 🎯 TEST ON PI

### Set Pi URL:

```bash
export PI_N8N_URL="http://192.168.1.226:5678"
```

### Test All on Pi:

```bash
./scripts/test-all-webhooks.sh
# Select option 2 when prompted
```

### Test Single on Pi:

```bash
./scripts/test-webhook.sh unity-build http://192.168.1.226:5678
```

---

## ✅ EXPECTED RESPONSES

### Unity Build:
```json
{
  "status": "ok",
  "request": "Test build",
  "branch": "main",
  "message": "Build dispatched..."
}
```

### Full Integration:
```json
{
  "status": "success",
  "actionPlan": {
    "analysis": {...},
    "schemaUpdates": {...}
  }
}
```

### Screenshot Fix:
```json
{
  "requestId": "fix-...",
  "success": true,
  "diagnosis": {...}
}
```

---

## 🚨 TROUBLESHOOTING

### 404 Error:
- ❌ Workflow not imported
- ❌ Workflow not activated
- ❌ Wrong webhook path

**Fix:** Import and activate workflow in n8n UI

### 500 Error:
- ❌ Workflow execution error
- ❌ Missing credentials
- ❌ Invalid node configuration

**Fix:** Check n8n execution logs for details

### No Response:
- ❌ Workflow still running
- ❌ Timeout (workflow too slow)
- ❌ Network issue

**Fix:** Check n8n executions, increase timeout

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Use


