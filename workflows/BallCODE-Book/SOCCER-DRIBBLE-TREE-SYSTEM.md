# Soccer Dribble Tree System - BallCODE Block Coding
## Numbered System for Soccer (Similar to Basketball)

**Date:** December 2025  
**Purpose:** Defines the numbered dribble system for soccer version  
**Based on:** Basketball Dribble Tree System (1-7 numbering)  
**Status:** 🚀 Ready for Implementation

---

## 🎯 OVERVIEW

The soccer version uses the **same numbered system (1-7)** as basketball, but with soccer-specific skills. This allows us to reuse the existing block coding framework and Unity implementation.

**Key Insight:** Same numbers, different skills = Same framework, different context!

---

## ⚽ SOCCER DRIBBLE TREE STRUCTURE

### 7 Primary Soccer Skills (Numbered 1-7)

#### 1. **Basic Dribble** (Soccer equivalent of Pound)
- **Number:** 1
- **Soccer Skill:** Basic forward dribble with one foot
- **Description:** Simple forward movement while controlling the ball
- **Difficulty:** Simplest
- **Movement:** Forward (↓)
- **Basketball Equivalent:** Pound Dribble

#### 2. **Cut Dribble** (Soccer equivalent of Crossover)
- **Number:** 2
- **Soccer Skill:** Quick change of direction (left or right)
- **Description:** Cutting the ball to one side while moving
- **Difficulty:** Simple
- **Movement:** Left (←) or Right (→)
- **Basketball Equivalent:** Crossover Dribble

#### 3. **In & Out Dribble** (Soccer equivalent)
- **Number:** 3
- **Soccer Skill:** Feint move - fake one direction, go the other
- **Description:** Deceptive move where you fake one way then go the other
- **Difficulty:** Intermediate
- **Movement:** Multiple directions (← → ↓ ↓)
- **Basketball Equivalent:** In & Out Dribble

#### 4. **Step Over** (Soccer equivalent of Between Legs)
- **Number:** 4
- **Soccer Skill:** Step over the ball to fake direction
- **Description:** Stepping over the ball to deceive defender
- **Difficulty:** Advanced
- **Movement:** Complex directional changes
- **Basketball Equivalent:** Between the Legs Dribble

#### 5. **Cruyff Turn** (Soccer equivalent of Behind Back)
- **Number:** 5
- **Soccer Skill:** Turn with ball behind standing leg
- **Description:** Advanced turn move to change direction quickly
- **Difficulty:** Advanced
- **Movement:** Turn and change direction
- **Basketball Equivalent:** Behind the Back Dribble

#### 6. **Half Turn** (Soccer equivalent of Half Spin)
- **Number:** 6
- **Soccer Skill:** 180-degree turn with the ball
- **Description:** Half rotation to face opposite direction
- **Difficulty:** Expert
- **Movement:** Rotational (↗ ↖)
- **Basketball Equivalent:** Half Spin Dribble

#### 7. **Full Turn** (Soccer equivalent of Spin)
- **Number:** 7
- **Soccer Skill:** 360-degree turn with the ball
- **Description:** Full rotation while maintaining ball control
- **Difficulty:** Expert
- **Movement:** Full rotation
- **Basketball Equivalent:** Spin Dribble

---

## 🎮 SOCCER MOVEMENT PATTERNS

### Offensive Strategy (Attacking)

**Movement Sequence:**
```
START → 1 → 2 → 3 → 4 → 5 → 6 → 7 → GOAL
```

### Dribble Actions & Arrows (Soccer)

**START**
- Horizontal light grey rectangular button
- Entry point for offensive sequence

**1 (Soccer Ball)**
- Single **forward arrow** (↓)
- Basic forward dribble
- Initial forward movement

**2 (Soccer Ball)**
- **Left arrow** (←) and **right arrow** (→)
- Cut dribble - lateral movement options
- Player can cut left or right

