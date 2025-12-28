using UnityEngine;
using UnityEngine.UI;
using UnityEditor;
using TMPro;

/// <summary>
/// UI/UX Button Setup Helper - Automatically applies improved button components
/// Usage: Select button GameObject → Right-click → UI → Apply UI/UX Improvements
/// </summary>
public class UIUXButtonSetupHelper : EditorWindow
{
    [MenuItem("UI/Apply UI/UX Improvements to Selected Buttons")]
    public static void ApplyUIUXImprovements()
    {
        GameObject[] selected = Selection.gameObjects;
        
        if (selected.Length == 0)
        {
            EditorUtility.DisplayDialog("No Selection", 
                "Please select one or more button GameObjects in the Hierarchy.", 
                "OK");
            return;
        }
        
        int applied = 0;
        foreach (GameObject obj in selected)
        {
            Button button = obj.GetComponent<Button>();
            if (button == null)
            {
                Debug.LogWarning($"[UIUXButtonSetupHelper] {obj.name} doesn't have a Button component. Skipping.");
                continue;
            }
            
            // Determine button type based on name or existing components
            string buttonName = obj.name.ToLower();
            
            // Check if it's a game mode button (Chess, Coding, Freeplay, Mathlete)
            if (buttonName.Contains("chess") || buttonName.Contains("coding") || 
                buttonName.Contains("freeplay") || buttonName.Contains("mathlete") ||
                buttonName.Contains("book"))
            {
                ApplyGameModeButton(obj);
                applied++;
            }
            // Check if it's a main action button (BallCode, Skins)
            else if (buttonName.Contains("ballcode") || buttonName.Contains("ball code"))
            {
                ApplyMainActionButton(obj, MainActionButton.MainActionType.BallCode);
                applied++;
            }
            else if (buttonName.Contains("skin"))
            {
                ApplyMainActionButton(obj, MainActionButton.MainActionType.Skins);
                applied++;
            }
            // Check if it's a feature button (Leaderboard, Settings)
            else if (buttonName.Contains("leaderboard") || buttonName.Contains("trophy"))
            {
                ApplyFeatureButton(obj, FeatureButton.FeatureType.Leaderboard);
                applied++;
            }
            else if (buttonName.Contains("setting") || buttonName.Contains("gear"))
            {
                ApplyFeatureButton(obj, FeatureButton.FeatureType.Settings);
                applied++;
            }
            // Check if it's exit button
            else if (buttonName.Contains("exit") || buttonName.Contains("close"))
            {
                ApplyExitButton(obj);
                applied++;
            }
            else
            {
                // Default: Apply ImprovedButton
                ApplyImprovedButton(obj);
                applied++;
            }
        }
        
        EditorUtility.DisplayDialog("UI/UX Improvements Applied", 
            $"Applied improvements to {applied} button(s).\n\n" +
            "Note: You may need to configure button settings in Inspector.", 
            "OK");
    }
    
    static void ApplyGameModeButton(GameObject obj)
    {
        // Remove old ImprovedButton if exists
        ImprovedButton oldImproved = obj.GetComponent<ImprovedButton>();
        if (oldImproved != null && !(oldImproved is GameModeButton))
        {
            DestroyImmediate(oldImproved);
        }
        
        // Add or get GameModeButton
        GameModeButton gameModeBtn = obj.GetComponent<GameModeButton>();
        if (gameModeBtn == null)
        {
            gameModeBtn = obj.AddComponent<GameModeButton>();
        }
        
        // Set game mode based on name
        string name = obj.name.ToLower();
        if (name.Contains("chess"))
            gameModeBtn.gameMode = GameModeButton.GameMode.Chess;
        else if (name.Contains("coding"))
            gameModeBtn.gameMode = GameModeButton.GameMode.Coding;
        else if (name.Contains("freeplay"))
            gameModeBtn.gameMode = GameModeButton.GameMode.Freeplay;
        else if (name.Contains("mathlete"))
            gameModeBtn.gameMode = GameModeButton.GameMode.Mathlete;
        else if (name.Contains("book"))
            gameModeBtn.gameMode = GameModeButton.GameMode.Book;
        
        // Setup references
        SetupButtonReferences(obj, gameModeBtn);
        
        Debug.Log($"[UIUXButtonSetupHelper] Applied GameModeButton to {obj.name}");
    }
    
