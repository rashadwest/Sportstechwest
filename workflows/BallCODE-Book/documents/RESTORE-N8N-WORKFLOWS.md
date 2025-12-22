# 🔄 Restore n8n Workflows After Container Recreation

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 16, 2025  
**Issue:** Container was recreated without volumes, workflows and credentials were lost  
**Solution:** Import workflows from JSON files and reconfigure credentials

---

## 🎯 QUICK RESTORATION STEPS

### Step 1: Set Up Owner Account

1. Open n8n: `http://192.168.1.226:5678`
2. Create your owner account (first time setup)
3. Complete the setup wizard

### Step 2: Import Workflows

**Available workflow files in repo:**

1. **Unity Build Orchestrator:**
   - `n8n-unity-build-orchestrator-13NODES-MAC-GUARDED-IMPORTABLE-IMPORTABLE.json`
   - This is the fixed, importable version

2. **BallCODE Full Integration:**
   - `n8n-ballcode-full-integration-workflow-SIMPLIFIED.json`

3. **Screenshot-to-Fix:**
   - `n8n-screenshot-to-fix-workflow.json`

**How to import:**
1. In n8n UI, click **"Workflows"** in left sidebar
2. Click **"Import from File"** button (top right)
3. Select the JSON file
4. Click **"Import"**
5. Repeat for each workflow

### Step 3: Configure Credentials

**Required credentials:**

1. **OpenAI API:**
   - Settings → Credentials → Add Credential
   - Type: OpenAI API
   - API Key: [Your OpenAI API key]

2. **GitHub (for GitHub Actions):**
   - Settings → Credentials → Add Credential
   - Type: GitHub API
   - Personal Access Token: [Your GitHub token with repo and workflow permissions]

3. **HTTP Header Auth (for GitHub Actions webhook):**
   - Settings → Credentials → Add Credential
   - Type: HTTP Header Auth
   - Name: `Authorization`
   - Value: `Bearer [Your GitHub token]`

### Step 4: Activate Workflows

1. Open each workflow
2. Click the **"Active"** toggle (top-right) to turn it ON
3. Verify webhook URLs show `192.168.1.226:5678` (not localhost)

---

## 📋 WORKFLOW IMPORT ORDER

**Recommended order:**

1. **Unity Build Orchestrator** (most important)
2. **BallCODE Full Integration**
3. **Screenshot-to-Fix**

---

## 🔍 VERIFY AFTER IMPORT

**Check each workflow:**

1. ✅ Workflow imported successfully
2. ✅ All nodes are connected
3. ✅ Credentials are configured
4. ✅ Environment variables are accessible (check Code nodes)
5. ✅ Webhook URLs show Pi IP (not localhost)
6. ✅ Workflow is activated

---

## 🚨 PREVENT FUTURE DATA LOSS

**The fixed script (`set-all-pi-n8n-env-vars-FIXED.sh`) now:**
- ✅ Uses volume mount: `-v /home/rw3hampton/.n8n:/home/node/.n8n`
- ✅ Preserves all n8n data across container restarts
- ✅ All workflows, credentials, and settings persist

**Always use the FIXED version for future updates!**

---

## 📝 QUICK REFERENCE

**n8n URL:** `http://192.168.1.226:5678`  
**Data Directory:** `/home/rw3hampton/.n8n` (on Pi)  
**Workflow Files:** In repo root (`n8n-*.json`)

---

**Version:** 1.0  
**Created:** December 16, 2025  
**Status:** 🔄 Restoration Guide


