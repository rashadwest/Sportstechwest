using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Helper script to create test story data for quick setup
/// Attach this to a GameObject to populate StoryModeManager with test data
/// Useful for testing before creating full ScriptableObject assets
/// </summary>
public class TestStoryDataHelper : MonoBehaviour
{
    [Header("Auto-Populate on Start")]
    [Tooltip("Automatically populate StoryModeManager with test data when scene starts")]
    public bool autoPopulateOnStart = true;
    
    [Header("Test Data")]
    [Tooltip("Number of test episodes to create")]
    [Range(1, 3)]
    public int numberOfEpisodes = 1;
    
    private void Start()
    {
        if (autoPopulateOnStart)
        {
            PopulateTestData();
        }
    }
    
    /// <summary>
    /// Populate StoryModeManager with test episode data
    /// </summary>
    [ContextMenu("Populate Test Data")]
    public void PopulateTestData()
    {
        StoryModeManager manager = FindObjectOfType<StoryModeManager>();
        if (manager == null)
        {
            Debug.LogError("StoryModeManager not found in scene!");
            return;
        }
        
        List<StoryEpisode> episodes = new List<StoryEpisode>();
        
        // Create Episode 1: The Tip-off Trial
        if (numberOfEpisodes >= 1)
        {
            episodes.Add(CreateEpisode1());
        }
        
        // Create Episode 2: The If/Then Fork
        if (numberOfEpisodes >= 2)
        {
            episodes.Add(CreateEpisode2());
        }
        
        // Create Episode 3: Loop of the Rotating Guardians
        if (numberOfEpisodes >= 3)
        {
            episodes.Add(CreateEpisode3());
        }
        
        manager.episodes = episodes.ToArray();
        Debug.Log($"Populated {episodes.Count} test episode(s) into StoryModeManager");
    }
    
    StoryEpisode CreateEpisode1()
    {
        StoryEpisode episode = new StoryEpisode
        {
            episodeNumber = 1,
            title = "The Tip-off Trial",
            subtitle = "Learn how robots think—through the game you love",
            codingConcept = "State",
            mathConcept = "Possession Statistics",
            aiConcept = "Vision Cues & State Detection",
            monsterName = "Shadow Press Scouts",
            gameMode = "Training",
            hasFinalExercise = true,
            spreads = new List<StorySpread>()
        };
        
        // Spread 1: Introduction
        episode.spreads.Add(new StorySpread
        {
            leftPageText = "The center circle of Data Court glowed with a soft blue light, pulsing like a heartbeat. Nova bounced on the balls of her feet, her eyes scanning the court. She could see it all—the lines of code that made up every play, the state of every possession, the flow of data like a river of information.\n\n\"Remember,\" Coach Circuit's voice crackled through their earpieces, \"the tip-off is where it all begins. One state becomes another. Start. Live. Dead. Outcome. That's the sequence. Don't let it glitch.\"",
            rightPageText = "",
            hasExercise = false,
            educationalConceptType = "coding",
            educationalHighlight = "State concept introduction"
        });
        
        // Spread 2: Action begins
        episode.spreads.Add(new StorySpread
        {
            leftPageText = "Nova nodded, her fingers twitching as if typing on an invisible keyboard. Beside her, Atlas stretched his long arms, his movements precise and calculated. Pixel adjusted his shooting sleeve, already calculating angles and percentages. And Anchor, the gentle giant, stood ready at the center circle, his massive frame a wall of protection.\n\n\"Here we go,\" Nova whispered, and the ball launched into the air.\n\nChaos erupted.",
            rightPageText = "",
            hasExercise = false,
            educationalConceptType = "coding",
            educationalHighlight = "Court layout as code structure"
        });
        
        // Spread 3: Problem introduced
        episode.spreads.Add(new StorySpread
        {
            leftPageText = "The ball bounced off Anchor's fingertips, but before Nova could react, it was gone—stolen by an opponent who moved like a shadow. The court seemed to glitch, the state of possession flickering between their team and the other side like a broken screen.\n\n\"What just happened?\" Pixel called out, his voice tight with confusion.",
            rightPageText = "",
            hasExercise = false,
            educationalConceptType = "coding",
            educationalHighlight = "State errors and debugging concepts"
        });
        
        // Spread 4: Solution approach
        episode.spreads.Add(new StorySpread
        {
            leftPageText = "Nova's eyes widened. She could see it—the state had changed too fast. START had become LIVE, but then something went wrong. The possession state was flickering, unstable, like code that hadn't been properly debugged.\n\n\"State error!\" she shouted. \"The possession changed, but the system didn't register it correctly!\"",
            rightPageText = "",
            hasExercise = false,
            educationalConceptType = "coding",
            educationalHighlight = "State transitions in action"
        });
        
        // Spread 5: Math concept
        episode.spreads.Add(new StorySpread
        {
            leftPageText = "Nova's mind raced. She had to track it. She had to count.\n\n\"Three possessions,\" she called back. \"Two turnovers. One successful—wait, no. That one ended in a shot, but it missed. So... three possessions, two turnovers, zero points.\"\n\nThe math was simple, but the problem was clear. Their turnover rate was too high.",
            rightPageText = "",
            hasExercise = false,
            educationalConceptType = "math",
            educationalHighlight = "Statistics calculation - possession count, turnover rate"
        });
        
        // Spread 6: AI collaboration
        episode.spreads.Add(new StorySpread
        {
            leftPageText = "\"Arc!\" Nova called out to their AI assistant. \"Can you detect the state shifts?\"\n\nA soft chime sounded in her earpiece. \"State shift detected,\" Arc's calm voice said. \"Current state: DEAD. Previous state: LIVE (opponent). Probability of next state: 70% LIVE (us), 30% LIVE (opponent).\"\n\nNova's eyes widened. \"Wait, you can see it?\"",
            rightPageText = "",
            hasExercise = false,
            educationalConceptType = "ai",
            educationalHighlight = "AI state detection, probability calculations, confidence scores"
        });
        
        // Spread 7: Resolution with exercise
        episode.spreads.Add(new StorySpread
        {
            leftPageText = "The ball came off the rim, and Anchor grabbed it with both hands. The state was DEAD—the shot had missed, the play was over. But Nova was already moving, already thinking ahead.\n\n\"State: DEAD,\" she called out. \"Next state: LIVE. We control this transition!\"\n\nAnchor's outlet pass was perfect—a controlled, precise throw that found Nova's hands exactly where she needed it. The state changed: DEAD → LIVE (us).",
            rightPageText = "",
            hasExercise = true,
            exerciseName = "state_tracker",
            educationalConceptType = "coding",
            educationalHighlight = "Success through proper state management"
        });
        
        return episode;
    }
    
