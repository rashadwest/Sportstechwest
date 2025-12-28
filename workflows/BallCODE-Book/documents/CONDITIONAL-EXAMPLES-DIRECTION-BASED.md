# Conditional Examples - Direction-Based

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Purpose:** Examples of direction-based conditionals for Book 2  
**Status:** Implementation Examples

---

## 🎯 USER EXAMPLE

**"If I go right, I go straight next"**

This is a perfect example of a direction-based conditional that works with existing game state!

---

## 📋 CONDITIONAL EXAMPLES

### Example 1: Direction-Based Conditional

**User's Example:**
```
IF I go RIGHT
THEN go STRAIGHT (forward)
ELSE go RIGHT
```

**Block Structure:**
```
┌─────────────────────┐
│  START              │
├─────────────────────┤
│  POUND (RIGHT)      │  ← First move
├─────────────────────┤
│  IF last move RIGHT │  ← Check previous direction
│  THEN               │
│  ┌─────────────────┐│
│  │ POUND (FORWARD) ││  ← Go straight
│  └─────────────────┘│
│  ELSE               │
│  ┌─────────────────┐│
│  │ POUND (RIGHT)   ││  ← Go right again
│  └─────────────────┘│
├─────────────────────┤
│  BUCKET             │
└─────────────────────┘
```

**How It Works:**
1. Execute first move: POUND (RIGHT)
2. Check: "Was last direction RIGHT?"
3. If YES → Execute THEN: POUND (FORWARD)
4. If NO → Execute ELSE: POUND (RIGHT)

**Game State Check:**
```csharp
// Check last direction from ActionsInput or GameInfo
string lastDirection = ActionsInput.myInstance.GetLastDirection();
// OR
string lastDirection = GameInfo.myInstance.GetInitialDirection();

if (lastDirection == "RIGHT" || lastDirection == "Right")
{
    // Execute THEN branch
    ExecuteBlock(thenBlock);
}
else
{
    // Execute ELSE branch
    ExecuteBlock(elseBlock);
}
```

---

### Example 2: Pattern-Based Conditional

**Example:**
```
IF last move was LEFT
THEN go RIGHT (counter move)
ELSE go LEFT
```

**Block Structure:**
```
┌─────────────────────┐
│  START              │
├─────────────────────┤
│  POUND (LEFT)       │  ← First move
├─────────────────────┤
│  IF last move LEFT  │  ← Check previous direction
│  THEN               │
│  ┌─────────────────┐│
│  │ CROSSOVER (RIGHT)││  ← Counter move
│  └─────────────────┘│
│  ELSE               │
│  ┌─────────────────┐│
│  │ POUND (LEFT)    ││  ← Same direction
│  └─────────────────┘│
├─────────────────────┤
│  BUCKET             │
└─────────────────────┘
```

**Basketball Context:**
- "If I went left, counter with a right move"
- Teaches reading and reacting
- Uses existing direction tracking

---

### Example 3: Action Count Conditional

**Example:**
```
IF action count < 3
THEN POUND
ELSE CROSSOVER
```

**Block Structure:**
```
┌─────────────────────┐
│  START              │
├─────────────────────┤
│  IF actions < 3      │  ← Check action count
│  THEN               │
│  ┌─────────────────┐│
│  │ POUND           ││  ← Simple move
│  └─────────────────┘│
│  ELSE               │
│  ┌─────────────────┐│
│  │ CROSSOVER       ││  ← Advanced move
│  └─────────────────┘│
├─────────────────────┤
│  BUCKET             │
└─────────────────────┘
```

**Game State Check:**
```csharp
int actionCount = ActionsInput.myInstance.GetActionsCount();

if (actionCount < 3)
{
    // Execute THEN branch
    ActionsInput.myInstance.Pound();
}
else
{
    // Execute ELSE branch
    ActionsInput.myInstance.Cross();
}
```

---

### Example 4: Hand-Based Conditional

**Example:**
```
IF last hand was RIGHT
THEN use LEFT
ELSE use RIGHT
```

