using UnityEngine;
using System.Collections.Generic;
using System.IO;
using System;

/// <summary>
/// Tool for creating new levels with player positions and dribble data
/// This script helps you create levels by providing x,y coordinates and dribble information
/// </summary>
public class LevelCreator : MonoBehaviour
{
    [Header("Level Creation Settings")]
    public string outputDirectory = "Assets/StreamingAssets/Levels";
    public bool useNormalizedCoordinates = false; // If true, use 0-1 range; if false, use feet (0-94, 0-50)
    
    [Header("Court Reference")]
    [Tooltip("Standard basketball court: 94 feet x 50 feet. Origin (0,0) is bottom-left.")]
    public float courtWidth = 94f;  // Feet
    public float courtHeight = 50f; // Feet
    
    /// <summary>
    /// Create a new level with player positions and dribble data
    /// </summary>
    public LevelData CreateLevel(
        string levelId,
        string levelName,
        string description,
        string gameMode,
        int episodeNumber,
        string codingConcept,
        List<StrategyStepWithPositions> steps,
        ExerciseConfig exercise = null
    )
    {
        LevelData level = new LevelData
        {
            levelId = levelId,
            levelName = levelName,
            description = description,
            gameMode = gameMode,
            episodeNumber = episodeNumber,
            codingConcept = codingConcept,
            videoPath = "",
            videoConfig = new VideoConfig
            {
                autoPlay = true,
                loop = false,
                playbackSpeed = 1.0f,
                allowSeeking = true,
                startTime = 0.0f,
                endTime = -1.0f,
                pausePoints = new float[0],
                analysisPoints = new List<VideoAnalysisPoint>()
            },
            strategy = new StrategyData
            {
                strategyName = levelName,
                strategyType = "offensive",
                description = description,
                steps = ConvertSteps(steps),
                keyConcepts = new string[] { codingConcept },
                basketballConcepts = ExtractBasketballConcepts(steps),
                diagramPath = "",
                showCourtDiagram = true
            },
            learningObjectives = GenerateLearningObjectives(codingConcept),
            successCriteria = GenerateSuccessCriteria(codingConcept),
            difficultyLevel = CalculateDifficulty(episodeNumber),
            prerequisiteLevels = new string[0],
            isUnlocked = true,
            exercise = exercise ?? GenerateDefaultExercise(gameMode, codingConcept),
            author = "Level Creator",
            createdDate = DateTime.Now.ToString("yyyy-MM-dd"),
            tags = GenerateTags(gameMode, codingConcept)
        };
        
        return level;
    }
    
    /// <summary>
    /// Convert steps with positions to StrategyStep objects
    /// </summary>
    List<StrategyStep> ConvertSteps(List<StrategyStepWithPositions> stepsWithPositions)
    {
        List<StrategyStep> steps = new List<StrategyStep>();
        
        foreach (var stepData in stepsWithPositions)
        {
            StrategyStep step = new StrategyStep
            {
                stepNumber = stepData.stepNumber,
                action = stepData.action,
                codeEquivalent = stepData.codeEquivalent,
                timing = stepData.timing,
                playerPositions = new List<PlayerPosition>()
            };
            
            // Add player positions
            if (stepData.positions != null)
            {
                foreach (var pos in stepData.positions)
                {
                    step.playerPositions.Add(new PlayerPosition(
                        pos.x,
                        pos.y,
                        pos.playerId,
                        pos.dribbleType,
                        pos.dribbleDirection,
                        useNormalizedCoordinates
                    ));
                }
            }
            
            steps.Add(step);
        }
        
        return steps;
    }
    
    /// <summary>
    /// Extract basketball concepts from steps
    /// </summary>
    string[] ExtractBasketballConcepts(List<StrategyStepWithPositions> steps)
    {
        HashSet<string> concepts = new HashSet<string>();
        
        foreach (var step in steps)
        {
            if (step.positions != null)
            {
                foreach (var pos in step.positions)
                {
                    if (pos.dribbleType > 0)
                    {
                        concepts.Add(GetDribbleName(pos.dribbleType));
                    }
                }
            }
        }
        
        return new List<string>(concepts).ToArray();
    }
    
