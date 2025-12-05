using UnityEngine;
using System.Collections.Generic;
using System.IO;

/// <summary>
/// AIMCODE-based automation system for generating level configurations
/// This allows you to create levels by simply providing videos and strategies
/// The system automatically generates Unity-compatible level data
/// </summary>
public class AIMCODELevelGenerator : MonoBehaviour
{
    [Header("AIMCODE Configuration")]
    public bool autoGenerateOnStart = false;
    public string outputPath = "Assets/StreamingAssets/Levels";
    
    /// <summary>
    /// Generate a level from video and strategy inputs
    /// This is the main method you'll use to create new levels
    /// </summary>
    public static LevelData GenerateLevelFromInputs(
        string levelName,
        string videoPath,
        StrategyData strategy,
        string gameMode,
        int episodeNumber,
        string codingConcept,
        ExerciseType exerciseType = ExerciseType.Analysis
    )
    {
        // AIMCODE Principle: Zhang - Start with basketball framework
        // The strategy provides the basketball context
        LevelData level = new LevelData
        {
            levelId = GenerateLevelId(gameMode, episodeNumber, codingConcept),
            levelName = levelName,
            description = GenerateDescription(strategy, codingConcept),
            gameMode = gameMode,
            episodeNumber = episodeNumber,
            codingConcept = codingConcept,
            videoPath = videoPath,
            strategy = strategy,
            exercise = GenerateExerciseConfig(exerciseType, strategy, codingConcept),
            learningObjectives = GenerateLearningObjectives(codingConcept, strategy),
            successCriteria = GenerateSuccessCriteria(codingConcept),
            difficultyLevel = CalculateDifficulty(episodeNumber, strategy),
            isUnlocked = true,
            tags = GenerateTags(gameMode, codingConcept, strategy),
            author = "AIMCODE Generator",
            createdDate = System.DateTime.Now.ToString("yyyy-MM-dd")
        };
        
        // AIMCODE Principle: Hassabis - Build systematically
        // Set prerequisites based on episode progression
        if (episodeNumber > 0)
        {
            level.prerequisiteLevels = GeneratePrerequisites(gameMode, episodeNumber - 1);
        }
        
        // AIMCODE Principle: Resnick - Include building activities
        // Configure exercise for hands-on learning
        ConfigureBuildingActivity(level, exerciseType);
        
        // AIMCODE Principle: Reggio - Multiple entry points
        // Ensure level supports different learning styles
        ConfigureMultipleEntryPoints(level);
        
        // AIMCODE Principle: Jobs - Keep it simple
        // Validate and simplify the configuration
        ValidateAndSimplify(level);
        
        return level;
    }
    
    /// <summary>
    /// Generate level ID from components
    /// </summary>
    static string GenerateLevelId(string gameMode, int episode, string concept)
    {
        return $"{gameMode}_{concept}_ep{episode}_{System.Guid.NewGuid().ToString().Substring(0, 8)}";
    }
    
    /// <summary>
    /// Generate description from strategy and concept
    /// </summary>
    static string GenerateDescription(StrategyData strategy, string concept)
    {
        if (strategy != null)
        {
            return $"Learn {concept} through analyzing the {strategy.strategyName} strategy. " +
                   $"{strategy.description}";
        }
        return $"Learn {concept} through interactive basketball analysis.";
    }
    
    /// <summary>
    /// Generate learning objectives based on concept and strategy
    /// </summary>
    static string[] GenerateLearningObjectives(string concept, StrategyData strategy)
    {
        List<string> objectives = new List<string>();
        
        // Concept-based objectives
        objectives.Add($"Understand {concept} in basketball context");
        objectives.Add($"Apply {concept} to analyze game situations");
        
        // Strategy-based objectives
        if (strategy != null)
        {
            objectives.Add($"Identify the {strategy.strategyName} strategy");
            objectives.Add($"Analyze how {concept} applies to {strategy.strategyName}");
        }
        
        // Building objectives (Resnick)
        objectives.Add("Build code blocks to represent basketball actions");
        objectives.Add("Create solutions through hands-on practice");
        
        return objectives.ToArray();
    }
    
    /// <summary>
    /// Generate success criteria
    /// </summary>
    static string[] GenerateSuccessCriteria(string concept)
    {
        return new string[]
        {
            $"Correctly identify {concept} in basketball scenarios",
            "Complete exercise with 70% or higher score",
            "Build code blocks that represent basketball actions",
            "Demonstrate understanding through interactive practice"
        };
    }
    
