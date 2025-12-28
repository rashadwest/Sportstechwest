# Soccer Unity Foundation Setup - This Week
## What's Needed to Get Unity Project Going

**Date:** December 2025  
**Timeline:** This Week (Foundation Setup)  
**Status:** 🚀 Ready to Execute

---

## 🎯 FOUNDATION REQUIREMENTS

### What We Need This Week:

1. **Unity Project Access & Setup**
2. **Sport-Agnostic Framework Extraction**
3. **Soccer-Specific Module Structure**
4. **Dependencies & Configuration**
5. **Initial Soccer Environment**

---

## 📋 PART 1: UNITY PROJECT ACCESS & SETUP

### Step 1: Locate Unity Project
**Questions to Answer:**
- [ ] Where is the Unity project stored?
  - Local path: `_________________`
  - Git repository: `_________________`
  - Cloud storage: `_________________`
- [ ] How do we access it?
  - Direct file access
  - Git clone
  - Shared folder

### Step 2: Unity Version & Requirements
**Check Current Setup:**
- [ ] Unity version: `_________________` (Need: 2021.3 LTS or 2022.3 LTS)
- [ ] Unity Editor installed: `_________________`
- [ ] Project opens successfully: `_________________`
- [ ] Build target: WebGL (for website integration)

### Step 3: Required Unity Packages
**Install/Verify:**
- [ ] TextMeshPro (UI text)
- [ ] Unity WebGL Support
- [ ] Unity Analytics (optional)
- [ ] JSON.NET (if using Newtonsoft.Json)

**Action:** Open Unity → Window → Package Manager → Install required packages

---

## 🏗️ PART 2: SPORT-AGNOSTIC FRAMEWORK EXTRACTION

### Current Basketball-Specific Code to Extract:

#### 1. GameModeManager.cs
**Current:** Basketball-specific game modes
**Needed:** Sport-agnostic base class

**Extraction Plan:**
```csharp
// Create base class
public abstract class SportGameManager : MonoBehaviour
{
    public abstract void InitializeSport();
    public abstract void HandleSportSpecificMechanics();
}

// Basketball implementation (existing)
public class BasketballGameManager : SportGameManager
{
    // Existing basketball code
}

// Soccer implementation (new)
public class SoccerGameManager : SportGameManager
{
    // New soccer code
}
```

#### 2. PythonCodingManager.cs
**Current:** Basketball-specific functions (dribble, pass, shoot)
**Needed:** Sport-agnostic command system

**Key Insight:** Same number system (1-7) = Same function structure!

**Extraction Plan:**
```csharp
// Create sport-agnostic command interface
public interface ISportCommand
{
    void Execute(string action, params object[] args);
    void ExecuteSkill(int skillNumber, float clock); // Number system (1-7)
}

// Basketball commands (existing)
public class BasketballCommands : ISportCommand
{
    // dribble_1_pound(), dribble_2_crossover(), etc. (1-7)
    // dribble(), pass_to(), shoot(), etc.
}

// Soccer commands (new) - SAME NUMBER SYSTEM!
public class SoccerCommands : ISportCommand
{
    // skill_1_basic_dribble(), skill_2_cut_dribble(), etc. (1-7)
    // Same numbers, different skill names
    // dribble(), pass_to(), shoot(), etc. (soccer context)
}
```

**Number System Mapping:**
- Basketball: DRIBBLE 1-7 (Pound, Crossover, In & Out, etc.)
- Soccer: SKILL 1-7 (Basic Dribble, Cut, In & Out, etc.)
- **Same numbers, same structure, different names!**

#### 3. LevelData.cs
**Current:** Basketball-specific level data
**Needed:** Sport-agnostic level structure

**Extraction Plan:**
```csharp
// Add sport field to level data
[System.Serializable]
public class LevelData
{
    public string sport; // "basketball" or "soccer"
    public string levelId;
    public string levelName;
    // ... rest of level data
}
```

#### 4. StoryModeManager.cs
**Current:** Basketball story integration
**Needed:** Sport-agnostic story system

**Extraction Plan:**
```csharp
// Add sport parameter
public void LoadStory(string sport, string episodeId)
{
    // Load story based on sport
}
```

---

## ⚽ PART 3: SOCCER-SPECIFIC MODULE STRUCTURE

### New Files to Create:

#### 1. SoccerGameManager.cs
**Location:** `Assets/Scripts/Soccer/SoccerGameManager.cs`
**Purpose:** Soccer-specific game logic

**Initial Structure:**
```csharp
using UnityEngine;

public class SoccerGameManager : SportGameManager
{
    public override void InitializeSport()
    {
        // Initialize soccer field
        // Set up soccer ball
        // Configure soccer player
    }
    
    public override void HandleSportSpecificMechanics()
    {
        // Soccer-specific game mechanics
    }
}
```

#### 2. SoccerCommands.cs
**Location:** `Assets/Scripts/Soccer/SoccerCommands.cs`
**Purpose:** Soccer-specific Python commands

**Key:** Uses same number system (1-7) as basketball!

**Initial Structure:**
```csharp
public class SoccerCommands : ISportCommand
{
    // Number system (1-7) - same as basketball!
    public void ExecuteSkill(int skillNumber, float clock)
    {
        switch (skillNumber)
        {
            case 1: ExecuteSkill1_BasicDribble(clock); break;
            case 2: ExecuteSkill2_CutDribble(clock); break;
            case 3: ExecuteSkill3_InAndOut(clock); break;
            case 4: ExecuteSkill4_StepOver(clock); break;
            case 5: ExecuteSkill5_CruyffTurn(clock); break;
            case 6: ExecuteSkill6_HalfTurn(clock); break;
            case 7: ExecuteSkill7_FullTurn(clock); break;
        }
    }
    
    public void Execute(string action, params object[] args)
    {
        switch (action)
        {
            case "skill_1":
            case "basic_dribble":
                ExecuteSkill1_BasicDribble(args);
                break;
            case "skill_2":
            case "cut_dribble":
                ExecuteSkill2_CutDribble(args);
                break;
            // ... skills 3-7
            case "dribble":
                ExecuteDribble(args);
                break;
            case "pass_to":
                ExecutePass(args);
                break;
            case "shoot":
            case "goal":
                ExecuteShoot(args);
                break;
        }
    }
    
    // Skill implementations (1-7)
    private void ExecuteSkill1_BasicDribble(float clock) { }
    private void ExecuteSkill2_CutDribble(float clock) { }
    // ... skills 3-7
    
    // General commands
    private void ExecuteDribble(object[] args) { }
    private void ExecutePass(object[] args) { }
    private void ExecuteShoot(object[] args) { }
}
```

#### 3. SoccerField.cs
**Location:** `Assets/Scripts/Soccer/SoccerField.cs`
**Purpose:** Soccer field environment

**Initial Structure:**
```csharp
public class SoccerField : MonoBehaviour
{
    public GameObject field;
    public GameObject goalLeft;
    public GameObject goalRight;
    public GameObject centerCircle;
    
    void Start()
    {
        CreateField();
    }
    
    void CreateField()
    {
        // Create soccer field geometry
    }
}
```

#### 4. SoccerBall.cs
**Location:** `Assets/Scripts/Soccer/SoccerBall.cs`
**Purpose:** Soccer ball physics and behavior

**Initial Structure:**
```csharp
public class SoccerBall : MonoBehaviour
{
    public Rigidbody rb;
    public float ballSpeed = 10f;
    
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }
    
    public void Kick(Vector3 direction, float power)
    {
        rb.AddForce(direction * power * ballSpeed);
    }
}
```

#### 5. SoccerPlayer.cs
**Location:** `Assets/Scripts/Soccer/SoccerPlayer.cs`
**Purpose:** Soccer player movement and actions

**Initial Structure:**
```csharp
public class SoccerPlayer : MonoBehaviour
{
    public float moveSpeed = 5f;
    public float dribbleSpeed = 3f;
    
    public void Move(Vector3 direction)
    {
        transform.position += direction * moveSpeed * Time.deltaTime;
    }
    
    public void Dribble(Vector3 direction)
    {
        // Dribble ball in direction
    }
}
```

---

## 📁 PART 4: DIRECTORY STRUCTURE

### New Folder Structure:

```
Assets/
├── Scripts/
│   ├── Managers/              # Existing (keep)
│   │   ├── GameModeManager.cs
│   │   └── StoryModeManager.cs
│   ├── Sport/                 # NEW - Sport-agnostic base
│   │   ├── SportGameManager.cs (abstract base)
│   │   ├── ISportCommand.cs (interface)
│   │   └── SportLevelData.cs (base class)
│   ├── Basketball/            # Existing (refactor)
│   │   ├── BasketballGameManager.cs
│   │   ├── BasketballCommands.cs
│   │   └── BasketballCourt.cs
│   └── Soccer/                # NEW - Soccer-specific
│       ├── SoccerGameManager.cs
│       ├── SoccerCommands.cs
│       ├── SoccerField.cs
│       ├── SoccerBall.cs
│       └── SoccerPlayer.cs
├── Scenes/
│   ├── Basketball/            # Existing
│   │   └── BasketballGame.unity
│   └── Soccer/                # NEW
│       └── SoccerGame.unity
└── Prefabs/
    ├── Basketball/            # Existing
    └── Soccer/                # NEW
        ├── SoccerField.prefab
        ├── SoccerBall.prefab
        └── SoccerPlayer.prefab
```

---

## 🔧 PART 5: DEPENDENCIES & CONFIGURATION

### Unity Project Settings:

#### Build Settings:
- [ ] Platform: WebGL
- [ ] Compression: Gzip or Brotli
- [ ] Template: Default or Custom
- [ ] Memory Size: Appropriate for game

#### Player Settings:
- [ ] Company Name: BallCODE
- [ ] Product Name: BallCODE Soccer
- [ ] Version: 1.0.0
- [ ] API Compatibility: .NET Standard 2.1

#### Project Settings:
- [ ] Color Space: Linear (for better graphics)
- [ ] Graphics API: WebGL 2.0
- [ ] Scripting Backend: IL2CPP (for WebGL)

### External Dependencies:

#### JSON Data:
- [ ] Level data format compatible
- [ ] Story data format compatible
- [ ] Curriculum data format compatible

#### n8n Integration:
- [ ] URL parameter handling (for book-to-game linking)
- [ ] Return flow implementation
- [ ] Progress tracking integration

---

## ⚽ PART 6: INITIAL SOCCER ENVIRONMENT

### Week 1 Goals:

#### Day 1-2: Framework Extraction
- [ ] Create `Sport/` folder structure
- [ ] Extract sport-agnostic base classes
- [ ] Refactor basketball code to use base classes
- [ ] Test basketball still works

#### Day 3-4: Soccer Module Creation
- [ ] Create `Soccer/` folder structure
- [ ] Create `SoccerGameManager.cs`
- [ ] Create `SoccerCommands.cs`
- [ ] Create basic soccer scene

#### Day 5: Soccer Field & Basic Mechanics
- [ ] Create `SoccerField.cs` and prefab
- [ ] Create `SoccerBall.cs` and prefab
- [ ] Create `SoccerPlayer.cs` and prefab
- [ ] Basic movement working

---

## 🚀 THIS WEEK'S ACTION ITEMS

### Immediate (Day 1):

1. **Locate Unity Project**
   ```bash
   # Find Unity project location
   # Document path
   # Verify access
   ```

2. **Verify Unity Setup**
   - [ ] Unity version correct
   - [ ] Required packages installed
   - [ ] Project opens successfully
   - [ ] Can build WebGL

3. **Create Folder Structure**
   ```bash
   # In Unity project:
   Assets/Scripts/Sport/
   Assets/Scripts/Soccer/
   Assets/Scenes/Soccer/
   Assets/Prefabs/Soccer/
   ```

### Day 2-3: Framework Extraction

4. **Extract Sport-Agnostic Base**
   - [ ] Create `SportGameManager.cs` (abstract)
   - [ ] Create `ISportCommand.cs` (interface)
   - [ ] Refactor `GameModeManager.cs` to use base
   - [ ] Test basketball still works

5. **Refactor Basketball Code**
   - [ ] Move basketball code to `Basketball/` folder
   - [ ] Update references
   - [ ] Test functionality

### Day 4-5: Soccer Module Creation

6. **Create Soccer Manager**
   - [ ] Create `SoccerGameManager.cs`
   - [ ] Implement base class methods
   - [ ] Basic initialization working

7. **Create Soccer Commands**
   - [ ] Create `SoccerCommands.cs`
   - [ ] Implement basic commands (dribble, pass, shoot)
   - [ ] Connect to PythonCodingManager

