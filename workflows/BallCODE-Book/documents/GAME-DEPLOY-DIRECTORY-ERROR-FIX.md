# Game Deploy Directory Error - Fix Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Error:** "Deploy directory 'Builds/WebGL' does not exist"  
**Status:** Extensions error fixed! Now need to fix publish directory

---

## 🎯 THE PROBLEM

**Error:** 
```
Deploy did not succeed: Deploy directory 'Builds/WebGL' does not exist
```

**What's Happening:**
- Netlify is looking for `Builds/WebGL` directory
- This directory doesn't exist in the repository
- Unity game builds are likely created by GitHub Actions, not in the repo

---

## ✅ THE FIX

### **Option 1: Check Build Settings in Netlify** ⭐ FIRST

**The publish directory might be set incorrectly:**

1. **Go to:** Netlify Dashboard → ballcode → Site Settings
2. **Go to:** Build & deploy → Build settings
3. **Check:** "Publish directory"
4. **Current:** Probably set to `Builds/WebGL`
5. **Fix:** 
   - If build files are in root → Change to `.` (root)
   - If build files are in different folder → Change to that folder
   - If build files don't exist yet → Need to build first

---

### **Option 2: Check netlify.toml on GitHub**

**The netlify.toml might specify wrong publish directory:**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/blob/main/netlify.toml
2. **Look for:** `publish = "Builds/WebGL"`
3. **Check:** Does `Builds/WebGL` directory exist in the repo?
4. **If not:**
   - Change `publish = "."` (root) if files are in root
   - OR remove publish line to use Netlify UI settings
   - OR ensure build creates the directory first

---

### **Option 3: Unity Game Build Process**

**For Unity games, the build process is usually:**

1. **GitHub Actions builds Unity game** → Creates `Builds/WebGL/`
2. **Build files are committed/pushed** to repository
3. **Netlify deploys** from `Builds/WebGL/`

**If this is your setup:**
- Check if GitHub Actions is building the game
- Check if build files are being committed to repo
- If not, you need to either:
  - Run GitHub Actions build first
  - OR change publish directory to where files actually are

---

## 🔍 DIAGNOSTIC STEPS

### **Step 1: Check What's Actually in the Repository**

**Check GitHub repository structure:**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE
2. **Check:** Does `Builds/WebGL/` folder exist?
3. **If yes:** Check if it has files
4. **If no:** That's the problem - need to build first

---

### **Step 2: Check Netlify Build Settings**

**Check what Netlify thinks the publish directory should be:**

1. **Go to:** Netlify Dashboard → ballcode → Site Settings
2. **Go to:** Build & deploy → Build settings
3. **Check:** "Publish directory" field
4. **Note:** What is it set to?

**If set to `Builds/WebGL` but directory doesn't exist:**
- Change to `.` (root) if files are in root
- OR ensure build creates the directory

---

### **Step 3: Check netlify.toml**

**Check the configuration file:**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/blob/main/netlify.toml
2. **Look for:** `[build]` section
3. **Check:** `publish = "..."` value
4. **Fix:** Change to match where files actually are

---

## 🚀 RECOMMENDED ACTION

**Step 1: Check Netlify Build Settings**

1. **Go to:** Netlify Dashboard → ballcode → Site Settings
2. **Go to:** Build & deploy → Build settings
3. **Check:** "Publish directory"
4. **If it says `Builds/WebGL`:**
   - Check if that directory exists in GitHub repo
   - If not, change to `.` (root) temporarily
   - OR check where build files actually are

**Step 2: Check GitHub Repository**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE
2. **Check:** What folders/files are in the root?
3. **Look for:** WebGL build files (index.html, .wasm files, etc.)
4. **Note:** Where are the actual game files?

**Step 3: Fix Publish Directory**

**Based on what you find:**
- If files are in root → Set publish to `.` (root)
- If files are in `Builds/WebGL` → Ensure that directory exists
- If files don't exist → Need to build game first

---

## 📋 COMMON SCENARIOS

### **Scenario 1: Build Files in Root**

**If game files are in repository root:**
- **Fix:** Set publish directory to `.` (root)
- **In Netlify:** Build settings → Publish directory → `.`
- **In netlify.toml:** `publish = "."`

---

### **Scenario 2: Build Files in Builds/WebGL**

**If build files should be in Builds/WebGL:**
- **Problem:** Directory doesn't exist yet
- **Fix:** 
  - Run GitHub Actions build first
  - OR build locally and commit Builds/WebGL folder
  - OR change publish directory to where files actually are

---

### **Scenario 3: GitHub Actions Builds Game**

**If GitHub Actions creates the build:**
- **Check:** Is GitHub Actions workflow running?
- **Check:** Is it committing build files to repo?
- **If yes:** Wait for build to complete, then retry Netlify
- **If no:** Need to trigger GitHub Actions build first

---

## ✅ QUICK FIX (If Files Are in Root)

**If your game files are in the repository root:**

1. **Netlify Dashboard:**
   - Site Settings → Build & deploy → Build settings
   - Publish directory: Change to `.` (root)
   - Save

2. **OR netlify.toml:**
   - Edit: `publish = "."`
   - Commit and push

3. **Retry deployment**

---

**Status:** 🔍 **CHECK PUBLISH DIRECTORY** - Where are the actual game files?

**Next:** Check Netlify build settings and GitHub repository structure

