# 📥 Import All 6 Production Workflows to Pi n8n

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Source:** `ALL-N8N-WORKFLOWS-SUMMARY.md`  
**Purpose:** Complete guide to import all production workflows after container recreation

---

## 🎯 ALL 6 PRODUCTION WORKFLOWS

Based on your saved document (`ALL-N8N-WORKFLOWS-SUMMARY.md`), here are all 6 workflows to import:

### Phase 1 Workflows (Core Integration):

1. **Unity Build Orchestrator**
   - **File:** `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE-IMPORTABLE.json`
   - **Webhook:** `/webhook/unity-build`
   - **Purpose:** Automates Unity builds, GitHub Actions, Netlify deployment

2. **Full Integration Workflow**
   - **File:** `n8n-ballcode-full-integration-workflow-SIMPLIFIED.json`
   - **Webhook:** `/webhook/ballcode-dev`
   - **Purpose:** AI-driven development automation (updates all 4 systems)

3. **Screenshot to Fix Workflow**
   - **File:** `n8n-screenshot-to-fix-workflow.json`
   - **Webhook:** `/webhook/screenshot-fix`
   - **Purpose:** Visual debugging and auto-repair

### Phase 2 Workflows (Content Management):

4. **Book Content Update Workflow**
   - **File:** `n8n-book-content-update-workflow.json`
   - **Webhook:** `/webhook/book-content-update`
   - **Purpose:** Automate book content updates across all systems

5. **Curriculum Schema Sync Workflow**
   - **File:** `n8n-curriculum-sync-workflow.json`
   - **Webhook:** `/webhook/curriculum-sync`
   - **Purpose:** Keep all systems synchronized with curriculum changes

6. **Game Exercise Integration Workflow**
   - **File:** `n8n-game-exercise-integration-workflow.json`
   - **Webhook:** `/webhook/game-exercise-integration`
   - **Purpose:** Automatically integrate new game exercises with books and curriculum

---

## 📋 STEP-BY-STEP IMPORT PROCESS

### Step 1: Open Pi n8n

1. Go to: `http://192.168.1.226:5678`
2. Log in with your owner account

### Step 2: Import Each Workflow

**For each workflow file:**

1. Click **"Workflows"** in left sidebar
2. Click **"Import from File"** button (top right)
3. Navigate to and select the JSON file
4. Click **"Import"**
5. Repeat for all 6 workflows

**Import Order (Recommended):**

1. ✅ Unity Build Orchestrator (most critical)
2. ✅ Full Integration Workflow
3. ✅ Screenshot to Fix Workflow
4. ✅ Book Content Update Workflow
5. ✅ Curriculum Schema Sync Workflow
6. ✅ Game Exercise Integration Workflow

### Step 3: Configure Credentials

**After importing, configure these credentials:**

1. **OpenAI API:**
   - Settings → Credentials → Add Credential
   - Type: OpenAI API
   - API Key: [Your OpenAI API key]
   - **Used by:** Full Integration, Screenshot to Fix

2. **GitHub API:**
   - Settings → Credentials → Add Credential
   - Type: GitHub API
   - Personal Access Token: [Your GitHub token]
   - **Used by:** Unity Build Orchestrator, Screenshot to Fix

3. **HTTP Header Auth (GitHub Actions):**
   - Settings → Credentials → Add Credential
   - Type: HTTP Header Auth
   - Name: `Authorization`
   - Value: `Bearer [Your GitHub token]`
   - **Used by:** Unity Build Orchestrator, Screenshot to Fix

### Step 4: Activate All Workflows

**For each workflow:**

1. Open the workflow in n8n UI
2. Click the **"Active"** toggle (top-right)
3. Toggle should turn green/blue
4. Verify webhook URL shows `192.168.1.226:5678` (not localhost)

---

## ✅ VERIFICATION CHECKLIST

After importing all workflows, verify:

- [ ] All 6 workflows are imported
- [ ] All workflows are visible in "Workflows" list
- [ ] All credentials are configured
- [ ] All workflows are activated (green toggle)
- [ ] Webhook URLs show Pi IP (`192.168.1.226:5678`)
- [ ] Environment variables are accessible (check Code nodes)

---

## 🚀 QUICK IMPORT COMMANDS (Alternative)

If you prefer using the deployment script:

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./deploy-all-workflows-to-pi.sh
```

**Note:** The script may require an API key. Manual import via UI is more reliable.

---

## 📝 WORKFLOW FILES LOCATION

All workflow JSON files are in:
```
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/
```

**Files to import:**
- `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE-IMPORTABLE.json`
- `n8n-ballcode-full-integration-workflow-SIMPLIFIED.json`
- `n8n-screenshot-to-fix-workflow.json`
- `n8n-book-content-update-workflow.json`
- `n8n-curriculum-sync-workflow.json`
- `n8n-game-exercise-integration-workflow.json`

---

## 🆘 TROUBLESHOOTING

### Import Fails: "Could not find property option"

**Fix:** Use the `-IMPORTABLE-IMPORTABLE.json` version for Unity Build Orchestrator (already fixed)

### Credentials Not Working

**Fix:** 
1. Re-add credentials in Settings
2. Re-select credentials in workflow nodes
3. Save workflow

### Webhook URLs Show localhost

**Fix:** Environment variables are set correctly. The webhook will work with Pi IP even if UI shows localhost. Or refresh the page.

---

**Version:** 1.0  
**Created:** December 16, 2025  
**Status:** ✅ Complete Import Guide



