using UnityEngine;
using UnityEngine.SceneManagement;

/// <summary>
/// Main entry point for BallCODE Story Mode
/// Handles initialization and scene setup
/// Place this on a GameObject in your main scene
/// </summary>
public class BallCODEStarter : MonoBehaviour
{
    [Header("Scene References")]
    [Tooltip("The scene name for Story Mode (create this scene separately)")]
    public string storyModeSceneName = "StoryModeScene";
    
    [Tooltip("The scene name for your main game")]
    public string mainGameSceneName = "MainGameScene";
    
    [Header("Auto-Start Options")]
    [Tooltip("Automatically enter story mode on start (for testing)")]
    public bool autoStartStoryMode = false;
    
    [Tooltip("Episode to start with (0-indexed, so 0 = Episode 1)")]
    public int startEpisode = 0;
    
    [Header("Component References")]
    [Tooltip("Story Mode Manager (will be found automatically if null)")]
    public StoryModeManager storyModeManager;
    
    [Tooltip("Game Mode Manager (will be found automatically if null)")]
    public GameModeManager gameModeManager;
    
    private void Awake()
    {
        // Find managers if not assigned
        if (storyModeManager == null)
        {
            storyModeManager = FindObjectOfType<StoryModeManager>();
        }
        
        if (gameModeManager == null)
        {
            gameModeManager = FindObjectOfType<GameModeManager>();
        }
        
        // Ensure GameModeManager is set up as singleton
        if (gameModeManager == null)
        {
            GameObject gameModeObj = new GameObject("GameModeManager");
            gameModeManager = gameModeObj.AddComponent<GameModeManager>();
        }
    }
    
    private void Start()
    {
        // Connect StoryModeManager to GameModeManager
        if (storyModeManager != null && gameModeManager != null)
        {
            storyModeManager.gameModeManager = gameModeManager;
        }
        
        // Auto-start story mode if enabled (for testing)
        if (autoStartStoryMode && storyModeManager != null)
        {
            storyModeManager.EnterStoryMode(startEpisode);
        }
        
        // Check for URL parameters (WebGL builds)
        CheckURLParameters();
    }
    
    /// <summary>
    /// Check URL parameters for story mode deep linking and book exercises
    /// Used for QR code integration from physical book and website book integration
    /// </summary>
    void CheckURLParameters()
    {
        #if UNITY_WEBGL && !UNITY_EDITOR
        string url = Application.absoluteURL;
        
        // Check for book parameter (book integration)
        if (GetURLParameter("book", out string bookStr))
        {
            if (int.TryParse(bookStr, out int bookNumber))
            {
                string exercise = GetURLParameter("exercise", out string exerciseStr) ? exerciseStr : "";
                string source = GetURLParameter("source", out string sourceStr) ? sourceStr : "direct";
                string returnUrl = GetURLParameter("return", out string returnUrlStr) ? returnUrlStr : "";
                
                LoadBookExercise(bookNumber, exercise, source, returnUrl);
                return; // Don't check for story/episode if book parameter is present
            }
        }
        
        // Check for story parameter (existing story mode)
        if (url.Contains("story"))
        {
            if (GetURLParameter("episode", out string episodeStr))
            {
                int episode = int.Parse(episodeStr) - 1; // Convert to 0-indexed
                if (storyModeManager != null)
                {
                    storyModeManager.EnterStoryMode(episode);
                }
            }
        }
        #endif
    }
    
