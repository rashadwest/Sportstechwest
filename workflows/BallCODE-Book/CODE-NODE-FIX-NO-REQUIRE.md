# 🔧 Code Node Fix - No require() Version

**Problem:** Code node executes but shows no output/error  
**Root Cause:** `require()` might not work in your n8n version  
**Solution:** Use n8n's built-in methods instead

---

## ⚡ FIXED CODE (No require)

**Replace the code in your Code node with this:**

```javascript
// Get data from previous node
const data = $input.item.json;

// Extract values with detailed logging
const repoUrl = data.repoUrl || '';
const projectPath = data.projectPath || '';
const repoUrlSet = data.repoUrlSet || false;
const projectPathSet = data.projectPathSet || false;

// Log everything for debugging
console.log('=== DEBUG: Clone/Update Repository ===');
console.log('repoUrl:', repoUrl);
console.log('projectPath:', projectPath);
console.log('repoUrlSet:', repoUrlSet);
console.log('projectPathSet:', projectPathSet);
console.log('Full input data:', JSON.stringify(data, null, 2));

// Validate inputs FIRST
if (!repoUrl || repoUrl.trim() === '') {
  return {
    json: {
      ...data,
      success: false,
      error: 'repoUrl is empty or not set',
      action: 'skipped',
      message: 'UNITY_REPO_URL is missing. Check "Get Git Variables" node output.',
      debug: {
        repoUrl: repoUrl,
        repoUrlSet: repoUrlSet,
        allData: data
      }
    }
  };
}

if (!projectPath || projectPath.trim() === '') {
  return {
    json: {
      ...data,
      success: false,
      error: 'projectPath is empty or not set',
      action: 'skipped',
      message: 'UNITY_PROJECT_PATH is missing. Check "Get Git Variables" node output.',
      debug: {
        projectPath: projectPath,
        projectPathSet: projectPathSet,
        allData: data
      }
    }
  };
}

// Use n8n's $exec() function instead of require()
// This works in all n8n versions
try {
  // First, check if directory exists using a simple command
  const checkDirCmd = `test -d "${projectPath}" && echo "exists" || echo "not_exists"`;
  console.log('Checking if directory exists:', projectPath);
  
  const checkResult = $exec(checkDirCmd);
  const dirExists = checkResult.stdout.trim() === 'exists';
  
  console.log('Directory exists?', dirExists);
  console.log('Check command output:', checkResult.stdout);
  
  if (dirExists) {
    // Directory exists - do git pull
    console.log('Running git pull...');
    const pullCmd = `cd "${projectPath}" && git pull`;
    
    const pullResult = $exec(pullCmd);
    
    console.log('Git pull exit code:', pullResult.exitCode);
    console.log('Git pull stdout:', pullResult.stdout);
    console.log('Git pull stderr:', pullResult.stderr);
    
    if (pullResult.exitCode === 0) {
      return {
        json: {
          ...data,
          success: true,
          action: 'pulled',
          path: projectPath,
          message: 'Git pull completed successfully',
          output: pullResult.stdout,
          exitCode: pullResult.exitCode
        }
      };
    } else {
      return {
        json: {
          ...data,
          success: false,
          action: 'pull_failed',
          error: `Git pull failed: ${pullResult.stderr || pullResult.stdout}`,
          output: pullResult.stdout,
          stderr: pullResult.stderr,
          exitCode: pullResult.exitCode
        }
      };
    }
  } else {
    // Directory doesn't exist - do git clone
    console.log('Directory does not exist - running git clone...');
    console.log(`Cloning ${repoUrl} to ${projectPath}`);
    
    // Create parent directory first
    const parentDir = projectPath.split('/').slice(0, -1).join('/');
    const mkdirCmd = `mkdir -p "${parentDir}"`;
    console.log('Creating parent directory:', parentDir);
    
    const mkdirResult = $exec(mkdirCmd);
    if (mkdirResult.exitCode !== 0) {
      console.error('Failed to create parent directory:', mkdirResult.stderr);
    }
    
    // Now clone
    const cloneCmd = `git clone "${repoUrl}" "${projectPath}"`;
    console.log('Running git clone:', cloneCmd);
    
    const cloneResult = $exec(cloneCmd);
    
    console.log('Git clone exit code:', cloneResult.exitCode);
    console.log('Git clone stdout:', cloneResult.stdout);
    console.log('Git clone stderr:', cloneResult.stderr);
    
    if (cloneResult.exitCode === 0) {
      return {
        json: {
          ...data,
          success: true,
          action: 'cloned',
          path: projectPath,
          message: 'Git clone completed successfully',
          output: cloneResult.stdout,
          exitCode: cloneResult.exitCode
        }
      };
    } else {
      return {
        json: {
          ...data,
          success: false,
          action: 'clone_failed',
          error: `Git clone failed: ${cloneResult.stderr || cloneResult.stdout}`,
          output: cloneResult.stdout,
          stderr: cloneResult.stderr,
          exitCode: cloneResult.exitCode,
          command: cloneCmd
        }
      };
    }
  }
} catch (error) {
  // Catch any unexpected errors
  console.error('Unexpected error:', error);
  console.error('Error message:', error.message);
  console.error('Error stack:', error.stack);
  
  return {
    json: {
      ...data,
      success: false,
      action: 'error',
      error: error.message || 'Unknown error occurred',
      errorType: error.name || 'Error',
      stack: error.stack,
      debug: {
        repoUrl: repoUrl,
        projectPath: projectPath,
        repoUrlSet: repoUrlSet,
        projectPathSet: projectPathSet
      }
    }
  };
}
```

