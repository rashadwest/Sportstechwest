# Fix: Arguments Field Empty / Expression Mode Not Working

**Date:** December 10, 2025  
**Issue:** Arguments field empty, `={{` not working  
**Solution:** Alternative approaches that actually work

---

## 🚨 THE PROBLEM

**What you're seeing:**
- Arguments field is completely empty
- Node stuck executing
- Expression Mode (`={{`) not working

**Why this happens:**
- n8n sometimes doesn't preserve Arguments field on import
- Expression Mode toggle might not be working
- Syntax might be getting stripped

---

## ✅ SOLUTION 1: Use Code Node Instead (RECOMMENDED)

**This is the most reliable approach:**

### Step 1: Delete the executeCommand Node
- Right-click "Commit & Push Changes" node
- Delete it

### Step 2: Add Code Node
- Add new node → Code
- Name it: "Commit & Push Changes"

### Step 3: Paste This JavaScript:

```javascript
// Check if should proceed
const shouldProceed = $json.actionPlan?.shouldProceed === true;
const status = $json.actionPlan?.status;
const repoUrlSet = $json.repoUrlSet === true;
const projectPathSet = $json.projectPathSet === true;

// Early exit if shouldn't run
if (!shouldProceed || status === 'skipped' || !repoUrlSet || !projectPathSet) {
  return {
    json: {
      ...$json,
      skipped: true,
      reason: `shouldProceed=${shouldProceed}, status=${status}, repoUrlSet=${repoUrlSet}, projectPathSet=${projectPathSet}`,
      message: 'Commit & Push skipped - conditions not met'
    }
  };
}

// If we get here, we need to actually do git operations
// But Code node can't execute shell commands directly
// So we'll prepare the data and use a separate executeCommand node

return {
  json: {
    ...$json,
    readyToCommit: true,
    commitMessage: `AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}`,
    branch: $json.branch || 'main',
    projectPath: $json.projectPath,
    gitCommand: `cd '${$json.projectPath}' && git add -A && git commit -m 'AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}' && git push origin '${$json.branch || 'main'}' || true`
  }
};
```

### Step 4: Add Simple executeCommand Node After Code Node
- Add new node → Execute Command
- Name it: "Execute Git Commit"
- **Command:** `sh`
- **Arguments:** `={{ $json.gitCommand }}`
- Enable Expression Mode on Arguments field

**This splits the logic (Code node) from execution (executeCommand), which is more reliable.**

---

## ✅ SOLUTION 2: Single Command Field (If You Must Use executeCommand)

**Put everything in the Command field, leave Arguments empty:**

### Step 1: Open "Commit & Push Changes" node

### Step 2: Set Command Field (Enable Expression Mode First!)
1. Click in **Command** field
2. Click the **Expression** toggle (fx icon or `=` button)
3. **Paste this:**

```javascript
={{ `/bin/sh -c "if [ '${$json.actionPlan?.shouldProceed}' != 'true' ] || [ '${$json.actionPlan?.status}' = 'skipped' ] || [ '${$json.repoUrlSet}' != 'true' ] || [ '${$json.projectPathSet}' != 'true' ]; then echo 'Skipping commit'; exit 0; fi; cd '${$json.projectPath}' && git add -A && git commit -m 'AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}' && git push origin '${$json.branch || 'main'}' || true"` }}
```

### Step 3: Leave Arguments Field Empty
- Don't put anything in Arguments field
- Everything goes in Command field

### Step 4: Save and Test

---

## ✅ SOLUTION 3: Manual Arguments Field Fix (If Expression Mode Works)

**If Expression Mode toggle actually works:**

### Step 1: Open "Commit & Push Changes" node
### Step 2: Command Field
- Set to: `/bin/sh`
- **Do NOT enable Expression Mode on Command**

### Step 3: Arguments Field
1. Click in **Arguments** field
2. **Click the Expression toggle** (fx icon) - this is critical!
3. **Paste this (without the `={{` at start, n8n adds it):**

```
-c "if [ '${$json.actionPlan?.shouldProceed}' != 'true' ] || [ '${$json.actionPlan?.status}' = 'skipped' ] || [ '${$json.repoUrlSet}' != 'true' ] || [ '${$json.projectPathSet}' != 'true' ]; then echo 'Skipping commit'; exit 0; fi; cd '${$json.projectPath}' && git add -A && git commit -m 'AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}' && git push origin '${$json.branch || 'main'}' || true"
```

**Note:** When Expression Mode is enabled, n8n automatically adds `={{ }}` wrapper. You just paste the content.

### Step 4: Verify
- Arguments field should show the code
- Should see `fx` icon or Expression Mode indicator
- Save

---

## 🎯 RECOMMENDED: Use Solution 1 (Code Node)

**Why:**
- Most reliable
- No Expression Mode issues
- Easier to debug
- Can test logic separately from execution
- Follows AI Automation Society best practices

**Steps:**
1. Replace executeCommand with Code node
2. Code node checks conditions and prepares git command
3. Simple executeCommand node runs the prepared command

---

## 🔍 VERIFICATION

After applying any solution:

1. **Check the node:**
   - [ ] Command field has value (or Code node has JavaScript)
   - [ ] Arguments field has value (if using executeCommand)
   - [ ] Expression Mode is enabled (if using expressions)

2. **Test the workflow:**
   - [ ] Node doesn't get stuck
   - [ ] Skips gracefully when `shouldProceed: false`
   - [ ] Executes when conditions are met

---

## 💡 WHY THIS KEEPS HAPPENING

**Root Cause:**
- n8n's executeCommand Arguments field with Expression Mode is fragile
- Import/export doesn't always preserve Expression Mode
- UI sometimes doesn't show Expression Mode correctly
- Syntax can get stripped or corrupted

**Solution:**
- Use Code node for logic (more reliable)
- Use simple executeCommand for execution
- Or put everything in Command field (single field, less fragile)

---

**Status:** ✅ Multiple solutions provided  
**Recommended:** Solution 1 (Code Node approach)  
**Reason:** Most reliable, no Expression Mode issues


