# Phase 1: Netlify Setup Guide
## Complete Setup for Netlify Site and WebGL Deployment

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 5, 2025  
**Purpose:** Set up Netlify account, get WebGL build, deploy to Netlify, and configure credentials  
**Time:** 15-20 minutes  
**Status:** Ready to follow

---

## 🎯 What You're Setting Up

**Netlify** = Website hosting service (where your Unity WebGL game will live)  
**WebGL Build** = Unity game built for web browsers  
**GitHub Actions** = Automated build system (builds WebGL in the cloud - **EASIEST OPTION!**)

**Goal:** 
1. Create Netlify account
2. Get WebGL build (using GitHub Actions - no local Unity WebGL module needed!)
3. Deploy to Netlify
4. Get credentials for automation
5. Add credentials to GitHub Secrets

---

## 📋 STEP 1: Create Netlify Account (5 minutes)

### Option A: Sign Up with Email (Recommended)

1. **Go to Netlify:** https://app.netlify.com/signup
2. **Choose "Sign up with email"**
3. **Enter your information:**
   - Email: [Your email address]
   - Password: [Create a strong password]
   - Full name: Rashad West
4. **Click "Sign up"**
5. **Check your email** for verification link
6. **Click verification link** in email
7. **You're in!** You'll see the Netlify dashboard

### Option B: Sign Up with GitHub (If you have GitHub account)

1. **Go to Netlify:** https://app.netlify.com/signup
2. **Click "Sign up with GitHub"**
3. **Authorize Netlify** to access your GitHub
4. **You're in!** Netlify will automatically connect to your GitHub

**✅ Checkpoint:** You have a Netlify account and are logged in

---

## 📋 STEP 2: Get WebGL Build - **OPTION 1: GitHub Actions (EASIEST!)** ⭐

**Best for:** No local Unity WebGL module needed, automated builds

If you see "No WebGL module loaded" in Unity Build Settings, this is the **easiest solution**!

### Why GitHub Actions?

- ✅ **No local WebGL module needed** - Builds in the cloud
- ✅ **Automated** - Just push code or click a button
- ✅ **Already configured** - You have the workflow file ready
- ✅ **Auto-deploys** - Can deploy directly to Netlify

### Step 2.1: Verify Unity Project is on GitHub

1. **Check if your Unity project is on GitHub:**
   - Repository should be: `rashadwest/BTEBallCODE` (or your Unity repo)
   - If not on GitHub, push it there first

2. **Verify workflow file exists:**
   - Go to: `https://github.com/rashadwest/BTEBallCODE` (or your repo)
   - Navigate to: `.github/workflows/` folder
   - Look for: `unity-webgl-build.yml`
   - **If missing:** See `PHASE-2-GITHUB-ACTIONS-SETUP.md` to create it

### Step 2.2: Configure GitHub Secrets (Required for Build)

**Before building, you need these secrets in GitHub:**

1. **Go to GitHub Repository:**
   - Navigate to: `https://github.com/rashadwest/BTEBallCODE` (or your repo)
   - Click **Settings** → **Secrets and variables** → **Actions**

2. **Add Required Secrets:**

   **a. UNITY_LICENSE (if using Unity Pro):**
   - Click **"New repository secret"**
   - Name: `UNITY_LICENSE`
   - Value: Your Unity license (get from Unity account if needed)
   - Click **"Add secret"**
   - **Note:** If using Unity Personal (free), you may not need this

   **b. NETLIFY_AUTH_TOKEN:**
   - We'll get this in Step 4 (after Netlify site is created)
   - For now, skip this - we'll come back to it

   **c. NETLIFY_SITE_ID:**
   - We'll get this in Step 4 (after Netlify site is created)
   - For now, skip this - we'll come back to it

**✅ Checkpoint:** GitHub repository ready, workflow file exists (or will be created in Phase 2)

### Step 2.3: Build WebGL Using GitHub Actions

**Option A: Manual Trigger (Easiest for First Build)**

1. **Go to GitHub Repository:**
   - Navigate to: `https://github.com/rashadwest/BTEBallCODE` (or your repo)
   - Click **Actions** tab

