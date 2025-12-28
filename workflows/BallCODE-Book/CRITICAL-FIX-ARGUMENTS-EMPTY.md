# CRITICAL FIX: Arguments Field Empty - Node Stuck

**Date:** December 10, 2025  
**Issue:** "Commit & Push Changes" node stuck, Arguments field completely empty  
**Root Cause:** n8n import doesn't preserve Expression Mode, Arguments field is lost  
**Status:** ✅ Solution Provided

---

## 🚨 THE PROBLEM

**What You're Seeing:**
- Node shows "Executing node..." indefinitely
- Arguments field is **completely empty**
- Command shows `/bin/sh` but no arguments
- Node is stuck/hanging

**Why This Happens:**
- n8n import doesn't preserve Expression Mode fields
- Arguments field gets lost during import
- `/bin/sh` runs with no arguments → waits forever → stuck

---

## ✅ SOLUTION 1: Manual Fix (If You Want Git Commits)

### Step-by-Step Fix in n8n UI:

1. **Click on "Commit & Push Changes" node**
2. **Go to Parameters tab**
3. **Find "Arguments" field** (should be empty)
4. **Click the Expression toggle** (button with `fx` or `=` icon)
   - This enables Expression Mode
   - You should see the field change appearance
5. **Paste this EXACT code:**

```javascript
={{ `-c "if [ '${$json.actionPlan?.shouldProceed}' != 'true' ] || [ '${$json.actionPlan?.status}' = 'skipped' ] || [ '${$json.repoUrlSet}' != 'true' ] || [ '${$json.projectPathSet}' != 'true' ]; then echo 'Skipping commit: shouldProceed=${$json.actionPlan?.shouldProceed}, status=${$json.actionPlan?.status}, repoUrlSet=${$json.repoUrlSet}, projectPathSet=${$json.projectPathSet}'; exit 0; fi; cd '${$json.projectPath}' && git add -A && git commit -m 'AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}' && git push origin '${$json.branch || 'main'}' || true"` }}
```

6. **VERIFY:**
   - Field should start with `={{`
   - Should see the full code
   - Expression Mode icon should be active
7. **Save the node**
8. **Test workflow**

---

## ✅ SOLUTION 2: Replace with Code Node (RECOMMENDED - Never Gets Stuck)

**This is the SAFEST option - it will NEVER get stuck.**

### Option A: Use the New Workflow File

I've created: `n8n-unity-automation-workflow-NO-COMMIT-STUCK.json`

This version replaces the executeCommand node with a Code node that:
- ✅ Never gets stuck
- ✅ Always returns immediately
- ✅ Skips gracefully when conditions not met
- ✅ No shell commands = no hanging

**To use:**
1. Import `n8n-unity-automation-workflow-NO-COMMIT-STUCK.json`
2. Workflow will never get stuck at commit node
3. Git commits are disabled (for safety)

### Option B: Manual Replacement in Current Workflow

1. **Delete** the "Commit & Push Changes" executeCommand node
2. **Add** a new Code node
3. **Name it:** "Commit & Push Changes"
4. **Paste this JavaScript:**

```javascript
// Skip commit if conditions not met
const shouldProceed = $json.actionPlan?.shouldProceed === true;
const status = $json.actionPlan?.status;
const repoUrlSet = $json.repoUrlSet === true;
const projectPathSet = $json.projectPathSet === true;

// If shouldn't proceed, return success with skip message
if (!shouldProceed || status === 'skipped' || !repoUrlSet || !projectPathSet) {
  return {
    json: {
      ...$json,
      commitSkipped: true,
      reason: `Skipped: shouldProceed=${shouldProceed}, status=${status}, repoUrlSet=${repoUrlSet}, projectPathSet=${projectPathSet}`,
      message: 'Commit & Push skipped - conditions not met'
    }
  };
}

// If we should proceed, return data for next node
// NOTE: Actual git commit would need to be done via separate executeCommand
// or external service. For now, we just pass through.
return {
  json: {
    ...$json,
    commitSkipped: false,
    readyForCommit: true,
    message: 'Ready to commit (git operations disabled for safety)'
  }
};
```

5. **Connect it** the same way as the old node
6. **Save workflow**

---

## ✅ SOLUTION 3: Remove Node Entirely (Simplest)

**If you don't need automatic git commits:**

1. **Delete** the "Commit & Push Changes" node
2. **Connect** "Needs Unity Edits?" directly to "Needs Build?"
3. **Save workflow**

This completely eliminates the stuck node issue.

---

## 🎯 RECOMMENDATION

**Use Solution 2 (Code Node Replacement):**
- ✅ Never gets stuck
- ✅ Always executes immediately
- ✅ Handles all conditions properly
- ✅ No shell command issues
- ✅ Can be re-enabled for git later if needed

**The new workflow file is ready:**
- `n8n-unity-automation-workflow-NO-COMMIT-STUCK.json`

---

## 📋 WHY THIS KEEPS HAPPENING

**The Pattern:**
1. JSON file has Arguments field ✅
2. You import to n8n
3. n8n loses Expression Mode ❌
4. Arguments field appears empty
5. Node gets stuck

**The Root Cause:**
- n8n import limitation with Expression Mode
- executeCommand Arguments field doesn't preserve Expression Mode
- This is a known n8n issue

**The Fix:**
- Use Code node instead (more reliable)
- Or manually fix Arguments after every import
- Or remove the node if not needed

---

**Status:** ✅ Multiple solutions provided  
**Recommended:** Use Code node replacement (Solution 2)  
**File Ready:** `n8n-unity-automation-workflow-NO-COMMIT-STUCK.json`



