# Netlify Automation Setup - Easy Deployment
## One Command to Deploy Everything

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 20, 2025  
**Goal:** Make Netlify deployment effortless  
**Status:** ✅ Ready to Use

---

## 🚀 THE SIMPLE SOLUTION

### **One Command:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/deploy-to-netlify.sh
```

**That's it!** This will:
1. ✅ Stage all changes
2. ✅ Commit with timestamp
3. ✅ Push to GitHub
4. ✅ Trigger Netlify deployment (if configured)
5. ✅ Done!

---

## ⚙️ SETUP (One-Time, 5 Minutes)

### **Step 1: Create Netlify Build Hook**

1. Go to: https://app.netlify.com
2. Select site: **ballcode.co**
3. Go to: **Site Settings** → **Build & deploy** → **Build hooks**
4. Click: **"Add build hook"**
5. **Name:** `BALLCODE Auto-Deploy`
6. **Branch:** `main`
7. Click: **"Save"**
8. **Copy the URL** (looks like: `https://api.netlify.com/build_hooks/xxxxx`)

### **Step 2: Set Environment Variable**

```bash
# Add to ~/.zshrc (permanent)
echo 'export NETLIFY_BUILD_HOOK="https://api.netlify.com/build_hooks/YOUR_HOOK_ID"' >> ~/.zshrc
source ~/.zshrc
```

**Or set temporarily:**
```bash
export NETLIFY_BUILD_HOOK="https://api.netlify.com/build_hooks/YOUR_HOOK_ID"
```

---

## 📋 USAGE

### **Basic Usage:**
```bash
./scripts/deploy-to-netlify.sh
```

### **With Custom Message:**
```bash
./scripts/deploy-to-netlify.sh "Book 2 curriculum integration"
```

### **What It Does:**
1. Checks for changes
2. Stages all files (`git add -A`)
3. Commits with message
4. Pushes to GitHub (`git push origin main`)
5. Triggers Netlify (if `NETLIFY_BUILD_HOOK` is set)
6. Reports completion

---

## ✅ ALTERNATIVE: Use Existing Script

**If you prefer the full script:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode
./deploy-ballcode-website.sh
```

**This provides:**
- More detailed logging
- Deployment reports
- Error handling
- Same Netlify trigger

---

## 🎯 RECOMMENDED WORKFLOW

### **After Making Changes:**
```bash
# 1. Make your changes (edit files)

# 2. Deploy (one command)
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/deploy-to-netlify.sh "Book 2 curriculum integration"

# 3. Wait 1-3 minutes

# 4. Check site: https://ballcode.co
```

**That's it!** No manual steps needed.

---

## 🔧 TROUBLESHOOTING

### **Netlify Not Triggering:**
```bash
# Check if variable is set
echo $NETLIFY_BUILD_HOOK

# If empty, set it:
export NETLIFY_BUILD_HOOK="https://api.netlify.com/build_hooks/YOUR_HOOK_ID"
```

### **Git Push Fails:**
- Check git credentials
- Verify remote is correct: `git remote -v`
- Check internet connection

### **No Changes Detected:**
- This is normal if nothing changed
- Script will exit cleanly

---

## 📊 WHAT GETS DEPLOYED

**The script deploys:**
- All HTML files
- All CSS files
- All JavaScript files
- All images/assets
- All changes in `BallCode/` directory

**To GitHub:** `origin/main` branch  
**To Netlify:** Auto-deploys from GitHub (or via build hook)

---

## 🚀 FUTURE: n8n Integration (Optional)

**For full automation, you can:**
1. Create n8n workflow that calls this script
2. Trigger via webhook: `POST /webhook/deploy-website`
3. Fully automated deployments

**Current:** Manual command (but super simple!)  
**Future:** Can be fully automated via n8n

---

## ✅ STATUS

**Script Created:** ✅ `scripts/deploy-to-netlify.sh`  
**Setup Required:** ⏳ Netlify Build Hook (5 minutes)  
**Ready to Use:** ✅ Yes (after setup)

---

**Next:** Set up Netlify Build Hook, then use `./scripts/deploy-to-netlify.sh` whenever you want to deploy!

