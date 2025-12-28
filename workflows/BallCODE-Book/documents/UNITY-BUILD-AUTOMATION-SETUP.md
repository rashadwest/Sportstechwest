# Unity Build Automation Setup (Formerly Cloud Build)

**Date:** December 26, 2025  
**Important:** Unity Cloud Build is now called "Unity Build Automation"  
**Location:** Unity Developer Dashboard → Services → Build Automation

---

## 🎯 WHERE TO FIND IT

**Unity Cloud Build is now called "Unity Build Automation" and is accessed through:**

1. **Unity Developer Dashboard:** https://dashboard.unity3d.com/
2. **Services Section:** Build Automation (formerly Cloud Build)
3. **OR Unity Editor:** Window → Services → Cloud Build

**It's NOT a separate website - it's part of Unity Dashboard!**

---

## 📋 STEP-BY-STEP SETUP

### **Step 1: Access Unity Developer Dashboard**

1. **I opened Unity Dashboard for you**
2. **Sign in** with your Unity ID
3. **Navigate to:** Projects section

**Status:** ⏳ Sign in to Unity Dashboard

---

### **Step 2: Create or Select Project**

**In Unity Dashboard:**

1. **If project doesn't exist:**
   - Click "New Project"
   - Name: `BTEBallCODE` or `BallCODE`
   - Organization: Select your organization (or create one)

2. **If project exists:**
   - Click on your project
   - Navigate to project dashboard

**Status:** ⏳ Project selected/created

---

### **Step 3: Enable Build Automation**

**In your project dashboard:**

1. **Look for:** "Services" section or "Build Automation" tile
2. **Click:** "Build Automation" or "Cloud Build" tile
3. **If first time:** Click "Set up Build Automation" or "Enable Build Automation"
4. **It's free for Personal licenses!**

**Status:** ⏳ Build Automation enabled

---

### **Step 4: Connect GitHub Repository**

**In Build Automation dashboard:**

1. **Click:** "Set up Cloud Build" or "Connect Repository"
2. **Select VCS:** GitHub
3. **Authorize Unity:**
   - Click "Authorize" or "Connect GitHub"
   - Sign in to GitHub if needed
   - Authorize Unity to access repositories

4. **Select Repository:**
   - Find: `rashadwest/BTEBallCODE`
   - Click to select
   - Click "Connect" or "Link"

**Status:** ⏳ GitHub repository connected

---

### **Step 5: Configure Build Target**

**After repository is connected:**

1. **Click:** "Add new build target" or "New Build Target"
2. **Configure:**
   - **Platform:** WebGL
   - **Unity Version:** 2021.3.45f2 (or closest available)
   - **Build Name:** `BallCODE-WebGL`
   - **Project Subfolder:** (leave empty if project is at root)

3. **Build Triggers:**
   - ✅ Auto-build on push to `main` branch
   - ✅ Manual trigger available

4. **Save Configuration**

**Status:** ⏳ Build target configured

---

### **Step 6: Set Up Deployment (Optional)**

**Deploy to Netlify:**

1. **In Build Target settings:**
   - Find "Post-Build Actions" or "Deployment"
   - Add Netlify deployment

2. **Configure Netlify:**
   - Site ID: `[Your Netlify Site ID]`
   - Auth Token: `[Your Netlify Auth Token]`
   - Publish Directory: `Builds/WebGL`

**OR skip deployment:**
- Download build manually
- Upload to Netlify yourself

**Status:** ⏳ Deployment configured (or skipped)

---

### **Step 7: Test Build**

1. **Trigger First Build:**
   - Click "Start Build" or "Build Now"
   - OR push a commit to GitHub (if auto-build enabled)

2. **Monitor Build:**
   - Watch build progress in Build Automation dashboard
   - Check build logs
   - Wait for completion (~5-10 minutes)

3. **Verify Success:**
   - Build status: ✅ Success
   - Download link available
   - OR deployment succeeded

**Status:** ⏳ Build successful

---

## 🎯 ALTERNATIVE: Access via Unity Editor

**If you can't find it in Dashboard:**

1. **Open Unity Editor** (with your project)
2. **Go to:** Window → General → Services
3. **In Services window:**
   - Click "Cloud Build" tab
   - Click "Open Cloud Build Dashboard"
   - This opens Build Automation in browser

**This is another way to access it!**

---

## ✅ WHAT THIS SOLVES

**Benefits:**
- ✅ **Free for Personal licenses**
- ✅ **Handles license automatically** (no secrets needed!)
- ✅ **Works with GitHub** (connects to your repo)
- ✅ **Professional CI/CD** solution
- ✅ **No exit code 125 issues** (Unity handles everything)

**This is the solution that actually works!**

---

## 📋 QUICK CHECKLIST

- [ ] Step 1: Signed in to Unity Dashboard
- [ ] Step 2: Project selected/created
- [ ] Step 3: Build Automation enabled
- [ ] Step 4: GitHub repository connected
- [ ] Step 5: Build target configured (WebGL, 2021.3.45f2)
- [ ] Step 6: Deployment set up (optional)
- [ ] Step 7: Test build successful

---

## ✅ SUMMARY

**Where to find it:**
- ✅ Unity Developer Dashboard: https://dashboard.unity3d.com/
- ✅ Services section → Build Automation
- ✅ OR Unity Editor → Window → Services → Cloud Build

**I opened Unity Dashboard for you - look for "Build Automation" or "Cloud Build" in the Services section!**


