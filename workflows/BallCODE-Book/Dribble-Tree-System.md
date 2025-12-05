# Dribble Tree System - BallCODE Block Coding

**The 5 Primary Dribbles: Numbers, Colors, and Shapes**

Based on: "Understand Basketball | Sports Science | Dribble Tree"

---

## The Dribble Tree Structure

### 7 Primary Dribbles (Numbered 1-7)

#### 1. **Pound Dribble**
- **Number:** 1
- **Description:** A forceful bounce of the ball directly in front of the player using one hand
- **Difficulty:** Simplest
- **Color:** (To be specified from document)
- **Shape:** (To be specified from document)

#### 2. **Crossover Dribble**
- **Number:** 2
- **Description:** A swift transfer of the ball from one hand to the other in front of the body
- **Difficulty:** Simple
- **Color:** (To be specified from document)
- **Shape:** (To be specified from document)

#### 3. **In & Out Dribble**
- **Number:** 3
- **Description:** A deceptive move where the ball is faked to one side and then brought back to the original side using the same hand
- **Difficulty:** Intermediate
- **Color:** (To be specified from document)
- **Shape:** (To be specified from document)

#### 4. **Between the Legs Dribble**
- **Number:** 4
- **Description:** Passing the ball through the legs from one hand to the other
- **Difficulty:** Advanced
- **Color:** (To be specified from document)
- **Shape:** (To be specified from document)

#### 5. **Behind the Back Dribble**
- **Number:** 5
- **Description:** Transferring the ball from one hand to the other behind the back
- **Difficulty:** Advanced
- **Color:** (To be specified from document)
- **Shape:** (To be specified from document)

#### 6. **Half Spin Dribble**
- **Number:** 6
- **Description:** Half spin move while dribbling
- **Difficulty:** Expert
- **Color:** (To be specified from document)
- **Shape:** (To be specified from document)

#### 7. **Spin Dribble**
- **Number:** 7
- **Description:** Full spin move while dribbling
- **Difficulty:** Expert
- **Color:** (To be specified from document)
- **Shape:** (To be specified from document)

---

## Block Coding Integration

### How Dribbles Become Blocks

**Each dribble number = A block type**

**Block Structure:**
```
┌─────────────────────┐
│  DRIBBLE [NUMBER]   │
│  Clock: [TIME]     │
│  Type: [NAME]       │
└─────────────────────┘
```

**Example:**
```
┌─────────────────────┐
│  DRIBBLE 1          │
│  Clock: 0.5s        │
│  Type: Pound        │
└─────────────────────┘
```

---

## Creating Move Sequences

### Combining Dribbles

**Sequence Example:**
```
START
  ↓
DRIBBLE 1 (Pound, Clock: 0.5s)
  ↓
DRIBBLE 2 (Crossover, Clock: 0.8s)
  ↓
DRIBBLE 3 (In & Out, Clock: 1.0s)
  ↓
BUCKET
```

**This creates:** Pound → Crossover → In & Out → Shoot

---

## Dribble Tree Progression

### Learning Order (Simplest to Most Complex)

1. **Start with Dribble 1 (Pound)**
   - Simplest move
   - Foundation for all dribbling

2. **Progress to Dribble 2 (Crossover)**
   - Adds hand transfer
   - More complex coordination

3. **Learn Dribble 3 (In & Out)**
   - Adds deception
   - Requires timing

4. **Master Dribble 4 (Between Legs)**
   - Advanced coordination
   - Complex body movement

5. **Expert Dribble 5 (Behind Back)**
   - Advanced hand transfer
   - Requires body awareness

6. **Expert Dribble 6 (Half Spin)**
   - Half rotation move
   - Advanced footwork

7. **Expert Dribble 7 (Spin)**
   - Full rotation move
   - Requires balance and control
   - Most complex

---

## Block Coding with Dribble Tree

### Block Palette

**Available Blocks:**
- **START** (green) - Begin sequence
- **DRIBBLE 1** (Pound) - [Color/Shape TBD]
- **DRIBBLE 2** (Crossover) - [Color/Shape TBD]
- **DRIBBLE 3** (In & Out) - [Color/Shape TBD]
- **DRIBBLE 4** (Between Legs) - [Color/Shape TBD]
- **DRIBBLE 5** (Behind Back) - [Color/Shape TBD]
- **DRIBBLE 6** (Half Spin) - [Color/Shape TBD]
- **DRIBBLE 7** (Spin) - [Color/Shape TBD]
- **BUCKET** (orange) - Shoot/complete

### Creating Combinations

**Kids can combine any dribbles:**
```
START
  → DRIBBLE 1 (Pound)
  → DRIBBLE 2 (Crossover)
  → DRIBBLE 1 (Pound)
  → BUCKET
```

**Or more complex:**
```
START
  → DRIBBLE 3 (In & Out)
  → DRIBBLE 4 (Between Legs)
  → DRIBBLE 6 (Spin)
  → DRIBBLE 2 (Crossover)
  → BUCKET
```

**Expert combinations:**
```
START
  → DRIBBLE 5 (Behind Back)
  → DRIBBLE 6 (Half Spin)
  → DRIBBLE 7 (Spin)
  → BUCKET
```

---

## Python Mapping

### Dribble Numbers → Python Functions

```python
def dribble_1_pound(clock=0.5):
    """Pound dribble - forceful bounce"""
    execute_dribble(type="pound", clock=clock)

def dribble_2_crossover(clock=0.8):
    """Crossover - transfer between hands"""
    execute_dribble(type="crossover", clock=clock)

def dribble_3_in_and_out(clock=1.0):
    """In & Out - deceptive move"""
    execute_dribble(type="in_and_out", clock=clock)

def dribble_4_between_legs(clock=1.2):
    """Between legs - through legs"""
    execute_dribble(type="between_legs", clock=clock)

def dribble_5_behind_back(clock=1.5):
    """Behind back - advanced hand transfer"""
    execute_dribble(type="behind_back", clock=clock)

def dribble_6_half_spin(clock=1.6):
    """Half spin - half rotation move"""
    execute_dribble(type="half_spin", clock=clock)

def dribble_7_spin(clock=1.8):
    """Spin - full rotation move"""
    execute_dribble(type="spin", clock=clock)
```

### Example Sequence in Python

```python
def execute_combo():
    start()
    dribble_1_pound(clock=0.5)
    dribble_2_crossover(clock=0.8)
    dribble_3_in_and_out(clock=1.0)
    bucket()
```

---

## Story Integration

### How Stories Teach Dribble Tree

**Episode 3: Loops (Rotations)**
- Story teaches: Repetitive patterns
- Blocks: DRIBBLE 1 → DRIBBLE 2 → DRIBBLE 1 (repeat)
- Python: `for i in range(3): dribble_sequence()`

**Episode 4: Pattern Recognition**
- Story teaches: Recognizing dribble patterns
- Blocks: Identify which dribble combinations work
- Python: Pattern matching algorithms

---

## Next Steps

**Need from Document:**
1. ✅ **Numbers:** 1-7 (confirmed)
   - 1: Pound
   - 2: Crossover
   - 3: In & Out
   - 4: Between Legs
   - 5: Behind Back
   - 6: Half Spin
   - 7: Spin
2. ⏳ **Colors:** What color for each dribble block (1-7)?
3. ⏳ **Shapes:** What shape for each dribble block (1-7)?

**Once I have colors and shapes, I'll update:**
- Block coding examples
- Story visual prompts
- Production pipeline
- Episode JSON files

---

**The Dribble Tree provides the foundation: 7 numbered dribbles that become blocks in the game!**