2. **Select Workflow:**
   - Click **"Unity WebGL Build and Deploy"** workflow (on left sidebar)

3. **Run Workflow:**
   - Click **"Run workflow"** button (top right)
   - Select branch: `main` (or your default branch)
   - Click green **"Run workflow"** button

4. **Wait for Build:**
   - Build takes **10-15 minutes**
   - Watch progress in the Actions tab
   - You'll see steps: Checkout → Setup Unity → Build → Upload artifacts

5. **Download Build:**
   - When build completes, scroll down to **"Artifacts"** section
   - Click **"webgl-build"** to download
   - Extract the zip file
   - You now have `Builds/WebGL/` folder with your WebGL build!

**Option B: Push to Trigger (For Future Builds)**

- Just push code to `main` branch
- GitHub Actions will automatically build
- No manual trigger needed

**✅ Checkpoint:** You have a WebGL build (either downloaded from GitHub Actions or built locally)

---

## 📋 STEP 2 ALTERNATIVE: Get WebGL Build - Other Options

### Option 2: Install WebGL Module Locally

**If you prefer to build locally:**

1. **In Unity Build Settings:**
   - Click **"Install with Unity Hub"** button
   - Unity Hub will open
   - Click **"Install"** next to WebGL module
   - Wait for download (~500MB-1GB)
   - Restart Unity Editor

2. **Build WebGL:**
   - File → Build Settings
   - Select WebGL platform
   - Click **"Build"**
   - Choose output: `Builds/WebGL/`
   - Wait for build to complete

**Time:** ~15-30 minutes (download + build)

### Option 3: Get Build from Developer

**If someone else has the build:**

1. **Request WebGL build:**
   - Ask developer to zip `Builds/WebGL/` folder
   - See `EMAIL-TO-DEVELOPER-TEMPLATE.md` for email template

2. **Receive and extract:**
   - Download zip file
   - Extract to your project folder
   - You now have `Builds/WebGL/` folder

**✅ Checkpoint:** You have a WebGL build folder ready

---

## 📋 STEP 3: Deploy to Netlify (5 minutes)

### Step 3.1: Prepare Build Folder

**Ensure you have:**
- `Builds/WebGL/` folder with:
  - `index.html`
  - `Build/` folder (with .wasm, .js, .data files)
  - `StreamingAssets/` folder (if used)

### Step 3.2: Deploy via Netlify Dashboard (Easiest)

1. **Go to Netlify Dashboard:**
   - https://app.netlify.com
   - Make sure you're logged in

2. **Add New Site:**
   - Click **"Add new site"** button
   - Choose **"Deploy manually"**

3. **Upload Build:**
   - Drag and drop your `Builds/WebGL/` folder
   - OR click **"Browse to upload"** and select the folder
   - Wait for upload (~1-2 minutes)

4. **Site is Live!**
   - Netlify will show you the site URL
   - Example: `https://random-name-12345.netlify.app`
   - You can change the site name in Settings

**✅ Checkpoint:** Your WebGL game is deployed and live on Netlify!

### Step 3.3: (Optional) Add JavaScript Bridge

**If you need book integration:**

1. **Open:** `Builds/WebGL/index.html`
2. **Add JavaScript bridge** (before `</body>` tag)
3. **See:** `UNITY-WEBGL-BUILD-GUIDE.md` Step 4 for bridge code
4. **Redeploy** to Netlify (drag and drop again)

---

## 📋 STEP 4: Get Netlify Credentials (5 minutes)

**These are needed for GitHub Actions automation**

### Step 4.1: Get Netlify Site ID

1. **Go to Netlify Dashboard:**
   - https://app.netlify.com
   - Click on your site

2. **Find Site ID:**
   - Go to **Settings** → **General**
   - Scroll to **"Site details"** section
   - Copy **"Site ID"** (looks like: `abc123-def456-ghi789`)
   - **Save this** - you'll need it for GitHub Secrets

### Step 4.2: Get Netlify Auth Token

1. **Go to Netlify Dashboard:**
   - Click your profile icon (top right)
   - Click **"User settings"**