    /// <summary>
    /// Calculate difficulty based on episode and strategy complexity
    /// </summary>
    static int CalculateDifficulty(int episodeNumber, StrategyData strategy)
    {
        int difficulty = Mathf.Clamp(episodeNumber + 1, 1, 5);
        
        // Adjust based on strategy complexity
        if (strategy != null && strategy.steps != null)
        {
            if (strategy.steps.Count > 5)
            {
                difficulty = Mathf.Min(difficulty + 1, 5);
            }
        }
        
        return difficulty;
    }
    
    /// <summary>
    /// Generate prerequisites based on episode progression
    /// </summary>
    static string[] GeneratePrerequisites(string gameMode, int previousEpisode)
    {
        // Generate prerequisite level IDs
        List<string> prereqs = new List<string>();
        
        // Add prerequisite from previous episode
        string prereqId = $"{gameMode}_ep{previousEpisode}_*";
        prereqs.Add(prereqId);
        
        return prereqs.ToArray();
    }
    
    /// <summary>
    /// Generate tags for searchability
    /// </summary>
    static string[] GenerateTags(string gameMode, string concept, StrategyData strategy)
    {
        List<string> tags = new List<string> { gameMode, concept };
        
        if (strategy != null)
        {
            tags.Add(strategy.strategyType);
            tags.Add(strategy.strategyName.ToLower().Replace(" ", "_"));
        }
        
        return tags.ToArray();
    }
    
    /// <summary>
    /// Generate exercise configuration
    /// </summary>
    static ExerciseConfig GenerateExerciseConfig(ExerciseType type, StrategyData strategy, string concept)
    {
        ExerciseConfig config = new ExerciseConfig
        {
            exerciseType = type,
            scoring = new ScoringConfig
            {
                maxScore = 100,
                passingScore = 70,
                showScoreDuringExercise = false,
                allowRetry = true,
                maxAttempts = 3
            }
        };
        
        // Configure based on exercise type
        switch (type)
        {
            case ExerciseType.BlockCoding:
                config.blockCoding = new BlockCodingExercise
                {
                    availableBlocks = GetAvailableBlocksForConcept(concept),
                    requiredBlocks = GetRequiredBlocksForConcept(concept),
                    allowCustomBlocks = false
                };
                break;
                
            case ExerciseType.Analysis:
                config.analysis = new AnalysisExercise
                {
                    numberOfQuestions = 5,
                    showVideoDuringQuestions = true,
                    timeLimit = -1f
                };
                break;
                
            case ExerciseType.Prediction:
                config.prediction = new PredictionExercise
                {
                    numberOfPredictions = 3,
                    predictionWindow = 5f,
                    showFeedback = true
                };
                break;
                
            case ExerciseType.Math:
                config.math = new MathExercise
                {
                    mathConcept = concept,
                    numberOfProblems = 3,
                    showVisualAids = true
                };
                break;
        }
        
        return config;
    }
    
    /// <summary>
    /// Configure building activity (Resnick principle)
    /// </summary>
    static void ConfigureBuildingActivity(LevelData level, ExerciseType type)
    {
        // Ensure block coding is available for building activities
        if (type != ExerciseType.BlockCoding && level.exercise != null)
        {
            // Add block coding as an alternative entry point
            level.exercise.blockCoding = new BlockCodingExercise
            {
                availableBlocks = GetAvailableBlocksForConcept(level.codingConcept),
                allowCustomBlocks = true
            };
        }
    }
    
    /// <summary>
    /// Configure multiple entry points (Reggio principle)
    /// </summary>
    static void ConfigureMultipleEntryPoints(LevelData level)
    {
        // Ensure video is available for visual learners
        if (string.IsNullOrEmpty(level.videoPath))
        {
            Debug.LogWarning($"Level {level.levelId} missing video path - visual entry point unavailable");
        }
        
        // Ensure strategy is available for analytical learners
        if (level.strategy == null)
        {
            Debug.LogWarning($"Level {level.levelId} missing strategy - analytical entry point unavailable");
        }
        
        // Exercise provides kinesthetic entry point
        // Story connection provides narrative entry point (handled by GameModeManager)
    }
    
