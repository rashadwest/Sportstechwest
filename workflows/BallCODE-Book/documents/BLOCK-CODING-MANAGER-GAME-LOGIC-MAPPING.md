# BlockCodingManager - Game Logic Mapping

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Purpose:** Map each block in BlockCodingManager to existing BallCODE game logic  
**Status:** Assessment Document

---

## 🎯 OVERVIEW

This document maps each block type in `BlockCodingManager.cs` to the existing BallCODE game system to verify compatibility.

---

## 📋 BLOCK TYPES & GAME MAPPINGS

### 1. START Block

**Block Type:** `START`  
**Display Name:** "START"  
**Purpose:** Initialize the sequence, reset player position

**Current Implementation:**
```csharp
basketballActions["START"] = (args) => {
    ExecuteStart();
};
```

**Game Logic Mapping:**
- **Existing System:** `SyntaxToActionsParser` expects a `Start` block
- **ActionsInput:** No direct mapping (initialization happens automatically)
- **Status:** ✅ Compatible - START is standard in block coding systems

**What It Should Do:**
- Reset player position
- Clear previous actions
- Initialize sequence

---

### 2. BLOCK_1_POUND (Pound Dribble)

**Block Type:** `BLOCK_1_POUND`  
**Display Name:** "POUND"  
**Purpose:** Execute pound dribble (Book 1 - Foundation Block)

**Current Implementation:**
```csharp
basketballActions["BLOCK_1_POUND"] = (args) => {
    ExecutePoundDribble();
};
```

**Game Logic Mapping:**
- **Existing System:** `SyntaxToActionsParser.DetermineDribbleAction()` → `ActionsInput.Pound()`
- **SyntaxType:** `DraggableSyntaxObject.SyntaxType.Pound`
- **Action Number:** `Numbers.POUND_NUMBER` (typically 1)
- **ActionsInput Method:** `ActionsInput.Pound()`
- **Status:** ✅ **DIRECT MAPPING EXISTS**

**What It Should Do:**
```csharp
// Should call:
ActionsInput.myInstance.Pound();
// Then set direction if needed
```

**Direction Support:**
- Pound dribble uses direction dropdown (0-7)
- Maps to `ActionsInput.DIRECTION` enum

---

### 3. BLOCK_2_CROSSOVER (Crossover Dribble)

**Block Type:** `BLOCK_2_CROSSOVER`  
**Display Name:** "CROSSOVER"  
**Purpose:** Execute crossover dribble (Book 2 - Decision Crossover)

**Current Implementation:**
```csharp
basketballActions["BLOCK_2_CROSSOVER"] = (args) => {
    string direction = args != null && args.Length > 0 ? args[0].ToString() : "right";
    ExecuteCrossover(direction);
};
```

**Game Logic Mapping:**
- **Existing System:** `SyntaxToActionsParser.DetermineDribbleAction()` → `ActionsInput.Cross()`
- **SyntaxType:** `DraggableSyntaxObject.SyntaxType.Crossover`
- **Action Number:** `Numbers.CROSS_NUMBER` (typically 2)
- **ActionsInput Method:** `ActionsInput.Cross()`
- **Status:** ✅ **DIRECT MAPPING EXISTS**

**What It Should Do:**
```csharp
// Should call:
SetDirection(direction); // Convert string to ActionsInput.DIRECTION
ActionsInput.myInstance.Cross();
```

**Direction Support:**
- Crossover requires direction (left/right)
- Uses same direction system (0-7)

---

### 4. BLOCK_3_IN_OUT (In & Out Dribble)

**Block Type:** `BLOCK_3_IN_OUT`  
**Display Name:** "IN & OUT"  
**Purpose:** Execute in & out dribble (Book 3 - Pattern Loop)

**Current Implementation:**
```csharp
basketballActions["BLOCK_3_IN_OUT"] = (args) => {
    string type = args != null && args.Length > 0 ? args[0].ToString() : "real";
    ExecuteInOut(type);
};
```