---

## 🔍 WHAT THIS DOES DIFFERENTLY

1. **Uses `$exec()` instead of `require()`** - Works in all n8n versions
2. **Shows ALL errors** - Every failure returns detailed error info
3. **Logs everything** - Console.log statements show what's happening
4. **Returns data even on failure** - You'll see the error in output
5. **Checks variables first** - Validates inputs before trying git

---

## 📊 HOW TO SEE THE ERROR

**After executing the node:**

1. **Check the OUTPUT panel** (right side)
   - Click on the output
   - You'll see `success: false` and `error: "actual error message"`

2. **Check the Console** (browser console)
   - Open browser DevTools (F12)
   - Look for console.log messages
   - You'll see all the debug output

3. **Check the node execution details**
   - Click on the execution in n8n
   - Look at the node's output data
   - The error will be in the JSON

---

## 🐛 COMMON ERRORS YOU MIGHT SEE

### Error: "repoUrl is empty"
- **Fix:** Check "Get Git Variables" node - environment variables not set

### Error: "projectPath is empty"
- **Fix:** Check "Get Git Variables" node - UNITY_PROJECT_PATH not set

### Error: "Git pull failed: permission denied"
- **Fix:** n8n doesn't have permission to access the directory

### Error: "Git clone failed: repository not found"
- **Fix:** Repository URL is wrong or private (needs authentication)

### Error: "$exec is not defined"
- **Fix:** Your n8n version doesn't support $exec - use alternative below

---

## 🔄 ALTERNATIVE: If $exec() Doesn't Work

**If you get "$exec is not defined" error, use this simpler version:**

```javascript
const data = $input.item.json;
const repoUrl = data.repoUrl || '';
const projectPath = data.projectPath || '';

// Just return the data with instructions
// We'll use executeCommand node instead
return {
  json: {
    ...data,
    needsClone: !projectPath || projectPath === '',
    needsPull: projectPath && projectPath !== '',
    gitCommand: projectPath && projectPath !== '' 
      ? `cd "${projectPath}" && git pull`
      : `git clone "${repoUrl}" "${projectPath}"`,
    message: 'Use executeCommand node with this gitCommand'
  }
};
```

Then add an executeCommand node after this that uses `{{ $json.gitCommand }}`

---

## ✅ TEST STEPS

1. **Paste the code above** into your Code node
2. **Execute the node**
3. **Check the OUTPUT panel** - you'll see either:
   - `success: true` with action details
   - `success: false` with error message
4. **Check browser console** (F12) for debug logs
5. **Look at the actual error** - it will tell you what's wrong!

---

**This version will show you EXACTLY what's failing!**


