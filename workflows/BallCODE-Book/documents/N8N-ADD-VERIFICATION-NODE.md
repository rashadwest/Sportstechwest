# Add Netlify Verification Node to n8n Workflow
## Quick Setup Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Status:** 🎯 Ready to Add

---

## 🎯 WHAT THIS DOES

Adds automatic Netlify deployment verification to your n8n workflow. After each deployment, it automatically checks if the deployment succeeded without requiring manual checks.

---

## ⚡ QUICK SETUP (5 Minutes)

### Step 1: Add Code Node

1. **Open n8n workflow:** `n8n-unity-automation-workflow-FINAL-WORKING.json`
2. **Find node:** "Deploy to Netlify"
3. **Add new node:** Click "+" after "Deploy to Netlify"
4. **Select:** "Code" node
5. **Name it:** "Verify Netlify Deployment"

---

### Step 2: Paste This Code

**Replace everything in the Code node editor with this:**

```javascript
// Get deployment info from previous node
const deployResponse = $input.item.json;
const deployId = deployResponse.id || deployResponse.deploy_id;

// Get environment variables
const siteId = $env.NETLIFY_SITE_ID;
const authToken = $env.NETLIFY_AUTH_TOKEN;
const workflowPath = $env.WORKFLOW_PATH || '/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book';

// Validate required variables
if (!siteId) {
  return {
    json: {
      ...deployResponse,
      verification: {
        success: false,
        error: 'NETLIFY_SITE_ID environment variable is not set'
      },
      deploymentVerified: false
    }
  };
}

if (!authToken) {
  return {
    json: {
      ...deployResponse,
      verification: {
        success: false,
        error: 'NETLIFY_AUTH_TOKEN environment variable is not set'
      },
      deploymentVerified: false
    }
  };
}

// Import required modules
const { execSync } = require('child_process');
const path = require('path');

// Set environment variables for script
const env = {
  ...process.env,
  NETLIFY_SITE_ID: siteId,
  NETLIFY_AUTH_TOKEN: authToken
};

if (deployId) {
  env.NETLIFY_DEPLOY_ID = deployId;
}

// Run verification script
const scriptPath = path.join(workflowPath, 'scripts', 'verify-netlify-deployment.py');

try {
  console.log('Running Netlify verification script...');
  console.log(`Script path: ${scriptPath}`);
  console.log(`Site ID: ${siteId}`);
  console.log(`Deploy ID: ${deployId || 'latest'}`);
  
  const result = execSync(`python3 "${scriptPath}" --json`, {
    encoding: 'utf8',
    stdio: 'pipe',
    env: env,
    cwd: workflowPath
  });
  
  const verification = JSON.parse(result);
  
  console.log('Verification result:', JSON.stringify(verification, null, 2));
  
  return {
    json: {
      ...deployResponse,
      verification: verification,
      deploymentVerified: verification.success === true,
      deploymentState: verification.state,
      siteUrl: verification.site_url || verification.deploy_url || deployResponse.siteUrl,
      verificationMessage: verification.success 
        ? `✅ Deployment verified successfully`
        : `❌ Deployment verification failed: ${verification.error || 'Unknown error'}`
    }
  };
} catch (error) {
  console.error('Verification script error:', error);
  
  // Try to parse error output
  let errorDetails = {
    message: error.message,
    stderr: error.stderr?.toString() || '',
    stdout: error.stdout?.toString() || ''
  };
  
  // Try to parse JSON from stdout if available
  if (error.stdout) {
    try {
      const parsed = JSON.parse(error.stdout.toString());
      errorDetails = { ...errorDetails, ...parsed };
    } catch (e) {
      // Not JSON, use as-is
    }
  }
  
  return {
    json: {
      ...deployResponse,
      verification: {
        success: false,
        error: error.message,
        errorDetails: errorDetails
      },
      deploymentVerified: false,
      verificationMessage: `❌ Verification failed: ${error.message}`
    }
  };
}
```

---

### Step 3: Connect Nodes

1. **From:** "Deploy to Netlify" → **To:** "Verify Netlify Deployment"
2. **From:** "Verify Netlify Deployment" → **To:** "Finalize & Prepare Report"

---

### Step 4: Update Report Node

**Open "Finalize & Prepare Report" node and update the code:**

**Find this line:**
```javascript
const report = {
  status: 'success',
  // ... existing code
};
```

