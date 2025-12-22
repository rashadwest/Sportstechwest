# Repository Structure - Permanent Memory

**Copyright © 2025 Rashad West. All Rights Reserved.**

**CRITICAL:** This is the definitive guide for repository structure. Reference this for ALL deployment and code organization decisions.

---

## 🎯 REPOSITORY MAPPING (DEFINITIVE)

### **Repository 1: Website**
**GitHub URL:** `https://github.com/JuddCMelvin/BallCode`  
**Local Path:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode`  
**Purpose:** BallCODE Business Website (ballcode.co)  
**Contains:**
- HTML files (index.html, books/*.html, teachers/*.html)
- CSS files (css/style.css)
- JavaScript files (js/*.js)
- Website images/assets (assets/images/)
- Website deployment scripts (deploy-ballcode-website.sh)

**Git Remote:**
```bash
origin → https://github.com/JuddCMelvin/BallCode.git
```

**Deployment:**
- Push to: `JuddCMelvin/BallCode` repository
- Hosting: Netlify (ballcode.co)
- Auto-deploy: Yes (if configured)

**Commands:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode
git push origin main
```

---

### **Repository 2: Unity Game**
**GitHub URL:** `https://github.com/rashadwest/BTEBallCODE`  
**Local Path:** `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts` (development)  
**Unity Project Path:** (Actual Unity project location - TBD)  
**Purpose:** Unity Game Source Code  
**Contains:**
- Unity C# scripts (*.cs files)
- Level data JSON files (Levels/*.json)
- Game managers (GameModeManager.cs, StoryModeManager.cs, etc.)
- Unity project files (Assets/, ProjectSettings/, Packages/)
- WebGL builds

**Git Remote:**
- Unity project itself should be a git repository
- Remote: `https://github.com/rashadwest/BTEBallCODE.git`

**Note:** `Unity-Scripts/` is a local development directory, NOT a git repository. Scripts from here should be copied/synced to the actual Unity project.

**Deployment:**
- Push to: `rashadwest/BTEBallCODE` repository
- Build: Unity WebGL build
- Hosting: Netlify or other (for WebGL)

---

## 🚨 CRITICAL RULES

### **NEVER Confuse These:**

1. **Website Files → Website Repo**
   - ✅ HTML/CSS/JS → `JuddCMelvin/BallCode`
   - ❌ NEVER push website files to `rashadwest/BTEBallCODE`

2. **Unity Game Files → Game Repo**
   - ✅ C# scripts, Unity assets → `rashadwest/BTEBallCODE`
   - ❌ NEVER push Unity files to `JuddCMelvin/BallCode`

3. **Always Verify Before Pushing:**
   ```bash
   # Check which repo you're in
   git remote -v
   
   # Verify it's correct before pushing
   ```

---

## 📋 QUICK REFERENCE

### **When Working on Website:**
```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode
# Verify remote
git remote -v  # Should show: JuddCMelvin/BallCode
# Push changes
git push origin main
```

### **When Working on Unity Game:**
```bash
# Navigate to Unity project (not Unity-Scripts/)
cd /path/to/Unity/Project
# Verify remote
git remote -v  # Should show: rashadwest/BTEBallCODE
# Push changes
git push origin main
```

### **When Working on Unity-Scripts (Development):**
```bash
# Unity-Scripts/ is NOT a git repo
# It's a local development directory
# Copy/sync scripts to actual Unity project
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts
# Edit scripts here, then copy to Unity project
```

---

## ✅ VERIFICATION CHECKLIST

**Before ANY push, verify:**
- [ ] Which directory am I in? (BallCode or Unity project?)
- [ ] What does `git remote -v` show?
- [ ] Is this the correct repository for these files?
- [ ] Am I pushing website files to website repo?
- [ ] Am I pushing Unity files to Unity repo?

---

## 📝 MEMORY FORMAT

**Save this to AI memory:**

```
BallCODE Project Repository Structure:
- Website Repository: JuddCMelvin/BallCode (GitHub) → Local: BallCode/ directory → Purpose: ballcode.co website → Contains: HTML, CSS, JS, website assets → Deployment: Push to JuddCMelvin/BallCode, Netlify auto-deploys
- Unity Game Repository: rashadwest/BTEBallCODE (GitHub) → Local: Unity project directory → Purpose: Unity game source code → Contains: C# scripts, Unity assets, level JSON files → Deployment: Push to rashadwest/BTEBallCODE, Unity builds WebGL
- Unity-Scripts/ directory: Local development directory (NOT a git repo) → Contains: C# scripts for development/integration → Scripts should be synced to actual Unity project

CRITICAL RULES:
- NEVER push website files (HTML/CSS/JS) to rashadwest/BTEBallCODE
- NEVER push Unity files (C# scripts, Unity assets) to JuddCMelvin/BallCode
- ALWAYS verify git remote before pushing: git remote -v
- Website: cd BallCode → git push origin main → JuddCMelvin/BallCode
- Unity Game: cd Unity/Project → git push origin main → rashadwest/BTEBallCODE
```

---

**Last Updated:** December 20, 2025  
**Status:** ✅ Verified and Fixed

