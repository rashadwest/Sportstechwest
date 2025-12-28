using UnityEngine;

/// <summary>
/// Manages transitions between Story Mode and Game Modes
/// Handles parameter passing and exercise configuration
/// </summary>
public class GameModeManager : MonoBehaviour 
{
    public static GameModeManager Instance;
    
    [Header("Game Mode Scenes/Managers")]
    public TrainingModeManager trainingMode;
    public PredictionModeManager predictionMode;
    public MathModeManager mathMode;
    public BlockCodingManager blockCodingMode;
    public PythonCodingManager pythonCodingMode;
    
    [Header("Metrics Collection")]
    public MetricsCollector metricsCollector;
    
    private string currentGameMode;
    private int currentEpisode;
    private float gameModeStartTime;
    private int exerciseAttemptCount;
    
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
    
    /// <summary>
    /// Load a game mode with story episode context
    /// </summary>
    public void LoadGameMode(string mode, int episode, string codingConcept, string monster)
    {
        currentGameMode = mode;
        currentEpisode = episode;
        gameModeStartTime = Time.time;
        exerciseAttemptCount = 0;
        
        // Track game mode start
        if (metricsCollector != null)
        {
            metricsCollector.OnGameModeStart(episode - 1, mode, codingConcept); // Convert to 0-indexed
        }
        
        // Configure game mode based on story context
        switch (mode.ToLower())
        {
            case "training":
                LoadTrainingMode(episode, codingConcept, monster);
                break;
            case "prediction":
                LoadPredictionMode(episode, codingConcept, monster);
                break;
            case "math":
                LoadMathMode(episode, codingConcept, monster);
                break;
            case "blockcoding":
                LoadBlockCodingMode(episode, codingConcept, monster);
                break;
            case "python":
            case "pythoncoding":
                LoadPythonCodingMode(episode, codingConcept, monster);
                break;
            default:
                Debug.LogWarning($"Unknown game mode: {mode}");
                break;
        }
    }
    
    /// <summary>
    /// Load a game mode using level data (new video/strategy-based system)
    /// </summary>
    public void LoadGameModeFromLevel(string levelId)
    {
        if (LevelDataManager.Instance == null)
        {
            Debug.LogError("LevelDataManager not found! Make sure it's in the scene.");
            return;
        }
        
        LevelData level = LevelDataManager.Instance.GetLevel(levelId);
        if (level == null)
        {
            Debug.LogError($"Level not found: {levelId}");
            return;
        }
        
        currentGameMode = level.gameMode;
        currentEpisode = level.episodeNumber;
        
        // Load game mode with level data
        switch (level.gameMode.ToLower())
        {
            case "training":
                LoadTrainingModeFromLevel(level);
                break;
            case "prediction":
                LoadPredictionModeFromLevel(level);
                break;
            case "math":
                LoadMathModeFromLevel(level);
                break;
            case "blockcoding":
                LoadBlockCodingModeFromLevel(level);
                break;
            case "python":
            case "pythoncoding":
                LoadPythonCodingModeFromLevel(level);
                break;
            case "freeplay":
                LoadFreeplayModeFromLevel(level);
                break;
            default:
                Debug.LogWarning($"Unknown game mode: {level.gameMode}");
                break;
        }
    }
    
    /// <summary>
    /// Load training mode from level data
    /// </summary>
    void LoadTrainingModeFromLevel(LevelData level)
    {
        if (trainingMode == null)
        {
            Debug.LogError("TrainingModeManager not assigned!");
            return;
        }
        
        TrainingModeConfig config = new TrainingModeConfig
        {
            episode = level.episodeNumber,
            codingConcept = level.codingConcept,
            monster = "Level Challenge", // Can be customized per level
            focus = GetTrainingFocus(level.episodeNumber)
        };
        
        // Pass level data to training mode (if it supports it)
        // You'll need to extend TrainingModeManager to accept LevelData
        trainingMode.StartTraining(config);
    }
    
    /// <summary>
    /// Load prediction mode from level data
    /// </summary>
    void LoadPredictionModeFromLevel(LevelData level)
    {
        if (predictionMode == null)
        {
            Debug.LogError("PredictionModeManager not assigned!");
            return;
        }
        
        PredictionModeConfig config = new PredictionModeConfig
        {
            episode = level.episodeNumber,
            codingConcept = level.codingConcept,
            monster = "Level Challenge",
            difficulty = GetDifficultyString(level.difficultyLevel)
        };
        
        predictionMode.StartPrediction(config);
    }
    