**Block Structure:**
```
┌─────────────────────┐
│  START              │
├─────────────────────┤
│  POUND (RIGHT hand) │  ← First move
├─────────────────────┤
│  IF last hand RIGHT │  ← Check previous hand
│  THEN               │
│  ┌─────────────────┐│
│  │ POUND (LEFT)    ││  ← Switch hands
│  └─────────────────┘│
│  ELSE               │
│  ┌─────────────────┐│
│  │ POUND (RIGHT)   ││  ← Same hand
│  └─────────────────┘│
├─────────────────────┤
│  BUCKET             │
└─────────────────────┘
```

**Game State Check:**
```csharp
List<ActionsInput.HAND> hands = ActionsInput.myInstance.GetHandsList();
ActionsInput.HAND lastHand = hands[hands.Count - 1];

if (lastHand == ActionsInput.HAND.Right)
{
    // Execute THEN branch (switch to left)
    ActionsInput.myInstance.Pound(); // Will use left hand
}
else
{
    // Execute ELSE branch (use right)
    ActionsInput.myInstance.Pound(); // Will use right hand
}
```

---

## 🔧 IMPLEMENTATION DETAILS

### How to Check Last Direction

**Option 1: From ActionsInput**
```csharp
// Get last direction from ActionsInput
ActionsInput.DIRECTION lastDir = ActionsInput.myInstance.GetLastDirection();
string lastDirection = lastDir.ToString(); // "Right", "Left", "Forward", etc.
```

**Option 2: From GameInfo**
```csharp
// Get initial direction (first move direction)
string initialDir = GameInfo.myInstance.GetInitialDirection();

// Get counter direction (second move direction)
string counterDir = GameInfo.myInstance.GetCounterDirection();
```

**Option 3: From Actions List**
```csharp
// Get directions from actions list
List<ActionsInput.DIRECTION> directions = ActionsInput.myInstance.GetDirectionsList();
ActionsInput.DIRECTION lastDirection = directions[directions.Count - 1];
```

---

### Conditional Evaluation Function

```csharp
/// <summary>
/// Evaluate conditional condition based on game state
/// </summary>
bool EvaluateCondition(Block ifBlock, string conditionType)
{
    switch (conditionType)
    {
        case "last_direction_right":
            ActionsInput.DIRECTION lastDir = ActionsInput.myInstance.GetLastDirection();
            return lastDir == ActionsInput.DIRECTION.Right;
            
        case "last_direction_left":
            ActionsInput.DIRECTION lastDir = ActionsInput.myInstance.GetLastDirection();
            return lastDir == ActionsInput.DIRECTION.Left;
            
        case "action_count_less_than_3":
            int count = ActionsInput.myInstance.GetActionsCount();
            return count < 3;
            
        case "last_hand_right":
            List<ActionsInput.HAND> hands = ActionsInput.myInstance.GetHandsList();
            if (hands.Count > 0)
            {
                return hands[hands.Count - 1] == ActionsInput.HAND.Right;
            }
            return false;
            
        default:
            return false;
    }
}
```

---

## 📚 BOOK 2 EXAMPLE: Decision Crossover

**From Book 2 Level JSON:**
```json
{
  "targetCode": "START → IF [defender left] THEN [BLOCK_2_CROSSOVER right] ELSE [BLOCK_2_CROSSOVER left] → ADVANCE"
}
```

**Simplified Version (Direction-Based):**
```
START
  → POUND (LEFT)           ← First move
  → IF last move LEFT       ← Check: Did I go left?
  → THEN CROSSOVER (RIGHT)  ← If yes, go right (counter)
  → ELSE CROSSOVER (LEFT)   ← If no, go left (same)
  → BUCKET
```

**Basketball Context:**
- "If I went left, counter with a right crossover"
- "If I didn't go left, continue left"
- Teaches decision-making based on previous action

---

## ✅ SUMMARY

**User's Example: "If I go right, I go straight next"**

**Block Code:**
```
IF last move RIGHT
THEN go FORWARD (straight)
ELSE go RIGHT
```

**How It Works:**
1. Execute first move: POUND (RIGHT)
2. Check: "Was last direction RIGHT?"
3. If YES → Execute: POUND (FORWARD) - go straight
4. If NO → Execute: POUND (RIGHT) - go right again

**Game State:**
- Uses existing `ActionsInput.GetLastDirection()`
- No new game state needed
- Works with current game structure

**Status:** ✅ **PERFECT EXAMPLE** - This is exactly how direction-based conditionals should work!

---

**Version:** 1.0  
**Created:** December 2025  
**Status:** Implementation Examples Complete