**Game Logic Mapping:**
- **Existing System:** `SyntaxToActionsParser.DetermineDribbleAction()` → `ActionsInput.InAndOut()`
- **SyntaxType:** `DraggableSyntaxObject.SyntaxType.Inout`
- **Action Number:** `Numbers.INOUT_NUMBER` (typically 3)
- **ActionsInput Method:** `ActionsInput.InAndOut()`
- **Status:** ✅ **DIRECT MAPPING EXISTS**

**What It Should Do:**
```csharp
// Should call:
ActionsInput.myInstance.InAndOut();
// Type can be "fake" or "real" for pattern creation/breaking
```

**Type Parameter:**
- "fake" = pattern creation (deception)
- "real" = pattern breaking (actual move)

---

### 5. ADVANCE (Move Forward)

**Block Type:** `ADVANCE`  
**Display Name:** "ADVANCE"  
**Purpose:** Move player forward (or in specified direction)

**Current Implementation:**
```csharp
basketballActions["ADVANCE"] = (args) => {
    string direction = args != null && args.Length > 0 ? args[0].ToString() : "forward";
    ExecuteAdvance(direction);
};
```

**Game Logic Mapping:**
- **Existing System:** Direction is set via `ActionsInput.SetDirection()`
- **Direction System:** 8 directions (Forward, Right, Left, Backward, etc.)
- **ActionsInput Methods:** `ActionsInput.Forward()`, `ActionsInput.Right()`, etc.
- **Status:** ⚠️ **NEEDS DIRECTION MAPPING**

**What It Should Do:**
```csharp
// Should call:
int directionIndex = ConvertDirectionToIndex(direction);
ActionsInput.myInstance.SetDirection((ActionsInput.DIRECTION)directionIndex);
// Then execute movement (direction is set before next dribble)
```

**Direction Mapping:**
- 0: Forward
- 1: ForwardRight
- 2: Right
- 3: BackwardRight
- 4: Backward
- 5: BackwardLeft
- 6: Left
- 7: ForwardLeft

---

### 6. BUCKET (Shoot/Score)

**Block Type:** `BUCKET`  
**Display Name:** "BUCKET"  
**Purpose:** Shoot the ball (required at end of sequence)

**Current Implementation:**
```csharp
basketballActions["BUCKET"] = (args) => {
    ExecuteBucket();
};
```

**Game Logic Mapping:**
- **Existing System:** `SyntaxToActionsParser` → `ActionsInput.Bucket()`
- **SyntaxType:** `DraggableSyntaxObject.SyntaxType.Dunk`, `Layup`, `Floater`, etc.
- **ActionsInput Method:** `ActionsInput.Bucket()`
- **Validation:** Game requires BUCKET at end (checked by `ContainsShot()`)
- **Status:** ✅ **DIRECT MAPPING EXISTS**

**What It Should Do:**
```csharp
// Should call:
ActionsInput.myInstance.Bucket();
// This triggers shot selection/execution
```

**Shot Types:**
- Dunk
- Layup
- Floater
- Fadeaway
- Stepback
- Jumpshot

**Note:** Game validation requires BUCKET as last action in sequence.

---

### 7. END Block

**Block Type:** `END`  
**Display Name:** "END"  
**Purpose:** Mark end of sequence (optional, BUCKET usually serves this)

**Current Implementation:**
```csharp
basketballActions["END"] = (args) => {
    ExecuteEnd();
};
```

**Game Logic Mapping:**
- **Existing System:** `SyntaxToActionsParser` uses `SyntaxType.End` to mark loop end
- **Status:** ✅ **COMPATIBLE** - Used for loop termination

**What It Should Do:**
- Optional end marker
- BUCKET usually serves as end marker
- Used in loops to mark loop boundary

---

### 8. IF Block (Conditional)

**Block Type:** `IF`  
**Display Name:** "IF"  
**Purpose:** Conditional logic (Book 2 - Decision Crossover)

**Current Implementation:**
```csharp
basketballActions["IF"] = (args) => {
    // Conditional logic handled in ExecuteBlocks
};
```

