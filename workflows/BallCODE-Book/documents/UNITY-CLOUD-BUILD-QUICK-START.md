# Unity Cloud Build - Quick Start Guide

**Date:** December 26, 2025  
**Goal:** Set up Unity Cloud Build in 10-15 minutes

---

## 🎯 QUICK SETUP (Step by Step)

### **Step 1: Sign In to Unity**

1. **I opened Unity ID page for you**
2. **Sign in** with your Unity account
   - Email: [Your Unity email]
   - Password: [Your Unity password]
   - Same account as Unity Hub

**✅ Once signed in, proceed to Step 2**

---

### **Step 2: Access Unity Cloud Build**

1. **I opened Unity Cloud Build page for you**
2. **Click:** "Get Started" or "Sign In to Cloud Build"
3. **If first time:** You may need to enable Cloud Build service
   - Look for "Enable Cloud Build" or "Activate Cloud Build"
   - It's free for Personal licenses

**✅ Once Cloud Build dashboard is open, proceed to Step 3**

---

### **Step 3: Connect GitHub Repository**

1. **In Cloud Build dashboard:**
   - Click "New Project" or "+" button
   - Select "Connect Repository" or "Link GitHub Repository"

2. **Authorize Unity:**
   - Click "Authorize Unity" or "Connect GitHub"
   - Sign in to GitHub if needed
   - Authorize Unity to access your repositories

3. **Select Repository:**
   - Find: `rashadwest/BTEBallCODE`
   - Click to select it
   - Click "Connect" or "Link"

**✅ Once repository is connected, proceed to Step 4**

---

### **Step 4: Configure Build**

**After repository is connected:**

1. **Select Platform:**
   - Platform: **WebGL**
   - Unity Version: **2021.3.45f2** (or closest available - may show as 2021.3.x)

2. **Build Settings:**
   - Build Name: `BallCODE-WebGL`
   - Build Target: WebGL
   - Build Method: Default (or Auto)

3. **Build Triggers:**
   - ✅ On push to `main` branch
   - ✅ Manual trigger
   - Optional: Specific paths (Assets/**, ProjectSettings/**)

4. **Save Configuration:**
   - Click "Save" or "Create Build Configuration"

**✅ Once build is configured, proceed to Step 5**

---

### **Step 5: Set Up Deployment (Optional)**

**Deploy to Netlify automatically:**

1. **In Build Configuration:**
   - Find "Post-Build Actions" or "Deployment"
   - Click "Add Deployment" or "Configure Deployment"

2. **Add Netlify Deployment:**
   - Service: Netlify
   - Site ID: `[Your Netlify Site ID]` (from Netlify dashboard)
   - Auth Token: `[Your Netlify Auth Token]` (from Netlify)
   - Publish Directory: `Builds/WebGL`

**OR skip deployment:**
- Download build manually
- Upload to Netlify yourself

**✅ Once deployment is configured (or skipped), proceed to Step 6**

---

### **Step 6: Test Build**

1. **Trigger First Build:**
   - Click "Build Now" or "Start Build"
   - OR push a commit to GitHub (if auto-trigger enabled)

2. **Monitor Build:**
   - Watch build progress in Cloud Build dashboard
   - Check build logs
   - Wait for build to complete (~5-10 minutes)

3. **Verify Success:**
   - Build status: ✅ Success
   - Download link available
   - OR deployment to Netlify succeeded

**✅ Build successful = Setup complete!**

---

## 📋 WHAT YOU NEED

**Credentials:**
- ✅ Unity ID (email + password) - same as Unity Hub
- ✅ GitHub account access
- ✅ Netlify credentials (if auto-deploying)

**Repository:**
- ✅ `rashadwest/BTEBallCODE` - I opened this for you

**Build Settings:**
- ✅ Platform: WebGL
- ✅ Unity Version: 2021.3.45f2
- ✅ Build Target: WebGL

---

## ✅ EXPECTED RESULT

**After setup:**
- ✅ Builds trigger automatically on GitHub push
- ✅ License activates automatically (no errors!)
- ✅ Build completes successfully
- ✅ Download available or auto-deployed to Netlify

**No more exit code 125!**

---

## 🎯 QUICK CHECKLIST

- [ ] Step 1: Signed in to Unity ID
- [ ] Step 2: Cloud Build dashboard open
- [ ] Step 3: GitHub repository connected
- [ ] Step 4: Build configured (WebGL, 2021.3.45f2)
- [ ] Step 5: Deployment set up (optional)
- [ ] Step 6: Test build successful

---

## ✅ SUMMARY

**I opened all the pages you need:**
- ✅ Unity ID (sign in)
- ✅ Unity Cloud Build (set up)
- ✅ GitHub repository (reference)

**Follow the steps above - Unity Cloud Build handles license automatically!**

**This is the solution that actually works!**


