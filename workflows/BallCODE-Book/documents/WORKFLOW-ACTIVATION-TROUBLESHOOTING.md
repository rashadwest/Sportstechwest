# 🔧 Workflow Activation Troubleshooting

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Problem:** Workflows not triggering (404 errors persist after import)

---

## 🚨 COMMON ISSUES & FIXES

### Issue 1: Workflow Not Activated After Import

**Symptom:** 404 error even after importing

**Fix:**
1. Open workflow in n8n UI
2. Look for toggle switch in top-right
3. Toggle must be **ON** (blue/green)
4. If OFF (gray), click to turn ON
5. Click "Save" button

**Check:** Toggle should show "Active" not "Inactive"

---

### Issue 2: Webhook Path Mismatch

**Symptom:** 404 error with correct path

**Fix:**
1. Open workflow in n8n
2. Click on webhook trigger node
3. Check "Path" field in Parameters tab
4. Must match URL: `/webhook/[path]`

**Example:**
- Path: `screenshot-fix`
- URL: `http://192.168.1.226:5678/webhook/screenshot-fix`

---

### Issue 3: Respond to Webhook Node Not Connected

**Symptom:** Workflow shows error: "Insert a 'Respond to Webhook' node"

**Fix:**
1. Open workflow in n8n
2. Check for red error messages
3. If error shows, all execution paths must reach "Respond to Webhook" node
4. Connect all end nodes to "Respond to Webhook" node

**Note:** This should already be fixed in the workflow files

---

### Issue 4: Workflow Imported But Not Saved

**Symptom:** Workflow appears but disappears after refresh

**Fix:**
1. After importing, open workflow
2. Click "Save" button (even if no changes)
3. This ensures workflow is persisted

---

### Issue 5: n8n Instance Not Running

**Symptom:** Can't access n8n UI or 404 errors

**Check:**
```bash
# Ping Pi
ping 192.168.1.226

# Check if n8n is accessible
curl http://192.168.1.226:5678
```

**Fix:** Restart n8n on Pi if not running

---

## ✅ VERIFICATION CHECKLIST

After importing workflows, verify:

- [ ] **Workflow appears in "Workflows" list**
- [ ] **Workflow opens without errors**
- [ ] **Toggle switch is ON (blue/green)**
- [ ] **No red error messages in workflow**
- [ ] **Webhook node shows correct path**
- [ ] **Respond to Webhook node exists and is connected**
- [ ] **Workflow is saved (click Save button)**

---

## 🧪 TEST AFTER FIXING

Once all checkboxes are ✅, test:

```bash
# Test Screenshot Fix
curl -X POST "http://192.168.1.226:5678/webhook/screenshot-fix" \
  -H "Content-Type: application/json" \
  -d '{"screenshotUrl": "https://example.com/test.png", "context": "Test"}'

# Test Full Integration
curl -X POST "http://192.168.1.226:5678/webhook/ballcode-dev" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test", "mode": "quick"}'

# Test Unity Build
curl -X POST "http://192.168.1.226:5678/webhook/unity-build" \
  -H "Content-Type: application/json" \
  -d '{"request": "Test", "branch": "main"}'
```

**Expected:** JSON response (not 404)

---

## 🔍 DEBUGGING STEPS

### Step 1: Check Workflow Status in n8n

1. Go to "Workflows" list
2. Look for your workflows
3. Check status column (Active/Inactive)
4. If Inactive, click to open and activate

### Step 2: Check Webhook Node

1. Open workflow
2. Click on webhook trigger node
3. Check "Path" field
4. Verify it matches your test URL

### Step 3: Check for Errors

1. Open workflow
2. Look for red error messages
3. Hover over nodes to see errors
4. Fix any connection issues

### Step 4: Check Executions

1. Go to "Executions" in n8n
2. Look for recent webhook calls
3. If you see executions but 404, check execution details
4. If no executions, workflow is not active

---

## 💡 QUICK FIX COMMAND

**If workflows are imported but not activated:**

1. Open each workflow in n8n UI
2. Toggle switch to ON
3. Click Save
4. Test again

**This is the most common issue!**

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Troubleshooting Guide


