# ✅ Garvis Orchestrator - Import Instructions

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 23, 2025  
**Status:** ✅ Fixed JSON Ready - Import via UI

---

## ✅ What Was Fixed

**All 5 Route nodes fixed:**
- Changed from `array.contains` to `boolean.equals`
- `leftValue`: `{{ $json.systems.includes('book') }}` (returns boolean)
- `rightValue`: `true`
- `operator`: `boolean.equals`

**Fixed nodes:**
1. Route: Book System?
2. Route: Curriculum System?
3. Route: Game System?
4. Route: Website System?
5. Route: Sales System?

---

## 🚀 How to Import (UI Method - Recommended)

**The API import is being strict, so use UI import instead:**

### Step 1: Open n8n
1. Go to: `http://192.168.1.226:5678`
2. Log in if needed

### Step 2: Import Workflow
1. Click **"Workflows"** in left sidebar
2. Click **"Import from File"** button (top-right, or three dots menu → Import)
3. Select file: `n8n-garvis-orchestrator-workflow.json`
   - **Location options:**
     - Desktop: `~/Desktop/n8n-garvis-orchestrator-workflow-FIXED.json`
     - Project root: `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/n8n-garvis-orchestrator-workflow.json`
4. Click **"Import"**

### Step 3: Replace Existing (if prompted)
- If workflow already exists, choose **"Replace"** or **"Update"**
- This will update the existing workflow with the fixed version

### Step 4: Activate Workflow
1. Find: **"Garvis Orchestrator - BallCODE Fully Integrated System"**
2. Toggle **"Active"** to **ON** (top-right)
3. Click **"Save"**

### Step 5: Verify Fix
1. Click on **"Route: Book System?"** node
2. Check Parameters:
   - Left Value should show: `{{ $json.systems.includes('book') }}`
   - Right Value should show: `true`
   - Operator should be: `Boolean` → `Equals`
3. Repeat for other Route nodes

---

## 🧪 Test the Workflow

**Test webhook:**
```bash
curl -X POST "http://192.168.1.226:5678/webhook/garvis" \
  -H "Content-Type: application/json" \
  -d '{
    "one_thing": "Update book content",
    "tasks": ["book", "curriculum"],
    "context": "Testing fixed orchestrator"
  }'
```

**Expected:**
- Should route to Book and Curriculum systems
- No type validation errors
- Workflow executes successfully

---

## 📋 Alternative: API Import (If UI Doesn't Work)

**If you want to try API import:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/import-garvis-orchestrator.sh
```

**Note:** API import may still fail with "additional properties" error. UI import is more reliable.

---

## ✅ Status

- ✅ JSON file fixed in repository
- ✅ Import script created
- ✅ Ready for UI import
- ⚠️ API import may have issues (use UI instead)

---

**Next:** Import via UI, then test with webhook above.

