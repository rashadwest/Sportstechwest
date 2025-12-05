using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Story episode data structure with educational focus
/// Contains all spreads (pages) for an episode
/// Enhanced with code, math, and AI concept tracking
/// </summary>
[System.Serializable]
public class StoryEpisode 
{
    public int episodeNumber;
    public string title;
    public string subtitle;
    
    [Header("Educational Concepts")]
    public string codingConcept;
    public string mathConcept;
    public string aiConcept; // Added for AI concept tracking
    
    [Header("Learning Objectives")]
    public string[] learningObjectives; // Added for learning objective tracking
    
    [Header("Episode Info")]
    public string monsterName;
    public string gameMode;
    public bool hasFinalExercise = true;
    
    [Header("Content")]
    public List<StorySpread> spreads;
    
    [Header("Skill Pit-Stop")]
    public SkillPitStopData skillPitStop; // Added for educational content
}

/// <summary>
/// Story spread (two-page layout)
/// Left page: Story text + character art
/// Right page: Visual diagram + code example
/// Enhanced with educational highlights
/// </summary>
[System.Serializable]
public class StorySpread 
{
    [Header("Left Page")]
    [TextArea(5, 10)]
    public string leftPageText;
    public Sprite leftPageImage;
    
    [Header("Right Page")]
    public string rightPageText;
    public Sprite rightPageImage;
    
    [Header("Exercise")]
    public bool hasExercise;
    public string exerciseName;
    public int audioClipIndex;
    
    [Header("Educational Focus")]
    public string educationalConceptType; // "coding", "math", "ai", or "general"
    public string educationalHighlight; // What concept is being taught
}

/// <summary>
/// Skill Pit-Stop educational content
/// Contains code examples, math examples, and AI examples
/// </summary>
[System.Serializable]
public class SkillPitStopData
{
    public string title;
    [TextArea(10, 20)]
    public string content;
    
    [Header("Code Examples")]
    public CodeExample[] codeExamples;
    
    [Header("Math Examples")]
    public MathExample[] mathExamples;
    
    [Header("AI Examples")]
    public AIExample[] aiExamples;
}

/// <summary>
/// Code example for Skill Pit-Stop
/// </summary>
[System.Serializable]
public class CodeExample
{
    public string language;
    [TextArea(5, 10)]
    public string code;
    [TextArea(3, 5)]
    public string explanation;
}

/// <summary>
/// Math example for Skill Pit-Stop
/// </summary>
[System.Serializable]
public class MathExample
{
    public string type;
    [TextArea(3, 5)]
    public string example;
    [TextArea(3, 5)]
    public string explanation;
}

/// <summary>
/// AI example for Skill Pit-Stop
/// </summary>
[System.Serializable]
public class AIExample
{
    public string type;
    [TextArea(3, 5)]
    public string example;
    [TextArea(3, 5)]
    public string explanation;
}
