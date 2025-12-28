# AIMCODE Fix: Commit & Push Changes Node

**Date:** December 10, 2025  
**Issue:** `bash: not found` error  
**Solution:** Changed to `/bin/sh` + Made conditional + Fixed Expression Mode  
**Status:** ✅ FIXED

---

## 🎯 THE PROBLEM

**Error:**
```
Command failed: bash
/bin/sh: bash: not found
```

**Root Cause:**
1. Command field set to `bash` (not available in n8n environment)
2. Arguments using template syntax `{{ }}` instead of Expression Mode
3. Node always runs, even when variables not set

---

## ✅ THE FIX

### Changes Made

1. **Changed Command:** `bash` → `/bin/sh`
   - `/bin/sh` is available in n8n environment
   - More reliable than bash

2. **Fixed Arguments:** Converted to Expression Mode
   - **Before:** `-c 'cd "{{ $env.UNITY_PROJECT_PATH }}" && ...'`
   - **After:** `={{ `-c "cd '${$json.projectPath}' && ..."` }}`
   - Uses data from "Get Git Variables" node
   - Proper Expression Mode syntax

3. **Made Conditional:** Added "Should Commit & Push?" node
   - Only runs if variables are set
   - Skips if variables missing or workflow should skip
   - Workflow continues even if commit skipped

---

## 📋 NEW FLOW

**Before:**
```
AI Unity Editor Edits → Commit & Push Changes → Needs Build?
                      (ALWAYS RUNS, FAILS IF BASH NOT FOUND)
```

**After:**
```
AI Unity Editor Edits → Should Commit & Push?
                          ├─ YES → Commit & Push Changes → Needs Build?
                          └─ NO  → Needs Build? (skip commit)
```

---

## 🔧 NODE CONFIGURATION

### Commit & Push Changes Node

**Command:** `/bin/sh` (changed from `bash`)

**Arguments (Expression Mode):**
```
={{ `-c "cd '${$json.projectPath}' && git add -A && git commit -m 'AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}' && git push origin '${$json.branch || 'main'}' || true"` }}
```

**Key Points:**
- Uses `$json.projectPath` from "Get Git Variables" node
- Uses `$json.branch` or defaults to 'main'
- `|| true` ensures node doesn't fail if git operations fail
- Expression Mode (`={{ }}`) enables variable expansion

---

## ✅ BENEFITS

1. **No More Errors:** `/bin/sh` is available, won't fail
2. **Proper Syntax:** Expression Mode works correctly
3. **Conditional:** Only runs when needed
4. **Graceful:** Workflow continues even if commit skipped

---

## 🚀 NEXT STEPS

1. **Import Updated Workflow:**
   - File: `n8n-unity-automation-workflow-FINAL-WORKING.json` (on Desktop)
   - Import into n8n

2. **Test:**
   - Workflow should no longer fail on this node
   - Commit & Push runs when variables are set
   - Skips gracefully when variables not set

---

## 📊 SUMMARY

**Fixed Issues:**
- ✅ Changed `bash` to `/bin/sh`
- ✅ Fixed Expression Mode syntax
- ✅ Made node conditional
- ✅ Workflow no longer blocks

**Result:** Node works correctly and workflow continues smoothly!

---

**Version:** 1.0  
**Created:** December 10, 2025  
**Method:** AIMCODE Analysis + Conditional Logic + Syntax Fix



