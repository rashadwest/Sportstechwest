using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using TMPro;
using DG.Tweening;

/// <summary>
/// Improved Button Component - Duolingo/Steve Jobs Inspired
/// Tasteful, kid-friendly buttons with smooth animations
/// Enhanced with selection states, glow effects, and better styling
/// </summary>
public class ImprovedButton : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler, IPointerClickHandler
{
    [Header("Button Style")]
    public ButtonType buttonType = ButtonType.Primary;
    public string buttonText = "Button";
    
    [Header("References")]
    public Image buttonBackground;
    public Image buttonBorder; // Optional border image
    public Image glowEffect; // Optional glow overlay
    public TextMeshProUGUI buttonTextComponent;
    public RectTransform buttonRect;
    
    [Header("Colors")]
    public Color primaryColor = new Color(1f, 0.42f, 0.21f); // Orange #FF6B35
    public Color secondaryColor = new Color(0.31f, 0.80f, 0.77f); // Blue #4ECDC4
    public Color successColor = new Color(0.18f, 0.80f, 0.44f); // Green #2ECC71
    public Color neutralColor = new Color(0.96f, 0.96f, 0.96f); // Light gray #F5F5F5
    
    [Header("Selection State")]
    public bool isSelected = false;
    public bool showSelectionState = false;
    public Color selectedBorderColor = new Color(1f, 0.42f, 0.21f); // Orange border
    public float selectedGlowIntensity = 0.5f;
    
    [Header("Animation")]
    public float hoverScale = 1.05f;
    public float clickScale = 0.95f;
    public float animationDuration = 0.3f;
    public bool enablePulseAnimation = false;
    public float pulseSpeed = 2f;
    
    [Header("Glow Effect")]
    public bool enableGlow = false;
    public float glowIntensity = 0.3f;
    public Color glowColor = new Color(1f, 0.42f, 0.21f, 0.5f);
    
    public enum ButtonType
    {
        Primary,    // Orange, main action
        Secondary,  // Blue, secondary action
        Success,    // Green, positive action
        Neutral     // White/light gray, for game mode buttons
    }
    
    protected Vector3 originalScale;
    protected Color originalColor;
    protected bool isHovering = false;
    protected float pulseTimer = 0f;
    
    protected virtual void Start()
    {
        if (buttonRect == null)
            buttonRect = GetComponent<RectTransform>();
        
        if (buttonBackground == null)
            buttonBackground = GetComponent<Image>();
        
        originalScale = buttonRect.localScale;
        SetupButton();
    }
    
    void SetupButton()
    {
        // Set button color based on type
        Color buttonColor = buttonType switch
        {
            ButtonType.Primary => primaryColor,
            ButtonType.Secondary => secondaryColor,
            ButtonType.Success => successColor,
            ButtonType.Neutral => Color.white,
            _ => primaryColor
        };
        
        originalColor = buttonColor;
        
        // Apply selection state if enabled
        if (showSelectionState && isSelected)
        {
            buttonBackground.color = Color.white;
            if (buttonBorder != null)
            {
                buttonBorder.color = selectedBorderColor;
                buttonBorder.gameObject.SetActive(true);
            }
            if (glowEffect != null && enableGlow)
            {
                glowEffect.color = new Color(selectedBorderColor.r, selectedBorderColor.g, selectedBorderColor.b, selectedGlowIntensity);
                glowEffect.gameObject.SetActive(true);
            }
        }
        else
        {
            buttonBackground.color = buttonColor;
            if (buttonBorder != null)
                buttonBorder.gameObject.SetActive(false);
            if (glowEffect != null && !enableGlow)
                glowEffect.gameObject.SetActive(false);
        }
        
        // Set text
        if (buttonTextComponent != null)
        {
            buttonTextComponent.text = buttonText;
            // Text color based on button type
            if (buttonType == ButtonType.Neutral || (showSelectionState && !isSelected))
                buttonTextComponent.color = new Color(0.2f, 0.2f, 0.2f); // Dark gray
            else
                buttonTextComponent.color = Color.white;
            buttonTextComponent.fontSize = 22;
            buttonTextComponent.fontStyle = FontStyles.Bold;
        }
        
        // Set size (touch-friendly, min 200x60)
        if (buttonRect != null)
        {
            if (buttonRect.sizeDelta.x < 200)
                buttonRect.sizeDelta = new Vector2(200, buttonRect.sizeDelta.y);
            if (buttonRect.sizeDelta.y < 60)
                buttonRect.sizeDelta = new Vector2(buttonRect.sizeDelta.x, 60);
        }
    }
    
    private bool selectionStateDirty = false;
    