    StoryEpisode CreateEpisode2()
    {
        StoryEpisode episode = new StoryEpisode
        {
            episodeNumber = 2,
            title = "The If/Then Fork in the Key",
            subtitle = "Master conditional logic through basketball decisions",
            codingConcept = "Conditionals",
            mathConcept = "Probability",
            aiConcept = "Decision Trees",
            monsterName = "Turnover Trolls",
            gameMode = "Prediction",
            hasFinalExercise = true,
            spreads = new List<StorySpread>()
        };
        
        // Add basic spreads for Episode 2
        episode.spreads.Add(new StorySpread
        {
            leftPageText = "Episode 2: The If/Then Fork in the Key\n\nNova faced a critical decision at the top of the key. The Turnover Trolls were closing in, and she had to choose: pass left, pass right, or drive to the basket.\n\n\"If they press left, then pass right,\" she thought. \"But if they press right, then...\"",
            rightPageText = "",
            hasExercise = false,
            educationalConceptType = "coding",
            educationalHighlight = "Conditional logic introduction"
        });
        
        return episode;
    }
    
    StoryEpisode CreateEpisode3()
    {
        StoryEpisode episode = new StoryEpisode
        {
            episodeNumber = 3,
            title = "Loop of the Rotating Guardians",
            subtitle = "Understand loops through repetitive patterns",
            codingConcept = "Loops",
            mathConcept = "Sequences",
            aiConcept = "Pattern Recognition",
            monsterName = "Rotating Guardians",
            gameMode = "Math",
            hasFinalExercise = true,
            spreads = new List<StorySpread>()
        };
        
        // Add basic spreads for Episode 3
        episode.spreads.Add(new StorySpread
        {
            leftPageText = "Episode 3: Loop of the Rotating Guardians\n\nThe Rotating Guardians moved in a perfect circle, their positions shifting in a predictable pattern. Nova watched the sequence repeat: Position 1, Position 2, Position 3, then back to Position 1.\n\n\"It's a loop,\" she realized. \"The same pattern, over and over.\"",
            rightPageText = "",
            hasExercise = false,
            educationalConceptType = "coding",
            educationalHighlight = "Loop concept introduction"
        });
        
        return episode;
    }
}

