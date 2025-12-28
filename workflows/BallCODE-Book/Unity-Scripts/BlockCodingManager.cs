using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;
using System.Linq;

/// <summary>
/// Block Coding Manager - Manages block-based coding exercises for Books 1, 2, and 3
/// Handles sequences (Book 1), conditionals (Book 2), and loops (Book 3)
/// Uses same core game logic as coding game, just with different block elements
/// </summary>
public class BlockCodingManager : MonoBehaviour
{
    [Header("Block Coding UI")]
    public GameObject blockCodingPanel;
    public Transform blockPalette;              // Where available blocks are shown
    public Transform codeArea;                  // Where user drags blocks to create code
    public GameObject blockPrefab;               // Prefab for draggable blocks
    
    [Header("Exercise Display")]
    public Text exerciseTitleText;
    public Text exerciseDescriptionText;
    public Text storyContextText;
    public Text feedbackText;
    
    [Header("Block Execution")]
    public Button runCodeButton;
    public Button resetButton;
    public Button showSolutionButton;
    public Button hintButton;
    
    [Header("Court Visualization")]
    public GameObject courtContainer;
    public Camera courtCamera;
    
    [Header("Integration")]
    public GameModeManager gameModeManager;
    
    private LevelData currentLevel;
    private BlockCodingConfig currentConfig;
    private List<Block> currentBlocks = new List<Block>();  // Blocks in code area
    private bool isExecuting = false;
    private int executionIndex = 0;
    
    // Basketball action execution (similar to PythonCodingManager)
    // Note: In production, this should integrate with ActionsInput system from the game
    private Dictionary<string, System.Action<object[]>>> basketballActions;
    
    // Placeholder block support - blocks that exist but have no name/function yet
    private HashSet<string> placeholderBlocks = new HashSet<string>();
    
    void Start()
    {
        SetupButtons();
        SetupBasketballActions();
        if (blockCodingPanel != null)
        {
            blockCodingPanel.SetActive(false);
        }
    }
    
    /// <summary>
    /// Start block coding exercise from level data
    /// </summary>
    public void StartBlockCodingFromLevel(LevelData level)
    {
        if (level == null)
        {
            Debug.LogError("[BlockCodingManager] Level data is null!");
            return;
        }
        
        if (level.exercise == null || level.exercise.exerciseType != ExerciseType.BlockCoding)
        {
            Debug.LogError($"[BlockCodingManager] Level {level.levelId} is not a block coding exercise!");
            return;
        }
        
        currentLevel = level;
        
        // Show block coding panel
        if (blockCodingPanel != null)
        {
            blockCodingPanel.SetActive(true);
        }
        
        // Display exercise info
        if (exerciseTitleText != null)
        {
            exerciseTitleText.text = level.levelName;
        }
        
        if (exerciseDescriptionText != null)
        {
            exerciseDescriptionText.text = level.description;
        }
        
        // Load available blocks
        LoadAvailableBlocks(level.exercise.blockCoding);
        
        // Clear previous code
        ClearCodeArea();
        
        Debug.Log($"[BlockCodingManager] Started block coding exercise: {level.levelName}");
    }
    
    /// <summary>
    /// Start block coding exercise from config (legacy method for backward compatibility)
    /// </summary>
    public void StartBlockCoding(BlockCodingConfig config)
    {
        currentConfig = config;
        
        // Try to find level by episode and concept
        if (LevelDataManager.Instance != null)
        {
            LevelData level = FindLevelByEpisodeAndConcept(config.episode, config.codingConcept);
            if (level != null)
            {
                StartBlockCodingFromLevel(level);
                return;
            }
        }
        
        // Fallback: Create basic exercise from config
        Debug.LogWarning($"[BlockCodingManager] Level not found for episode {config.episode}, concept {config.codingConcept}. Using basic config.");
        
        if (blockCodingPanel != null)
        {
            blockCodingPanel.SetActive(true);
        }
        
        if (exerciseTitleText != null)
        {
            exerciseTitleText.text = $"Block Coding Exercise - Episode {config.episode}";
        }
        
        ClearCodeArea();
    }
    
