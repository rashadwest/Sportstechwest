# Unity & C# Gaming Development Rules
## BallCODE Game Development Standards

**Copyright © 2025 Rashad West. All Rights Reserved.**

**PROJECT IDENTIFIER:** `BALLCODE-GAME-2025-RULES-v1.0`  
**Project:** BallCODE Game - Unity Educational Basketball Game  
**Repository:** BallCODE-Book  
**Last Updated:** December 2025  
**Unique ID:** BCG-RULES-2025-12-UNITY-GAMING

---

## 🎯 Purpose & Scope

**This document defines rules, standards, and best practices specifically for Unity and C# game development in the BallCODE project.**

**Separate from:**
- Website development (see `AIMCODE-WEBSITE-FRAMEWORK.md`)
- n8n automation (see `N8N_WORKFLOW_DEVELOPMENT_GUIDE.md`)
- Book writing (see `.cursorrules` Book Writing Rules section)

**This document covers:**
- Unity C# coding standards
- Game architecture patterns
- Performance optimization
- Educational game design principles
- Integration with books and curriculum

---

## 🏗️ Tech Stack & Requirements

### Unity Version
- **Minimum:** Unity 2021.3 LTS
- **Recommended:** Unity 2022.3 LTS or later
- **Target Platforms:** WebGL (primary), Standalone (Windows/Mac/Linux)

### C# Version
- **Language Version:** C# 8.0 or later
- **.NET Standard:** 2.1
- **Unity API Compatibility:** .NET Standard 2.1

### Required Unity Packages
- **TextMeshPro** (for UI text)
- **Unity WebGL Support** (for web builds)
- **Unity Analytics** (optional, for metrics)

