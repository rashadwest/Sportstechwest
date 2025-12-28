# Rebuild Instructions - Fix Build Issues

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 27, 2025  
**Status:** 🔧 **REBUILD NEEDED** - Fix Build Issues

---

## 🚨 BUILD ISSUES IDENTIFIED

**Current build problems:**
1. ❌ Math and chess deleted
2. ❌ Robot UI wrong
3. ❌ Robot words messed up
4. ❌ Court grid hot pink (shouldn't be)
5. ❌ Robots hot pink (shouldn't be)

**Solution:** Rebuild from Unity with correct settings

---

## ✅ REBUILD STEPS

### Step 1: Open Unity Project

1. **Open Unity Hub**
2. **Open BallCODE project:**
   - Location: `/Users/rashadwest/BTEBallCODE`
3. **Wait for Unity to load**

---

### Step 2: Verify Features Are Present

**Check these in Unity:**

1. **Math and Chess Features:**
   - Check if they exist in project
   - Check if they're enabled in scenes
   - Check if they're included in build settings

2. **Robot UI:**
   - Check robot UI prefabs
   - Verify UI elements are correct
   - Check for any broken references

3. **Colors:**
   - Check grid material color (should NOT be hot pink)
   - Check robot material colors (should NOT be hot pink)
   - Verify shader settings

4. **Robot Text/Instructions:**
   - Check text files/scripts
   - Verify localization files
   - Check for any corrupted text

---

### Step 3: Fix Issues in Unity (If Needed)

**If features are missing:**
- Add them back to scenes
- Enable them in build settings
- Check for any disabled components

**If colors are wrong:**
- Fix material colors
- Check shader settings
- Verify color settings in scripts

**If UI is wrong:**
- Fix UI prefabs
- Check for broken references
- Verify UI elements are correct

---

### Step 4: Rebuild WebGL

**Using BuildScript (Recommended):**

1. **In Unity:**
   - File → Build Settings
   - Select WebGL platform
   - Click "Build" OR use BuildScript

2. **Or use command line:**
   ```bash
   cd /Users/rashadwest/BTEBallCODE
   /Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity \
     -batchmode \
     -quit \
     -projectPath /Users/rashadwest/BTEBallCODE \
     -executeMethod BuildScript.BuildWebGL \
     -logFile build.log
   ```

3. **Wait for build** (5-10 minutes)

4. **Verify build output:**
   - Check `Builds/WebGL/` folder
   - Verify all files are present
   - Check build size (~61MB)

---

### Step 5: Test Build Locally (Optional)

**Before deploying:**
1. Test build in browser locally
2. Verify all features work
3. Check colors are correct
4. Check UI is correct
5. Check robot text is correct

**If issues found:**
- Fix in Unity
- Rebuild
- Test again

---

### Step 6: Deploy Fixed Build

**Once build is correct:**

1. **Create zip file:**
   ```bash
   cd /Users/rashadwest/BTEBallCODE/Builds
   zip -r WebGL-fixed.zip WebGL/ -x "*.DS_Store"
   ```

2. **Upload to Netlify:**
   - Go to: https://app.netlify.com/sites/ballcode/deploys
   - Drag `WebGL-fixed.zip` to Netlify
   - Wait for deployment

3. **Verify:**
   - Check file browser for `index.html`
   - Test: https://ballcode.netlify.app
   - Verify all features work
   - Check colors are correct

---

## 🔍 CHECKLIST BEFORE REBUILDING

**In Unity, verify:**
- [ ] Math feature exists and is enabled
- [ ] Chess feature exists and is enabled
- [ ] Robot UI elements are correct
- [ ] Grid color is NOT hot pink
- [ ] Robot colors are NOT hot pink
- [ ] Robot text/instructions are correct
- [ ] All scenes are included in build settings
- [ ] All assets are included

---

## 🎯 QUICK REBUILD COMMAND

**If everything is correct in Unity, just rebuild:**

```bash
cd /Users/rashadwest/BTEBallCODE
python3 scripts/garvis-unity-build-deploy.py
```

**This will:**
- Build Unity WebGL
- Verify build
- Create zip file
- Provide deployment instructions

---

## 📋 WHAT TO CHECK AFTER REBUILD

**Test the new build:**
- [ ] Math feature works
- [ ] Chess feature works
- [ ] Robot UI is correct
- [ ] Grid color is correct (not hot pink)
- [ ] Robot colors are correct (not hot pink)
- [ ] Robot text/instructions are correct
- [ ] All features work as expected

---

**Status:** 🔧 **Ready to Rebuild** - Fix issues in Unity, then rebuild

