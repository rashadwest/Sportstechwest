# Correct Deployment Instructions - Fix 404 Error

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 27, 2025  
**Status:** ✅ **READY TO DEPLOY CORRECTLY**

---

## 🚨 PROBLEM IDENTIFIED

**What Was Deployed (Wrong):**
- ✅ `webgl.loader.js` (from Build/ folder)
- ✅ `webgl.framework.js` (from Build/ folder)
- ❌ Missing: `index.html` (CRITICAL!)
- ❌ Missing: `TemplateData/` folder
- ❌ Missing: `StreamingAssets/` folder

**Result:** Only Build/ folder files were deployed → 404 error

---

## ✅ CORRECT DEPLOYMENT

### Step 1: Open Finder

Navigate to: `/Users/rashadwest/BTEBallCODE/Builds/`

**You'll see:**
- `WebGL` (uppercase) ← **USE THIS ONE**
- `webgl` (lowercase) ← Don't use

---

### Step 2: Open the WebGL Folder

**Double-click:** `WebGL` (uppercase)

**You should see 4 items:**
- `index.html` (file)
- `Build/` (folder)
- `TemplateData/` (folder)
- `StreamingAssets/` (folder)

---

### Step 3: Drag ENTIRE Folder to Netlify

1. **Go to Netlify:**
   - https://app.netlify.com/sites/ballcode/deploys

2. **Drag the WebGL folder:**
   - Drag the **folder icon** (not individual files)
   - Make sure all 4 items are inside

3. **Wait for upload:**
   - Should take 1-2 minutes
   - Watch for upload progress

---

### Step 4: Verify Deployment

**In Netlify file browser, you should see:**
- ✅ `index.html` (in root - most important!)
- ✅ `Build/` folder (contains webgl.* files)
- ✅ `TemplateData/` folder
- ✅ `StreamingAssets/` folder

**All 4 items should be visible!**

---

### Step 5: Test Game

**Game URL:** https://ballcode.netlify.app

**Expected:**
- ✅ Game loads (Unity WebGL player appears)
- ✅ No 404 error
- ✅ Game is playable

---

## 📋 WHAT WENT WRONG

**Previous Deployment:**
- Only `Build/` folder files were uploaded
- `index.html` was missing
- Wrong folder structure

**Why:**
- Might have dragged `Build/` folder instead of `WebGL/` folder
- Or dragged from wrong location

---

## ✅ CORRECT FOLDER STRUCTURE

**What Should Be Deployed:**
```
WebGL/                    ← Drag THIS folder
├── index.html            ← MUST be in root!
├── Build/                ← Contains webgl.* files
│   ├── WebGL.data
│   ├── WebGL.framework.js
│   ├── WebGL.loader.js
│   └── WebGL.wasm
├── TemplateData/         ← UI assets
└── StreamingAssets/      ← Game data
```

**All files together = Working game!**

---

## 🎯 QUICK CHECKLIST

**Before Deploying:**
- [ ] I'm in `/Users/rashadwest/BTEBallCODE/Builds/`
- [ ] I see `WebGL` folder (uppercase)
- [ ] I opened the `WebGL` folder
- [ ] I see 4 items: `index.html`, `Build/`, `TemplateData/`, `StreamingAssets/`

**When Dragging:**
- [ ] I'm dragging the `WebGL` folder itself (not contents)
- [ ] All 4 items are inside the folder I'm dragging

**After Deploying:**
- [ ] Netlify shows `index.html` in root
- [ ] Netlify shows `Build/` folder
- [ ] Netlify shows `TemplateData/` folder
- [ ] Netlify shows `StreamingAssets/` folder
- [ ] Game URL loads: https://ballcode.netlify.app

---

## 🚨 COMMON MISTAKES

**❌ DON'T:**
- Drag just the `Build/` folder
- Drag individual files
- Drag from `webgl` (lowercase) folder
- Drag contents of folder (drag the folder itself)

**✅ DO:**
- Drag the entire `WebGL/` folder (uppercase)
- Make sure `index.html` is inside
- Verify all 4 items are included

---

## ✅ SUMMARY

**Problem:** Only Build/ folder files deployed (missing index.html)  
**Solution:** Deploy entire `WebGL/` folder with all 4 items  
**Location:** `/Users/rashadwest/BTEBallCODE/Builds/WebGL`

**Status:** ✅ **Ready to Deploy** - Follow steps above

