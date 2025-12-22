# 🔧 Complete Debugging Guide - Step by Step

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Goal:** Get all 3 webhooks working end-to-end

---

## 🎯 CURRENT STATUS

✅ **Unity Build:** Working (returns response)  
❌ **Screenshot Fix:** 200 status but empty response  
❌ **Full Integration:** 200 status but empty response

---

## 📋 STEP 1: Check n8n Executions (Find the Errors)

**This will show you EXACTLY what's failing:**

1. **Open Pi n8n UI:**
   ```
   http://192.168.1.226:5678
   ```

2. **Click "Executions" in left sidebar**

3. **Look for recent executions** (should be from the last few minutes)

4. **Click on each execution** to see:
   - ✅ Green nodes = worked
   - ❌ Red nodes = failed (THIS IS THE PROBLEM)
   - ⚠️ Yellow nodes = warnings

5. **Click on any RED node** to see the error message

**Write down:**
- Which workflow failed
- Which node is red
- What the error message says

---

## 🔍 STEP 2: Common Errors & Fixes

### Error 1: "Credential not found" or "OpenAI API key missing"

**Symptom:** Red node at OpenAI/Vision Analysis node

**Fix:**
1. Go to **Settings → Credentials**
2. Click **"Add Credential"**
3. Search for **"OpenAI"**
4. Select **"OpenAI API"**
5. Enter:
   - **Name:** `OpenAI API` (exactly this name)
   - **API Key:** Your OpenAI API key
6. Click **"Save"**
7. Go back to workflow
8. Click on the OpenAI node
9. Select the credential you just created
10. Click **"Save"** on the workflow

---

### Error 2: "Node execution failed" or "Timeout"

**Symptom:** Red node with timeout/execution error

**Possible Causes:**
- OpenAI API key invalid
- Network issue
- Node configuration wrong

**Fix:**
1. Check OpenAI API key is valid
2. Check internet connection on Pi
3. Verify node configuration matches workflow file

---

### Error 3: "Respond to Webhook node not reached"

**Symptom:** Workflow stops before Respond node

**Fix:**
1. Check all nodes before Respond node
2. Fix any red nodes
3. Ensure all paths lead to Respond node

---

## 🚀 STEP 3: Test After Fixing

**After fixing errors, test again:**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/test-webhooks-debug.sh
```

**Or test individually:**

```bash
# Test Screenshot Fix
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test"}'

# Test Full Integration
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test", "mode": "quick"}'
```

---

## 📸 STEP 4: If Still Not Working - Screenshot the Error

**If you still can't figure it out:**

1. **Open the failed execution in n8n**
2. **Screenshot the red node with error message**
3. **Send me the screenshot** - I'll tell you exactly what to fix

---

## 🎯 QUICK CHECKLIST

- [ ] Opened n8n Executions tab
- [ ] Found recent executions
- [ ] Clicked on failed executions
- [ ] Identified red nodes
- [ ] Read error messages
- [ ] Fixed errors (likely OpenAI credentials)
- [ ] Tested again
- [ ] All workflows now return responses

---

## 💡 MOST COMMON FIX (90% of cases)

**The issue is almost always OpenAI credentials:**

1. **Settings → Credentials → Add "OpenAI API"**
2. **Enter your API key**
3. **Save**
4. **Go to each workflow with OpenAI nodes**
5. **Click the OpenAI node**
6. **Select the credential**
7. **Save workflow**
8. **Test again**

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Complete Step-by-Step Guide


