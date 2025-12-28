# Connect GitHub to Netlify - Step-by-Step Instructions
## Enable Auto-Deploy for Website

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 22, 2025  
**Purpose:** Connect `rashadwest/BallCode` repository to Netlify for automatic deployments

---

## 🎯 QUICK OVERVIEW

**What this does:**
- Connects your GitHub repository to Netlify
- Enables automatic deployments when you push code
- No manual deployment needed - Garvis pushes, Netlify auto-deploys

**Time needed:** 5 minutes

---

## 📋 STEP-BY-STEP INSTRUCTIONS

### **Step 1: Open Netlify Dashboard**

1. Go to: **https://app.netlify.com**
2. Log in with your account (`rashadlwest@gmail.com`)
3. You should see your sites (including `ballcode`)

---

### **Step 2: Select Your Website Site**

1. Find the site named **`ballcode`** (or your website site)
2. Click on it to open the site dashboard

---

### **Step 3: Open Site Settings**

1. Click **"Site settings"** (gear icon, usually in the top navigation or left sidebar)
2. You should see a menu on the left with different settings categories

---

### **Step 4: Go to Build & Deploy Settings**

1. In the left sidebar, click **"Build & deploy"**
2. You should see sections like:
   - Continuous Deployment
   - Build settings
   - Deploy settings

---

### **Step 5: Connect to Git Provider**

1. Under **"Continuous Deployment"**, you should see:
   - **"Link to Git provider"** button (if not connected)
   - OR **"Connected to Git"** (if already connected)

2. **If you see "Link to Git provider":**
   - Click **"Link to Git provider"**
   - Select **"GitHub"**
   - You'll be redirected to GitHub to authorize Netlify
   - Click **"Authorize Netlify"** (or similar)
   - Grant permissions if prompted

3. **If you see "Connected to Git":**
   - Check if it's connected to the right repository
   - If not, click **"Disconnect"** and reconnect

---

### **Step 6: Select Repository**

1. After authorizing, you'll see a list of your repositories
2. Find and select: **`rashadwest/BallCode`**
3. Click on it

---

### **Step 7: Configure Build Settings**

1. **Branch to deploy:** Select **`main`** (or `master` if that's your default branch)
2. **Build command:** Leave empty (or set to your build command if you have one)
   - For static sites, this is usually empty
3. **Publish directory:** Leave empty (or set to your output directory)
   - For static sites, this is usually empty or `dist/` or `public/`

**For BallCode website:**
- **Build command:** (leave empty - it's a static site)
- **Publish directory:** (leave empty - root directory)

---

### **Step 8: Save and Deploy**

1. Click **"Save"** or **"Deploy site"**
2. Netlify will start deploying your site
3. You'll see a deployment in progress

---

### **Step 9: Verify Connection**

1. Go back to **"Build & deploy"** settings
2. Under **"Continuous Deployment"**, you should see:
   - ✅ **"Connected to Git"**
   - Repository: `rashadwest/BallCode`
   - Branch: `main`

3. **Test it:**
   - Make a small change to your website
   - Push to GitHub: `git push origin main`
   - Check Netlify dashboard - you should see a new deployment start automatically!

---

## ✅ VERIFICATION CHECKLIST

After connecting, verify:

- [ ] Site shows "Connected to Git" in Netlify
- [ ] Repository shows `rashadwest/BallCode`
- [ ] Branch shows `main` (or your default branch)
- [ ] Auto-deploy is enabled
- [ ] Test deployment works (push a change and see it deploy)

---

## 🔧 TROUBLESHOOTING

### **Issue: "Repository not found"**

**Solution:**
- Make sure you authorized Netlify to access your repositories
- Check that `rashadwest/BallCode` exists and is accessible
- Try disconnecting and reconnecting

### **Issue: "Build failed"**

**Solution:**
- Check build settings (build command, publish directory)
- For static sites, these should usually be empty
- Check Netlify build logs for errors

### **Issue: "No deployments triggered"**

**Solution:**
- Make sure you're pushing to the correct branch (`main`)
- Check that auto-deploy is enabled in settings
- Verify the repository connection is active

### **Issue: "Can't find repository"**

**Solution:**
- Make sure the repository name is exactly: `rashadwest/BallCode`
- Check that you have access to the repository
- Try refreshing the repository list

---

## 🚀 AFTER CONNECTION

**Once connected:**

1. **Garvis can deploy automatically:**
   ```bash
   python scripts/garvis-deploy-all.py
   ```
   - Garvis pushes to GitHub
   - Netlify auto-deploys automatically!

2. **Manual deployment:**
   - Just push to GitHub: `git push origin main`
   - Netlify will deploy automatically

3. **No more manual drag & drop needed!**

---

## 📊 WHAT THIS ENABLES

**Before connection:**
- ❌ Manual deployment required
- ❌ Drag & drop files to Netlify
- ❌ No automatic updates

**After connection:**
- ✅ Automatic deployment on every push
- ✅ Garvis can deploy seamlessly
- ✅ No manual steps needed
- ✅ Deployment history tracked

---

## 🎯 QUICK REFERENCE

**Repository:** `rashadwest/BallCode`  
**Branch:** `main`  
**Build command:** (empty - static site)  
**Publish directory:** (empty - root)  
**Netlify site:** `ballcode` (or your site name)

---

**Version:** 1.0  
**Created:** December 22, 2025  
**Status:** Ready to use


