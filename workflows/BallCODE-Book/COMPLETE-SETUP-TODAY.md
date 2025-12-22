# 🚀 Complete n8n Setup - Finish Today

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Goal:** Get ALL workflows working in production TODAY  
**Time:** 1-2 hours  
**Status:** 🔴 CRITICAL

---

## 🎯 WHAT WE NEED TO DO

1. ✅ Fix blank orchestrator workflow (use cleaned version)
2. ✅ Verify orchestrator actually triggers builds
3. ✅ Verify screenshot workflow actually processes images
4. ✅ Import 3 missing workflows
5. ✅ Test everything end-to-end

---

## 📋 STEP 1: Fix Orchestrator Workflow (15 minutes)

### A. Delete Blank Workflow
1. Open n8n: `http://192.168.1.226:5678`
2. Go to **Workflows**
3. Find: "AIMCODE (Demis) - Unity Build Orchestrator"
4. **If it shows blank:** Click **Delete** (trash icon)
5. Confirm deletion

### B. Import Cleaned Version
1. Click **Import from File**
2. Select: `n8n-unity-build-orchestrator-CLEANED-FOR-IMPORT.json`
3. Click **Import**
4. **Verify:** All 13 nodes are visible (not blank)

### C. Activate Workflow
1. Click the **Active** toggle (top-right)
2. Toggle should be **ON** (green/blue)

### D. Verify Configuration
**Environment Variables** (Settings → Environment Variables):
- [ ] `GITHUB_REPO_OWNER` = `rashadwest`
- [ ] `GITHUB_REPO_NAME` = `BTEBallCODE` (or your repo)
- [ ] `GITHUB_WORKFLOW_FILE` = `unity-webgl-build.yml`
- [ ] `NETLIFY_SITE_ID` = Your Netlify site ID
- [ ] `NETLIFY_SITE_NAME` = `ballcode-game`
- [ ] `N8N_INSTANCE_ROLE` = `prod`

**Credentials** (Settings → Credentials):
- [ ] `github-actions-token` - HTTP Header Auth with GitHub token
- [ ] `netlify-api-token` - HTTP Header Auth with Netlify token

### E. Test Orchestrator Actually Works
```bash
# Test webhook
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{"request": "Production test", "branch": "main"}'
```

**Then verify:**
1. Go to n8n → **Executions**
2. Find latest execution
3. Click on it
4. **Verify these nodes executed:**
   - ✅ "Dispatch GitHub Build" - Should show success
   - ✅ "Check Latest GitHub Run" - Should show GitHub data
   - ✅ "Check Latest Netlify Deploy" - Should show Netlify data
5. **Check GitHub Actions:**
   - Go to your GitHub repo → Actions
   - Verify a new workflow run was triggered
6. **Check response contains:**
   - `github` object with status
   - `netlify` object with state
   - `message` with build info

**If any step fails, see troubleshooting below.**

---

## 📋 STEP 2: Verify Screenshot Workflow (15 minutes)

### A. Verify Workflow is Visible
1. Open Screenshot to Fix workflow in n8n
2. **If blank:** Delete and re-import `n8n-screenshot-to-fix-workflow.json`

### B. Verify Configuration
**Environment Variables:**
- [ ] `WORKFLOW_PATH` = `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`
- [ ] `GITHUB_REPO_OWNER` = `rashadwest`
- [ ] `GITHUB_REPO_NAME` = `BTEBallCODE`
- [ ] `GITHUB_WORKFLOW_FILE` = `unity-webgl-build.yml`
- [ ] `NETLIFY_SITE_NAME` = `ballcode-game`

**Credentials:**
- [ ] `openai-credentials` - OpenAI API key (for GPT-4 Vision)

**Python Script:**
- [ ] File exists: `screenshot_fix_processor.py`
- [ ] Is executable: `chmod +x screenshot_fix_processor.py`

### C. Test Screenshot Workflow Actually Works
```bash
# Test with placeholder image
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://via.placeholder.com/800x600.png?text=Test+Error",
    "context": "Production test - verifying screenshot analysis"
  }'
```

**Then verify:**
1. Go to n8n → **Executions**
2. Find latest execution
3. Click on it
4. **Verify these nodes executed:**
   - ✅ "Vision Analysis (GPT-4 Vision)" - Should show OpenAI API call
   - ✅ "Parse Diagnosis" - Should show diagnosis data
   - ✅ "Generate Fix" - Should show fix generation (if canAutoFix=true)
5. **Check response contains:**
   - `diagnosis` object with `errorType`, `errorMessage`
   - `requestId` for tracking
   - `fix` object (if auto-fix was possible)

**If Vision Analysis fails:**
- Check OpenAI API key is valid
- Check you have GPT-4 Vision access
- Check API usage limits

---

## 📋 STEP 3: Import Missing Workflows (20 minutes)

### A. Book Content Update
1. Import: `n8n-book-content-update-workflow.json`
2. Activate workflow
3. Set `WORKFLOW_PATH` environment variable
4. Set `openai-credentials` credential
5. Test:
```bash
curl -X POST http://192.168.1.226:5678/webhook/book-content-update \
  -H "Content-Type: application/json" \
  -d '{
    "bookId": 1,
    "content": {
      "title": "Test Book",
      "slug": "test-book",
      "concepts": {"python": "Sequences"},
      "basketball": {"skill": "Pound Dribble"},
      "curriculum": {"gradeLevels": ["3-5"]}
    },
    "updateType": "modify"
  }'
```

