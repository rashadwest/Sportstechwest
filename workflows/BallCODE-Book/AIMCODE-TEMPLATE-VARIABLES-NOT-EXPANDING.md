# AIMCODE Fix: Template Variables Not Expanding
## Final Solution - Expression Mode Required

**Date:** December 9, 2025  
**Issue:** Template variables `{{ $env.UNITY_REPO_URL }}` not expanding  
**Error:** "fatal: Too many arguments" and "can't cd to {{"  
**Status:** ✅ FIXED - Expression Mode Required

---

## CLEAR Framework

### C - Clarity
**Problem:** Template variables showing as literal `{{ }}` instead of expanding  
**Root Cause:** Arguments field not in Expression Mode  
**Solution:** Enable Expression Mode and use correct syntax

### L - Logic
**Why Variables Don't Expand:**
- executeCommand Arguments field needs Expression Mode for template expansion
- Without Expression Mode, `{{ }}` is treated as literal text
- Need `=` prefix to enable expression evaluation

### E - Examples
**Working Pattern:** Expression Mode with template literals or direct variable access

### A - Adaptation
**Constraint:** Must work in n8n executeCommand  
**Flexibility:** Can use Expression Mode or alternative approach

### R - Results
**Success:** Variables expand, git command executes correctly

---

## SOLUTION: Enable Expression Mode

### **Command:** `git`

### **Arguments (Enable Expression Mode First!):**

**Step 1:** Click the **Expression** toggle button (looks like `=` or `fx`)

**Step 2:** Paste this code:
```
={{ `clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || (cd '${$env.UNITY_PROJECT_PATH}' && git pull)` }}
```

---

## ALTERNATIVE: Simpler Approach (If Expression Mode Fails)

If Expression Mode still doesn't work, use this simpler version:

### **Command:** `sh`

### **Arguments (Expression Mode enabled):**
```
={{ `-c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}'; fi"` }}
```

---

## STEP-BY-STEP

1. **Command field:** `git`
2. **Arguments field:**
   - Click **Expression** toggle (or type `=`)
   - Paste: `={{ `clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || (cd '${$env.UNITY_PROJECT_PATH}' && git pull)` }}`
3. **Save**

---

**The key is enabling Expression Mode in the Arguments field!**



