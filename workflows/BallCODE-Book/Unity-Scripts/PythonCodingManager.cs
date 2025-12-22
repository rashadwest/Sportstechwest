using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;
using System.Text.RegularExpressions;

/// <summary>
/// Python Coding Manager - Manages Python code execution in game
/// Similar to BlockCodingManager but for Python syntax
/// </summary>
public class PythonCodingManager : MonoBehaviour
{
    [Header("Python Code Editor")]
    public InputField pythonCodeInput;
    public Text codeLineNumbers;
    public Text syntaxFeedbackText;
    public Text executionFeedbackText;
    
    [Header("Block-to-Python Bridge")]
    public GameObject bridgePanel;
    public Text blockCodeText;
    public Text pythonCodeText;
    public Button showBridgeButton;
    public Button hideBridgeButton;
    
    [Header("Code Execution")]
    public Button runCodeButton;
    public Button resetButton;
    public Button showSolutionButton;
    public Button hintButton;
    
    [Header("Court Visualization")]
    public GameObject courtContainer;
    public Camera courtCamera;
    
    [Header("Exercise Configuration")]
    public Text exerciseTitleText;
    public Text exerciseDescriptionText;
    public Text storyContextText;
    
    [Header("Integration")]
    public GameModeManager gameModeManager;
    
    private PythonExerciseData currentExercise;
    private List<string> codeLines = new List<string>();
    private bool isExecuting = false;
    private PythonInterpreter pythonInterpreter;
    
    // Basketball Python API functions
    private Dictionary<string, System.Action<object[]>> basketballFunctions;
    
    void Start()
    {
        InitializePythonInterpreter();
        SetupButtons();
        SetupBasketballAPI();
    }
    
    /// <summary>
    /// Initialize Python interpreter for code execution.
    /// Architecture: Integrate with Unity Python integration library (Python.NET, IronPython) or custom interpreter.
    /// Current implementation uses placeholder PythonInterpreter class.
    /// </summary>
    void InitializePythonInterpreter()
    {
        // Architecture note: For production, integrate with:
        // - Python.NET (https://pythonnet.github.io/) for Unity
        // - IronPython for .NET integration
        // - Custom interpreter using System.Diagnostics.Process
        pythonInterpreter = new PythonInterpreter();
    }
    
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
        
        if (showBridgeButton != null)
        {
            showBridgeButton.onClick.AddListener(OnShowBridge);
        }
        
        if (hideBridgeButton != null)
        {
            hideBridgeButton.onClick.AddListener(OnHideBridge);
        }
        
