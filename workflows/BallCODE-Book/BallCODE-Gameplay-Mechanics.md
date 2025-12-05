# BallCODE Gameplay Mechanics

**Scratch-Style Block Coding with Basketball Terminology**

---

## Core Gameplay System

### The Block System (Like Scratch)

**Each dribble = A block that can be snapped together**

**Key Blocks:**
- **START** - Begin the sequence
- **DRIBBLE** - Action block (with clock timing)
- **BUCKET** - Shoot/end action

---

## How It Works

### 1. Start Block
**Purpose:** Begin the sequence
**Visual:** 
```
┌──────────┐
│  START   │
└──────────┘
```

### 2. Dribble Blocks (With Clock)
**Purpose:** Actions that can be chained together
**Each dribble has:**
- **Action:** What the player does (dribble, pass, move, etc.)
- **Clock:** Timing element (when it happens)

**Visual:**
```
┌─────────────────┐
│  DRIBBLE 1      │
│  Clock: 0.5s    │
│  Action: Move   │
└─────────────────┘
```

### 3. Bucket Block
**Purpose:** Shoot/complete the sequence
**Visual:**
```
┌──────────┐
│  BUCKET  │
│  (Shoot) │
└──────────┘
```

---

## Creating a Move Sequence

### Example: Simple Move

**Blocks Connected:**
```
┌──────────┐
│  START   │
└──────────┘
      ↓
┌─────────────────┐
│  DRIBBLE 1      │
│  Clock: 0.5s    │
│  Action: Dribble│
└─────────────────┘
      ↓
┌─────────────────┐
│  DRIBBLE 2      │
│  Clock: 1.0s    │
│  Action: Move   │
└─────────────────┘
      ↓
┌──────────┐
│  BUCKET  │
└──────────┘
```

**Result:** Player dribbles (0.5s), moves (1.0s), then shoots

---

## Clock System

### Timing Elements

**Each dribble block has a clock:**
- **Clock value:** How long the action takes
- **Sequential timing:** Blocks execute in order
- **Total time:** Sum of all clock values

**Example:**
```
START
  ↓ (0s)
DRIBBLE 1 (Clock: 0.5s)
  ↓ (0.5s)
DRIBBLE 2 (Clock: 1.0s)
  ↓ (1.5s)
DRIBBLE 3 (Clock: 0.8s)
  ↓ (2.3s)
BUCKET
```

**Total sequence time:** 2.3 seconds

---

## Block Types & Basketball Terminology

### Action Blocks (Dribbles)

**Movement:**
- `DRIBBLE` - Dribble the ball
- `MOVE` - Move to position
- `CUT` - Cut to basket
- `ROTATE` - Rotate position

**Passing:**
- `PASS LEFT` - Pass to left
- `PASS RIGHT` - Pass to right
- `OUTLET` - Outlet pass

**Shooting:**
- `BUCKET` - Shoot the ball

**Defense:**
- `DEFEND` - Defend position
- `CLOSEOUT` - Close out on shooter

### Timing Blocks (Clocks)

**Each action has a clock:**
- **Fast:** 0.3-0.5s (quick actions)
- **Medium:** 0.5-1.0s (normal actions)
- **Slow:** 1.0-2.0s (complex actions)

---

## Advanced: Conditional Blocks

### If/Then Blocks (Reads)

**Basketball terminology:**
```
┌─────────────────────┐
│ IF defender traps   │
│ THEN                │
│   PASS LEFT         │
│ ELSE                │
│   DRIVE RIGHT       │
└─────────────────────┘
```

### Loop Blocks (Rotations)

**Basketball terminology:**
```
┌─────────────────────┐
│ REPEAT 5 TIMES      │
│   ROTATE            │
│   CLOSEOUT          │
└─────────────────────┘
```

---

## Sports Language → Code Mapping

### Block Sequence → Python Code

**Sports Language (Blocks):**
```
START
  ↓
DRIBBLE 1 (Clock: 0.5s, Action: Move)
  ↓
DRIBBLE 2 (Clock: 1.0s, Action: Pass)
  ↓
BUCKET
```

**Python Equivalent:**
```python
def execute_move():
    start()
    dribble(action="move", clock=0.5)
    dribble(action="pass", clock=1.0)
    bucket()
```

---

## Learning Progression

### Level 1: Simple Sequences
**Learn:** START → DRIBBLE → BUCKET
**Example:**
```
START → DRIBBLE (move) → BUCKET
```

### Level 2: Multiple Dribbles
**Learn:** Chain multiple dribbles
**Example:**
```
START → DRIBBLE 1 → DRIBBLE 2 → DRIBBLE 3 → BUCKET
```

### Level 3: Clock Timing
**Learn:** Understand timing and sequencing
**Example:**
```
START
  → DRIBBLE 1 (Clock: 0.5s)
  → DRIBBLE 2 (Clock: 1.0s)
  → BUCKET
```

### Level 4: Conditionals
**Learn:** If/then logic with basketball reads
**Example:**
```
START
  → IF defender traps
      THEN PASS LEFT
      ELSE DRIVE RIGHT
  → BUCKET
```

### Level 5: Loops
**Learn:** Repetitive actions (rotations)
**Example:**
```
START
  → REPEAT 5 TIMES
      ROTATE
      CLOSEOUT
  → BUCKET
```

### Level 6: Python
**Learn:** Write Python code for same sequences
**Example:**
```python
def execute_play():
    if defender_traps():
        pass_left()
    else:
        drive_right()
    bucket()
```

---

## Story Integration

### How Stories Teach the Block System

**Episode 1: State**
- Story teaches: Game states (START, LIVE, DEAD, OUTCOME)
- Blocks: START block, state-based dribbles
- Python: `if state == "LIVE": execute_move()`

**Episode 2: Conditionals**
- Story teaches: If/then reads
- Blocks: IF defender traps THEN pass ELSE drive
- Python: `if defender_traps: pass_left() else: drive_right()`

**Episode 3: Loops**
- Story teaches: Rotations and repetition
- Blocks: REPEAT 5 TIMES rotate
- Python: `for i in range(5): rotate()`

---

## Production Pipeline Updates

### Story Assets Should Show:

1. **Block Examples:**
   - START block
   - DRIBBLE blocks with clocks
   - BUCKET block
   - Connected sequences

2. **Block Sequences:**
   - Visual of blocks snapped together
   - Clock timing shown
   - Result preview

3. **Python Equivalents:**
   - Show Python code for same sequence
   - Side-by-side comparison
   - Progressive learning option

---

**This is the actual gameplay: Scratch-style blocks using basketball terminology (START, DRIBBLE with clock, BUCKET)!**




