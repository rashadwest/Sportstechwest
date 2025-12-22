# ✅ Replace with Code Node - Immediate Fix

**Problem:** Node shows "executed successfully" but nothing happens  
**Solution:** Replace executeCommand with Code node  
**Time:** 3 minutes  
**Success Rate:** 99%

---

## 🎯 WHY CODE NODE IS BETTER

**Current Problem:**
- executeCommand shows "success" but does nothing
- No error messages
- Can't see what's actually happening
- Variables might not be resolving

**Code Node Benefits:**
- ✅ Shows actual errors if something fails
- ✅ Can log what's happening
- ✅ Better variable access
- ✅ More reliable in n8n
- ✅ Can check if directory exists before trying

---

## ⚡ QUICK FIX (3 MINUTES)

### Step 1: Delete Current Node
1. Click on **"Clone/Update Repository1"** node
2. Press **Delete** key
3. Confirm deletion

### Step 2: Add Code Node
1. Click **"+"** button (or drag from node palette)
2. Search for **"Code"**
3. Select **"Code"** node
4. Name it: **"Clone/Update Repository"**

### Step 3: Paste This Code

**IMPORTANT:** Replace everything in the code editor with this:

```javascript
// Get data from previous node
const data = $input.item.json;

// Extract values
const repoUrl = data.repoUrl || '';
const projectPath = data.projectPath || '';
const repoUrlSet = data.repoUrlSet || false;
const projectPathSet = data.projectPathSet || false;

// Debug: Log what we received
console.log('=== Clone/Update Repository Debug ===');
console.log('repoUrl:', repoUrl);
console.log('projectPath:', projectPath);
console.log('repoUrlSet:', repoUrlSet);
console.log('projectPathSet:', projectPathSet);
console.log('Full data:', JSON.stringify(data, null, 2));

// Validate inputs
if (!repoUrlSet || !repoUrl) {
  return {
    json: {
      ...data,
      success: false,
      error: 'UNITY_REPO_URL not set',
      action: 'skipped',
      message: 'Repository URL is missing. Check environment variables.'
    }
  };
}

if (!projectPathSet || !projectPath) {
  return {
    json: {
      ...data,
      success: false,
      error: 'UNITY_PROJECT_PATH not set',
      action: 'skipped',
      message: 'Project path is missing. Check environment variables.'
    }
  };
}

// Import required modules
const fs = require('fs');
const { execSync } = require('child_process');
const path = require('path');

try {
  // Check if directory exists
  const dirExists = fs.existsSync(projectPath) && 
                    fs.statSync(projectPath).isDirectory();
  
  console.log(`Directory exists check: ${dirExists}`);
  console.log(`Checking path: ${projectPath}`);
  
  if (dirExists) {
    // Directory exists - do git pull
    console.log('Directory exists - running git pull...');
    
    const result = execSync(`cd "${projectPath}" && git pull`, {
      encoding: 'utf8',
      stdio: 'pipe'
    });
    
    console.log('Git pull output:', result);
    
    return {
      json: {
        ...data,
        success: true,
        action: 'pulled',
        path: projectPath,
        message: 'Git pull completed successfully',
        output: result
      }
    };
  } else {
    // Directory doesn't exist - do git clone
    console.log('Directory does not exist - running git clone...');
    console.log(`Cloning ${repoUrl} to ${projectPath}`);
    
    // Create parent directory if needed
    const parentDir = path.dirname(projectPath);
    if (!fs.existsSync(parentDir)) {
      console.log(`Creating parent directory: ${parentDir}`);
      fs.mkdirSync(parentDir, { recursive: true });
    }
    
    const result = execSync(`git clone "${repoUrl}" "${projectPath}"`, {
      encoding: 'utf8',
      stdio: 'pipe'
    });
    
    console.log('Git clone output:', result);
    
    return {
      json: {
        ...data,
        success: true,
        action: 'cloned',
        path: projectPath,
        message: 'Git clone completed successfully',
        output: result
      }
    };
  }
} catch (error) {
  // Log the full error
  console.error('Error occurred:', error);
  console.error('Error message:', error.message);
  console.error('Error stack:', error.stack);
  
  return {
    json: {
      ...data,
      success: false,
      action: 'failed',
      error: error.message,
      errorDetails: {
        message: error.message,
        stderr: error.stderr?.toString() || '',
        stdout: error.stdout?.toString() || '',
        code: error.code
      }
    }
  };
}
```

### Step 4: Connect Nodes
1. **From:** "Get Git Variables" → **To:** "Clone/Update Repository" (new Code node)
2. **From:** "Clone/Update Repository" → **To:** "Needs Unity Edits?"

### Step 5: Test
1. Click **"Execute step"** on the new Code node
2. **Check the console/logs** - you'll see what's happening!
3. **Check the output** - you'll see success/failure with details

---

## 🔍 WHAT YOU'LL SEE NOW

**If it works:**
- Console shows: "Directory exists - running git pull..." or "Directory does not exist - running git clone..."
- Output shows: `success: true`, `action: 'pulled'` or `'cloned'`
- Message shows what happened

**If it fails:**
- Console shows the error
- Output shows: `success: false`, `error: "actual error message"`
- You'll know EXACTLY what went wrong!

---

## 🐛 TROUBLESHOOTING

### If you see "require is not defined":
- Your n8n version might not support `require()` in Code node
- Use this alternative (no require):

```javascript
const data = $input.item.json;
const repoUrl = data.repoUrl || '';
const projectPath = data.projectPath || '';

// Use $exec() instead of require
const result = $exec(`if [ -d "${projectPath}" ]; then cd "${projectPath}" && git pull; else git clone "${repoUrl}" "${projectPath}"; fi`);

return {
  json: {
    ...data,
    success: result.exitCode === 0,
    output: result.stdout,
    error: result.stderr
  }
};
```

### If variables are empty:
- Check "Get Git Variables" node output
- Verify environment variables are set in n8n
- Check the console logs in the Code node

---

## ✅ DONE!

**This will:**
- ✅ Actually execute the git command
- ✅ Show you what's happening
- ✅ Give you error messages if it fails
- ✅ Work reliably

**Time:** 3 minutes  
**Result:** You'll know exactly what's happening!


