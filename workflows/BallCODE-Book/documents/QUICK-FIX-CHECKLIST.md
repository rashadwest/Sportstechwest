# ⚡ Quick Fix Checklist - n8n Workflow Errors

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Purpose:** Quick reference for fixing the two current errors

---

## 🔧 ERROR 1: Unity Build Orchestrator - Header Error

**Error:** `Header name must be a valid HTTP token ["BalICODE n8n"]`

### ⚡ Quick Fix (2 minutes):

1. **Go to n8n:** http://192.168.1.226:5678
2. **Click:** Credentials (left sidebar)
3. **Find:** Credential used by "Dispatch GitHub Build" node
   - Look for: `github-actions-token` or similar
4. **Click:** Edit (pencil icon)
5. **Check:** "Header Name" field
6. **Fix:** Change to exactly `Authorization` (no spaces, no typos)
7. **Save**
8. **Test:** Run workflow again

**What to look for:**
- ❌ `BalICODE n8n` (invalid - has space)
- ❌ `BallCODE n8n` (invalid - has space)
- ✅ `Authorization` (valid)

---

## 🔧 ERROR 2: Screenshot-to-Fix - OpenAI API Error

**Error:** `Bad request - please check your parameters`

### ⚡ Quick Fix (3 minutes):

#### Step 1: Check Credential (1 minute)

1. **Go to n8n:** http://192.168.1.226:5678
2. **Click:** Credentials
3. **Find:** `openai-api-key` or `OpenAI API Key`
4. **Click:** Edit
5. **Verify:**
   - Header Name: `Authorization` (exactly)
   - Header Value: `Bearer sk-...` (with space after "Bearer")
6. **Save**

#### Step 2: Check HTTP Request Node (2 minutes)

1. **Open:** Screenshot-to-Fix workflow
2. **Click:** "Vision Analysis (HTTP Request)" or "Generate Fix (HTTP Request)" node
3. **Check JSON Body:**
   - Must have `"model": "gpt-4o"` or `"model": "gpt-4"`
   - Must have `"messages": [...]` array
4. **If missing:** Add them or fix the expression

**Quick Test:**
- Click "Execute step" button
- If still error, check the response for more details

---

## ✅ VERIFICATION

**After fixes, verify:**
- [ ] Unity Build Orchestrator runs without header errors
- [ ] Screenshot-to-Fix runs without OpenAI errors
- [ ] Both workflows complete successfully

---

## 📚 FULL DETAILS

See: `documents/N8N-WORKFLOW-ERRORS-AIMCODE-FIX.md` for complete solutions and self-healing system design.

---

**Quick Reference:** Keep this file open while fixing errors!

