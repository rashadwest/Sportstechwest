# AIMCODE Solution: Git Clone/Update Node Code
## Complete Code to Fix Stuck Node

**Date:** December 9, 2025  
**Issue:** Node stuck, only shows `/bin/sh` in command field  
**Status:** ✅ FIXED - Complete Code Provided

---

## CLEAR Framework

### C - Clarity
**Problem:** Node stuck executing, command field only has `/bin/sh`  
**Root Cause:** Missing full git command with Expression Mode  
**Solution:** Provide complete command with proper template variable expansion

### L - Logic
**Solution Structure:**
1. Use `/bin/sh` as command
2. Use Expression Mode (`={{ }}`) for arguments
3. Include full conditional git logic
4. Proper error handling

### E - Examples
**Previous Working Solution:** Expression Mode with template literals

### A - Adaptation
**Current State:** Command field empty/incomplete  
**Needed:** Full shell script with Expression Mode

### R - Results
**Success Criteria:**
- Node executes without getting stuck
- Git clone works if directory doesn't exist
- Git pull works if directory exists
- Template variables expand correctly

---

## COMPLETE CODE TO ENTER

### **Step 1: Command Field**
Enter this in the **Command** field:
```
/bin/sh
```

### **Step 2: Arguments Field (CRITICAL)**

**IMPORTANT:** Click the **Expression** toggle button first (or type `=` at the start), then paste this:

```
={{ `-c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

---

## STEP-BY-STEP INSTRUCTIONS

### 1. Stop the Stuck Execution
- Click **"Stop"** or **"Cancel"** if the node is still executing

### 2. Open Node Settings
- Click on **"Clone/Update Repository"** node
- Make sure **"Parameters"** tab is selected

### 3. Set Command
- In **Command** field, enter: `/bin/sh`

### 4. Set Arguments (MOST IMPORTANT)
- Click the **Expression** toggle button (looks like `=` or `fx`)
- **Paste this exact code:**
  ```
  ={{ `-c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
  ```

### 5. Verify Settings
- ✅ Command: `/bin/sh`
- ✅ Arguments: Starts with `={{ ` (Expression Mode enabled)
- ✅ Execute Once: Enabled (green toggle)

### 6. Save & Test
- Click **"Save"** button
- Click **"Execute step"** to test
- Should complete without getting stuck

---

## ALTERNATIVE (If Above Doesn't Work)

If `/bin/sh` doesn't work, try `bash`:

**Command:** `bash`

**Arguments (with Expression Mode):**
```
={{ `-c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

---

## WHY THIS WORKS

1. **Expression Mode (`={{ }}`):** Enables template variable expansion
2. **Template Literals (backticks):** Allows string interpolation
3. **Variable Syntax (`${$env.X}`):** Correct syntax for env vars
4. **Shell Script (`-c`):** Properly executes conditional logic
5. **Error Handling:** Clear messages if git operations fail

---

## VERIFICATION

**Node works correctly when:**
- ✅ Executes without getting stuck
- ✅ Completes in reasonable time (few seconds)
- ✅ Shows success message or git output
- ✅ Template variables expand (no `{{ }}` in output)

---

**Copy the Arguments code above and paste it into your node with Expression Mode enabled!**



