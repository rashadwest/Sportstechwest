# Level Push System - Automation Memory

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 21, 2025  
**Status:** ✅ Documented for Automation  
**Purpose:** Save the level push system to memory for repetitive automation

---

## 🎯 SYSTEM OVERVIEW

**The level push system is a repetitive process that can be automated:**
- Copy existing coding game level structure
- Modify content for new book/level
- Push to Unity repository via GitHub
- Trigger automatic build and deployment to Netlify

**This system should be saved to memory so it can be copied and reused for each new level.**

---

## 📋 LEVEL PUSH PROCESS (Step-by-Step)

### **Step 1: Copy Existing Level Template**

**Source Templates:**
- **Block Coding:** `book1_foundation_block.json` or `example_level_with_positions.json`
- **Math:** `book1_math_foundation.json`
- **Location:** `Unity-Scripts/Levels/` (local) or `Assets/StreamingAssets/Levels/` (Unity repo)

**Process:**
1. Copy existing level JSON file
2. Rename to new level ID (e.g., `book2_coding_level1.json`)
3. Keep same structure and format

---

### **Step 2: Modify Level Content**

**What to Change (Required):**
- `levelId`: Unique identifier (e.g., `book2_coding_level1`)
- `levelName`: Display name (e.g., "Book 2: Crossover Decision")
- `description`: What the level teaches
- `strategy.steps[]`: Dribble sequence/actions
- `exercise.blockCoding.targetCode`: Target code sequence (or `exercise.math.mathConcept` for math)
- `tags`: Update tags for new level

**What to Keep (Same):**
- `gameMode`: "blockcoding" or "math"
- `episodeNumber`: Book number (0 = Book 1, 1 = Book 2, etc.)
- `codingConcept`: Concept type (e.g., "basic_blocks_sequences", "conditionals", etc.)
- `difficultyLevel`: Difficulty (1 = beginner, 2 = intermediate, etc.)
- Overall JSON structure and format
- `videoPath`: Empty for now
- `videoConfig`: Same structure
- `scoring`: Same structure

**Optional Changes:**
- `exercise.blockCoding.availableBlocks`: Add more blocks if needed
- `learningObjectives`: Update if needed
- `successCriteria`: Update if needed
- `prerequisiteLevels`: Add if level requires previous completion

---

### **Step 3: Save Level File**

**Location Options:**
1. **Local Development:** `Unity-Scripts/Levels/` (in workflows repo)
2. **Unity Repository:** `Assets/StreamingAssets/Levels/` (in Unity repo)

**File Naming Convention:**
- `book{BOOK}_coding_level{LEVEL}.json` (for block coding)
- `book{BOOK}_math_level{LEVEL}.json` (for math)
- `book{BOOK}_{CONCEPT}_level{LEVEL}.json` (for specific concepts)

**Example:**
- `book1_coding_level1.json`
- `book2_decision_level1.json`
- `book3_pattern_level1.json`

---

### **Step 4: Push to Unity Repository**

**Repository:** `rashadwest/BTEBallCODE`  
**Path in Repo:** `Assets/StreamingAssets/Levels/`

**Process:**
1. **If level file is in local workflows repo:**
   ```bash
   # Copy file to Unity repo (if cloned locally)
   cp Unity-Scripts/Levels/book2_coding_level1.json \
      /path/to/BTEBallCODE/Assets/StreamingAssets/Levels/
   
   # Commit and push
   cd /path/to/BTEBallCODE
   git add Assets/StreamingAssets/Levels/book2_coding_level1.json
   git commit -m "Add Book 2 coding level 1"
   git push origin main
   ```

2. **If using GitHub UI:**
   - Go to: `https://github.com/rashadwest/BTEBallCODE`
   - Navigate to: `Assets/StreamingAssets/Levels/`
   - Click "Add file" → "Upload files"
   - Upload the JSON file
   - Commit: "Add Book 2 coding level 1"

3. **If using n8n automation:**
   - Trigger Unity Build Orchestrator workflow
   - Workflow handles commit and push automatically

---

### **Step 5: Automatic Build & Deployment**

**What Happens Automatically:**
1. ✅ GitHub Actions detects change to `Assets/**`
2. ✅ Workflow triggers automatically
3. ✅ Unity builds WebGL (10-15 minutes)
4. ✅ Build deploys to Netlify automatically
5. ✅ Game is live with new level!

**Monitor Build:**
- GitHub Actions: `https://github.com/rashadwest/BTEBallCODE/actions`
- Workflow: "Unity WebGL Build and Deploy"
- Watch real-time progress

---

## 🔄 AUTOMATION WORKFLOW

### **Complete Automation Process:**

