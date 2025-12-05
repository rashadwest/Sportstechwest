using UnityEngine;
using UnityEditor;
using System.IO;
using Newtonsoft.Json;
using System.Collections.Generic;

/// <summary>
/// Enhanced Unity Editor script for generating educational story assets
/// Handles code, math, and AI concept integration
/// </summary>
public class EducationalStoryAssetGenerator : EditorWindow
{
    [MenuItem("BallCODE/Generate Educational Story Assets")]
    public static void GenerateAssets()
    {
        string jsonPath = EditorUtility.OpenFilePanel("Select Episode JSON", "", "json");
        if (string.IsNullOrEmpty(jsonPath)) return;
        
        // Load and parse JSON
        string jsonContent = File.ReadAllText(jsonPath);
        EducationalEpisodeData episodeData = JsonConvert.DeserializeObject<EducationalEpisodeData>(jsonContent);
        
        if (episodeData == null)
        {
            EditorUtility.DisplayDialog("Error", "Failed to parse JSON file", "OK");
            return;
        }
        
        // Create ScriptableObject
        StoryEpisodeData episodeAsset = ScriptableObject.CreateInstance<StoryEpisodeData>();
        
        // Map basic episode info
        episodeAsset.episodeNumber = episodeData.episodeNumber;
        episodeAsset.title = episodeData.title;
        episodeAsset.subtitle = episodeData.subtitle;
        episodeAsset.monsterName = episodeData.monsterName;
        episodeAsset.hasFinalExercise = episodeData.hasFinalExercise;
        
        // Map educational concepts
        episodeAsset.codingConcept = episodeData.educationalConcepts.codingConcept.name;
        episodeAsset.mathConcept = episodeData.educationalConcepts.mathConcept.name;
        episodeAsset.aiConcept = episodeData.educationalConcepts.aiConcept.name;
        
        // Map learning objectives
        if (episodeData.learningObjectives != null && episodeData.learningObjectives.Length > 0)
        {
            episodeAsset.learningObjectives = new string[episodeData.learningObjectives.Length];
            for (int i = 0; i < episodeData.learningObjectives.Length; i++)
            {
                episodeAsset.learningObjectives[i] = episodeData.learningObjectives[i];
            }
        }
        
        // Process spreads
        List<StorySpread> spreads = new List<StorySpread>();
        for (int i = 0; i < episodeData.spreads.Count; i++)
        {
            var spreadData = episodeData.spreads[i];
            StorySpread spread = new StorySpread();
            
            // Map text
            spread.leftPageText = spreadData.leftPage.text;
            spread.rightPageText = spreadData.rightPage.text;
            
            // Load left page image
            string leftImagePath = $"Assets/StoryContent/Images/Episode{episodeData.episodeNumber}/ep{episodeData.episodeNumber}_spread{spreadData.spreadNumber}_left.png";
            if (File.Exists(leftImagePath))
            {
                spread.leftPageImage = AssetDatabase.LoadAssetAtPath<Sprite>(leftImagePath);
                if (spread.leftPageImage == null)
                {
                    // Try loading as Texture2D and convert
                    Texture2D texture = AssetDatabase.LoadAssetAtPath<Texture2D>(leftImagePath);
                    if (texture != null)
                    {
                        // Create sprite from texture
                        spread.leftPageImage = Sprite.Create(
                            texture,
                            new Rect(0, 0, texture.width, texture.height),
                            new Vector2(0.5f, 0.5f)
                        );
                    }
                }
            }
            
            // Load right page image
            string rightImagePath = $"Assets/StoryContent/Images/Episode{episodeData.episodeNumber}/ep{episodeData.episodeNumber}_spread{spreadData.spreadNumber}_right.png";
            if (File.Exists(rightImagePath))
            {
                spread.rightPageImage = AssetDatabase.LoadAssetAtPath<Sprite>(rightImagePath);
                if (spread.rightPageImage == null)
                {
                    Texture2D texture = AssetDatabase.LoadAssetAtPath<Texture2D>(rightImagePath);
                    if (texture != null)
                    {
                        spread.rightPageImage = Sprite.Create(
                            texture,
                            new Rect(0, 0, texture.width, texture.height),
                            new Vector2(0.5f, 0.5f)
                        );
                    }
                }
            }
            
            // Map exercise info
            spread.hasExercise = spreadData.hasExercise;
            if (spread.hasExercise)
            {
                spread.exerciseName = spreadData.exerciseName;
            }
            
            // Map educational focus
            spread.educationalConceptType = spreadData.leftPage.educationalHighlight?.concept ?? "general";
            spread.educationalHighlight = spreadData.leftPage.educationalHighlight?.highlight ?? "";
            
            // Map audio clip index
            spread.audioClipIndex = i; // Will be set when loading audio clips
            
            spreads.Add(spread);
        }
        
        episodeAsset.spreads = spreads.ToArray();
        
        // Load audio clips
        AudioClip[] audioClips = LoadAudioClips(episodeData.episodeNumber);
        
        // Save asset
        string assetPath = $"Assets/StoryContent/Episodes/Episode{episodeData.episodeNumber}.asset";
        
        // Create directory if it doesn't exist
        string assetDir = Path.GetDirectoryName(assetPath);
        if (!Directory.Exists(assetDir))
        {
            Directory.CreateDirectory(assetDir);
        }
        
        AssetDatabase.CreateAsset(episodeAsset, assetPath);
        AssetDatabase.SaveAssets();
        
        // Store audio clips reference (you may need to modify StoryEpisodeData to include this)
        // For now, we'll log the audio clips
        // Map Skill Pit-Stop if present
        if (episodeData.skillPitStop != null)
        {
            episodeAsset.skillPitStop = new SkillPitStopData
            {
                title = episodeData.skillPitStop.title,
                content = episodeData.skillPitStop.content,
                codeExamples = ConvertCodeExamples(episodeData.skillPitStop.codeExamples),
                mathExamples = ConvertMathExamples(episodeData.skillPitStop.mathExamples),
                aiExamples = ConvertAIExamples(episodeData.skillPitStop.aiExamples)
            };
        }
        
        Debug.Log($"Generated educational story asset: {assetPath}");
        Debug.Log($"  Coding Concept: {episodeAsset.codingConcept}");
        Debug.Log($"  Math Concept: {episodeAsset.mathConcept}");
        Debug.Log($"  AI Concept: {episodeAsset.aiConcept}");
        Debug.Log($"  Learning Objectives: {episodeData.learningObjectives.Length}");
        Debug.Log($"  Spreads: {spreads.Count}");
        Debug.Log($"  Audio Clips: {audioClips.Length}");
        
        EditorUtility.DisplayDialog("Success", 
            $"Generated Episode {episodeData.episodeNumber} asset!\n\n" +
            $"Coding: {episodeAsset.codingConcept}\n" +
            $"Math: {episodeAsset.mathConcept}\n" +
            $"Spreads: {spreads.Count}\n" +
            $"Audio: {audioClips.Length} clips",
            "OK");
    }
    