2. **Generate Access Token:**
   - Go to **"Applications"** tab
   - Scroll to **"Personal access tokens"** section
   - Click **"New access token"**
   - **Description:** "GitHub Actions Unity Build"
   - Click **"Generate token"**
   - **⚠️ IMPORTANT:** Copy the token immediately (you won't see it again!)
   - **Save this** - you'll need it for GitHub Secrets

**✅ Checkpoint:** You have:
- Netlify Site ID
- Netlify Auth Token

---

## 📋 STEP 5: Add Credentials to GitHub Secrets (5 minutes)

**This enables GitHub Actions to deploy automatically**

### Step 5.1: Go to GitHub Secrets

1. **Go to GitHub Repository:**
   - Navigate to: `https://github.com/rashadwest/BTEBallCODE` (or your repo)
   - Click **Settings** → **Secrets and variables** → **Actions**

### Step 5.2: Add Netlify Secrets

**Add NETLIFY_AUTH_TOKEN:**
1. Click **"New repository secret"**
2. **Name:** `NETLIFY_AUTH_TOKEN`
3. **Value:** Paste your Netlify Auth Token (from Step 4.2)
4. Click **"Add secret"**

**Add NETLIFY_SITE_ID:**
1. Click **"New repository secret"**
2. **Name:** `NETLIFY_SITE_ID`
3. **Value:** Paste your Netlify Site ID (from Step 4.1)
4. Click **"Add secret"**

**Add NETLIFY_SITE_NAME (Optional):**
1. Click **"New repository secret"**
2. **Name:** `NETLIFY_SITE_NAME`
3. **Value:** Your Netlify site name (e.g., `ballcode-game`)
4. Click **"Add secret"**

**✅ Checkpoint:** All GitHub Secrets configured

---

## ✅ PHASE 1 COMPLETE!

**You now have:**
- ✅ Netlify account created
- ✅ WebGL build (via GitHub Actions - easiest!)
- ✅ Game deployed to Netlify
- ✅ Netlify credentials saved
- ✅ GitHub Secrets configured

**Next Steps:**
- **Phase 2:** Verify GitHub Actions workflow (see `PHASE-2-GITHUB-ACTIONS-SETUP.md`)
- **Phase 3:** Set up n8n automation (see `PHASE-3-N8N-WORKFLOW-BUILD.md`)

---

## 🐛 TROUBLESHOOTING

### "No WebGL module loaded" in Unity

**Solution:** Use **Option 1 (GitHub Actions)** from Step 2 - no local module needed!

### GitHub Actions build fails

**Check:**
- Unity version in workflow matches your project
- `UNITY_LICENSE` secret is set (if using Pro)
- Build script path is correct

### Netlify deployment fails

**Check:**
- `Builds/WebGL/` folder has `index.html`
- `Build/` folder exists with .wasm files
- File size isn't too large (Netlify free tier has limits)

### Can't find Netlify credentials

**Site ID:**
- Settings → General → Site details → Site ID

**Auth Token:**
- User settings → Applications → Personal access tokens → Generate new

---

## 📚 RELATED DOCUMENTATION

- **GitHub Actions Setup:** `PHASE-2-GITHUB-ACTIONS-SETUP.md`
- **WebGL Build Guide:** `UNITY-WEBGL-BUILD-GUIDE.md`
- **WebGL Options:** `WEBGL-OPTIONS-WITHOUT-MODULE.md`
- **Netlify Status:** `NETLIFY-WEBGL-STATUS-REPORT.md`

---

## 🎯 QUICK REFERENCE

**Netlify Signup:** https://app.netlify.com/signup  
**GitHub Actions:** Repository → Actions tab → Run workflow  
**Netlify Site ID:** Settings → General → Site details  
**Netlify Auth Token:** User settings → Applications → Personal access tokens  
**GitHub Secrets:** Repository → Settings → Secrets and variables → Actions

---

**Status:** ✅ Ready to follow  
**Time:** 15-20 minutes  
**Difficulty:** Easy (mostly clicking buttons)  
**Next:** Phase 2 - GitHub Actions Setup
