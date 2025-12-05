# Story Mode Integration Guide

## Overview

This document explains how to integrate the Story Mode system into your Unity BallCODE game.

## File Structure

```
Assets/
├── Scripts/
│   ├── StoryMode/
│   │   ├── StoryModeManager.cs
│   │   ├── StoryData.cs
│   │   └── GameModeManager.cs
│   ├── GameModes/
│   │   ├── TrainingModeManager.cs
│   │   ├── PredictionModeManager.cs
│   │   └── MathModeManager.cs
│   └── ...
├── StoryContent/
│   ├── Episodes/
│   │   ├── Episode1.asset (ScriptableObject)
│   │   ├── Episode2.asset
│   │   └── Episode3.asset
│   └── Audio/
│       ├── Episode1/
│       ├── Episode2/
│       └── Episode3/
└── UI/
    └── StoryMode/
        └── StoryModeCanvas.prefab
```

## Setup Instructions

### 1. Create Story Mode Scene

1. Create new scene: `StoryModeScene`
2. Add empty GameObject: `StoryModeManager`
3. Attach `StoryModeManager` script
4. Create UI Canvas: `StoryModeCanvas`
5. Set up UI elements (see UI Layout below)

### 2. Configure Story Episodes

1. Create ScriptableObject assets for each episode:
   - Right-click in Project → Create → Story Episode
   - Fill in episode data (title, spreads, etc.)
2. Assign episode assets to `StoryModeManager.episodes` array

### 3. Set Up Audio

1. Import audio files for narration
2. Organize by episode: `Audio/Episode1/`, `Episode2/`, etc.
3. Assign audio clips to `StoryModeManager`:
   - `episode1AudioClips[]`
   - `episode2AudioClips[]`
   - `episode3AudioClips[]`

### 4. Connect Game Modes

1. Ensure your game mode managers exist:
   - `TrainingModeManager`
   - `PredictionModeManager`
   - `MathModeManager`
2. Assign them to `GameModeManager` in inspector
3. Implement the configuration interfaces

## UI Layout

### Story Mode Canvas Structure

```
StoryModeCanvas
├── PageTurnerContainer
│   ├── LeftPage
│   │   ├── LeftPageImage (Image)
│   │   └── LeftPageText (Text)
│   └── RightPage
│       ├── RightPageImage (Image)
│       └── RightPageText (Text)
├── NavigationPanel
│   ├── PreviousButton
│   ├── NextButton
│   └── PageIndicator (Text)
├── AudioControls
│   ├── PlayPauseButton
│   └── ProgressSlider
└── ExerciseButton
```

## Episode-to-Game Mode Mapping

### Episode 1: The Tip-off Trial → Training Mode
- **Story teaches:** State management, position analysis
- **Game mode:** Training Mode
- **Focus:** Watch footage → Analyze robot positioning → Correct mistakes

### Episode 2: The If/Then Fork → Opponent Prediction
- **Story teaches:** Conditional logic, decision trees
- **Game mode:** Opponent Prediction
- **Focus:** Predict opponent behavior using if/then logic

### Episode 3: Loop of the Rotating Guardians → Math Version
- **Story teaches:** Loops, sequences, patterns
- **Game mode:** Math Version
- **Focus:** Number system for dribbles, repetitive patterns

## Integration Points

### From Story to Game

```csharp
// In StoryModeManager.TransitionToGame()
gameModeManager.LoadGameMode(
    "Training",           // Game mode name
    currentEpisode + 1,   // Episode number
    episode.codingConcept, // Concept being taught
    episode.monsterName    // Story monster
);
```

### From Game to Story

```csharp
// In your game mode manager, when exercise completes:
GameModeManager.Instance.OnExerciseComplete(success, score);
```

## URL Parameter Support (WebGL)

For physical book QR codes:
- `ballcode.co/story?episode=1` → Opens Episode 1
- `ballcode.co/story?episode=2` → Opens Episode 2
- `ballcode.co/story?episode=3` → Opens Episode 3

The `StoryModeManager` automatically checks URL parameters on start.

## Next Steps

1. **Create Story Content**
   - Write Episode 1-3 story text
   - Create visual assets (character art, diagrams)
   - Record audiobook narration

2. **Implement Game Mode Interfaces**
   - Update your game mode managers to accept configuration
   - Implement completion callbacks

3. **Test Integration**
   - Test story → game transitions
   - Test game → story return flow
   - Test progress tracking

4. **Create Physical Book**
   - Design book layout
   - Generate QR codes
   - Print physical version