        if (pythonCodeInput != null)
        {
            pythonCodeInput.onValueChanged.AddListener(OnCodeChanged);
        }
    }
    
    void SetupBasketballAPI()
    {
        // Define basketball Python API functions
        basketballFunctions = new Dictionary<string, System.Action<object[]>>();
        
        // Dribble function: dribble(action, clock)
        basketballFunctions["dribble"] = (args) => {
            string action = args[0].ToString();
            float clock = args.Length > 1 ? float.Parse(args[1].ToString()) : 0.5f;
            ExecuteDribble(action, clock);
        };
        
        // Pass function: pass_to(direction)
        basketballFunctions["pass_to"] = (args) => {
            string direction = args[0].ToString();
            ExecutePass(direction);
        };
        
        // Shoot function: shoot()
        basketballFunctions["shoot"] = (args) => {
            ExecuteShoot();
        };
        
        // Move function: move(direction, distance)
        basketballFunctions["move"] = (args) => {
            string direction = args[0].ToString();
            float distance = args.Length > 1 ? float.Parse(args[1].ToString()) : 1.0f;
            ExecuteMove(direction, distance);
        };
        
        // Conditional: if_defender(condition, action)
        basketballFunctions["if_defender"] = (args) => {
            string condition = args[0].ToString();
            string action = args[1].ToString();
            ExecuteConditional(condition, action);
        };
        
        // Loop: repeat(times, action)
        basketballFunctions["repeat"] = (args) => {
            int times = int.Parse(args[0].ToString());
            string action = args[1].ToString();
            ExecuteLoop(times, action);
        };
    }
    
    public void LoadExercise(PythonExerciseData exercise)
    {
        if (exercise == null)
        {
            Debug.LogError("[PythonCodingManager] Cannot load null exercise!");
            return;
        }
        
        currentExercise = exercise;
        
        // Display exercise info
        if (exerciseTitleText != null)
        {
            exerciseTitleText.text = exercise.title;
        }
        
        if (exerciseDescriptionText != null)
        {
            exerciseDescriptionText.text = exercise.description;
        }
        
        if (storyContextText != null && !string.IsNullOrEmpty(exercise.storyContext))
        {
            storyContextText.text = $"💡 Story Context: {exercise.storyContext}";
            storyContextText.gameObject.SetActive(true);
        }
        
        // Load starter code if provided
        if (pythonCodeInput != null && !string.IsNullOrEmpty(exercise.starterCode))
        {
            pythonCodeInput.text = exercise.starterCode;
        }
        else if (pythonCodeInput != null)
        {
            pythonCodeInput.text = "# Write your Python code here\n# Use basketball functions like: dribble('move', 0.5)";
        }
        
        // Update line numbers
        UpdateLineNumbers();
        
        // Reset feedback
        if (syntaxFeedbackText != null)
        {
            syntaxFeedbackText.text = "Ready to code...";
            syntaxFeedbackText.color = Color.white;
        }
        
        if (executionFeedbackText != null)
        {
            executionFeedbackText.text = "";
        }
    }
    
    void OnCodeChanged(string code)
    {
        UpdateLineNumbers();
        ValidateSyntax(code);
    }
    
    void UpdateLineNumbers()
    {
        if (pythonCodeInput == null || codeLineNumbers == null)
        {
            return;
        }
        
        string code = pythonCodeInput.text;
        string[] lines = code.Split('\n');
        
        string lineNumbers = "";
        for (int i = 1; i <= lines.Length; i++)
        {
            lineNumbers += i + "\n";
        }
        
        codeLineNumbers.text = lineNumbers;
    }
    
    bool ValidateSyntax(string code)
    {
        if (string.IsNullOrEmpty(code))
        {
            if (syntaxFeedbackText != null)
            {
                syntaxFeedbackText.text = "Code is empty";
                syntaxFeedbackText.color = Color.yellow;
            }
            return false;
        }
        
        // Basic syntax validation
        // Check for common Python syntax errors
        
        // Check for unmatched parentheses
        int openParens = Regex.Matches(code, @"\(").Count;
        int closeParens = Regex.Matches(code, @"\)").Count;
        if (openParens != closeParens)
        {
            if (syntaxFeedbackText != null)
            {
                syntaxFeedbackText.text = "⚠️ Unmatched parentheses";
                syntaxFeedbackText.color = Color.red;
            }
            return false;
        }
        
        // Check for unmatched brackets
        int openBrackets = Regex.Matches(code, @"\[").Count;
        int closeBrackets = Regex.Matches(code, @"\]").Count;
        if (openBrackets != closeBrackets)
        {
            if (syntaxFeedbackText != null)
            {
                syntaxFeedbackText.text = "⚠️ Unmatched brackets";
                syntaxFeedbackText.color = Color.red;
            }
            return false;
        }
        
        // Check for unmatched braces
        int openBraces = Regex.Matches(code, @"\{").Count;
        int closeBraces = Regex.Matches(code, @"\}").Count;
        if (openBraces != closeBraces)
        {
            if (syntaxFeedbackText != null)
            {
                syntaxFeedbackText.text = "⚠️ Unmatched braces";
                syntaxFeedbackText.color = Color.red;
            }
            return false;
        }
        
        // Basic validation passed
        if (syntaxFeedbackText != null)
        {
            syntaxFeedbackText.text = "✓ Syntax looks good";
            syntaxFeedbackText.color = Color.green;
        }
        
        return true;
    }
    
    void OnRunCode()
    {
        if (currentExercise == null || isExecuting)
        {
            return;
        }
        
        string code = pythonCodeInput != null ? pythonCodeInput.text : "";
        
        if (string.IsNullOrEmpty(code))
        {
            ShowError("Please write some code first!");
            return;
        }
        
        if (!ValidateSyntax(code))
        {
            ShowError("Please fix syntax errors before running.");
            return;
        }
        
        // Execute Python code
        ExecutePythonCode(code);
    }
    
    void ExecutePythonCode(string code)
    {
        isExecuting = true;
        
        if (executionFeedbackText != null)
        {
            executionFeedbackText.text = "Executing code...";
            executionFeedbackText.color = Color.blue;
        }
        
        // Parse and execute Python code
        // TODO: Integrate with actual Python interpreter
        // For now, use simplified execution
        
        try
        {
            // Parse code into commands
            List<PythonCommand> commands = ParsePythonCode(code);
            
            // Execute commands on basketball court
            StartCoroutine(ExecuteCommands(commands));
        }
        catch (System.Exception e)
        {
            ShowError($"Execution error: {e.Message}");
            isExecuting = false;
        }
    }
    
    List<PythonCommand> ParsePythonCode(string code)
    {
        List<PythonCommand> commands = new List<PythonCommand>();
        
        // Simple parser for basketball Python API
        // TODO: Replace with proper Python parser
        
        string[] lines = code.Split('\n');
        foreach (string line in lines)
        {
            string trimmed = line.Trim();
            if (string.IsNullOrEmpty(trimmed) || trimmed.StartsWith("#"))
            {
                continue;
            }
            
            // Parse function calls
            if (trimmed.Contains("dribble("))
            {
                commands.Add(ParseDribbleCall(trimmed));
            }
            else if (trimmed.Contains("pass_to("))
            {
                commands.Add(ParsePassCall(trimmed));
            }
            else if (trimmed.Contains("shoot()"))
            {
                commands.Add(new PythonCommand { function = "shoot", args = new object[0] });
            }
            else if (trimmed.Contains("move("))
            {
                commands.Add(ParseMoveCall(trimmed));
            }
        }
        
        return commands;
    }
    
    PythonCommand ParseDribbleCall(string line)
    {
        // Parse: dribble('move', 0.5)
        var match = Regex.Match(line, @"dribble\(['""]([^'""]+)['""]\s*,\s*([0-9.]+)\)");
        if (match.Success)
        {
            return new PythonCommand
            {
                function = "dribble",
                args = new object[] { match.Groups[1].Value, float.Parse(match.Groups[2].Value) }
            };
        }
        return null;
    }
    
    PythonCommand ParsePassCall(string line)
    {
        // Parse: pass_to('left')
        var match = Regex.Match(line, @"pass_to\(['""]([^'""]+)['""]\)");
        if (match.Success)
        {
            return new PythonCommand
            {
                function = "pass_to",
                args = new object[] { match.Groups[1].Value }
            };
        }
        return null;
    }
    
    PythonCommand ParseMoveCall(string line)
    {
        // Parse: move('right', 2.0)
        var match = Regex.Match(line, @"move\(['""]([^'""]+)['""]\s*,\s*([0-9.]+)\)");
        if (match.Success)
        {
            return new PythonCommand
            {
                function = "move",
                args = new object[] { match.Groups[1].Value, float.Parse(match.Groups[2].Value) }
            };
        }
        return null;
    }
    
    System.Collections.IEnumerator ExecuteCommands(List<PythonCommand> commands)
    {
        foreach (PythonCommand cmd in commands)
        {
            if (basketballFunctions.ContainsKey(cmd.function))
            {
                basketballFunctions[cmd.function](cmd.args);
                yield return new WaitForSeconds(0.5f); // Wait between commands
            }
        }
        
        // Check if solution is correct
        yield return new WaitForSeconds(1f);
        CheckSolution();
        isExecuting = false;
    }
    
    /// <summary>
    /// Execute dribble action on basketball court.
    /// Architecture: Connect to existing court visualization system (GameModeManager, TrainingModeManager).
    /// </summary>
    void ExecuteDribble(string action, float clock)
    {
        Debug.Log($"[PythonCodingManager] Executing dribble: {action}, clock: {clock}");
        // Architecture note: Connect to court visualization via GameModeManager or TrainingModeManager
        // This requires integration with the existing basketball court rendering system
    }
    
    /// <summary>
    /// Execute pass action on basketball court.
    /// Architecture: Connect to existing court visualization system.
    /// </summary>
    void ExecutePass(string direction)
    {
        Debug.Log($"[PythonCodingManager] Executing pass: {direction}");
        // Architecture note: Connect to court visualization via GameModeManager
    }
    
    /// <summary>
    /// Execute shoot action on basketball court.
    /// Architecture: Connect to existing court visualization system.
    /// </summary>
    void ExecuteShoot()
    {
        Debug.Log("[PythonCodingManager] Executing shoot");
        // Architecture note: Connect to court visualization via GameModeManager
    }
    
    /// <summary>
    /// Execute move action on basketball court.
    /// Architecture: Connect to existing court visualization system.
    /// </summary>
    void ExecuteMove(string direction, float distance)
    {
        Debug.Log($"[PythonCodingManager] Executing move: {direction}, distance: {distance}");
        // Architecture note: Connect to court visualization via GameModeManager
    }
    
    /// <summary>
    /// Execute conditional action on basketball court.
    /// Architecture: Connect to existing court visualization system.
    /// </summary>
    void ExecuteConditional(string condition, string action)
    {
        Debug.Log($"[PythonCodingManager] Executing conditional: if {condition} then {action}");
        // Architecture note: Connect to court visualization via GameModeManager
    }
    
    /// <summary>
    /// Execute loop action on basketball court.
    /// Architecture: Connect to existing court visualization system.
    /// </summary>
    void ExecuteLoop(int times, string action)
    {
        Debug.Log($"[PythonCodingManager] Executing loop: repeat {times} times: {action}");
        // Architecture note: Connect to court visualization via GameModeManager
    }
    
    void CheckSolution()
    {
        if (currentExercise == null)
        {
            return;
        }
        
        string code = pythonCodeInput != null ? pythonCodeInput.text : "";
        
        // Simple solution checking
        // TODO: Implement proper solution validation
        bool isCorrect = !string.IsNullOrEmpty(currentExercise.solutionCode) &&
                         code.Contains(currentExercise.solutionCode);
        
        if (isCorrect)
        {
            OnExerciseSuccess(100f);
        }
        else
        {
            ShowError("Code executed but didn't produce expected result. Try again!");
        }
    }
    
    void OnExerciseSuccess(float score)
    {
        if (executionFeedbackText != null)
        {
            executionFeedbackText.text = "✅ Success! Code executed correctly.";
            executionFeedbackText.color = Color.green;
        }
        
        // Track completion
        if (gameModeManager != null)
        {
            gameModeManager.OnExerciseComplete(true, score);
        }
    }
    
    void ShowError(string message)
    {
        if (executionFeedbackText != null)
        {
            executionFeedbackText.text = $"❌ {message}";
            executionFeedbackText.color = Color.red;
        }
    }
    
    void OnReset()
    {
        if (pythonCodeInput != null && currentExercise != null)
        {
            pythonCodeInput.text = currentExercise.starterCode ?? "";
        }
        
        if (syntaxFeedbackText != null)
        {
            syntaxFeedbackText.text = "Ready to code...";
            syntaxFeedbackText.color = Color.white;
        }
        
        if (executionFeedbackText != null)
        {
            executionFeedbackText.text = "";
        }
    }
    
    void OnShowSolution()
    {
        if (currentExercise != null && !string.IsNullOrEmpty(currentExercise.solutionCode))
        {
            if (pythonCodeInput != null)
            {
                pythonCodeInput.text = currentExercise.solutionCode;
            }
        }
    }
    
    void OnShowHint()
    {
        if (currentExercise != null && currentExercise.hints != null && currentExercise.hints.Length > 0)
        {
            // Show first hint
            string hint = currentExercise.hints[0];
            if (executionFeedbackText != null)
            {
                executionFeedbackText.text = $"💡 Hint: {hint}";
                executionFeedbackText.color = Color.yellow;
            }
        }
    }
    
    void OnShowBridge()
    {
        if (bridgePanel != null)
        {
            bridgePanel.SetActive(true);
        }
        
        // Show block code equivalent
        if (currentExercise != null && blockCodeText != null)
        {
            blockCodeText.text = currentExercise.blockCodeEquivalent ?? "No block code equivalent";
        }
        
        // Show Python code
        if (pythonCodeText != null && pythonCodeInput != null)
        {
            pythonCodeText.text = pythonCodeInput.text;
        }
    }
    
    void OnHideBridge()
    {
        if (bridgePanel != null)
        {
            bridgePanel.SetActive(false);
        }
    }
}

// Data structures
[System.Serializable]
public class PythonExerciseData
{
    public string exerciseId;
    public string title;
    public string description;
    public string storyContext;
    public string starterCode;
    public string solutionCode;
    public string blockCodeEquivalent; // For bridge view
    public string[] hints;
    public int difficultyLevel;
    public string codingConcept; // "sequences", "conditionals", "loops"
}

[System.Serializable]
public class PythonCommand
{
    public string function;
    public object[] args;
}

// Simple Python interpreter wrapper
// TODO: Replace with actual Python integration
public class PythonInterpreter
{
    public void Execute(string code)
    {
        // TODO: Integrate with Unity Python library or custom interpreter
        Debug.Log($"[PythonInterpreter] Executing: {code}");
    }
}

