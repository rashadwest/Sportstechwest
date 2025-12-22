# Restore Working Workflow - Permission Fix

**Date:** December 10, 2025  
**Issue:** Permission denied when creating `/Users/rashadwest/BTEBallCODE`  
**Solution:** Use original working workflow

---

## 🎯 THE PROBLEM

**Error:**
```
fatal: could not create leading directories of '/Users/rashadwest/BTEBallCODE': Permission denied
```

**Root Cause:**
- The directory `/Users/rashadwest/BTEBallCODE` already exists
- Git clone is trying to CREATE it again (which fails)
- The new workflow tries to create directories that already exist

---

## ✅ THE SOLUTION

**Use the original working workflow:** `n8n-unity-automation-workflow.json`

**Why it works:**
- Uses simpler template syntax: `{{ $env.UNITY_REPO_URL }}`
- Doesn't try to create directories
- Just does git clone or git pull
- Was working before

---

## 📋 WORKFLOW FILES

### Original Working Workflow ✅
**File:** `n8n-unity-automation-workflow-ORIGINAL-WORKING.json` (on Desktop)

**What it does:**
- Uses simple template variables
- Git command: `clone {{ $env.UNITY_REPO_URL }} {{ $env.UNITY_PROJECT_PATH }}`
- Falls back to: `cd {{ $env.UNITY_PROJECT_PATH }} && git pull`
- Doesn't try to create directories

### Current Workflow (Not Working) ❌
**File:** `n8n-unity-automation-workflow-FINAL-WORKING.json`

**What's wrong:**
- Uses complex shell script with `if [ -d ... ]`
- Tries to create directory with `git clone` even if it exists
- Causes permission denied error

---

## 🔧 TO USE THE WORKING WORKFLOW

1. **Import:** `n8n-unity-automation-workflow-ORIGINAL-WORKING.json` from Desktop
2. **Set environment variables** in n8n UI:
   - `UNITY_REPO_URL` = `https://github.com/rashadwest/BallCode.git`
   - `UNITY_PROJECT_PATH` = `/Users/rashadwest/BTEBallCODE`
3. **Test:** Should work without permission errors

---

## 📝 KEY DIFFERENCES

**Original (Working):**
```bash
git clone {{ $env.UNITY_REPO_URL }} {{ $env.UNITY_PROJECT_PATH }} || (cd {{ $env.UNITY_PROJECT_PATH }} && git pull)
```

**New (Not Working):**
```bash
if [ -d '${$json.projectPath}' ]; then 
  cd '${$json.projectPath}' && git pull
else 
  git clone '${$json.repoUrl}' '${$json.projectPath}'  # Tries to create directory
fi
```

**The problem:** The `else` branch tries to create the directory even if it exists, causing permission error.

---

## ✅ RECOMMENDATION

**Use the original working workflow** - it was working before and doesn't have the permission issue.

**File on Desktop:** `n8n-unity-automation-workflow-ORIGINAL-WORKING.json`

---

**Status:** ✅ Original workflow restored  
**Action:** Import from Desktop  
**Result:** Should work without permission errors


