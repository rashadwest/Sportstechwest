using UnityEngine;
using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

/// <summary>
/// Metrics collection system for BallCODE Build-Measure-Learn feedback loop
/// Tracks story engagement, game performance, and story→game integration metrics
/// </summary>
public class MetricsCollector : MonoBehaviour
{
    public static MetricsCollector Instance;
    
    [Header("Metrics Configuration")]
    public bool enableMetrics = true;
    public bool saveToFile = true;
    public string metricsFileName = "ballcode_metrics.json";
    
    // Metrics data storage
    private MetricsData currentSession;
    private List<MetricsData> sessionHistory;
    
    // Story engagement metrics
    private Dictionary<int, StoryMetrics> storyMetrics; // Episode index → metrics
    private Dictionary<int, GameMetrics> gameMetrics;   // Episode index → metrics
    
    // Story→Game transition tracking
    private List<TransitionEvent> transitionEvents;
    
    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            InitializeMetrics();
        }
        else
        {
            Destroy(gameObject);
        }
    }
    
    void InitializeMetrics()
    {
        currentSession = new MetricsData
        {
            sessionId = System.Guid.NewGuid().ToString(),
            startTime = DateTime.Now,
            storyMetrics = new Dictionary<int, StoryMetrics>(),
            gameMetrics = new Dictionary<int, GameMetrics>(),
            transitionEvents = new List<TransitionEvent>()
        };
        
        storyMetrics = new Dictionary<int, StoryMetrics>();
        gameMetrics = new Dictionary<int, GameMetrics>();
        transitionEvents = new List<TransitionEvent>();
        sessionHistory = new List<MetricsData>();
    }
    
    // ============================================
    // STORY METRICS TRACKING
    // ============================================
    
    /// <summary>
    /// Track when a story page is viewed
    /// </summary>
    public void OnStoryPageView(int episodeIndex, int spreadIndex, float timeOnPage)
    {
        if (!enableMetrics) return;
        
        if (!storyMetrics.ContainsKey(episodeIndex))
        {
            storyMetrics[episodeIndex] = new StoryMetrics
            {
                episodeIndex = episodeIndex,
                pageViews = new List<PageViewEvent>()
            };
        }
        
        storyMetrics[episodeIndex].pageViews.Add(new PageViewEvent
        {
            spreadIndex = spreadIndex,
            timestamp = DateTime.Now,
            timeSpent = timeOnPage
        });
        
        // Update session data
        if (!currentSession.storyMetrics.ContainsKey(episodeIndex))
        {
            currentSession.storyMetrics[episodeIndex] = new StoryMetrics
            {
                episodeIndex = episodeIndex,
                pageViews = new List<PageViewEvent>()
            };
        }
        
        currentSession.storyMetrics[episodeIndex].pageViews.Add(new PageViewEvent
        {
            spreadIndex = spreadIndex,
            timestamp = DateTime.Now,
            timeSpent = timeOnPage
        });
        
        Debug.Log($"[Metrics] Story page viewed: Episode {episodeIndex + 1}, Spread {spreadIndex + 1}, Time: {timeOnPage}s");
    }
    
    /// <summary>
    /// Track when "Play Exercise" button is clicked
    /// </summary>
    public void OnPlayExerciseClick(int episodeIndex, int spreadIndex)
    {
        if (!enableMetrics) return;
        
        TransitionEvent transition = new TransitionEvent
        {
            eventType = "story_to_game",
            episodeIndex = episodeIndex,
            spreadIndex = spreadIndex,
            timestamp = DateTime.Now,
            success = true
        };
        
        transitionEvents.Add(transition);
        currentSession.transitionEvents.Add(transition);
        
        Debug.Log($"[Metrics] Play Exercise clicked: Episode {episodeIndex + 1}, Spread {spreadIndex + 1}");
    }
    
    /// <summary>
    /// Track when episode is completed
    /// </summary>
    public void OnEpisodeComplete(int episodeIndex, float totalTime, int totalPages)
    {
        if (!enableMetrics) return;
        
        if (!storyMetrics.ContainsKey(episodeIndex))
        {
            storyMetrics[episodeIndex] = new StoryMetrics
            {
                episodeIndex = episodeIndex,
                pageViews = new List<PageViewEvent>()
            };
        }
        
        storyMetrics[episodeIndex].episodeCompleted = true;
        storyMetrics[episodeIndex].completionTime = totalTime;
        storyMetrics[episodeIndex].totalPages = totalPages;
        storyMetrics[episodeIndex].completionTimestamp = DateTime.Now;
        
        // Update session data
        if (currentSession.storyMetrics.ContainsKey(episodeIndex))
        {
            currentSession.storyMetrics[episodeIndex].episodeCompleted = true;
            currentSession.storyMetrics[episodeIndex].completionTime = totalTime;
            currentSession.storyMetrics[episodeIndex].totalPages = totalPages;
            currentSession.storyMetrics[episodeIndex].completionTimestamp = DateTime.Now;
        }
        
        Debug.Log($"[Metrics] Episode {episodeIndex + 1} completed in {totalTime}s");
    }
    
    /// <summary>
    /// Track when player returns to story from game
    /// </summary>
    public void OnReturnToStory(int episodeIndex, bool exerciseCompleted, float exerciseScore)
    {
        if (!enableMetrics) return;
        
        TransitionEvent transition = new TransitionEvent
        {
            eventType = "game_to_story",
            episodeIndex = episodeIndex,
            timestamp = DateTime.Now,
            success = exerciseCompleted,
            score = exerciseScore
        };
        
        transitionEvents.Add(transition);
        currentSession.transitionEvents.Add(transition);
        
        Debug.Log($"[Metrics] Returned to story: Episode {episodeIndex + 1}, Exercise completed: {exerciseCompleted}, Score: {exerciseScore}");
    }
    
    // ============================================
    // GAME METRICS TRACKING
    // ============================================
    
    /// <summary>
    /// Track when game mode starts from story
    /// </summary>
    public void OnGameModeStart(int episodeIndex, string gameMode, string codingConcept)
    {
        if (!enableMetrics) return;
        
        if (!gameMetrics.ContainsKey(episodeIndex))
        {
            gameMetrics[episodeIndex] = new GameMetrics
            {
                episodeIndex = episodeIndex,
                gameMode = gameMode,
                codingConcept = codingConcept,
                exerciseAttempts = new List<ExerciseAttempt>()
            };
        }
        
        gameMetrics[episodeIndex].startTime = DateTime.Now;
        
        // Update session data
        if (!currentSession.gameMetrics.ContainsKey(episodeIndex))
        {
            currentSession.gameMetrics[episodeIndex] = new GameMetrics
            {
                episodeIndex = episodeIndex,
                gameMode = gameMode,
                codingConcept = codingConcept,
                exerciseAttempts = new List<ExerciseAttempt>()
            };
        }
        
        currentSession.gameMetrics[episodeIndex].startTime = DateTime.Now;
        
        Debug.Log($"[Metrics] Game mode started: Episode {episodeIndex + 1}, Mode: {gameMode}, Concept: {codingConcept}");
    }
    
    /// <summary>
    /// Track exercise attempt
    /// </summary>
    public void OnExerciseAttempt(int episodeIndex, int attemptNumber, float timeSpent)
    {
        if (!enableMetrics) return;
        
        if (!gameMetrics.ContainsKey(episodeIndex))
        {
            gameMetrics[episodeIndex] = new GameMetrics
            {
                episodeIndex = episodeIndex,
                exerciseAttempts = new List<ExerciseAttempt>()
            };
        }
        
        ExerciseAttempt attempt = new ExerciseAttempt
        {
            attemptNumber = attemptNumber,
            timestamp = DateTime.Now,
            timeSpent = timeSpent
        };
        
        gameMetrics[episodeIndex].exerciseAttempts.Add(attempt);
        
        // Update session data
        if (currentSession.gameMetrics.ContainsKey(episodeIndex))
        {
            currentSession.gameMetrics[episodeIndex].exerciseAttempts.Add(attempt);
        }
        
        Debug.Log($"[Metrics] Exercise attempt: Episode {episodeIndex + 1}, Attempt #{attemptNumber}, Time: {timeSpent}s");
    }
    
    /// <summary>
    /// Track exercise completion
    /// </summary>
    public void OnExerciseComplete(int episodeIndex, bool success, float score, int totalAttempts, float totalTime)
    {
        if (!enableMetrics) return;
        
        if (!gameMetrics.ContainsKey(episodeIndex))
        {
            gameMetrics[episodeIndex] = new GameMetrics
            {
                episodeIndex = episodeIndex,
                exerciseAttempts = new List<ExerciseAttempt>()
            };
        }
        
        gameMetrics[episodeIndex].exerciseCompleted = success;
        gameMetrics[episodeIndex].finalScore = score;
        gameMetrics[episodeIndex].totalAttempts = totalAttempts;
        gameMetrics[episodeIndex].totalTime = totalTime;
        gameMetrics[episodeIndex].completionTimestamp = DateTime.Now;
        
        // Update session data
        if (currentSession.gameMetrics.ContainsKey(episodeIndex))
        {
            currentSession.gameMetrics[episodeIndex].exerciseCompleted = success;
            currentSession.gameMetrics[episodeIndex].finalScore = score;
            currentSession.gameMetrics[episodeIndex].totalAttempts = totalAttempts;
            currentSession.gameMetrics[episodeIndex].totalTime = totalTime;
            currentSession.gameMetrics[episodeIndex].completionTimestamp = DateTime.Now;
        }
        
        Debug.Log($"[Metrics] Exercise completed: Episode {episodeIndex + 1}, Success: {success}, Score: {score}, Attempts: {totalAttempts}");
    }
    
    /// <summary>
    /// Track exercise failure
    /// </summary>
    public void OnExerciseFailed(int episodeIndex, string errorType, string errorMessage)
    {
        if (!enableMetrics) return;
        
        if (!gameMetrics.ContainsKey(episodeIndex))
        {
            gameMetrics[episodeIndex] = new GameMetrics
            {
                episodeIndex = episodeIndex,
                exerciseAttempts = new List<ExerciseAttempt>()
            };
        }
        
        gameMetrics[episodeIndex].failures++;
        gameMetrics[episodeIndex].lastError = errorMessage;
        gameMetrics[episodeIndex].lastErrorType = errorType;
        
        // Update session data
        if (currentSession.gameMetrics.ContainsKey(episodeIndex))
        {
            currentSession.gameMetrics[episodeIndex].failures++;
            currentSession.gameMetrics[episodeIndex].lastError = errorMessage;
            currentSession.gameMetrics[episodeIndex].lastErrorType = errorType;
        }
        
        Debug.Log($"[Metrics] Exercise failed: Episode {episodeIndex + 1}, Error: {errorType} - {errorMessage}");
    }
    
    // ============================================
    // DATA PERSISTENCE
    // ============================================
    
    /// <summary>
    /// Save metrics to file
    /// </summary>
    public void SaveMetrics()
    {
        if (!saveToFile || !enableMetrics) return;
        
        currentSession.endTime = DateTime.Now;
        currentSession.duration = (float)(currentSession.endTime - currentSession.startTime).TotalSeconds;
        
        string json = JsonUtility.ToJson(currentSession, true);
        string filePath = Path.Combine(Application.persistentDataPath, metricsFileName);
        
        try
        {
            File.WriteAllText(filePath, json);
            Debug.Log($"[Metrics] Saved to: {filePath}");
        }
        catch (Exception e)
        {
            Debug.LogError($"[Metrics] Failed to save: {e.Message}");
        }
    }
    
    /// <summary>
    /// Get metrics summary for analysis
    /// </summary>
    public MetricsSummary GetSummary()
    {
        MetricsSummary summary = new MetricsSummary
        {
            totalEpisodesViewed = storyMetrics.Count,
            totalExercisesAttempted = gameMetrics.Count,
            totalTransitions = transitionEvents.Count,
            storyCompletionRate = CalculateStoryCompletionRate(),
            exerciseSuccessRate = CalculateExerciseSuccessRate(),
            averageTimePerPage = CalculateAverageTimePerPage(),
            averageExerciseAttempts = CalculateAverageExerciseAttempts()
        };
        
        return summary;
    }
    
    // ============================================
    // HELPER METHODS
    // ============================================
    
    float CalculateStoryCompletionRate()
    {
        if (storyMetrics.Count == 0) return 0f;
        
        int completed = 0;
        foreach (var metrics in storyMetrics.Values)
        {
            if (metrics.episodeCompleted) completed++;
        }
        
        return (float)completed / storyMetrics.Count;
    }
    
    float CalculateExerciseSuccessRate()
    {
        if (gameMetrics.Count == 0) return 0f;
        
        int successful = 0;
        foreach (var metrics in gameMetrics.Values)
        {
            if (metrics.exerciseCompleted) successful++;
        }
        
        return (float)successful / gameMetrics.Count;
    }
    
    float CalculateAverageTimePerPage()
    {
        float totalTime = 0f;
        int totalPages = 0;
        
        foreach (var metrics in storyMetrics.Values)
        {
            foreach (var pageView in metrics.pageViews)
            {
                totalTime += pageView.timeSpent;
                totalPages++;
            }
        }
        
        return totalPages > 0 ? totalTime / totalPages : 0f;
    }
    
    float CalculateAverageExerciseAttempts()
    {
        if (gameMetrics.Count == 0) return 0f;
        
        int totalAttempts = 0;
        foreach (var metrics in gameMetrics.Values)
        {
            totalAttempts += metrics.totalAttempts;
        }
        
        return (float)totalAttempts / gameMetrics.Count;
    }
    
    void OnApplicationQuit()
    {
        SaveMetrics();
    }
    
    void OnApplicationPause(bool pauseStatus)
    {
        if (pauseStatus)
        {
            SaveMetrics();
        }
    }
}

