# BallCODE Game Architecture - Complete Documentation

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** November 26, 2025  
**Status:** Complete Architecture Documentation  
**Purpose:** Full understanding of Unity game structure for book integration

---

## Game Overview

BallCODE is a Unity-based educational game that teaches AI, Math, and Coding concepts through basketball. The game supports multiple modes, exercise types, and integrates with story content.

---

## Core Architecture Components

### 1. Entry Point System

**BallCODEStarter.cs** - Main entry point for the game
- **Purpose:** Handles initialization, scene setup, URL parameter parsing
- **Key Features:**
  - Auto-start options for testing
  - URL parameter parsing for WebGL builds
  - Connects StoryModeManager to GameModeManager
  - Supports deep linking via URL parameters

**URL Parameter Support:**
- `story?episode=N` - Loads story mode for specific episode
- `play?mode=X&episode=N` - Loads game mode with episode context
- Currently supports: `episode` parameter
- **Needs Extension:** Add `book` and `exercise` parameters

---

### 2. Story Mode System

**StoryModeManager.cs** - Manages story reading experience
- **Purpose:** Handles page turning, audio narration, transitions to game modes
- **Key Features:**
  - Page turner interface (left/right pages)
  - Audio narration player
  - Exercise integration buttons
  - Progress tracking
  - Episode-to-game mode mapping

**Current Episode Mapping:**
- Episode 1 (index 0) → Training Mode
- Episode 2 (index 1) → Prediction Mode
- Episode 3 (index 2) → Math Mode

**Story Data Structure:**
- `StoryEpisode` - Contains episode data with spreads
- `StorySpread` - Two-page layout (left/right pages)
- `SkillPitStopData` - Educational content structure

**Integration Points:**
- `PlayExercise()` - Transitions to game mode
- `OnExerciseComplete()` - Handles return from game
- `TransitionToGame()` - Loads appropriate game mode

---

### 3. Game Mode Management

**GameModeManager.cs** - Manages transitions between story and game modes
- **Purpose:** Handles parameter passing, exercise configuration, completion callbacks
- **Key Features:**
  - Singleton pattern (DontDestroyOnLoad)
  - Supports multiple game modes
  - LevelData-based loading
  - Metrics collection integration

**Supported Game Modes:**
1. **Training Mode** (`training`)
   - Manager: `TrainingModeManager`
   - Focus: State tracking, position analysis
   - Episode 1 mapping

2. **Prediction Mode** (`prediction`)
   - Manager: `PredictionModeManager`
   - Focus: Opponent behavior prediction
   - Episode 2 mapping

3. **Math Mode** (`math`)
   - Manager: `MathModeManager`
   - Focus: Math-based calculations
   - Episode 3 mapping

4. **Block Coding Mode** (`blockcoding`)
   - Manager: `BlockCodingManager`
   - Focus: Drag-and-drop code blocks
   - Future episodes

5. **Freeplay Mode** (`freeplay`)
   - Manager: None specified
   - Focus: Open-ended exploration
   - Available but needs implementation

**Loading Methods:**
- `LoadGameMode(mode, episode, codingConcept, monster)` - Episode-based loading
- `LoadGameModeFromLevel(levelId)` - LevelData-based loading (preferred)

**Configuration Classes:**
- `TrainingModeConfig` - Training mode parameters
- `PredictionModeConfig` - Prediction mode parameters
- `MathModeConfig` - Math mode parameters
- `BlockCodingConfig` - Block coding parameters

**Completion Flow:**
- `OnExerciseComplete(success, score)` - Called when exercise finishes
- Notifies StoryModeManager to return to story
- Tracks metrics via MetricsCollector

---

### 4. Level Data System

**LevelData.cs** - Data structure for video/strategy-based levels
- **Purpose:** Define levels using videos and basketball strategies
- **Key Features:**
  - Video configuration
  - Strategy data
  - Exercise configuration
  - Learning objectives
  - Difficulty and progression

**LevelData Structure:**
```csharp
- levelId: Unique identifier
- levelName: Display name
- gameMode: Which game mode (training, prediction, math, blockcoding, freeplay)
- episodeNumber: Associated episode (0-based)
- codingConcept: Concept taught (e.g., "state", "conditionals", "loops")
- videoPath: Path to video file
- videoConfig: Video playback settings
- strategy: Basketball strategy/play data
- exercise: Exercise-specific configuration
- learningObjectives: What students will learn
- difficultyLevel: 1-5 difficulty rating
- prerequisiteLevels: Level IDs that must be completed first
```

