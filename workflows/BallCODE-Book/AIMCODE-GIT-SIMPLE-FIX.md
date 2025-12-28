# AIMCODE Simple Fix: Git Node - Direct Solution
## Simplest Working Code

**Date:** December 9, 2025  
**Issue:** Node still not running  
**Solution:** Use Code Node with JavaScript (More Reliable)

---

## CLEAR Framework

### C - Clarity
**Problem:** executeCommand node stuck/not running  
**Root Cause:** Shell command execution issues in n8n environment  
**Solution:** Use Code node with JavaScript (more reliable in n8n)

### L - Logic
**Better Approach:** JavaScript Code node can:
- Access environment variables directly
- Use Node.js built-in modules
- Better error handling
- More reliable execution

### E - Examples
**Code Node Pattern:** Use `$env.VARIABLE_NAME` directly in JavaScript

### A - Adaptation
**Change:** Convert from executeCommand to Code node

### R - Results
**Success:** Node executes reliably without getting stuck

---

## SOLUTION: Use Code Node Instead

### **Step 1: Change Node Type**

1. **Delete** the current "Clone/Update Repository" executeCommand node
2. **Add** a new **Code** node
3. **Name it:** "Clone/Update Repository"

### **Step 2: Paste This JavaScript Code**

```javascript
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Get environment variables
const repoUrl = $env.UNITY_REPO_URL;
const projectPath = $env.UNITY_PROJECT_PATH;

// Validate inputs
if (!repoUrl || !projectPath) {
  return {
    json: {
      success: false,
      error: 'Missing environment variables: UNITY_REPO_URL or UNITY_PROJECT_PATH',
      repoUrl: repoUrl || 'NOT SET',
      projectPath: projectPath || 'NOT SET'
    }
  };
}

try {
  // Check if directory exists
  const dirExists = fs.existsSync(projectPath) && fs.statSync(projectPath).isDirectory();
  
  if (dirExists) {
    // Directory exists - do git pull
    console.log(`Directory exists: ${projectPath}`);
    console.log('Running git pull...');
    
    execSync(`cd "${projectPath}" && git pull`, {
      stdio: 'inherit',
      cwd: projectPath
    });
    
    return {
      json: {
        success: true,
        action: 'pulled',
        path: projectPath,
        message: 'Git pull completed successfully'
      }
    };
  } else {
    // Directory doesn't exist - do git clone
    console.log(`Directory does not exist: ${projectPath}`);
    console.log(`Cloning repository: ${repoUrl}`);
    
    // Create parent directory if needed
    const parentDir = path.dirname(projectPath);
    if (!fs.existsSync(parentDir)) {
      fs.mkdirSync(parentDir, { recursive: true });
    }
    
    execSync(`git clone "${repoUrl}" "${projectPath}"`, {
      stdio: 'inherit'
    });
    
    return {
      json: {
        success: true,
        action: 'cloned',
        path: projectPath,
        message: 'Git clone completed successfully'
      }
    };
  }
} catch (error) {
  return {
    json: {
      success: false,
      action: 'failed',
      error: error.message,
      stderr: error.stderr?.toString() || '',
      stdout: error.stdout?.toString() || ''
    }
  };
}
```

---

## ALTERNATIVE: If You Must Use executeCommand

Try this **much simpler** version:

### **Command:** `git`

### **Arguments (NO Expression Mode - just plain text with template variables):**
```
clone {{ $env.UNITY_REPO_URL }} {{ $env.UNITY_PROJECT_PATH }} || (cd {{ $env.UNITY_PROJECT_PATH }} && git pull)
```

**Note:** This uses n8n's default template syntax `{{ }}` instead of Expression Mode.

---

## RECOMMENDED: Code Node Solution

**Why Code Node is Better:**
- ✅ More reliable in n8n
- ✅ Better error handling
- ✅ Direct access to environment variables
- ✅ Can check if directory exists before running git
- ✅ Clearer error messages

**Steps:**
1. Replace executeCommand node with Code node
2. Paste the JavaScript code above
3. Save and test

---

**Try the Code Node solution first - it's more reliable!**