    /// <summary>
    /// Find level by episode number and coding concept
    /// </summary>
    LevelData FindLevelByEpisodeAndConcept(int episode, string concept)
    {
        if (LevelDataManager.Instance == null)
        {
            return null;
        }
        
        // Get all levels for this episode
        List<LevelData> episodeLevels = LevelDataManager.Instance.GetLevelsByEpisode(episode);
        
        // Find block coding level with matching concept
        foreach (LevelData level in episodeLevels)
        {
            if (level.gameMode == "blockcoding" && 
                level.codingConcept == concept &&
                level.exercise != null &&
                level.exercise.exerciseType == ExerciseType.BlockCoding)
            {
                return level;
            }
        }
        
        return null;
    }
    
    /// <summary>
    /// Load available blocks into palette based on level configuration
    /// Based on existing drag-and-drop system design from CODING-BLOCKS-DESIGN-IDEATION.md
    /// Uses Scratch-style blocks: START, POUND DRIBBLE, CROSSOVER, IN & OUT, IF/THEN/ELSE, LOOP/REPEAT
    /// </summary>
    void LoadAvailableBlocks(BlockCodingExercise exercise)
    {
        if (exercise == null || blockPalette == null || blockPrefab == null)
        {
            Debug.LogWarning("[BlockCodingManager] Cannot load blocks - missing exercise, palette, or prefab");
            return;
        }
        
        // Clear existing blocks in palette
        foreach (Transform child in blockPalette)
        {
            Destroy(child.gameObject);
        }
        
        // Create blocks for each available block type
        // Block types match level JSON: START, BLOCK_1_POUND, BLOCK_2_CROSSOVER, BLOCK_3_IN_OUT, 
        // IF, THEN, ELSE, LOOP, REPEAT, ADVANCE, BUCKET, END, PLACEHOLDER
        foreach (string blockType in exercise.availableBlocks)
        {
            GameObject blockObj = Instantiate(blockPrefab, blockPalette);
            Block block = blockObj.GetComponent<Block>();
            if (block == null)
            {
                block = blockObj.AddComponent<Block>();
            }
            
            // Check if this is a placeholder block (no name/function yet)
            bool isPlaceholder = placeholderBlocks.Contains(blockType) || 
                                 string.IsNullOrEmpty(blockType) || 
                                 blockType == "PLACEHOLDER";
            
            block.Initialize(blockType, true, isPlaceholder); // true = is palette block (draggable)
            
            // Make block draggable (similar to DraggableUISpawner pattern)
            BlockDragger dragger = blockObj.GetComponent<BlockDragger>();
            if (dragger == null)
            {
                dragger = blockObj.AddComponent<BlockDragger>();
            }
            dragger.Initialize(block, codeArea);
        }
        
        Debug.Log($"[BlockCodingManager] Loaded {exercise.availableBlocks.Length} available blocks for {currentLevel?.levelName ?? "exercise"}");
    }
    
    /// <summary>
    /// Clear all blocks from code area
    /// </summary>
    void ClearCodeArea()
    {
        if (codeArea == null)
        {
            return;
        }
        
        foreach (Transform child in codeArea)
        {
            Destroy(child.gameObject);
        }
        
        currentBlocks.Clear();
        executionIndex = 0;
        
        if (feedbackText != null)
        {
            feedbackText.text = "";
        }
    }
    
    /// <summary>
    /// Setup button listeners
    /// </summary>
    void SetupButtons()
    {
        if (runCodeButton != null)
        {
            runCodeButton.onClick.AddListener(OnRunCode);
        }
        
        if (resetButton != null)
        {
            resetButton.onClick.AddListener(OnReset);
        }
        
        if (showSolutionButton != null)
        {
            showSolutionButton.onClick.AddListener(OnShowSolution);
        }
        
        if (hintButton != null)
        {
            hintButton.onClick.AddListener(OnShowHint);
        }
    }
    
