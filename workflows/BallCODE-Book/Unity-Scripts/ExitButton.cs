using UnityEngine;
using UnityEngine.EventSystems;
using DG.Tweening;

/// <summary>
/// Exit Button Component - Top-left exit button
/// Larger, more visible, with orange hover effect
/// </summary>
public class ExitButton : ImprovedButton
{
    void Start()
    {
        // Configure as neutral button
        buttonType = ButtonType.Neutral;
        buttonText = ""; // Icon only, no text
        
        // Set size for exit button (60x60px)
        if (buttonRect != null)
        {
            buttonRect.sizeDelta = new Vector2(60, 60);
        }
        
        // Set background color
        if (buttonBackground != null)
        {
            buttonBackground.color = neutralColor; // Light gray #F5F5F5
            originalColor = neutralColor;
        }
    }
    
    public override void OnPointerEnter(PointerEventData eventData)
    {
        isHovering = true;
        
        // Hover animation - scale up
        if (buttonRect != null)
        {
            buttonRect.DOScale(originalScale * hoverScale, animationDuration)
                .SetEase(Ease.OutQuad);
        }
        
        // Orange tint on hover
        if (buttonBackground != null)
        {
            Color hoverColor = new Color(1f, 0.96f, 0.95f); // Light orange tint #FFF5F2
            buttonBackground.DOColor(hoverColor, animationDuration);
        }
    }
    
    public override void OnPointerExit(PointerEventData eventData)
    {
        isHovering = false;
        
        // Return to normal
        if (buttonRect != null)
        {
            buttonRect.DOScale(originalScale, animationDuration)
                .SetEase(Ease.OutQuad);
        }
        
        // Return to neutral color
        if (buttonBackground != null)
        {
            buttonBackground.DOColor(neutralColor, animationDuration);
        }
    }
}

