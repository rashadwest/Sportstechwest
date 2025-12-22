# 📥 Import Workflows to Pi n8n - UI Method (Fastest)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Status:** ✅ Ready - Use this method (no API key needed)

---

## 🚀 QUICK IMPORT (2 Minutes)

### Step 1: Open Pi n8n UI

Open in browser:
```
http://192.168.1.226:5678
```

### Step 2: Import Each Workflow

For each workflow file:

1. Click **"Workflows"** in left sidebar
2. Click **"Import from File"** button (top right)
3. Select workflow file from project directory:
   - `n8n-ballcode-full-integration-workflow.json`
   - `n8n-screenshot-to-fix-workflow.json`
   - `n8n-book-content-update-workflow.json`
   - `n8n-curriculum-sync-workflow.json`
   - `n8n-game-exercise-integration-workflow.json`
4. Click **"Import"**

**Repeat for all 5 workflows.**

### Step 3: Activate Workflows

For each imported workflow:

1. Open the workflow in n8n
2. Toggle **"Inactive"** → **"Active"** (top-right switch)
3. Switch should turn green/blue when active

---

## ✅ VERIFY IMPORT

After importing, you should see:

**In n8n Workflows list:**
- ✅ BallCODE Full Integration - AI Development Workflow
- ✅ Screenshot to Fix Workflow (if imported)
- ✅ BallCODE Book Content Update Workflow
- ✅ BallCODE Curriculum Schema Sync Workflow
- ✅ BallCODE Game Exercise Integration Workflow

---

## 🧪 TEST AFTER IMPORT

Once imported and activated, test with:

```bash
# Set Pi URL
export PI_N8N_URL="http://192.168.1.226:5678"

# Test Book Content Update
curl -X POST "${PI_N8N_URL}/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{"bookId": 1, "content": {"title": "Test"}, "updateType": "modify"}'

# Test Curriculum Sync
curl -X POST "${PI_N8N_URL}/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{"changeType": "modify"}'

# Test Game Exercise Integration
curl -X POST "${PI_N8N_URL}/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{"exerciseType": "new", "exerciseData": {"exerciseId": "test", "bookId": 1}}'
```

---

## 📋 WORKFLOW FILES LOCATION

All workflow files are in:
```
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/
```

Files to import:
1. `n8n-ballcode-full-integration-workflow.json`
2. `n8n-screenshot-to-fix-workflow.json`
3. `n8n-book-content-update-workflow.json`
4. `n8n-curriculum-sync-workflow.json`
5. `n8n-game-exercise-integration-workflow.json`

---

## 🎯 QUICK CHECKLIST

- [ ] Open Pi n8n UI: `http://192.168.1.226:5678`
- [ ] Import 5 workflow files
- [ ] Activate all workflows (toggle switch)
- [ ] Test webhook endpoints
- [ ] Verify workflows are working

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Use


