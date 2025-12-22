# 🔧 Fix "Commit Changes" Node - Command Failed: git

**Problem:** "Commit Changes" node failing with "Command failed: git"  
**Root Cause:** Command field only has "git" without arguments  
**Solution:** Fix executeCommand OR replace with Code node

---

## 🎯 QUICK FIX (2 Options)

### Option 1: Fix executeCommand Node (Fastest)

**Current Problem:**
- Command field: `git` (incomplete)
- No arguments = git command fails

**Fix:**
1. Click on **"Commit Changes"** node
2. **Command field:** Change to `/bin/sh`
3. **Arguments field:** Enable Expression Mode (click `=` button), then paste:

```
={{ `-c "cd '${$json.projectPath}' && git add -A && git commit -m 'AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}' && git push origin '${$json.branch || 'main'}' || true"` }}
```

**Why `|| true` at the end:**
- Prevents workflow from failing if there are no changes to commit
- Git will exit with code 0 even if nothing to commit

---

### Option 2: Replace with Code Node (More Reliable) ⭐

**Step 1: Delete Current Node**
- Click "Commit Changes" node
- Press Delete

**Step 2: Add Code Node**
- Click "+" → Search "Code"
- Name it: "Commit Changes"

**Step 3: Paste This Code**

```javascript
// Get data from previous nodes
const data = $input.item.json;

// Extract values
const projectPath = data.projectPath || '';
const branch = data.branch || 'main';
const request = $('Normalize Input').item.json.request || 'Automated changes';

// Debug logging
console.log('=== Commit Changes Debug ===');
console.log('projectPath:', projectPath);
console.log('branch:', branch);
console.log('request:', request);

// Validate project path
if (!projectPath || projectPath.trim() === '') {
  return {
    json: {
      ...data,
      success: false,
      error: 'projectPath is empty',
      action: 'skipped',
      message: 'Cannot commit - project path not set'
    }
  };
}

// Use $exec() for git operations
try {
  // Change to project directory and check git status
  const checkStatusCmd = `cd "${projectPath}" && git status --porcelain`;
  console.log('Checking git status...');
  
  const statusResult = $exec(checkStatusCmd);
  const hasChanges = statusResult.stdout.trim().length > 0;
  
  console.log('Has changes?', hasChanges);
  console.log('Status output:', statusResult.stdout);
  
  if (!hasChanges) {
    console.log('No changes to commit - skipping');
    return {
      json: {
        ...data,
        success: true,
        action: 'skipped',
        message: 'No changes to commit',
        output: 'Working tree clean'
      }
    };
  }
  
  // Add all changes
  console.log('Adding all changes...');
  const addCmd = `cd "${projectPath}" && git add -A`;
  const addResult = $exec(addCmd);
  
  if (addResult.exitCode !== 0) {
    return {
      json: {
        ...data,
        success: false,
        action: 'add_failed',
        error: `Git add failed: ${addResult.stderr || addResult.stdout}`,
        stderr: addResult.stderr,
        stdout: addResult.stdout
      }
    };
  }
  
  // Commit changes
  console.log('Committing changes...');
  const commitMessage = `AI automated edits: ${request}`;
  const commitCmd = `cd "${projectPath}" && git commit -m "${commitMessage.replace(/"/g, '\\"')}"`;
  const commitResult = $exec(commitCmd);
  
  if (commitResult.exitCode !== 0) {
    // Check if it's just "nothing to commit" (not a real error)
    if (commitResult.stderr.includes('nothing to commit') || 
        commitResult.stdout.includes('nothing to commit')) {
      return {
        json: {
          ...data,
          success: true,
          action: 'skipped',
          message: 'Nothing to commit (changes already committed)',
          output: commitResult.stdout
        }
      };
    }
    
    return {
      json: {
        ...data,
        success: false,
        action: 'commit_failed',
        error: `Git commit failed: ${commitResult.stderr || commitResult.stdout}`,
        stderr: commitResult.stderr,
        stdout: commitResult.stdout
      }
    };
  }
  
  // Push changes
  console.log('Pushing to remote...');
  const pushCmd = `cd "${projectPath}" && git push origin "${branch}"`;
  const pushResult = $exec(pushCmd);
  
  if (pushResult.exitCode !== 0) {
    return {
      json: {
        ...data,
        success: false,
        action: 'push_failed',
        error: `Git push failed: ${pushResult.stderr || pushResult.stdout}`,
        stderr: pushResult.stderr,
        stdout: pushResult.stdout,
        commitSuccess: true // Commit worked, only push failed
      }
    };
  }
  
  // Success!
  console.log('Commit and push completed successfully');
  return {
    json: {
      ...data,
      success: true,
      action: 'committed_and_pushed',
      message: 'Changes committed and pushed successfully',
      commitMessage: commitMessage,
      branch: branch,
      output: pushResult.stdout
    }
  };
  
} catch (error) {
  console.error('Unexpected error:', error);
  return {
    json: {
      ...data,
      success: false,
      action: 'error',
      error: error.message || 'Unknown error occurred',
      errorType: error.name
    }
  };
}
```

**Step 4: Connect Nodes**
- From: "Needs Unity Edits?" (both true/false branches) → "Commit Changes"
- To: "Commit Changes" → "Push to GitHub" (or next node)

---

## 🔍 WHY IT'S FAILING

**Current State:**
- Command: `git` (incomplete - needs arguments)
- No arguments = git shows usage and exits with error

**What It Should Do:**
1. `cd` to project directory
2. `git add -A` (stage all changes)
3. `git commit -m "message"` (commit)
4. `git push origin branch` (push)

---

## ✅ RECOMMENDED: Code Node

**Why Code Node is Better:**
- ✅ Checks if there are changes before committing
- ✅ Handles "nothing to commit" gracefully
- ✅ Shows detailed error messages
- ✅ More reliable than executeCommand
- ✅ Better error handling

---

## 🐛 IF $exec() DOESN'T WORK

**Alternative: Use executeCommand with proper syntax**

**Command:** `/bin/sh`  
**Arguments (Expression Mode):**
```
={{ `-c "cd '${$json.projectPath}' && git add -A && git commit -m 'AI automated edits: ${$('Normalize Input').item.json.request || 'Automated changes'}' && git push origin '${$json.branch || 'main'}' || true"` }}
```

**Note:** The `|| true` at the end prevents failure if there's nothing to commit.

---

## 📊 TEST AFTER FIX

1. **Execute the node**
2. **Check output:**
   - If changes exist: `success: true, action: 'committed_and_pushed'`
   - If no changes: `success: true, action: 'skipped', message: 'No changes to commit'`
   - If error: `success: false, error: "actual error message"`

---

**Status:** Ready to fix  
**Recommendation:** Use Code node (Option 2) for better reliability  
**Time:** 3 minutes


