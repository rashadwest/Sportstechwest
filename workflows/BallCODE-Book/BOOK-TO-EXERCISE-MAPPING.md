# Book-to-Exercise Mapping

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** November 26, 2025  
**Status:** Complete Mapping Document  
**Purpose:** Map each book to appropriate exercise type and game mode

---

## Mapping Overview

This document maps the three BallCODE books to Unity game exercises, defining which exercise types and game modes are appropriate for each book's learning objectives.

---

## Book 1: The Foundation Block

### Book Details
- **Title:** The Foundation Block
- **Dribble Level:** 1 (Pound Dribble)
- **Coding Concept:** Basic Blocks and Sequences
- **AI Concept:** Sequences and Patterns
- **Math Concept:** Basic Arithmetic and Counting

### Recommended Exercise Type: **Block Coding**

**Rationale:**
- Book teaches foundation blocks (Block 1: Pound Dribble)
- Students need to practice dragging and dropping blocks
- Exercise should reinforce: START → Block 1 → Block 1 → Block 1 → ADVANCE
- Block coding is the most appropriate for "foundation blocks" concept

### Recommended Game Mode: **Block Coding Mode**

**Rationale:**
- Block Coding Mode supports drag-and-drop block exercises
- Aligns with book's focus on basic blocks and sequences
- Students can practice repeating Block 1 (Pound) multiple times

### Exercise Configuration

**Block Coding Exercise:**
```csharp
BlockCodingExercise {
    availableBlocks: ["START", "BLOCK_1_POUND", "ADVANCE", "REPEAT"]
    requiredBlocks: ["BLOCK_1_POUND"]
    targetCode: "START → BLOCK_1_POUND → BLOCK_1_POUND → BLOCK_1_POUND → ADVANCE"
    allowCustomBlocks: false
}
```

**Scoring Configuration:**
```csharp
ScoringConfig {
    maxScore: 100
    passingScore: 70
    showScoreDuringExercise: false
    allowRetry: true
    maxAttempts: 3
}
```

**Learning Objectives:**
- Understand that coding starts with simple, repeatable blocks
- Practice creating sequences by repeating foundation blocks
- Learn that Block 1 (Pound) can be repeated to create sequences

**Success Criteria:**
- Correctly drag Block 1 (Pound) at least 3 times
- Create a sequence: START → Block 1 → Block 1 → Block 1 → ADVANCE
- Complete exercise with 70% or higher score

### Alternative Exercise Types (If Block Coding Not Available)

**Option 1: Analysis Exercise**
- Analyze video of pound dribble sequence
- Identify how many times Block 1 is repeated
- Answer questions about foundation blocks

**Option 2: Math Exercise**
- Count dribbles: "If Nova pounds 3 times, how many steps does she advance?"
- Calculate time: "3 Pounds × 0.5s = ?"
- Basic arithmetic through basketball context

---

## Book 2: The Code of Flow (The Decision Crossover)

### Book Details
- **Title:** The Code of Flow / The Decision Crossover
- **Dribble Level:** 2 (Crossover Dribble)
- **Coding Concept:** If/Then Conditionals
- **AI Concept:** Decision Trees and Conditional Logic
- **Math Concept:** Probability and Decision Making

### Recommended Exercise Type: **Block Coding** (with Conditionals)

**Rationale:**
- Book teaches if/then conditionals
- Students need to practice IF/THEN blocks with Block 2 (Crossover)
- Exercise should reinforce: IF [defender left] THEN [Block 2 right] ELSE [Block 2 left]
- Block coding with conditionals is most appropriate

### Recommended Game Mode: **Block Coding Mode**

**Rationale:**
- Block Coding Mode supports conditional blocks
- Aligns with book's focus on if/then decision-making
- Students can practice IF/THEN blocks with Block 2 (Crossover)

### Exercise Configuration

**Block Coding Exercise:**
```csharp
BlockCodingExercise {
    availableBlocks: ["START", "IF", "THEN", "ELSE", "BLOCK_2_CROSSOVER", "ADVANCE"]
    requiredBlocks: ["IF", "THEN", "BLOCK_2_CROSSOVER"]
    targetCode: "START → IF [defender left] THEN [BLOCK_2_CROSSOVER right] ELSE [BLOCK_2_CROSSOVER left] → ADVANCE"
    allowCustomBlocks: false
}
```

**Scoring Configuration:**
```csharp
ScoringConfig {
    maxScore: 100
    passingScore: 70
    showScoreDuringExercise: false
    allowRetry: true
    maxAttempts: 3
}
```

**Learning Objectives:**
- Understand that coding uses if/then to make decisions
- Practice creating conditional sequences
- Learn that Block 2 (Crossover) requires reading conditions

**Success Criteria:**
- Correctly use IF/THEN blocks
- Create conditional sequence with Block 2
- Complete exercise with 70% or higher score

### Alternative Exercise Types

**Option 1: Prediction Exercise**
- Predict what defender will do (left or right)
- Use prediction to decide crossover direction
- Reinforces decision-making based on conditions

**Option 2: Analysis Exercise**
- Analyze video of defender movements
- Identify patterns: "Defender goes left 70% of the time"
- Answer questions about conditional logic

---

## Book 3: The Pattern (In & Out Dribble)

