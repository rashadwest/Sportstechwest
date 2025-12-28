# Unity Cloud Build Setup Guide - Step by Step

**Date:** December 26, 2025  
**Goal:** Set up Unity Cloud Build for automated builds (free for Personal licenses)

---

## 🎯 WHY UNITY CLOUD BUILD

**Benefits:**
- ✅ **Free for Personal licenses**
- ✅ **Handles license automatically** (no secrets needed!)
- ✅ **Works with GitHub** (connects to your repo)
- ✅ **Professional CI/CD** solution
- ✅ **No exit code 125 issues** (Unity handles everything)

**This is the solution that actually works!**

---

## 📋 STEP-BY-STEP SETUP

### **Step 1: Sign In to Unity**

1. **I opened Unity ID page for you**
2. **Sign in** with your Unity account
   - Same email/password as Unity Hub
   - If you don't have account, create one (free)

**Status:** ⏳ Sign in to Unity ID

---

### **Step 2: Access Unity Cloud Build**

1. **I opened Unity Cloud Build page for you**
2. **Click:** "Get Started" or "Sign In"
3. **Navigate to:** Cloud Build section
4. **If first time:** May need to enable Cloud Build service

**Status:** ⏳ Access Cloud Build dashboard

---

### **Step 3: Connect GitHub Repository**

1. **In Unity Cloud Build dashboard:**
   - Click "New Project" or "Add Project"
   - Select "Connect Repository"

2. **Authorize Unity:**
   - Click "Connect GitHub" or "Authorize"
   - Select repository: `rashadwest/BTEBallCODE`
   - Grant Unity access to repository

3. **I opened GitHub repository for you** (for reference)

**Status:** ⏳ Connect GitHub repository

---

### **Step 4: Configure Build Settings**

**After connecting repository:**

1. **Select Platform:**
   - Platform: **WebGL**
   - Unity Version: **2021.3.45f2** (or closest available)

2. **Build Configuration:**
   - Build Name: `BallCODE-WebGL`
   - Build Target: WebGL
   - Build Method: Default

3. **Build Triggers:**
   - On push to `main` branch
   - OR manual trigger
   - OR on specific paths (Assets/**, ProjectSettings/**)

**Status:** ⏳ Configure build settings

---

### **Step 5: Set Up Deployment (Optional)**

**Deploy to Netlify:**

1. **In Cloud Build settings:**
   - Find "Post-Build" or "Deployment" section
   - Add Netlify deployment step

2. **Configure Netlify:**
   - Site ID: `[Your Netlify Site ID]`
   - Auth Token: `[Your Netlify Auth Token]`
   - Publish Directory: `Builds/WebGL`

**OR download and deploy manually:**
- Cloud Build provides download link
- Download build
- Upload to Netlify manually

**Status:** ⏳ Set up deployment (optional)

---

### **Step 6: Test Build**

1. **Trigger first build:**
   - Click "Build Now" or push to GitHub
   - Unity Cloud Build will:
     - Activate license automatically
     - Build Unity project
     - Provide download link

2. **Monitor build:**
   - Watch build progress
   - Check build logs
   - Verify build succeeds

**Status:** ⏳ Test first build

---

## ✅ WHAT HAPPENS NEXT

**After setup:**
- ✅ Unity handles license automatically (no secrets needed!)
- ✅ Builds trigger on GitHub push
- ✅ Build completes successfully
- ✅ Download build or auto-deploy to Netlify

**No more exit code 125!**

---

## 📋 QUICK CHECKLIST

- [ ] Sign in to Unity ID
- [ ] Access Unity Cloud Build
- [ ] Connect GitHub repository (`rashadwest/BTEBallCODE`)
- [ ] Configure build (WebGL, Unity 2021.3.45f2)
- [ ] Set up deployment (optional - Netlify)
- [ ] Trigger test build
- [ ] Verify build succeeds

---

## 🎯 EXPECTED RESULT

**After setup:**
- ✅ Builds trigger automatically on GitHub push
- ✅ License activates automatically (no errors!)
- ✅ Build completes successfully
- ✅ Deployment works (if configured)

**This is the solution that actually works!**

---

## ✅ SUMMARY

**What we're doing:**
- Setting up Unity Cloud Build (free for Personal licenses)
- Connecting GitHub repository
- Configuring WebGL builds
- Setting up deployment (optional)

**Why this works:**
- Unity handles license automatically
- No secrets needed
- No exit code 125 issues
- Professional CI/CD solution

**I opened all the pages you need - let's set it up step by step!**