// ============================================
// DATA STRUCTURES
// ============================================

[System.Serializable]
public class MetricsData
{
    public string sessionId;
    public DateTime startTime;
    public DateTime endTime;
    public float duration;
    public Dictionary<int, StoryMetrics> storyMetrics;
    public Dictionary<int, GameMetrics> gameMetrics;
    public List<TransitionEvent> transitionEvents;
}

[System.Serializable]
public class StoryMetrics
{
    public int episodeIndex;
    public List<PageViewEvent> pageViews;
    public bool episodeCompleted;
    public float completionTime;
    public int totalPages;
    public DateTime completionTimestamp;
}

[System.Serializable]
public class PageViewEvent
{
    public int spreadIndex;
    public DateTime timestamp;
    public float timeSpent;
}

[System.Serializable]
public class GameMetrics
{
    public int episodeIndex;
    public string gameMode;
    public string codingConcept;
    public DateTime startTime;
    public DateTime completionTimestamp;
    public List<ExerciseAttempt> exerciseAttempts;
    public bool exerciseCompleted;
    public float finalScore;
    public int totalAttempts;
    public float totalTime;
    public int failures;
    public string lastError;
    public string lastErrorType;
}

[System.Serializable]
public class ExerciseAttempt
{
    public int attemptNumber;
    public DateTime timestamp;
    public float timeSpent;
}

[System.Serializable]
public class TransitionEvent
{
    public string eventType; // "story_to_game" or "game_to_story"
    public int episodeIndex;
    public int spreadIndex;
    public DateTime timestamp;
    public bool success;
    public float score;
}

[System.Serializable]
public class MetricsSummary
{
    public int totalEpisodesViewed;
    public int totalExercisesAttempted;
    public int totalTransitions;
    public float storyCompletionRate;
    public float exerciseSuccessRate;
    public float averageTimePerPage;
    public float averageExerciseAttempts;
}



