using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Example script showing how to create a level with x,y positions and dribble data
/// This demonstrates the level creation system
/// </summary>
public class LevelCreationExample : MonoBehaviour
{
    [Header("Level Creator Reference")]
    public LevelCreator levelCreator;
    
    [ContextMenu("Create Example Level with Positions")]
    void CreateExampleLevel()
    {
        if (levelCreator == null)
        {
            levelCreator = FindObjectOfType<LevelCreator>();
            if (levelCreator == null)
            {
                Debug.LogError("LevelCreator not found! Add LevelCreator component to scene.");
                return;
            }
        }
        
        // Example: Create a level with player positions and dribbles
        // Court coordinates: X (0-94 feet), Y (0-50 feet)
        // Origin (0,0) is bottom-left corner
        
        List<StrategyStepWithPositions> steps = new List<StrategyStepWithPositions>
        {
            // Step 1: Start position - Nova at top of key
            new StrategyStepWithPositions
            {
                stepNumber = 1,
                action = "Nova starts at top of key with ball",
                codeEquivalent = "START",
                timing = 0.0f,
                positions = new List<PlayerPositionData>
                {
                    new PlayerPositionData
                    {
                        x = 47f,  // Center of court (94/2)
                        y = 40f,  // Top of key area
                        playerId = "Nova",
                        dribbleType = 0,  // No dribble yet
                        dribbleDirection = "none"
                    }
                }
            },
            
            // Step 2: Nova performs Pound Dribble (Dribble 1) moving forward
            new StrategyStepWithPositions
            {
                stepNumber = 2,
                action = "Nova performs Pound Dribble (Block 1) moving forward",
                codeEquivalent = "BLOCK_1_POUND",
                timing = 0.5f,
                positions = new List<PlayerPositionData>
                {
                    new PlayerPositionData
                    {
                        x = 47f,  // Still center
                        y = 35f,  // Moved forward (down on court)
                        playerId = "Nova",
                        dribbleType = 1,  // Pound Dribble
                        dribbleDirection = "forward"
                    }
                }
            },
            
            // Step 3: Nova performs Crossover (Dribble 2) to the right
            new StrategyStepWithPositions
            {
                stepNumber = 3,
                action = "Nova performs Crossover (Block 2) to the right",
                codeEquivalent = "BLOCK_2_CROSSOVER",
                timing = 1.0f,
                positions = new List<PlayerPositionData>
                {
                    new PlayerPositionData
                    {
                        x = 52f,  // Moved right
                        y = 35f,  // Same Y position
                        playerId = "Nova",
                        dribbleType = 2,  // Crossover Dribble
                        dribbleDirection = "right"
                    }
                }
            },
            
            // Step 4: Nova performs In & Out (Dribble 3) faking left then going right
            new StrategyStepWithPositions
            {
                stepNumber = 4,
                action = "Nova performs In & Out Dribble (Block 3) - fake left, go right",
                codeEquivalent = "BLOCK_3_IN_OUT",
                timing = 1.5f,
                positions = new List<PlayerPositionData>
                {
                    new PlayerPositionData
                    {
                        x = 55f,  // Further right
                        y = 30f,  // Moving forward
                        playerId = "Nova",
                        dribbleType = 3,  // In & Out Dribble
                        dribbleDirection = "right"  // Final direction after fake
                    }
                }
            },
            
            // Step 5: Advance to basket
            new StrategyStepWithPositions
            {
                stepNumber = 5,
                action = "Nova advances to basket",
                codeEquivalent = "ADVANCE",
                timing = 2.0f,
                positions = new List<PlayerPositionData>
                {
                    new PlayerPositionData
                    {
                        x = 55f,  // Near basket
                        y = 10f,  // Close to basket
                        playerId = "Nova",
                        dribbleType = 0,  // No dribble
                        dribbleDirection = "forward"
                    }
                }
            }
        };
        
        // Create the level
        LevelData level = levelCreator.CreateLevel(
            levelId: "example_level_with_positions",
            levelName: "Example Level with Player Positions",
            description: "A demonstration level showing player positions and dribble sequences",
            gameMode: "blockcoding",
            episodeNumber: 0,
            codingConcept: "basic_blocks_sequences",
            steps: steps
        );
        
        // Save to JSON
        levelCreator.SaveLevelToJSON(level, "example_level_with_positions.json");
        
        Debug.Log("Example level created successfully!");
    }
    
    [ContextMenu("Create Multi-Player Level Example")]
    void CreateMultiPlayerLevel()
    {
        if (levelCreator == null)
        {
            levelCreator = FindObjectOfType<LevelCreator>();
        }
        
        // Example with multiple players
        List<StrategyStepWithPositions> steps = new List<StrategyStepWithPositions>
        {
            // Step 1: Starting positions
            new StrategyStepWithPositions
            {
                stepNumber = 1,
                action = "Team starting positions",
                codeEquivalent = "START",
                timing = 0.0f,
                positions = new List<PlayerPositionData>
                {
                    // Nova at top of key
                    new PlayerPositionData { x = 47f, y = 40f, playerId = "Nova", dribbleType = 0, dribbleDirection = "none" },
                    // Atlas on left wing
                    new PlayerPositionData { x = 30f, y = 35f, playerId = "Atlas", dribbleType = 0, dribbleDirection = "none" },
                    // Pixel on right wing
                    new PlayerPositionData { x = 64f, y = 35f, playerId = "Pixel", dribbleType = 0, dribbleDirection = "none" },
                    // Anchor in paint
                    new PlayerPositionData { x = 47f, y = 15f, playerId = "Anchor", dribbleType = 0, dribbleDirection = "none" }
                }
            },
            
            // Step 2: Nova dribbles, others move
            new StrategyStepWithPositions
            {
                stepNumber = 2,
                action = "Nova dribbles forward, team moves into position",
                codeEquivalent = "BLOCK_1_POUND",
                timing = 0.5f,
                positions = new List<PlayerPositionData>
                {
                    new PlayerPositionData { x = 47f, y = 35f, playerId = "Nova", dribbleType = 1, dribbleDirection = "forward" },
                    new PlayerPositionData { x = 30f, y = 30f, playerId = "Atlas", dribbleType = 0, dribbleDirection = "none" },
                    new PlayerPositionData { x = 64f, y = 30f, playerId = "Pixel", dribbleType = 0, dribbleDirection = "none" },
                    new PlayerPositionData { x = 47f, y = 12f, playerId = "Anchor", dribbleType = 0, dribbleDirection = "none" }
                }
            }
        };
        
        LevelData level = levelCreator.CreateLevel(
            levelId: "example_multiplayer_level",
            levelName: "Multi-Player Level Example",
            description: "Example level with multiple players and their positions",
            gameMode: "blockcoding",
            episodeNumber: 0,
            codingConcept: "basic_blocks_sequences",
            steps: steps
        );
        
        levelCreator.SaveLevelToJSON(level, "example_multiplayer_level.json");
        
        Debug.Log("Multi-player example level created!");
    }
}



