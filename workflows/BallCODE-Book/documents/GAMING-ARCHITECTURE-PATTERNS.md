# BallCODE Gaming Architecture & Patterns
## System Architecture and Design Patterns for Unity Game

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Purpose:** Define architecture, design patterns, and system structure for BallCODE Unity game  
**Status:** Active Documentation

---

## 🎯 Architecture Overview

The BallCODE game follows a **Manager-based architecture** with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                    Unity Game Layer                          │
├─────────────────────────────────────────────────────────────┤
│  Story Mode  │  Game Modes  │  UI System  │  Data Layer    │
│  Manager     │  Managers    │  Managers   │  Managers      │
├─────────────────────────────────────────────────────────────┤
│                    Integration Layer                         │
│  Book Integration  │  Website Integration  │  Curriculum      │
├─────────────────────────────────────────────────────────────┤
│                    External Systems                          │
│  Website (Jekyll)  │  n8n Automation  │  Curriculum JSON   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Core Architecture Patterns

### 1. Manager Pattern (Singleton)

**Purpose:** Centralized control for major game systems

**Implementation:**
```csharp
public class GameModeManager : MonoBehaviour
{
    public static GameModeManager Instance { get; private set; }
    
    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }
}
```

**Managers in System:**
- `GameModeManager` - Game mode transitions
- `StoryModeManager` - Story mode control
- `LevelDataManager` - Level data loading
- `MetricsCollector` - Analytics tracking

**Benefits:**
- Single point of access
- Persistent across scenes
- Easy to reference from anywhere

---

### 2. Configuration Pattern

**Purpose:** Separate configuration from implementation

**Implementation:**
```csharp
[System.Serializable]
public class TrainingModeConfig
{
    public int episode;
    public string codingConcept;
    public string monster;
    public string focus;
}

public class TrainingModeManager : MonoBehaviour
{
    public void StartTraining(TrainingModeConfig config)
    {
        // Use config to set up training mode
    }
}
```

**Usage:**
- Game mode configurations
- Level data structures
- Exercise settings

**Benefits:**
- Easy to modify without code changes
- Serializable (can save/load)
- Clear separation of data and logic

---

### 3. Data-Driven Design

**Purpose:** Define game content through data files, not code

**Structure:**
```
LevelData (JSON)
    ├── Level Identification
    ├── Game Mode Configuration
    ├── Video Configuration
    ├── Strategy Configuration
    ├── Learning Objectives
    └── Exercise Configuration
```

**Implementation:**
```csharp
public class LevelDataManager : MonoBehaviour
{
    private Dictionary<string, LevelData> _levelCache;
    
    public LevelData GetLevel(string levelId)
    {
        // Load from JSON, cache, return
    }
}
```

**Benefits:**
- Easy content creation (no code changes)
- Can be edited by non-programmers
- Supports dynamic content loading

---

### 4. State Machine Pattern

**Purpose:** Manage game state transitions

**States:**
- Story Mode
- Game Mode (Training/Prediction/Math/Block Coding/Python)
- Exercise Active
- Exercise Complete
- Return to Story/Book

**Implementation:**
```csharp
public enum GameState
{
    StoryMode,
    GameMode,
    ExerciseActive,
    ExerciseComplete,
    Returning
}

public class GameStateManager : MonoBehaviour
{
    private GameState _currentState;
    
    public void TransitionToState(GameState newState)
    {
        ExitState(_currentState);
        _currentState = newState;
        EnterState(_currentState);
    }
}
```

---

### 5. Observer Pattern (Events)

**Purpose:** Decouple systems through events

**Implementation:**
```csharp
public class ExerciseManager : MonoBehaviour
{
    public static event Action<bool, float> OnExerciseComplete;
    
    private void CompleteExercise(bool success, float score)
    {
        OnExerciseComplete?.Invoke(success, score);
    }
}

public class StoryModeManager : MonoBehaviour
{
    void OnEnable()
    {
        ExerciseManager.OnExerciseComplete += HandleExerciseComplete;
    }
    
    void OnDisable()
    {
        ExerciseManager.OnExerciseComplete -= HandleExerciseComplete;
    }
    
    private void HandleExerciseComplete(bool success, float score)
    {
        // Handle completion
    }
}
```

**Benefits:**
- Loose coupling
- Easy to add new listeners
- Flexible system communication

---

## 📦 System Components

### Story Mode System