**Game Logic Mapping:**
- **Existing System:** ❌ **NO DIRECT MAPPING** - Conditionals not in current game
- **Status:** ⚠️ **NEW FEATURE** - Needs implementation

**What It Should Do:**
- Evaluate condition (e.g., defender position)
- Execute THEN branch if true
- Execute ELSE branch if false

**Implementation Notes:**
- Condition evaluation needs game state access
- Defender position checking required
- This is a new feature for Book 2

---

### 9. THEN Block

**Block Type:** `THEN`  
**Display Name:** "THEN"  
**Purpose:** True branch of conditional

**Current Implementation:**
```csharp
basketballActions["THEN"] = (args) => {
    // Conditional logic handled in ExecuteBlocks
};
```

**Game Logic Mapping:**
- **Status:** ⚠️ **NEW FEATURE** - Part of conditional system

**What It Should Do:**
- Marks true branch of IF statement
- Executes blocks after THEN if condition is true

---

### 10. ELSE Block

**Block Type:** `ELSE`  
**Display Name:** "ELSE"  
**Purpose:** False branch of conditional

**Current Implementation:**
```csharp
basketballActions["ELSE"] = (args) => {
    // Conditional logic handled in ExecuteBlocks
};
```

**Game Logic Mapping:**
- **Status:** ⚠️ **NEW FEATURE** - Part of conditional system

**What It Should Do:**
- Marks false branch of IF statement
- Executes blocks after ELSE if condition is false

---

### 11. LOOP Block

**Block Type:** `LOOP`  
**Display Name:** "LOOP"  
**Purpose:** Loop start (Book 3 - Pattern Loop)

**Current Implementation:**
```csharp
basketballActions["LOOP"] = (args) => {
    // Loop logic handled in ExecuteBlocks
};
```

**Game Logic Mapping:**
- **Existing System:** `SyntaxToActionsParser` has `ForLoop` support
- **SyntaxType:** `DraggableSyntaxObject.SyntaxType.ForLoop`
- **ActionsInput:** Loops handled by repeating action list
- **Status:** ✅ **PARTIAL MAPPING** - Loop structure exists

**What It Should Do:**
```csharp
// Similar to existing ForLoop:
// 1. Get repeat count from REPEAT block
// 2. Collect blocks between LOOP and END
// 3. Execute those blocks repeatCount times
```

**Existing Loop Pattern:**
```csharp
// From SyntaxToActionsParser:
else if (type == DraggableSyntaxObject.SyntaxType.ForLoop)
{
    // Collect blocks until END
    // Repeat those blocks N times
    ParseSyntaxToActions(newSyntaxList);
}
```

---

### 12. REPEAT Block

**Block Type:** `REPEAT`  
**Display Name:** "REPEAT"  
**Purpose:** Specify loop count

**Current Implementation:**
```csharp
basketballActions["REPEAT"] = (args) => {
    // Loop logic handled in ExecuteBlocks
};
```

**Game Logic Mapping:**
- **Existing System:** `DraggableSyntaxObject.GetAmount()` gets repeat count
- **Input Field:** `TMP_InputField` for number input
- **Status:** ✅ **COMPATIBLE** - Amount system exists

**What It Should Do:**
- Store repeat count (e.g., 3, 5, 10)
- Used by LOOP to determine iterations

---

### 13. BREAK Block

**Block Type:** `BREAK`  
**Display Name:** "BREAK"  
**Purpose:** Exit loop early

**Current Implementation:**
```csharp
basketballActions["BREAK"] = (args) => {
    // Loop break handled in ExecuteBlocks
};
```

**Game Logic Mapping:**
- **Status:** ⚠️ **NEW FEATURE** - Break not in current system

**What It Should Do:**
- Exit loop before repeat count is reached
- Used for conditional loop termination

---

### 14. PLACEHOLDER Block

**Block Type:** `PLACEHOLDER`  
**Display Name:** "" (empty - no name)  
**Purpose:** Placeholder for future blocks