**Exercise Types:**
1. **BlockCoding** - Drag and drop code blocks
2. **Analysis** - Analyze video/strategy
3. **Prediction** - Predict opponent behavior
4. **Math** - Math-based calculations
5. **Freeplay** - Open-ended exploration

**Exercise Configuration:**
- `BlockCodingExercise` - Available blocks, required blocks, target code
- `AnalysisExercise` - Number of questions, time limits
- `PredictionExercise` - Number of predictions, prediction window
- `MathExercise` - Math concept, number of problems
- `ScoringConfig` - Max score, passing score, retry options

---

### 5. Level Data Manager

**LevelDataManager.cs** - Manages loading and accessing level data
- **Purpose:** Load levels from JSON files and StreamingAssets
- **Key Features:**
  - Singleton pattern
  - Loads from TextAsset JSON files
  - Loads from StreamingAssets folder
  - Organizes levels by mode, episode, concept
  - Prerequisite checking

**Organization:**
- `allLevels` - Dictionary by levelId
- `levelsByMode` - Dictionary by game mode
- `levelsByEpisode` - Dictionary by episode number
- `levelsByConcept` - Dictionary by coding concept

**Key Methods:**
- `GetLevel(levelId)` - Get level by ID
- `GetLevelsForMode(gameMode)` - Get all levels for a mode
- `GetLevelsForEpisode(episodeNumber)` - Get all levels for an episode
- `GetLevelsForConcept(codingConcept)` - Get all levels for a concept
- `IsLevelUnlocked(levelId, completedLevels)` - Check prerequisites

---

### 6. AIMCODE Level Generator

**AIMCODELevelGenerator.cs** - Automated level generation system
- **Purpose:** Generate levels from videos and strategies using AIMCODE principles
- **Key Features:**
  - Automatic level generation
  - AIMCODE methodology integration
  - Batch generation support
  - JSON export

**AIMCODE Principles Applied:**
- **Zhang (Basketball Framework):** Strategy provides basketball context
- **Hassabis (Systematic Building):** Prerequisites based on episode progression
- **Resnick (Building Activities):** Configures hands-on exercises
- **Reggio (Multiple Entry Points):** Ensures video, strategy, exercise available
- **Jobs (Simplicity):** Validates and simplifies configuration

**Generation Method:**
- `GenerateLevelFromInputs()` - Main generation method
- Takes: levelName, videoPath, strategy, gameMode, episodeNumber, codingConcept, exerciseType
- Returns: Complete LevelData object

---

### 7. Metrics Collection

**MetricsCollector.cs** - Build-Measure-Learn feedback loop system
- **Purpose:** Track story engagement, game performance, integration metrics
- **Key Features:**
  - Singleton pattern
  - Story metrics tracking
  - Game metrics tracking
  - Transition event tracking
  - JSON file persistence

**Story Metrics:**
- `OnStoryPageView()` - Track page views and time spent
- `OnPlayExerciseClick()` - Track "Play Exercise" button clicks
- `OnEpisodeComplete()` - Track episode completion
- `OnReturnToStory()` - Track return from game

**Game Metrics:**
- `OnGameModeStart()` - Track game mode start
- `OnExerciseAttempt()` - Track exercise attempts
- `OnExerciseComplete()` - Track exercise completion
- `OnExerciseFailed()` - Track exercise failures

**Data Structures:**
- `MetricsData` - Session data
- `StoryMetrics` - Episode-level story metrics
- `GameMetrics` - Episode-level game metrics
- `TransitionEvent` - Story↔Game transition events

---

## Integration Capabilities

### Current Integration Points

1. **URL Parameters (WebGL)**
   - `story?episode=N` - Story mode deep linking
   - `play?mode=X&episode=N` - Game mode with episode
   - **Extension Needed:** `book` and `exercise` parameters

2. **Story → Game Transition**
   - StoryModeManager calls GameModeManager.LoadGameMode()
   - Passes episode, coding concept, monster name
   - Game mode loads with context

3. **Game → Story Return**
   - GameModeManager.OnExerciseComplete() called
   - Notifies StoryModeManager
   - Returns to story with completion status

4. **LevelData System**
   - Can load exercises by levelId
   - Supports all exercise types
   - Configurable difficulty and progression

### Integration Limitations

1. **No Book Parameter Support**
   - Current system uses episodes, not books
   - Need to add book-to-episode mapping
   - Need to add book parameter parsing

2. **No Direct Book Return Flow**
   - Current return goes to StoryModeManager
   - Need JavaScript communication for website return
   - Need URL redirect option

3. **Exercise-to-Book Mapping Missing**
   - No system to map exercises to specific books
   - Need to create book exercise levels
   - Need book-specific level IDs

