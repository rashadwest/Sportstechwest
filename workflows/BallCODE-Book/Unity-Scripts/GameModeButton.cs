using UnityEngine;

/// <summary>
/// Game Mode Button Component - For Chess, Coding, Freeplay, Mathlete buttons
/// Card-style design with selection states and orange glow when selected
/// </summary>
public class GameModeButton : ImprovedButton
{
    [Header("Game Mode Settings")]
    public GameMode gameMode = GameMode.Coding;
    
    public enum GameMode
    {
        Chess,
        Coding,
        Freeplay,
        Mathlete
    }
    
    void Start()
    {
        // Configure as neutral button with selection state
        buttonType = ButtonType.Neutral;
        showSelectionState = true;
        enableGlow = true;
        
        // Set button text based on game mode
        buttonText = gameMode.ToString();
        
        // Set size for game mode buttons (180x100px)
        if (buttonRect != null)
        {
            buttonRect.sizeDelta = new Vector2(180, 100);
        }
        
        // Initialize selection state
        UpdateSelectionState();
    }
    
    public void SelectMode()
    {
        // Deselect all other game mode buttons
        GameModeButton[] allModeButtons = FindObjectsOfType<GameModeButton>();
        foreach (GameModeButton btn in allModeButtons)
        {
            if (btn != this)
            {
                btn.SetSelected(false);
            }
        }
        
        // Select this button
        SetSelected(true);
    }
}

