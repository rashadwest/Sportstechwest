# AIMCODE Diagnosis: Code Node Failure
## Research-Based Solution for n8n Code Node Error

**Date:** December 9, 2025  
**Error:** `/bin/sh: syntax error: unexpected "("`  
**Issue:** JavaScript code being executed as shell command  
**Methodology:** AIMCODE with Web Research

---

## CLEAR Framework

### C - Clarity
**Problem:** Code node JavaScript is being executed as shell command  
**Error:** `/bin/sh: syntax error: unexpected "("`  
**Root Cause:** Node type mismatch or incorrect Code node configuration  
**Expected:** JavaScript executes in Node.js environment  
**Actual:** Code being passed to `/bin/sh` shell

### L - Logic
**Diagnosis Path:**
1. Node type might still be executeCommand (not Code)
2. Code node syntax might be incorrect
3. Environment variable access syntax might be wrong
4. n8n version compatibility issues

### E - Examples
**Need to Research:**
- Correct n8n Code node syntax
- How to access environment variables in Code nodes
- How to use execSync in n8n Code nodes

### A - Adaptation
**Constraints:** Must work in n8n Code node environment  
**Flexibility:** Can adjust syntax, use different approaches

### R - Results
**Success Criteria:**
- Code executes in Node.js (not shell)
- Environment variables accessible
- Git operations work correctly

---

## Research Phase

### Finding 1: n8n Code Node Syntax
**Research Needed:** How Code nodes work in n8n, correct syntax

### Finding 2: Environment Variables
**Research Needed:** Correct way to access `$env` in Code nodes

### Finding 3: execSync Usage
**Research Needed:** How to use child_process in n8n Code nodes

---

## Expert Consultation

### Hassabis (Systematic)
- Build solution layer by layer: Node Type → Syntax → Variables → Execution
- Verify each component before moving forward

### Jobs (Simplicity)
- Use simplest approach that works
- Avoid complex workarounds

---

## DIAGNOSIS

**The error `/bin/sh: syntax error` means:**
- The JavaScript code is being passed to a shell command
- This happens when the node is still `executeCommand` type, not `code` type
- OR the Code node is misconfigured

---

## SOLUTION

### **Step 1: Verify Node Type**

**In n8n UI:**
1. Click on "Clone/Update Repository" node
2. Check the node icon:
   - **Code node:** Shows `>_` icon
   - **Execute Command node:** Shows terminal/command icon
3. If it's still executeCommand, you need to:
   - **Delete** the executeCommand node
   - **Add** a new **Code** node
   - **Name it:** "Clone/Update Repository"

### **Step 2: Correct Code Node Syntax**

**For n8n Code nodes, use this corrected syntax:**

```javascript
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Get environment variables - CORRECT SYNTAX for n8n Code nodes
const repoUrl = process.env.UNITY_REPO_URL || $env.UNITY_REPO_URL;
const projectPath = process.env.UNITY_PROJECT_PATH || $env.UNITY_PROJECT_PATH;

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
    
    execSync(`git pull`, {
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

### **Step 3: Alternative - Use getWorkflowStaticData or getEnvironmentVariable**

**If `$env` doesn't work, try:**

```javascript
// Try different ways to get environment variables
const repoUrl = $env.UNITY_REPO_URL || 
                process.env.UNITY_REPO_URL || 
                getEnvironmentVariable('UNITY_REPO_URL');

const projectPath = $env.UNITY_PROJECT_PATH || 
                    process.env.UNITY_PROJECT_PATH || 
                    getEnvironmentVariable('UNITY_PROJECT_PATH');
```

---

## VERIFICATION CHECKLIST

**Before testing, verify:**
- [ ] Node type is **Code** (not executeCommand)
- [ ] Node icon shows `>_` (Code node icon)
- [ ] Code is in the JavaScript code field (not command/arguments)
- [ ] Environment variables are set in n8n Settings

---

**The most likely issue: The node is still an executeCommand node, not a Code node. Delete it and create a new Code node!**




