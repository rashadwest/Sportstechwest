# CRITICAL FIX: Arguments Field Missing

**Date:** December 10, 2025  
**Issue:** Commit & Push node shows only `/bin/sh` with NO arguments  
**Root Cause:** Arguments field missing or not being saved  
**Status:** ✅ FIXED

---

## 🚨 THE REAL PROBLEM

**What you're seeing:**
- Command field: `/bin/sh`
- Arguments field: **EMPTY or MISSING**
- Node stuck executing because shell has no command to run

**Why it's stuck:**
- `/bin/sh` starts a shell
- Shell has no command (`-c "..."`) to execute
- Shell waits forever for input
- Node appears "stuck"

---

## ✅ THE FIX

**Arguments field MUST be set with:**

```javascript
={{ `-c "if [ '${$json.actionPlan?.shouldProceed}' != 'true' ] || [ '${$json.actionPlan?.status}' = 'skipped' ] || [ '${$json.repoUrlSet}' != 'true' ] || [ '${$json.projectPathSet}' != 'true' ]; then echo 'Skipping commit: shouldProceed=${$json.actionPlan?.shouldProceed}, status=${$json.actionPlan?.status}, repoUrlSet=${$json.repoUrlSet}, projectPathSet=${$json.projectPathSet}'; exit 0; fi; cd '${$json.projectPath}' && git add -A && git commit -m 'AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}' && git push origin '${$json.branch || 'main'}' || true"` }}
```

**This provides:**
1. Early exit check (exits immediately if shouldn't run)
2. Git commands (only runs if checks pass)
3. Proper shell command structure

---

## 🔧 HOW TO VERIFY IN n8n

After importing the workflow:

1. **Click on "Commit & Push Changes" node**
2. **Check Parameters tab:**
   - Command: Should be `/bin/sh`
   - **Arguments:** Should have the long Expression Mode code above
   - If Arguments is empty → The fix didn't apply

3. **If Arguments is empty:**
   - Click the **Expression** toggle (or type `=` at start)
   - Paste the arguments code from above
   - Save the node

---

## ⚠️ IMPORTANT NOTE

**When importing workflows, n8n sometimes:**
- Doesn't preserve Expression Mode on arguments field
- Shows arguments as empty even though they're in JSON
- Requires manual re-enabling of Expression Mode

**Solution:**
- After importing, check the Arguments field
- If empty, manually enable Expression Mode and paste the code
- This ensures the node works correctly

---

## 📋 COMPLETE NODE CONFIGURATION

**Command:** `/bin/sh`

**Arguments (Expression Mode enabled):**
```
={{ `-c "if [ '${$json.actionPlan?.shouldProceed}' != 'true' ] || [ '${$json.actionPlan?.status}' = 'skipped' ] || [ '${$json.repoUrlSet}' != 'true' ] || [ '${$json.projectPathSet}' != 'true' ]; then echo 'Skipping commit: shouldProceed=${$json.actionPlan?.shouldProceed}, status=${$json.actionPlan?.status}, repoUrlSet=${$json.repoUrlSet}, projectPathSet=${$json.projectPathSet}'; exit 0; fi; cd '${$json.projectPath}' && git add -A && git commit -m 'AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}' && git push origin '${$json.branch || 'main'}' || true"` }}
```

**Execute Once:** Enabled

---

## ✅ VERIFICATION CHECKLIST

After importing, verify:
- [ ] Command field has `/bin/sh`
- [ ] Arguments field has the Expression Mode code
- [ ] Expression Mode is enabled (see `=` or `fx` icon)
- [ ] Arguments field is NOT empty
- [ ] Node can execute without getting stuck

---

**Status:** ✅ Arguments field properly set in workflow file  
**Note:** May need to manually enable Expression Mode after import