    /// <summary>
    /// Setup basketball action execution
    /// Integrates with game logic: matches SyntaxToActionsParser pattern
    /// Supports: Pound (1), Crossover (2), InAndOut (3), and direction system
    /// </summary>
    void SetupBasketballActions()
    {
        basketballActions = new Dictionary<string, System.Action<object[]>>();
        
        // START block - Initialize sequence
        basketballActions["START"] = (args) => {
            ExecuteStart();
        };
        
        // BLOCK_1_POUND - Pound dribble (Book 1)
        // Maps to ActionsInput.Pound() in game
        basketballActions["BLOCK_1_POUND"] = (args) => {
            ExecutePoundDribble();
        };
        
        // BLOCK_2_CROSSOVER - Crossover dribble (Book 2)
        // Maps to ActionsInput.Cross() in game
        basketballActions["BLOCK_2_CROSSOVER"] = (args) => {
            string direction = args != null && args.Length > 0 ? args[0].ToString() : "right";
            ExecuteCrossover(direction);
        };
        
        // BLOCK_3_IN_OUT - In & Out dribble (Book 3)
        // Maps to ActionsInput.InAndOut() in game
        basketballActions["BLOCK_3_IN_OUT"] = (args) => {
            string type = args != null && args.Length > 0 ? args[0].ToString() : "real";
            ExecuteInOut(type);
        };
        
        // ADVANCE - Move forward (direction-based movement)
        // Maps to ActionsInput direction system (Forward, Right, Left, etc.)
        basketballActions["ADVANCE"] = (args) => {
            string direction = args != null && args.Length > 0 ? args[0].ToString() : "forward";
            ExecuteAdvance(direction);
        };
        
        // BUCKET - Shoot/score (required at end of sequence)
        // Maps to ActionsInput.Bucket() in game
        basketballActions["BUCKET"] = (args) => {
            ExecuteBucket();
        };
        
        // END - End of sequence (optional, BUCKET usually serves this)
        basketballActions["END"] = (args) => {
            ExecuteEnd();
        };
        
        // IF/THEN/ELSE - Conditionals (Book 2) - Logic handled in ExecuteBlocks
        basketballActions["IF"] = (args) => {
            // Conditional logic handled in ExecuteBlocks
        };
        
        basketballActions["THEN"] = (args) => {
            // Conditional logic handled in ExecuteBlocks
        };
        
        basketballActions["ELSE"] = (args) => {
            // Conditional logic handled in ExecuteBlocks
        };
        
        // LOOP/REPEAT - Loops (Book 3) - Logic handled in ExecuteBlocks
        basketballActions["LOOP"] = (args) => {
            // Loop logic handled in ExecuteBlocks
        };
        
        basketballActions["REPEAT"] = (args) => {
            // Loop logic handled in ExecuteBlocks
        };
        
        basketballActions["BREAK"] = (args) => {
            // Loop break handled in ExecuteBlocks
        };
        
        // Placeholder blocks - blocks that exist but have no implementation yet
        // These will show in palette but do nothing when executed
        placeholderBlocks.Add("PLACEHOLDER");
        basketballActions["PLACEHOLDER"] = (args) => {
            Debug.Log("[BlockCodingManager] Placeholder block executed - no action");
        };
    }
    
    /// <summary>
    /// Run code - execute blocks in sequence
    /// </summary>
    void OnRunCode()
    {
        if (isExecuting)
        {
            return;
        }
        
        if (currentLevel == null || currentLevel.exercise == null)
        {
            ShowFeedback("No exercise loaded!", Color.red);
            return;
        }
        
        // Get blocks from code area
        currentBlocks = GetBlocksFromCodeArea();
        
        if (currentBlocks.Count == 0)
        {
            ShowFeedback("Please add some blocks to your code!", Color.yellow);
            return;
        }
        
        // Execute blocks
        StartCoroutine(ExecuteBlocks(currentBlocks));
    }
    
    /// <summary>
    /// Get all blocks from code area in execution order
    /// </summary>
    List<Block> GetBlocksFromCodeArea()
    {
        List<Block> blocks = new List<Block>();
        
        if (codeArea == null)
        {
            return blocks;
        }
        
        // Get all blocks in code area
        Block[] allBlocks = codeArea.GetComponentsInChildren<Block>();
        
        // Sort by position (top to bottom, left to right)
        blocks = allBlocks.OrderBy(b => -b.transform.position.y)
                          .ThenBy(b => b.transform.position.x)
                          .ToList();
        
        return blocks;
    }
    