### Key Dependencies
- **Unity Engine:** Core game engine
- **Unity UI System:** For all UI elements
- **Unity Audio System:** For narration and sound effects
- **JSON.NET** (Newtonsoft.Json): For level data loading (if not using Unity's built-in JSON)

---

## 📁 Project Structure

### Unity Project Organization

```
Assets/
├── Scripts/
│   ├── Managers/              # Game management scripts
│   │   ├── GameModeManager.cs
│   │   ├── StoryModeManager.cs
│   │   └── LevelDataManager.cs
│   ├── GameModes/            # Game mode implementations
│   │   ├── TrainingModeManager.cs
│   │   ├── PredictionModeManager.cs
│   │   ├── MathModeManager.cs
│   │   ├── BlockCodingManager.cs
│   │   └── PythonCodingManager.cs
│   ├── Data/                 # Data structures
│   │   ├── LevelData.cs
│   │   ├── StoryData.cs
│   │   └── PlayerData.cs
│   ├── UI/                   # UI scripts
│   │   ├── PageTurner.cs
│   │   ├── ExerciseUI.cs
│   │   └── ScoreDisplay.cs
│   ├── Utils/                # Utility scripts
│   │   ├── MetricsCollector.cs
│   │   └── BookReturnHandler.cs
│   └── Editor/               # Editor tools
│       ├── StoryEpisodeCreator.cs
│       └── LevelCreator.cs
├── Scenes/
│   ├── StoryModeScene.unity
│   ├── TrainingModeScene.unity
│   └── MainMenuScene.unity
├── Resources/
│   └── Levels/               # Level JSON files
├── StreamingAssets/
│   └── Videos/                # Video files for exercises
└── Audio/
    ├── Narration/
    └── SoundEffects/
```

---

## 📝 Naming Conventions

### C# Classes & Scripts
- **Classes:** `PascalCase` (e.g., `GameModeManager`, `LevelData`)
- **Script Files:** Match class name exactly (e.g., `GameModeManager.cs`)
- **Interfaces:** `IPascalCase` with "I" prefix (e.g., `IGameMode`, `ILevelLoader`)

### Variables & Fields
- **Public Fields:** `camelCase` (e.g., `currentLevel`, `playerScore`)
- **Private Fields:** `_camelCase` with underscore prefix (e.g., `_currentEpisode`, `_gameState`)
- **Serialized Fields:** `camelCase` with `[SerializeField]` attribute
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_LEVEL_COUNT`, `DEFAULT_DIFFICULTY`)

### Methods
- **Public Methods:** `PascalCase` (e.g., `LoadGameMode()`, `OnExerciseComplete()`)
- **Private Methods:** `PascalCase` (e.g., `InitializeLevel()`, `CalculateScore()`)
- **Event Handlers:** `OnEventName` (e.g., `OnButtonClick()`, `OnLevelComplete()`)

### Unity-Specific
- **GameObjects:** Descriptive names (e.g., `StoryModeCanvas`, `ExerciseButton`)
- **Scenes:** `PascalCase` with "Scene" suffix (e.g., `StoryModeScene.unity`)
- **Prefabs:** `PascalCase` (e.g., `PlayerPrefab`, `ExerciseButtonPrefab`)

---

## 🎮 Unity Script Patterns

### ✅ CORRECT: MonoBehaviour Script Structure

```csharp
using UnityEngine;
using System.Collections;

/// <summary>
/// Manages game mode transitions and exercise configuration
/// Handles parameter passing and completion callbacks
/// </summary>
public class GameModeManager : MonoBehaviour
{
    // Singleton pattern
    public static GameModeManager Instance;
    
    [Header("Game Mode References")]
    [SerializeField] private TrainingModeManager trainingMode;
    [SerializeField] private PredictionModeManager predictionMode;
    
    [Header("Configuration")]
    [SerializeField] private int defaultDifficulty = 1;
    
    // Private fields with underscore prefix
    private string _currentGameMode;
    private int _currentEpisode;
    private float _gameModeStartTime;
    
    // Constants
    private const int MAX_ATTEMPTS = 3;
    private const float DEFAULT_TIMEOUT = 30f;
    
    void Awake()
    {
        // Singleton setup
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
    
    void Start()
    {
        InitializeGameMode();
    }
    
    /// <summary>
    /// Load a game mode with story episode context
    /// </summary>
    /// <param name="mode">Game mode name</param>
    /// <param name="episode">Episode number</param>
    /// <param name="codingConcept">Coding concept to teach</param>
    /// <param name="monster">Monster name from story</param>
    public void LoadGameMode(string mode, int episode, string codingConcept, string monster)
    {
        if (string.IsNullOrEmpty(mode))
        {
            Debug.LogError("[GameModeManager] Mode cannot be null or empty!");
            return;
        }
        
        _currentGameMode = mode;
        _currentEpisode = episode;
        _gameModeStartTime = Time.time;
        
        // Configure and start game mode
        switch (mode.ToLower())
        {
            case "training":
                LoadTrainingMode(episode, codingConcept, monster);
                break;
            case "prediction":
                LoadPredictionMode(episode, codingConcept, monster);
                break;
            default:
                Debug.LogWarning($"[GameModeManager] Unknown game mode: {mode}");
                break;
        }
    }
    
    /// <summary>
    /// Called when exercise is completed
    /// </summary>
    /// <param name="success">Whether exercise was successful</param>
    /// <param name="score">Final score (0-100)</param>
    public void OnExerciseComplete(bool success, float score)
    {
        // Validate score
        score = Mathf.Clamp(score, 0f, 100f);
        
        // Track metrics
        if (MetricsCollector.Instance != null)
        {
            float totalTime = Time.time - _gameModeStartTime;
            MetricsCollector.Instance.OnExerciseComplete(
                _currentEpisode,
                success,
                score,
                totalTime
            );
        }
        
        // Return to story mode or book
        ReturnToStoryOrBook(success, score);
    }
    
    private void InitializeGameMode()
    {
        // Initialization logic
    }
    
    private void LoadTrainingMode(int episode, string concept, string monster)
    {
        if (trainingMode == null)
        {
            Debug.LogError("[GameModeManager] TrainingModeManager not assigned!");
            return;
        }
        
        TrainingModeConfig config = new TrainingModeConfig
        {
            episode = episode,
            codingConcept = concept,
            monster = monster,
            focus = GetTrainingFocus(episode)
        };
        
        trainingMode.StartTraining(config);
    }
    
    private void LoadPredictionMode(int episode, string concept, string monster)
    {
        // Implementation
    }
    
    private string GetTrainingFocus(int episode)
    {
        return episode switch
        {
            1 => "state_tracking",
            2 => "position_analysis",
            3 => "pattern_recognition",
            _ => "general"
        };
    }
    
    private void ReturnToStoryOrBook(bool success, float score)
    {
        // Return logic
    }
}
```

### ❌ WRONG: Poor Unity Script Structure

```csharp
// Missing documentation
// No error handling
// No validation
// Poor naming
public class gameModeManager : MonoBehaviour
{
    public TrainingModeManager training; // No [SerializeField]
    public int difficulty; // Magic number, no default
    
    void Start()
    {
        // No null checks
        training.StartTraining(null); // Passing null
    }
    
    // No documentation
    public void loadMode(string m, int e)
    {
        // No validation
        // No error handling
        // Abbreviated names
    }
}
```

---

## 🛡️ Error Handling & Validation

### ✅ CORRECT: Comprehensive Error Handling

```csharp
public void LoadGameModeFromLevel(string levelId)
{
    // Validate input
    if (string.IsNullOrEmpty(levelId))
    {
        Debug.LogError("[GameModeManager] Level ID cannot be null or empty!");
        return;
    }
    
    // Check dependencies
    if (LevelDataManager.Instance == null)
    {
        Debug.LogError("[GameModeManager] LevelDataManager not found! Make sure it's in the scene.");
        return;
    }
    
    // Get level data
    LevelData level = LevelDataManager.Instance.GetLevel(levelId);
    if (level == null)
    {
        Debug.LogError($"[GameModeManager] Level not found: {levelId}");
        return;
    }
    
    // Validate level data
    if (string.IsNullOrEmpty(level.gameMode))
    {
        Debug.LogError($"[GameModeManager] Level {levelId} has no game mode specified!");
        return;
    }
    
    // Load game mode
    try
    {
        LoadGameMode(level.gameMode, level.episodeNumber, level.codingConcept, "Level Challenge");
    }
    catch (Exception e)
    {
        Debug.LogError($"[GameModeManager] Error loading game mode: {e.Message}");
        Debug.LogException(e);
    }
}
```

### ❌ WRONG: Missing Error Handling

```csharp
public void LoadGameModeFromLevel(string levelId)
{
    // No validation
    LevelData level = LevelDataManager.Instance.GetLevel(levelId);
    // No null check
    LoadGameMode(level.gameMode, level.episodeNumber, level.codingConcept, "Level Challenge");
    // No error handling
}
```

---

## 🎯 Unity Lifecycle Methods

### Proper Usage

```csharp
public class GameModeManager : MonoBehaviour
{
    void Awake()
    {
        // Use for:
        // - Singleton setup
        // - Initializing references
        // - Setting up before other objects
        // DO NOT use for:
        // - Finding objects (use Start)
        // - Accessing other objects (may not be initialized)
    }
    
    void Start()
    {
        // Use for:
        // - Finding objects (FindObjectOfType, etc.)
        // - Initializing after all objects are created
        // - Setting up UI
        // - Starting coroutines
    }
    
    void Update()
    {
        // Use for:
        // - Input handling
        // - Continuous updates
        // AVOID if possible - use events/coroutines instead
    }
    
    void OnEnable()
    {
        // Use for:
        // - Subscribing to events
        // - Re-enabling after disable
    }
    
    void OnDisable()
    {
        // Use for:
        // - Unsubscribing from events
        // - Cleanup
    }
    
    void OnDestroy()
    {
        // Use for:
        // - Final cleanup
        // - Releasing resources
    }
}
```

---

## 🔄 Singleton Pattern

### ✅ CORRECT: Thread-Safe Singleton

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
    
    void OnDestroy()
    {
        if (Instance == this)
        {
            Instance = null;
        }
    }
}
```

### ❌ WRONG: Unsafe Singleton

```csharp
public class GameModeManager : MonoBehaviour
{
    public static GameModeManager Instance; // No property, no null check
    
    void Awake()
    {
        Instance = this; // No check for existing instance
        // Multiple instances possible
    }
}
```

---

## 📊 Data Structures & Serialization

### ✅ CORRECT: Serializable Data Classes

```csharp
using UnityEngine;
using System;

/// <summary>
/// Configuration for training mode exercises
/// </summary>
[System.Serializable]
public class TrainingModeConfig
{
    [Header("Episode Info")]
    public int episode;
    
    [Header("Educational Content")]
    public string codingConcept;
    public string monster;
    public string focus;
    
    [Header("Difficulty")]
    [Range(1, 5)]
    public int difficultyLevel = 1;
    
    [Header("Options")]
    public bool allowRetry = true;
    public int maxAttempts = 3;
    
    // Validation method
    public bool IsValid()
    {
        if (episode < 1 || episode > 10)
        {
            Debug.LogError($"[TrainingModeConfig] Invalid episode: {episode}");
            return false;
        }
        
        if (string.IsNullOrEmpty(codingConcept))
        {
            Debug.LogError("[TrainingModeConfig] Coding concept cannot be empty!");
            return false;
        }
        
        return true;
    }
}
```

### ❌ WRONG: Poor Data Structure

```csharp
// No serialization
// No documentation
// No validation
public class TrainingModeConfig
{
    public int episode; // No range validation
    public string concept; // No null check
    // No organization
    // No header attributes
}
```

---

## 🎨 UI Patterns

### ✅ CORRECT: UI Manager Pattern

```csharp
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class ExerciseUI : MonoBehaviour
{
    [Header("UI References")]
    [SerializeField] private TextMeshProUGUI exerciseTitle;
    [SerializeField] private TextMeshProUGUI scoreText;
    [SerializeField] private Button submitButton;
    [SerializeField] private Button retryButton;
    
    [Header("Configuration")]
    [SerializeField] private Color successColor = Color.green;
    [SerializeField] private Color failureColor = Color.red;
    
    private void Start()
    {
        // Validate references
        if (exerciseTitle == null)
        {
            Debug.LogError("[ExerciseUI] Exercise title text not assigned!");
        }
        
        if (submitButton == null)
        {
            Debug.LogError("[ExerciseUI] Submit button not assigned!");
        }
        else
        {
            submitButton.onClick.AddListener(OnSubmitClicked);
        }
        
        if (retryButton != null)
        {
            retryButton.onClick.AddListener(OnRetryClicked);
        }
    }
    
    public void UpdateScore(float score)
    {
        if (scoreText != null)
        {
            scoreText.text = $"Score: {score:F1}%";
            scoreText.color = score >= 70f ? successColor : failureColor;
        }
    }
    
    public void ShowSuccess()
    {
        // Show success UI
    }
    
    public void ShowFailure()
    {
        // Show failure UI
    }
    
    private void OnSubmitClicked()
    {
        // Handle submit
    }
    
    private void OnRetryClicked()
    {
        // Handle retry
    }
    
    private void OnDestroy()
    {
        // Clean up event listeners
        if (submitButton != null)
        {
            submitButton.onClick.RemoveListener(OnSubmitClicked);
        }
        
        if (retryButton != null)
        {
            retryButton.onClick.RemoveListener(OnRetryClicked);
        }
    }
}
```

---

## ⚡ Performance Optimization

### ✅ CORRECT: Performance-Conscious Code

```csharp
public class LevelDataManager : MonoBehaviour
{
    // Cache frequently accessed data
    private Dictionary<string, LevelData> _levelCache = new Dictionary<string, LevelData>();
    private List<LevelData> _allLevels = new List<LevelData>();
    
    // Use object pooling for frequently created/destroyed objects
    private Queue<GameObject> _objectPool = new Queue<GameObject>();
    
    public LevelData GetLevel(string levelId)
    {
        // Check cache first
        if (_levelCache.TryGetValue(levelId, out LevelData cachedLevel))
        {
            return cachedLevel;
        }
        
        // Load from resources
        LevelData level = LoadLevelFromResources(levelId);
        if (level != null)
        {
            _levelCache[levelId] = level; // Cache for future use
        }
        
        return level;
    }
    
    // Use coroutines for async operations
    private IEnumerator LoadLevelAsync(string levelId, System.Action<LevelData> callback)
    {
        // Simulate async loading
        yield return new WaitForSeconds(0.1f);
        
        LevelData level = GetLevel(levelId);
        callback?.Invoke(level);
    }
    
    // Avoid Update() when possible - use events
    private void OnLevelComplete()
    {
        // Event-driven instead of polling in Update()
    }
}
```

### ❌ WRONG: Performance Issues

```csharp
public class LevelDataManager : MonoBehaviour
{
    void Update()
    {
        // Loading in Update() - runs every frame!
        LevelData level = LoadLevelFromResources("level1");
        
        // Finding objects every frame
        GameModeManager manager = FindObjectOfType<GameModeManager>();
        
        // No caching
        // No object pooling
        // No async loading
    }
}
```

---

## 🎓 Educational Game Design Principles

### Curriculum Integration

```csharp
/// <summary>
/// Ensures game exercises align with curriculum learning objectives
/// </summary>
public class CurriculumValidator
{
    /// <summary>
    /// Validates that level data includes required curriculum elements
    /// </summary>
    public static bool ValidateCurriculumAlignment(LevelData level)
    {
        // Must have learning objectives
        if (level.learningObjectives == null || level.learningObjectives.Length == 0)
        {
            Debug.LogWarning($"[CurriculumValidator] Level {level.levelId} has no learning objectives!");
            return false;
        }
        
        // Must have success criteria
        if (level.successCriteria == null || level.successCriteria.Length == 0)
        {
            Debug.LogWarning($"[CurriculumValidator] Level {level.levelId} has no success criteria!");
            return false;
        }
        
        // Must have coding concept
        if (string.IsNullOrEmpty(level.codingConcept))
        {
            Debug.LogWarning($"[CurriculumValidator] Level {level.levelId} has no coding concept!");
            return false;
        }
        
        return true;
    }
    
    /// <summary>
    /// Maps curriculum phase to game exercise type
    /// </summary>
    public static ExerciseType GetExerciseTypeForPhase(CurriculumPhase phase)
    {
        return phase switch
        {
            CurriculumPhase.BlockCoding => ExerciseType.BlockCoding,
            CurriculumPhase.TransitionBridge => ExerciseType.Analysis,
            CurriculumPhase.PythonLearning => ExerciseType.Prediction,
            _ => ExerciseType.Freeplay
        };
    }
}

public enum CurriculumPhase
{
    BlockCoding,        // Phase 1: Sports Language (Block Coding)
    TransitionBridge,   // Phase 2: Transition Bridge
    PythonLearning      // Phase 3: Python Learning
}
```

---

## 🔗 Integration Patterns

### Book → Game Integration

```csharp
/// <summary>
/// Handles integration between physical books and game exercises
/// </summary>
public class BookGameIntegration : MonoBehaviour
{
    /// <summary>
    /// Load exercise from book URL parameters
    /// Expected format: ?book=1&exercise=foundation-block&source=book
    /// </summary>
    public void LoadExerciseFromBook(int bookNumber, string exerciseId, string returnUrl)
    {
        // Validate book number
        if (bookNumber < 1 || bookNumber > 3)
        {
            Debug.LogError($"[BookGameIntegration] Invalid book number: {bookNumber}");
            return;
        }
        
        // Map book + exercise to level ID
        string levelId = MapBookToLevelId(bookNumber, exerciseId);
        if (string.IsNullOrEmpty(levelId))
        {
            Debug.LogError($"[BookGameIntegration] Could not map book {bookNumber}, exercise '{exerciseId}' to level ID");
            return;
        }
        
        // Store return information
        PlayerPrefs.SetInt("BookNumber", bookNumber);
        PlayerPrefs.SetString("BookReturnUrl", returnUrl);
        PlayerPrefs.SetString("ExerciseSource", "book");
        PlayerPrefs.Save();
        
        // Load exercise
        if (GameModeManager.Instance != null)
        {
            GameModeManager.Instance.LoadGameModeFromLevel(levelId);
        }
    }
    
    private string MapBookToLevelId(int bookNumber, string exerciseId)
    {
        // Map book number and exercise to level ID
        return bookNumber switch
        {
            1 => exerciseId switch
            {
                "foundation-block" => "book1_foundation_block",
                "coding-1-2" => "book1_coding_1_2",
                "math-foundation" => "book1_math_foundation",
                _ => $"book1_{exerciseId.Replace("-", "_")}"
            },
            2 => exerciseId switch
            {
                "decision-crossover" => "book2_decision_crossover",
                "math-decision" => "book2_math_decision",
                _ => $"book2_{exerciseId.Replace("-", "_")}"
            },
            3 => exerciseId switch
            {
                "pattern-loop" => "book3_pattern_loop",
                "math-pattern" => "book3_math_pattern",
                _ => $"book3_{exerciseId.Replace("-", "_")}"
            },
            _ => null
        };
    }
}
```

---

## 📋 Code Review Checklist

Before considering Unity/C# code complete:

- [ ] No TODO comments remain
- [ ] All public methods have XML documentation (`/// <summary>`)
- [ ] All parameters validated (null checks, range checks)
- [ ] All error cases handled with appropriate Debug.LogError
- [ ] Singleton pattern implemented correctly (if used)
- [ ] Unity lifecycle methods used appropriately
- [ ] No FindObjectOfType in Update() or frequent calls
- [ ] Object pooling used for frequently created/destroyed objects
- [ ] Event listeners cleaned up in OnDestroy/OnDisable
- [ ] Serialized fields use [SerializeField] attribute
- [ ] Constants used instead of magic numbers
- [ ] Naming conventions followed (PascalCase classes, camelCase fields)
- [ ] Curriculum alignment validated (for game levels)
- [ ] Performance considerations addressed
- [ ] Code tested in Unity Editor
- [ ] Code tested in WebGL build (if applicable)

---

## 🚫 Common Mistakes to Avoid

### ❌ Don't: Use Update() for Everything

```csharp
void Update()
{
    // Polling every frame - inefficient!
    if (Input.GetKeyDown(KeyCode.Space))
    {
        // Handle input
    }
    
    // Finding objects every frame - very inefficient!
    GameModeManager manager = FindObjectOfType<GameModeManager>();
}
```

### ✅ Do: Use Events and Coroutines

```csharp
void Start()
{
    // Subscribe to events
    InputManager.Instance.OnSpacePressed += HandleSpacePressed;
}

void OnDestroy()
{
    // Unsubscribe
    if (InputManager.Instance != null)
    {
        InputManager.Instance.OnSpacePressed -= HandleSpacePressed;
    }
}

private void HandleSpacePressed()
{
    // Handle input via event
}
```

### ❌ Don't: Forget to Clean Up

```csharp
void Start()
{
    button.onClick.AddListener(OnClick);
    // Missing: RemoveListener in OnDestroy
}
```

### ✅ Do: Always Clean Up

```csharp
void Start()
{
    button.onClick.AddListener(OnClick);
}

void OnDestroy()
{
    if (button != null)
    {
        button.onClick.RemoveListener(OnClick);
    }
}
```

---

## 📚 Reference Documents

- **Unity Setup Guide:** `Unity-Scripts/UNITY-SETUP-GUIDE.md`
- **Game Architecture:** `GAME-ARCHITECTURE-COMPLETE.md`
- **Level Data Structure:** `Unity-Scripts/LevelData.cs`
- **Story Data Structure:** `Unity-Scripts/StoryData.cs`
- **Integration Guide:** `Unity-Scripts/INTEGRATION-WITH-EXISTING-GAME.md`

---

## 🎯 Key Takeaways

1. **Always validate inputs** - Check for null, empty, and invalid values
2. **Use proper Unity lifecycle** - Awake for setup, Start for initialization, OnDestroy for cleanup
3. **Document public APIs** - XML documentation for all public methods
4. **Follow naming conventions** - PascalCase classes, camelCase fields, _prefix for private
5. **Optimize performance** - Cache data, use object pooling, avoid Update() when possible
6. **Integrate with curriculum** - All game exercises must align with learning objectives
7. **Handle errors gracefully** - Use Debug.LogError with context, validate before use
8. **Clean up resources** - Remove event listeners, release references in OnDestroy

---

**Remember:** Game code is complete when it's implemented, tested, documented, validated, and performs well. No TODOs, no partial implementations, no moving on until the current task is 100% done.


