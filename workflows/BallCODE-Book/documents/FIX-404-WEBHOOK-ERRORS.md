# 🔧 Fix 404 Webhook Errors - Import & Activate Workflows

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Problem:** 404 errors - "webhook is not registered"  
**Solution:** Import and activate workflows on Pi n8n

---

## 🚨 PROBLEM

**Error:** `{"code":404,"message":"The requested webhook \"POST screenshot-fix\" is not registered."}`

**Cause:** Workflows are either:
1. ❌ Not imported into Pi n8n
2. ❌ Imported but not activated (toggle is OFF)

---

## ✅ SOLUTION - STEP BY STEP

### Step 1: Access Pi n8n UI

1. Open browser: `http://192.168.1.226:5678`
2. Login to n8n (if required)

---

### Step 2: Import Workflows (One by One)

**For each workflow file in `~/Desktop/n8n-workflows-to-import/`:**

1. **Click "Workflows"** in left sidebar
2. **Click "Import from File"** (top right)
3. **Select workflow file:**
   - `n8n-screenshot-to-fix-workflow.json`
   - `n8n-ballcode-full-integration-workflow-SIMPLIFIED.json`
   - `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`
4. **Click "Import"**

**Repeat for all 3 workflows.**

---

### Step 3: Activate Each Workflow

**For each imported workflow:**

1. **Click on the workflow** to open it
2. **Look for toggle switch** in top-right corner (next to "Save" button)
3. **Click toggle to turn it ON** (should turn blue/green)
4. **Click "Save"** (if prompted)

**You should see:**
- ✅ Toggle is ON (blue/green)
- ✅ No red error messages
- ✅ Webhook URL visible in webhook node

---

### Step 4: Verify Webhook Paths

**Check that webhook paths match:**

1. **Screenshot Fix:**
   - Webhook path: `screenshot-fix`
   - URL: `http://192.168.1.226:5678/webhook/screenshot-fix`

2. **Full Integration:**
   - Webhook path: `ballcode-dev`
   - URL: `http://192.168.1.226:5678/webhook/ballcode-dev`

3. **Unity Build:**
   - Webhook path: `unity-build`
   - URL: `http://192.168.1.226:5678/webhook/unity-build`

**To check:**
- Open workflow in n8n
- Click on webhook trigger node
- Check "Path" field in Parameters tab

---

### Step 5: Test Again

**After importing and activating, test:**

```bash
# Test Screenshot Fix
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test error"}'

# Test Full Integration
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test AI analysis", "mode": "quick"}'

# Test Unity Build
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test build", "branch": "main"}'
```

**Expected:** JSON response (not 404 error)

---

## 🔍 TROUBLESHOOTING

### Still Getting 404?

**Check 1: Workflow is Active**
- Open workflow in n8n
- Toggle must be ON (blue/green)
- If OFF, turn it ON and save

**Check 2: Webhook Path Matches**
- Open webhook trigger node
- Check "Path" field
- Must match URL: `/webhook/[path]`

**Check 3: Workflow Imported**
- Go to "Workflows" list
- Should see all 3 workflows listed
- If missing, import again

**Check 4: n8n Running on Pi**
- Check Pi is running: `ping 192.168.1.226`
- Check n8n is running: Open `http://192.168.1.226:5678` in browser

---

## 📋 QUICK CHECKLIST

- [ ] Pi n8n accessible at `http://192.168.1.226:5678`
- [ ] All 3 workflows imported
- [ ] All 3 workflows activated (toggle ON)
- [ ] Webhook paths match test URLs
- [ ] No red error messages in workflows
- [ ] Test commands return JSON (not 404)

---

## 🎯 WORKFLOW NAMES TO LOOK FOR

**In Pi n8n "Workflows" list, you should see:**

1. **"Screenshot-to-Fix Automation - Visual Debugging & Auto-Repair"**
   - Webhook: `screenshot-fix`

2. **"BallCODE Full Integration - AI Analysis (Simplified)"**
   - Webhook: `ballcode-dev`

3. **"Unity Build Orchestrator"** (or similar name)
   - Webhook: `unity-build`

---

## 💡 PRO TIP

**If workflows are already imported but not activated:**

1. Go to "Workflows" list
2. Look for workflows with toggle OFF (gray)
3. Click toggle to turn ON
4. Save each workflow

**Much faster than re-importing!**

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Step-by-Step Fix Guide



