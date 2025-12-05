# BTEBallCODE Netlify Deployment Plan

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Repository:** https://github.com/rashadwest/BTEBallCODE  
**Status:** ✅ Repository Access Confirmed  
**Date:** January 2025

---

## 📋 Repository Analysis

### Current Repository Structure

**Repository Type:** Unity Source Project (not WebGL build)

**Contents:**
- ✅ Unity project files (Assets, ProjectSettings, Packages)
- ✅ WebGL configuration files present
- ✅ Addressable Assets configured for WebGL
- ❌ **No WebGL build files** (Builds folder not in repo - likely in .gitignore)

**Branches Available:**
- `main` (current)
- `development`
- `Dev-Merged`
- `Haseeb-branch`
- `Jimmy-branch`
- `action-tree`
- `karthik-branch`

---

## 🎯 Deployment Options

### Option 1: Deploy Existing WebGL Build (Recommended - No Code Changes)

**If the developer already has a WebGL build:**

1. **Locate the WebGL Build:**
   - Check if developer has `Builds/WebGL/` folder locally
   - Or check if it's deployed elsewhere (current `ballcode.netlify.app`)

2. **Get the Build Files:**
   - Ask developer for the WebGL build folder
   - Or download from current Netlify deployment
   - Or build from Unity project

3. **Deploy to Your New Netlify:**
   - Create new Netlify site
   - Upload WebGL build folder
   - Configure `netlify.toml` (already have template)
   - Done - no code changes needed!

---

### Option 2: Build from Source (If No Build Available)

**If you need to build from Unity:**

1. **Requirements:**
   - Unity Editor installed
   - Unity project opens successfully
   - WebGL build target configured

2. **Build Process:**
   - Open project in Unity
   - File → Build Settings → WebGL
   - Build to `Builds/WebGL/` folder
   - This creates the deployable files

3. **Then Deploy:**
   - Use Option 1 steps above

---

## 🚀 Step-by-Step: Deploy to New Netlify (Zero Code Changes)

### Step 1: Get WebGL Build Files

**Option A: From Developer**
- Ask developer to provide `Builds/WebGL/` folder
- Should contain: `index.html`, `Build/`, `StreamingAssets/`, etc.

**Option B: From Current Deployment**
- If `ballcode.netlify.app` is already live, download files from there
- Or ask developer for access to current Netlify account

**Option C: Build Locally (if Unity installed)**
```bash
# If you have Unity installed
# Open project in Unity
# File → Build Settings → WebGL → Build
# Output: Builds/WebGL/
```

---

### Step 2: Prepare Netlify Configuration

**Create `netlify.toml` in WebGL build folder:**

```toml
# Netlify Configuration for Unity WebGL Build
# BallCODE Game Deployment

[build]
  # Publish the WebGL build directory
  publish = "."

# Redirect all routes to index.html (for SPA routing and URL parameters)
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

# Security headers
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "SAMEORIGIN"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

# WebGL-specific headers for .wasm files
[[headers]]
  for = "/*.wasm"
  [headers.values]
    Content-Type = "application/wasm"
    Cross-Origin-Embedder-Policy = "require-corp"
    Cross-Origin-Opener-Policy = "same-origin"

# JavaScript files
[[headers]]
  for = "/*.js"
  [headers.values]
    Content-Type = "application/javascript"
    Cross-Origin-Embedder-Policy = "require-corp"

# Unity data files
[[headers]]
  for = "/*.data"
  [headers.values]
    Content-Type = "application/octet-stream"

# Unity web files
[[headers]]
  for = "/*.unityweb"
  [headers.values]
    Content-Type = "application/octet-stream"

# Cache static build assets (long cache)
[[headers]]
  for = "/Build/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

# Cache StreamingAssets (shorter cache for updates)
[[headers]]
  for = "/StreamingAssets/*"
  [headers.values]
    Cache-Control = "public, max-age=3600"
```

**Note:** This file already exists at `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Builds/WebGL/netlify.toml`

---

### Step 3: Deploy to Netlify

#### Method A: Netlify Dashboard (Easiest - No Code Changes)

1. **Go to Netlify:** https://app.netlify.com
2. **Sign up / Log in** (use GitHub account for easiest setup)
3. **Add New Site:**
   - Click "Add new site"
   - Select "Deploy manually" or "Import an existing project"
4. **Upload WebGL Build:**
   - Drag and drop your `Builds/WebGL/` folder
   - Or use "Browse to upload"