    /// <summary>
    /// Execute blocks in sequence (handles sequences, conditionals, and loops)
    /// </summary>
    System.Collections.IEnumerator ExecuteBlocks(List<Block> blocks)
    {
        isExecuting = true;
        executionIndex = 0;
        
        ShowFeedback("Executing code...", Color.blue);
        
        int i = 0;
        while (i < blocks.Count)
        {
            Block block = blocks[i];
            string blockType = block.blockType;
            
            // Handle sequences (Book 1) - simple sequential execution
            if (blockType == "START")
            {
                ExecuteStart();
                yield return new WaitForSeconds(0.5f);
                i++;
            }
            else if (blockType == "BLOCK_1_POUND")
            {
                ExecutePoundDribble();
                yield return new WaitForSeconds(0.5f);
                i++;
            }
            else if (blockType == "ADVANCE")
            {
                ExecuteAdvance();
                yield return new WaitForSeconds(0.5f);
                i++;
            }
            // Handle conditionals (Book 2) - Direction-based conditionals
            // Example: "IF last move RIGHT THEN go FORWARD ELSE go RIGHT"
            else if (blockType == "IF")
            {
                // Find THEN and ELSE blocks
                Block thenBlock = FindNextBlock(blocks, i, "THEN");
                Block elseBlock = FindNextBlock(blocks, i, "ELSE");
                
                // Evaluate condition using game state (direction-based)
                // Supports: "last_direction_right", "last_direction_left", "action_count_less_than_3", etc.
                string conditionType = block.parameters != null && block.parameters.Length > 0 
                    ? block.parameters[0].ToString() 
                    : "last_direction_right"; // Default condition
                
                bool condition = EvaluateCondition(block, conditionType);
                
                if (condition)
                {
                    // Execute THEN branch
                    if (thenBlock != null)
                    {
                        int thenIndex = blocks.IndexOf(thenBlock);
                        i = thenIndex + 1;
                        // Execute action after THEN (skip THEN block itself)
                        while (i < blocks.Count && blocks[i].blockType != "ELSE" && blocks[i].blockType != "ADVANCE" && blocks[i].blockType != "BUCKET")
                        {
                            if (blocks[i].blockType.StartsWith("BLOCK_") || blocks[i].blockType == "ADVANCE")
                            {
                                ExecuteBlock(blocks[i]);
                                yield return new WaitForSeconds(0.5f);
                            }
                            i++;
                        }
                        i--; // Adjust for loop increment
                    }
                }
                else
                {
                    // Execute ELSE branch
                    if (elseBlock != null)
                    {
                        int elseIndex = blocks.IndexOf(elseBlock);
                        i = elseIndex + 1;
                        // Execute action after ELSE
                        while (i < blocks.Count && blocks[i].blockType != "ADVANCE" && blocks[i].blockType != "BUCKET")
                        {
                            if (blocks[i].blockType.StartsWith("BLOCK_") || blocks[i].blockType == "ADVANCE")
                            {
                                ExecuteBlock(blocks[i]);
                                yield return new WaitForSeconds(0.5f);
                            }
                            i++;
                        }
                        i--; // Adjust for loop increment
                    }
                }
                
                // Skip past the conditional structure
                i = FindEndOfConditional(blocks, i);
            }
            // Handle loops (Book 3) - Repeat dribble without putting it in each time
            // Example: "REPEAT 5 TIMES: POUND" instead of "POUND → POUND → POUND → POUND → POUND"
            else if (blockType == "LOOP")
            {
                // Find REPEAT block with count
                Block repeatBlock = FindNextBlock(blocks, i, "REPEAT");
                int repeatCount = 3; // Default
                
                if (repeatBlock != null)
                {
                    // Extract repeat count from block
                    repeatCount = repeatBlock.repeatCount > 0 ? repeatBlock.repeatCount : 3;
                }
                
                // Find loop body (blocks between LOOP and END/THEN/BREAK)
                int loopStart = i + 1;
                int loopEnd = FindEndOfLoop(blocks, i);
                
                // Collect loop body blocks
                List<Block> loopBody = new List<Block>();
                for (int j = loopStart; j < loopEnd; j++)
                {
                    if (blocks[j].blockType != "REPEAT" && blocks[j].blockType != "LOOP")
                    {
                        loopBody.Add(blocks[j]);
                    }
                }
                
                // Execute loop body repeatCount times (like existing ForLoop pattern)
                for (int loop = 0; loop < repeatCount; loop++)
                {
                    foreach (Block bodyBlock in loopBody)
                    {
                        if (bodyBlock.blockType.StartsWith("BLOCK_") || bodyBlock.blockType == "ADVANCE")
                        {
                            ExecuteBlock(bodyBlock);
                            yield return new WaitForSeconds(0.5f);
                        }
                    }
                }
                
                i = loopEnd;
            }
            else
            {
                // Execute other blocks
                ExecuteBlock(block);
                yield return new WaitForSeconds(0.5f);
                i++;
            }
        }
        
        // Check solution
        yield return new WaitForSeconds(1f);
        
        // Show sequence feedback (Book 1 concept)
        ShowSequenceFeedback(blocks);
        
        CheckSolution();
        isExecuting = false;
    }
    
