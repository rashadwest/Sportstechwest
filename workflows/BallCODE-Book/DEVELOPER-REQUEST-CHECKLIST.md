# Developer Request Checklist - BallCODE Netlify Deployment

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** Complete list of everything needed from developer to deploy BallCODE game to new Netlify account  
**Date:** January 2025  
**Status:** Ready to Share with Developer

---

## 📋 REQUEST SUMMARY

**What We Need:** WebGL build files and deployment information to set up BallCODE game on a new Netlify account  
**Why:** Moving deployment to new Netlify account without changing any code  
**Time Required from Developer:** 15-30 minutes  
**Code Changes Required:** ❌ NONE - Just need build files

---

## 🎯 PRIORITY 1: WebGL Build Files (REQUIRED)

### What We Need:

**Complete WebGL Build Folder**

**Location:** `Builds/WebGL/` (or wherever Unity outputs the WebGL build)

**Required Contents:**
- [ ] `index.html` - Main entry point
- [ ] `Build/` folder - Contains:
  - [ ] `.wasm` files (WebAssembly)
  - [ ] `.js` files (JavaScript)
  - [ ] `.data` files (game data)
  - [ ] `.unityweb` files (if used)
- [ ] `StreamingAssets/` folder - Contains:
  - [ ] `Levels/` folder with JSON level data files
  - [ ] Any other StreamingAssets content
- [ ] `TemplateData/` folder (if exists)
- [ ] Any other assets or configuration files

**How to Provide:**
- **Option A (Preferred):** Zip the entire `Builds/WebGL/` folder and share via:
  - Google Drive / Dropbox link
  - GitHub release / tag
  - Direct file transfer
- **Option B:** If build is already deployed, provide access to download from current Netlify
- **Option C:** If Unity project is accessible, we can build it ourselves (see below)

**File Size:** WebGL builds are typically 50-200MB, so a zip file is recommended

---

## 🔧 PRIORITY 2: Build Configuration (HELPFUL)

### Unity Build Settings Information:

**If you can provide these, it helps ensure consistency:**

- [ ] **Unity Version:** (e.g., Unity 2021.3.15f1)
- [ ] **WebGL Build Settings:**
  - [ ] Compression Format: (Gzip / Brotli / Disabled)
  - [ ] Code Optimization: (Size / Speed)
  - [ ] Memory Size: (e.g., 256MB)
  - [ ] Data Caching: (Enabled / Disabled)
- [ ] **Build Target:** WebGL
- [ ] **Any Custom WebGL Template Used:** (Default / Custom name)

**Why We Need This:**
- Ensures we can rebuild if needed in the future
- Helps troubleshoot any deployment issues
- Maintains consistency with current deployment

---

## 📁 PRIORITY 3: Current Deployment Information (OPTIONAL BUT HELPFUL)

### Current Netlify Deployment Details:

**If the game is currently deployed at `ballcode.netlify.app`:**

- [ ] **Current Netlify Site Name:** (e.g., `ballcode`)
- [ ] **Netlify Account Access:** (Optional - only if you want us to download directly)
- [ ] **Custom Domain:** (if any - e.g., `play.ballcode.co`)
- [ ] **Environment Variables:** (if any are set in Netlify)
- [ ] **Build Command:** (if any custom build command is used)
- [ ] **Publish Directory:** (usually `Builds/WebGL` or root)

**Why We Need This:**
- Can download build files directly from current deployment
- Ensures we match current configuration
- Helps with domain setup if needed

---

## 🔐 PRIORITY 4: Access & Credentials (OPTIONAL)

### GitHub Repository Access:

**Repository:** `https://github.com/rashadwest/BTEBallCODE`

**If you want us to build from source:**

- [ ] **GitHub Access:** (Personal Access Token or SSH key)
- [ ] **Branch to Build From:** (usually `main` or `development`)
- [ ] **Unity Project Path:** (if repo structure is complex)

**Note:** We already have read access to the repo, but may need write access if building from source

---

## 📝 PRIORITY 5: Documentation (HELPFUL)

### Any Existing Documentation:

- [ ] **Build Instructions:** (How to build WebGL from Unity)
- [ ] **Deployment Guide:** (If one exists)
- [ ] **Known Issues:** (Any deployment quirks or requirements)
- [ ] **Dependencies:** (Any external services, APIs, or requirements)
- [ ] **Environment Variables:** (If game needs any API keys or config)

---

## 🚀 PRIORITY 6: Testing & Verification (HELPFUL)

### Current Game Functionality:

**To ensure everything works after deployment:**

- [ ] **Test Checklist:** (What features should we test?)
- [ ] **Known Working Features:** (List of features that work in current deployment)
- [ ] **Known Issues:** (Any bugs or limitations)
- [ ] **Browser Compatibility:** (Which browsers are supported?)

---

## 📦 DELIVERY OPTIONS

### How Developer Can Provide Files:

**Option 1: File Sharing Service (Easiest)**
- Zip the `Builds/WebGL/` folder
- Upload to Google Drive, Dropbox, or similar
- Share download link

**Option 2: GitHub Release**
- Create a new release/tag in the repository
- Attach WebGL build zip as release asset
- We can download directly

**Option 3: Direct Transfer**
- If we have shared access, developer can place files in shared location
- Or use file transfer service (WeTransfer, etc.)

**Option 4: Current Netlify Access**
- If developer has access to current Netlify account
- Can download build files directly from there
- Or provide temporary access for us to download

**Option 5: Build Instructions**
- If Unity project is accessible
- Provide build instructions
- We can build it ourselves

---

## ✅ MINIMUM REQUIREMENTS (Must Have)

**To proceed with deployment, we MUST have:**

1. ✅ **WebGL Build Folder** - Complete `Builds/WebGL/` with all files
2. ✅ **Verification** - Confirmation that build works (currently deployed or tested)

**Everything else is helpful but not required.**

---

## 📋 REQUEST TEMPLATE (Copy & Send to Developer)

```
Hi [Developer Name],

I need to deploy the BallCODE game to a new Netlify account. To do this without 
changing any code, I need the following:

PRIORITY 1 - REQUIRED:
- Complete WebGL build folder (Builds/WebGL/) with all contents:
  - index.html
  - Build/ folder (with .wasm, .js, .data files)
  - StreamingAssets/ folder (with level data)
  - Any other assets

  Please zip the entire Builds/WebGL/ folder and share via:
  [Google Drive / Dropbox / GitHub Release / etc.]

PRIORITY 2 - HELPFUL:
- Unity version and build settings used
- Any custom configuration or environment variables

PRIORITY 3 - OPTIONAL:
- Access to current Netlify deployment (if you want us to download directly)
- Any deployment documentation or known issues

The goal is to deploy the exact same build to a new Netlify account - no code 
changes needed, just the build files.

Let me know the best way to get these files. Thanks!
```

---

## 🎯 WHAT WE'LL DO WITH THE FILES

**Once we receive the WebGL build:**

1. ✅ **Verify Build:** Check that all files are present
2. ✅ **Add Netlify Config:** Ensure `netlify.toml` is properly configured
3. ✅ **Deploy to Netlify:** Upload to new Netlify account
4. ✅ **Test Deployment:** Verify game loads and works correctly
5. ✅ **Configure Domain:** Set up custom domain if needed
6. ✅ **Documentation:** Update deployment docs with new URL

**No Code Changes:** We will NOT modify any Unity code, C# scripts, or project files. We're just deploying the existing build.

---

## ❓ FREQUENTLY ASKED QUESTIONS

### Q: Do you need the Unity project source code?
**A:** No, just the WebGL build files. We already have read access to the GitHub repo if needed.

### Q: Can you build it from the GitHub repo?
**A:** Yes, if you provide Unity build instructions and we have Unity installed. But it's easier if you provide the build files directly.

### Q: Will you change any code?
**A:** No, absolutely not. We're just deploying the existing build to a new Netlify account.

### Q: How long will this take?
**A:** Once we have the build files, deployment takes 10-15 minutes.

### Q: What if the build is already deployed?
**A:** If you can provide access to the current Netlify account, we can download the build files directly from there.

### Q: Do you need any API keys or credentials?
**A:** Only if the game uses external services. Please list any required API keys or environment variables.

---

## 📞 CONTACT INFORMATION

**If Developer Has Questions:**

- **Purpose:** Deploy existing BallCODE game to new Netlify account
- **Code Changes:** None required
- **Time Needed:** 15-30 minutes to prepare build files
- **Priority:** WebGL build folder is the only critical requirement

---

## ✅ CHECKLIST FOR DEVELOPER

**Developer can use this checklist:**

- [ ] Located `Builds/WebGL/` folder in Unity project
- [ ] Verified build folder contains:
  - [ ] `index.html`
  - [ ] `Build/` folder with game files
  - [ ] `StreamingAssets/` folder (if used)
- [ ] Zipped the entire `Builds/WebGL/` folder
- [ ] Shared zip file via preferred method
- [ ] (Optional) Provided Unity version and build settings
- [ ] (Optional) Provided current Netlify deployment info
- [ ] (Optional) Provided any documentation or known issues

---

## 🎯 SUMMARY

**What We Need:**
1. **WebGL Build Folder** (REQUIRED) - Complete `Builds/WebGL/` folder zipped
2. **Build Info** (HELPFUL) - Unity version and settings
3. **Deployment Info** (OPTIONAL) - Current Netlify details

**What We DON'T Need:**
- ❌ Unity source code (we have repo access if needed)
- ❌ Code changes or modifications
- ❌ Developer to deploy for us (we'll handle deployment)

**Goal:** Get the exact same build that's currently working, deploy it to new Netlify account, done!

---

**Status:** Ready to send to developer  
**Last Updated:** January 2025


