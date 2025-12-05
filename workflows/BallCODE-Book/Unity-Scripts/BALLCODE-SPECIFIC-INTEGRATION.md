# BallCODE Game-Specific Integration Guide

Based on your game screenshots, here's how to integrate Story Mode with your existing BallCODE block-coding system.

## Understanding Your Game Structure

From the screenshots, I can see:

1. **Block Coding System:**
   - Left panel: Library of dribble moves (POUND, CROSS, BETWEEN THE LEGS, etc.)
   - Middle panel: Sequence builder (START → moves → BUCKET)
   - Visual block-code interface with drag-and-drop

2. **Ball Code & Syntax System:**
   - "Ball code" UI shows visual basketball moves
   - "Syntax" UI shows corresponding code commands (Pound(FR), Cross(R), Bucket(), etc.)
   - These are mapped together

3. **Game Modes:**
   - Grid-based basketball court
   - Robot characters that execute sequences
   - Path highlighting system

## Integration Strategy

### Episode 1: The Tip-off Trial → Training Mode

Your Training Mode should focus on **State Management** using the block-coding system:

```csharp
// Example: TrainingModeManager.cs (adapt to your actual class name)
public class TrainingModeManager : MonoBehaviour
{
    // Your existing block coding system
    public BlockCodingUI blockCodingUI;
    public BallCodeSequenceBuilder sequenceBuilder;
    public SyntaxDisplay syntaxDisplay;
    
    public void StartTraining(TrainingModeConfig config)
    {
        // Episode 1 focuses on "State" concept
        if (config.episode == 1 && config.focus == "state_tracking")
        {
            // Configure training for state management
            SetupStateTrackingExercise(config);
        }
    }
    
    void SetupStateTrackingExercise(TrainingModeConfig config)
    {
        // Pre-populate sequence with state-related blocks
        // Example: Show how states affect block execution
        
        // Clear existing sequence
        sequenceBuilder.ClearSequence();
        
        // Add START block (state: START)
        sequenceBuilder.AddBlock("START");
        
        // Add dribble blocks that demonstrate state transitions
        // State: START → LIVE
        sequenceBuilder.AddBlock("POUND", new BlockParams { state = "LIVE" });
        
        // State: LIVE → DEAD (if mistake)
        sequenceBuilder.AddBlock("CROSS", new BlockParams { state = "LIVE" });
        
        // State: LIVE → OUTCOME (if successful)
        sequenceBuilder.AddBlock("BUCKET", new BlockParams { state = "OUTCOME" });
        
        // Show state diagram overlay
        ShowStateDiagram();
        
        // Configure exercise goal
        SetExerciseGoal("Create a sequence that maintains LIVE state through 3 dribbles");
    }
    
    void OnExerciseComplete(bool success, float score)
    {
        // Notify story mode
        if (GameModeManager.Instance != null)
        {
            GameModeManager.Instance.OnExerciseComplete(success, score);
        }
    }
}
```

### Episode 2: The If/Then Fork → Prediction Mode

For conditional logic, enhance your block system with IF/THEN blocks:

```csharp
public void StartPrediction(PredictionModeConfig config)
{
    if (config.episode == 2)
    {
        // Add conditional blocks to library
        blockCodingUI.AddBlockType("IF", BlockType.Conditional);
        blockCodingUI.AddBlockType("THEN", BlockType.Conditional);
        blockCodingUI.AddBlockType("ELSE", BlockType.Conditional);
        
        // Example sequence:
        // IF opponent_presses_left
        //   THEN Cross(R)
        // ELSE Pound(FR)
        
        SetupConditionalExercise(config);
    }
}
```

### Episode 3: Loop of the Rotating Guardians → Math Mode

For loops, add loop blocks to your system:

```csharp
public void StartMathMode(MathModeConfig config)
{
    if (config.episode == 3)
    {
        // Add loop blocks
        blockCodingUI.AddBlockType("LOOP", BlockType.Loop);
        blockCodingUI.AddBlockType("REPEAT", BlockType.Loop);
        
        // Example: Loop dribble sequence 3 times
        // LOOP 3 TIMES:
        //   Pound(FR)
        //   Cross(R)
        //   BTL(FL)
        
        SetupLoopExercise(config);
    }
}
```

## Mapping Story Concepts to Your Block System

### State Management (Episode 1)

**Story teaches:** START → LIVE → DEAD → OUTCOME states

**Block system integration:**
- Add state indicators to blocks
- Show current state in UI
- Highlight state transitions
- Validate state changes in sequence

```csharp
// Example: Add state tracking to your block system
public class BallCodeBlock : MonoBehaviour
{
    public string blockType; // "POUND", "CROSS", etc.
    public string currentState; // "START", "LIVE", "DEAD", "OUTCOME"
    public string nextState; // What state this block transitions to
    
    public void Execute()
    {
        // Execute block action
        ExecuteDribbleMove(blockType);
        
        // Update state
        UpdateGameState(nextState);
    }
}
```

### Conditional Logic (Episode 2)

**Story teaches:** IF/THEN/ELSE decision trees

**Block system integration:**
- Add IF/THEN/ELSE blocks to library
- Show decision tree visualization
- Map to opponent prediction system

### Loops (Episode 3)

**Story teaches:** Repetitive patterns and sequences

**Block system integration:**
- Add LOOP/REPEAT blocks
- Show loop visualization
- Map to dribble sequences

## UI Integration Points

### Story Mode → Block Coding Transition

When player clicks "Play Exercise" in story mode:

```csharp
// In StoryModeManager.cs - TransitionToGame()
void TransitionToGame()
{
    // Hide story mode UI
    storyModeCanvas.SetActive(false);
    
    // Show block coding UI
    blockCodingUI.gameObject.SetActive(true);
    
    // Configure based on episode
    StoryEpisode episode = episodes[currentEpisode];
    
    if (episode.gameMode == "Training")
    {
        // Load Training Mode with block coding
        gameModeManager.LoadGameMode("Training", currentEpisode + 1, 
            episode.codingConcept, episode.monsterName);
    }
}
```

### Block Coding → Story Mode Return

When exercise completes:

```csharp
// In your block coding completion handler
public void OnSequenceComplete(bool success, float score)
{
    // Your existing completion logic...
    
    // Notify story mode
    if (GameModeManager.Instance != null)
    {
        GameModeManager.Instance.OnExerciseComplete(success, score);
    }
    
    // Hide block coding UI
    blockCodingUI.gameObject.SetActive(false);
    
    // Show story mode UI
    StoryModeManager storyMode = FindObjectOfType<StoryModeManager>();
    if (storyMode != null)
    {
        storyMode.storyModeCanvas.SetActive(true);
        storyMode.OnExerciseComplete(success, score);
    }
}
```

## Specific Integration for Your Game

### 1. Block Library Enhancement

Add episode-specific blocks to your "Dribbles" library:

```csharp
// When Episode 1 loads, show state-aware blocks
public void LoadEpisodeBlocks(int episode)
{
    switch (episode)
    {
        case 1: // State Management
            // All existing blocks, but with state indicators
            ShowStateIndicators(true);
            break;
            
        case 2: // Conditionals
            // Add IF/THEN/ELSE blocks
            AddConditionalBlocks();
            break;
            
        case 3: // Loops
            // Add LOOP/REPEAT blocks
            AddLoopBlocks();
            break;
    }
}
```

### 2. Sequence Builder Integration

Enhance your sequence builder to show educational concepts:

```csharp
// In your sequence builder
public class SequenceBuilder : MonoBehaviour
{
    public void AddBlockToSequence(Block block)
    {
        // Your existing add block logic...
        
        // Add educational overlay based on episode
        if (currentEpisode == 1)
        {
            ShowStateTransition(block);
        }
        else if (currentEpisode == 2)
        {
            ShowConditionalLogic(block);
        }
        else if (currentEpisode == 3)
        {
            ShowLoopPattern(block);
        }
    }
}
```

### 3. Ball Code ↔ Syntax Mapping

Your existing "Ball code" to "Syntax" mapping is perfect for story mode:

```csharp
// When story explains a concept, highlight corresponding syntax
public void HighlightConceptInSyntax(string concept)
{
    // Example: Story explains "State"
    // Highlight state-related syntax in your Syntax panel
    
    if (concept == "State")
    {
        syntaxDisplay.HighlightStateSyntax();
        // Show: Pound(FR) → state = LIVE
        //       Bucket() → state = OUTCOME
    }
}
```

## Exercise Configuration Examples

### Episode 1 Exercise: State Tracker

```csharp
TrainingModeConfig config = new TrainingModeConfig
{
    episode = 1,
    codingConcept = "State",
    monster = "Shadow Press Scouts",
    focus = "state_tracking"
};

// Exercise goal: Create sequence that maintains LIVE state
// Pre-populate: START block
// Challenge: Add 3 dribble blocks that keep state as LIVE
// Success: Sequence executes without state errors
```

### Episode 2 Exercise: Conditional Predictor

```csharp
PredictionModeConfig config = new PredictionModeConfig
{
    episode = 2,
    codingConcept = "Conditionals",
    monster = "Turnover Trolls",
    difficulty = "beginner"
};

// Exercise goal: Use IF/THEN to predict opponent
// Pre-populate: IF opponent_presses_left
// Challenge: Add THEN/ELSE blocks with correct moves
// Success: Correct prediction and execution
```

### Episode 3 Exercise: Loop Sequence

```csharp
MathModeConfig config = new MathModeConfig
{
    episode = 3,
    codingConcept = "Loops",
    monster = "Rotating Guardians",
    focus = "dribbles"
};

// Exercise goal: Create loop for repeating pattern
// Pre-populate: LOOP 3 TIMES block
// Challenge: Add dribble sequence inside loop
// Success: Loop executes correctly 3 times
```

## Visual Integration

### Story Mode UI Overlay

Consider showing story mode as an overlay on top of your game:

```csharp
// Story mode canvas as overlay
Canvas storyCanvas = storyModeCanvas.GetComponent<Canvas>();
storyCanvas.renderMode = RenderMode.ScreenSpaceOverlay;
storyCanvas.sortingOrder = 100; // Above game UI

// When story mode is active, dim game behind it
// When exercise starts, hide story, show game
```

### State Diagram Overlay

For Episode 1, add a state diagram overlay to your game:

```csharp
// Show state diagram when Episode 1 exercise loads
public void ShowStateDiagram()
{
    stateDiagramUI.SetActive(true);
    // Display: START → LIVE → DEAD → OUTCOME
    // Highlight current state as blocks execute
}
```

## Testing Checklist

- [ ] Story mode appears over game
- [ ] "Play Exercise" button transitions to block coding
- [ ] Block coding UI shows episode-specific blocks
- [ ] Sequence builder accepts episode configuration
- [ ] Ball code ↔ Syntax mapping works with story concepts
- [ ] Exercise completion returns to story mode
- [ ] State indicators work (Episode 1)
- [ ] Conditional blocks work (Episode 2)
- [ ] Loop blocks work (Episode 3)

## Next Steps

1. **Identify your block coding manager class** - What's the actual class name?
2. **Find your sequence builder** - How does it currently work?
3. **Locate your Ball code/Syntax system** - Where is this implemented?
4. **Test Episode 1 integration** - Start with state management
5. **Add Episode 2/3 blocks** - Conditionals and loops

Share your actual class names and I can provide more specific code!

