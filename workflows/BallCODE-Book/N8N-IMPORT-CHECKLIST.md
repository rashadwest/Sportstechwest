# n8n Workflow Import Checklist

**Date:** December 10, 2025  
**Purpose:** Ensure workflow works correctly after import

---

## ⚠️ CRITICAL: n8n Import Limitation

**Known Issue:** Expression Mode fields in executeCommand nodes may not import correctly.  
**Result:** Arguments field appears empty even though it's in the JSON file.  
**Solution:** Manually verify and fix after import.

---

## 📋 POST-IMPORT CHECKLIST

### 1. Commit & Push Changes Node

**After importing, check this node FIRST:**

- [ ] Open "Commit & Push Changes" node
- [ ] Go to Parameters tab
- [ ] **Command field:** Should be `/bin/sh`
- [ ] **Arguments field:** 
  - [ ] Is it empty? → **THIS IS THE PROBLEM!**
  - [ ] If empty, click Expression toggle (`=` or `fx`)
  - [ ] Paste the code from CLAUDE-REVIEW-COMMIT-PUSH-NODE.md
  - [ ] Verify Expression Mode is enabled
- [ ] Save the node

### 2. Clone/Update Repository Node

- [ ] Command: `/bin/sh`
- [ ] Arguments: Should have Expression Mode code
- [ ] If empty, fix same way as above

### 3. Verify Conditional Nodes

- [ ] "Should Clone Repository?" exists
- [ ] "Should Commit & Push?" exists
- [ ] Both have proper conditions set

### 4. Test Workflow

- [ ] Run workflow
- [ ] Check execution logs
- [ ] Verify nodes don't get stuck
- [ ] Check for error messages

---

## 🔧 QUICK FIX FOR EMPTY ARGUMENTS

**If Arguments field is empty:**

1. Click Expression toggle
2. Paste this:

```javascript
={{ `-c "set -e; if [ '${$json.shouldProceed}' != 'true' ] || [ '${$json.status}' = 'skipped' ] || [ '${$json.repoUrlSet}' != 'true' ] || [ '${$json.projectPathSet}' != 'true' ] || [ -n '${$json.error || ''}' ]; then echo 'Skipping commit/push: shouldProceed=${$json.shouldProceed}, status=${$json.status}, repoUrlSet=${$json.repoUrlSet}, projectPathSet=${$json.projectPathSet}, error=${$json.error || ''}'; exit 0; fi; cd '${$json.projectPath}'; git add -A; if git diff --cached --quiet; then echo 'No changes to commit.'; else git commit -m 'AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}'; fi; git push origin '${$json.branch || 'main'}'"` }}
```

3. Save
4. Test

---

**This checklist prevents the "stuck" issue!**

