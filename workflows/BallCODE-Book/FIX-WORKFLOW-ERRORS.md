# 🔧 Fix Workflow Errors - Step by Step Guide

**Date:** December 17, 2025  
**Goal:** Get all workflows working 100%

---

## 🎯 Step 1: Test All Workflows

**Run the test script:**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 scripts/test-all-n8n-workflows.py
```

**This will:**
- Test all 3 active workflows
- Show which ones work
- Show which ones fail
- Give you error details

---

## 🔍 Step 2: Check n8n Executions for Errors

**After running tests:**

1. **Open n8n:** `http://192.168.1.226:5678`
2. **Click "Executions" tab**
3. **Find the most recent execution** (should be from just now)
4. **Click on it** to see details
5. **Look for RED nodes** - these are the failures

**For each red node:**
- Click on it
- Read the error message
- Note which node failed
- Copy the error text

---

## 🔧 Step 3: Fix Common Errors

### Error Type 1: Environment Variables Missing

**Error Message:**
- "environment variable is not set"
- "UNITY_REPO_URL is not defined"
- "process.env.GITHUB_REPO_OWNER is undefined"

**Fix:**

1. **Go to n8n Settings:**
   - Click "Settings" (gear icon) in left sidebar
   - Click "Environment Variables"

2. **Add these variables:**
   ```
   GITHUB_REPO_OWNER=rashadwest
   GITHUB_REPO_NAME=BTEBallCODE
   GITHUB_WORKFLOW_FILE=unity-webgl-build.yml
   NETLIFY_SITE_ID=your-site-id
   NETLIFY_SITE_NAME=ballcode-game
   N8N_INSTANCE_ROLE=prod
   ```

3. **Save and restart n8n:**
   ```bash
   # SSH to Pi
   ssh pi@192.168.1.226
   
   # Restart n8n
   sudo systemctl restart n8n
   ```

4. **Re-test the workflow**

---

### Error Type 2: API Credentials Missing

**Error Message:**
- "Credential not found"
- "OpenAI API key missing"
- "401 Unauthorized"
- "Authentication failed"

**Fix:**

1. **Go to n8n Credentials:**
   - Click "Credentials" in left sidebar
   - Click "Add Credential"

2. **Add OpenAI Credential:**
   - Search for "OpenAI"
   - Select "OpenAI API"
   - Name: `OpenAI API`
   - API Key: Your OpenAI API key
   - Save

3. **Add GitHub Credential (if needed):**
   - Search for "HTTP Header Auth"
   - Name: `github-actions-token`
   - Header Name: `Authorization`
   - Header Value: `Bearer YOUR_GITHUB_TOKEN`
   - Save

4. **Add Netlify Credential (if needed):**
   - Search for "HTTP Header Auth"
   - Name: `netlify-api-token`
   - Header Name: `Authorization`
   - Header Value: `Bearer YOUR_NETLIFY_TOKEN`
   - Save

5. **Assign credentials to workflows:**
   - Open each workflow
   - Click on nodes that need credentials
   - Select the credential from dropdown
   - Save workflow

6. **Re-test the workflow**

---

### Error Type 3: Workflow Node Configuration Error

**Error Message:**
- "Cannot read property of undefined"
- "TypeError"
- "ReferenceError"
- "Node execution failed"

**Fix:**

1. **Open the workflow in n8n**

2. **Click on the RED node** (the one that failed)

3. **Check the node configuration:**
   - Look for undefined variables
   - Check if expressions are correct
   - Verify node parameters

4. **For Code nodes:**
   - Check for typos
   - Add null checks
   - Fix variable references

5. **Example fix for Code node:**
   ```javascript
   // Before (might fail):
   const value = $json.someProperty.nested;
   
   // After (safe):
   const value = $json?.someProperty?.nested || null;
   ```

6. **Save and re-test**

---

### Error Type 4: Webhook Not Registered

**Error Message:**
- "404 Not Found"
- "Webhook not found"
- "Route not found"

**Fix:**

1. **Check workflow is active:**
   - Open workflow in n8n
   - Toggle "Active" switch ON (top right)
   - Should be green/blue

2. **Check webhook path:**
   - Click on "Webhook Trigger" node
   - Note the path (e.g., `/webhook/unity-build`)
   - Verify it matches what you're calling

3. **Test webhook directly:**
   ```bash
   curl -X POST http://192.168.1.226:5678/webhook/unity-build \
     -H "Content-Type: application/json" \
     -d '{"request": "test"}'
   ```

4. **If still 404:**
   - Deactivate workflow
   - Save
   - Activate workflow
   - Save
   - Re-test

---

### Error Type 5: Network/Timeout Error

**Error Message:**
- "Connection timeout"
- "ECONNREFUSED"
- "Request timeout"

**Fix:**

1. **Check network connectivity:**
   ```bash
   # Test connectivity
   ping 192.168.1.226
   curl http://192.168.1.226:5678/healthz
   ```

2. **Increase timeout in HTTP Request nodes:**
   - Open workflow
   - Click on HTTP Request node
   - Find "Timeout" setting
   - Increase to 60 seconds or more
   - Save

3. **Check if external APIs are accessible:**
   - Test OpenAI API
   - Test GitHub API
   - Test Netlify API

---

## 🧪 Step 4: Test Each Workflow Individually

### Test Unity Build Orchestrator:

```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Test build",
    "branch": "main"
  }'
```

**Expected:** Should return JSON response, not 404 or error

### Test Full Integration:

```bash
curl -X POST http://192.168.1.226:5678/webhook/full-integration \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Test integration"
  }'
```

**Expected:** Should return JSON response

### Test Screenshot-to-Fix:

```bash
curl -X POST http://192.168.1.226:5678/webhook/screenshot-fix \
  -H "Content-Type: application/json" \
  -d '{
    "screenshotUrl": "https://example.com/test.png",
    "context": "Test"
  }'
```

**Expected:** Should return JSON response

---

## 📋 Step 5: Verify Fixes

**After fixing errors:**

1. **Re-run test script:**
   ```bash
   python3 scripts/test-all-n8n-workflows.py
   ```

2. **Check n8n Executions:**
   - Go to Executions tab
   - Verify new executions are successful
   - No red nodes

3. **Monitor for 24 hours:**
   - Check executions daily
   - Ensure success rate stays high
   - Fix any new errors quickly

---

## 🎯 Quick Fix Checklist

**For Unity Build Orchestrator (the failing one):**

- [ ] Check environment variables are set
- [ ] Check GitHub credential is configured
- [ ] Check Netlify credential is configured
- [ ] Verify workflow is active
- [ ] Test webhook endpoint
- [ ] Check execution logs for specific error
- [ ] Fix the error
- [ ] Re-test

---

## 💡 Pro Tips

1. **Start with environment variables** - Most common issue
2. **Check credentials next** - Second most common
3. **Look at execution details** - Shows exact error
4. **Test one workflow at a time** - Easier to debug
5. **Fix and re-test immediately** - Verify fix works

---

## 🚀 Expected Result

**After fixes:**
- ✅ All 3 workflows test successfully
- ✅ No errors in n8n Executions
- ✅ 100% success rate
- ✅ Ready to activate inactive workflows
- ✅ Ready to import Garvis workflows

---

**Let's start by running the test script and seeing what errors we get!** 🧪


