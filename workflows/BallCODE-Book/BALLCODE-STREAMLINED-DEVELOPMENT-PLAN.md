# BallCODE Streamlined Development Plan
## Organized Approach for Consistent Level & UI/UX Development

**Date:** December 11, 2025  
**Status:** Ready for Implementation  
**Purpose:** Standardize all game development processes

---

## 🎯 CORE PRINCIPLE: ONE PROCESS FOR EVERYTHING

**Rule:** Every level, section, and feature follows the SAME process:
1. **Define** → 2. **Create** → 3. **Test** → 4. **Build** → 5. **Deploy**

---

## 📋 STANDARD LEVEL CREATION PROCESS

### **Step 1: Define Level Requirements**

**Use This Template:**
```json
{
  "levelId": "book{BOOK}_mode{MODE}_level{LEVEL}",
  "levelName": "Descriptive Name",
  "gameMode": "blockcoding|math|training|prediction|freeplay",
  "episodeNumber": 0,
  "codingConcept": "sequences|conditionals|loops|state|data",
  "difficultyLevel": 1,
  "prerequisiteLevels": ["previous_level_id"],
  "learningObjectives": ["Objective 1", "Objective 2"],
  "successCriteria": ["Criterion 1", "Criterion 2"]
}
```

**Naming Convention:**
- `book1_blockcoding_level1` = Book 1, Block Coding, Level 1
- `book1_math_level1` = Book 1, Math Mode, Level 1
- `book2_blockcoding_level1` = Book 2, Block Coding, Level 1

---

### **Step 2: Create Level JSON**

**Location:** `Unity-Scripts/Levels/`  
**File Name:** `{levelId}.json`

**Standard Structure:**
```json
{
  "levels": [
    {
      "levelId": "book1_blockcoding_level1",
      "levelName": "Foundation Block: Basic Sequence",
      "description": "Learn basic block sequences",
      "gameMode": "blockcoding",
      "episodeNumber": 0,
      "codingConcept": "sequences",
      "strategy": {
        "strategyName": "Basic Pound Sequence",
        "strategyType": "offensive",
        "steps": [
          {
            "stepNumber": 1,
            "action": "Start at top of key",
            "codeEquivalent": "START",
            "timing": 0.0,
            "playerPositions": [
              {
                "x": 47.0,
                "y": 40.0,
                "playerId": "Nova",
                "dribbleType": 0,
                "dribbleDirection": "none",
                "isNormalized": false
              }
            ]
          },
          {
            "stepNumber": 2,
            "action": "Pound dribble forward",
            "codeEquivalent": "BLOCK_1_POUND",
            "timing": 0.5,
            "playerPositions": [
              {
                "x": 47.0,
                "y": 35.0,
                "playerId": "Nova",
                "dribbleType": 1,
                "dribbleDirection": "forward",
                "isNormalized": false
              }
            ]
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
      },
      "learningObjectives": [
        "Understand basic sequences",
        "Practice block placement"
      ],
      "successCriteria": [
        "Complete sequence correctly",
        "Use required blocks"
      ],
      "difficultyLevel": 1,
      "isUnlocked": true,
      "author": "BallCODE Team",
      "createdDate": "2025-12-11"
    }
  ],
  "version": "1.0",
  "lastUpdated": "2025-12-11"
}
```

---

### **Step 3: UI/UX Consistency Standards**

**Every Level Must Have:**

1. **Consistent UI Elements:**
   - Basketball court with grid overlay (standardized)
   - Block code area (top right corner)
   - Generated code display (below blocks)
   - Navigation: House (menu), Reverse (back), Delete
   - Magnifying glass (video playback) - if applicable

2. **Standard Layout:**
   ```
   ┌─────────────────────────────────────┐
   │  [House] [Video]    [Block Area]   │
   │                                     │
   │  [Court Visualization]              │
   │                                     │
   │  [Generated Code Display]           │
   │  [Navigation: Reverse, Delete]      │
   └─────────────────────────────────────┘
   ```

3. **Color Scheme (Standardized):**
   - Court: Standard basketball court colors
   - Blocks: Consistent block colors per type
   - UI Elements: Consistent across all levels

