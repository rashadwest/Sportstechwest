# 🚀 Start Building Action Plan

**Date:** December 5, 2025  
**Status:** Ready to Build  
**Goal:** Get the game building with new levels

---

## ✅ **WHAT WE HAVE READY**

1. **Workflow File** ✅
   - Added to GitHub: `rashadwest/BTEBallCODE`
   - Production-ready with validation
   - Auto-triggers on push to `main`

2. **GitHub Secrets** ✅
   - `NETLIFY_AUTH_TOKEN` configured
   - `NETLIFY_SITE_ID` configured

3. **New Level Files** ✅
   - Created 5 new level JSON files:
     - `book1_math_foundation.json`
     - `book2_math_decision.json`
     - `book3_math_pattern.json`
     - `book4_advanced_sequences.json`
     - `book5_nested_conditionals.json`
   - Currently in: `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels/`

4. **Automation Scripts** ✅
   - `automate-webgl-build.sh` - Trigger and monitor builds
   - All prerequisites checked

---

## 🎯 **WHAT NEEDS TO BE DONE**

### **Step 1: Add Level Files to Unity Repository** ⚠️ **REQUIRED**

**Current Situation:**
- Level files are in the workflows repo
- They need to be in the Unity repository (`rashadwest/BTEBallCODE`)

**Where They Should Go:**
The Unity repository needs these files in one of these locations:
- `Assets/StreamingAssets/Levels/` (most common)
- `Assets/Resources/Levels/` (alternative)
- Or wherever `LevelDataManager.cs` loads them from

**Options to Add Them:**

#### **Option A: If You Have Unity Repo Cloned Locally**

```bash
# 1. Copy level files to Unity repo
cp /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels/*.json \
   /path/to/BTEBallCODE/Assets/StreamingAssets/Levels/

# 2. Commit and push
cd /path/to/BTEBallCODE
git add Assets/StreamingAssets/Levels/*.json
git commit -m "Add Math and additional Coding level exercises"
git push origin main
```

#### **Option B: Use GitHub UI**

