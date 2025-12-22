# Existing Games Action Plan
## Focus: Block Coding, Math, Chess, Tutorial (Before Python)

**Date:** December 10, 2025  
**Status:** Active Priority  
**Goal:** Expand existing games first, then return to Python later

---

## 🎯 PRIORITY FOCUS

**Current Status:**
- ✅ **Block Coding:** 1 level (book1_foundation_block)
- ✅ **Math:** 1 level (math_level_1)
- ✅ **Chess:** 1 level (chess_level_1)
- ✅ **Tutorial:** 1 level (full tutorial)

**What We Need:**
- 🔴 **HIGH:** More Math levels (same format)
- 🔴 **HIGH:** More Coding levels (same format)
- 🔴 **HIGH:** Chess multiplayer system
- 🟡 **MEDIUM:** Tutorial enhancements (shots, pivots)

**Python Game:** ⏸️ **LAST PRIORITY** - Can work on Python 1.0 this week, but only if everything else is working/complete. Add to mix when other things are done, before starting next chapters.

---

## 📋 ACTION ITEMS BY GAME MODE

### 1. 🧮 MATH GAME (High Priority)

**Current:** 1 level exists  
**Need:** Multiple levels with same format

#### Math Level 1 (Existing):
- ✅ `book1_math_foundation.json` - Already created
- ✅ Format: Math problems using basketball moves
- ✅ Concept: Order of operations

#### Math Levels to Create (Carbon Copy Approach):

**Book 1 - Sequences (Counting):**
- [ ] **Math Level 1.2:** "Count the Pounds"
  - **Concept:** Counting sequences
  - **Task:** Count how many pound dribbles needed
  - **Format:** Carbon copy `book1_math_foundation.json`
  - **Difficulty:** Beginner
  - **Approach:** Copy structure, change content

- [ ] **Math Level 1.3:** "Add the Moves"
  - **Concept:** Addition with moves
  - **Task:** Add point values of moves
  - **Format:** Carbon copy `book1_math_foundation.json`
  - **Difficulty:** Beginner
  - **Approach:** Copy structure, change content

**Book 2 - Conditionals (Formulas):**
- [ ] **Math Level 2.1:** "If/Then Math"
  - **Concept:** Conditional math
  - **Task:** Solve formulas with conditions
  - **Format:** Same as existing math level
  - **Difficulty:** Intermediate

- [ ] **Math Level 2.2:** "Decision Math"
  - **Concept:** Math with decisions
  - **Task:** Calculate based on choices
  - **Format:** Same as existing math level
  - **Difficulty:** Intermediate

**Book 3 - Loops (Patterns):**
- [ ] **Math Level 3.1:** "Pattern Math"
  - **Concept:** Pattern recognition in math
  - **Task:** Find patterns in sequences
  - **Format:** Same as existing math level
  - **Difficulty:** Intermediate

**Reference Format:**
- Use `book1_math_foundation.json` as template
- Keep same structure
- Change: concept, task, difficulty

---

### 2. 💻 BLOCK CODING GAME (High Priority)

**Current:** 1 level exists (book1_foundation_block)  
**Need:** Multiple levels with same format

#### Coding Level 1 (Existing):
- ✅ `book1_foundation_block.json` - Already created
- ✅ Format: Block coding sequences
- ✅ Concept: Basic blocks, sequences

#### Coding Levels to Create (Carbon Copy Approach):

**Book 1 - Sequences:**
- [ ] **Coding Level 1.2:** "Multiple Dribbles"
  - **Concept:** Sequences with different dribbles
  - **Task:** Create sequence: START → POUND → CROSSOVER → POUND → ADVANCE
  - **Format:** Carbon copy `book1_foundation_block.json`
  - **Difficulty:** Beginner
  - **Available Blocks:** START, BLOCK_1_POUND, BLOCK_2_CROSSOVER, ADVANCE
  - **Approach:** Copy structure, change dribble sequence

- [ ] **Coding Level 1.3:** "Long Sequences"
  - **Concept:** Longer sequences
  - **Task:** Create 5+ move sequence
  - **Format:** Carbon copy `book1_foundation_block.json`
  - **Difficulty:** Beginner
  - **Approach:** Copy structure, extend sequence

**Book 2 - Conditionals:**
- [ ] **Coding Level 2.1:** "If Defender Close"
  - **Concept:** Conditionals
  - **Task:** Use IF/THEN blocks
  - **Format:** Same as book1_foundation_block (add IF/THEN blocks)
  - **Difficulty:** Intermediate
  - **Available Blocks:** START, IF, THEN, ELSE, BLOCK_1_POUND, BLOCK_2_CROSSOVER, ADVANCE, BUCKET

