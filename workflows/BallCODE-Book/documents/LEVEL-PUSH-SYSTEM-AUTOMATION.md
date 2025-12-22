# Level Push System - Automation Memory

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 22, 2025 (Updated)  
**Status:** ✅ Documented for Automation - Complete with Curriculum Integration  
**Purpose:** Save the level push system to memory for repetitive automation  
**Last Updated:** December 22, 2025

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
- `levelId`: Unique identifier (e.g., `book2_decision_crossover`)
- `levelName`: Display name (e.g., "Decision Crossover Exercise")
- `description`: What the level teaches
- `episodeNumber`: Book number (0 = Book 1, 1 = Book 2, 2 = Book 3, etc.)
- `codingConcept`: Concept type (e.g., `basic_blocks_sequences`, `if_then_conditionals`, `loops_repetition`)
- `strategy.steps[]`: Dribble sequence/actions
- `exercise.blockCoding.targetCode`: Target code sequence (or `exercise.math.mathConcept` for math)
- `exercise.blockCoding.availableBlocks`: Blocks available for this level
- `exercise.blockCoding.requiredBlocks`: Blocks required to complete
- `curriculum`: **MANDATORY** - Complete curriculum section (see below)
- `tags`: Update tags for new level
- `prerequisiteLevels`: Add previous level IDs if needed

**What to Keep (Same):**
- `gameMode`: "blockcoding" (for book levels - uses same logic as coding game)
- `exerciseType`: "BlockCoding" (for block coding levels)
- `difficultyLevel`: Difficulty (1 = beginner, 2 = intermediate, 3 = advanced)
- Overall JSON structure and format
- `videoPath`: Empty for now
- `videoConfig`: Same structure
- `scoring`: Same structure
- `learningObjectives`: Structure (update content)
- `successCriteria`: Structure (update content)

**Optional Changes:**
- `learningObjectives`: Update content (keep structure)
- `successCriteria`: Update content (keep structure)
- `strategy.strategyName`: Update for new strategy
- `strategy.strategyType`: Update if needed

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
- [ ] `episodeNumber` (book number: 0=Book1, 1=Book2, 2=Book3, etc.)
- [ ] `codingConcept` (concept type: `basic_blocks_sequences`, `if_then_conditionals`, `loops_repetition`)
- [ ] `strategy.steps[]` (dribble sequence)
- [ ] `exercise.blockCoding.targetCode` (target code sequence)
- [ ] `exercise.blockCoding.availableBlocks` (blocks available)
- [ ] `exercise.blockCoding.requiredBlocks` (blocks required)
- [ ] `curriculum` (MANDATORY - complete curriculum section)
- [ ] `prerequisiteLevels` (previous level IDs if needed)
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

## 📚 CURRICULUM INTEGRATION (MANDATORY)

**CRITICAL:** Every new level MUST include a complete `curriculum` section. This is mandatory for all book levels.

### **Curriculum Section Structure:**

```json
"curriculum": {
  "gradeLevels": ["3-5", "6-8", "9-12"],
  "standards": {
    "csta": ["1B-AP-10", "1B-AP-11"],
    "commonCore": ["MP.2", "MP.7"],
    "ngss": ["ETS1-2"]
  },
  "phases": {
    "phase1": {
      "name": "Sports Language (Block Coding)",
      "description": "Learn [concept] using basketball terminology. Visual block interface: [example]",
      "example": "[Block code example]",
      "learningObjective": "Students understand [concept]"
    },
    "phase2": {
      "name": "Transition Bridge",
      "description": "See how [concept] maps to Python code. Side-by-side view: Block | Python",
      "example": "Block: [example]\nCode: [Python example]",
      "learningObjective": "Students understand that blocks = code"
    },
    "phase3": {
      "name": "Python Learning",
      "description": "Write Python code for [concept]. Create [type] programs",
      "example": "[Python code example]",
      "learningObjective": "Students can write Python [concept]"
    }
  },
  "concepts": {
    "python": "[Python concept name]",
    "pythonSyntax": "[Python syntax example]",
    "aiConcept": "[AI concept]",
    "mathConcept": "[Math concept]"
  },
  "basketball": {
    "skill": "[Basketball skill name]",
    "level": [skill_level_number],
    "context": "[Context description]"
  }
}
```

### **What to Update in Curriculum:**

**For Each New Level:**
- [ ] `gradeLevels`: Usually `["3-5", "6-8", "9-12"]` (adjust if needed)
- [ ] `standards.csta`: Update with relevant CSTA standards
- [ ] `standards.commonCore`: Update with relevant Common Core standards
- [ ] `standards.ngss`: Update with relevant NGSS standards
- [ ] `phases.phase1`: Update description, example, learning objective
- [ ] `phases.phase2`: Update description, example, learning objective
- [ ] `phases.phase3`: Update description, example, learning objective
- [ ] `concepts.python`: Update Python concept name
- [ ] `concepts.pythonSyntax`: Update Python syntax example
- [ ] `concepts.aiConcept`: Update AI concept
- [ ] `concepts.mathConcept`: Update math concept
- [ ] `basketball.skill`: Update basketball skill name
- [ ] `basketball.level`: Update skill level number
- [ ] `basketball.context`: Update context description

### **Curriculum Examples by Book:**

**Book 1 (Sequences):**
- Python: "Sequences"
- Python Syntax: "Sequential code execution"
- AI Concept: "Step-by-step reasoning"
- Basketball Skill: "Pound Dribble"

**Book 2 (Conditionals):**
- Python: "Conditionals"
- Python Syntax: "if condition: action"
- AI Concept: "Decision-making logic"
- Basketball Skill: "Crossover Dribble"

**Book 3 (Loops):**
- Python: "Loops"
- Python Syntax: "for i in range(3): action"
- AI Concept: "Pattern recognition and repetition"
- Basketball Skill: "In & Out Dribble"

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

---

## ✅ COMPLETED EXAMPLES

### **Book 1: Foundation Block** (`book1_foundation_block.json`)
- ✅ Complete with curriculum
- ✅ Uses `blockcoding` game mode
- ✅ Concept: `basic_blocks_sequences`
- ✅ Prerequisites: None (starting level)

### **Book 2: Decision Crossover** (`book2_decision_crossover.json`)
- ✅ Complete with curriculum
- ✅ Uses `blockcoding` game mode
- ✅ Concept: `if_then_conditionals`
- ✅ Prerequisites: `["book1_foundation_block"]`

### **Book 3: Pattern Loop** (`book3_pattern_loop.json`)
- ✅ Complete with curriculum
- ✅ Uses `blockcoding` game mode
- ✅ Concept: `loops_repetition`
- ✅ Prerequisites: `["book1_foundation_block", "book2_decision_crossover"]`

**All three levels follow this exact process and are ready for Unity integration.**

---

## 🎯 QUICK COPY-PASTE TEMPLATE

**To create a new level, copy this structure:**

1. Copy `book1_foundation_block.json` (or most recent similar level)
2. Update all required fields (see checklist above)
3. **MANDATORY:** Add/update complete `curriculum` section
4. Save as `book{N}_{concept}_{name}.json`
5. Push to Unity repository
6. Build auto-triggers

**Time to create new level:** ~15-20 minutes (copy + modify + push)

---

**Version:** 2.0  
**Created:** December 21, 2025  
**Last Updated:** December 22, 2025  
**Purpose:** Save level push system to memory for automation  
**Status:** ✅ Complete - Ready for use with curriculum integration

