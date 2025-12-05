# BallCODE Unity Setup Guide

## Quick Start

This guide will help you set up the BallCODE Story Mode system in your Unity project.

## Step 1: Copy Scripts to Your Unity Project

1. Copy all scripts from `Unity-Scripts/` folder to your Unity project:
   ```
   Assets/
   └── Scripts/
       └── StoryMode/
           ├── StoryModeManager.cs
           ├── StoryData.cs
           ├── GameModeManager.cs
           ├── StoryEpisodeCreator.cs
           └── BallCODEStarter.cs
   ```

2. Unity will automatically compile the scripts.

## Step 2: Create Story Mode Scene

1. **Create New Scene:**
   - File → New Scene → Basic (Built-in)
   - Save as: `StoryModeScene`

2. **Set Up Main Objects:**
   - Create empty GameObject: `BallCODEStarter`
   - Add `BallCODEStarter` component
   - Create empty GameObject: `StoryModeManager`
   - Add `StoryModeManager` component
   - Create empty GameObject: `GameModeManager`
   - Add `GameModeManager` component

3. **Create UI Canvas:**
   - GameObject → UI → Canvas
   - Name it: `StoryModeCanvas`
   - Set Canvas Scaler to "Scale With Screen Size"
   - Reference Resolution: 1920x1080

## Step 3: Set Up Story Mode UI

### Create Page Turner Container

1. **Create Container:**
   - Right-click `StoryModeCanvas` → UI → Panel
   - Name: `PageTurnerContainer`
   - Add `CanvasGroup` component (for fade effects)

2. **Left Page:**
   - Right-click `PageTurnerContainer` → UI → Panel
   - Name: `LeftPage`
   - Add child: UI → Image (for character art)
     - Name: `LeftPageImage`
   - Add child: UI → Text - TextMeshPro (for story text)
     - Name: `LeftPageText`
     - Set font size: 18-24
     - Set alignment: Top-Left
     - Enable word wrap

3. **Right Page:**
   - Right-click `PageTurnerContainer` → UI → Panel
   - Name: `RightPage`
   - Add child: UI → Image (for diagrams)
     - Name: `RightPageImage`
   - Add child: UI → Text - TextMeshPro (for code examples)
     - Name: `RightPageText`
     - Set font size: 16-20
     - Set alignment: Top-Left

### Create Navigation Panel

1. **Navigation Container:**
   - Right-click `StoryModeCanvas` → UI → Panel
   - Name: `NavigationPanel`
   - Position at bottom of screen

2. **Buttons:**
   - Right-click `NavigationPanel` → UI → Button - TextMeshPro
     - Name: `PreviousButton`
     - Text: "← Previous"
   - Right-click `NavigationPanel` → UI → Button - TextMeshPro
     - Name: `NextButton`
     - Text: "Next →"
   - Right-click `NavigationPanel` → UI → Button - TextMeshPro
     - Name: `PlayExerciseButton`
     - Text: "Play Exercise"
     - Initially set inactive (will show on exercise spreads)

3. **Page Indicator:**
   - Right-click `NavigationPanel` → UI → Text - TextMeshPro
   - Name: `PageIndicator`
   - Text: "Page 1 of 6"
   - Center align

### Create Audio Controls (Optional)

1. **Audio Panel:**
   - Right-click `StoryModeCanvas` → UI → Panel
   - Name: `AudioControls`
   - Position at top-right

2. **Audio Components:**
   - Add `AudioSource` component to `StoryModeManager` GameObject
   - Create Play/Pause button in `AudioControls` panel

## Step 4: Connect References in Inspector

1. **Select `StoryModeManager` GameObject:**
   - Drag `StoryModeCanvas` to "Story Mode Canvas"
   - Drag `PageTurnerContainer` to "Page Turner Container"
   - Drag `LeftPageImage` to "Left Page Image"
   - Drag `RightPageImage` to "Right Page Image"
   - Drag `LeftPageText` to "Left Page Text"
   - Drag `RightPageText` to "Right Page Text"
   - Drag `NextButton` to "Next Page Button"
   - Drag `PreviousButton` to "Previous Page Button"
   - Drag `PlayExerciseButton` to "Play Exercise Button"
   - Drag `PageIndicator` to "Page Indicator"
   - Drag `AudioSource` component to "Narration Source"

2. **Select `GameModeManager` GameObject:**
   - Assign your game mode managers:
     - Training Mode Manager
     - Prediction Mode Manager
     - Math Mode Manager
     - Block Coding Manager (if exists)

3. **Select `BallCODEStarter` GameObject:**
   - Drag `StoryModeManager` to "Story Mode Manager"
   - Drag `GameModeManager` to "Game Mode Manager"
   - Set "Story Mode Scene Name" if using separate scene
   - Enable "Auto Start Story Mode" for testing

## Step 5: Create Story Episode Data

### Option A: Using ScriptableObject (Recommended)

1. **Open Editor Tool:**
   - Menu: BallCODE → Create Story Episode
   - Fill in episode information
   - Click "Create Episode Asset"

