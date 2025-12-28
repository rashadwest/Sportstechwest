# Deploy All 3 Books Levels - Action Plan
## Complete Deployment Guide for Books 1, 2, and 3

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 21, 2025  
**Status:** 🚀 Ready to Deploy  
**Goal:** Push all 3 book levels to Unity game with focus on specific elements

---

## 🎯 THE 3 BOOKS & THEIR SPECIFIC ELEMENTS

### **Book 1: The Foundation Block**
**Element:** **Sequences** (Basic Programming)
- **Python Concept:** Sequences, step-by-step execution
- **Basketball Skill:** Pound Dribble (Block 1)
- **Level File:** `book1_foundation_block.json`
- **Focus:** Students learn that code executes in order, step by step

### **Book 2: The Code of Flow**
**Element:** **Conditionals** (Decision-Making)
- **Python Concept:** `if/elif/else` statements
- **Basketball Skill:** Crossover Dribble (Block 2)
- **Level File:** `book2_decision_crossover.json`
- **Focus:** Students learn that coding uses if/then to make decisions

### **Book 3: The Pattern**
**Element:** **Loops** (Repetition & Patterns)
- **Python Concept:** `for` loops, `range()`, pattern repetition
- **Basketball Skill:** In & Out Dribble (Block 3)
- **Level File:** `book3_pattern_loop.json`
- **Focus:** Students learn that coding uses loops to repeat patterns

---

## ✅ LEVEL FILES STATUS

All 3 level files are **COMPLETE** with:
- ✅ Complete curriculum sections (Phase 1, 2, 3)
- ✅ Learning objectives aligned to specific elements
- ✅ Basketball context (Pound, Crossover, In & Out)
- ✅ Python progression (Sequences → Conditionals → Loops)
- ✅ Standards alignment (CSTA, Common Core, NGSS)
- ✅ Prerequisites set correctly

**File Locations:**
- `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels/book1_foundation_block.json`
- `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels/book2_decision_crossover.json`
- `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels/book3_pattern_loop.json`

---

## 🚀 DEPLOYMENT STEPS

### **Step 1: Push Level Files to Unity Repository**

**Repository:** `https://github.com/rashadwest/BTEBallCODE`  
**Path in Repo:** `Assets/StreamingAssets/Levels/`

**Option A: Using GitHub UI (Recommended - 5 minutes)**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE
2. **Navigate to:** `Assets/StreamingAssets/Levels/` (create folder if doesn't exist)
3. **Upload all 3 files:**
   - Click "Add file" → "Upload files"
   - Upload:
     - `book1_foundation_block.json`
     - `book2_decision_crossover.json`
     - `book3_pattern_loop.json`
   - Commit message: "Add all 3 book levels: Sequences, Conditionals, Loops"
   - Click "Commit changes"

**Option B: Using Git (If Unity repo is cloned locally)**

```bash
# 1. Copy level files to Unity repo
cp /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels/book1_foundation_block.json \
   /path/to/BTEBallCODE/Assets/StreamingAssets/Levels/

cp /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels/book2_decision_crossover.json \
   /path/to/BTEBallCODE/Assets/StreamingAssets/Levels/

cp /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels/book3_pattern_loop.json \
   /path/to/BTEBallCODE/Assets/StreamingAssets/Levels/

# 2. Commit and push
cd /path/to/BTEBallCODE
git add Assets/StreamingAssets/Levels/book*.json
git commit -m "Add all 3 book levels: Sequences, Conditionals, Loops"
git push origin main
```

---

### **Step 2: Automatic Build & Deployment**

**What Happens Automatically:**
1. ✅ GitHub Actions detects change to `Assets/StreamingAssets/Levels/`
2. ✅ Workflow triggers automatically
3. ✅ Unity builds WebGL (10-15 minutes)
4. ✅ Build deploys to Netlify automatically
5. ✅ Game is live with all 3 book levels!

**Monitor Build:**
- GitHub Actions: `https://github.com/rashadwest/BTEBallCODE/actions`
- Workflow: "Unity WebGL Build and Deploy"
- Watch real-time progress

---

## 📋 VERIFICATION CHECKLIST

After deployment, verify:

- [ ] **Book 1 Level (Sequences):**
  - [ ] Level appears in game
  - [ ] Focuses on sequences (step-by-step execution)
  - [ ] Uses Block 1 (Pound Dribble)
  - [ ] Curriculum section visible
  - [ ] Exercise works correctly

- [ ] **Book 2 Level (Conditionals):**
  - [ ] Level appears in game
  - [ ] Focuses on conditionals (if/then decisions)
  - [ ] Uses Block 2 (Crossover Dribble)
  - [ ] Curriculum section visible
  - [ ] Exercise works correctly
  - [ ] Prerequisite (Book 1) set correctly

- [ ] **Book 3 Level (Loops):**
  - [ ] Level appears in game
  - [ ] Focuses on loops (pattern repetition)
  - [ ] Uses Block 3 (In & Out Dribble)
  - [ ] Curriculum section visible
  - [ ] Exercise works correctly
  - [ ] Prerequisites (Book 1, Book 2) set correctly

- [ ] **Netlify Deployment:**
  - [ ] Game loads at: `https://ballcode.netlify.app/`
  - [ ] All 3 levels accessible
  - [ ] Levels load correctly
  - [ ] Exercises function properly

---

## 🎯 ELEMENT FOCUS VERIFICATION

### **Book 1: Sequences Focus**
**Verify:**
- Level teaches step-by-step execution
- Students create sequences: START → Block 1 → Block 1 → Block 1 → ADVANCE
- No conditionals or loops introduced
- Pure sequence focus

### **Book 2: Conditionals Focus**
**Verify:**
- Level teaches if/then decision-making
- Students create conditionals: IF [defender left] THEN [crossover right] ELSE [crossover left]
- No loops introduced
- Pure conditional focus

### **Book 3: Loops Focus**
**Verify:**
- Level teaches pattern repetition
- Students create loops: LOOP [Block 3 fake] REPEAT 3, THEN [Block 3 real]
- Builds on sequences and conditionals
- Pure loop focus

---

## 📊 DEPLOYMENT STATUS

**Website Changes:**
- ✅ Committed and pushed to `JuddCMelvin/BallCode`
- ⏳ Netlify auto-deploy in progress

**Level Files:**
- ✅ All 3 files complete with curriculum
- ⏳ Ready to push to Unity repository
- ⏳ Waiting for upload to `rashadwest/BTEBallCODE`

**Next Steps:**
1. Upload level files to Unity repository (Step 1 above)
2. Wait for automatic build (10-15 minutes)
3. Verify deployment (checklist above)
4. Test all 3 levels in game

---

## 🔗 RELATED DOCUMENTS

- `documents/LEVEL-PUSH-SYSTEM-AUTOMATION.md` - Complete level push system
- `Unity-Scripts/Levels/book1_foundation_block.json` - Book 1 level file
- `Unity-Scripts/Levels/book2_decision_crossover.json` - Book 2 level file
- `Unity-Scripts/Levels/book3_pattern_loop.json` - Book 3 level file

---

**Version:** 1.0  
**Created:** December 21, 2025  
**Status:** Ready for Deployment


