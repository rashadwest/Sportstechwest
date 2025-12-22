# BallCODE Gaming Quick Reference
## Quick Reference Guide for Unity Game Development

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 2025  
**Purpose:** Quick reference for common Unity/C# gaming tasks  
**Status:** Active Documentation

---

## 📚 Documentation Index

1. **`UNITY-GAMING-RULES.md`** - Complete Unity/C# coding standards and rules
2. **`GAMING-TECH-STACK.md`** - Technology stack and dependencies
3. **`GAMING-ARCHITECTURE-PATTERNS.md`** - System architecture and design patterns
4. **This Document** - Quick reference for common tasks

---

## 🎯 Common Code Patterns

### Singleton Manager

```csharp
public class MyManager : MonoBehaviour
{
    public static MyManager Instance { get; private set; }
    
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

### Load Level from JSON

```csharp
LevelData level = LevelDataManager.Instance.GetLevel("book1_foundation_block");
if (level != null)
{
    GameModeManager.Instance.LoadGameModeFromLevel(level.levelId);
}
```

### Handle Exercise Completion

```csharp
public void OnExerciseComplete(bool success, float score)
{
    // Validate score
    score = Mathf.Clamp(score, 0f, 100f);
    
    // Track metrics
    if (MetricsCollector.Instance != null)
    {
        MetricsCollector.Instance.OnExerciseComplete(episode, success, score, timeSpent);
    }
    
    // Return to story/book
    GameModeManager.Instance.OnExerciseComplete(success, score);
}
```

### URL Parameter Parsing (WebGL)

```csharp
#if UNITY_WEBGL && !UNITY_EDITOR
string url = Application.absoluteURL;
if (url.Contains("book="))
{
    // Parse book parameter
    int bookNumber = int.Parse(GetURLParameter("book"));
    string exercise = GetURLParameter("exercise");
    LoadBookExercise(bookNumber, exercise);
}
#endif
```

### Event Subscription Pattern

```csharp
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
    // Handle event
}
```

---

## 📋 Naming Conventions Quick Reference

| Type | Convention | Example |
|------|-----------|---------|
| Classes | PascalCase | `GameModeManager` |
| Script Files | Match class name | `GameModeManager.cs` |
| Public Fields | camelCase | `currentLevel` |
| Private Fields | _camelCase | `_currentEpisode` |
| Serialized Fields | camelCase + `[SerializeField]` | `[SerializeField] private int levelCount;` |
| Constants | UPPER_SNAKE_CASE | `MAX_LEVEL_COUNT` |
| Methods | PascalCase | `LoadGameMode()` |
| GameObjects | Descriptive | `StoryModeCanvas` |
| Scenes | PascalCase + "Scene" | `StoryModeScene.unity` |

---

## ✅ Code Checklist

Before submitting Unity/C# code:

- [ ] All public methods have XML documentation (`/// <summary>`)
- [ ] All inputs validated (null checks, range checks)
- [ ] Error handling with `Debug.LogError` and context
- [ ] Singleton pattern correct (if used)
- [ ] Event listeners cleaned up in `OnDestroy`/`OnDisable`
- [ ] No `FindObjectOfType` in `Update()` or frequent calls
- [ ] Serialized fields use `[SerializeField]` attribute
- [ ] Constants used instead of magic numbers
- [ ] Naming conventions followed
- [ ] Curriculum alignment validated (for game levels)

---

## 🚫 Common Mistakes to Avoid

### ❌ Don't:
- Use `Update()` for everything
- Forget to clean up event listeners
- Use `FindObjectOfType` in `Update()`
- Hardcode values (use constants)
- Skip null checks
- Forget error handling

### ✅ Do:
- Use events and coroutines
- Clean up in `OnDestroy`/`OnDisable`
- Cache frequently accessed objects
- Use constants for magic numbers
- Validate all inputs
- Handle errors gracefully

---

## 🔗 Integration Quick Reference

### Book → Game Integration

```csharp
// In BallCODEStarter.cs
void LoadBookExercise(int bookNumber, string exercise, string returnUrl)
{
    // Map to level ID
    string levelId = $"book{bookNumber}_{exercise.Replace("-", "_")}";
    
    // Store return info
    PlayerPrefs.SetInt("BookNumber", bookNumber);
    PlayerPrefs.SetString("BookReturnUrl", returnUrl);
    PlayerPrefs.Save();
    
    // Load exercise
    GameModeManager.Instance.LoadGameModeFromLevel(levelId);
}
```

### Return to Book (WebGL)

```csharp
#if UNITY_WEBGL && !UNITY_EDITOR
string returnUrl = PlayerPrefs.GetString("BookReturnUrl", "/books/book1");
Application.ExternalEval($"window.location.href = '{returnUrl}';");
#endif
```

---

## 📊 Data Structure Quick Reference

### LevelData Key Fields

```csharp
LevelData level = new LevelData
{
    levelId = "book1_foundation_block",
    levelName = "Foundation Block Challenge",
    gameMode = "blockcoding",
    episodeNumber = 1,
    codingConcept = "sequences",
    difficultyLevel = 1,
    learningObjectives = new[] { "Objective 1", "Objective 2" },
    successCriteria = new[] { "Criterion 1", "Criterion 2" }
};
```

### TrainingModeConfig

```csharp
TrainingModeConfig config = new TrainingModeConfig
{
    episode = 1,
    codingConcept = "state",
    monster = "Shadow Press Scouts",
    focus = "state_tracking"
};
```

---

## 🎮 Unity Lifecycle Methods

| Method | When to Use | Common Tasks |
|--------|-------------|--------------|
| `Awake()` | Before Start | Singleton setup, initialize references |
| `Start()` | After all objects created | Find objects, set up UI, start coroutines |
| `Update()` | Every frame | Input handling (avoid if possible) |
| `OnEnable()` | When object enabled | Subscribe to events |
| `OnDisable()` | When object disabled | Unsubscribe from events |
| `OnDestroy()` | When object destroyed | Final cleanup, release resources |

---

## 🔧 Performance Tips

1. **Cache frequently accessed objects:**
```csharp
private GameModeManager _gameModeManager;
void Start()
{
    _gameModeManager = GameModeManager.Instance; // Cache once
}
```

2. **Use object pooling for frequently created/destroyed objects:**
```csharp
private Queue<GameObject> _pool = new Queue<GameObject>();
```

3. **Avoid `Update()` when possible:**
```csharp
// Use events instead
void OnEnable()
{
    InputManager.OnSpacePressed += HandleSpace;
}
```

4. **Load assets asynchronously:**
```csharp
IEnumerator LoadLevelAsync(string levelId)
{
    yield return new WaitForSeconds(0.1f);
    LevelData level = GetLevel(levelId);
}
```

---

## 📖 Full Documentation

For complete details, see:
- **`UNITY-GAMING-RULES.md`** - Full coding standards
- **`GAMING-TECH-STACK.md`** - Complete tech stack
- **`GAMING-ARCHITECTURE-PATTERNS.md`** - Architecture details

---

**Quick Reference Updated:** December 2025