2. **Create Episode Assets:**
   - Right-click in Project → Create → BallCODE → Story Episode
   - Name: `Episode1`, `Episode2`, `Episode3`
   - Fill in all fields in Inspector

3. **Assign to StoryModeManager:**
   - Select `StoryModeManager`
   - Set "Episodes" array size to 3
   - Drag `Episode1`, `Episode2`, `Episode3` assets to array

### Option B: Create Runtime Data (For Testing)

You can create StoryEpisode data directly in code for quick testing:

```csharp
// Create a test script to populate episodes
public class TestStoryData : MonoBehaviour
{
    void Start()
    {
        StoryModeManager manager = FindObjectOfType<StoryModeManager>();
        if (manager != null)
        {
            manager.episodes = CreateTestEpisodes();
        }
    }
    
    StoryEpisode[] CreateTestEpisodes()
    {
        // Create Episode 1
        StoryEpisode episode1 = new StoryEpisode
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
        
        // Add spreads to episode1.spreads...
        
        return new StoryEpisode[] { episode1 };
    }
}
```

## Step 6: Set Up Audio (Optional)

1. **Import Audio Files:**
   - Create folder: `Assets/StoryContent/Audio/Episode1/`
   - Import narration audio files
   - Name them: `episode1_spread1.mp3`, `episode1_spread2.mp3`, etc.

2. **Assign Audio Clips:**
   - Select `StoryModeManager`
   - Set "Episode 1 Audio Clips" array size to number of spreads
   - Drag audio clips to array

## Step 7: Connect Game Modes

Your game mode managers need to implement these interfaces:

### TrainingModeManager Example

```csharp
public class TrainingModeManager : MonoBehaviour
{
    public void StartTraining(TrainingModeConfig config)
    {
        // Configure training mode based on story episode
        Debug.Log($"Starting Training Mode for Episode {config.episode}");
        Debug.Log($"Teaching: {config.codingConcept}");
        Debug.Log($"Monster: {config.monster}");
        Debug.Log($"Focus: {config.focus}");
        
        // Start your training mode here
        // When complete, call:
        // GameModeManager.Instance.OnExerciseComplete(success, score);
    }
}
```

### Completion Callback

When exercise completes, notify the story mode:

```csharp
// In your game mode manager
public void OnExerciseComplete(bool success, float score)
{
    GameModeManager.Instance.OnExerciseComplete(success, score);
}
```

## Step 8: Test the System

1. **Test Story Mode:**
   - Play the scene
   - If "Auto Start Story Mode" is enabled, story should appear
   - Test page navigation (Previous/Next buttons)
   - Test audio playback (if set up)

2. **Test Game Mode Transition:**
   - Navigate to a spread with `hasExercise = true`
   - Click "Play Exercise" button
   - Verify game mode loads with correct parameters
   - Complete exercise and verify return to story

3. **Test URL Parameters (WebGL):**
   - Build as WebGL
   - Test URL: `yourgame.com/story?episode=1`
   - Verify correct episode loads

## Troubleshooting

### Story Mode Not Appearing
- Check that `StoryModeCanvas` is active
- Verify `StoryModeManager` has episodes assigned
- Check console for errors

### Buttons Not Working
- Verify button references are assigned in Inspector
- Check that `SetupUI()` is called in `StoryModeManager.Start()`

### Game Mode Not Loading
- Verify `GameModeManager` has game mode managers assigned
- Check that game mode managers implement the required methods
- Verify episode-to-game-mode mapping in `GameModeManager`

### Audio Not Playing
- Check that `AudioSource` is assigned
- Verify audio clips are assigned to correct episode arrays
- Check audio clip import settings (should be "Audio Clip" type)

## Next Steps

1. **Create Story Content:**
   - Write Episode 1-3 story text
   - Create visual assets (character art, diagrams)
   - Record audiobook narration

2. **Integrate with Your Game:**
   - Update game mode managers to accept story configuration
   - Implement completion callbacks
   - Test end-to-end flow

3. **Add QR Code Support:**
   - Generate QR codes for each episode
   - Test deep linking from physical book
   - Verify URL parameter parsing

4. **Polish UI:**
   - Add page turn animations
   - Enhance audio controls
   - Add progress tracking UI

## File Structure Summary

```
Assets/
├── Scripts/
│   └── StoryMode/
│       ├── StoryModeManager.cs
│       ├── StoryData.cs
│       ├── GameModeManager.cs
│       ├── StoryEpisodeCreator.cs
│       └── BallCODEStarter.cs
├── StoryContent/
│   ├── Episodes/
│   │   ├── Episode1.asset
│   │   ├── Episode2.asset
│   │   └── Episode3.asset
│   └── Audio/
│       ├── Episode1/
│       ├── Episode2/
│       └── Episode3/
└── Scenes/
    ├── StoryModeScene.unity
    └── MainGameScene.unity
```

## Support

If you encounter issues:
1. Check Unity Console for errors
2. Verify all references are assigned in Inspector
3. Review the script comments for usage notes
4. Check that your game mode managers implement required interfaces