- [ ] **Coding Level 2.2:** "Multiple Conditions"
  - **Concept:** Complex conditionals
  - **Task:** Use multiple IF/THEN/ELSE
  - **Format:** Same as book1_foundation_block
  - **Difficulty:** Intermediate

**Book 3 - Loops:**
- [ ] **Coding Level 3.1:** "Repeat the Move"
  - **Concept:** Loops
  - **Task:** Use REPEAT blocks
  - **Format:** Same as book1_foundation_block (add REPEAT blocks)
  - **Difficulty:** Intermediate
  - **Available Blocks:** START, REPEAT, BLOCK_1_POUND, BLOCK_2_CROSSOVER, ADVANCE, BUCKET

- [ ] **Coding Level 3.2:** "Nested Loops"
  - **Concept:** Nested loops
  - **Task:** Use loops inside loops
  - **Format:** Same as book1_foundation_block
  - **Difficulty:** Advanced

**Reference Format:**
- **Carbon copy** `book1_foundation_block.json` as template
- Keep same structure (infrastructure already handles it)
- Change: levelId, levelName, description, strategy.steps, targetCode
- **No need to overthink** - just duplicate and modify content
- See: `CARBON-COPY-LEVELS-PLAN.md` for detailed approach

---

### 3. ♟️ CHESS GAME (High Priority)

**Current:** 1 level exists  
**Need:** Multiplayer system (two players on different computers)

#### Chess Level 1 (Existing):
- ✅ `chess_level_1` - Already created
- ✅ Format: Chess-like strategy game
- ✅ Concept: Strategic thinking

#### Chess Enhancements to Create:

**Multiplayer System:**
- [ ] **Chess Multiplayer Architecture**
  - **Goal:** Two players on different computers
  - **Components:**
    - [ ] Network connection system
    - [ ] Player matching system
    - [ ] Real-time move synchronization
    - [ ] Turn-based gameplay
    - [ ] Connection status indicators
  - **Priority:** High
  - **Timeline:** 2-3 weeks

**Additional Chess Levels:**
- [ ] **Chess Level 2.1:** "Advanced Strategy"
  - **Concept:** Advanced chess tactics
  - **Task:** More complex scenarios
  - **Format:** Same as chess_level_1
  - **Difficulty:** Intermediate

- [ ] **Chess Level 2.2:** "Competitive Play"
  - **Concept:** Competitive scenarios
  - **Task:** Play against AI or player
  - **Format:** Same as chess_level_1
  - **Difficulty:** Advanced

**Reference Format:**
- Use existing chess level as template
- Add multiplayer components
- Keep same game mechanics

---

### 4. 📚 TUTORIAL GAME (Medium Priority)

**Current:** 1 full tutorial exists  
**Need:** Tutorials for shots, pivots, etc.

#### Tutorial Level (Existing):
- ✅ Full tutorial - Goes through each dribble
- ✅ Format: Step-by-step teaching
- ✅ Concept: Foundation skills

#### Tutorial Enhancements to Create:

**Shot Tutorials:**
- [ ] **Tutorial: Layup Shot**
  - **Concept:** Learn layup
  - **Shows:** How to do layup
  - **Practice:** Make 5 layups
  - **Learning:** Close-range shot
  - **Format:** Same as existing tutorial

- [ ] **Tutorial: Jump Shot**
  - **Concept:** Learn jump shot
  - **Shows:** How to shoot
  - **Practice:** Make 5 shots
  - **Learning:** Shooting form
  - **Format:** Same as existing tutorial

- [ ] **Tutorial: Three-Pointer**
  - **Concept:** Learn long shot
  - **Shows:** How to shoot from far
  - **Practice:** Make 3 three-pointers
  - **Learning:** Long-range shooting
  - **Format:** Same as existing tutorial

**Pivot Tutorials:**
- [ ] **Tutorial: Pivot Left**
  - **Concept:** Learn left pivot
  - **Shows:** How to pivot left
  - **Practice:** Do it 5 times
  - **Learning:** Footwork
  - **Format:** Same as existing tutorial

- [ ] **Tutorial: Pivot Right**
  - **Concept:** Learn right pivot
  - **Shows:** How to pivot right
  - **Practice:** Do it 5 times
  - **Learning:** Footwork
  - **Format:** Same as existing tutorial

**Reference Format:**
- Use existing tutorial as template
- Keep same step-by-step structure
- Change: skill being taught, practice requirements

---

## 🎯 IMPLEMENTATION PRIORITY

**See:** `PHASED-DEVELOPMENT-PLAN.md` for complete phased approach

### Phase 1: Level Development (Week 1)
- [ ] Block Coding 1.2, 1.3
- [ ] Math 1.2, 1.3
- [ ] Tutorial 1.2, 1.3

