using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Level/Scenario data structure for video and strategy-based game levels
/// This allows you to add new levels by simply providing videos and strategies
/// </summary>
[System.Serializable]
public class LevelData
{
    [Header("Level Identification")]
    public string levelId;                    // Unique identifier (e.g., "training_state_001")
    public string levelName;                   // Display name (e.g., "State Tracking Challenge 1")
    public string description;                 // Brief description of the level
    
    [Header("Game Mode Configuration")]
    public string gameMode;                    // Which game mode this belongs to: "training", "prediction", "math", "blockcoding", "freeplay"
    public int episodeNumber;                  // Associated episode number (0-based)
    public string codingConcept;               // Coding concept taught (e.g., "state", "conditionals", "loops")
    
    [Header("Video Configuration")]
    public string videoPath;                   // Path to video file (relative to StreamingAssets or Resources)
    public VideoConfig videoConfig;              // Video playback settings
    
    [Header("Strategy Configuration")]
    public StrategyData strategy;             // Basketball strategy/play to analyze
    
    [Header("Learning Objectives")]
    public string[] learningObjectives;       // What students will learn
    public string[] successCriteria;           // How success is measured
    
    [Header("Difficulty & Progression")]
    public int difficultyLevel;                // 1-5 difficulty rating
    public string[] prerequisiteLevels;        // Level IDs that must be completed first
    public bool isUnlocked = true;              // Whether level is available
    
    [Header("Exercise Configuration")]
    public ExerciseConfig exercise;            // Exercise-specific settings
    
    [Header("Metadata")]
    public string author;                      // Who created this level
    public string createdDate;                  // When it was created
    public string[] tags;                       // Searchable tags
}

/// <summary>
/// Video playback and analysis configuration
/// </summary>
[System.Serializable]
public class VideoConfig
{
    [Header("Playback Settings")]
    public bool autoPlay = true;               // Start playing automatically
    public bool loop = false;                   // Loop the video
    public float playbackSpeed = 1.0f;          // Playback speed multiplier
    public bool allowSeeking = true;            // Allow scrubbing through video
    
    [Header("Analysis Points")]
    public List<VideoAnalysisPoint> analysisPoints;  // Key moments to analyze
    
    [Header("Timing")]
    public float startTime = 0f;                // Start time in seconds
    public float endTime = -1f;                 // End time (-1 = end of video)
    public float[] pausePoints;                 // Times to pause for analysis
}

/// <summary>
/// Key moments in video for analysis or interaction
/// </summary>
[System.Serializable]
public class VideoAnalysisPoint
{
    public float timestamp;                     // Time in video (seconds)
    public string description;                  // What to analyze at this point
    public string question;                     // Question to ask student
    public string[] correctAnswers;             // Acceptable answers
    public AnalysisType type;                   // Type of analysis required
}

/// <summary>
/// Types of analysis students can perform
/// </summary>
public enum AnalysisType
{
    StateIdentification,        // Identify game state
    PositionAnalysis,           // Analyze player positions
    DecisionPrediction,         // Predict what will happen
    StrategyIdentification,    // Identify the strategy
    ErrorDetection,             // Find mistakes
    PatternRecognition,          // Recognize patterns
    CodeBlockSelection          // Select correct code blocks
}

/// <summary>
/// Basketball strategy/play data
/// </summary>
[System.Serializable]
public class StrategyData
{
    [Header("Strategy Info")]
    public string strategyName;                // Name of the strategy (e.g., "Fast Break")
    public string strategyType;                 // Type: "offensive", "defensive", "transition"
    public string description;                  // Description of the strategy
    
    [Header("Strategy Steps")]
    public List<StrategyStep> steps;            // Sequential steps of the strategy
    
    [Header("Key Concepts")]
    public string[] keyConcepts;                // Coding/math/AI concepts demonstrated
    public string[] basketballConcepts;         // Basketball concepts involved
    
    [Header("Visualization")]
    public string diagramPath;                  // Path to strategy diagram
    public bool showCourtDiagram = true;        // Show court visualization
}

/// <summary>
/// Individual step in a basketball strategy
/// </summary>
[System.Serializable]
public class StrategyStep
{
    public int stepNumber;                      // Step order
    public string action;                       // Action description (e.g., "Point guard receives ball")
    public string codeEquivalent;               // Equivalent code/block representation
    public float timing;                        // When this step occurs (seconds)
    public string[] playerPositions;            // Key player positions
}

/// <summary>
/// Exercise-specific configuration
/// </summary>
[System.Serializable]
public class ExerciseConfig
{
    [Header("Exercise Type")]
    public ExerciseType exerciseType;           // Type of exercise
    
    [Header("Block Coding Exercise")]
    public BlockCodingExercise blockCoding;     // Block coding configuration
    
    [Header("Analysis Exercise")]
    public AnalysisExercise analysis;            // Analysis exercise configuration
    
    [Header("Prediction Exercise")]
    public PredictionExercise prediction;      // Prediction exercise configuration
    
    [Header("Math Exercise")]
    public MathExercise math;                   // Math exercise configuration
    
    [Header("Scoring")]
    public ScoringConfig scoring;               // How the exercise is scored
}

/// <summary>
/// Types of exercises available
/// </summary>
public enum ExerciseType
{
    BlockCoding,        // Drag and drop code blocks
    Analysis,           // Analyze video/strategy
    Prediction,         // Predict opponent behavior
    Math,               // Math-based calculations
    Freeplay            // Open-ended exploration
}

/// <summary>
/// Block coding exercise configuration
/// </summary>
[System.Serializable]
public class BlockCodingExercise
{
    public string[] availableBlocks;            // Which blocks are available
    public string[] requiredBlocks;            // Blocks that must be used
    public string targetCode;                   // Target code/sequence
    public bool allowCustomBlocks = false;      // Allow creating custom blocks
}

/// <summary>
/// Analysis exercise configuration
/// </summary>
[System.Serializable]
public class AnalysisExercise
{
    public int numberOfQuestions;               // How many questions to ask
    public bool showVideoDuringQuestions = true; // Show video while answering
    public float timeLimit = -1f;              // Time limit (-1 = no limit)
}

/// <summary>
/// Prediction exercise configuration
/// </summary>
[System.Serializable]
public class PredictionExercise
{
    public int numberOfPredictions;            // How many predictions to make
    public float predictionWindow = 5f;         // Seconds ahead to predict
    public bool showFeedback = true;            // Show if prediction was correct
}

/// <summary>
/// Math exercise configuration
/// </summary>
[System.Serializable]
public class MathExercise
{
    public string mathConcept;                  // Math concept (e.g., "angles", "probability")
    public int numberOfProblems;               // Number of math problems
    public bool showVisualAids = true;          // Show visual aids
}

/// <summary>
/// Scoring configuration
/// </summary>
[System.Serializable]
public class ScoringConfig
{
    public int maxScore = 100;                  // Maximum possible score
    public int passingScore = 70;                // Minimum score to pass
    public bool showScoreDuringExercise = false; // Show score while playing
    public bool allowRetry = true;              // Allow retrying the exercise
    public int maxAttempts = 3;                 // Maximum number of attempts
}

/// <summary>
/// Collection of level data (for loading from JSON)
/// </summary>
[System.Serializable]
public class LevelDataCollection
{
    public List<LevelData> levels;
    public string version;
    public string lastUpdated;
}



