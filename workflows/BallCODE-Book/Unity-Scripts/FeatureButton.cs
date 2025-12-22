using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using DG.Tweening;

/// <summary>
/// Feature Button Component - For Leaderboard and Settings buttons
/// Card-style design with colored icons
/// </summary>
public class FeatureButton : ImprovedButton
{
    [Header("Feature Settings")]
    public FeatureType featureType = FeatureType.Leaderboard;
    public Image featureIcon; // Icon image component
    
    public enum FeatureType
    {
        Leaderboard,
        Settings
    }
    
    void Start()
    {
        // Configure as neutral button (card style)
        buttonType = ButtonType.Neutral;
        buttonText = featureType.ToString();
        
        // Set size for feature buttons (120x120px - square)
        if (buttonRect != null)
        {
            buttonRect.sizeDelta = new Vector2(120, 120);
        }
        
        // Set icon color based on feature type
        if (featureIcon != null)
        {
            if (featureType == FeatureType.Leaderboard)
            {
                // Gold trophy color
                featureIcon.color = new Color(1f, 0.84f, 0f); // #FFD700
            }
            else // Settings
            {
                // Gray gear color
                featureIcon.color = new Color(0.4f, 0.4f, 0.4f); // #666666
            }
        }
        
        // Set background to white with shadow (card style)
        if (buttonBackground != null)
        {
            buttonBackground.color = Color.white;
        }
        
        // Increase hover scale for feature buttons
        hoverScale = 1.1f;
    }
    
    public override void OnPointerEnter(PointerEventData eventData)
    {
        base.OnPointerEnter(eventData);
        
        // Enhance icon color on hover
        if (featureIcon != null)
        {
            Color currentColor = featureIcon.color;
            Color hoverColor = new Color(
                Mathf.Min(1f, currentColor.r * 1.2f),
                Mathf.Min(1f, currentColor.g * 1.2f),
                Mathf.Min(1f, currentColor.b * 1.2f)
            );
            featureIcon.DOColor(hoverColor, animationDuration);
        }
    }
    
    public override void OnPointerExit(PointerEventData eventData)
    {
        base.OnPointerExit(eventData);
        
        // Restore icon color
        if (featureIcon != null)
        {
            Color originalColor = featureType == FeatureType.Leaderboard 
                ? new Color(1f, 0.84f, 0f) 
                : new Color(0.4f, 0.4f, 0.4f);
            featureIcon.DOColor(originalColor, animationDuration);
        }
    }
}

