# Level Creation Guide - Adding Levels with X,Y Positions and Dribble Data

**Copyright © 2025 Rashad West. All Rights Reserved.**

---

## Overview

This guide explains how to create new levels for BallCODE with player positions (x,y coordinates) and dribble information.

---

## Court Coordinate System

### Standard Basketball Court
- **Width:** 94 feet (X-axis: 0 to 94)
- **Height:** 50 feet (Y-axis: 0 to 50)
- **Origin (0,0):** Bottom-left corner of the court
- **Center:** (47, 25) - Middle of court

### Key Court Locations
- **Top of Key:** ~(47, 40)
- **Three-Point Line:** Varies by position
- **Paint/Basket:** ~(47, 10-15)
- **Corners:** (0,0), (94,0), (0,50), (94,50)

### Alternative: Normalized Coordinates
You can also use normalized coordinates (0-1 range):
- X: 0.0 (left) to 1.0 (right)
- Y: 0.0 (bottom) to 1.0 (top)
- Set `useNormalizedCoordinates = true` in LevelCreator

---

## Dribble Types (1-7)

1. **Pound Dribble** - Basic bounce, foundation move
2. **Crossover Dribble** - Ball transfers from one hand to other
3. **In & Out Dribble** - Fake one direction, go the other
4. **Between the Legs** - Ball passes through legs
5. **Behind the Back** - Ball transfers behind back
6. **Half Spin Dribble** - Half rotation while dribbling
7. **Spin Dribble** - Full rotation while dribbling

---

## Creating a Level

### Method 1: Using LevelCreator Script (Recommended)

1. **Add LevelCreator to Scene:**
   - Create empty GameObject
   - Add `LevelCreator` component
   - Set `outputDirectory` if needed

2. **Use LevelCreationExample:**
   - Add `LevelCreationExample` component
   - Right-click component → "Create Example Level with Positions"
   - This creates a sample level with positions

3. **Create Your Own Level:**
   ```csharp
   LevelCreator creator = FindObjectOfType<LevelCreator>();
   
   List<StrategyStepWithPositions> steps = new List<StrategyStepWithPositions>
   {
       new StrategyStepWithPositions
       {
           stepNumber = 1,
           action = "Player starts at top of key",
           codeEquivalent = "START",
           timing = 0.0f,
           positions = new List<PlayerPositionData>
           {
               new PlayerPositionData
               {
                   x = 47f,  // Center X
                   y = 40f,  // Top of key Y
                   playerId = "Nova",
                   dribbleType = 0,  // No dribble
                   dribbleDirection = "none"
               }
           }
       },
       // Add more steps...
   };
   
   LevelData level = creator.CreateLevel(
       levelId: "my_level_001",
       levelName: "My Level",
       description: "Description here",
       gameMode: "blockcoding",
       episodeNumber: 0,
       codingConcept: "basic_blocks_sequences",
       steps: steps
   );
   
   creator.SaveLevelToJSON(level, "my_level_001.json");
   ```

### Method 2: Manual JSON Creation

Create a JSON file in `Assets/StreamingAssets/Levels/`:

```json
{
  "levels": [
    {
      "levelId": "manual_level_001",
      "levelName": "Manual Level",
      "description": "Level created manually",
      "gameMode": "blockcoding",
      "episodeNumber": 0,
      "codingConcept": "basic_blocks_sequences",
      "strategy": {
        "strategyName": "Manual Strategy",
        "strategyType": "offensive",
        "description": "Strategy description",
        "steps": [
          {
            "stepNumber": 1,
            "action": "Start position",
            "codeEquivalent": "START",
            "timing": 0.0,
            "playerPositions": [
              {
                "x": 47.0,
                "y": 40.0,
                "playerId": "Nova",
                "dribbleType": 0,
                "dribbleDirection": "none",
                "isNormalized": false
              }
            ]
          },
          {
            "stepNumber": 2,
            "action": "Pound dribble forward",
            "codeEquivalent": "BLOCK_1_POUND",
            "timing": 0.5,
            "playerPositions": [
              {
                "x": 47.0,
                "y": 35.0,
                "playerId": "Nova",
                "dribbleType": 1,
                "dribbleDirection": "forward",
                "isNormalized": false
              }
            ]
          }
        ]
      }
    }
  ],
  "version": "1.0",
  "lastUpdated": "2025-01-XX"
}
```