**3 (Soccer Ball)**
- **Left arrow** (←)
- **Right arrow** (→)
- **Two forward arrows** forming V shape (↓ ↓)
- In & Out move - multiple directional options
- Can move left, right, or forward (feint move)

**4 (Soccer Ball)**
- **Left arrow** (←)
- **Right arrow** (→)
- **Two forward arrows** forming V shape (↓ ↓)
- Step Over - similar to #3
- Multiple directional options with deception

**5 (Soccer Ball)**
- **Two left arrows** (← ←)
- **Two right arrows** (→ →)
- Rapid directional change
- Cruyff Turn - quick turn move
- Advanced direction change

**6 (Soccer Ball)**
- **Two upward-curving arrows** (↗ ↖)
- Half Turn - 180-degree rotation
- Turn to face opposite direction
- Shooting preparation

**7 (Soccer Ball)**
- **Two downward-curving arrows** (↘ ↙)
- Full Turn - 360-degree rotation
- Complete rotation move
- Advanced ball control

**GOAL** (Soccer equivalent of DUNK)
- Horizontal light grey rectangular button
- Soccer goal icon
- Final scoring action
- End of offensive sequence

---

## 🛡️ DEFENSIVE STRATEGY (Soccer)

**Movement Sequence:**
```
START → 1 → 2 → 3 → 4 → 5 → TACKLE/BLOCK
```

### Defensive Actions & Arrows (Soccer)

**START**
- Horizontal light grey rectangular button
- Entry point for defensive sequence

**1 (Soccer Ball)**
- **Upward arrow** (↑)
- **Downward arrow** (↓)
- Vertical positioning
- Up and down defensive movement

**2 (Soccer Ball)**
- **Left arrow** (←)
- **Right arrow** (→)
- Lateral defensive movement
- Side-to-side positioning

**3 (Soccer Ball)**
- **Two downward arrows angled outwards** (↓ ↘ and ↓ ↙)
- Closing down on attacker
- Spreading defense
- Defensive positioning

**4 (Soccer Ball)**
- **Two downward arrows angled outwards** (↓ ↘ and ↓ ↙)
- Similar to #3
- Closing down on attacker
- Defensive pressure

**5 (Soccer Ball)**
- **"Jockey" text** to the right
- Defensive posture
- Active positioning
- Ready to tackle

**TACKLE/BLOCK**
- Two lines of text:
  - "TACKLE" (top line)
  - "BLOCK" (bottom line)
- Defensive outcomes
- End of defensive sequence

---

## 🔄 BASKETBALL TO SOCCER MAPPING

| Number | Basketball | Soccer | Movement Pattern |
|--------|-----------|--------|------------------|
| 1 | Pound Dribble | Basic Dribble | Forward (↓) |
| 2 | Crossover | Cut Dribble | Left/Right (← →) |
| 3 | In & Out | In & Out | Multi-directional (← → ↓ ↓) |
| 4 | Between Legs | Step Over | Complex directional |
| 5 | Behind Back | Cruyff Turn | Rapid change (← ← → →) |
| 6 | Half Spin | Half Turn | Rotational (↗ ↖) |
| 7 | Spin | Full Turn | Full rotation (↘ ↙) |
| Final | DUNK | GOAL | Scoring action |

---

## 🎯 BLOCK CODING INTEGRATION

### How Soccer Skills Become Blocks

**Each skill number = A block type (same as basketball!)**

**Block Structure:**
```
┌─────────────────────┐
│  SKILL [NUMBER]     │
│  Clock: [TIME]      │
│  Type: [NAME]       │
└─────────────────────┘
```

**Example:**
```
┌─────────────────────┐
│  SKILL 1            │
│  Clock: 0.5s        │
│  Type: Basic Dribble│
└─────────────────────┘
```

### Block Palette (Soccer)

