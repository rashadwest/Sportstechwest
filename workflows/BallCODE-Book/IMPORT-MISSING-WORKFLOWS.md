# 🚀 Import Missing n8n Workflows - Quick Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Status:** 3 workflows working, 3 need import  
**Time:** 5 minutes

---

## ✅ CURRENT STATUS

**Working (HTTP 200):**
- ✅ Unity Build Orchestrator
- ✅ Full Integration Workflow  
- ✅ Screenshot to Fix Workflow

**Need Import (404):**
- ⚠️ Book Content Update
- ⚠️ Curriculum Sync
- ⚠️ Game Exercise Integration

---

## 📋 QUICK IMPORT STEPS

### Step 1: Open n8n UI
```
http://192.168.1.226:5678
```

### Step 2: Import Each Workflow

For each workflow below:
1. Click **Workflows** (top navigation)
2. Click **Import from File** button
3. Select the JSON file
4. Click **Import**
5. **Activate** the workflow (toggle switch)

---

## 📁 FILES TO IMPORT

### 1. Book Content Update Workflow
**File:** `n8n-book-content-update-workflow.json`  
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/`  
**Webhook:** `/webhook/book-content-update`

**After Import:**
- ✅ Verify webhook path is `/webhook/book-content-update`
- ✅ Activate workflow
- ✅ Test: `curl -X POST http://192.168.1.226:5678/webhook/book-content-update -H "Content-Type: application/json" -d '{"bookId": 1, "content": {"title": "Test"}}'`

---

### 2. Curriculum Sync Workflow
**File:** `n8n-curriculum-sync-workflow.json`  
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/`  
**Webhook:** `/webhook/curriculum-sync`

**After Import:**
- ✅ Verify webhook path is `/webhook/curriculum-sync`
- ✅ Activate workflow
- ✅ Test: `curl -X POST http://192.168.1.226:5678/webhook/curriculum-sync -H "Content-Type: application/json" -d '{"changeType": "newObjective"}'`

---

### 3. Game Exercise Integration Workflow
**File:** `n8n-game-exercise-integration-workflow.json`  
**Location:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/`  
**Webhook:** `/webhook/game-exercise-integration`

**Note:** ✅ This file was recreated and is ready to import!

**After Import:**
- ✅ Verify webhook path is `/webhook/game-exercise-integration`
- ✅ Activate workflow
- ✅ Test: `curl -X POST http://192.168.1.226:5678/webhook/game-exercise-integration -H "Content-Type: application/json" -d '{"exerciseType": "new", "exerciseData": {"exerciseId": "test-1"}}'`

---

## ⚙️ CONFIGURE AFTER IMPORT

### Environment Variables (if not already set)
In n8n UI → Settings → Environment Variables:
```
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

### Credentials (if not already set)
In n8n UI → Settings → Credentials:
- **OpenAI API** - Name: `openai-credentials`
  - Required by: Book Content Update, Curriculum Sync, Game Exercise Integration

---

## 🧪 VERIFY AFTER IMPORT

Run the test script again:
```bash
./scripts/test-all-n8n-workflows.sh
```

**Expected Result:**
- All 6 workflows should show ✅ (HTTP 200)
- No more 404 errors

---

## 🐛 TROUBLESHOOTING

### If Workflow Shows Blank After Import
1. **Try the cleaned version** (if available)
2. **Clear browser cache** and refresh
3. **Try incognito/private window**
4. **Delete and re-import**

See `N8N-BLANK-WORKFLOW-FIX.md` for detailed solutions.

### If Webhook Still Returns 404
1. **Check workflow is activated** (toggle switch ON)
2. **Verify webhook path** in workflow settings
3. **Check n8n logs** for errors
4. **Restart n8n** if needed

---

## ✅ CHECKLIST

- [ ] Import Book Content Update workflow
- [ ] Import Curriculum Sync workflow
- [ ] Import Game Exercise Integration workflow
- [ ] Activate all 3 workflows
- [ ] Verify environment variable `WORKFLOW_PATH` is set
- [ ] Verify `openai-credentials` credential exists
- [ ] Run test script: `./scripts/test-all-n8n-workflows.sh`
- [ ] All 6 workflows should return HTTP 200

---

**Version:** 1.0  
**Created:** January 2025  
**Status:** Ready to Import