### B. Curriculum Sync
1. Import: `n8n-curriculum-sync-workflow.json`
2. Activate workflow
3. Set `WORKFLOW_PATH` environment variable
4. Set `openai-credentials` credential
5. Test:
```bash
curl -X POST http://192.168.1.226:5678/webhook/curriculum-sync \
  -H "Content-Type: application/json" \
  -d '{
    "changeType": "newObjective",
    "learningObjective": {
      "objective": "Test objective",
      "gradeLevels": ["3-5"]
    }
  }'
```

### C. Game Exercise Integration
1. Import: `n8n-game-exercise-integration-workflow.json`
2. Activate workflow
3. Set `WORKFLOW_PATH` environment variable
4. Set `openai-credentials` credential
5. Test:
```bash
curl -X POST http://192.168.1.226:5678/webhook/game-exercise-integration \
  -H "Content-Type: application/json" \
  -d '{
    "exerciseType": "new",
    "exerciseData": {
      "exerciseId": "test-exercise-1",
      "bookId": 1,
      "difficulty": "beginner",
      "concept": "Sequences"
    }
  }'
```

---

## 📋 STEP 4: Complete Validation (30 minutes)

### A. Run Validation Script
```bash
./scripts/validate-workflows-complete.sh
```

### B. Manual Verification Checklist

**For Unity Build Orchestrator:**
- [ ] Webhook returns HTTP 200
- [ ] Response contains `github` object
- [ ] Response contains `netlify` object
- [ ] n8n execution shows all nodes executed
- [ ] GitHub Actions shows new workflow run
- [ ] Response has meaningful `message` field

**For Screenshot to Fix:**
- [ ] Webhook returns HTTP 200
- [ ] Response contains `diagnosis` object
- [ ] Response contains `errorType` and `errorMessage`
- [ ] n8n execution shows Vision Analysis executed
- [ ] OpenAI API was called (check usage)
- [ ] Diagnosis was generated

**For Full Integration:**
- [ ] Webhook returns HTTP 200
- [ ] Response contains `actionPlan` or `analysis`
- [ ] n8n execution shows AI analysis executed
- [ ] Response has meaningful data

**For Book Content Update:**
- [ ] Webhook returns HTTP 200
- [ ] Python script executed
- [ ] Response contains `completionReport`

**For Curriculum Sync:**
- [ ] Webhook returns HTTP 200
- [ ] Python script executed
- [ ] Response contains `verificationReport`

**For Game Exercise Integration:**
- [ ] Webhook returns HTTP 200
- [ ] Python script executed
- [ ] Response contains `integrationStatus`

### C. Run Final Test Suite
```bash
./scripts/test-all-n8n-workflows.sh
```

**Expected:** All 6 workflows return HTTP 200

---

## 🐛 TROUBLESHOOTING

### Issue: Orchestrator Shows Blank
**Solution:**
1. Use `n8n-unity-build-orchestrator-CLEANED-FOR-IMPORT.json`
2. Delete blank workflow
3. Clear browser cache (Ctrl+Shift+Delete)
4. Re-import cleaned version
5. See: `N8N-BLANK-WORKFLOW-FIX.md`

### Issue: Orchestrator Returns 200 But Doesn't Trigger Build
**Check:**
1. GitHub token has `repo` and `workflow` scopes
2. Environment variables are set correctly
3. GitHub repo name matches exactly
4. Workflow file name matches exactly
5. Check n8n execution logs for errors

**Fix:**
- Verify credentials in n8n UI
- Check GitHub token permissions
- Verify environment variables match your setup

### Issue: Screenshot Workflow Doesn't Analyze Images
**Check:**
1. OpenAI API key is valid
2. You have GPT-4 Vision access
3. API usage limits not exceeded
4. Image URL is accessible

**Fix:**
- Test OpenAI API key directly
- Check OpenAI account for Vision access
- Use a publicly accessible image URL

### Issue: Python Scripts Don't Execute
**Check:**
1. `WORKFLOW_PATH` environment variable is set
2. Scripts exist at that path
3. Scripts are executable: `chmod +x scripts/*.py`
4. Python 3 is available: `python3 --version`

**Fix:**
- Set `WORKFLOW_PATH` correctly
- Make scripts executable
- Test scripts manually: `python3 scripts/n8n-update-schema.py --help`

---

## ✅ SUCCESS CRITERIA

**You're done when:**
1. ✅ All 6 workflows imported and visible in n8n
2. ✅ All 6 workflows activated
3. ✅ All workflows return HTTP 200
4. ✅ Orchestrator actually triggers GitHub Actions
5. ✅ Screenshot workflow actually analyzes images
6. ✅ All environment variables set
7. ✅ All credentials configured
8. ✅ All Python scripts executable
9. ✅ All workflows tested end-to-end
10. ✅ No errors in n8n executions

---

## 📊 QUICK REFERENCE

**Files:**
- Orchestrator (cleaned): `n8n-unity-build-orchestrator-CLEANED-FOR-IMPORT.json`
- Screenshot Fix: `n8n-screenshot-to-fix-workflow.json`
- Book Update: `n8n-book-content-update-workflow.json`
- Curriculum Sync: `n8n-curriculum-sync-workflow.json`
- Game Exercise: `n8n-game-exercise-integration-workflow.json`

**Scripts:**
- Test all: `./scripts/test-all-n8n-workflows.sh`
- Validate: `./scripts/validate-workflows-complete.sh`

**n8n URL:** `http://192.168.1.226:5678`

---

**Version:** 1.0  
**Created:** January 2025  
**Status:** 🔴 Complete Today

