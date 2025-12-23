# Netlify Build Settings for Unity Game
## Configuration for ballcode.netlify.app (Game Site)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 22, 2025  
**Site:** ballcode.netlify.app (Game)  
**Repository:** `rashadwest/BTEBallCODE`

---

## ✅ SETTINGS FOR UNITY GAME

### **Branch to deploy:**
- ✅ **Keep:** `main` (already selected)
- This is correct - deploy from main branch

### **Base directory:**
- ✅ **Leave empty** (blank)
- Not needed - build happens in GitHub Actions

### **Build command:**
- ✅ **Leave empty** (blank)
- **Why:** Unity builds happen via GitHub Actions, not on Netlify
- GitHub Actions builds Unity WebGL → outputs to `Builds/WebGL`
- Netlify just serves the already-built files

### **Publish directory:**
- ✅ **Set to:** `Builds/WebGL`
- **Why:** This is where GitHub Actions outputs the Unity WebGL build
- The built game files (index.html, Build/, etc.) are in this directory
- Netlify will serve files from this directory

### **Functions directory:**
- ✅ **Keep:** `netlify/functions` (default)
- You're not using Netlify Functions, but leaving the default is fine

---

## 🎯 SUMMARY: WHAT TO SET

**Settings for Unity Game:**

- ✅ **Branch to deploy:** `main` (keep as-is)
- ✅ **Base directory:** (empty - leave blank)
- ✅ **Build command:** (empty - leave blank)
- ✅ **Publish directory:** `Builds/WebGL` ← **CHANGE THIS**
- ✅ **Functions directory:** `netlify/functions` (keep default)

**Key change:** Set **Publish directory** to `Builds/WebGL`

---

## 📋 HOW IT WORKS

**Build & Deploy Flow:**

1. **GitHub Actions builds Unity:**
   - Unity project builds to `Builds/WebGL/`
   - Build output includes: `index.html`, `Build/`, `StreamingAssets/`

2. **GitHub Actions commits build:**
   - Build files are committed to the repository
   - OR GitHub Actions deploys directly to Netlify (via Netlify action)

3. **Netlify serves the build:**
   - If files are in repo: Netlify serves from `Builds/WebGL/`
   - If GitHub Actions deploys directly: Netlify receives the files

---

## 🔧 TWO DEPLOYMENT SCENARIOS

### **Scenario A: GitHub Actions Deploys Directly (Current Setup)**

**If your GitHub Actions workflow deploys directly to Netlify:**
- ✅ Build command: Empty (correct)
- ✅ Publish directory: `Builds/WebGL` (for reference, but GitHub Actions handles deployment)
- Netlify receives files directly from GitHub Actions

### **Scenario B: GitHub Actions Commits Build, Netlify Auto-Deploys**

**If GitHub Actions commits build files to the repo:**
- ✅ Build command: Empty (correct)
- ✅ Publish directory: `Builds/WebGL` (Netlify serves from here)
- Netlify auto-deploys when build files are committed

---

## 🚀 RECOMMENDED SETTINGS

**For your Unity game site:**

```
Branch to deploy: main
Base directory: (empty)
Build command: (empty)
Publish directory: Builds/WebGL
Functions directory: netlify/functions
```

**Then click "Save"!**

---

## ✅ VERIFICATION

**After saving, verify:**

1. **Check that publish directory is set:**
   - Should show: `Builds/WebGL`
   - This tells Netlify where to find the built game files

2. **Test deployment:**
   - Trigger a Unity build via GitHub Actions
   - Check if Netlify deploys automatically
   - Visit `ballcode.netlify.app` to verify game loads

---

## 📝 NOTES

**Important:**
- Unity builds happen in GitHub Actions (not on Netlify)
- Netlify just serves the already-built files
- Publish directory must match where GitHub Actions outputs the build

**If build files are in a different location:**
- Check your GitHub Actions workflow
- Look for `publish-dir` or `buildsPath` setting
- Match Netlify's publish directory to that location

---

**Version:** 1.0  
**Created:** December 22, 2025  
**Status:** Ready to configure