    /// <summary>
    /// Show sequence feedback after execution
    /// "You created a sequence! These blocks executed in order."
    /// </summary>
    void ShowSequenceFeedback(List<Block> executedBlocks)
    {
        if (executedBlocks == null || executedBlocks.Count == 0)
        {
            return;
        }
        
        // Count action blocks (not control blocks)
        int actionBlockCount = 0;
        foreach (Block block in executedBlocks)
        {
            if (block.blockType.StartsWith("BLOCK_") || block.blockType == "ADVANCE" || block.blockType == "BUCKET")
            {
                actionBlockCount++;
            }
        }
        
        if (actionBlockCount > 1)
        {
            ShowFeedback($"✓ You created a sequence! {actionBlockCount} blocks executed in order.", Color.green);
            
            // Visual feedback: Highlight the sequence
            StartCoroutine(HighlightSequence(executedBlocks));
        }
    }
    
    /// <summary>
    /// Highlight sequence blocks visually
    /// </summary>
    System.Collections.IEnumerator HighlightSequence(List<Block> blocks)
    {
        // Highlight each block briefly to show sequence
        foreach (Block block in blocks)
        {
            if (block != null && block.blockType.StartsWith("BLOCK_"))
            {
                // TODO: Add visual highlighting (e.g., change block color temporarily)
                // For now, just log
                Debug.Log($"[BlockCodingManager] Highlighting block: {block.blockType}");
                yield return new WaitForSeconds(0.3f);
            }
        }
    }
    
    /// <summary>
    /// Execute a single block
    /// </summary>
    void ExecuteBlock(Block block)
    {
        string blockType = block.blockType;
        
        if (basketballActions.ContainsKey(blockType))
        {
            basketballActions[blockType](block.parameters);
        }
        else
        {
            Debug.LogWarning($"[BlockCodingManager] Unknown block type: {blockType}");
        }
    }
    
    /// <summary>
    /// Find next block of specific type
    /// </summary>
    Block FindNextBlock(List<Block> blocks, int startIndex, string blockType)
    {
        for (int i = startIndex + 1; i < blocks.Count; i++)
        {
            if (blocks[i].blockType == blockType)
            {
                return blocks[i];
            }
        }
        return null;
    }
    
    /// <summary>
    /// Find end of conditional structure
    /// </summary>
    int FindEndOfConditional(List<Block> blocks, int startIndex)
    {
        // Skip past THEN, ELSE, and their action blocks
        for (int i = startIndex + 1; i < blocks.Count; i++)
        {
            if (blocks[i].blockType == "ADVANCE" || blocks[i].blockType == "START")
            {
                return i;
            }
        }
        return blocks.Count;
    }
    