    /// <summary>
    /// Validate and simplify configuration (Jobs principle)
    /// </summary>
    static void ValidateAndSimplify(LevelData level)
    {
        // Ensure required fields are present
        if (string.IsNullOrEmpty(level.levelId))
        {
            level.levelId = GenerateLevelId(level.gameMode, level.episodeNumber, level.codingConcept);
        }
        
        if (string.IsNullOrEmpty(level.levelName))
        {
            level.levelName = $"{level.codingConcept} Exercise";
        }
        
        // Simplify video config if not set
        if (level.videoConfig == null)
        {
            level.videoConfig = new VideoConfig
            {
                autoPlay = true,
                loop = false,
                playbackSpeed = 1.0f,
                allowSeeking = true
            };
        }
    }
    
    /// <summary>
    /// Get available code blocks for a concept
    /// </summary>
    static string[] GetAvailableBlocksForConcept(string concept)
    {
        // Map concepts to available blocks
        Dictionary<string, string[]> conceptBlocks = new Dictionary<string, string[]>
        {
            { "state", new string[] { "START", "LIVE", "DEAD", "OUTCOME", "IF_STATE", "SET_STATE" } },
            { "conditionals", new string[] { "IF", "THEN", "ELSE", "IF_DEFENDER_TRAPS", "PASS_LEFT", "DRIVE_RIGHT" } },
            { "loops", new string[] { "REPEAT", "FOR_EACH", "WHILE", "ROTATE", "CLOSEOUT" } },
            { "variables", new string[] { "SET_VARIABLE", "GET_VARIABLE", "INCREMENT", "DECREMENT" } },
            { "functions", new string[] { "DEFINE_FUNCTION", "CALL_FUNCTION", "RETURN" } }
        };
        
        if (conceptBlocks.ContainsKey(concept.ToLower()))
        {
            return conceptBlocks[concept.ToLower()];
        }
        
        // Default blocks
        return new string[] { "START", "DRIBBLE", "PASS", "SHOOT", "BUCKET" };
    }
    
    /// <summary>
    /// Get required blocks for a concept
    /// </summary>
    static string[] GetRequiredBlocksForConcept(string concept)
    {
        Dictionary<string, string[]> conceptRequired = new Dictionary<string, string[]>
        {
            { "state", new string[] { "IF_STATE", "SET_STATE" } },
            { "conditionals", new string[] { "IF", "THEN" } },
            { "loops", new string[] { "REPEAT" } }
        };
        
        if (conceptRequired.ContainsKey(concept.ToLower()))
        {
            return conceptRequired[concept.ToLower()];
        }
        
        return new string[] { };
    }
    
    /// <summary>
    /// Save level data to JSON file
    /// </summary>
    public static void SaveLevelToJSON(LevelData level, string filePath)
    {
        LevelDataCollection collection = new LevelDataCollection
        {
            levels = new List<LevelData> { level },
            version = "1.0",
            lastUpdated = System.DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
        };
        
        string json = JsonUtility.ToJson(collection, true);
        
        // Ensure directory exists
        string directory = Path.GetDirectoryName(filePath);
        if (!Directory.Exists(directory))
        {
            Directory.CreateDirectory(directory);
        }
        
        File.WriteAllText(filePath, json);
        Debug.Log($"Saved level to: {filePath}");
    }
    
    /// <summary>
    /// Batch generate levels from a list of inputs
    /// </summary>
    public static void BatchGenerateLevels(List<LevelInput> inputs, string outputDirectory)
    {
        foreach (LevelInput input in inputs)
        {
            LevelData level = GenerateLevelFromInputs(
                input.levelName,
                input.videoPath,
                input.strategy,
                input.gameMode,
                input.episodeNumber,
                input.codingConcept,
                input.exerciseType
            );
            
            string fileName = $"{level.levelId}.json";
            string filePath = Path.Combine(outputDirectory, fileName);
            
            SaveLevelToJSON(level, filePath);
        }
    }
}

/// <summary>
/// Simple input structure for generating levels
/// This is what you'll fill out to create new levels
/// </summary>
[System.Serializable]
public class LevelInput
{
    public string levelName;
    public string videoPath;
    public StrategyData strategy;
    public string gameMode;
    public int episodeNumber;
    public string codingConcept;
    public ExerciseType exerciseType = ExerciseType.Analysis;
}



