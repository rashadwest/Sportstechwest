# 🔧 Set n8n Environment Variables - Fix Missing UNITY_REPO_URL

**Problem:** `UNITY_REPO_URL not set` - Environment variables missing  
**Solution:** Set environment variables in n8n  
**Time:** 2 minutes

---

## 🎯 QUICK FIX

### Step 1: Open n8n Settings
1. Go to: **http://192.168.1.226:5678**
2. Click **Settings** (gear icon, top right)
3. Click **Environment Variables** (in left sidebar)

### Step 2: Add Environment Variables

**Add these 3 variables:**

#### Variable 1: UNITY_REPO_URL
- **Name:** `UNITY_REPO_URL`
- **Value:** `https://github.com/rashadwest/BallCode.git`
- **Click:** "Add" or "Save"

#### Variable 2: UNITY_PROJECT_PATH
- **Name:** `UNITY_PROJECT_PATH`
- **Value:** `/Users/rashadwest/BTEBallCODE`
- **Click:** "Add" or "Save"

#### Variable 3: WORKFLOW_PATH (if needed)
- **Name:** `WORKFLOW_PATH`
- **Value:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`
- **Click:** "Add" or "Save"

### Step 3: Save and Restart
1. **Save** all variables
2. **Restart n8n** (if required by your setup)
   - Or just refresh the workflow page

### Step 4: Test
1. Go back to your workflow
2. Execute "Get Git Variables" node
3. Should now show: `repoUrlSet: true, projectPathSet: true`

---

## 📋 COMPLETE ENVIRONMENT VARIABLES LIST

**Required Variables:**
- ✅ `UNITY_REPO_URL` = `https://github.com/rashadwest/BallCode.git`
- ✅ `UNITY_PROJECT_PATH` = `/Users/rashadwest/BTEBallCODE`

**Optional (for full workflow):**
- `WORKFLOW_PATH` = `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book`
- `GITHUB_REPO_OWNER` = `rashadwest`
- `GITHUB_REPO_NAME` = `BallCode`
- `GITHUB_WORKFLOW_FILE` = `your-workflow-file.yml`
- `NETLIFY_SITE_ID` = `your-netlify-site-id`
- `BUILD_OUTPUT_PATH` = `path/to/build/output`

---

## 🔍 HOW TO VERIFY

**After setting variables:**

1. **In n8n UI:**
   - Go to Settings → Environment Variables
   - You should see all variables listed

2. **In Workflow:**
   - Execute "Get Git Variables" node
   - Check output - should show:
     ```json
     {
       "repoUrl": "https://github.com/rashadwest/BallCode.git",
       "projectPath": "/Users/rashadwest/BTEBallCODE",
       "repoUrlSet": true,
       "projectPathSet": true,
       "error": null
     }
     ```

---

## 🐛 TROUBLESHOOTING

### Variables Not Showing Up?
- **Refresh the workflow page** after adding variables
- **Restart n8n** if variables still don't work
- **Check variable names** - must match exactly (case-sensitive)

### Still Getting "not set" Error?
- **Verify variable names** match exactly:
  - `UNITY_REPO_URL` (not `unity_repo_url` or `Unity_Repo_Url`)
  - `UNITY_PROJECT_PATH` (not `unity_project_path`)
- **Check for typos** in variable values
- **Make sure you saved** the variables

### Variables Set But Still Failing?
- **Check the path** - make sure `/Users/rashadwest/BTEBallCODE` exists
- **Check permissions** - n8n needs access to that directory
- **Check repository URL** - make sure it's accessible

---

## 📝 ALTERNATIVE: Set via Terminal (If UI Doesn't Work)

**If you can't set variables in n8n UI, use the Python script:**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python3 robot-set-n8n-env-vars.py
```

**This script:**
- Sets variables directly in n8n's SQLite database
- Works if UI method doesn't work
- Requires n8n database access

---

## ✅ AFTER SETTING VARIABLES

**Test the workflow:**
1. Execute "Get Git Variables" node
2. Should show: `repoUrlSet: true, projectPathSet: true, error: null`
3. Continue with "Update/Clone Repo" node
4. Should now work!

---

**Status:** Environment variables need to be set  
**Action:** Add variables in n8n Settings → Environment Variables  
**Time:** 2 minutes


