# Test Unity Build Workflow - Step by Step

**Date:** December 18, 2025  
**Purpose:** Test the Unity Build workflow after credential setup

---

## 🧪 TEST OPTIONS

### **Option 1: Quick Test Script (Recommended)**

**Run the test script:**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./test-unity-build-workflow.sh
```

**What it does:**
- Sends a POST request to the Unity Build webhook
- Shows the response
- Indicates success/failure

---

### **Option 2: Manual cURL Test**

**Test the webhook directly:**

```bash
curl -X POST http://192.168.1.226:5678/webhook/unity-build \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Test build",
    "branch": "main"
  }'
```

**Expected response:**
```json
{
  "status": "ok",
  "request": "Test build",
  "branch": "main",
  "github": { ... },
  "netlify": { ... }
}
```

---

### **Option 3: Test via n8n UI**

1. **Open:** Unity Build Orchestrator workflow in n8n
2. **Click:** "Execute Workflow" button
3. **Watch:** Execution in real-time
4. **Check:** Each node for errors

---

## 🔍 WHAT TO CHECK

### **1. Webhook Trigger**
- ✅ Receives the request
- ✅ Parses input correctly

### **2. Env Preflight**
- ✅ Checks for required environment variables
- ⚠️ If fails: Missing env vars (GITHUB_REPO_OWNER, etc.)

### **3. Dispatch GitHub Build**
- ✅ Credential found: `github-actions-token`
- ✅ API call succeeds
- ⚠️ If fails: Credential issue or wrong token

### **4. Check Latest GitHub Run**
- ✅ Credential found: `github-actions-token`
- ✅ Gets workflow run status
- ⚠️ If fails: Credential issue

### **5. Check Latest Netlify Deploy**
- ✅ Credential found: `netlify-api-token`
- ✅ Gets deployment status
- ⚠️ If fails: Credential issue or missing Site ID

---

## ⚠️ COMMON ERRORS

### **Error: "Credential not found"**
**Fix:**
- Check credential Name/ID matches exactly:
  - `github-actions-token`
  - `netlify-api-token`

### **Error: "Unauthorized" or "401"**
**Fix:**
- Check Header Value has correct token
- For GitHub: `token YOUR_PAT`
- For Netlify: `Bearer YOUR_TOKEN`

### **Error: "Missing required env var"**
**Fix:**
- Run `robot-hardcode-env-vars.py` again
- Or set environment variables manually

### **Error: "Workflow not found"**
**Fix:**
- Check GitHub workflow file exists
- Verify `GITHUB_WORKFLOW_FILE` env var is correct

---

## ✅ SUCCESS INDICATORS

**If everything works:**
1. ✅ Webhook responds with status "ok"
2. ✅ GitHub Actions workflow is triggered
3. ✅ Netlify deployment status is retrieved
4. ✅ No credential errors in n8n execution

**Check in n8n UI:**
- Execution shows green checkmarks ✅
- No red error nodes ❌
- Response shows GitHub and Netlify status

---

## 📋 TEST CHECKLIST

- [ ] Run test script or manual test
- [ ] Check webhook receives request
- [ ] Verify no credential errors
- [ ] Confirm GitHub Actions triggered
- [ ] Check Netlify status retrieved
- [ ] Review execution in n8n UI

---

## 🎯 AFTER TESTING

**If it works:**
- ✅ Credentials are set up correctly!
- ✅ Ready for production use

**If it fails:**
- Check error message
- Verify credential field names
- Re-run credential setup if needed

---

**Run the test and let's see what happens!** ✅