    /// <summary>
    /// Find end of loop structure
    /// </summary>
    int FindEndOfLoop(List<Block> blocks, int startIndex)
    {
        // Find THEN or BREAK after loop
        for (int i = startIndex + 1; i < blocks.Count; i++)
        {
            if (blocks[i].blockType == "THEN" || blocks[i].blockType == "BREAK" || blocks[i].blockType == "ADVANCE")
            {
                return i + 1;
            }
        }
        return blocks.Count;
    }
    
    /// <summary>
    /// Evaluate conditional condition based on game state
    /// Supports direction-based conditionals: "IF last move RIGHT THEN go FORWARD"
    /// Uses existing ActionsInput/GameInfo state - no new game state needed
    /// </summary>
    bool EvaluateCondition(Block ifBlock, string conditionType = "last_direction_right")
    {
        // Check condition type from block parameters or default
        if (ifBlock.parameters != null && ifBlock.parameters.Length > 0)
        {
            conditionType = ifBlock.parameters[0].ToString();
        }
        
        switch (conditionType.ToLower())
        {
            case "last_direction_right":
            case "last_move_right":
                // Check if last direction was RIGHT
                // Uses existing ActionsInput or GameInfo state
                return CheckLastDirection("Right");
                
            case "last_direction_left":
            case "last_move_left":
                // Check if last direction was LEFT
                return CheckLastDirection("Left");
                
            case "last_direction_forward":
            case "last_move_forward":
                // Check if last direction was FORWARD
                return CheckLastDirection("Forward");
                
            case "action_count_less_than_3":
                // Check if action count < 3
                return CheckActionCount(3, lessThan: true);
                
            case "last_hand_right":
                // Check if last hand was RIGHT
                return CheckLastHand("Right");
                
            case "last_hand_left":
                // Check if last hand was LEFT
                return CheckLastHand("Left");
                
            default:
                // Default: Check if last direction was RIGHT
                return CheckLastDirection("Right");
        }
    }
    
    /// <summary>
    /// Check last direction from game state
    /// </summary>
    bool CheckLastDirection(string direction)
    {
        // Try to get from ActionsInput (if available)
        // Note: This requires ActionsInput to expose direction tracking
        // For now, use GameInfo as fallback
        
        if (GameInfo.myInstance != null)
        {
            string initialDir = GameInfo.myInstance.GetInitialDirection();
            string counterDir = GameInfo.myInstance.GetCounterDirection();
            
            // Check counter direction first (most recent), then initial
            if (!string.IsNullOrEmpty(counterDir))
            {
                return counterDir.Contains(direction, System.StringComparison.OrdinalIgnoreCase);
            }
            else if (!string.IsNullOrEmpty(initialDir))
            {
                return initialDir.Contains(direction, System.StringComparison.OrdinalIgnoreCase);
            }
        }
        
        // Fallback: Check ActionsInput if available
        // TODO: Integrate with ActionsInput.GetLastDirection() when available
        
        return false;
    }
    
    /// <summary>
    /// Check action count
    /// </summary>
    bool CheckActionCount(int threshold, bool lessThan = true)
    {
        // Try to get from ActionsInput
        // TODO: Integrate with ActionsInput.GetActionsCount() when available
        
        // For now, use currentBlocks count as approximation
        int currentCount = currentBlocks.Count;
        
        if (lessThan)
        {
            return currentCount < threshold;
        }
        else
        {
            return currentCount >= threshold;
        }
    }
    
    /// <summary>
    /// Check last hand used
    /// </summary>
    bool CheckLastHand(string hand)
    {
        // Try to get from ActionsInput
        // TODO: Integrate with ActionsInput.GetHandsList() when available
        
        // For now, return false (needs ActionsInput integration)
        return false;
    }
    
    // Basketball action execution methods
    // These should integrate with ActionsInput system in production
    // For now, they log actions and can be connected to actual game logic
    
    void ExecuteStart()
    {
        Debug.Log("[BlockCodingManager] Executing START - Initializing sequence");
        // TODO: Integrate with game initialization
        // Reset player position, clear previous actions, etc.
    }
    