**Available Blocks:**
- **START** (green) - Begin sequence
- **SKILL 1** (Basic Dribble) - Forward movement
- **SKILL 2** (Cut Dribble) - Left/Right cut
- **SKILL 3** (In & Out) - Feint move
- **SKILL 4** (Step Over) - Deceptive step
- **SKILL 5** (Cruyff Turn) - Advanced turn
- **SKILL 6** (Half Turn) - 180° rotation
- **SKILL 7** (Full Turn) - 360° rotation
- **GOAL** (orange) - Shoot/score

---

## 📝 CREATING SOCCER SEQUENCES

### Example: Simple Move

**Blocks Connected:**
```
┌──────────┐
│  START   │
└──────────┘
      ↓
┌─────────────────────┐
│  SKILL 1            │
│  Clock: 0.5s        │
│  Type: Basic Dribble│
└─────────────────────┘
      ↓
┌─────────────────────┐
│  SKILL 2            │
│  Clock: 0.8s        │
│  Type: Cut Dribble  │
└─────────────────────┘
      ↓
┌──────────┐
│  GOAL    │
└──────────┘
```

**Result:** Player dribbles forward (0.5s), cuts right (0.8s), then shoots

### Example: Advanced Combination

```
START
  → SKILL 1 (Basic Dribble)
  → SKILL 3 (In & Out)
  → SKILL 4 (Step Over)
  → SKILL 6 (Half Turn)
  → SKILL 2 (Cut Dribble)
  → GOAL
```

---

## 💻 PYTHON MAPPING (Soccer)

### Soccer Skills → Python Functions

```python
def skill_1_basic_dribble(clock=0.5):
    """Basic dribble - forward movement"""
    execute_skill(type="basic_dribble", clock=clock)

def skill_2_cut_dribble(clock=0.8):
    """Cut dribble - left/right cut"""
    execute_skill(type="cut_dribble", clock=clock)

def skill_3_in_and_out(clock=1.0):
    """In & Out - feint move"""
    execute_skill(type="in_and_out", clock=clock)

def skill_4_step_over(clock=1.2):
    """Step Over - deceptive step"""
    execute_skill(type="step_over", clock=clock)

def skill_5_cruyff_turn(clock=1.5):
    """Cruyff Turn - advanced turn"""
    execute_skill(type="cruyff_turn", clock=clock)

def skill_6_half_turn(clock=1.6):
    """Half Turn - 180° rotation"""
    execute_skill(type="half_turn", clock=clock)

def skill_7_full_turn(clock=1.8):
    """Full Turn - 360° rotation"""
    execute_skill(type="full_turn", clock=clock)
```

### Example Sequence in Python

```python
def execute_soccer_combo():
    start()
    skill_1_basic_dribble(clock=0.5)
    skill_2_cut_dribble(clock=0.8)
    skill_3_in_and_out(clock=1.0)
    goal()
```

---

## 🎮 UNITY IMPLEMENTATION

### Reusing Basketball Framework

**Key Insight:** Same number system = Same code structure!

#### SoccerCommands.cs Structure:

```csharp
public class SoccerCommands : ISportCommand
{
    public void Execute(string action, params object[] args)
    {
        switch (action)
        {
            case "skill_1":
            case "basic_dribble":
                ExecuteBasicDribble(args);
                break;
            case "skill_2":
            case "cut_dribble":
                ExecuteCutDribble(args);
                break;
            case "skill_3":
            case "in_and_out":
                ExecuteInAndOut(args);
                break;
            case "skill_4":
            case "step_over":
                ExecuteStepOver(args);
                break;
            case "skill_5":
            case "cruyff_turn":
                ExecuteCruyffTurn(args);
                break;
            case "skill_6":
            case "half_turn":
                ExecuteHalfTurn(args);
                break;
            case "skill_7":
            case "full_turn":
                ExecuteFullTurn(args);
                break;
            case "goal":
                ExecuteGoal(args);
                break;
        }
    }
    
    private void ExecuteBasicDribble(object[] args) 
    {
        // Forward dribble movement
        // Same structure as basketball dribble_1
    }
    
    // ... other skill implementations
}
```

### Level Data Structure (Soccer)

