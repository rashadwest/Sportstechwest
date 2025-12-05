using UnityEngine;
using System.Collections.Generic;
using System.IO;
using System.Linq;

/// <summary>
/// Manages loading and accessing level data from videos and strategies
/// This is the main system for adding new levels - just add videos and strategies!
/// </summary>
public class LevelDataManager : MonoBehaviour
{
    public static LevelDataManager Instance;
    
    [Header("Level Data Sources")]
    public TextAsset[] levelDataJSONFiles;      // JSON files containing level data
    public string streamingAssetsPath = "Levels";  // Path in StreamingAssets folder
    
    [Header("Level Organization")]
    public bool organizeByGameMode = true;      // Group levels by game mode
    public bool organizeByEpisode = true;       // Group levels by episode
    
    private Dictionary<string, LevelData> allLevels;           // All levels by ID
    private Dictionary<string, List<LevelData>> levelsByMode;  // Levels grouped by game mode
    private Dictionary<int, List<LevelData>> levelsByEpisode;   // Levels grouped by episode
    private Dictionary<string, List<LevelData>> levelsByConcept; // Levels grouped by coding concept
    
    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            LoadAllLevels();
        }
        else
        {
            Destroy(gameObject);
        }
    }
    
    /// <summary>
    /// Load all level data from JSON files and StreamingAssets
    /// </summary>
    public void LoadAllLevels()
    {
        allLevels = new Dictionary<string, LevelData>();
        levelsByMode = new Dictionary<string, List<LevelData>>();
        levelsByEpisode = new Dictionary<int, List<LevelData>>();
        levelsByConcept = new Dictionary<string, List<LevelData>>();
        
        // Load from TextAsset JSON files (Resources folder)
        if (levelDataJSONFiles != null)
        {
            foreach (TextAsset jsonFile in levelDataJSONFiles)
            {
                LoadLevelsFromJSON(jsonFile.text);
            }
        }
        
        // Load from StreamingAssets folder
        LoadLevelsFromStreamingAssets();
        
        // Organize levels
        OrganizeLevels();
        
        Debug.Log($"Loaded {allLevels.Count} levels total");
    }
    
    /// <summary>
    /// Load levels from JSON text
    /// </summary>
    void LoadLevelsFromJSON(string jsonText)
    {
        try
        {
            LevelDataCollection collection = JsonUtility.FromJson<LevelDataCollection>(jsonText);
            
            if (collection != null && collection.levels != null)
            {
                foreach (LevelData level in collection.levels)
                {
                    RegisterLevel(level);
                }
            }
        }
        catch (System.Exception e)
        {
            Debug.LogError($"Error loading levels from JSON: {e.Message}");
        }
    }
    
    /// <summary>
    /// Load levels from StreamingAssets folder
    /// </summary>
    void LoadLevelsFromStreamingAssets()
    {
        string path = Path.Combine(Application.streamingAssetsPath, streamingAssetsPath);
        
        if (!Directory.Exists(path))
        {
            Debug.LogWarning($"StreamingAssets path not found: {path}");
            return;
        }
        
        string[] jsonFiles = Directory.GetFiles(path, "*.json", SearchOption.AllDirectories);
        
        foreach (string jsonFile in jsonFiles)
        {
            try
            {
                string jsonText = File.ReadAllText(jsonFile);
                LoadLevelsFromJSON(jsonText);
            }
            catch (System.Exception e)
            {
                Debug.LogError($"Error loading level file {jsonFile}: {e.Message}");
            }
        }
    }
    
    /// <summary>
    /// Register a level in all dictionaries
    /// </summary>
    void RegisterLevel(LevelData level)
    {
        if (string.IsNullOrEmpty(level.levelId))
        {
            Debug.LogWarning("Level missing levelId, skipping...");
            return;
        }
        
        // Add to main dictionary
        if (allLevels.ContainsKey(level.levelId))
        {
            Debug.LogWarning($"Duplicate level ID: {level.levelId}, overwriting...");
        }
        allLevels[level.levelId] = level;
        
        // Add to mode dictionary
        if (!string.IsNullOrEmpty(level.gameMode))
        {
            if (!levelsByMode.ContainsKey(level.gameMode))
            {
                levelsByMode[level.gameMode] = new List<LevelData>();
            }
            levelsByMode[level.gameMode].Add(level);
        }
        
        // Add to episode dictionary
        if (!levelsByEpisode.ContainsKey(level.episodeNumber))
        {
            levelsByEpisode[level.episodeNumber] = new List<LevelData>();
        }
        levelsByEpisode[level.episodeNumber].Add(level);
        
        // Add to concept dictionary
        if (!string.IsNullOrEmpty(level.codingConcept))
        {
            if (!levelsByConcept.ContainsKey(level.codingConcept))
            {
                levelsByConcept[level.codingConcept] = new List<LevelData>();
            }
            levelsByConcept[level.codingConcept].Add(level);
        }
    }
    
    /// <summary>
    /// Organize levels by various criteria
    /// </summary>
    void OrganizeLevels()
    {
        // Sort levels within each group by difficulty
        foreach (var mode in levelsByMode.Keys.ToList())
        {
            levelsByMode[mode] = levelsByMode[mode]
                .OrderBy(l => l.difficultyLevel)
                .ThenBy(l => l.levelName)
                .ToList();
        }
        
        foreach (var episode in levelsByEpisode.Keys.ToList())
        {
            levelsByEpisode[episode] = levelsByEpisode[episode]
                .OrderBy(l => l.difficultyLevel)
                .ThenBy(l => l.levelName)
                .ToList();
        }
    }
    
    /// <summary>
    /// Get a level by ID
    /// </summary>
    public LevelData GetLevel(string levelId)
    {
        if (allLevels.ContainsKey(levelId))
        {
            return allLevels[levelId];
        }
        return null;
    }
    
    /// <summary>
    /// Get all levels for a specific game mode
    /// </summary>
    public List<LevelData> GetLevelsForMode(string gameMode)
    {
        if (levelsByMode.ContainsKey(gameMode))
        {
            return levelsByMode[gameMode].Where(l => l.isUnlocked).ToList();
        }
        return new List<LevelData>();
    }
    
    /// <summary>
    /// Get all levels for a specific episode
    /// </summary>
    public List<LevelData> GetLevelsForEpisode(int episodeNumber)
    {
        if (levelsByEpisode.ContainsKey(episodeNumber))
        {
            return levelsByEpisode[episodeNumber].Where(l => l.isUnlocked).ToList();
        }
        return new List<LevelData>();
    }
    
    /// <summary>
    /// Get all levels for a specific coding concept
    /// </summary>
    public List<LevelData> GetLevelsForConcept(string codingConcept)
    {
        if (levelsByConcept.ContainsKey(codingConcept))
        {
            return levelsByConcept[codingConcept].Where(l => l.isUnlocked).ToList();
        }
        return new List<LevelData>();
    }
    
    /// <summary>
    /// Get the next level after completing a level
    /// </summary>
    public LevelData GetNextLevel(string completedLevelId)
    {
        LevelData completedLevel = GetLevel(completedLevelId);
        if (completedLevel == null) return null;
        
        // Get all levels in the same mode and episode
        List<LevelData> availableLevels = GetLevelsForMode(completedLevel.gameMode)
            .Where(l => l.episodeNumber == completedLevel.episodeNumber)
            .ToList();
        
        // Find the next level by difficulty or order
        int currentIndex = availableLevels.FindIndex(l => l.levelId == completedLevelId);
        if (currentIndex >= 0 && currentIndex < availableLevels.Count - 1)
        {
            return availableLevels[currentIndex + 1];
        }
        
        return null;
    }
    
    /// <summary>
    /// Check if a level is unlocked (prerequisites met)
    /// </summary>
    public bool IsLevelUnlocked(string levelId, HashSet<string> completedLevels)
    {
        LevelData level = GetLevel(levelId);
        if (level == null) return false;
        if (!level.isUnlocked) return false;
        
        // Check prerequisites
        if (level.prerequisiteLevels != null && level.prerequisiteLevels.Length > 0)
        {
            foreach (string prereq in level.prerequisiteLevels)
            {
                if (!completedLevels.Contains(prereq))
                {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    /// <summary>
    /// Get all available levels (unlocked and prerequisites met)
    /// </summary>
    public List<LevelData> GetAvailableLevels(HashSet<string> completedLevels)
    {
        return allLevels.Values
            .Where(l => IsLevelUnlocked(l.levelId, completedLevels))
            .OrderBy(l => l.episodeNumber)
            .ThenBy(l => l.difficultyLevel)
            .ToList();
    }
    
    /// <summary>
    /// Reload all levels (useful for hot-reloading during development)
    /// </summary>
    public void ReloadLevels()
    {
        LoadAllLevels();
    }
}



