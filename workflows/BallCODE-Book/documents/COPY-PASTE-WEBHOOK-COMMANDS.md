# 📋 Copy-Paste Webhook Test Commands

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Purpose:** Direct curl commands you can copy/paste (no script needed)

---

## 🚀 QUICK COPY-PASTE COMMANDS

### Test Unity Build Orchestrator:

```bash
curl -X POST "http://localhost:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build from terminal", "branch": "main"}'
```

### Test Full Integration Simplified:

```bash
curl -X POST "http://localhost:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test AI analysis from terminal", "mode": "quick"}'
```

### Test Screenshot to Fix:

```bash
curl -X POST "http://localhost:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test-error.png", "context": "Terminal test - n8n workflow error"}'
```

---

## 🎯 TEST ON PI (192.168.1.226:5678)

### Unity Build (Pi):

```bash
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build from terminal", "branch": "main"}'
```

### Full Integration (Pi):

```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test AI analysis from terminal", "mode": "quick"}'
```

### Screenshot Fix (Pi):

```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test-error.png", "context": "Terminal test - n8n workflow error"}'
```

---

## 💡 USING ENVIRONMENT VARIABLES

### If you've sourced `.n8n-env`:

```bash
# Source the environment first
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env

# Then use $N8N_URL variable
curl -X POST "$N8N_URL/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

---

## 📝 ONE-LINER VERSIONS (No Line Breaks)

### Unity Build:
```bash
curl -X POST "http://localhost:5678/webhook/unity-build" -H "Content-Type: application/json" -d '{"request": "Test build", "branch": "main"}'
```

### Full Integration:
```bash
curl -X POST "http://localhost:5678/webhook/ballcode-dev" -H "Content-Type: application/json" -d '{"prompt": "Test AI analysis", "mode": "quick"}'
```

### Screenshot Fix:
```bash
curl -X POST "http://localhost:5678/webhook/screenshot-fix" -H "Content-Type: application/json" -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}'
```

---

## ✅ EXPECTED RESPONSES

**Success (200/201):**
- JSON response with workflow execution results
- Status codes and data from workflow

**Error (404):**
- Workflow not imported or not activated
- Check n8n UI to import/activate workflow

**Error (500):**
- Workflow execution error
- Check n8n execution logs for details

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Copy-Paste