    /// <summary>
    /// Load math mode from level data
    /// </summary>
    void LoadMathModeFromLevel(LevelData level)
    {
        if (mathMode == null)
        {
            Debug.LogError("MathModeManager not assigned!");
            return;
        }
        
        MathModeConfig config = new MathModeConfig
        {
            episode = level.episodeNumber,
            codingConcept = level.codingConcept,
            monster = "Level Challenge",
            focus = "dribbles"
        };
        
        mathMode.StartMathMode(config);
    }
    
    /// <summary>
    /// Load block coding mode from level data
    /// Passes full level data to BlockCodingManager for Books 1, 2, 3
    /// </summary>
    void LoadBlockCodingModeFromLevel(LevelData level)
    {
        if (blockCodingMode == null)
        {
            Debug.LogError("BlockCodingManager not assigned!");
            return;
        }
        
        // Pass full level data to BlockCodingManager (preferred method)
        // BlockCodingManager can access all level data: availableBlocks, targetCode, etc.
        if (blockCodingMode is BlockCodingManager blockManager)
        {
            blockManager.StartBlockCodingFromLevel(level);
        }
        else
        {
            // Fallback: Use config method (legacy support)
            BlockCodingConfig config = new BlockCodingConfig
            {
                episode = level.episodeNumber,
                codingConcept = level.codingConcept,
                monster = "Level Challenge"
            };
            
            blockCodingMode.StartBlockCoding(config);
        }
    }
    
    /// <summary>
    /// Load freeplay mode from level data
    /// </summary>
    void LoadFreeplayModeFromLevel(LevelData level)
    {
        // Freeplay mode - open exploration
        Debug.Log($"Loading freeplay level: {level.levelName}");
        // Implement freeplay mode loading here
    }
    
    /// <summary>
    /// Convert difficulty level to string
    /// </summary>
    string GetDifficultyString(int difficultyLevel)
    {
        return difficultyLevel switch
        {
            1 => "beginner",
            2 => "easy",
            3 => "medium",
            4 => "hard",
            5 => "expert",
            _ => "medium"
        };
    }
    
    void LoadTrainingMode(int episode, string concept, string monster)
    {
        if (trainingMode == null)
        {
            Debug.LogError("TrainingModeManager not assigned!");
            return;
        }
        
        // Configure training mode based on episode
        TrainingModeConfig config = new TrainingModeConfig
        {
            episode = episode,
            codingConcept = concept,
            monster = monster,
            focus = GetTrainingFocus(episode)
        };
        
        trainingMode.StartTraining(config);
    }
    
    void LoadPredictionMode(int episode, string concept, string monster)
    {
        if (predictionMode == null)
        {
            Debug.LogError("PredictionModeManager not assigned!");
            return;
        }
        
        PredictionModeConfig config = new PredictionModeConfig
        {
            episode = episode,
            codingConcept = concept,
            monster = monster,
            difficulty = "beginner"
        };
        
        predictionMode.StartPrediction(config);
    }
    
    void LoadMathMode(int episode, string concept, string monster)
    {
        if (mathMode == null)
        {
            Debug.LogError("MathModeManager not assigned!");
            return;
        }
        
        MathModeConfig config = new MathModeConfig
        {
            episode = episode,
            codingConcept = concept,
            monster = monster,
            focus = "dribbles"
        };
        
        mathMode.StartMathMode(config);
    }
    
    void LoadBlockCodingMode(int episode, string concept, string monster)
    {
        if (blockCodingMode == null)
        {
            Debug.LogError("BlockCodingManager not assigned!");
            return;
        }
        
        BlockCodingConfig config = new BlockCodingConfig
        {
            episode = episode,
            codingConcept = concept,
            monster = monster
        };
        
        blockCodingMode.StartBlockCoding(config);
    }
    
    /// <summary>
    /// Load Python coding mode from level data
    /// </summary>
    void LoadPythonCodingModeFromLevel(LevelData level)
    {
        if (pythonCodingMode == null)
        {
            Debug.LogError("PythonCodingManager not assigned!");
            return;
        }
        
        // Convert LevelData to PythonExerciseData
        PythonExerciseData exercise = new PythonExerciseData
        {
            exerciseId = level.levelId,
            title = level.levelName,
            description = level.description,
            storyContext = level.storyContext,
            codingConcept = level.codingConcept,
            difficultyLevel = level.difficultyLevel
        };
        
        pythonCodingMode.LoadExercise(exercise);
    }
    