    static void ApplyMainActionButton(GameObject obj, MainActionButton.MainActionType actionType)
    {
        // Remove old ImprovedButton if exists
        ImprovedButton oldImproved = obj.GetComponent<ImprovedButton>();
        if (oldImproved != null && !(oldImproved is MainActionButton))
        {
            DestroyImmediate(oldImproved);
        }
        
        // Add or get MainActionButton
        MainActionButton mainActionBtn = obj.GetComponent<MainActionButton>();
        if (mainActionBtn == null)
        {
            mainActionBtn = obj.AddComponent<MainActionButton>();
        }
        
        mainActionBtn.actionType = actionType;
        
        // Setup references
        SetupButtonReferences(obj, mainActionBtn);
        
        Debug.Log($"[UIUXButtonSetupHelper] Applied MainActionButton ({actionType}) to {obj.name}");
    }
    
    static void ApplyFeatureButton(GameObject obj, FeatureButton.FeatureType featureType)
    {
        // Remove old ImprovedButton if exists
        ImprovedButton oldImproved = obj.GetComponent<ImprovedButton>();
        if (oldImproved != null && !(oldImproved is FeatureButton))
        {
            DestroyImmediate(oldImproved);
        }
        
        // Add or get FeatureButton
        FeatureButton featureBtn = obj.GetComponent<FeatureButton>();
        if (featureBtn == null)
        {
            featureBtn = obj.AddComponent<FeatureButton>();
        }
        
        featureBtn.featureType = featureType;
        
        // Setup references
        SetupButtonReferences(obj, featureBtn);
        
        // Try to find icon image
        Image[] images = obj.GetComponentsInChildren<Image>();
        foreach (Image img in images)
        {
            if (img.gameObject != obj && img.sprite != null)
            {
                featureBtn.featureIcon = img;
                break;
            }
        }
        
        Debug.Log($"[UIUXButtonSetupHelper] Applied FeatureButton ({featureType}) to {obj.name}");
    }
    
    static void ApplyExitButton(GameObject obj)
    {
        // Remove old ImprovedButton if exists
        ImprovedButton oldImproved = obj.GetComponent<ImprovedButton>();
        if (oldImproved != null && !(oldImproved is ExitButton))
        {
            DestroyImmediate(oldImproved);
        }
        
        // Add or get ExitButton
        ExitButton exitBtn = obj.GetComponent<ExitButton>();
        if (exitBtn == null)
        {
            exitBtn = obj.AddComponent<ExitButton>();
        }
        
        // Setup references
        SetupButtonReferences(obj, exitBtn);
        
        Debug.Log($"[UIUXButtonSetupHelper] Applied ExitButton to {obj.name}");
    }
    
    static void ApplyImprovedButton(GameObject obj)
    {
        // Add or get ImprovedButton
        ImprovedButton improvedBtn = obj.GetComponent<ImprovedButton>();
        if (improvedBtn == null)
        {
            improvedBtn = obj.AddComponent<ImprovedButton>();
        }
        
        // Setup references
        SetupButtonReferences(obj, improvedBtn);
        
        Debug.Log($"[UIUXButtonSetupHelper] Applied ImprovedButton to {obj.name}");
    }
    
    static void SetupButtonReferences(GameObject obj, ImprovedButton button)
    {
        // Find or create button background
        if (button.buttonBackground == null)
        {
            button.buttonBackground = obj.GetComponent<Image>();
            if (button.buttonBackground == null)
            {
                button.buttonBackground = obj.AddComponent<Image>();
            }
        }
        
        // Find button rect
        if (button.buttonRect == null)
        {
            button.buttonRect = obj.GetComponent<RectTransform>();
        }
        
        // Find text component
        if (button.buttonTextComponent == null)
        {
            button.buttonTextComponent = obj.GetComponentInChildren<TextMeshProUGUI>();
        }
        
        // Set button text from TextMeshProUGUI if exists
        if (button.buttonTextComponent != null && string.IsNullOrEmpty(button.buttonText))
        {
            button.buttonText = button.buttonTextComponent.text;
        }
    }
}


