# BallCODE Unity Scripts

Complete Unity integration for BallCODE Story Mode system.

## 📁 Files

### Core Scripts

- **`StoryModeManager.cs`** - Main story mode controller
  - Handles page turning, audio narration, game mode transitions
  - Manages story episode progression
  - Supports URL parameter deep linking (for QR codes)

- **`StoryData.cs`** - Data structures
  - `StoryEpisode` - Complete episode data with spreads
  - `StorySpread` - Two-page layout (left/right pages)
  - `SkillPitStopData` - Educational content structure
  - Code, Math, and AI example structures

- **`GameModeManager.cs`** - Integration layer
  - Maps story episodes to game modes
  - Handles parameter passing to game modes
  - Manages completion callbacks
  - Singleton pattern for easy access

- **`StoryEpisodeCreator.cs`** - Editor tool
  - Creates ScriptableObject assets for story episodes
  - Menu: `BallCODE → Create Story Episode`
  - Makes it easy to create and edit episode data

- **`BallCODEStarter.cs`** - Setup and initialization
  - Main entry point for BallCODE system
  - Handles scene setup and component connections
  - Supports auto-start for testing
  - URL parameter parsing for WebGL builds

## 🚀 Quick Start

1. **Copy scripts to your Unity project:**
   ```
   Assets/Scripts/StoryMode/
   ```

2. **Follow the setup guide:**
   - See `UNITY-SETUP-GUIDE.md` for detailed instructions

3. **Create story episodes:**
   - Use `StoryEpisodeCreator` editor tool
   - Or create ScriptableObject assets manually

4. **Connect to your game modes:**
   - Assign game mode managers to `GameModeManager`
   - Implement configuration interfaces

## 📖 Documentation

- **`UNITY-SETUP-GUIDE.md`** - Complete setup instructions
- **`StoryModeIntegration.md`** - Integration architecture
- **`Story-Mode-Complete-Summary.md`** - Feature overview

## 🎮 Game Mode Mapping

| Episode | Story Title | Game Mode | Concept Taught |
|---------|------------|-----------|----------------|
| 1 | The Tip-off Trial | Training Mode | State Management |
| 2 | The If/Then Fork | Opponent Prediction | Conditional Logic |
| 3 | Loop of the Rotating Guardians | Math Version | Loops & Sequences |

## 🔗 Integration Flow

```
Physical Book QR Code
    ↓
ballcode.co/story?episode=1
    ↓
Unity Story Mode (Episode 1)
    ↓
Read story with audio narration
    ↓
"Play Exercise" button appears
    ↓
Transition to Game Mode
    ↓
Complete exercise
    ↓
Return to Story Mode
    ↓
Unlock next spread/episode
```

## 💡 Key Features

- ✅ Page-turner interface with animations
- ✅ Audiobook narration (syncs with pages)
- ✅ Deep linking from QR codes (WebGL)
- ✅ Progress tracking
- ✅ Seamless game mode transitions
- ✅ Return flow after exercise completion
- ✅ Educational concept tracking (coding, math, AI)

## 🛠️ Requirements

- Unity 2021.3 or later
- TextMeshPro (for UI text)
- Audio Source component (for narration)

## 📝 Usage Example

```csharp
// Enter story mode programmatically
StoryModeManager storyMode = FindObjectOfType<StoryModeManager>();
storyMode.EnterStoryMode(0); // Episode 1

// Load game mode from story
GameModeManager.Instance.LoadGameMode(
    "Training",      // Game mode name
    1,               // Episode number
    "State",         // Coding concept
    "Shadow Press"   // Monster name
);

// Notify completion
GameModeManager.Instance.OnExerciseComplete(true, 100f);
```

## 🎯 Next Steps

1. Set up Unity scene (see `UNITY-SETUP-GUIDE.md`)
2. Create story episode data
3. Connect to your existing game modes
4. Test end-to-end flow
5. Generate QR codes for physical book

## 📞 Support

For questions or issues:
- Review the setup guide
- Check script comments
- Verify Inspector references
- Check Unity Console for errors

