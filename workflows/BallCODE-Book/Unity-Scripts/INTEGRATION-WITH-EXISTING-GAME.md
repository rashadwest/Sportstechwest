# Integrating Story Mode with Your Existing BallCODE Game

This guide helps you connect the Story Mode scripts to your existing BallCODE Unity game repository.

## Step 1: Understand Your Current Game Structure

Before integrating, identify these components in your existing game:

### Key Components to Find

1. **Game Mode Managers:**
   - Do you have a `TrainingModeManager` or similar?
   - Do you have a `PredictionModeManager` or opponent prediction system?
   - Do you have a `MathModeManager` or math-based gameplay?
   - Do you have a `BlockCodingManager` or drag-and-drop coding system?

2. **Scene Structure:**
   - What scenes do you currently have?
   - Is there a main menu scene?
   - Are game modes in separate scenes or all in one scene?

3. **Game State Management:**
   - How do you currently handle game state?
   - Do you have a singleton manager pattern?
   - How do you transition between game modes?

## Step 2: Copy Story Mode Scripts

1. **Copy all scripts from `Unity-Scripts/` to your Unity project:**
   ```
   YourUnityProject/
   └── Assets/
       └── Scripts/
           └── StoryMode/
               ├── StoryModeManager.cs
               ├── StoryData.cs
               ├── GameModeManager.cs
               ├── StoryEpisodeCreator.cs
               ├── BallCODEStarter.cs
               └── TestStoryDataHelper.cs
   ```

2. **Unity will auto-compile** - check Console for any errors

## Step 3: Adapt GameModeManager to Your Structure

The `GameModeManager.cs` expects these game mode managers. You need to either:

### Option A: Your Managers Already Exist

If you already have managers with different names, update `GameModeManager.cs`:

```csharp
// In GameModeManager.cs, change these lines:
[Header("Game Mode Scenes/Managers")]
public YourTrainingManager trainingMode;  // Change from TrainingModeManager
public YourPredictionManager predictionMode;  // Change from PredictionModeManager
public YourMathManager mathMode;  // Change from MathModeManager
public YourBlockCodingManager blockCodingMode;  // Change from BlockCodingManager
```

Then update the `LoadTrainingMode`, `LoadPredictionMode`, etc. methods to call your existing manager methods.

### Option B: Create Adapter Scripts

If your game structure is very different, create adapter scripts that bridge the story mode to your game:

```csharp
// Example: TrainingModeAdapter.cs
public class TrainingModeAdapter : MonoBehaviour
{
    public YourExistingGameManager gameManager;
    
    public void StartTraining(TrainingModeConfig config)
    {
        // Convert story config to your game's format
        YourGameConfig gameConfig = new YourGameConfig
        {
            episode = config.episode,
            concept = config.codingConcept,
            // ... map other fields
        };
        
        // Call your existing game manager
        gameManager.StartGame(gameConfig);
    }
}
```

## Step 4: Connect Your Game Modes

### For Training Mode (Episode 1)

Your training mode needs to accept configuration from the story:

```csharp
// In your TrainingModeManager (or adapter)
public void StartTraining(TrainingModeConfig config)
{
    // Use config.episode to load episode-specific content
    // Use config.codingConcept to focus on "State" concept
    // Use config.monster to set the opponent (Shadow Press Scouts)
    // Use config.focus to set training focus ("state_tracking")
    
    // Start your training mode
    // When complete, call:
    GameModeManager.Instance.OnExerciseComplete(success, score);
}
```

### For Prediction Mode (Episode 2)

```csharp
// In your PredictionModeManager
public void StartPrediction(PredictionModeConfig config)
{
    // Use config to set up conditional logic exercises
    // Focus on "Conditionals" concept
    // When complete, call:
    GameModeManager.Instance.OnExerciseComplete(success, score);
}
```

### For Math Mode (Episode 3)

```csharp
// In your MathModeManager
public void StartMathMode(MathModeConfig config)
{
    // Use config to set up loop/sequence exercises
    // Focus on "Loops" concept
    // When complete, call:
    GameModeManager.Instance.OnExerciseComplete(success, score);
}
```

## Step 5: Handle Exercise Completion

When a player completes an exercise in your game, notify the story mode:

```csharp
// In your game mode's completion handler
public void OnExerciseComplete(bool success, float score)
{
    // Your existing completion logic here...
    
    // Notify story mode
    if (GameModeManager.Instance != null)
    {
        GameModeManager.Instance.OnExerciseComplete(success, score);
    }
    
    // Return to story mode or show results
}
```

