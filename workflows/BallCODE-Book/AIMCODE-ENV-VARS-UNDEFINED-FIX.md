# AIMCODE Fix: Environment Variables Showing as 'undefined'
## Correct Syntax for Accessing Environment Variables

**Date:** December 9, 2025  
**Issue:** Environment variables showing as 'undefined' in executeCommand  
**Status:** ✅ DIAGNOSED - Wrong Syntax

---

## CLEAR Framework

### C - Clarity
**Problem:** `$env.UNITY_REPO_URL` returns `undefined`  
**Root Cause:** Wrong syntax for accessing environment variables in Expression Mode  
**Solution:** Use correct syntax or verify variables are set

### L - Logic
**Possible Causes:**
1. Environment variables not set in n8n
2. Wrong syntax: `${$env.X}` might not work
3. Need different syntax: `$env.X` or `process.env.X`

### E - Examples
**Correct Syntax Options:**
- `$env.VARIABLE_NAME` (direct access)
- `process.env.VARIABLE_NAME` (Node.js style)
- Verify variables exist first

### A - Adaptation
**Fix:** Try different syntax or verify variables are set

### R - Results
**Success:** Variables expand to actual values, not 'undefined'

---

## SOLUTION 1: Verify Environment Variables Are Set

**First, check if variables exist:**

1. Go to **Settings** → **Environment Variables** in n8n
2. Verify these exist:
   - `UNITY_REPO_URL` (should be your GitHub repo URL)
   - `UNITY_PROJECT_PATH` (should be path like `/path/to/project`)
3. If missing, add them

---

## SOLUTION 2: Try Different Syntax

### **Option A: Direct Access (No Template Literal)**

**Enable Expression Mode, then paste:**
```
={{ `/bin/sh -c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

**If that doesn't work, try Option B:**

### **Option B: Use process.env**

**Enable Expression Mode, then paste:**
```
={{ `/bin/sh -c "if [ -d '${process.env.UNITY_PROJECT_PATH}' ]; then cd '${process.env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${process.env.UNITY_REPO_URL}' '${process.env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

---

## SOLUTION 3: Use Code Node to Get Variables First

**Add a Code node BEFORE executeCommand:**

```javascript
// Get environment variables and pass to next node
return {
  json: {
    repoUrl: $env.UNITY_REPO_URL || 'NOT SET',
    projectPath: $env.UNITY_PROJECT_PATH || 'NOT SET',
    // Verify they exist
    repoUrlSet: !!$env.UNITY_REPO_URL,
    projectPathSet: !!$env.UNITY_PROJECT_PATH
  }
};
```

**Then in executeCommand, use:**
```
={{ `/bin/sh -c "if [ -d '${$json.projectPath}' ]; then cd '${$json.projectPath}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$json.repoUrl}' '${$json.projectPath}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

---

## SOLUTION 4: Hardcode for Testing (Verify Command Works)

**To test if command structure works, temporarily hardcode values:**

**Enable Expression Mode, paste:**
```
={{ `/bin/sh -c "if [ -d '/tmp/test' ]; then cd '/tmp/test' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone 'https://github.com/your-repo/your-project.git' '/tmp/test' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

**If this works, the issue is environment variable access, not the command.**

---

## DIAGNOSTIC: Check Variables

**Add a Code node to check variables:**

```javascript
return {
  json: {
    unityRepoUrl: $env.UNITY_REPO_URL,
    unityProjectPath: $env.UNITY_PROJECT_PATH,
    allEnvVars: Object.keys($env || {}),
    test: 'Variables check'
  }
};
```

**This will show:**
- What variables are available
- Their actual values
- If they're set at all

---

## RECOMMENDED: Solution 3 (Code Node First)

**This is most reliable:**
1. Code node gets variables and validates
2. Passes them to executeCommand
3. executeCommand uses `$json.variableName` (more reliable)

---

**First, verify your environment variables are set in n8n Settings!**




