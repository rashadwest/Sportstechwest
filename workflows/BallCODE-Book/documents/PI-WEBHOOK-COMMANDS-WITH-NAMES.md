# 🥧 Pi Webhook Commands - With Workflow Names

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Pi n8n URL:** `http://192.168.1.226:5678`

---

## 🚀 WEBHOOK TRIGGER COMMANDS

### 1. Screenshot-to-Fix Automation - Visual Debugging & Auto-Repair

```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test-error.png", "context": "Terminal test - n8n workflow error"}'
```

**One-liner:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" -H "Content-Type: application/json" -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}'
```

---

### 2. BallCODE Full Integration - AI Analysis (Simplified)

```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test AI analysis from terminal", "mode": "quick"}'
```

**One-liner:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" -H "Content-Type: application/json" -d '{"prompt": "Test AI analysis", "mode": "quick"}'
```

---

### 3. BallCODE Orchestrator (WORKING CLONE)

```bash
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build from terminal", "branch": "main"}'
```

**One-liner:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" -H "Content-Type: application/json" -d '{"request": "Test build", "branch": "main"}'
```

---

## 📋 ALL COMMANDS IN ONE PLACE

```bash
# 1. Screenshot-to-Fix Automation
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" -H "Content-Type: application/json" -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}'

# 2. BallCODE Full Integration - AI Analysis (Simplified)
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" -H "Content-Type: application/json" -d '{"prompt": "Test AI analysis", "mode": "quick"}'

# 3. BallCODE Orchestrator (WORKING CLONE)
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" -H "Content-Type: application/json" -d '{"request": "Test build", "branch": "main"}'
```

---

## 🎯 WORKFLOW NAME → WEBHOOK PATH MAPPING

| Workflow Name | Webhook Path | Full URL |
|--------------|--------------|----------|
| Screenshot-to-Fix Automation - Visual Debugging & Auto-Repair | `screenshot-fix` | `http://192.168.1.226:5678/webhook/screenshot-fix` |
| BallCODE Full Integration - AI Analysis (Simplified) | `ballcode-dev` | `http://192.168.1.226:5678/webhook/ballcode-dev` |
| BallCODE Orchestrator (WORKING CLONE) | `unity-build` | `http://192.168.1.226:5678/webhook/unity-build` |

---

## ✅ EXPECTED RESPONSES

**Success (200/201):**
- JSON response with workflow execution results
- Check n8n "Executions" tab to see workflow run

**Error (404):**
- Workflow not active (but you showed they're all active ✅)
- Wrong webhook path
- n8n not running on Pi

**Error (500):**
- Workflow execution error
- Check n8n execution logs for details

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Use