    void ExecutePoundDribble()
    {
        Debug.Log("[BlockCodingManager] Executing BLOCK_1_POUND (Pound Dribble)");
        // TODO: Integrate with ActionsInput.Pound()
        // In production: ActionsInput.myInstance.Pound();
        // Then set direction if needed
    }
    
    void ExecuteCrossover(string direction)
    {
        Debug.Log($"[BlockCodingManager] Executing BLOCK_2_CROSSOVER ({direction})");
        // TODO: Integrate with ActionsInput.Cross()
        // In production: 
        //   SetDirection(direction); // Convert string to ActionsInput.DIRECTION
        //   ActionsInput.myInstance.Cross();
    }
    
    void ExecuteInOut(string type)
    {
        Debug.Log($"[BlockCodingManager] Executing BLOCK_3_IN_OUT ({type})");
        // TODO: Integrate with ActionsInput.InAndOut()
        // In production: ActionsInput.myInstance.InAndOut();
        // Type can be "fake" or "real" for pattern creation/breaking
    }
    
    void ExecuteAdvance(string direction = "forward")
    {
        Debug.Log($"[BlockCodingManager] Executing ADVANCE ({direction})");
        // TODO: Integrate with ActionsInput direction system
        // In production: SetDirection(direction); // Convert to ActionsInput.DIRECTION enum
        // Direction options: Forward, Right, Left, Backward, ForwardRight, ForwardLeft, etc.
    }
    
    void ExecuteBucket()
    {
        Debug.Log("[BlockCodingManager] Executing BUCKET (Shoot/Score)");
        // TODO: Integrate with ActionsInput.Bucket()
        // In production: ActionsInput.myInstance.Bucket();
        // Required at end of sequence (game validation checks for this)
    }
    
    void ExecuteEnd()
    {
        Debug.Log("[BlockCodingManager] Executing END - Sequence complete");
        // Optional end marker - BUCKET usually serves this purpose
    }
    
    /// <summary>
    /// Convert direction string to ActionsInput.DIRECTION enum
    /// Matches SyntaxToActionsParser direction system (0-7)
    /// </summary>
    int ConvertDirectionToIndex(string direction)
    {
        // Map direction strings to dropdown index (0-7)
        // 0: Forward, 1: ForwardRight, 2: Right, 3: BackwardRight
        // 4: Backward, 5: BackwardLeft, 6: Left, 7: ForwardLeft
        switch (direction.ToLower())
        {
            case "forward": case "f": case "s": return 0;
            case "forwardright": case "fr": case "dsr": return 1;
            case "right": case "r": return 2;
            case "backwardright": case "br": case "dbr": return 3;
            case "backward": case "b": return 4;
            case "backwardleft": case "bl": case "dbl": return 5;
            case "left": case "l": return 6;
            case "forwardleft": case "fl": case "dsl": return 7;
            default: return 0; // Default to Forward
        }
    }
    
    /// <summary>
    /// Check if solution matches target code
    /// </summary>
    void CheckSolution()
    {
        if (currentLevel == null || currentLevel.exercise == null || currentLevel.exercise.blockCoding == null)
        {
            return;
        }
        
        string targetCode = currentLevel.exercise.blockCoding.targetCode;
        string playerCode = GetPlayerCodeString();
        
        // Simple comparison (can be enhanced with more sophisticated matching)
        bool matches = playerCode.Contains(targetCode) || targetCode.Contains(playerCode);
        
        if (matches)
        {
            ShowFeedback("✓ Correct! Great job!", Color.green);
            
            // Notify game mode manager
            if (gameModeManager != null)
            {
                gameModeManager.OnExerciseComplete(true, 100f);
            }
        }
        else
        {
            ShowFeedback("Not quite right. Try again!", Color.yellow);
        }
    }
    
    /// <summary>
    /// Get player's code as string for comparison
    /// </summary>
    string GetPlayerCodeString()
    {
        List<Block> blocks = GetBlocksFromCodeArea();
        List<string> blockTypes = new List<string>();
        
        foreach (Block block in blocks)
        {
            blockTypes.Add(block.blockType);
        }
        
        return string.Join(" → ", blockTypes);
    }
    