### Book Details
- **Title:** The Pattern / The Deception Loop
- **Dribble Level:** 3 (In & Out Dribble)
- **Coding Concept:** Loops and Repetition
- **AI Concept:** Pattern Recognition and Loop Detection
- **Math Concept:** Sequences and Patterns

### Recommended Exercise Type: **Block Coding** (with Loops)

**Rationale:**
- Book teaches loops and repetition
- Students need to practice LOOP blocks with Block 3 (In & Out)
- Exercise should reinforce: LOOP [Block 3 fake] REPEAT 3, THEN [Block 3 real]
- Block coding with loops is most appropriate

### Recommended Game Mode: **Block Coding Mode**

**Rationale:**
- Block Coding Mode supports loop blocks
- Aligns with book's focus on repetition and pattern creation
- Students can practice LOOP blocks with Block 3 (In & Out)

### Exercise Configuration

**Block Coding Exercise:**
```csharp
BlockCodingExercise {
    availableBlocks: ["START", "LOOP", "REPEAT", "THEN", "BREAK", "BLOCK_3_IN_OUT", "ADVANCE"]
    requiredBlocks: ["LOOP", "REPEAT", "BLOCK_3_IN_OUT"]
    targetCode: "START → LOOP [BLOCK_3_IN_OUT fake] REPEAT 3, THEN [BLOCK_3_IN_OUT real] → ADVANCE"
    allowCustomBlocks: false
}
```

**Scoring Configuration:**
```csharp
ScoringConfig {
    maxScore: 100
    passingScore: 70
    showScoreDuringExercise: false
    allowRetry: true
    maxAttempts: 3
}
```

**Learning Objectives:**
- Understand that coding uses loops to repeat patterns
- Practice creating loop sequences
- Learn that Block 3 (In & Out) requires pattern creation and breaking

**Success Criteria:**
- Correctly use LOOP blocks
- Create loop sequence with Block 3
- Complete exercise with 70% or higher score

### Alternative Exercise Types

**Option 1: Analysis Exercise**
- Analyze video of in & out dribble pattern
- Identify loop structure: "Fake left, fake left, fake left, then go right"
- Answer questions about pattern recognition

**Option 2: Math Exercise**
- Calculate sequences: "Repeat fake 3 times, then go real"
- Pattern recognition: "What pattern creates best deception?"
- Sequence counting and pattern analysis

---

## Summary Table

| Book | Dribble Level | Coding Concept | Exercise Type | Game Mode | Level ID Pattern |
|------|---------------|----------------|---------------|-----------|-----------------|
| Book 1 | 1 (Pound) | Basic Blocks & Sequences | Block Coding | Block Coding Mode | `book1_foundation_block` |
| Book 2 | 2 (Crossover) | If/Then Conditionals | Block Coding (Conditionals) | Block Coding Mode | `book2_decision_crossover` |
| Book 3 | 3 (In & Out) | Loops & Repetition | Block Coding (Loops) | Block Coding Mode | `book3_pattern_loop` |

---

## Implementation Notes

### Exercise Type Priority

1. **Primary:** Block Coding (all books)
   - Most aligned with book concepts
   - Supports foundation blocks, conditionals, loops
   - Hands-on building activity (Resnick principle)

2. **Secondary:** Analysis Exercise
   - Good alternative if Block Coding not available
   - Reinforces concepts through video analysis
   - Supports visual learners (Reggio principle)

3. **Tertiary:** Math Exercise
   - Supports math concepts in books
   - Good for math-focused learning
   - Reinforces arithmetic and pattern recognition

### Game Mode Priority

1. **Primary:** Block Coding Mode
   - Best fit for all three books
   - Supports all exercise types needed
   - Aligns with constructionist learning (Resnick)

2. **Secondary:** Math Mode (for Book 1)
   - Good for counting and arithmetic
   - Supports math concepts in Book 1
   - Alternative if Block Coding not available

3. **Tertiary:** Prediction Mode (for Book 2)
   - Good for decision-making concepts
   - Supports conditional logic
   - Alternative if Block Coding not available

### Level ID Naming Convention

**Format:** `book{N}_{concept_name}`

**Examples:**
- Book 1: `book1_foundation_block`
- Book 2: `book2_decision_crossover`
- Book 3: `book3_pattern_loop`

### Exercise Difficulty

- **Book 1:** Difficulty Level 1 (Beginner)
  - Foundation concept, simplest exercise
  - Focus on basic block repetition

- **Book 2:** Difficulty Level 2 (Easy)
  - Builds on Book 1, adds conditionals
  - Focus on decision-making

- **Book 3:** Difficulty Level 3 (Medium)
  - Builds on Books 1 & 2, adds loops
  - Focus on pattern creation and breaking

---

## Next Steps

1. **Create LevelData for Each Book**
   - Book 1: `book1_foundation_block` level
   - Book 2: `book2_decision_crossover` level
   - Book 3: `book3_pattern_loop` level

2. **Configure Exercise Types**
   - Block Coding exercises for all books
   - Alternative exercises as fallbacks

3. **Test Exercise Flow**
   - Verify exercises load correctly
   - Test completion and return flow
   - Validate learning objectives

---

**Document Status:** Complete  
**Last Updated:** November 26, 2025  
**Next Review:** After exercise implementation


