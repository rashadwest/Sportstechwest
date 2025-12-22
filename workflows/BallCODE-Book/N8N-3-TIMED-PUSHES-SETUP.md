# n8n Setup: 3 Timed Pushes for Game Today

**Date:** December 11, 2025  
**Status:** ✅ Workflow Created - Ready to Import

---

## 🎯 What This Does

Automatically triggers 3 git pushes to the Unity game repository at specific times today:
- **Push 1:** 10:30 AM EST
- **Push 2:** 1:00 PM EST  
- **Push 3:** 5:00 PM EST

Each push will:
1. Pull latest changes from main branch
2. Commit any changes (if needed)
3. Push to main branch
4. Trigger GitHub Actions build automatically
5. Deploy to Netlify (via GitHub Actions)

---

## 📋 Setup Instructions

### Step 1: Import Workflow to n8n

1. Open n8n UI
2. Go to **Workflows** → **Import from File**
3. Select: `n8n-unity-3-timed-pushes-today.json`
4. Click **Import**

### Step 2: Configure Environment Variables

Make sure these are set in n8n Settings → Environment Variables:
- `UNITY_PROJECT_PATH` - Path to Unity project (e.g., `/Users/rashadwest/BTEBallCODE`)
- `UNITY_REPO_URL` - GitHub repository URL

### Step 3: Activate Workflow

1. Open the imported workflow
2. Click **Active** toggle to activate
3. Verify all 3 schedule triggers are enabled

### Step 4: Verify Schedule Times

The workflow is set for:
- **10:30 AM EST** (Push 1)
- **1:00 PM EST** (Push 2)
- **5:00 PM EST** (Push 3)

**Note:** Times are in server timezone. Adjust if n8n server is in different timezone.

---

## 🔧 Customize Times

To change the times, edit the cron expressions in the workflow:

- **10:30 AM:** `"30 10 * * *"` (minute hour day month weekday)
- **1:00 PM:** `"0 13 * * *"`
- **5:00 PM:** `"0 17 * * *"`

Cron format: `minute hour day-of-month month day-of-week`

---

## 📊 What Happens at Each Push

1. **Trigger fires** at scheduled time
2. **Prepare Push Data** - Determines push number and creates commit message
3. **Git pull** latest changes from main branch
4. **Git commit & push** - Commits any changes with message: "Automated build - Push X at [time]"
5. **Completion Report** - Logs success
6. **GitHub Actions** automatically triggers build (via git push)
7. **Netlify** automatically deploys when build completes

---

## ✅ Verification

After setup, you can:
1. Check n8n workflow execution history
2. Check GitHub Actions for build status
3. Check Netlify for deployment status
4. Verify game is live at your Netlify URL

---

## 🚨 Important Notes

- **One-time workflow:** This is configured for TODAY (December 11, 2025)
- **For recurring daily:** Modify cron to run daily or use the main Unity automation workflow
- **Git credentials:** Make sure n8n has access to push to GitHub (SSH keys or token)
- **Build time:** Each build takes ~10-15 minutes, so pushes are spaced 4 hours apart

---

**Status:** ✅ Ready to import and activate!