    private static AudioClip[] LoadAudioClips(int episodeNumber)
    {
        string audioDir = $"Assets/StoryContent/Audio/Episode{episodeNumber}/";
        
        if (!Directory.Exists(audioDir))
        {
            Debug.LogWarning($"Audio directory not found: {audioDir}");
            return new AudioClip[0];
        }
        
        string[] audioFiles = Directory.GetFiles(audioDir, "*.mp3");
        List<AudioClip> clips = new List<AudioClip>();
        
        foreach (string audioFile in audioFiles)
        {
            string relativePath = audioFile.Replace(Application.dataPath, "Assets");
            AudioClip clip = AssetDatabase.LoadAssetAtPath<AudioClip>(relativePath);
            if (clip != null)
            {
                clips.Add(clip);
            }
        }
        
        // Sort by filename to ensure correct order
        clips.Sort((a, b) => string.Compare(a.name, b.name));
        
        return clips.ToArray();
    }
    
    private static CodeExample[] ConvertCodeExamples(CodeExample[] examples)
    {
        if (examples == null) return new CodeExample[0];
        return examples;
    }
    
    private static MathExample[] ConvertMathExamples(MathExample[] examples)
    {
        if (examples == null) return new MathExample[0];
        return examples;
    }
    
    private static AIExample[] ConvertAIExamples(AIExample[] examples)
    {
        if (examples == null) return new AIExample[0];
        return examples;
    }
}

// JSON data structures matching the episode JSON format
[System.Serializable]
public class EducationalEpisodeData
{
    public int episodeNumber;
    public string title;
    public string subtitle;
    public EducationalConcepts educationalConcepts;
    public string[] learningObjectives;
    public string monsterName;
    public string gameMode;
    public bool hasFinalExercise;
    public List<EducationalSpread> spreads;
    public SkillPitStopData skillPitStop;
    public List<EducationalExercise> exercises;
}

[System.Serializable]
public class EducationalConcepts
{
    public CodingConcept codingConcept;
    public MathConcept mathConcept;
    public AIConcept aiConcept;
}

[System.Serializable]
public class CodingConcept
{
    public string name;
    public string description;
    public string[] keyPoints;
    public string codeExample;
    public string visualType;
    public string difficulty;
}

[System.Serializable]
public class MathConcept
{
    public string name;
    public string description;
    public string[] keyPoints;
    public string mathExample;
    public string visualType;
    public string difficulty;
}

[System.Serializable]
public class AIConcept
{
    public string name;
    public string description;
    public string[] keyPoints;
    public string aiExample;
    public string visualType;
    public string difficulty;
}

[System.Serializable]
public class EducationalSpread
{
    public int spreadNumber;
    public PageData leftPage;
    public PageData rightPage;
    public AudioData audio;
    public bool hasExercise;
    public string exerciseName;
}

[System.Serializable]
public class PageData
{
    public string text;
    public string imagePrompt;
    public string imageStyle;
    public EducationalHighlight educationalHighlight;
}

[System.Serializable]
public class EducationalHighlight
{
    public string concept;
    public string highlight;
}

[System.Serializable]
public class AudioData
{
    public string text;
    public string voice;
    public float speed;
    public string[] emphasis;
}

[System.Serializable]
public class SkillPitStopData
{
    public string title;
    public string content;
    public CodeExample[] codeExamples;
    public MathExample[] mathExamples;
    public AIExample[] aiExamples;
}

[System.Serializable]
public class CodeExample
{
    public string language;
    public string code;
    public string explanation;
}

[System.Serializable]
public class MathExample
{
    public string type;
    public string example;
    public string explanation;
}

[System.Serializable]
public class AIExample
{
    public string type;
    public string example;
    public string explanation;
}

[System.Serializable]
public class EducationalExercise
{
    public int exerciseNumber;
    public string type;
    public string title;
    public string instructions;
    public int duration;
    public string codingFocus;
    public string mathFocus;
    public string aiFocus;
    public string difficulty;
}