## Step 6: Scene Setup Options

### Option A: Story Mode in Separate Scene

1. Create new scene: `StoryModeScene`
2. Set up UI (see `UNITY-SETUP-GUIDE.md`)
3. Use `SceneManager.LoadScene()` to transition

### Option B: Story Mode in Same Scene

1. Add Story Mode UI Canvas to your main scene
2. Show/hide canvas based on mode
3. Use `storyModeCanvas.SetActive(true/false)` to toggle

### Option C: Story Mode as Overlay

1. Add Story Mode Canvas to your main scene
2. Set Canvas Render Mode to "Screen Space - Overlay"
3. Show/hide as needed without scene changes

## Step 7: URL Parameter Support (WebGL)

If your game is WebGL, the story mode scripts already support URL parameters:

- `ballcode.co/story?episode=1` → Opens Episode 1
- `ballcode.co/story?episode=2` → Opens Episode 2
- `ballcode.co/play?mode=training&episode=1` → Direct to game mode

The `BallCODEStarter.cs` and `StoryModeManager.cs` handle this automatically.

## Step 8: Testing Integration

### Test Story → Game Flow

1. Start story mode
2. Navigate to a spread with `hasExercise = true`
3. Click "Play Exercise" button
4. Verify your game mode loads with correct parameters
5. Complete exercise
6. Verify return to story mode

### Test Game → Story Flow

1. Start from game mode
2. Complete exercise
3. Call `GameModeManager.Instance.OnExerciseComplete()`
4. Verify story mode appears
5. Verify next spread/episode unlocks

## Common Integration Patterns

### Pattern 1: Scene-Based Game Modes

If your game modes are in separate scenes:

```csharp
// In GameModeManager.cs
void LoadTrainingMode(int episode, string concept, string monster)
{
    // Store config for next scene
    PlayerPrefs.SetInt("StoryEpisode", episode);
    PlayerPrefs.SetString("StoryConcept", concept);
    
    // Load training scene
    SceneManager.LoadScene("TrainingScene");
}

// In your TrainingScene's manager
void Start()
{
    // Read config
    int episode = PlayerPrefs.GetInt("StoryEpisode", 1);
    string concept = PlayerPrefs.GetString("StoryConcept", "");
    
    // Configure training mode
    StartTraining(episode, concept);
}
```

### Pattern 2: Single Scene with Mode Switching

If all modes are in one scene:

```csharp
// In GameModeManager.cs
void LoadTrainingMode(int episode, string concept, string monster)
{
    // Hide story mode UI
    storyModeManager.storyModeCanvas.SetActive(false);
    
    // Show training mode UI
    trainingMode.gameObject.SetActive(true);
    
    // Configure and start
    trainingMode.StartTraining(new TrainingModeConfig { ... });
}
```

### Pattern 3: Event-Based System

If you use events:

```csharp
// Create event
public static event Action<TrainingModeConfig> OnTrainingModeRequested;

// In GameModeManager.cs
void LoadTrainingMode(int episode, string concept, string monster)
{
    var config = new TrainingModeConfig { ... };
    OnTrainingModeRequested?.Invoke(config);
}

// In your TrainingModeManager
void OnEnable()
{
    GameModeManager.OnTrainingModeRequested += HandleTrainingRequest;
}

void HandleTrainingRequest(TrainingModeConfig config)
{
    StartTraining(config);
}
```

## Troubleshooting

### "GameModeManager not found"
- Ensure `GameModeManager` GameObject exists in scene
- Check that `DontDestroyOnLoad` is working if using scene transitions
- Verify singleton pattern is set up correctly

### "TrainingModeManager not assigned"
- Assign your training mode manager in Inspector
- Or create an adapter script if your manager has a different name

### Story mode doesn't appear
- Check that `StoryModeCanvas` is active
- Verify `StoryModeManager` has episodes assigned
- Check Console for errors

### Game mode doesn't load
- Verify your game mode managers implement the required methods
- Check that configuration is being passed correctly
- Add debug logs to trace the flow

## Next Steps

1. **Identify your game mode managers** - Find them in your codebase
2. **Create adapters if needed** - Bridge story mode to your game structure
3. **Test integration** - Start with Episode 1 → Training Mode
4. **Iterate** - Adjust based on your specific game architecture

## Need More Help?

If you can share:
- Your game mode manager scripts (or their structure)
- Your scene setup approach
- Any specific integration challenges

I can provide more targeted guidance!

