# What to Update Next

**Date:** December 18, 2025  
**Context:** After running robot-hardcode-env-vars.py

---

## ✅ WHAT THE ROBOT SCRIPT UPDATED

**The robot script modified:**
- ✅ `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`
  - Hardcoded GitHub repo values
  - Hardcoded Netlify Site ID (or placeholder)
  - Updated Code nodes to use hardcoded values
  - Updated HTTP Request URLs

**Created backup:**
- ✅ `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json.backup`

---

## 🔄 WHAT YOU NEED TO UPDATE

### **Step 1: Re-import Workflow in n8n (Required)**

**The modified workflow file needs to be imported into n8n:**

1. **Go to n8n UI:**
   - http://192.168.1.226:5678

2. **Delete/Deactivate Old Workflow:**
   - Find "Unity Build Orchestrator" workflow
   - Click **"..." menu** → **"Delete"** (or deactivate first)
   - Confirm deletion

3. **Import Modified Workflow:**
   - Click **"Workflows"** → **"Import from File"**
   - Select: `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE.json`
   - Click **"Import"**

4. **Activate Workflow:**
   - Toggle the **"Active"** switch (top right)
   - Workflow is now using hardcoded values

**Why:** The workflow file was modified locally, but n8n is using the old version. Re-importing loads the new version.

---

### **Step 2: Verify URL Expressions (Check After Import)**

**After importing, verify the expressions are set:**

1. **Open the workflow** in n8n UI
2. **Click on "Dispatch GitHub Build" node**
3. **Check URL field:**
   - Should show: `https://api.github.com/repos/rashadwest/BTEBallCODE/dispatches`
   - If it shows `{{ $env.GITHUB_REPO_OWNER }}`, the expression didn't import correctly
   - **Fix:** Re-enable Expression Mode and set the URL manually

4. **Click on "Check Latest Netlify Deploy" node**
5. **Check URL field:**
   - Should show your Site ID (or placeholder)
   - If empty, set it manually

**This is a known n8n quirk - expressions sometimes need manual re-enable after import.**

---

### **Step 3: Update Credentials (If Not Done)**

**Make sure credentials are set in n8n:**

1. **Go to:** Credentials (left sidebar)
2. **Check:**
   - `github-actions-token` exists and has value
   - `netlify-api-token` exists and has value
3. **If missing:** Create them (see credential guide)

---

## 📋 NOTHING TO UPDATE IN UNITY REPO

**You don't need to update anything in `~/BTEBallCODE`:**

- ✅ The Unity repo is fine as-is
- ✅ GitHub Actions workflow already exists (`.github/workflows/unity-webgl-build.yml`)
- ✅ The n8n workflow will trigger GitHub Actions, which builds Unity
- ✅ No changes needed to Unity code

**The integration works by:**
1. n8n triggers GitHub Actions (via API)
2. GitHub Actions builds Unity (already configured)
3. GitHub Actions deploys to Netlify (already configured)

**No Unity repo changes needed!**

---

## 🎯 SUMMARY: What to Update

**Update in n8n:**
1. ✅ Re-import the modified workflow file
2. ✅ Verify URL expressions are set correctly
3. ✅ Check credentials exist

**Don't update:**
- ❌ Unity repo (`~/BTEBallCODE`) - no changes needed
- ❌ GitHub Actions workflow - already configured
- ❌ GitHub repository - no changes needed

---

## ✅ NEXT STEPS

1. **Re-import workflow** in n8n (Step 1 above)
2. **Verify setup:**
   ```bash
   python scripts/verify-garvis-unity-integration.py
   ```
3. **Test integration:**
   ```bash
   python scripts/garvis-command.py \
     --one-thing "Test Unity build integration" \
     --tasks "Build Unity game"
   ```

---

**Main thing to update: Re-import the workflow in n8n!** ✅

