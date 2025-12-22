# n8n URL Configuration

**Date:** December 17, 2025  
**Status:** Active Configuration

---

## 🎯 PRIMARY n8n INSTANCE

**URL:** `http://192.168.1.226:5678/`

**This is the ONLY n8n instance we use.**

---

## ✅ CONFIRMED IN CODE

### Scripts Using This URL:

1. **`scripts/garvis-execution-engine.py`**
   - Default: `http://192.168.1.226:5678`
   - Environment variable: `N8N_BASE_URL`
   - Line 37: `N8N_BASE_URL = os.getenv("N8N_BASE_URL", "http://192.168.1.226:5678")`

2. **`scripts/verify-garvis-unity-integration.py`**
   - Default: `http://192.168.1.226:5678`
   - Environment variable: `N8N_URL`

---

## 🔗 WEBHOOK ENDPOINTS

All webhooks use this base URL:

- **Garvis Orchestrator:** `http://192.168.1.226:5678/webhook/garvis`
- **Unity Build Orchestrator:** `http://192.168.1.226:5678/webhook/unity-build`
- **Full Integration:** `http://192.168.1.226:5678/webhook/ballcode-dev`
- **Website Auto-Update:** `http://192.168.1.226:5678/webhook/website-update`
- **School Onboarding:** `http://192.168.1.226:5678/webhook/school-onboarding`
- **Sales Automation:** `http://192.168.1.226:5678/webhook/sales-automation`

---

## 📝 RULE FOR ALL FUTURE WORK

**Always use:** `http://192.168.1.226:5678/`

**Never use:** `localhost:5678` or `127.0.0.1:5678`

**Exception:** Only if explicitly overridden via environment variable `N8N_URL` or `N8N_BASE_URL`

---

## 🧪 QUICK TEST

```bash
# Test n8n is accessible
curl http://192.168.1.226:5678/healthz

# Test webhook
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Test", "branch": "main"}'
```

---

**This URL is saved to memory and should be used for all n8n interactions.** ✅

