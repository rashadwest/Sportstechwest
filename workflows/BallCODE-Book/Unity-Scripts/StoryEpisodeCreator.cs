using UnityEngine;
using UnityEditor;
using System.Collections.Generic;

/// <summary>
/// Editor tool for creating Story Episode ScriptableObjects
/// Enhanced with educational concept support
/// </summary>
public class StoryEpisodeCreator : EditorWindow
{
    [MenuItem("BallCODE/Create Story Episode")]
    public static void ShowWindow()
    {
        GetWindow<StoryEpisodeCreator>("Create Story Episode");
    }
    
    private int episodeNumber = 1;
    private string title = "";
    private string subtitle = "";
    private string codingConcept = "";
    private string mathConcept = "";
    private string aiConcept = "";
    private string monsterName = "";
    private string gameMode = "Training";
    
    void OnGUI()
    {
        GUILayout.Label("Create New Story Episode", EditorStyles.boldLabel);
        
        episodeNumber = EditorGUILayout.IntField("Episode Number", episodeNumber);
        title = EditorGUILayout.TextField("Title", title);
        subtitle = EditorGUILayout.TextField("Subtitle", subtitle);
        
        EditorGUILayout.Space();
        GUILayout.Label("Educational Concepts", EditorStyles.boldLabel);
        codingConcept = EditorGUILayout.TextField("Coding Concept", codingConcept);
        mathConcept = EditorGUILayout.TextField("Math Concept", mathConcept);
        aiConcept = EditorGUILayout.TextField("AI Concept", aiConcept);
        
        EditorGUILayout.Space();
        monsterName = EditorGUILayout.TextField("Monster Name", monsterName);
        gameMode = EditorGUILayout.TextField("Game Mode", gameMode);
        
        EditorGUILayout.Space();
        if (GUILayout.Button("Create Episode Asset"))
        {
            CreateEpisodeAsset();
        }
    }
    
    void CreateEpisodeAsset()
    {
        StoryEpisodeData episode = ScriptableObject.CreateInstance<StoryEpisodeData>();
        episode.episodeNumber = episodeNumber;
        episode.title = title;
        episode.subtitle = subtitle;
        episode.codingConcept = codingConcept;
        episode.mathConcept = mathConcept;
        episode.monsterName = monsterName;
        episode.hasFinalExercise = true;
        episode.spreads = new StorySpreadData[0];
        
        string path = $"Assets/StoryContent/Episodes/Episode{episodeNumber}.asset";
        AssetDatabase.CreateAsset(episode, path);
        AssetDatabase.SaveAssets();
        
        EditorUtility.DisplayDialog("Success", $"Created Episode {episodeNumber} asset at {path}", "OK");
    }
}

/// <summary>
/// ScriptableObject for Story Episode data
/// Enhanced with educational fields
/// </summary>
[CreateAssetMenu(fileName = "Story Episode", menuName = "BallCODE/Story Episode")]
public class StoryEpisodeData : ScriptableObject
{
    [Header("Episode Info")]
    public int episodeNumber;
    public string title;
    public string subtitle;
    
    [Header("Educational Concepts")]
    public string codingConcept;
    public string mathConcept;
    public string aiConcept;
    
    [Header("Learning Objectives")]
    public string[] learningObjectives;
    
    [Header("Episode Details")]
    public string monsterName;
    public string gameMode;
    public bool hasFinalExercise = true;
    
    [Header("Spreads (Pages)")]
    public StorySpreadData[] spreads;
    
    [Header("Skill Pit-Stop")]
    public SkillPitStopData skillPitStop;
    
    /// <summary>
    /// Convert to runtime StoryEpisode format
    /// </summary>
    public StoryEpisode ToRuntimeEpisode()
    {
        StoryEpisode episode = new StoryEpisode
        {
            episodeNumber = this.episodeNumber,
            title = this.title,
            subtitle = this.subtitle,
            codingConcept = this.codingConcept,
            mathConcept = this.mathConcept,
            aiConcept = this.aiConcept,
            learningObjectives = this.learningObjectives,
            monsterName = this.monsterName,
            gameMode = this.gameMode,
            hasFinalExercise = this.hasFinalExercise,
            spreads = new System.Collections.Generic.List<StorySpread>(),
            skillPitStop = this.skillPitStop
        };
        
        foreach (var spreadData in spreads)
        {
            episode.spreads.Add(spreadData.ToRuntimeSpread());
        }
        
        return episode;
    }
}

[System.Serializable]
public class StorySpreadData
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
    public string educationalHighlight;
    
    public StorySpread ToRuntimeSpread()
    {
        return new StorySpread
        {
            leftPageText = this.leftPageText,
            leftPageImage = this.leftPageImage,
            rightPageText = this.rightPageText,
            rightPageImage = this.rightPageImage,
            hasExercise = this.hasExercise,
            exerciseName = this.exerciseName,
            audioClipIndex = this.audioClipIndex,
            educationalConceptType = this.educationalConceptType,
            educationalHighlight = this.educationalHighlight
        };
    }
}

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

[System.Serializable]
public class CodeExample
{
    public string language;
    [TextArea(5, 10)]
    public string code;
    [TextArea(3, 5)]
    public string explanation;
}

[System.Serializable]
public class MathExample
{
    public string type;
    [TextArea(3, 5)]
    public string example;
    [TextArea(3, 5)]
    public string explanation;
}

[System.Serializable]
public class AIExample
{
    public string type;
    [TextArea(3, 5)]
    public string example;
    [TextArea(3, 5)]
    public string explanation;
}