---

## Game Mode Details

### Training Mode
- **Focus:** State tracking, position analysis
- **Exercise Type:** Analysis (video analysis, state identification)
- **Episode Mapping:** Episode 1
- **Manager:** TrainingModeManager (needs to exist in game)

### Prediction Mode
- **Focus:** Opponent behavior prediction
- **Exercise Type:** Prediction (predict what opponent will do)
- **Episode Mapping:** Episode 2
- **Manager:** PredictionModeManager (needs to exist in game)

### Math Mode
- **Focus:** Math-based calculations
- **Exercise Type:** Math (calculations, measurements)
- **Episode Mapping:** Episode 3
- **Manager:** MathModeManager (needs to exist in game)

### Block Coding Mode
- **Focus:** Drag-and-drop code blocks
- **Exercise Type:** BlockCoding (drag blocks to create sequences)
- **Episode Mapping:** Future episodes
- **Manager:** BlockCodingManager (needs to exist in game)

### Freeplay Mode
- **Focus:** Open-ended exploration
- **Exercise Type:** Freeplay (no specific constraints)
- **Episode Mapping:** None
- **Manager:** None specified (needs implementation)

---

## Exercise Configuration Options

### Block Coding Exercise
- **Available Blocks:** Array of block names
- **Required Blocks:** Blocks that must be used
- **Target Code:** Expected code/sequence
- **Allow Custom Blocks:** Boolean flag

### Analysis Exercise
- **Number of Questions:** How many questions to ask
- **Show Video During Questions:** Boolean flag
- **Time Limit:** Time limit in seconds (-1 = no limit)

### Prediction Exercise
- **Number of Predictions:** How many predictions to make
- **Prediction Window:** Seconds ahead to predict
- **Show Feedback:** Boolean flag

### Math Exercise
- **Math Concept:** Concept name (e.g., "angles", "probability")
- **Number of Problems:** How many math problems
- **Show Visual Aids:** Boolean flag

### Scoring Configuration
- **Max Score:** Maximum possible score (default: 100)
- **Passing Score:** Minimum to pass (default: 70)
- **Show Score During Exercise:** Boolean flag
- **Allow Retry:** Boolean flag
- **Max Attempts:** Maximum retry attempts (default: 3)

---

## File Structure

```
Unity-Scripts/
├── BallCODEStarter.cs          # Entry point, URL parsing
├── StoryModeManager.cs         # Story reading interface
├── GameModeManager.cs          # Game mode transitions
├── StoryData.cs                # Story data structures
├── LevelData.cs                # Level/exercise data structures
├── LevelDataManager.cs         # Level loading and management
├── AIMCODELevelGenerator.cs    # Automated level generation
├── MetricsCollector.cs         # Metrics collection system
├── StoryEpisodeCreator.cs      # Editor tool for creating episodes
└── TestStoryDataHelper.cs      # Testing utilities
```

---

## WebGL Integration

### Current WebGL Support
- URL parameter parsing in WebGL builds
- `Application.absoluteURL` for URL reading
- `#if UNITY_WEBGL && !UNITY_EDITOR` conditional compilation

### WebGL Limitations
- No direct JavaScript communication currently
- Need to add `window.parent.postMessage()` for return flow
- Need to add JavaScript bridge for website communication

---

## Next Steps for Book Integration

1. **Extend URL Parameter Parsing**
   - Add `book` parameter support
   - Add `exercise` parameter support
   - Add `source=book` tracking

2. **Create Book-to-Episode Mapping**
   - Map Book 1 → Episode 1 concepts
   - Map Book 2 → Episode 2 concepts
   - Map Book 3 → Episode 3 concepts

3. **Create Book Exercise Levels**
   - Create LevelData for each book exercise
   - Use appropriate exercise types
   - Configure for book-specific learning objectives

4. **Implement Return Flow**
   - Add JavaScript communication for WebGL
   - Add URL redirect option
   - Handle completion status

5. **Extend GameModeManager**
   - Add book parameter handling
   - Add book exercise loading
   - Add return URL generation

---

## Summary

The BallCODE game has a robust architecture with:
- ✅ Story mode system ready
- ✅ Game mode management system ready
- ✅ LevelData system for exercises ready
- ✅ Metrics collection system ready
- ✅ URL parameter support (needs extension)
- ⚠️ Book integration needs implementation
- ⚠️ Return flow to website needs implementation

**The game is ready for book integration with the extensions outlined above.**

---

**Document Status:** Complete  
**Last Updated:** November 26, 2025  
**Next Review:** After book integration implementation


