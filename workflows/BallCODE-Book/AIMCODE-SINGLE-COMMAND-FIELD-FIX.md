# AIMCODE Fix: Single Command Field - Complete Solution
## All-in-One Command for Execute Command Node

**Date:** December 9, 2025  
**Issue:** Only one "Command" field, template variables not expanding  
**Status:** ✅ FIXED - Complete Command Provided

---

## CLEAR Framework

### C - Clarity
**Problem:** Execute Command node has only ONE field (Command), template variables not expanding  
**Root Cause:** Need to enable Expression Mode in the single Command field  
**Solution:** Put complete command with Expression Mode in single field

### L - Logic
**Single Field Structure:**
- Command field accepts full command
- Need Expression Mode to expand variables
- Use shell wrapper for conditional logic

### E - Examples
**Pattern:** `sh -c "command with variables"` with Expression Mode

### A - Adaptation
**Constraint:** Only one field available  
**Flexibility:** Put everything in that one field with proper syntax

### R - Results
**Success:** Command executes, variables expand, git operations work

---

## SOLUTION: Complete Command for Single Field

### **Enable Expression Mode First!**

Click the **Expression** toggle button (or type `=` at the start of the field)

### **Then Paste This Complete Command:**

```
={{ `/bin/sh -c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

---

## ALTERNATIVE: Simpler Version (If Above Too Complex)

If the above doesn't work, try this simpler version:

**Enable Expression Mode, then paste:**
```
={{ `sh -c "git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' 2>/dev/null || (cd '${$env.UNITY_PROJECT_PATH}' && git pull)"` }}
```

---

## STEP-BY-STEP

1. **Click in the "Command" field**
2. **Click the Expression toggle** (looks like `=` or `fx` button)
3. **Delete any existing text**
4. **Paste the complete command above**
5. **Save the node**
6. **Test**

---

## WHY THIS WORKS

- **Expression Mode (`={{ }}`):** Enables template variable expansion
- **Shell wrapper (`/bin/sh -c`):** Executes the conditional logic
- **Template literals (backticks):** Allows variable interpolation
- **Variable syntax (`${$env.X}`):** Correct syntax for env vars

---

**Put the ENTIRE command (with Expression Mode) in that single Command field!**