### Phase 2: Chess Improvements (Week 2)
- [ ] Chess level improvements
- [ ] Multiplayer architecture
- [ ] Chess UI/UX

### Phase 3: UI/UX Enhancements (Week 3)
- [ ] Critical fixes (localhost-first)
- [ ] Kid-friendly elements
- [ ] Visual feedback

### Phase 4: Integration & Testing (Week 4)
- [ ] System integration
- [ ] End-to-end testing
- [ ] Final polish

### Week 2: Continue High Priority

**Day 1-2: More Math Levels**
- [ ] Create Math Level 2.1
- [ ] Create Math Level 2.2

**Day 3-4: More Coding Levels**
- [ ] Create Coding Level 2.1
- [ ] Create Coding Level 2.2

**Day 5: Chess Multiplayer Start**
- [ ] Begin multiplayer implementation
- [ ] Set up network infrastructure

### Week 3: Medium Priority + Continue

**Day 1-2: Tutorial Enhancements**
- [ ] Create Layup Tutorial
- [ ] Create Jump Shot Tutorial

**Day 3-4: Continue High Priority**
- [ ] Create Math Level 3.1
- [ ] Create Coding Level 3.1

**Day 5: Chess Multiplayer Continue**
- [ ] Continue multiplayer development

---

## 📊 SUCCESS CRITERIA

### Math Game:
- ✅ 5+ math levels created
- ✅ All use same format
- ✅ Cover sequences, conditionals, loops
- ✅ Tested and working

### Block Coding Game:
- ✅ 5+ coding levels created
- ✅ All use same format
- ✅ Cover sequences, conditionals, loops
- ✅ Tested and working

### Chess Game:
- ✅ Multiplayer system designed
- ✅ Two players can play on different computers
- ✅ Real-time synchronization working
- ✅ Tested and working

### Tutorial Game:
- ✅ 3+ shot tutorials created
- ✅ 2+ pivot tutorials created
- ✅ All use same format
- ✅ Tested and working

---

## 🎨 UI/UX IMPROVEMENTS (Parallel Work)

**Using AIMCODE with Steve Jobs Expert + Duolingo/Notion Inspiration**

**⚠️ CRITICAL: All UI/UX work on localhost first for preview before pushing!**

**Timeline:** Parallel with game development

**Week 1: Critical Fixes (Localhost First)**
- [ ] Fix buttons out of place (test on localhost)
- [ ] Fix words/text out of place (test on localhost)
- [ ] Make it kid-friendly (Duolingo style) (test on localhost)
- [ ] Fix navigation confusion (test on localhost)

**Week 2: Enhancements (Localhost First)**
- [ ] Add progress indicators (Duolingo style) (test on localhost)
- [ ] Add celebration animations (test on localhost)
- [ ] Add gamification (points, badges) (test on localhost)
- [ ] Improve design consistency (test on localhost)

**Week 3: Polish (Localhost First)**
- [ ] Mobile optimization (test on localhost)
- [ ] Accessibility improvements (test on localhost)
- [ ] Final polish (test on localhost)

**See:** `UI-UX-IMPROVEMENT-PLAN.md` for full details

---

## 🎬 VIDEO INTEGRATION (Critical for Level Development)

**Status:** Needs clarification and video information

**Current State:**
- ✅ Level JSON structure has `videoPath` field (but empty)
- ✅ Video config settings exist
- ✅ Dribble sequences defined in `strategy.steps`
- ❌ **No videos connected to levels**
- ❌ **Need video file information**

**What We Need:**
- [ ] Video file locations/paths
- [ ] Video format (.mp4, .mov, etc.)
- [ ] Video-to-level mapping (which video for which level)
- [ ] Dribble sequence in video (how to show "you need to do this move")
- [ ] Video integration structure (how videos connect to exercises)

**See:** `VIDEO-INTEGRATION-EXPLANATION.md` for full details and questions

---

## 🔄 AFTER EXISTING GAMES ARE EXPANDED

**Then we can return to:**
- 🐍 Python Coding Game (ideation phase)
- 🐍 1-2 Python levels for testing
- 🐍 Evaluate concept before full build

---

## 📋 QUICK REFERENCE

### Level JSON Template Location:
- **Math:** `Unity-Scripts/Levels/book1_math_foundation.json`
- **Coding:** `Unity-Scripts/Levels/book1_foundation_block.json`
- **Chess:** Existing chess level structure
- **Tutorial:** Existing tutorial structure

### Key Files:
- `curriculum-schema.json` - Update with new levels
- `LEVEL-IDEATIONS-COMPLETE.md` - Reference for level ideas
- `GAME-MODES-ELI10-EXPLAINED.md` - Understand each game mode

---

**Status:** Active - Focus on existing games  
**Python:** Paused until existing games expanded  
**Next Step:** Start with Math Level 1.2