    /// <summary>
    /// Show feedback message
    /// </summary>
    void ShowFeedback(string message, Color color)
    {
        if (feedbackText != null)
        {
            feedbackText.text = message;
            feedbackText.color = color;
        }
        
        Debug.Log($"[BlockCodingManager] {message}");
    }
    
    void OnReset()
    {
        ClearCodeArea();
        ShowFeedback("Code cleared. Start fresh!", Color.blue);
    }
    
    void OnShowSolution()
    {
        if (currentLevel == null || currentLevel.exercise == null)
        {
            return;
        }
        
        string targetCode = currentLevel.exercise.blockCoding.targetCode;
        ShowFeedback($"Target code: {targetCode}", Color.cyan);
    }
    
    void OnShowHint()
    {
        if (currentLevel == null)
        {
            return;
        }
        
        // Show hint based on book/concept
        string hint = GetHintForLevel(currentLevel);
        ShowFeedback($"Hint: {hint}", Color.cyan);
    }
    
    /// <summary>
    /// Get hint based on level concept
    /// </summary>
    string GetHintForLevel(LevelData level)
    {
        if (level.codingConcept == "basic_blocks_sequences")
        {
            return "Try repeating Block 1 (Pound) multiple times in sequence!";
        }
        else if (level.codingConcept == "if_then_conditionals")
        {
            return "Use IF to check the defender, THEN choose your move!";
        }
        else if (level.codingConcept == "loops_repetition")
        {
            return "Use LOOP and REPEAT to create patterns!";
        }
        
        return "Think about what the book taught you!";
    }
}

/// <summary>
/// Block component - represents a single code block
/// </summary>
public class Block : MonoBehaviour
{
    public string blockType;           // Type of block (e.g., "START", "BLOCK_1_POUND")
    public bool isPaletteBlock;        // Is this a palette block (draggable) or code block
    public bool isPlaceholder;        // Is this a placeholder block (no name/function yet)
    public int repeatCount;            // For REPEAT blocks
    public object[] parameters;        // Block parameters
    
    public void Initialize(string type, bool isPalette, bool isPlaceholderBlock = false)
    {
        blockType = type;
        isPaletteBlock = isPalette;
        isPlaceholder = isPlaceholderBlock;
        repeatCount = 0;
        parameters = null;
        
        // Set block visual/text based on type
        Text blockText = GetComponentInChildren<Text>();
        if (blockText != null)
        {
            if (isPlaceholder)
            {
                blockText.text = ""; // No name for placeholder blocks
                // Could add visual indicator (e.g., grayed out, dashed border)
            }
            else
            {
                blockText.text = GetBlockDisplayName(type);
            }
        }
    }
    
    /// <summary>
    /// Get display name for block type
    /// </summary>
    string GetBlockDisplayName(string type)
    {
        switch (type)
        {
            case "START": return "START";
            case "BLOCK_1_POUND": return "POUND";
            case "BLOCK_2_CROSSOVER": return "CROSSOVER";
            case "BLOCK_3_IN_OUT": return "IN & OUT";
            case "ADVANCE": return "ADVANCE";
            case "BUCKET": return "BUCKET";
            case "END": return "END";
            case "IF": return "IF";
            case "THEN": return "THEN";
            case "ELSE": return "ELSE";
            case "LOOP": return "LOOP";
            case "REPEAT": return "REPEAT";
            case "BREAK": return "BREAK";
            case "PLACEHOLDER": return ""; // No name for placeholder
            default: return type;
        }
    }
}

/// <summary>
/// Block Dragger - handles drag and drop of blocks
/// </summary>
public class BlockDragger : MonoBehaviour
{
    private Block block;
    private Transform codeArea;
    private bool isDragging = false;
    
    public void Initialize(Block block, Transform codeArea)
    {
        this.block = block;
        this.codeArea = codeArea;
        
        // Add drag handlers
        // Note: This is simplified - in production, use Unity's EventSystem for proper drag handling
    }
}

