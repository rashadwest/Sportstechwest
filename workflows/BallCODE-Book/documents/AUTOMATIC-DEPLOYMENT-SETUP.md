# Automatic Deployment Setup - Complete Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 27, 2025  
**Status:** ✅ Ready for Automatic Deployment

---

## 🎯 QUICK SETUP

**To enable automatic deployment, set these in your terminal:**

```bash
export NETLIFY_SITE_ID='39ebfb47-c716-4f38-8f8b-7bfba36f3dc7'
export NETLIFY_AUTH_TOKEN='your_token_here'
```

**Then deploy:**
```bash
cd /Users/rashadwest/BTEBallCODE
python3 scripts/deploy-only-netlify.py
```

---

## 📋 STEP-BY-STEP

### **Step 1: Get Netlify Auth Token**

1. Go to: https://app.netlify.com/user/applications
2. Click: "New access token"
3. Name: "Garvis Automation"
4. Copy the token

### **Step 2: Set Environment Variables**

**In your terminal:**
```bash
export NETLIFY_SITE_ID='39ebfb47-c716-4f38-8f8b-7bfba36f3dc7'
export NETLIFY_AUTH_TOKEN='your_token_here'
```

**Or add permanently to ~/.zshrc:**
```bash
echo 'export NETLIFY_SITE_ID="39ebfb47-c716-4f38-8f8b-7bfba36f3dc7"' >> ~/.zshrc
echo 'export NETLIFY_AUTH_TOKEN="your_token_here"' >> ~/.zshrc
source ~/.zshrc
```

### **Step 3: Deploy**

**Option A: Deploy existing build (fast):**
```bash
cd /Users/rashadwest/BTEBallCODE
python3 scripts/deploy-only-netlify.py
```

**Option B: Build + Deploy (full):**
```bash
cd /Users/rashadwest/BTEBallCODE
python3 scripts/garvis-unity-build-deploy.py
```

---

## ✅ WHAT HAPPENS

**Automatic Deployment:**
1. ✅ Checks for existing build
2. ✅ Creates zip package
3. ✅ Creates Netlify deploy via API
4. ✅ Uploads files via API
5. ✅ Publishes deploy automatically
6. ✅ Game goes live!

**No manual steps needed!**

---

## 🔍 VERIFY SETUP

**Check if variables are set:**
```bash
echo $NETLIFY_SITE_ID
echo $NETLIFY_AUTH_TOKEN
```

**Should show:**
- Site ID: `39ebfb47-c716-4f38-8f8b-7bfba36f3dc7`
- Token: `your_token_here`

---

## 🚀 GARVIS AUTOMATION

**Once set up, Garvis can:**
- ✅ Build Unity WebGL automatically
- ✅ Deploy to Netlify automatically
- ✅ No manual intervention needed
- ✅ Full automation from start to finish

---

## 📋 SCRIPT LOCATIONS

**Unity Project:**
- `scripts/garvis-unity-build-deploy.py` - Full build + deploy
- `scripts/deploy-only-netlify.py` - Deploy only (skip build)

**Both scripts use Netlify API for full automation!**

---

**Status:** ✅ Ready for automatic deployment once variables are set!