    void Update()
    {
        // Pulse animation for selected buttons or primary buttons
        if (enablePulseAnimation && (isSelected || buttonType == ButtonType.Primary))
        {
            pulseTimer += Time.deltaTime * pulseSpeed;
            
            if (glowEffect != null && glowEffect.gameObject.activeSelf)
            {
                float alpha = selectedGlowIntensity + Mathf.Sin(pulseTimer) * 0.2f;
                Color pulseColor = glowEffect.color;
                pulseColor.a = Mathf.Clamp01(alpha);
                glowEffect.color = pulseColor;
            }
        }
        
        // Update selection state only if changed externally (event-driven)
        if (selectionStateDirty && showSelectionState)
        {
            UpdateSelectionState();
            selectionStateDirty = false;
        }
    }
    
    public void SetSelected(bool selected)
    {
        if (isSelected != selected)
        {
            isSelected = selected;
            selectionStateDirty = true;
            UpdateSelectionState();
        }
    }
    
    protected void UpdateSelectionState()
    {
        if (isSelected)
        {
            buttonBackground.color = Color.white;
            if (buttonBorder != null)
            {
                buttonBorder.color = selectedBorderColor;
                buttonBorder.gameObject.SetActive(true);
            }
            if (glowEffect != null)
            {
                glowEffect.color = new Color(selectedBorderColor.r, selectedBorderColor.g, selectedBorderColor.b, selectedGlowIntensity);
                glowEffect.gameObject.SetActive(true);
            }
            if (buttonTextComponent != null)
                buttonTextComponent.color = selectedBorderColor; // Orange text when selected
        }
        else
        {
            buttonBackground.color = originalColor;
            if (buttonBorder != null)
                buttonBorder.gameObject.SetActive(false);
            if (glowEffect != null && !enableGlow)
                glowEffect.gameObject.SetActive(false);
            if (buttonTextComponent != null)
            {
                if (buttonType == ButtonType.Neutral)
                    buttonTextComponent.color = new Color(0.2f, 0.2f, 0.2f);
                else
                    buttonTextComponent.color = Color.white;
            }
        }
    }
    
    public virtual void OnPointerEnter(PointerEventData eventData)
    {
        isHovering = true;
        
        // Hover animation - scale up
        if (buttonRect != null)
        {
            buttonRect.DOScale(originalScale * hoverScale, animationDuration)
                .SetEase(Ease.OutQuad);
        }
        
        // Enhanced hover effects
        if (buttonBackground != null)
        {
            Color hoverColor;
            if (buttonType == ButtonType.Neutral || (showSelectionState && !isSelected))
            {
                // Light orange tint on hover for neutral buttons
                hoverColor = new Color(1f, 0.96f, 0.95f); // #FFF5F2
            }
            else
            {
                // Brighten color for colored buttons
                hoverColor = new Color(
                    Mathf.Min(1f, originalColor.r * 1.2f),
                    Mathf.Min(1f, originalColor.g * 1.2f),
                    Mathf.Min(1f, originalColor.b * 1.2f)
                );
            }
            buttonBackground.DOColor(hoverColor, animationDuration);
        }
        
        // Increase glow on hover
        if (glowEffect != null && glowEffect.gameObject.activeSelf)
        {
            Color currentGlow = glowEffect.color;
            Color hoverGlow = new Color(currentGlow.r, currentGlow.g, currentGlow.b, Mathf.Min(1f, currentGlow.a * 1.5f));
            glowEffect.DOColor(hoverGlow, animationDuration);
        }
    }
    
    public virtual void OnPointerExit(PointerEventData eventData)
    {
        isHovering = false;
        
        // Return to normal
        if (buttonRect != null)
        {
            buttonRect.DOScale(originalScale, animationDuration)
                .SetEase(Ease.OutQuad);
        }
        
        // Restore original color
        if (buttonBackground != null)
        {
            Color restoreColor = (showSelectionState && isSelected) ? Color.white : originalColor;
            buttonBackground.DOColor(restoreColor, animationDuration);
        }
        
        // Restore glow
        if (glowEffect != null && glowEffect.gameObject.activeSelf)
        {
            Color originalGlow = new Color(glowEffect.color.r, glowEffect.color.g, glowEffect.color.b, 
                isSelected ? selectedGlowIntensity : glowIntensity);
            glowEffect.DOColor(originalGlow, animationDuration);
        }
    }
    
    public void OnPointerClick(PointerEventData eventData)
    {
        // Click animation - quick scale down then up (bounce effect)
        if (buttonRect != null)
        {
            Sequence clickSequence = DOTween.Sequence();
            clickSequence.Append(buttonRect.DOScale(originalScale * clickScale, 0.1f).SetEase(Ease.OutQuad));
            clickSequence.Append(buttonRect.DOScale(originalScale * 1.05f, 0.15f).SetEase(Ease.OutQuad));
            clickSequence.Append(buttonRect.DOScale(originalScale, 0.1f).SetEase(Ease.OutQuad));
        }
        
        // Play sound (if ButtonBehaviour is attached)
        ButtonBehaviour buttonBehaviour = GetComponent<ButtonBehaviour>();
        if (buttonBehaviour == null)
        {
            // Try to find it in children
            buttonBehaviour = GetComponentInChildren<ButtonBehaviour>();
        }
        // Sound will be handled by ButtonBehaviour if it exists
    }
}