**Components:**
- `StoryModeManager` - Main controller
- `StoryData` - Data structures
- `StoryEpisodeCreator` - Editor tool
- `BallCODEStarter` - Entry point

**Flow:**
```
BallCODEStarter (URL params)
    ↓
StoryModeManager (Load episode)
    ↓
Page Turner UI (Display spreads)
    ↓
Exercise Button (if exercise spread)
    ↓
GameModeManager (Load exercise)
    ↓
Return to StoryModeManager (On completion)
```

**Key Features:**
- Page-by-page navigation
- Audio narration sync
- Exercise integration
- Progress tracking

---

### Game Mode System

**Components:**
- `GameModeManager` - Central coordinator
- `TrainingModeManager` - Training exercises
- `PredictionModeManager` - Prediction exercises
- `MathModeManager` - Math exercises
- `BlockCodingManager` - Block coding exercises
- `PythonCodingManager` - Python coding exercises

**Flow:**
```
GameModeManager.LoadGameMode()
    ↓
Determine mode type
    ↓
Load appropriate ModeManager
    ↓
Configure with LevelData
    ↓
Start exercise
    ↓
Track progress
    ↓
OnExerciseComplete()
    ↓
Return to Story/Book
```

**Key Features:**
- Mode-agnostic interface
- Consistent completion handling
- Metrics collection
- Book integration support

---

### Level Data System

**Components:**
- `LevelData` - Data structure
- `LevelDataManager` - Loading and caching
- `LevelCreator` - Editor tool
- JSON level files

**Flow:**
```
Level JSON File
    ↓
LevelDataManager.LoadLevel()
    ↓
Parse JSON → LevelData object
    ↓
Cache in dictionary
    ↓
Return to GameModeManager
    ↓
Configure exercise
```

**Key Features:**
- JSON-based level definitions
- Runtime loading
- Caching for performance
- Editor tools for creation

---

### Integration System

**Components:**
- `BallCODEStarter` - URL parameter parsing
- `BookReturnHandler` - JavaScript interop
- `BookGameIntegration` - Book mapping

**Flow:**
```
Website/Book URL
    ↓
BallCODEStarter.CheckURLParameters()
    ↓
Parse book/exercise parameters
    ↓
Map to Level ID
    ↓
Store return URL in PlayerPrefs
    ↓
Load exercise via GameModeManager
    ↓
On completion: BookReturnHandler
    ↓
JavaScript communication
    ↓
Return to website/book page
```

**Key Features:**
- Deep linking from books
- URL parameter parsing
- JavaScript interop (WebGL)
- Seamless return flow

---

## 🔄 Data Flow Patterns

### Level Loading Flow

```
1. Request Level (Level ID)
    ↓
2. Check Cache (LevelDataManager)
    ↓
3. If not cached: Load from Resources/StreamingAssets
    ↓
4. Parse JSON → LevelData object
    ↓
5. Cache for future use
    ↓
6. Return LevelData
    ↓
7. Configure Game Mode
    ↓
8. Start Exercise
```

### Exercise Completion Flow

```
1. Exercise Complete (success, score)
    ↓
2. GameModeManager.OnExerciseComplete()
    ↓
3. MetricsCollector.TrackCompletion()
    ↓
4. Check PlayerPrefs for BookNumber
    ↓
5. If from book: BookReturnHandler
    ↓
6. If from story: StoryModeManager.OnExerciseComplete()
    ↓
7. JavaScript interop (if WebGL + book)
    ↓
8. Return to appropriate location
```

---

## 🎨 UI Architecture

### UI Manager Pattern

**Structure:**
```
Canvas (Root)
    ├── StoryModeCanvas
    │   ├── PageTurnerContainer
    │   ├── NavigationPanel
    │   └── AudioControls
    ├── GameModeCanvas
    │   ├── ExerciseUI
    │   ├── ScoreDisplay
    │   └── InstructionsPanel
    └── OverlayCanvas
        └── LoadingIndicator
```

**Managers:**
- `StoryModeUI` - Story mode interface
- `ExerciseUI` - Exercise interface
- `ScoreDisplay` - Score and feedback

**Pattern:**
- Separate Canvas per major mode
- UI Managers handle their own canvas
- Overlay canvas for global UI (loading, errors)

---

## 🔌 Integration Patterns

### Book Integration Pattern

