# ✅ Production-Ready Checklist - Complete n8n Setup

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** January 2025  
**Purpose:** Complete checklist to ensure ALL workflows work in production  
**Status:** 🔴 CRITICAL - Complete Today

---

## 🎯 GOAL

**Ensure ALL workflows are:**
1. ✅ Imported into n8n
2. ✅ Activated and working
3. ✅ Properly configured with all dependencies
4. ✅ Tested end-to-end
5. ✅ Production-ready

---

## 📋 WORKFLOW STATUS

### ✅ Working (HTTP 200)
- [x] Unity Build Orchestrator - Returns 200, but needs full validation
- [x] Full Integration Workflow - Returns 200, needs validation
- [x] Screenshot to Fix Workflow - Returns 200, needs validation

### ⚠️ Not Imported (404)
- [ ] Book Content Update Workflow
- [ ] Curriculum Sync Workflow
- [ ] Game Exercise Integration Workflow

---

## 🔧 STEP 1: Unity Build Orchestrator - Complete Setup

### A. Verify Workflow is Visible in n8n UI
- [ ] Open n8n: `http://192.168.1.226:5678`
- [ ] Go to Workflows
- [ ] Find: "AIMCODE (Demis) - Unity Build Orchestrator"
- [ ] **If blank/empty:** Use `n8n-unity-build-orchestrator-CLEANED-FOR-IMPORT.json`
- [ ] Delete blank workflow and re-import cleaned version

### B. Required Environment Variables
Set in n8n UI → Settings → Environment Variables:

- [ ] `GITHUB_REPO_OWNER` = `rashadwest`
- [ ] `GITHUB_REPO_NAME` = `BTEBallCODE` (or your actual repo)
- [ ] `GITHUB_WORKFLOW_FILE` = `unity-webgl-build.yml` (or your actual workflow file)
- [ ] `NETLIFY_SITE_ID` = Your Netlify site ID
- [ ] `NETLIFY_SITE_NAME` = `ballcode-game` (or your site name)
- [ ] `N8N_INSTANCE_ROLE` = `prod` (on Pi) or `dev` (on Mac)

### C. Required Credentials
Set in n8n UI → Settings → Credentials:

- [ ] **GitHub Actions Token**
  - Name: `github-actions-token`
  - Type: HTTP Header Auth
  - Header: `Authorization`
  - Value: `Bearer YOUR_GITHUB_PERSONAL_ACCESS_TOKEN`
  - Scope needed: `repo` (full control of private repositories)

- [ ] **Netlify API Token**
  - Name: `netlify-api-token`
  - Type: HTTP Header Auth
  - Header: `Authorization`
  - Value: `Bearer YOUR_NETLIFY_API_TOKEN`

### D. Verify Workflow Actually Works
- [ ] Test webhook: `curl -X POST http://192.168.1.226:5678/webhook/unity-build -H "Content-Type: application/json" -d '{"request": "Test", "branch": "main"}'`
- [ ] Check n8n Executions: Verify workflow ran
- [ ] Check GitHub Actions: Verify new workflow run was triggered
- [ ] Check Netlify: Verify deployment status was checked
- [ ] Verify response contains: `github`, `netlify`, `status`, `message`

---

## 🔧 STEP 2: Screenshot to Fix - Complete Setup

### A. Verify Workflow is Visible
- [ ] Open workflow in n8n UI
- [ ] Verify all nodes are visible (not blank)
- [ ] If blank, delete and re-import

### B. Required Environment Variables
- [ ] `WORKFLOW_PATH` = `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`
- [ ] `GITHUB_REPO_OWNER` = `rashadwest`
- [ ] `GITHUB_REPO_NAME` = `BTEBallCODE`
- [ ] `GITHUB_WORKFLOW_FILE` = `unity-webgl-build.yml`
- [ ] `NETLIFY_SITE_NAME` = `ballcode-game`
- [ ] `WEBHOOK_NOTIFICATION_URL` = (optional, for notifications)

### C. Required Credentials
- [ ] **OpenAI API Key**
  - Name: `openai-credentials`
  - Type: OpenAI API
  - Value: Your OpenAI API key
  - Model access: GPT-4, GPT-4 Vision

- [ ] **GitHub Actions Token** (same as Orchestrator)

### D. Verify Python Script Exists
- [ ] File exists: `screenshot_fix_processor.py`
- [ ] Script is executable: `chmod +x screenshot_fix_processor.py`
- [ ] Script has correct permissions

### E. Verify Workflow Actually Works
- [ ] Test with test screenshot: `curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix -H "Content-Type: application/json" -d '{"screenshotUrl": "https://via.placeholder.com/800x600.png?text=Test", "context": "Test error"}'`
- [ ] Check n8n Executions: Verify workflow ran
- [ ] Verify "Vision Analysis" node executed
- [ ] Verify OpenAI API was called (check API usage)
- [ ] Verify response contains: `diagnosis`, `errorType`, `fix` or `requestId`

---

## 🔧 STEP 3: Full Integration Workflow - Complete Setup

### A. Verify Workflow is Visible
- [ ] Open workflow in n8n UI
- [ ] Verify all nodes are visible