4. **Interaction Patterns:**
   - Drag & drop blocks (same behavior everywhere)
   - Click to execute (same feedback everywhere)
   - Error messages (same style everywhere)

---

### **Step 4: Level Organization by Book & Mode**

**Structure:**
```
Book 1 (Sequences)
├── Block Coding Levels
│   ├── Level 1.1: Basic Sequence
│   ├── Level 1.2: Multiple Dribbles
│   └── Level 1.3: Long Sequences
├── Math Levels
│   ├── Level 1.1: Count the Pounds
│   ├── Level 1.2: Sequence Math
│   └── Level 1.3: Pattern Recognition
└── Training Levels
    ├── Level 1.1: State Tracking
    └── Level 1.2: Position Analysis

Book 2 (Conditionals)
├── Block Coding Levels
│   ├── Level 2.1: Basic Conditionals
│   └── Level 2.2: Nested Conditionals
└── [Same pattern...]
```

**Rule:** Each book has the same mode structure for consistency

---

## 🔄 STANDARDIZED WORKFLOW PROCESS

### **For Adding New Levels:**

1. **Create Level JSON** (using template above)
2. **Save to:** `Unity-Scripts/Levels/{levelId}.json`
3. **Commit to Git:** `git add Unity-Scripts/Levels/{levelId}.json`
4. **Push:** `git push origin main`
5. **Trigger Build:** n8n workflow automatically builds
6. **Deploy:** Automatically deploys to Netlify

**OR Use n8n Workflow:**
- Send webhook request with level data
- Workflow creates JSON file
- Commits and pushes automatically
- Builds and deploys

---

## 📐 UI/UX STANDARDS CHECKLIST

**Before Finalizing Any Level:**

- [ ] Court visualization matches standard layout
- [ ] Block area uses standard positioning
- [ ] Navigation buttons in standard locations
- [ ] Color scheme matches game palette
- [ ] Font sizes consistent (16px minimum for mobile)
- [ ] Touch targets 44x44px minimum
- [ ] Error messages use standard format
- [ ] Success feedback uses standard animation
- [ ] Loading states use standard spinner
- [ ] Transitions use standard timing (0.3s)

---

## 🎮 GAME MODE STANDARDS

### **Block Coding Mode:**
- **UI:** Block palette (left), Code area (right), Court (center)
- **Interaction:** Drag blocks, click execute
- **Feedback:** Visual code generation, execution animation

### **Math Mode:**
- **UI:** Problem display (top), Input area (center), Court visualization (background)
- **Interaction:** Number input, calculation buttons
- **Feedback:** Correct/incorrect indicators

### **Training Mode:**
- **UI:** Video player (left), Analysis area (right), Court overlay
- **Interaction:** Video controls, analysis tools
- **Feedback:** Analysis results, progress indicators

**Rule:** Each mode has consistent UI across all levels

---

## 📦 BUILD REQUEST FORMAT

**To trigger build via n8n:**

```json
{
  "request": "Build BallCode game with latest levels and UI updates",
  "actionPlan": {
    "needsUnityEdits": true,
    "needsBuild": true,
    "needsDeploy": true,
    "unityEdits": [
      {
        "file": "Assets/StreamingAssets/Levels/new_level.json",
        "action": "add",
        "changes": "Add new level following standard template"
      }
    ],
    "estimatedTime": "20 minutes",
    "priority": "high"
  }
}
```

---

## ✅ QUALITY CHECKLIST

**Before Pushing Any Level:**

- [ ] Follows naming convention
- [ ] Uses standard JSON structure
- [ ] Has all required fields
- [ ] Player positions are valid (0-94 x, 0-50 y)
- [ ] Dribble types are valid (0-7)
- [ ] Learning objectives are clear
- [ ] Success criteria are measurable
- [ ] UI elements match standards
- [ ] Tested in Unity editor
- [ ] No console errors

---

## 🚀 QUICK START: Add Your First Level

1. **Copy template** from this document
2. **Fill in level details**
3. **Save as:** `Unity-Scripts/Levels/book1_blockcoding_level1.json`
4. **Test in Unity**
5. **Commit & push**
6. **Workflow builds automatically**

---

**Remember:** Consistency is key! Every level follows the same process.