    void LoadPythonCodingMode(int episode, string concept, string monster)
    {
        if (pythonCodingMode == null)
        {
            Debug.LogError("PythonCodingManager not assigned!");
            return;
        }
        
        // Create Python exercise from episode context
        PythonExerciseData exercise = new PythonExerciseData
        {
            exerciseId = $"python_episode_{episode}",
            title = $"Python Exercise - Episode {episode}",
            description = $"Practice Python coding with {concept}",
            storyContext = $"From Episode {episode}: {monster}",
            codingConcept = concept,
            difficultyLevel = episode
        };
        
        pythonCodingMode.LoadExercise(exercise);
    }
    
    string GetTrainingFocus(int episode)
    {
        return episode switch
        {
            1 => "state_tracking",      // Episode 1: State & Flow
            2 => "position_analysis",    // Episode 2: Conditionals
            3 => "pattern_recognition",  // Episode 3: Loops
            _ => "general"
        };
    }
    
    /// <summary>
    /// Track exercise attempt (call this when player makes an attempt)
    /// </summary>
    public void OnExerciseAttempt(float timeSpent)
    {
        exerciseAttemptCount++;
        if (metricsCollector != null)
        {
            metricsCollector.OnExerciseAttempt(currentEpisode - 1, exerciseAttemptCount, timeSpent); // Convert to 0-indexed
        }
    }
    
    /// <summary>
    /// Track exercise failure (call this when exercise fails)
    /// </summary>
    public void OnExerciseFailed(string errorType, string errorMessage)
    {
        if (metricsCollector != null)
        {
            metricsCollector.OnExerciseFailed(currentEpisode - 1, errorType, errorMessage); // Convert to 0-indexed
        }
    }
    
    /// <summary>
    /// Called when exercise is completed
    /// Returns to story mode or book page (if from book)
    /// </summary>
    public void OnExerciseComplete(bool success, float score)
    {
        // Track exercise completion
        if (metricsCollector != null)
        {
            float totalTime = Time.time - gameModeStartTime;
            metricsCollector.OnExerciseComplete(
                currentEpisode - 1, // Convert to 0-indexed
                success,
                score,
                exerciseAttemptCount,
                totalTime
            );
        }
        
        // Check if this exercise came from a book
        int bookNumber = PlayerPrefs.GetInt("BookNumber", 0);
        if (bookNumber > 0)
        {
            // Return to book page
            ReturnToBook(bookNumber, success, score);
        }
        else
        {
            // Return to story mode (existing behavior)
            StoryModeManager storyMode = FindObjectOfType<StoryModeManager>();
            if (storyMode != null)
            {
                storyMode.OnExerciseComplete(success, score);
            }
        }
    }
    
    /// <summary>
    /// Return to book page after exercise completion
    /// Uses JavaScript communication for WebGL builds
    /// </summary>
    void ReturnToBook(int bookNumber, bool success, float score)
    {
        string returnUrl = PlayerPrefs.GetString("BookReturnUrl", $"/books/book{bookNumber}");
        
        Debug.Log($"[GameModeManager] Exercise complete for Book {bookNumber}. Success: {success}, Score: {score}. Returning to: {returnUrl}");
        
        #if UNITY_WEBGL && !UNITY_EDITOR
        // Use JavaScript communication
        BookReturnHandler returnHandler = FindObjectOfType<BookReturnHandler>();
        if (returnHandler != null)
        {
            returnHandler.OnExerciseComplete(bookNumber, success, score);
        }
        else
        {
            // Fallback: URL redirect
            string redirectUrl = $"{returnUrl}?exercise=complete&success={(success ? 1 : 0)}&score={score}";
            Application.ExternalEval($"window.location.href = '{redirectUrl}';");
        }
        #else
        // Editor/Standalone: Just log
        Debug.Log($"[GameModeManager] Would return to book {bookNumber} with success={success}, score={score}");
        #endif
        
        // Clear book-related PlayerPrefs
        PlayerPrefs.DeleteKey("BookNumber");
        PlayerPrefs.DeleteKey("BookReturnUrl");
        PlayerPrefs.DeleteKey("ExerciseSource");
        PlayerPrefs.DeleteKey("ExerciseLevelId");
        PlayerPrefs.Save();
    }
}

// Configuration classes for each game mode
[System.Serializable]
public class TrainingModeConfig
{
    public int episode;
    public string codingConcept;
    public string monster;
    public string focus;
}

[System.Serializable]
public class PredictionModeConfig
{
    public int episode;
    public string codingConcept;
    public string monster;
    public string difficulty;
}

[System.Serializable]
public class MathModeConfig
{
    public int episode;
    public string codingConcept;
    public string monster;
    public string focus;
}

[System.Serializable]
public class BlockCodingConfig
{
    public int episode;
    public string codingConcept;
    public string monster;
}

[System.Serializable]
public class PythonCodingConfig
{
    public int episode;
    public string codingConcept;
    public string monster;
}