    /// <summary>
    /// Load book exercise based on book number and exercise identifier
    /// Protected by feature flag for reversible MVP push
    /// </summary>
    void LoadBookExercise(int bookNumber, string exercise, string source, string returnUrl)
    {
        // Feature flag check - can be disabled instantly for rollback
        if (bookNumber == 1 && !FeatureFlags.Book1MVPEnabled)
        {
            Debug.LogWarning("[BallCODEStarter] Book 1 MVP is disabled via feature flag. Exercise not loaded.");
            // Optionally show message to user or redirect
            return;
        }
        
        // Validate book number
        if (bookNumber < 1 || bookNumber > 3)
        {
            Debug.LogError($"Invalid book number: {bookNumber}. Must be 1, 2, or 3.");
            return;
        }
        
        // Map book to level ID
        string levelId = GetBookLevelId(bookNumber, exercise);
        
        if (string.IsNullOrEmpty(levelId))
        {
            Debug.LogError($"Could not determine level ID for book {bookNumber}, exercise '{exercise}'");
            return;
        }
        
        // Store return information for later use
        PlayerPrefs.SetString("BookReturnUrl", returnUrl);
        PlayerPrefs.SetInt("BookNumber", bookNumber);
        PlayerPrefs.SetString("ExerciseSource", source);
        PlayerPrefs.SetString("ExerciseLevelId", levelId);
        PlayerPrefs.Save();
        
        Debug.Log($"[BallCODEStarter] Loading book exercise: Book {bookNumber}, Exercise '{exercise}', Level ID '{levelId}'");
        
        // Load exercise via GameModeManager
        if (gameModeManager != null)
        {
            gameModeManager.LoadGameModeFromLevel(levelId);
        }
        else
        {
            Debug.LogError("GameModeManager not found! Cannot load book exercise.");
        }
    }
    
    /// <summary>
    /// Map book number and exercise identifier to level ID
    /// </summary>
    string GetBookLevelId(int bookNumber, string exercise)
    {
        // Default exercise identifiers if not provided
        if (string.IsNullOrEmpty(exercise))
        {
            exercise = bookNumber switch
            {
                1 => "foundation-block",
                2 => "decision-crossover",
                3 => "pattern-loop",
                _ => ""
            };
        }
        
        // Map book number and exercise to level ID
        string levelId = bookNumber switch
        {
            1 => "book1_foundation_block",
            2 => "book2_decision_crossover",
            3 => "book3_pattern_loop",
            _ => ""
        };
        
        // If exercise identifier provided and doesn't match default, use it
        if (!string.IsNullOrEmpty(exercise) && !string.IsNullOrEmpty(levelId))
        {
            // Level ID format: book{N}_{exercise-name}
            // Replace spaces/hyphens with underscores
            string exerciseId = exercise.Replace(" ", "_").Replace("-", "_");
            levelId = $"book{bookNumber}_{exerciseId}";
        }
        
        return levelId;
    }
    
    bool GetURLParameter(string paramName, out string value)
    {
        value = "";
        #if UNITY_WEBGL && !UNITY_EDITOR
        string url = Application.absoluteURL;
        if (string.IsNullOrEmpty(url)) return false;
        
        int startIndex = url.IndexOf(paramName + "=");
        if (startIndex == -1) return false;
        
        startIndex += paramName.Length + 1;
        int endIndex = url.IndexOf("&", startIndex);
        if (endIndex == -1) endIndex = url.Length;
        
        value = url.Substring(startIndex, endIndex - startIndex);
        return true;
        #else
        return false;
        #endif
    }
    
    /// <summary>
    /// Public method to enter story mode (can be called from UI buttons)
    /// </summary>
    public void EnterStoryMode(int episodeIndex = 0)
    {
        if (storyModeManager != null)
        {
            storyModeManager.EnterStoryMode(episodeIndex);
        }
        else
        {
            Debug.LogError("StoryModeManager not found! Make sure it's in the scene.");
        }
    }
    
    /// <summary>
    /// Public method to exit story mode
    /// </summary>
    public void ExitStoryMode()
    {
        if (storyModeManager != null)
        {
            storyModeManager.ExitStoryMode();
        }
    }
    
    /// <summary>
    /// Load a specific game mode (for testing or direct access)
    /// </summary>
    public void LoadGameMode(string mode, int episode, string codingConcept, string monster)
    {
        if (gameModeManager != null)
        {
            gameModeManager.LoadGameMode(mode, episode, codingConcept, monster);
        }
        else
        {
            Debug.LogError("GameModeManager not found! Make sure it's in the scene.");
        }
    }
}

