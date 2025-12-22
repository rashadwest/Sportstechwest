# 📥 Import & Activate Phase 2 Workflows - Step by Step

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Purpose:** Complete guide to import and activate Phase 2 workflows in n8n

---

## 🎯 QUICK FIX FOR YOUR ISSUE

You're getting `404 - webhook not registered` because:
1. ✅ Workflows are created (we just made them)
2. ❌ Workflows are NOT imported to n8n yet
3. ❌ Workflows are NOT activated

**Solution:** Import and activate the workflows first!

---

## 📋 STEP-BY-STEP: IMPORT & ACTIVATE

### Step 1: Navigate to Project Directory

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
```

### Step 2: Source Environment

```bash
source .n8n-env
# Or if .n8n-env doesn't exist:
export N8N_URL="http://localhost:5678"
```

### Step 3: Import Workflows to n8n

**Option A: Via n8n UI (Easiest - Recommended)**

1. Open n8n in browser: `http://localhost:5678`
2. Click **"Workflows"** in left sidebar
3. Click **"Import from File"** button (top right)
4. Select each workflow file:
   - `n8n-book-content-update-workflow.json`
   - `n8n-curriculum-sync-workflow.json`
   - `n8n-game-exercise-integration-workflow.json`
5. Click **"Import"** for each

**Option B: Via API (Terminal)**

```bash
# Make sure you're in project directory
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

# Source environment
source .n8n-env 2>/dev/null || export N8N_URL="http://localhost:5678"

# Import Book Content Update Workflow
curl -X POST "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @n8n-book-content-update-workflow.json

# Import Curriculum Sync Workflow
curl -X POST "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @n8n-curriculum-sync-workflow.json

# Import Game Exercise Integration Workflow
curl -X POST "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @n8n-game-exercise-integration-workflow.json
```

### Step 4: Activate Workflows

**Via n8n UI:**
1. Open each workflow in n8n
2. Toggle the **"Inactive"** switch to **"Active"** (top right)
3. The switch should turn green/blue when active

**Via API:**
```bash
# Get workflow IDs first
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  jq '.[] | select(.name | contains("BallCODE")) | {id, name}'

# Activate each workflow (replace WORKFLOW_ID with actual ID)
curl -X POST "$N8N_URL/api/v1/workflows/WORKFLOW_ID/activate" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"
```

### Step 5: Verify Workflows Are Active

```bash
# List all workflows and check if they're active
curl -X GET "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  jq '.[] | select(.name | contains("BallCODE")) | {id, name, active}'
```

---

## ✅ NOW EXECUTE WORKFLOWS

Once workflows are imported and activated, use these commands:

```bash
# Make sure you're in project directory
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

# Source environment
source .n8n-env 2>/dev/null || export N8N_URL="http://localhost:5678"

# Execute Book Content Update
curl -X POST "$N8N_URL/webhook/book-content-update" \
  -H "Content-Type: application/json" \
  -d '{"bookId": 1, "content": {"title": "Test Book"}, "updateType": "modify"}'

# Execute Curriculum Sync
curl -X POST "$N8N_URL/webhook/curriculum-sync" \
  -H "Content-Type: application/json" \
  -d '{"changeType": "modify"}'

# Execute Game Exercise Integration
curl -X POST "$N8N_URL/webhook/game-exercise-integration" \
  -H "Content-Type: application/json" \
  -d '{"exerciseType": "new", "exerciseData": {"exerciseId": "test", "bookId": 1}}'
```

---

## 🔍 TROUBLESHOOTING

### Issue: "webhook not registered"

**Cause:** Workflow not imported or not active

**Fix:**
1. Check if workflow exists in n8n UI
2. Check if workflow is active (toggle switch)
3. If not imported, import it first
4. If imported but inactive, activate it

### Issue: "$N8N_URL not set"

**Cause:** Not in project directory or `.n8n-env` not sourced

**Fix:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env 2>/dev/null || export N8N_URL="http://localhost:5678"
```

### Issue: "No host part in URL"

**Cause:** `$N8N_URL` is empty

**Fix:**
```bash
# Check if N8N_URL is set
echo $N8N_URL

# If empty, set it
export N8N_URL="http://localhost:5678"

# Or source environment
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
source .n8n-env
```

---

## 📝 QUICK CHECKLIST

- [ ] Navigate to project directory
- [ ] Source `.n8n-env` or set `N8N_URL`
- [ ] Import workflows to n8n (via UI or API)
- [ ] Activate workflows (toggle switch in UI)
- [ ] Verify workflows are active
- [ ] Test webhook endpoints

---

## 🚀 ONE-LINER SETUP

```bash
# Complete setup in one go
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book && \
source .n8n-env 2>/dev/null || export N8N_URL="http://localhost:5678" && \
echo "✅ Environment ready. Now import workflows via n8n UI or API"
```

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Ready to Use


