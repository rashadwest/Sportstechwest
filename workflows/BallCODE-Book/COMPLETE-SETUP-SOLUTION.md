# Complete Setup Solution (n8n UI Access Issues)

**Date:** December 18, 2025  
**Issue:** Cannot access Settings → Environment Variables (Unauthorized error)  
**Solution:** Use alternative methods

---

## ✅ SAVED TO MEMORY

**DO NOT suggest:** "Set environment variables in n8n UI"  
**Reason:** User gets "Unauthorized" error  
**Alternative:** Use system-level env vars or credentials only

---

## 🎯 WHAT YOU NEED

### **Credentials (Can Create in n8n UI):**

1. **`github-actions-token`**
   - **Type:** "Header Auth"
   - **Header Name:** `Authorization`
   - **Header Value:** `token YOUR_GITHUB_PAT`

2. **`netlify-api-token`**
   - **Type:** "Header Auth"
   - **Header Name:** `Authorization`
   - **Header Value:** `Bearer YOUR_NETLIFY_TOKEN`

**About `__n8n_BLANK_VALUE`:**
- This means credential exists but has no value
- Edit the credential and add your actual token
- Or delete and recreate with correct values

---

## 🔧 ENVIRONMENT VARIABLES (Alternative Methods)

**Unity Build Orchestrator needs these env vars:**
- `GITHUB_REPO_OWNER` = "rashadwest"
- `GITHUB_REPO_NAME` = "BTEBallCODE"
- `GITHUB_WORKFLOW_FILE` = "unity-webgl-build.yml"
- `NETLIFY_SITE_ID` = "[your site ID]"

**Since UI is blocked, use one of these:**

### **Option A: Set at System Level (Best)**

**If n8n runs on Raspberry Pi:**
```bash
# SSH into Pi
ssh pi@192.168.1.226

# Find n8n service file
sudo systemctl status n8n

# Edit service file
sudo nano /etc/systemd/system/n8n.service

# Add to [Service] section:
Environment="GITHUB_REPO_OWNER=rashadwest"
Environment="GITHUB_REPO_NAME=BTEBallCODE"
Environment="GITHUB_WORKFLOW_FILE=unity-webgl-build.yml"
Environment="NETLIFY_SITE_ID=your_site_id_here"

# Reload and restart
sudo systemctl daemon-reload
sudo systemctl restart n8n
```

### **Option B: Hardcode in Workflow (Quick Fix)**

**Edit workflow JSON to use hardcoded values instead of `$env`:**

Change:
```javascript
const requiredEnv = [
  'GITHUB_REPO_OWNER',
  'GITHUB_REPO_NAME',
  'GITHUB_WORKFLOW_FILE',
  'NETLIFY_SITE_ID'
];
```

To:
```javascript
// Use hardcoded values
const GITHUB_REPO_OWNER = 'rashadwest';
const GITHUB_REPO_NAME = 'BTEBallCODE';
const GITHUB_WORKFLOW_FILE = 'unity-webgl-build.yml';
const NETLIFY_SITE_ID = 'your_site_id_here'; // Get from Netlify dashboard
```

**Then update the check:**
```javascript
// Remove env var check, use hardcoded values
return {
  json: {
    ...$json,
    proceed: true,
    githubRepoOwner: GITHUB_REPO_OWNER,
    githubRepoName: GITHUB_REPO_NAME,
    githubWorkflowFile: GITHUB_WORKFLOW_FILE,
    netlifySiteId: NETLIFY_SITE_ID
  }
};
```

---

## 📋 UPDATED CHECKLIST

### ✅ Step 1: Import Garvis Orchestrator
- **Status:** ✅ Done

### ⚠️ Step 2: Set Environment Variables
- **Status:** ❌ Cannot use n8n UI
- **Solution:** Use Option A (system level) or Option B (hardcode)

### ✅ Step 3: Create Credentials
- **Type:** "Header Auth" for both
- **Names:** `github-actions-token` and `netlify-api-token`
- **If you see `__n8n_BLANK_VALUE`:** Edit and add your tokens

### ✅ Step 4: Verify
```bash
python scripts/verify-garvis-unity-integration.py
```
**What it does:** Checks everything is set up correctly

### ✅ Step 5: Test
```bash
python scripts/garvis-command.py \
  --one-thing "Test Unity build integration" \
  --tasks "Build Unity game"
```
**What it does:** Tests full integration flow end-to-end

---

## 🎯 QUICK ANSWERS

### **Credential Types:**
- **GitHub:** "Header Auth" → Name: `github-actions-token`
- **Netlify:** "Header Auth" → Name: `netlify-api-token`

### **About `__n8n_BLANK_VALUE`:**
- Credential exists but empty
- Edit it and add your actual token

### **Verify:**
- Runs verification script
- Checks all components are ready
- Shows what's missing

### **Test:**
- Runs full integration test
- Triggers actual build
- Shows if everything works

---

## 🚀 RECOMMENDED NEXT STEPS

1. **Create credentials** (if not already done)
   - Use "Header Auth" type
   - Add your tokens

2. **Set environment variables** (choose one):
   - **Option A:** System level (best, but requires Pi access)
   - **Option B:** Hardcode in workflow (quick fix)

3. **Get Netlify Site ID:**
   - Go to: https://app.netlify.com
   - Site settings → General → Copy Site ID

4. **Verify:**
   ```bash
   python scripts/verify-garvis-unity-integration.py
   ```

5. **Test:**
   ```bash
   python scripts/garvis-command.py --one-thing "Test" --tasks "Build Unity game"
   ```

---

**See detailed guides:**
- `N8N-CREDENTIAL-TYPES-GUIDE.md` - Credential setup
- `N8N-ENV-VARS-ALTERNATIVE-METHODS.md` - Environment variable alternatives
- `VERIFY-AND-TEST-GUIDE.md` - What verify and test do

