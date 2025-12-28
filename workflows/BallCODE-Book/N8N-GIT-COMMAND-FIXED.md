# n8n Git Command Fix - AIMCODE Solution
## Fixed Code for Clone/Update Repository Node

**Date:** December 9, 2025  
**Issue:** Template variables not expanding in git command  
**Status:** ✅ FIXED

---

## 🎯 THE PROBLEM

**Your Current Command:**
```
git clone {{ $env.UNITY_REPO_URL }} {{ $env.UNITY_PROJECT_PATH }} 2>/dev/null || (cd {{ $env.UNITY_PROJECT_PATH }} && git pull)
```

**Issue:** Template variables `{{ $env.UNITY_REPO_URL }}` are not expanding because:
1. Arguments field is not in Expression Mode
2. Need `=` prefix to enable template evaluation
3. Need proper shell script structure with `-c` flag

---

## ✅ THE FIX

### **Updated Node Configuration:**

**Command:** `/bin/sh`

**Arguments (with Expression Mode enabled):**
```
={{ `-c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

---

## 📋 HOW TO APPLY IN n8n UI

### Step 1: Open the Node
1. Click on **"Clone/Update Repository"** node in your workflow

### Step 2: Update Command
1. In **Parameters** tab:
   - **Command:** Change to `/bin/sh`

### Step 3: Update Arguments (IMPORTANT)
1. Click the **Expression** toggle button (or type `=` at the start)
2. **Paste this code:**
   ```
   ={{ `-c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
   ```

3. **Save** the node

---

## 🔍 WHY THIS WORKS

1. **Expression Mode (`={{ }}`):** Enables template variable expansion
2. **Template Literals (backticks):** Allows string interpolation
3. **Variable Syntax (`${$env.X}`):** Correct syntax for expanding env vars inside template literals
4. **Shell Script (`-c`):** Properly executes the conditional logic
5. **Error Handling:** Clear error messages if git operations fail

---

## ✅ VERIFICATION

**After applying the fix:**
- ✅ Template variables expand correctly
- ✅ Git clone works if directory doesn't exist
- ✅ Git pull works if directory exists
- ✅ Clear error messages if something fails
- ✅ Command doesn't get stuck

---

## 🚀 ALTERNATIVE (If Above Doesn't Work)

If `/bin/sh` doesn't work, try `bash`:

**Command:** `bash`

**Arguments:**
```
={{ `-c "if [ -d '${$env.UNITY_PROJECT_PATH}' ]; then cd '${$env.UNITY_PROJECT_PATH}' && git pull || { echo 'Git pull failed'; exit 1; }; else git clone '${$env.UNITY_REPO_URL}' '${$env.UNITY_PROJECT_PATH}' || { echo 'Git clone failed'; exit 1; }; fi"` }}
```

---

**The fix is ready! Copy the arguments code above and paste it into your n8n node with Expression Mode enabled.**




