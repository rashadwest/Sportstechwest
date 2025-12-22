# Carbon Copy Levels Plan
## Use Existing Infrastructure - Just Duplicate & Modify

**Date:** December 10, 2025  
**Status:** Ready to Execute  
**Approach:** Copy existing level structure, modify content

---

## 🎯 UNDERSTANDING

### Infrastructure Already Exists:
- ✅ `LevelDataManager.cs` - Auto-loads JSON files from `StreamingAssets/Levels/`
- ✅ Just add JSON file → System loads it automatically
- ✅ Organizes by gameMode, episodeNumber, codingConcept
- ✅ Handles prerequisites, unlocking, progression

### Current Levels (1.1):
- ✅ `book1_foundation_block.json` - Block coding (1.1)
- ✅ `book1_math_foundation.json` - Math (1.1)

### Strategy:
- **1.x levels:** Carbon copy structure, change content
- **2.0 levels:** Get creative (conditionals, more complex)
- **Focus:** Setting the stage for coding + basketball together

---

## 📋 CARBON COPY TEMPLATE

### Block Coding Levels (1.2, 1.3, etc.)

**Base Template:** `book1_foundation_block.json`

**What to Change:**
1. `levelId`: `book1_coding_1_2`, `book1_coding_1_3`, etc.
2. `levelName`: "Multiple Dribbles Exercise", "Long Sequences Exercise", etc.
3. `description`: Update to match new sequence
4. `strategy.steps[]`: Change dribble sequence
5. `exercise.blockCoding.availableBlocks`: Add more blocks if needed
6. `exercise.blockCoding.targetCode`: Update target sequence
7. `tags`: Update tags

**What to Keep:**
- Same `gameMode`: "blockcoding"
- Same `episodeNumber`: 0 (Book 1)
- Same `codingConcept`: "basic_blocks_sequences"
- Same `difficultyLevel`: 1
- Same structure/format

---

### Math Levels (1.2, 1.3, etc.)

**Base Template:** `book1_math_foundation.json`

**What to Change:**
1. `levelId`: `book1_math_1_2`, `book1_math_1_3`, etc.
2. `levelName`: "Count the Pounds", "Add the Moves", etc.
3. `description`: Update math concept
4. `strategy.steps[]`: Change counting/sequence
5. `exercise.math.mathConcept`: Update concept
6. `tags`: Update tags

**What to Keep:**
- Same `gameMode`: "math"
- Same `episodeNumber`: 0 (Book 1)
- Same `codingConcept`: "basic_blocks_sequences"
- Same `difficultyLevel`: 1
- Same structure/format

---

## 🎮 LEVEL IDEAS (1.x - Setting the Stage)

### Block Coding 1.2: "Multiple Dribbles"
**Copy from:** `book1_foundation_block.json`

**Changes:**
- `levelId`: `book1_coding_1_2`
- `levelName`: "Multiple Dribbles Exercise"
- `description`: "Practice using different dribbles in a sequence. Learn Block 1 (Pound) and Block 2 (Crossover)."
- `strategy.steps`: 
  - Step 1: START → BLOCK_1_POUND
  - Step 2: BLOCK_2_CROSSOVER
  - Step 3: BLOCK_1_POUND
  - Step 4: ADVANCE
- `availableBlocks`: ["START", "BLOCK_1_POUND", "BLOCK_2_CROSSOVER", "ADVANCE"]
- `targetCode`: "START → BLOCK_1_POUND → BLOCK_2_CROSSOVER → BLOCK_1_POUND → ADVANCE"

---

### Block Coding 1.3: "Long Sequences"
**Copy from:** `book1_foundation_block.json`

**Changes:**
- `levelId`: `book1_coding_1_3`
- `levelName`: "Long Sequences Exercise"
- `description`: "Create longer sequences with multiple dribbles. Practice building complex moves."
- `strategy.steps`: 
  - Step 1: START → BLOCK_1_POUND
  - Step 2: BLOCK_1_POUND
  - Step 3: BLOCK_2_CROSSOVER
  - Step 4: BLOCK_2_CROSSOVER
  - Step 5: BLOCK_1_POUND
  - Step 6: ADVANCE
