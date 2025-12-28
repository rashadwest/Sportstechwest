# All 3 Workflows - Complete Pi n8n Verification
## End-to-End Check for All Workflows

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 15, 2025  
**Purpose:** Verify all 3 workflows use Pi n8n infrastructure  
**Status:** ✅ Ready for Testing

---

## 🎯 THE 3 WORKFLOWS

### **1. Unity Build Orchestrator** ✅
- **File:** `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`
- **Webhook Path:** `unity-build`
- **Nodes:** 13
- **Status:** ✅ Verified - No localhost references

### **2. BallCODE Full Integration - AI Analysis (Simplified)** ✅
- **File:** `n8n-ballcode-full-integration-workflow-SIMPLIFIED.json`
- **Webhook Path:** `ballcode-dev`
- **Nodes:** 5
- **Status:** ✅ Verified - No localhost references

### **3. Screenshot-to-Fix Automation** ✅
- **File:** `n8n-screenshot-to-fix-workflow.json`
- **Webhook Path:** `screenshot-fix`
- **Nodes:** ~10
- **Status:** ✅ Verified - No localhost references

---

## ✅ INFRASTRUCTURE VERIFICATION SUMMARY

### **All 3 Workflows:**
- ✅ **0 localhost references** found
- ✅ **0 Mac-specific URLs** found
- ✅ **All webhooks use relative paths** (work with any n8n instance)
- ✅ **All external APIs:** OpenAI, GitHub, Netlify (not n8n URLs)
- ✅ **Ready for Pi deployment**

---

## 🧪 TERMINAL COMMANDS FOR ALL 3 WEBHOOKS

### **1. Unity Build Orchestrator**

#### **Test URL (Recommended):**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Test build", "branch": "main"}'
```

#### **Production URL (If Active):**
```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Test build", "branch": "main"}'
```

#### **With Pretty Print:**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Test build", "branch": "main"}' | python3 -m json.tool
```

---

### **2. BallCODE Full Integration - AI Analysis**

#### **Test URL (Recommended):**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/ballcode-dev \
  -H 'Content-Type: application/json' \
  -d '{"prompt": "Test AI analysis", "mode": "quick"}'
```

#### **Production URL (If Active):**
```bash
curl -X POST http://192.168.1.226:5678/webhook/ballcode-dev \
  -H 'Content-Type: application/json' \
  -d '{"prompt": "Test AI analysis", "mode": "quick"}'
```

#### **With Full Mode:**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/ballcode-dev \
  -H 'Content-Type: application/json' \
  -d '{
    "prompt": "Create new level for Book 1",
    "mode": "full",
    "context": {"bookId": 1, "levelType": "coding"}
  }' | python3 -m json.tool
```

---

### **3. Screenshot-to-Fix Automation**

#### **Test URL (Recommended):**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/screenshot-fix \
  -H 'Content-Type: application/json' \
  -d '{
    "screenshotUrl": "https://example.com/error-screenshot.png",
    "context": "n8n workflow error"
  }'
```

#### **Production URL (If Active):**
```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H 'Content-Type: application/json' \
  -d '{
    "screenshotUrl": "https://example.com/error-screenshot.png",
    "context": "n8n workflow error"
  }'
```

#### **With Pretty Print:**
```bash
curl -X POST http://192.168.1.226:5678/webhook-test/screenshot-fix \
  -H 'Content-Type: application/json' \
  -d '{
    "screenshotUrl": "https://example.com/error-screenshot.png",
    "context": "n8n workflow error"
  }' | python3 -m json.tool
```

---

## 🚀 TEST ALL 3 AT ONCE

### **Using Test Script:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/test-all-webhooks.sh
# Select option 1 for Pi when prompted
```

### **Manual Test All 3:**
```bash
# Test 1: Unity Build
echo "Testing Unity Build Orchestrator..."
curl -X POST http://192.168.1.226:5678/webhook-test/unity-build \
  -H 'Content-Type: application/json' \
  -d '{"request": "Test", "branch": "main"}' && echo ""

# Test 2: Full Integration
echo "Testing Full Integration..."
curl -X POST http://192.168.1.226:5678/webhook-test/ballcode-dev \
  -H 'Content-Type: application/json' \
  -d '{"prompt": "Test", "mode": "quick"}' && echo ""

# Test 3: Screenshot Fix
echo "Testing Screenshot Fix..."
curl -X POST http://192.168.1.226:5678/webhook-test/screenshot-fix \
  -H 'Content-Type: application/json' \
  -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test"}' && echo ""
```

---

## 📋 PRE-TEST CHECKLIST FOR ALL 3

### **Before Testing:**
- [ ] All 3 workflows imported into Pi n8n
- [ ] All 3 workflows are ACTIVE (toggle ON)
- [ ] Environment variables set on Pi (for Unity Build Orchestrator)
- [ ] Credentials configured:
  - [ ] OpenAI API (for Full Integration & Screenshot Fix)
  - [ ] GitHub Actions Token (for Unity Build Orchestrator)
  - [ ] Netlify API Token (for Unity Build Orchestrator)

---

## 📊 WEBHOOK URL REFERENCE

| Workflow | Webhook Path | Test URL | Production URL |
|----------|-------------|----------|----------------|
| **Unity Build Orchestrator** | `unity-build` | `http://192.168.1.226:5678/webhook-test/unity-build` | `http://192.168.1.226:5678/webhook/unity-build` |
| **Full Integration** | `ballcode-dev` | `http://192.168.1.226:5678/webhook-test/ballcode-dev` | `http://192.168.1.226:5678/webhook/ballcode-dev` |
| **Screenshot Fix** | `screenshot-fix` | `http://192.168.1.226:5678/webhook-test/screenshot-fix` | `http://192.168.1.226:5678/webhook/screenshot-fix` |

---

## ✅ VERIFICATION COMPLETE

**All 3 workflows verified:**
- ✅ No localhost references
- ✅ All webhooks use relative paths (Pi-compatible)
- ✅ All external APIs verified
- ✅ Ready for Pi deployment and testing

**Ready to test all 3 workflows!** 🚀

---

**Version:** 1.0  
**Created:** December 15, 2025  
**Status:** ✅ Complete - Ready for Testing