```json
{
  "levelId": "soccer_book1_skill_1",
  "sport": "soccer",
  "levelName": "Basic Dribble",
  "gameMode": "blockcoding",
  "skills": [
    {
      "number": 1,
      "name": "Basic Dribble",
      "clock": 0.5,
      "movement": "forward"
    }
  ],
  "successCriteria": {
    "requiredSkills": [1],
    "maxTime": 5.0
  }
}
```

---

## 📚 STORY INTEGRATION

### How Soccer Stories Teach Skills

**Book 1: "The Foundation Pass"**
- Story teaches: Basic ball control
- Blocks: SKILL 1 (Basic Dribble)
- Python: `skill_1_basic_dribble()`
- World Cup context: Learning to control the ball like a World Cup player

**Book 2: "The Code of Flow"**
- Story teaches: Sequences and patterns
- Blocks: SKILL 1 → SKILL 2 → SKILL 1 (repeat)
- Python: `for i in range(3): skill_sequence()`
- World Cup context: Dribbling through defenders

**Book 3: "The Pattern"**
- Story teaches: Loops and repeating patterns
- Blocks: SKILL 3 → SKILL 4 → SKILL 3 (loop)
- Python: `while defender_ahead(): skill_pattern()`
- World Cup context: Passing patterns and sequences

---

## ✅ IMPLEMENTATION CHECKLIST

### Unity Integration:
- [ ] Create `SoccerCommands.cs` with skill 1-7
- [ ] Map skills to movement patterns
- [ ] Create soccer skill blocks (reuse basketball block system)
- [ ] Update level data structure for soccer
- [ ] Test skill execution in Unity

### Block Coding System:
- [ ] Reuse existing block coding framework
- [ ] Update block labels (DRIBBLE → SKILL)
- [ ] Update block types (Pound → Basic Dribble, etc.)
- [ ] Test block combinations

### Python Integration:
- [ ] Create soccer Python functions (skill_1 through skill_7)
- [ ] Map to Unity commands
- [ ] Test Python execution

### Content Integration:
- [ ] Update stories to reference soccer skills
- [ ] Create soccer skill tutorials
- [ ] Map skills to coding concepts

---

## 🎯 KEY ADVANTAGES

### 1. Framework Reuse
- ✅ Same number system (1-7)
- ✅ Same block coding structure
- ✅ Same Unity implementation pattern
- ✅ Same Python function structure

### 2. Easy Adaptation
- ✅ Just change skill names
- ✅ Same movement patterns (arrows)
- ✅ Same clock timing system
- ✅ Same level structure

### 3. Consistent Learning
- ✅ Students learn same number system
- ✅ Transfer knowledge between sports
- ✅ Same coding concepts
- ✅ Familiar structure

---

## 📊 COMPARISON TABLE

| Aspect | Basketball | Soccer | Reusable? |
|--------|-----------|--------|-----------|
| Number System | 1-7 | 1-7 | ✅ YES |
| Block Structure | DRIBBLE [N] | SKILL [N] | ✅ YES |
| Movement Arrows | Same | Same | ✅ YES |
| Clock System | Same | Same | ✅ YES |
| Python Functions | dribble_N() | skill_N() | ✅ YES |
| Unity Commands | Same structure | Same structure | ✅ YES |
| Level Data | Same format | Same format | ✅ YES |

**Result:** ~90% code reuse possible!

---

## 🚀 NEXT STEPS

### This Week:
1. [ ] Document soccer skill details
2. [ ] Create `SoccerCommands.cs` in Unity
3. [ ] Map skills to movement patterns
4. [ ] Test in Unity scene

### Next Week:
1. [ ] Create soccer skill blocks
2. [ ] Integrate with block coding system
3. [ ] Create soccer levels
4. [ ] Test end-to-end

---

**Status:** ✅ Ready to Implement  
**Framework Reuse:** ~90%  
**Key Insight:** Same numbers, different skills = Same code, different context!

