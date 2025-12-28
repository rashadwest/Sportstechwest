# Project Structure Clarification

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 20, 2025  
**Purpose:** Clearly define what each component is

---

## 🎯 PROJECT COMPONENTS

### **1. BTEBallCODE (GitHub Repository)**
**Repository:** `https://github.com/rashadwest/BTEBallCODE`  
**Purpose:** Unity Game Source Code  
**Contains:**
- Unity project files (Assets/, ProjectSettings/, Packages/)
- Unity C# scripts
- WebGL build configuration
- Game levels (JSON files in StreamingAssets/Levels/)
- Unity game UI/UX

**What goes here:**
- ✅ Unity game code
- ✅ Unity scripts (C#)
- ✅ Game UI improvements
- ✅ Game button improvements
- ✅ Unity scenes
- ✅ Game assets

**What does NOT go here:**
- ❌ Website files (HTML, CSS, JS)
- ❌ Book content
- ❌ Website deployment

---

### **2. BallCode (Local Directory - Website)**
**Path:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode`  
**Purpose:** Business Website (ballcode.co)  
**Contains:**
- HTML files (index.html, books/book1.html, etc.)
- CSS (style.css)
- JavaScript
- Website images
- Website deployment scripts

**GitHub Repository:** `rashadwest/BTEBallCODE` (same repo as game? Need to verify)

**What goes here:**
- ✅ Website HTML/CSS/JS
- ✅ Website button improvements
- ✅ Book pages
- ✅ Website deployment

**What does NOT go here:**
- ❌ Unity game code
- ❌ Unity scripts
- ❌ Game assets

---

### **3. Unity-Scripts (Local Directory)**
**Path:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts`  
**Purpose:** Unity Game Scripts (Development/Integration)  
**Contains:**
- C# scripts for Unity game
- Level data JSON files
- Integration scripts
- Game managers

**Relationship:**
- These scripts should be synced to BTEBallCODE repository
- They're the source of truth for game functionality
- Used for integration with books/curriculum

**What goes here:**
- ✅ Unity C# scripts
- ✅ Game integration code
- ✅ Level data files
- ✅ Game managers

---

## 🔍 CURRENT CONFUSION

**Issue:** I was updating website buttons (CSS) when you wanted Unity game buttons.

**Clarification Needed:**
1. **BTEBallCODE repository** = Unity game only
2. **BallCode directory** = Website only
3. **Unity-Scripts directory** = Game scripts (syncs to BTEBallCODE)

---

## ✅ WHAT WE'RE WORKING ON NOW

**You said:** "We need to clearly state what we are working on. The BTEBallCODE is only for the game in Github."

**This means:**
- ✅ **BTEBallCODE** = Unity game repository (GitHub)
- ✅ **Unity game buttons** = What we should be improving
- ❌ **Website buttons** = What I mistakenly updated

**Next Steps:**
1. Confirm BTEBallCODE repository structure
2. Work on Unity game button improvements
3. Update Unity-Scripts/ImprovedButton.cs
4. Sync changes to BTEBallCODE repository

---

## 📋 VERIFICATION NEEDED

**Questions to answer:**
1. Is `BallCode/` directory in the same GitHub repo as BTEBallCODE?
2. Or is `BallCode/` in a separate repository?
3. Where should Unity game button improvements go?
   - Unity-Scripts/ImprovedButton.cs (local)
   - Then sync to BTEBallCODE repository

---

**Status:** Awaiting clarification on repository structure


