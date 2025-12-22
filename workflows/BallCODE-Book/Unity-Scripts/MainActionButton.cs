using UnityEngine;

/// <summary>
/// Main Action Button Component - For BallCode and Skins buttons
/// Enhanced with stronger glow, pulsing animation, and better visual hierarchy
/// </summary>
public class MainActionButton : ImprovedButton
{
    [Header("Main Action Settings")]
    public MainActionType actionType = MainActionType.BallCode;
    
    public enum MainActionType
    {
        BallCode,
        Skins
    }
    
    void Start()
    {
        // Configure based on action type
        if (actionType == MainActionType.BallCode)
        {
            buttonType = ButtonType.Primary;
            buttonText = "BallCode";
            enablePulseAnimation = true;
            enableGlow = true;
            glowIntensity = 0.5f;
            pulseSpeed = 2f;
        }
        else // Skins
        {
            buttonType = ButtonType.Secondary;
            buttonText = "Skins";
            enableGlow = true;
            glowIntensity = 0.3f;
            glowColor = secondaryColor;
        }
        
        // Set size for main action buttons (280x180px)
        if (buttonRect != null)
        {
            buttonRect.sizeDelta = new Vector2(280, 180);
        }
        
        // Increase hover scale for main buttons
        hoverScale = 1.08f;
    }
}

