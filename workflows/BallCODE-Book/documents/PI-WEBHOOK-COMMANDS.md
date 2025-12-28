# 🥧 Pi Webhook Test Commands - Copy & Paste

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Pi n8n URL:** `http://192.168.1.226:5678`

---

## 🚀 COPY-PASTE COMMANDS FOR PI

### Test Unity Build Orchestrator (Pi):

```bash
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build from terminal", "branch": "main"}'
```

### Test Full Integration Simplified (Pi):

```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test AI analysis from terminal", "mode": "quick"}'
```

### Test Screenshot to Fix (Pi):

```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test-error.png", "context": "Terminal test - n8n workflow error"}'
```

---

## 📝 ONE-LINER VERSIONS (Pi)

### Unity Build:
```bash
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" -H "Content-Type: application/json" -d '{"request": "Test build", "branch": "main"}'
```

### Full Integration:
```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" -H "Content-Type: application/json" -d '{"prompt": "Test AI analysis", "mode": "quick"}'
```

### Screenshot Fix:
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" -H "Content-Type: application/json" -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}'
```

---

## 💡 USING ENVIRONMENT VARIABLE (Pi)

### Set Pi URL:
```bash
export PI_N8N_URL="http://192.168.1.226:5678"
```

### Then use:
```bash
curl -X POST "$PI_N8N_URL/webhook/unity-build" -H "Content-Type: application/json" -d '{"request": "Test build", "branch": "main"}'
```

---

## ✅ EXPECTED RESPONSES

**Success (200/201):**
- JSON response with workflow execution results

**Error (404):**
- Workflow not imported or not activated on Pi
- Check Pi n8n UI: `http://192.168.1.226:5678`

**Error (500):**
- Workflow execution error
- Check Pi n8n execution logs

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready for Pi Testing