```
1. Copy Template Level
   ↓
2. Modify Content (levelId, levelName, description, strategy, exercise)
   ↓
3. Save to Unity-Scripts/Levels/ (local)
   ↓
4. Push to Unity Repository (Assets/StreamingAssets/Levels/)
   ↓
5. GitHub Actions Auto-Triggers
   ↓
6. Unity Builds WebGL (10-15 min)
   ↓
7. Auto-Deploy to Netlify
   ↓
8. Game Live with New Level!
```

---

## 📝 QUICK REFERENCE: What to Change

### **For Each New Level:**

**Required Changes:**
- [ ] `levelId` (unique identifier)
- [ ] `levelName` (display name)
- [ ] `description` (what the level teaches)
- [ ] `strategy.steps[]` (dribble sequence)
- [ ] `exercise.blockCoding.targetCode` (or `exercise.math.mathConcept`)
- [ ] `tags` (update tags)

**Optional Changes:**
- [ ] `exercise.blockCoding.availableBlocks` (add more blocks)
- [ ] `learningObjectives` (update if needed)
- [ ] `successCriteria` (update if needed)
- [ ] `prerequisiteLevels` (add if needed)

**Keep the Same:**
- ✅ `gameMode` (blockcoding or math)
- ✅ `episodeNumber` (book number)
- ✅ `codingConcept` (concept type)
- ✅ `difficultyLevel` (difficulty)
- ✅ `videoPath` (empty for now)
- ✅ `videoConfig` (same structure)
- ✅ `scoring` (same structure)
- ✅ Overall JSON structure

---

## 🎯 LEVEL TEMPLATE STRUCTURE

### **Block Coding Level Template:**

```json
{
  "levels": [
    {
      "levelId": "book{BOOK}_coding_level{LEVEL}",
      "levelName": "Descriptive Name",
      "description": "What this level teaches",
      "gameMode": "blockcoding",
      "episodeNumber": {BOOK_NUMBER},
      "codingConcept": "basic_blocks_sequences",
      "difficultyLevel": 1,
      "strategy": {
        "steps": [
          {
            "stepNumber": 1,
            "action": "Description of action",
            "codeEquivalent": "BLOCK_1_POUND",
            "timing": 0.0
          }
        ]
      },
      "exercise": {
        "exerciseType": "BlockCoding",
        "blockCoding": {
          "availableBlocks": ["START", "BLOCK_1_POUND", "ADVANCE"],
          "requiredBlocks": ["BLOCK_1_POUND"],
          "targetCode": "START → BLOCK_1_POUND → ADVANCE"
        }
      }
    }
  ],
  "version": "1.0",
  "lastUpdated": "2025-12-21"
}
```

---

## 🚀 AUTOMATION COMMANDS

### **Quick Level Push Script:**

```bash
#!/bin/bash
# Quick Level Push - Automate level creation and push

LEVEL_ID="book2_coding_level1"
SOURCE_TEMPLATE="book1_foundation_block.json"
UNITY_REPO="/path/to/BTEBallCODE"

# 1. Copy template
cp "Unity-Scripts/Levels/${SOURCE_TEMPLATE}" \
   "Unity-Scripts/Levels/${LEVEL_ID}.json"

# 2. Modify content (requires manual edit or sed)
# ... modify levelId, levelName, description, etc. ...

# 3. Copy to Unity repo
cp "Unity-Scripts/Levels/${LEVEL_ID}.json" \
   "${UNITY_REPO}/Assets/StreamingAssets/Levels/"

# 4. Commit and push
cd "${UNITY_REPO}"
git add "Assets/StreamingAssets/Levels/${LEVEL_ID}.json"
git commit -m "Add ${LEVEL_ID}"
git push origin main

echo "✅ Level pushed! Build will auto-trigger."
```

---

## 📊 SYSTEM STATUS

**Current Status:**
- ✅ Level structure documented
- ✅ Push process documented
- ✅ Automation workflow defined
- ✅ Template structure saved
- ✅ Ready for repetitive use

**Next Steps:**
- Use this system for Book 1 and Book 2 levels
- Automate level creation when possible
- Save time by copying and modifying instead of creating from scratch

---

## 🔗 RELATED DOCUMENTS

- `CARBON-COPY-LEVELS-PLAN.md` - Detailed level creation plan
- `QUICK-START-ADD-LEVELS-TONIGHT.md` - Quick start guide
- `BALLCODE-STREAMLINED-DEVELOPMENT-PLAN.md` - Standard development process
- `Unity-Scripts/Levels/example_level_with_positions.json` - Example level file

---

**Version:** 1.0  
**Created:** December 21, 2025  
**Purpose:** Save level push system to memory for automation  
**Status:** ✅ Ready for use