---

## Player Position Data Structure

### PlayerPosition Class
```csharp
{
    "x": float,              // X coordinate (0-94 feet or 0-1 normalized)
    "y": float,              // Y coordinate (0-50 feet or 0-1 normalized)
    "playerId": string,      // "Nova", "Atlas", "Pixel", "Anchor", etc.
    "dribbleType": int,      // 0=none, 1-7=dribble types
    "dribbleDirection": string, // "left", "right", "forward", "backward", "none"
    "isNormalized": bool     // true if using 0-1 range, false for feet
}
```

---

## Example: Complete Level with Dribble Sequence

```csharp
// Step 1: Start
{
    stepNumber: 1,
    action: "Nova starts at top of key",
    codeEquivalent: "START",
    timing: 0.0f,
    positions: [
        { x: 47f, y: 40f, playerId: "Nova", dribbleType: 0, dribbleDirection: "none" }
    ]
}

// Step 2: Pound Dribble (Block 1)
{
    stepNumber: 2,
    action: "Nova performs Pound Dribble forward",
    codeEquivalent: "BLOCK_1_POUND",
    timing: 0.5f,
    positions: [
        { x: 47f, y: 35f, playerId: "Nova", dribbleType: 1, dribbleDirection: "forward" }
    ]
}

// Step 3: Crossover (Block 2)
{
    stepNumber: 3,
    action: "Nova performs Crossover to the right",
    codeEquivalent: "BLOCK_2_CROSSOVER",
    timing: 1.0f,
    positions: [
        { x: 52f, y: 35f, playerId: "Nova", dribbleType: 2, dribbleDirection: "right" }
    ]
}

// Step 4: In & Out (Block 3)
{
    stepNumber: 4,
    action: "Nova performs In & Out Dribble",
    codeEquivalent: "BLOCK_3_IN_OUT",
    timing: 1.5f,
    positions: [
        { x: 55f, y: 30f, playerId: "Nova", dribbleType: 3, dribbleDirection: "right" }
    ]
}
```

---

## Multi-Player Levels

You can include multiple players in each step:

```csharp
positions: [
    { x: 47f, y: 40f, playerId: "Nova", dribbleType: 1, dribbleDirection: "forward" },
    { x: 30f, y: 35f, playerId: "Atlas", dribbleType: 0, dribbleDirection: "none" },
    { x: 64f, y: 35f, playerId: "Pixel", dribbleType: 0, dribbleDirection: "none" },
    { x: 47f, y: 15f, playerId: "Anchor", dribbleType: 0, dribbleDirection: "none" }
]
```

---

## Tips for Creating Levels

1. **Start Simple:** Begin with single-player, single-dribble sequences
2. **Use Court Reference:** Keep a court diagram handy for accurate coordinates
3. **Test Positions:** Verify positions make basketball sense
4. **Dribble Sequences:** Follow logical dribble progressions (1→2→3, etc.)
5. **Timing:** Space timing appropriately (0.5s between steps is common)
6. **Player IDs:** Use consistent player IDs ("Nova", "Atlas", etc.)

---

## Updating Existing Levels

To add position data to existing levels:

1. Open the JSON file in `Unity-Scripts/Levels/`
2. Find the `steps` array
3. For each step, replace empty `playerPositions: []` with:
   ```json
   "playerPositions": [
       {
           "x": 47.0,
           "y": 40.0,
           "playerId": "Nova",
           "dribbleType": 1,
           "dribbleDirection": "forward",
           "isNormalized": false
       }
   ]
   ```

---

## Validation

The level system will:
- ✅ Load levels with position data
- ✅ Display positions on court (if visualization is implemented)
- ✅ Track dribble sequences
- ⚠️ Validate coordinates are within court bounds (recommended to add)

---

## Next Steps

1. Create your first level using `LevelCreationExample`
2. Test loading the level in Unity
3. Verify positions display correctly
4. Add more complex sequences
5. Create multi-player scenarios

---

**Questions?** Check the Unity Console for errors when loading levels.