- `availableBlocks`: ["START", "BLOCK_1_POUND", "BLOCK_2_CROSSOVER", "ADVANCE"]
- `targetCode`: "START → BLOCK_1_POUND → BLOCK_1_POUND → BLOCK_2_CROSSOVER → BLOCK_2_CROSSOVER → BLOCK_1_POUND → ADVANCE"

---

### Math 1.2: "Count the Pounds"
**Copy from:** `book1_math_foundation.json`

**Changes:**
- `levelId`: `book1_math_1_2`
- `levelName`: "Count the Pounds Exercise"
- `description`: "Count how many pound dribbles are in a sequence. Practice counting sequences."
- `strategy.steps`: 
  - Step 1: COUNT = 1 (first pound)
  - Step 2: COUNT = 2 (second pound)
  - Step 3: COUNT = 3 (third pound)
  - Step 4: COUNT = 4 (fourth pound)
  - Step 5: IF COUNT >= 4 THEN ADVANCE
- `mathConcept`: "counting_sequences_extended"

---

### Math 1.3: "Add the Moves"
**Copy from:** `book1_math_foundation.json`

**Changes:**
- `levelId`: `book1_math_1_3`
- `levelName`: "Add the Moves Exercise"
- `description`: "Add point values of different moves. Learn that each move has a value."
- `strategy.steps`: 
  - Step 1: POUND = 1 point
  - Step 2: CROSSOVER = 2 points
  - Step 3: TOTAL = POUND + CROSSOVER = 3 points
  - Step 4: IF TOTAL >= 3 THEN ADVANCE
- `mathConcept`: "addition_sequences"

---

## 🚀 IMPLEMENTATION STEPS

### Step 1: Create Block Coding 1.2
1. Copy `book1_foundation_block.json`
2. Rename to `book1_coding_1_2.json`
3. Update fields (see above)
4. Save to `Unity-Scripts/Levels/`

### Step 2: Create Block Coding 1.3
1. Copy `book1_foundation_block.json`
2. Rename to `book1_coding_1_3.json`
3. Update fields (see above)
4. Save to `Unity-Scripts/Levels/`

### Step 3: Create Math 1.2
1. Copy `book1_math_foundation.json`
2. Rename to `book1_math_1_2.json`
3. Update fields (see above)
4. Save to `Unity-Scripts/Levels/`

### Step 4: Create Math 1.3
1. Copy `book1_math_foundation.json`
2. Rename to `book1_math_1_3.json`
3. Update fields (see above)
4. Save to `Unity-Scripts/Levels/`

---

## 📝 QUICK REFERENCE: What to Change

### For Each New Level:

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

**Keep the Same:**
- ✅ `gameMode` (blockcoding or math)
- ✅ `episodeNumber` (0 for Book 1)
- ✅ `codingConcept` (basic_blocks_sequences for 1.x)
- ✅ `difficultyLevel` (1 for 1.x levels)
- ✅ `videoPath` (empty for now)
- ✅ `videoConfig` (same structure)
- ✅ `scoring` (same structure)
- ✅ Overall JSON structure

---

## 🎯 LEVEL PROGRESSION (1.x)

### Book 1 - Sequences (Setting the Stage):

**Block Coding:**
- 1.1: Foundation Block (Pound × 3) ✅ Exists
- 1.2: Multiple Dribbles (Pound + Crossover) ⏳ Create
- 1.3: Long Sequences (Multiple moves) ⏳ Create

**Math:**
- 1.1: Foundation Math (Counting) ✅ Exists
- 1.2: Count the Pounds (Extended counting) ⏳ Create
- 1.3: Add the Moves (Addition) ⏳ Create

**Focus:** Simple sequences, setting the stage for coding + basketball together

---

## 🔄 WHEN WE GET TO 2.0

**Then we get creative:**
- Conditionals (IF/THEN)
- More complex sequences
- Decision-making
- Different game mechanics

**For now:** Keep it simple, carbon copy structure, focus on 1.x levels

---

## ✅ SUCCESS CRITERIA

- [ ] Block Coding 1.2 created (carbon copy)
- [ ] Block Coding 1.3 created (carbon copy)
- [ ] Math 1.2 created (carbon copy)
- [ ] Math 1.3 created (carbon copy)
- [ ] All levels load in Unity
- [ ] All levels follow same structure
- [ ] Ready for 2.0 creative work

---

**Status:** Ready to create levels  
**Approach:** Carbon copy existing structure  
**Focus:** 1.x levels - setting the stage


