# Setup Netlify Token for Restore Script

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 27, 2025  
**Status:** 🔧 **SETUP NEEDED**

---

## 🚨 ISSUE

**Script needs `NETLIFY_AUTH_TOKEN` to restore deployments.**

---

## ✅ QUICK SETUP

### Step 1: Get Netlify Token

1. **Go to:** https://app.netlify.com/user/applications
2. **Click:** "New access token"
3. **Name it:** "Garvis Restore" (or any name)
4. **Click:** "Generate token"
5. **Copy the token** (you'll only see it once!)

---

### Step 2: Add to ~/.zshrc

**Using the safe script:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
./scripts/safe-add-to-zshrc.sh NETLIFY_AUTH_TOKEN "your-token-here"
```

**Or manually:**
```bash
echo 'export NETLIFY_AUTH_TOKEN="your-token-here"' >> ~/.zshrc
source ~/.zshrc
```

---

### Step 3: Verify

```bash
echo $NETLIFY_AUTH_TOKEN
```

**Should show your token (not empty)**

---

### Step 4: Run Restore Script

```bash
cd /Users/rashadwest/BTEBallCODE
python3 scripts/garvis-restore-netlify-deployment.py
```

---

## 📋 ALTERNATIVE: Manual Restore (If Token Setup Fails)

**If you don't want to set up token:**

1. **Go to:** https://app.netlify.com/sites/ballcode/deploys
2. **Find** previous working deployment
3. **Click** on it
4. **Click** "Publish deploy" or "Restore"
5. **Done!**

**This works without any token setup!**

---

## ✅ SUMMARY

**Option 1: Set up token (for automation)**
- Get token from Netlify
- Add to ~/.zshrc
- Run script

**Option 2: Manual restore (fastest)**
- Go to Netlify dashboard
- Click restore on previous deployment
- Done!

---

**Status:** 🔧 **Choose Option 1 or 2** - Both work!