### B. Required Environment Variables
- [ ] `WORKFLOW_PATH` = `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`

### C. Required Credentials
- [ ] **OpenAI API Key** (same as Screenshot Fix)

### D. Verify Workflow Actually Works
- [ ] Test: `curl -X POST http://192.168.1.226:5678/webhook/ballcode-dev -H "Content-Type: application/json" -d '{"prompt": "Test", "mode": "quick"}'`
- [ ] Check n8n Executions
- [ ] Verify AI analysis node executed
- [ ] Verify response contains: `actionPlan`, `analysis`, `systemsAffected`

---

## 🔧 STEP 4: Import Missing Workflows

### Book Content Update
- [ ] Import: `n8n-book-content-update-workflow.json`
- [ ] Activate workflow
- [ ] Set `WORKFLOW_PATH` environment variable
- [ ] Set `openai-credentials` credential
- [ ] Test webhook
- [ ] Verify Python script executes: `scripts/n8n-update-schema.py`

### Curriculum Sync
- [ ] Import: `n8n-curriculum-sync-workflow.json`
- [ ] Activate workflow
- [ ] Set `WORKFLOW_PATH` environment variable
- [ ] Set `openai-credentials` credential
- [ ] Test webhook
- [ ] Verify Python script executes

### Game Exercise Integration
- [ ] Import: `n8n-game-exercise-integration-workflow.json`
- [ ] Activate workflow
- [ ] Set `WORKFLOW_PATH` environment variable
- [ ] Set `openai-credentials` credential
- [ ] Test webhook
- [ ] Verify Python script executes

---

## 🧪 STEP 5: Complete End-to-End Testing

### Run Validation Script
```bash
./scripts/validate-workflows-complete.sh
```

### Manual Verification
For each workflow:

1. **Unity Build Orchestrator:**
   - [ ] Trigger webhook
   - [ ] Check n8n execution log
   - [ ] Verify GitHub Actions was triggered
   - [ ] Verify Netlify status was checked
   - [ ] Verify response has meaningful data

2. **Screenshot to Fix:**
   - [ ] Upload test screenshot
   - [ ] Check n8n execution log
   - [ ] Verify Vision Analysis executed
   - [ ] Verify diagnosis was generated
   - [ ] Verify fix was attempted (if auto-fix enabled)

3. **Full Integration:**
   - [ ] Send test prompt
   - [ ] Check n8n execution log
   - [ ] Verify AI analysis executed
   - [ ] Verify action plan was generated

4. **Book Content Update:**
   - [ ] Send test book data
   - [ ] Verify Python script executed
   - [ ] Verify schema was updated
   - [ ] Verify website updates were generated

5. **Curriculum Sync:**
   - [ ] Send test curriculum change
   - [ ] Verify Python script executed
   - [ ] Verify all systems were updated

6. **Game Exercise Integration:**
   - [ ] Send test exercise data
   - [ ] Verify Python script executed
   - [ ] Verify exercise was integrated

---

## 📊 FINAL VERIFICATION

### Run Complete Test Suite
```bash
./scripts/test-all-n8n-workflows.sh
```

**Expected Result:**
- All 6 workflows return HTTP 200
- No 404 errors
- All responses contain expected data

### Check n8n Executions
- [ ] Go to: `http://192.168.1.226:5678/executions`
- [ ] Verify recent executions for all workflows
- [ ] Check for any errors
- [ ] Verify all nodes executed successfully

### Production Readiness
- [ ] All workflows imported
- [ ] All workflows activated
- [ ] All environment variables set
- [ ] All credentials configured
- [ ] All Python scripts exist and are executable
- [ ] All workflows tested end-to-end
- [ ] All workflows return meaningful responses

---

## 🚨 CRITICAL ISSUES TO FIX

### Issue 1: Blank Workflow Display
**Solution:**
1. Use cleaned workflow file: `n8n-unity-build-orchestrator-CLEANED-FOR-IMPORT.json`
2. Delete blank workflow from n8n
3. Clear browser cache
4. Re-import cleaned version
5. See: `N8N-BLANK-WORKFLOW-FIX.md`

### Issue 2: Workflow Returns 200 But Doesn't Actually Work
**Solution:**
1. Check n8n execution logs
2. Verify all nodes executed
3. Check for errors in node execution
4. Verify credentials are correct
5. Verify environment variables are set
6. Run: `./scripts/validate-workflows-complete.sh`

### Issue 3: Missing Dependencies
**Solution:**
1. Check all environment variables are set
2. Check all credentials are configured
3. Verify Python scripts exist
4. Verify scripts are executable
5. Check file paths are correct

---

## ✅ SUCCESS CRITERIA

**Workflow is production-ready when:**
1. ✅ Returns HTTP 200
2. ✅ All nodes execute successfully
3. ✅ Produces expected output
4. ✅ Integrates with external services (GitHub, Netlify, OpenAI)
5. ✅ No errors in execution logs
6. ✅ Handles errors gracefully

---

**Version:** 1.0  
**Created:** January 2025  
**Status:** 🔴 CRITICAL - Complete Today