**Replace with:**
```javascript
// Get verification results
const verification = $('Verify Netlify Deployment')?.item?.json?.verification || {};
const deploymentVerified = verification.success === true;

const report = {
  status: deploymentVerified ? 'success' : 'failed',
  timestamp: new Date().toISOString(),
  request: $('Normalize Input').item.json.request,
  triggerType: $('Normalize Input').item.json.triggerType,
  buildCompleted: true,
  deployCompleted: true,
  deploymentVerified: deploymentVerified,
  deploymentState: verification.state || 'unknown',
  siteUrl: verification.site_url || verification.deploy_url || ('https://' + ($env.NETLIFY_SITE_NAME || 'ballcode-game') + '.netlify.app'),
  message: deploymentVerified
    ? `✅ Deployment verified successfully. Site: ${verification.site_url || verification.deploy_url}`
    : `❌ Deployment verification failed: ${verification.error || 'Unknown error'}`,
  hasNotificationURL: !!$env.WEBHOOK_NOTIFICATION_URL,
  isWebhookTrigger: $('Normalize Input').item.json.triggerType === 'webhook' || $('Normalize Input').item.json.triggerType === 'github',
  verification: verification
};
```

---

### Step 5: Verify Environment Variables

**In n8n Settings → Environment Variables, make sure these are set:**

- ✅ `NETLIFY_SITE_ID` - Your Netlify site ID
- ✅ `NETLIFY_AUTH_TOKEN` - Your Netlify API token
- ✅ `WORKFLOW_PATH` - Path to workflow directory (optional, defaults to `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`)

---

### Step 6: Test

1. **Execute workflow manually** (click "Execute Workflow")
2. **Monitor execution:**
   - Check "Deploy to Netlify" completes
   - Check "Verify Netlify Deployment" runs
   - Check output shows verification results
3. **Check final report:**
   - Should include `deploymentVerified: true/false`
   - Should include `verification` object
   - Should include `siteUrl`

---

## ✅ VERIFICATION CHECKLIST

### Before Testing:
- [ ] Code node added after "Deploy to Netlify"
- [ ] Code pasted into node
- [ ] Nodes connected correctly
- [ ] Report node updated
- [ ] Environment variables set
- [ ] Python script exists and is executable

### After Testing:
- [ ] Workflow executes successfully
- [ ] Verification node runs
- [ ] Verification results appear in output
- [ ] Report includes verification status
- [ ] Success/failure is correctly reported

---

## 🐛 TROUBLESHOOTING

### Issue: "NETLIFY_SITE_ID is not set"

**Solution:**
1. Go to n8n Settings → Environment Variables
2. Add `NETLIFY_SITE_ID` with your site ID
3. Save and retry

---

### Issue: "NETLIFY_AUTH_TOKEN is not set"

**Solution:**
1. Go to n8n Settings → Environment Variables
2. Add `NETLIFY_AUTH_TOKEN` with your API token
3. Save and retry

---

### Issue: "Script not found" or "Python not found"

**Solution:**
1. Check `WORKFLOW_PATH` is set correctly
2. Verify script exists at: `{WORKFLOW_PATH}/scripts/verify-netlify-deployment.py`
3. Check Python 3 is installed: `python3 --version`
4. Make script executable: `chmod +x scripts/verify-netlify-deployment.py`

---

### Issue: Verification always fails

**Solution:**
1. Test script manually first:
   ```bash
   export NETLIFY_SITE_ID="your-site-id"
   export NETLIFY_AUTH_TOKEN="your-token"
   python3 scripts/verify-netlify-deployment.py --json
   ```
2. Check script output for errors
3. Verify API token has correct permissions
4. Check site ID is correct

---

## 📊 EXPECTED OUTPUT

### Successful Verification:
```json
{
  "verification": {
    "success": true,
    "deploy_id": "abc123",
    "state": "ready",
    "site_url": "https://ballcode-game.netlify.app",
    "deploy_url": "https://deploy-preview-123.netlify.app",
    "elapsed": 45.2
  },
  "deploymentVerified": true,
  "deploymentState": "ready",
  "siteUrl": "https://ballcode-game.netlify.app",
  "verificationMessage": "✅ Deployment verified successfully"
}
```

### Failed Verification:
```json
{
  "verification": {
    "success": false,
    "error": "Deployment failed",
    "state": "error"
  },
  "deploymentVerified": false,
  "deploymentState": "error",
  "verificationMessage": "❌ Deployment verification failed: Deployment failed"
}
```

---

## 🎯 NEXT STEPS

### After Adding Node:
1. Test workflow execution
2. Verify results appear correctly
3. Monitor for a few builds
4. Check verification success rate
5. Adjust timeout/polling if needed

---

**Version:** 1.0  
**Created:** December 12, 2025  
**Status:** Ready to Add