    /// <summary>
    /// Get dribble name from type number
    /// </summary>
    string GetDribbleName(int dribbleType)
    {
        return dribbleType switch
        {
            1 => "pound_dribble",
            2 => "crossover_dribble",
            3 => "in_out_dribble",
            4 => "between_legs_dribble",
            5 => "behind_back_dribble",
            6 => "half_spin_dribble",
            7 => "spin_dribble",
            _ => "unknown_dribble"
        };
    }
    
    /// <summary>
    /// Generate learning objectives
    /// </summary>
    string[] GenerateLearningObjectives(string codingConcept)
    {
        return codingConcept switch
        {
            "basic_blocks_sequences" => new string[] {
                "Understand that coding starts with simple, repeatable blocks",
                "Practice creating sequences by repeating foundation blocks"
            },
            "if_then_conditionals" => new string[] {
                "Understand that coding uses if/then to make decisions",
                "Practice creating conditional sequences"
            },
            "loops_repetition" => new string[] {
                "Understand that coding uses loops to repeat patterns",
                "Practice creating loop sequences"
            },
            _ => new string[] { "Learn coding concepts through basketball" }
        };
    }
    
    /// <summary>
    /// Generate success criteria
    /// </summary>
    string[] GenerateSuccessCriteria(string codingConcept)
    {
        return new string[] {
            "Complete exercise with 70% or higher score",
            "Demonstrate understanding through interactive practice"
        };
    }
    
    /// <summary>
    /// Calculate difficulty based on episode
    /// </summary>
    int CalculateDifficulty(int episodeNumber)
    {
        return Mathf.Clamp(episodeNumber + 1, 1, 5);
    }
    
    /// <summary>
    /// Generate default exercise config
    /// </summary>
    ExerciseConfig GenerateDefaultExercise(string gameMode, string codingConcept)
    {
        ExerciseConfig exercise = new ExerciseConfig
        {
            exerciseType = gameMode == "blockcoding" ? ExerciseType.BlockCoding : ExerciseType.Analysis,
            scoring = new ScoringConfig
            {
                maxScore = 100,
                passingScore = 70,
                showScoreDuringExercise = false,
                allowRetry = true,
                maxAttempts = 3
            }
        };
        
        if (exercise.exerciseType == ExerciseType.BlockCoding)
        {
            exercise.blockCoding = new BlockCodingExercise
            {
                availableBlocks = new string[] { "START", "DRIBBLE", "ADVANCE" },
                requiredBlocks = new string[] { "DRIBBLE" },
                targetCode = "",
                allowCustomBlocks = false
            };
        }
        
        return exercise;
    }
    
    /// <summary>
    /// Generate tags
    /// </summary>
    string[] GenerateTags(string gameMode, string codingConcept)
    {
        return new string[] { gameMode, codingConcept };
    }
    
    /// <summary>
    /// Save level to JSON file
    /// </summary>
    public void SaveLevelToJSON(LevelData level, string filename)
    {
        LevelDataCollection collection = new LevelDataCollection
        {
            levels = new List<LevelData> { level },
            version = "1.0",
            lastUpdated = DateTime.Now.ToString("yyyy-MM-dd")
        };
        
        string json = JsonUtility.ToJson(collection, true);
        
        // Ensure directory exists
        string directory = Path.Combine(Application.dataPath, "StreamingAssets", "Levels");
        if (!Directory.Exists(directory))
        {
            Directory.CreateDirectory(directory);
        }
        
        string filepath = Path.Combine(directory, filename);
        File.WriteAllText(filepath, json);
        
        Debug.Log($"Level saved to: {filepath}");
    }
}

/// <summary>
/// Helper class for creating steps with position data
/// </summary>
[System.Serializable]
public class StrategyStepWithPositions
{
    public int stepNumber;
    public string action;
    public string codeEquivalent;
    public float timing;
    public List<PlayerPositionData> positions;
}

/// <summary>
/// Simplified position data for level creation
/// </summary>
[System.Serializable]
public class PlayerPositionData
{
    public float x;
    public float y;
    public string playerId;
    public int dribbleType;        // 1-7
    public string dribbleDirection; // "left", "right", "forward", "backward", "none"
}




