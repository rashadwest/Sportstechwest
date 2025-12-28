# 🔍 Debug Recent Workflow Failures

**Date:** December 17, 2025  
**Recent Failures:**
- Exec ID 74: Screenshot-to-Fix - Error (964ms) - 14:02:57
- Exec ID 73: Unity Build Orchestrator - Error (81ms) - 14:02:56

**Observation:** Webhooks return 200 OK, but workflows fail internally

---

## 🎯 The Problem

**What's happening:**
1. ✅ Webhook receives request (200 OK response)
2. ✅ Workflow starts executing
3. ❌ Workflow fails internally (very quickly - 81ms, 964ms)
4. ❌ Error shows in Executions tab

**This means:**
- Webhooks are working (registered correctly)
- Workflows are triggering
- But something is failing inside the workflow

---

## 🔍 Step 1: Check Execution Details

**For each failed execution:**

1. **Open n8n:** `http://192.168.1.226:5678`
2. **Click "Executions" tab**
3. **Click on Exec ID 73** (Unity Build Orchestrator - 14:02:56)
4. **Click on Exec ID 74** (Screenshot-to-Fix - 14:02:57)

**For each execution, identify:**
- Which node is RED (failed)
- What the error message says
- When in the workflow it failed

---

## 🔧 Common Causes for Fast Failures

### Cause 1: Environment Variables Missing

**Symptoms:**
- Fails in first Code node
- Error: "environment variable is not set"
- Very fast failure (<100ms)

**Check:**
- Exec 73 (Unity Build) - likely this one
- Look for "Get Git Variables" or first Code node

**Fix:**
1. Go to n8n Settings → Environment Variables
2. Add missing variables
3. Restart n8n

---

### Cause 2: Credentials Not Configured

**Symptoms:**
- Fails at OpenAI/API node
- Error: "Credential not found"
- Fails after webhook trigger

**Check:**
- Exec 74 (Screenshot-to-Fix) - likely this one
- Look for "Vision Analysis" or OpenAI node

**Fix:**
1. Go to n8n Credentials
2. Add OpenAI API credential
3. Assign to workflow nodes

---

### Cause 3: Node Configuration Error

**Symptoms:**
- Fails at specific node
- Error: "Cannot read property" or "TypeError"
- Node shows red in execution

**Check:**
- Look at which node is red
- Check node configuration
- Fix the code/configuration

---

### Cause 4: Workflow Validation Error

**Symptoms:**
- Fails immediately
- Error: "Workflow validation failed"
- Very fast failure

**Check:**
- Open workflow in editor
- Look for yellow/red warnings
- Fix configuration issues

---

## 🎯 Most Likely Issues

### For Unity Build Orchestrator (Exec 73):

**81ms failure = Startup/Validation issue**

**Most likely:**
1. **Environment variables missing** (90% probability)
   - `GITHUB_REPO_OWNER`
   - `GITHUB_REPO_NAME`
   - `NETLIFY_SITE_ID`
   - `N8N_INSTANCE_ROLE`

2. **First Code node error** (10% probability)
   - "Get Git Variables" node failing
   - Variable access error

**Action:**
- Check Exec 73 details
- Look at first node that failed
- Add missing environment variables

---

### For Screenshot-to-Fix (Exec 74):

**964ms failure = Slightly longer, likely API call**

**Most likely:**
1. **OpenAI credential missing** (80% probability)
   - "Vision Analysis" node needs credential
   - Credential not assigned

2. **Invalid API request** (20% probability)
   - Test payload format wrong
   - API endpoint issue

**Action:**
- Check Exec 74 details
- Look for OpenAI/Vision node
- Add/assign OpenAI credential

---

## 📋 Diagnostic Checklist

**For Exec 73 (Unity Build):**

- [ ] Open execution details
- [ ] Find red node
- [ ] Check error message
- [ ] If "environment variable" → Add env vars
- [ ] If "credential" → Add credentials
- [ ] If "TypeError" → Fix code node
- [ ] Re-test after fix

**For Exec 74 (Screenshot-to-Fix):**

- [ ] Open execution details
- [ ] Find red node
- [ ] Check error message
- [ ] If "credential not found" → Add OpenAI credential
- [ ] If "API error" → Check API key validity
- [ ] If "invalid request" → Fix payload format
- [ ] Re-test after fix

---

## 🔧 Quick Fixes

### Fix 1: Add Environment Variables

1. **Go to n8n Settings:**
   - Click gear icon (Settings)
   - Click "Environment Variables"

2. **Add these:**
   ```
   GITHUB_REPO_OWNER=rashadwest
   GITHUB_REPO_NAME=BTEBallCODE
   GITHUB_WORKFLOW_FILE=unity-webgl-build.yml
   NETLIFY_SITE_ID=your-site-id
   NETLIFY_SITE_NAME=ballcode-game
   N8N_INSTANCE_ROLE=prod
   ```

3. **Restart n8n:**
   ```bash
   ssh pi@192.168.1.226
   sudo systemctl restart n8n
   ```

### Fix 2: Add OpenAI Credential

1. **Go to n8n Credentials:**
   - Click "Credentials" in sidebar
   - Click "Add Credential"

2. **Add OpenAI:**
   - Search "OpenAI"
   - Select "OpenAI API"
   - Name: `OpenAI API`
   - API Key: Your key
   - Save

3. **Assign to workflow:**
   - Open Screenshot-to-Fix workflow
   - Click on "Vision Analysis" node
   - Select "OpenAI API" credential
   - Save workflow

---

## 🧪 After Fixes

**Re-test:**

```bash
python3 scripts/test-all-n8n-workflows.py
```

**Expected:**
- ✅ All workflows return 200
- ✅ No errors in Executions tab
- ✅ All executions show Success

---

## 💡 Next Steps

1. **Check Exec 73 and 74 details** (5 min)
   - See exact error messages
   - Identify which nodes failed

2. **Apply fixes** (10-30 min)
   - Based on error type
   - Add env vars or credentials

3. **Re-test** (2 min)
   - Run test script
   - Verify all work

4. **Monitor** (ongoing)
   - Check executions daily
   - Fix any new errors quickly

---

**The key is to check Exec 73 and 74 details to see the exact error messages. That will tell us exactly what to fix!** 🔍


