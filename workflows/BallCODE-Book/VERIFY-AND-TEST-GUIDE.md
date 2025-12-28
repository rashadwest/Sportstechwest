# Verify & Test Guide

**Date:** December 18, 2025  
**Purpose:** What to do for "Verify" and "Test" steps

---

## ✅ STEP 4: VERIFY (2 minutes)

### **What It Does:**

The verification script checks:
- ✅ n8n is running and accessible
- ✅ Webhooks are accessible (Garvis, Unity Build)
- ✅ Environment variables are set (or credentials exist)
- ✅ GitHub Actions workflow file exists
- ✅ Overall integration readiness

### **How to Run:**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/verify-garvis-unity-integration.py
```

### **What You'll See:**

**If everything is ready:**
```
✅ n8n is running
✅ Garvis Orchestrator webhook: Webhook accessible
✅ Unity Build Orchestrator webhook: Webhook accessible
✅ All required environment variables are set
✅ GitHub Actions workflow file exists

🎉 All checks passed! Integration is ready!
```

**If something is missing:**
```
❌ Missing required environment variables: GITHUB_PAT, NETLIFY_AUTH_TOKEN
⚠️  Some checks failed. Please fix the issues above.
```

### **What to Do:**

- **If all pass:** Proceed to test! ✅
- **If checks fail:** Fix the issues shown, then re-run verification

---

## 🧪 STEP 5: TEST (5 minutes)

### **What It Does:**

Tests the **full integration flow:**
1. Garvis command triggers request
2. Garvis Orchestrator receives request
3. Routes to Unity Build Orchestrator
4. Unity Build Orchestrator triggers GitHub Actions
5. GitHub Actions builds Unity
6. Deploys to Netlify

### **How to Run:**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/garvis-command.py \
  --one-thing "Test Unity build integration" \
  --tasks "Build Unity game"
```

### **What Happens:**

1. **Garvis creates a job:**
   - Job ID: `garvis-xxxxx`
   - Status: `pending`

2. **Garvis routes to n8n:**
   - Calls `/webhook/garvis`
   - Garvis Orchestrator receives request
   - Routes to Unity Build Orchestrator

3. **Unity Build Orchestrator:**
   - Triggers GitHub Actions
   - Monitors build status
   - Deploys to Netlify

4. **You see:**
   - Job status updates
   - Build progress
   - Final result

### **What to Monitor:**

**In Terminal:**
- Job ID created
- Status updates
- Success/failure message

**In n8n UI:**
- Go to: http://192.168.1.226:5678
- Click **Executions** (left sidebar)
- See workflow executions running

**In GitHub:**
- Go to: https://github.com/rashadwest/BTEBallCODE/actions
- See workflow run triggered
- Watch build progress

**In Netlify:**
- Go to: https://app.netlify.com
- See new deployment triggered
- Watch deployment progress

### **Expected Result:**

**Success:**
```
✅ Job completed successfully
✅ Unity build triggered
✅ GitHub Actions workflow running
✅ Netlify deployment in progress
```

**Failure:**
```
❌ Job failed: [error message]
```

### **If Test Fails:**

1. **Check n8n executions:**
   - See which node failed
   - Check error message

2. **Check verification:**
   - Re-run verification script
   - Fix any missing components

3. **Check credentials:**
   - Verify credentials are set correctly
   - Check tokens are valid

4. **Check GitHub Actions:**
   - Verify workflow file exists
   - Check if build is running

---

## 📊 QUICK REFERENCE

**Verify:**
```bash
python scripts/verify-garvis-unity-integration.py
```
**Checks:** Everything is set up correctly

**Test:**
```bash
python scripts/garvis-command.py \
  --one-thing "Test Unity build integration" \
  --tasks "Build Unity game"
```
**Tests:** Full integration flow works end-to-end

---

## ✅ SUCCESS CRITERIA

**Verification passes when:**
- All 5 checks show ✅
- No missing variables/credentials
- Webhooks accessible

**Test passes when:**
- Job completes successfully
- GitHub Actions workflow runs
- Netlify deployment succeeds
- Game is live on Netlify

---

**Run verify first, then test!** 🚀