1. Go to: https://github.com/rashadwest/BTEBallCODE
2. Navigate to: `Assets/StreamingAssets/Levels/` (or create if doesn't exist)
3. Click "Add file" → "Upload files"
4. Upload the 5 new JSON files:
   - `book1_math_foundation.json`
   - `book2_math_decision.json`
   - `book3_math_pattern.json`
   - `book4_advanced_sequences.json`
   - `book5_nested_conditionals.json`
5. Commit with message: "Add Math and additional Coding level exercises"

#### **Option C: Use GitHub CLI**

```bash
cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book

# For each file, add to Unity repo
for file in Unity-Scripts/Levels/book*_math*.json Unity-Scripts/Levels/book4*.json Unity-Scripts/Levels/book5*.json; do
  gh api repos/rashadwest/BTEBallCODE/contents/Assets/StreamingAssets/Levels/$(basename $file) \
    -X PUT \
    -f message="Add $(basename $file)" \
    -f content="$(base64 -i $file)" \
    -f branch="main"
done
```

---

### **Step 2: Verify Level Files Location** ✅

**Check where Unity loads levels from:**

1. **Check `LevelDataManager.cs`:**
   - Look for `StreamingAssets` or `Resources` paths
   - See what folder structure it expects

2. **Common Locations:**
   - `Assets/StreamingAssets/Levels/` ← Most likely
   - `Assets/Resources/Levels/`
   - `Assets/StreamingAssets/Unity-Scripts/Levels/`

3. **Verify in Unity Repo:**
   - Check if `Assets/StreamingAssets/` exists
   - Check if `Levels/` folder exists there
   - See what existing level files are there (if any)

---

### **Step 3: Trigger Build** 🚀

**Once level files are in Unity repo, the build will auto-trigger!**

The workflow watches for changes to:
- `Unity-Scripts/**`
- `Assets/**`
- `ProjectSettings/**`

**So pushing the level files will automatically trigger a build!**

**Or trigger manually:**

```bash
# Option 1: Use automation script
./automate-webgl-build.sh
# Choose option 1 (Trigger new build)

# Option 2: GitHub UI
# Go to: https://github.com/rashadwest/BTEBallCODE/actions
# Click "Unity WebGL Build and Deploy"
# Click "Run workflow"

# Option 3: Wait for auto-trigger
# Just push the files - build starts automatically!
```

---

## 📋 **QUICK CHECKLIST**

### **Before Building:**
- [ ] Verify Unity repo structure (where levels should go)
- [ ] Copy level files to Unity repository
- [ ] Commit and push level files
- [ ] Verify workflow file exists in Unity repo (✅ Already done)

### **During Build:**
- [ ] Monitor build progress (GitHub Actions)
- [ ] Check for any errors
- [ ] Wait 10-15 minutes for build

### **After Build:**
- [ ] Download build artifacts (if needed)
- [ ] Verify deployment to Netlify
- [ ] Test game with new levels

---

## 🔍 **VERIFY UNITY REPO STRUCTURE**

**Let's check what exists in the Unity repo:**

```bash
# Check if StreamingAssets exists
gh api repos/rashadwest/BTEBallCODE/contents/Assets/StreamingAssets 2>&1

# Check if Levels folder exists
gh api repos/rashadwest/BTEBallCODE/contents/Assets/StreamingAssets/Levels 2>&1

# List existing level files (if any)
gh api repos/rashadwest/BTEBallCODE/contents/Assets/StreamingAssets/Levels 2>&1 | grep -E "name|path"
```

**Or check in GitHub UI:**
- Go to: https://github.com/rashadwest/BTEBallCODE/tree/main/Assets
- Look for `StreamingAssets/` folder
- Check if `Levels/` exists inside it

---

## 🎯 **RECOMMENDED NEXT STEPS**

### **Immediate (5 minutes):**

1. **Check Unity repo structure:**
   ```bash
   gh api repos/rashadwest/BTEBallCODE/contents/Assets 2>&1 | head -20
   ```

2. **Find where levels should go:**
   - Check `LevelDataManager.cs` in Unity repo
   - Or check existing level files location

3. **Add level files to correct location**

### **Then (automatic):**

4. **Build auto-triggers** when you push
5. **Monitor build** in GitHub Actions
6. **Deploy happens automatically** to Netlify

---

## 📊 **CURRENT STATUS**

| Task | Status | Next Action |
|------|--------|-------------|
| Workflow in GitHub | ✅ Done | Ready |
| GitHub Secrets | ✅ Done | Ready |
| Level Files Created | ✅ Done | Need to add to Unity repo |
| Level Files in Unity Repo | ❌ Pending | Add files (Step 1) |
| Build Triggered | ⏳ Waiting | After Step 1 |
| Build Complete | ⏳ Waiting | After build |
| Deployed to Netlify | ⏳ Waiting | Auto after build |

---

## 🚀 **QUICK START**

**Fastest path to building:**

1. **Check Unity repo structure** (2 min)
2. **Add level files via GitHub UI** (3 min)
3. **Build auto-triggers** (10-15 min wait)
4. **Done!** Game builds and deploys automatically

**Total time:** ~20 minutes (mostly waiting for build)

---

## 📝 **FILES TO ADD**

**These 5 files need to go to Unity repo:**

1. `book1_math_foundation.json` - Math version of Book 1
2. `book2_math_decision.json` - Math version of Book 2
3. `book3_math_pattern.json` - Math version of Book 3
4. `book4_advanced_sequences.json` - Advanced coding level
5. `book5_nested_conditionals.json` - Nested conditionals level

**Location:** `Assets/StreamingAssets/Levels/` (or wherever Unity loads from)

---

**Status:** ✅ Ready to add files and build!  
**Blocker:** Need to add level files to Unity repository  
**Time to Build:** ~20 minutes after files are added



