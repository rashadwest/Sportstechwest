# What to Deploy to Netlify - Complete Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 27, 2025  
**Status:** ✅ **Complete Deployment Guide**

---

## ❌ DON'T: Deploy Just index.html

**Why Not:**
- `index.html` alone won't work
- Game needs ALL files and folders
- Missing files = Game won't load

---

## ✅ DO: Deploy the ENTIRE WebGL Folder

**What to Deploy:**
```
Builds/WebGL/  ← Drag THIS ENTIRE FOLDER
├── index.html          ← Main entry point
├── Build/              ← Game code (WebGL.wasm, WebGL.js, WebGL.data)
├── TemplateData/       ← UI assets (CSS, images, loading screen)
└── StreamingAssets/    ← Game data (levels, localization bundles)
```

**All 4 items together are REQUIRED!**

---

## 📋 WHY EACH FILE/FOLDER IS NEEDED

### 1. index.html (Main Entry Point)
**What it does:**
- Loads the Unity WebGL game
- Provides the HTML structure
- Connects to Build/ folder

**Without it:**
- ❌ Nothing loads
- ❌ 404 error

**With it alone:**
- ❌ Still won't work (needs Build/ folder)

---

### 2. Build/ Folder (Game Code)
**What it contains:**
- `WebGL.wasm` - WebAssembly game code (28MB)
- `WebGL.js` - JavaScript runtime (412KB)
- `WebGL.data` - Game assets (33MB)
- `WebGL.loader.js` - Loader script (19KB)

**Without it:**
- ❌ Game won't load
- ❌ Error: "Failed to load game"

**Why needed:**
- This IS the game code
- Unity compiles your game into these files

---

### 3. TemplateData/ Folder (UI Assets)
**What it contains:**
- `style.css` - Styling for loading screen
- `favicon.ico` - Site icon
- Images for loading screen
- JavaScript for Unity player

**Without it:**
- ❌ Game loads but looks broken
- ❌ No loading screen
- ❌ Poor user experience

---

### 4. StreamingAssets/ Folder (Game Data)
**What it contains:**
- `Levels/` - Level JSON files
- `aa/WebGL/` - Localization bundles (.bundle files)
- Configuration files

**Without it:**
- ❌ Game loads but can't play levels
- ❌ No localization (English/Spanish)
- ❌ Missing game data

---

## 🎯 CORRECT DEPLOYMENT PROCESS

### Step 1: Open Finder
Navigate to: `/Users/rashadwest/BTEBallCODE/Builds/WebGL`

### Step 2: Drag ENTIRE Folder
**Drag the WebGL folder itself:**
- ✅ Drag the folder icon
- ✅ Not just index.html
- ✅ Not just one subfolder
- ✅ The ENTIRE folder with all 4 items

### Step 3: Verify in Netlify
**In deploy file browser, you should see:**
- ✅ `index.html` (in root)
- ✅ `Build/` folder
- ✅ `TemplateData/` folder
- ✅ `StreamingAssets/` folder

**All 4 items should be visible!**

---

## 📊 FILE SIZE REFERENCE

**Total Build Size:** ~61MB

**Breakdown:**
- `Build/WebGL.data` - 33MB (game assets)
- `Build/WebGL.wasm` - 28MB (game code)
- `Build/WebGL.js` - 412KB (runtime)
- `Build/WebGL.loader.js` - 19KB (loader)
- `TemplateData/` - ~100KB (UI assets)
- `StreamingAssets/` - ~500KB (game data)
- `index.html` - 4.8KB (entry point)

**All files together = Working game!**

---

## 🚨 COMMON MISTAKES

**❌ DON'T:**
- Deploy just `index.html`
- Deploy just `Build/` folder
- Deploy individual files
- Deploy subfolders separately

**✅ DO:**
- Deploy the ENTIRE `WebGL/` folder
- All files and folders together
- One drag-and-drop operation

---

## ✅ QUICK CHECKLIST

**Before Deploying:**
- [ ] I'm in `/Users/rashadwest/BTEBallCODE/Builds/WebGL`
- [ ] I can see 4 items: `index.html`, `Build/`, `TemplateData/`, `StreamingAssets/`
- [ ] I'm dragging the ENTIRE `WebGL` folder

**After Deploying:**
- [ ] Netlify shows `index.html` in root
- [ ] Netlify shows `Build/` folder
- [ ] Netlify shows `TemplateData/` folder
- [ ] Netlify shows `StreamingAssets/` folder
- [ ] Game URL loads: https://ballcode.netlify.app

---

## 🎯 SUMMARY

**Deploy:** The ENTIRE `WebGL/` folder (all 4 items together)  
**Not:** Just `index.html` or individual files  
**Why:** All files are required for the game to work

**Think of it like this:**
- `index.html` = The door to your house
- `Build/` = The house itself (game code)
- `TemplateData/` = The furniture (UI)
- `StreamingAssets/` = The contents (game data)

**You need all of them for a complete, working game!**

---

**Status:** ✅ **Deploy entire folder** - All files required!