```
Physical Book QR Code
    ↓
Website URL: ballcode.co/play?book=1&exercise=foundation-block
    ↓
Unity WebGL Build
    ↓
BallCODEStarter.CheckURLParameters()
    ↓
Parse: book=1, exercise=foundation-block
    ↓
Map to Level ID: "book1_foundation_block"
    ↓
Store return URL in PlayerPrefs
    ↓
Load exercise
    ↓
On completion: Return to book page via JavaScript
```

### Curriculum Integration Pattern

```
LevelData
    ├── learningObjectives[] (Curriculum alignment)
    ├── successCriteria[] (Assessment alignment)
    ├── codingConcept (Concept mapping)
    └── difficultyLevel (Grade level mapping)
    ↓
CurriculumValidator.ValidateAlignment()
    ↓
Ensure curriculum consistency
    ↓
Map to Three-Phase Learning Pathway
    ↓
Display in UI (if needed)
```

---

## 🎯 Design Principles

### 1. Separation of Concerns
- **Data:** Separate from logic (LevelData, StoryData)
- **UI:** Separate from game logic (UI Managers)
- **Integration:** Separate from core game (Integration handlers)

### 2. Single Responsibility
- Each manager handles one system
- Each data structure represents one concept
- Each UI component has one purpose

### 3. Dependency Injection (via Inspector)
- Managers assigned in Unity Inspector
- No hard dependencies in code
- Easy to swap implementations

### 4. Data-Driven Design
- Content defined in JSON/data files
- Code handles logic, not content
- Easy to add new levels/exercises

### 5. Event-Driven Communication
- Systems communicate via events
- Loose coupling between components
- Easy to extend functionality

---

## 📊 System Dependencies

```
BallCODEStarter
    ├── StoryModeManager
    │   └── GameModeManager
    │       ├── TrainingModeManager
    │       ├── PredictionModeManager
    │       ├── MathModeManager
    │       ├── BlockCodingManager
    │       └── PythonCodingManager
    ├── LevelDataManager
    │   └── LevelData (JSON)
    └── BookReturnHandler
        └── JavaScript Interop
```

**Key Dependencies:**
- `GameModeManager` depends on mode managers
- `StoryModeManager` depends on `GameModeManager`
- All systems can access `LevelDataManager`
- Integration systems are independent

---

## 🔧 Extension Points

### Adding New Game Mode

1. **Create Mode Manager:**
```csharp
public class NewModeManager : MonoBehaviour
{
    public void StartNewMode(NewModeConfig config)
    {
        // Implementation
    }
}
```

2. **Add to GameModeManager:**
```csharp
public class GameModeManager : MonoBehaviour
{
    public NewModeManager newMode;
    
    void LoadNewMode(int episode, string concept, string monster)
    {
        // Load new mode
    }
}
```

3. **Create Level Data:**
```json
{
  "levelId": "newmode_level1",
  "gameMode": "newmode",
  "codingConcept": "concept",
  ...
}
```

### Adding New Integration

1. **Create Integration Handler:**
```csharp
public class NewIntegrationHandler : MonoBehaviour
{
    public void HandleIntegration(string data)
    {
        // Handle integration
    }
}
```

2. **Add to BallCODEStarter:**
```csharp
void CheckURLParameters()
{
    if (GetURLParameter("newparam", out string value))
    {
        newIntegrationHandler.HandleIntegration(value);
    }
}
```

---

## 📚 Reference Architecture Documents

- **Unity Setup:** `Unity-Scripts/UNITY-SETUP-GUIDE.md`
- **Game Architecture:** `GAME-ARCHITECTURE-COMPLETE.md`
- **Integration Guide:** `Unity-Scripts/INTEGRATION-WITH-EXISTING-GAME.md`
- **Level Data Structure:** `Unity-Scripts/LevelData.cs`

---

## 🎯 Key Takeaways

1. **Manager Pattern:** Centralized control with singleton managers
2. **Configuration Pattern:** Separate data from logic
3. **Data-Driven:** Content in JSON, logic in code
4. **Event-Driven:** Loose coupling via events
5. **Separation of Concerns:** Clear boundaries between systems
6. **Extension Points:** Easy to add new modes/integrations
7. **Integration Layer:** Clean separation from external systems

---

**This architecture supports:**
- Easy content creation (JSON levels)
- Multiple game modes (extensible)
- Book integration (URL parameters)
- Website integration (JavaScript interop)
- Curriculum alignment (data-driven)
- Performance optimization (caching, pooling)