5. **Deploy:**
   - Netlify will automatically detect `netlify.toml` if it's in the folder
   - Click "Deploy site"
6. **Done!**
   - You'll get a URL like: `ballcode-xxxxx.netlify.app`
   - Site is live immediately

---

#### Method B: Netlify CLI (If You Prefer Command Line)

```bash
# 1. Install Netlify CLI (if not installed)
npm install -g netlify-cli

# 2. Login to Netlify
netlify login

# 3. Navigate to WebGL build directory
cd /path/to/Builds/WebGL

# 4. Deploy
netlify deploy --prod

# Follow prompts to create new site or link existing
```

---

#### Method C: Git Integration (For Future Updates)

**If you want auto-deploy from GitHub:**

1. **Create WebGL Build Branch/Folder:**
   - Create a separate branch or folder for WebGL builds
   - Push WebGL build files to that location

2. **Connect to Netlify:**
   - In Netlify: Add new site → Import from Git
   - Select `rashadwest/BTEBallCODE`
   - Choose the branch/folder with WebGL build

3. **Configure Build Settings:**
   - Build command: (leave empty - already built)
   - Publish directory: `Builds/WebGL` (or wherever build is)

4. **Deploy:**
   - Netlify will deploy automatically
   - Future pushes to that branch will auto-deploy

---

### Step 4: Verify Deployment

**Checklist:**
- [ ] Site loads at Netlify URL
- [ ] Game loads and plays correctly
- [ ] All assets load (images, sounds, etc.)
- [ ] No console errors in browser
- [ ] WebGL files load correctly (.wasm, .data, .js)

**Test URL:** `https://your-site-name.netlify.app`

---

## 🔄 Keeping It the Same (No Developer Changes Needed)

### What We're NOT Changing:
- ✅ No Unity source code changes
- ✅ No C# script modifications
- ✅ No project settings changes
- ✅ No asset changes
- ✅ No build process changes (if using existing build)

### What We ARE Doing:
- ✅ Deploying existing WebGL build to new Netlify account
- ✅ Using proper `netlify.toml` configuration
- ✅ Setting up headers for WebGL files
- ✅ Configuring redirects for SPA routing

---

## 📝 Next Steps

### Immediate Actions:

1. **Get WebGL Build:**
   - [ ] Ask developer for `Builds/WebGL/` folder
   - [ ] OR download from current `ballcode.netlify.app`
   - [ ] OR build from Unity if you have access

2. **Set Up Netlify Account:**
   - [ ] Sign up at netlify.com
   - [ ] Verify email if needed

3. **Deploy:**
   - [ ] Upload WebGL build folder
   - [ ] Verify `netlify.toml` is included
   - [ ] Deploy site

4. **Test:**
   - [ ] Visit Netlify URL
   - [ ] Test game functionality
   - [ ] Verify all features work

---

## 🎯 Questions to Answer

Before proceeding, please confirm:

1. **Do you have the WebGL build files?**
   - [ ] Yes - I have the `Builds/WebGL/` folder
   - [ ] No - Need to get from developer
   - [ ] No - Need to build from Unity

2. **Where is the current game deployed?**
   - [ ] `ballcode.netlify.app` (current Netlify)
   - [ ] Different URL: _______________
   - [ ] Not deployed yet

3. **Do you have Unity installed?**
   - [ ] Yes - Can build locally
   - [ ] No - Need developer to build

4. **What's your Netlify account status?**
   - [ ] Already have account
   - [ ] Need to create account
   - [ ] Need help setting up

---

## 📚 Reference Files

**Existing Configuration Files:**
- `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Builds/WebGL/netlify.toml` - Netlify config template
- `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/WEBGL-NETLIFY-DEPLOYMENT-GUIDE.md` - Full deployment guide
- `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode/netlify.toml` - Website Netlify config

**Repository:**
- https://github.com/rashadwest/BTEBallCODE - Unity source project

---

## ✅ Summary

**Goal:** Deploy BallCODE game to your new Netlify account without changing developer's code

**Approach:**
1. Get WebGL build files (from developer or current deployment)
2. Create new Netlify site
3. Upload WebGL build folder
4. Deploy - done!

**No Code Changes Required:** ✅  
**Developer Involvement:** Minimal (just need build files)  
**Time Required:** 10-15 minutes

---

**Status:** Ready to proceed once WebGL build files are available  
**Last Updated:** January 2025