8. **Create Soccer Scene**
   - [ ] New scene: `SoccerGame.unity`
   - [ ] Add soccer field
   - [ ] Add soccer ball
   - [ ] Add soccer player
   - [ ] Basic scene working

---

## 📝 CODE TEMPLATES

### Sport-Agnostic Base Class:

```csharp
// Assets/Scripts/Sport/SportGameManager.cs
using UnityEngine;

public abstract class SportGameManager : MonoBehaviour
{
    public string sportName;
    
    public abstract void InitializeSport();
    public abstract void HandleSportSpecificMechanics();
    public abstract void LoadLevel(string levelId);
    public abstract void ExecuteCommand(string command, params object[] args);
}
```

### Soccer Implementation:

```csharp
// Assets/Scripts/Soccer/SoccerGameManager.cs
using UnityEngine;

public class SoccerGameManager : SportGameManager
{
    public SoccerField field;
    public SoccerBall ball;
    public SoccerPlayer player;
    
    public override void InitializeSport()
    {
        sportName = "soccer";
        // Initialize soccer-specific components
        field = FindObjectOfType<SoccerField>();
        ball = FindObjectOfType<SoccerBall>();
        player = FindObjectOfType<SoccerPlayer>();
    }
    
    public override void HandleSportSpecificMechanics()
    {
        // Soccer-specific game logic
    }
    
    public override void LoadLevel(string levelId)
    {
        // Load soccer level
    }
    
    public override void ExecuteCommand(string command, params object[] args)
    {
        // Execute soccer command
    }
}
```

---

## ✅ CHECKLIST FOR THIS WEEK

### Setup (Day 1):
- [ ] Unity project located and accessible
- [ ] Unity version verified (2021.3+ or 2022.3+)
- [ ] Required packages installed
- [ ] Project opens successfully
- [ ] Folder structure created

### Framework (Day 2-3):
- [ ] Sport-agnostic base classes created
- [ ] Basketball code refactored
- [ ] Basketball functionality still works
- [ ] Tests pass

### Soccer Module (Day 4-5):
- [ ] SoccerGameManager created
- [ ] SoccerCommands created
- [ ] Soccer scene created
- [ ] Basic soccer environment working
- [ ] Can switch between basketball/soccer

---

## 🎯 SUCCESS CRITERIA

### End of Week 1:
- ✅ Unity project accessible
- ✅ Sport-agnostic framework extracted
- ✅ Basketball code refactored (still works)
- ✅ Soccer module structure created
- ✅ Basic soccer scene functional
- ✅ Can switch between sports

### Ready for Week 2:
- ✅ Framework ready for game mechanics
- ✅ Soccer environment set up
- ✅ Ready to build soccer game mechanics
- ✅ Ready to create soccer levels

---

## 📚 RESOURCES NEEDED

### Documentation:
- [ ] Current Unity project structure documented
- [ ] Basketball code architecture documented
- [ ] Integration points identified
- [ ] Dependencies listed

### Assets:
- [ ] Soccer field model/texture (or create in Unity)
- [ ] Soccer ball model/texture (or use Unity primitives)
- [ ] Soccer player model (or use Unity primitives)
- [ ] World Cup 2026 branding assets (optional)

### Tools:
- [ ] Unity Editor (2021.3+ or 2022.3+)
- [ ] Git (for version control)
- [ ] Code editor (VS Code, Visual Studio, Rider)

---

## 🚨 BLOCKERS TO RESOLVE

### Potential Issues:

1. **Unity Project Access**
   - Need: Location and access method
   - Solution: Document path, set up access

2. **Unity Version Mismatch**
   - Need: Correct Unity version
   - Solution: Install required version

3. **Missing Dependencies**
   - Need: Required packages
   - Solution: Install via Package Manager

4. **Code Dependencies**
   - Need: Understand current architecture
   - Solution: Review existing scripts, document structure

---

## 📞 NEXT STEPS

### This Week:
1. **Day 1:** Locate Unity project, verify setup
2. **Day 2-3:** Extract framework, refactor basketball
3. **Day 4-5:** Create soccer module, basic scene

### Next Week:
1. Build soccer game mechanics
2. Create soccer levels
3. Integrate with content system

---

**Status:** 🚀 Ready to Execute  
**Priority:** HIGH - Foundation for 3-month timeline  
**Next Action:** Locate Unity project and verify setup