**Current Implementation:**
```csharp
placeholderBlocks.Add("PLACEHOLDER");
basketballActions["PLACEHOLDER"] = (args) => {
    Debug.Log("[BlockCodingManager] Placeholder block executed - no action");
};
```

**Game Logic Mapping:**
- **Status:** ✅ **PLACEHOLDER** - No game logic needed

**What It Should Do:**
- Show in palette but do nothing when executed
- Visual indicator (grayed out, dashed border)
- Reserved for future functionality

---

## 🔄 DIRECTION SYSTEM MAPPING

### Direction Conversion

**BlockCodingManager Direction Strings → ActionsInput.DIRECTION Enum:**

| String | Index | ActionsInput.DIRECTION | Description |
|--------|-------|----------------------|-------------|
| "forward" / "f" / "s" | 0 | Forward | Straight ahead |
| "forwardright" / "fr" / "dsr" | 1 | ForwardRight | Diagonal forward-right |
| "right" / "r" | 2 | Right | Right side |
| "backwardright" / "br" / "dbr" | 3 | BackwardRight | Diagonal back-right |
| "backward" / "b" | 4 | Backward | Straight back |
| "backwardleft" / "bl" / "dbl" | 5 | BackwardLeft | Diagonal back-left |
| "left" / "l" | 6 | Left | Left side |
| "forwardleft" / "fl" / "dsl" | 7 | ForwardLeft | Diagonal forward-left |

**Implementation:**
```csharp
int ConvertDirectionToIndex(string direction)
{
    // Maps to SyntaxToActionsParser.SetDirection() index system
    // Matches TMP_Dropdown values (0-7)
}
```

---

## ✅ COMPATIBILITY ASSESSMENT

### ✅ Fully Compatible Blocks

1. **START** - Standard initialization
2. **BLOCK_1_POUND** - Maps to `ActionsInput.Pound()`
3. **BLOCK_2_CROSSOVER** - Maps to `ActionsInput.Cross()`
4. **BLOCK_3_IN_OUT** - Maps to `ActionsInput.InAndOut()`
5. **BUCKET** - Maps to `ActionsInput.Bucket()`
6. **END** - Used in loop termination
7. **REPEAT** - Uses existing amount system
8. **LOOP** - Similar to existing ForLoop structure

### ⚠️ Needs Implementation

1. **ADVANCE** - Needs direction mapping to `ActionsInput.SetDirection()`
2. **IF/THEN/ELSE** - New conditional system (not in current game)
3. **BREAK** - New loop break feature (not in current game)

### ✅ Placeholder Support

1. **PLACEHOLDER** - Reserved for future blocks

---

## 🔧 INTEGRATION REQUIREMENTS

### Required Changes

1. **Connect to ActionsInput:**
   ```csharp
   // In ExecutePoundDribble():
   if (ActionsInput.myInstance != null)
   {
       ActionsInput.myInstance.Pound();
   }
   ```

2. **Direction System:**
   ```csharp
   // In ExecuteCrossover/ExecuteAdvance():
   int dirIndex = ConvertDirectionToIndex(direction);
   ActionsInput.myInstance.SetDirection((ActionsInput.DIRECTION)dirIndex);
   ```

3. **Conditional System:**
   - Need game state access for condition evaluation
   - Defender position checking
   - THEN/ELSE branch execution

4. **Loop System:**
   - Use existing ForLoop pattern
   - Collect blocks between LOOP and END
   - Repeat execution

---

## 📊 SUMMARY

**Total Blocks:** 14  
**Fully Compatible:** 8 (57%)  
**Needs Implementation:** 3 (21%)  
**Placeholders:** 1 (7%)  
**New Features:** 2 (14% - IF/THEN/ELSE, BREAK)

**Overall Status:** ✅ **MOSTLY COMPATIBLE** - Core blocks map directly to existing game logic. Conditionals and break are new features that need game state integration.

---

**Version:** 1.0  
**Created:** December 2025  
**Status:** Assessment Complete

