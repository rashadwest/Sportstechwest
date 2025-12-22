# Create Netlify Site First (Before Getting Site ID)

**Date:** December 18, 2025  
**Issue:** Need to create a Netlify site before you can get a Site ID

---

## 🎯 THE PROBLEM

**You can't get a Netlify Site ID until you have a Netlify site!**

**Solution:** Create a Netlify site first (even if empty), then get the Site ID.

---

## 🚀 QUICK SOLUTION

### **Option 1: Create Site via Netlify Dashboard (Easiest)**

1. **Go to Netlify:**
   - https://app.netlify.com
   - Sign up or log in

2. **Add New Site:**
   - Click **"Add new site"** button
   - Choose **"Deploy manually"**

3. **Upload a Dummy File:**
   - Create a simple `index.html` file:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>BallCODE Game - Coming Soon</title>
     </head>
     <body>
         <h1>BallCODE Game</h1>
         <p>Unity game will be deployed here.</p>
     </body>
     </html>
     ```
   - Drag and drop this file to Netlify
   - OR create a folder with `index.html` and upload the folder

4. **Site is Created!**
   - Netlify will give you a URL like: `https://random-name-12345.netlify.app`
   - **Now you can get the Site ID!**

5. **Get Site ID:**
   - Click on your site
   - Go to: **Settings** → **General**
   - Scroll to **"Site details"**
   - Copy **"Site ID"** (looks like: `abc123-def456-ghi789`)

---

### **Option 2: Connect GitHub Repository (Recommended for Auto-Deploy)**

1. **Go to Netlify:**
   - https://app.netlify.com

2. **Add New Site:**
   - Click **"Add new site"**
   - Choose **"Import an existing project"**
   - Click **"GitHub"**

3. **Authorize Netlify:**
   - Grant Netlify access to your GitHub account
   - Select repository: `rashadwest/BTEBallCODE`

4. **Configure Build Settings:**
   - **Build command:** (leave empty - Unity builds separately)
   - **Publish directory:** `Builds/WebGL` (or wherever your Unity build is)
   - Click **"Deploy site"**

5. **Site is Created!**
   - Netlify will create the site
   - **Now you can get the Site ID!**

6. **Get Site ID:**
   - Click on your site
   - Go to: **Settings** → **General**
   - Copy **"Site ID"**

---

## ⚠️ TEMPORARY WORKAROUND

**If you want to proceed without Site ID for now:**

The robot script now allows you to skip the Site ID:

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/robot-hardcode-env-vars.py
```

**When prompted:**
- Enter `skip` or press Enter
- The workflow will work without Netlify status checks
- You can add the Site ID later

**What won't work without Site ID:**
- ❌ Netlify deployment status checks
- ❌ Automatic Netlify verification

**What will still work:**
- ✅ GitHub Actions builds
- ✅ Unity builds
- ✅ Basic workflow execution

---

## 📋 RECOMMENDED APPROACH

1. **Create Netlify site now** (Option 1 or 2 above) - takes 2 minutes
2. **Get Site ID** from site settings
3. **Run robot script** with the Site ID
4. **Everything works** including Netlify checks

---

## ✅ AFTER YOU HAVE SITE ID

**Run the robot script:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
python scripts/robot-hardcode-env-vars.py
```

**Enter your Site ID when prompted.**

---

**Create the site first, then get the Site ID!** 🚀

