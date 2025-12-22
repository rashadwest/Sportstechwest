#!/usr/bin/env python3
"""
Unity Game Landing Page UI/UX Improvement
Using AIMCODE + Steve Jobs + Duolingo Principles

Copyright © 2025 Rashad West. All Rights Reserved.
"""

from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).parent.parent
UNITY_SCRIPTS = PROJECT_ROOT / "Unity-Scripts"

# Steve Jobs + Duolingo Design Principles
DESIGN_PRINCIPLES = {
    "simplicity": "Remove everything unnecessary - one clear action per screen",
    "delight": "Make it fun, not just functional - colorful, playful",
    "user_experience": "Make it obvious - big, clear buttons",
    "details": "Every pixel counts - perfect alignment, consistent spacing"
}

def print_header(title):
    """Print formatted header."""
    print("\n" + "=" * 70)
    print(f"🎮 {title}")
    print("=" * 70)

def analyze_current_ui():
    """ANALYZE: Review current Unity UI structure."""
    print_header("ANALYZE: Current Unity UI Structure")
    
    issues = []
    
    # Check Unity scripts for UI references
    ui_files = list(UNITY_SCRIPTS.rglob("*.cs"))
    print(f"\n📄 Found {len(ui_files)} Unity C# scripts")
    
    for script_file in ui_files:
        try:
            with open(script_file, 'r', encoding='utf-8') as f:
                content = f.read()
                relative_path = script_file.relative_to(PROJECT_ROOT)
                
                # Look for UI/Button references
                if 'Button' in content or 'UI' in content:
                    # Check for bottom-left positioning
                    if 'bottom' in content.lower() or 'left' in content.lower():
                        issues.append({
                            'file': str(relative_path),
                            'issue': 'Contains bottom/left UI references',
                            'type': 'positioning'
                        })
                    
                    # Check for button styling
                    if 'button' in content.lower():
                        issues.append({
                            'file': str(relative_path),
                            'issue': 'Contains button references',
                            'type': 'button'
                        })
        except Exception as e:
            print(f"   ⚠️  Error reading {script_file}: {e}")
    
    return issues

def ideate_improvements():
    """IDEATE: Design improvements using Steve Jobs + Duolingo principles."""
    print_header("IDEATE: UI/UX Improvements")
    
    improvements = {
        "button_redesign": {
            "principle": "delight + user_experience",
            "issues": [
                "Bottom-left buttons not tasteful",
                "Buttons don't match overall design"
            ],
            "solutions": [
                "Redesign buttons with Duolingo-style: big, colorful, rounded",
                "Move buttons to better position (center-bottom or right-side)",
                "Add hover animations and feedback",
                "Use consistent color scheme (orange/blue from website)",
                "Add icons to buttons for clarity"
            ]
        },
        "overall_cohesion": {
            "principle": "simplicity + details",
            "issues": [
                "UI elements don't go together",
                "Inconsistent styling"
            ],
            "solutions": [
                "Create unified design system (colors, fonts, spacing)",
                "Use 8px grid system for spacing",
                "Standardize button sizes and styles",
                "Add visual hierarchy (clear primary/secondary actions)",
                "Improve typography consistency"
            ]
        },
        "kid_friendly": {
            "principle": "delight",
            "issues": [
                "Not playful enough",
                "Missing fun elements"
            ],
            "solutions": [
                "Add colorful backgrounds/gradients",
                "Use friendly, encouraging language",
                "Add celebration animations",
                "Include progress indicators",
                "Add character/mascot presence"
            ]
        }
    }
    
    return improvements

def create_unity_ui_improvement_guide():
    """Create comprehensive Unity UI improvement guide."""
    print_header("MODEL: Creating Unity UI Improvement Guide")
    
    guide = """# 🎮 Unity Game Landing Page UI/UX Improvement Guide

**Date:** December 17, 2025  
**Methodology:** AIMCODE + Steve Jobs + Duolingo Principles  
**Focus:** Landing page buttons (bottom-left) and overall UI cohesion

---

## 🎯 ISSUES IDENTIFIED

### 1. Bottom-Left Buttons Not Tasteful
- **Current:** Buttons in bottom-left corner
- **Problem:** Not visually appealing, doesn't match design
- **Impact:** Poor first impression, not kid-friendly

### 2. Overall UI/UX Not Cohesive
- **Current:** UI elements don't work together
- **Problem:** Inconsistent styling, colors, spacing
- **Impact:** Confusing, unprofessional appearance

---

## ✅ IMPROVEMENTS (Steve Jobs + Duolingo)

### Phase 1: Button Redesign

#### 1.1 Move Buttons to Better Position
**Steve Jobs:** "Make it obvious"

**Options:**
- **Option A:** Center-bottom (most common, Duolingo-style)
  - Primary action in center
  - Secondary actions on sides
  - Clear visual hierarchy

- **Option B:** Right-side vertical (modern, clean)
  - Stack buttons vertically
  - More space for content
  - Less cluttered

- **Option C:** Top-right corner (minimal, elegant)
  - Small, unobtrusive
  - More screen space
  - Modern approach

**Recommendation:** Center-bottom (Option A) - most kid-friendly

#### 1.2 Redesign Button Style
**Duolingo-Inspired:**
- **Size:** Big, touch-friendly (min 100x50px)
- **Shape:** Rounded corners (12-16px radius)
- **Colors:** 
  - Primary: Orange (#FF6B35) - main action
  - Secondary: Blue (#4ECDC4) - secondary action
  - Success: Green (#2ECC71) - positive action
- **Typography:** Bold, clear font (18-24px)
- **Spacing:** 16px between buttons
- **Shadow:** Subtle drop shadow for depth

#### 1.3 Add Button Animations
**Steve Jobs:** "Delight the user"

**Animations:**
- **Hover:** Slight scale up (1.05x) + shadow increase
- **Click:** Scale down (0.95x) + color brighten
- **Success:** Celebration animation (confetti, bounce)
- **Transitions:** Smooth (0.3s ease)

---

### Phase 2: Overall UI Cohesion

#### 2.1 Create Design System
**Steve Jobs:** "Details matter"

**Color Palette:**
```csharp
// Primary Colors
public static Color PrimaryOrange = new Color(1f, 0.42f, 0.21f); // #FF6B35
public static Color PrimaryBlue = new Color(0.31f, 0.80f, 0.77f); // #4ECDC4
public static Color PrimaryGreen = new Color(0.58f, 0.88f, 0.83f); // #95E1D3

// Accent Colors
public static Color AccentYellow = new Color(1f, 0.90f, 0.43f); // #FFE66D
public static Color AccentPink = new Color(1f, 0.55f, 0.58f); // #FF8B94

// Neutral Colors
public static Color NeutralDark = new Color(0.17f, 0.24f, 0.31f); // #2C3E50
public static Color NeutralLight = new Color(0.93f, 0.94f, 0.95f); // #ECF0F1
```

**Typography:**
- **Headings:** Bold, 32-48px
- **Body:** Regular, 18-24px
- **Buttons:** Bold, 20-24px
- **Font:** Montserrat or Nunito (friendly, readable)

**Spacing (8px Grid):**
- **XS:** 4px
- **SM:** 8px
- **MD:** 16px
- **LG:** 24px
- **XL:** 32px
- **XXL:** 48px

#### 2.2 Standardize Button Component
**Create reusable button prefab:**

```csharp
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using DG.Tweening; // For animations (or use Unity's built-in)

public class ImprovedButton : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler, IPointerClickHandler
{
    [Header("Button Style")]
    public ButtonType buttonType = ButtonType.Primary;
    public string buttonText = "Button";
    
    [Header("References")]
    public Image buttonBackground;
    public TextMeshProUGUI buttonTextComponent;
    public RectTransform buttonRect;
    
    [Header("Colors")]
    public Color primaryColor = new Color(1f, 0.42f, 0.21f); // Orange
    public Color secondaryColor = new Color(0.31f, 0.80f, 0.77f); // Blue
    public Color hoverColor = new Color(1f, 0.50f, 0.30f); // Lighter orange
    
    [Header("Animation")]
    public float hoverScale = 1.05f;
    public float clickScale = 0.95f;
    public float animationDuration = 0.3f;
    
    public enum ButtonType
    {
        Primary,    // Orange, main action
        Secondary,  // Blue, secondary action
        Success,    // Green, positive action
        Danger      // Red, warning action
    }
    
    void Start()
    {
        SetupButton();
    }
    
    void SetupButton()
    {
        // Set button color based on type
        Color buttonColor = buttonType switch
        {
            ButtonType.Primary => primaryColor,
            ButtonType.Secondary => secondaryColor,
            ButtonType.Success => new Color(0.18f, 0.80f, 0.44f), // Green
            ButtonType.Danger => new Color(0.91f, 0.30f, 0.24f), // Red
            _ => primaryColor
        };
        
        buttonBackground.color = buttonColor;
        
        // Set text
        if (buttonTextComponent != null)
        {
            buttonTextComponent.text = buttonText;
            buttonTextComponent.color = Color.white;
            buttonTextComponent.fontSize = 22;
            buttonTextComponent.fontStyle = FontStyles.Bold;
        }
        
        // Set rounded corners (requires Image component with Sprite)
        // You'll need to create a rounded rectangle sprite or use a shader
        
        // Set size (touch-friendly)
        if (buttonRect != null)
        {
            buttonRect.sizeDelta = new Vector2(200, 60); // Big, touch-friendly
        }
    }
    
    public void OnPointerEnter(PointerEventData eventData)
    {
        // Hover animation
        buttonRect.DOScale(hoverScale, animationDuration);
        buttonBackground.DOColor(hoverColor, animationDuration);
    }
    
    public void OnPointerExit(PointerEventData eventData)
    {
        // Return to normal
        buttonRect.DOScale(1f, animationDuration);
        Color normalColor = buttonType switch
        {
            ButtonType.Primary => primaryColor,
            ButtonType.Secondary => secondaryColor,
            ButtonType.Success => new Color(0.18f, 0.80f, 0.44f),
            ButtonType.Danger => new Color(0.91f, 0.30f, 0.24f),
            _ => primaryColor
        };
        buttonBackground.DOColor(normalColor, animationDuration);
    }
    
    public void OnPointerClick(PointerEventData eventData)
    {
        // Click animation
        buttonRect.DOScale(clickScale, 0.1f).OnComplete(() => {
            buttonRect.DOScale(1f, 0.1f);
        });
    }
}
```

#### 2.3 Improve Landing Page Layout
**Steve Jobs:** "Simplicity is the ultimate sophistication"

**Recommended Layout:**
```
┌─────────────────────────────────────┐
│  [Logo/Title]                        │
│                                      │
│  [Main Content Area]                 │
│  - Game preview                      │
│  - Character/mascot                   │
│  - Fun illustration                  │
│                                      │
│                                      │
│  ┌─────────┐  ┌─────────┐  ┌──────┐│
│  │ Primary │  │Secondary│  │  ... ││
│  │ Button  │  │ Button  │  │      ││
│  └─────────┘  └─────────┘  └──────┘│
│      ↑                              │
│   Center-Bottom (Recommended)        │
└─────────────────────────────────────┘
```

**Alternative (Right-Side):**
```
┌──────────────────────────┬─────────┐
│                          │ [Btn 1] │
│  [Main Content]          │ [Btn 2] │
│                          │ [Btn 3] │
│                          │   ...   │
└──────────────────────────┴─────────┘
```

---

### Phase 3: Kid-Friendly Enhancements

#### 3.1 Add Visual Elements
- **Background:** Colorful gradient or pattern
- **Characters:** Mascot/character presence
- **Illustrations:** Fun, playful graphics
- **Animations:** Subtle, delightful movements

#### 3.2 Friendly Language
- "Let's Play!" instead of "Start"
- "Continue Learning" instead of "Resume"
- "You're doing great!" encouragement
- "Keep going!" motivation

#### 3.3 Progress Indicators
- Visual progress bar
- Streak counter
- Achievement badges
- Level completion celebrations

---

## 🔧 IMPLEMENTATION STEPS

### Step 1: Create Button Prefab
1. Create new GameObject: `ImprovedButton`
2. Add `Image` component (background)
3. Add `TextMeshProUGUI` component (text)
4. Add `ImprovedButton` script
5. Style with colors, rounded corners
6. Save as prefab

### Step 2: Update Landing Page
1. Open landing page scene
2. Remove old bottom-left buttons
3. Create new button container (center-bottom or right-side)
4. Add improved buttons using prefab
5. Position with proper spacing (16px between buttons)

### Step 3: Apply Design System
1. Create `DesignSystem.cs` script with color constants
2. Apply colors to all UI elements
3. Standardize fonts and sizes
4. Apply 8px grid spacing

### Step 4: Add Animations
1. Install DOTween (or use Unity's built-in)
2. Add hover/click animations
3. Test on mobile and desktop

### Step 5: Test & Polish
1. Test on different screen sizes
2. Verify touch targets (min 44x44px)
3. Check color contrast
4. Test animations
5. Get feedback

---

## 📋 UNITY INSPECTOR SETUP

### Button Container (Center-Bottom):
```
Canvas
└── LandingPageUI
    └── ButtonContainer (RectTransform)
        ├── Anchor: Bottom-Center
        ├── Position: (0, 50, 0)
        ├── Size: (600, 100)
        ├── Layout: Horizontal Layout Group
        │   ├── Spacing: 16
        │   ├── Child Alignment: Middle Center
        │   └── Padding: 16
        ├── PrimaryButton (ImprovedButton)
        ├── SecondaryButton (ImprovedButton)
        └── SettingsButton (ImprovedButton)
```

### Button Container (Right-Side):
```
Canvas
└── LandingPageUI
    └── RightSidePanel (RectTransform)
        ├── Anchor: Right-Center
        ├── Position: (-50, 0, 0)
        ├── Size: (200, 400)
        ├── Layout: Vertical Layout Group
        │   ├── Spacing: 16
        │   ├── Child Alignment: Upper Center
        │   └── Padding: 16
        ├── PlayButton (ImprovedButton)
        ├── SettingsButton (ImprovedButton)
        └── LeaderboardButton (ImprovedButton)
```

---

## 🎨 COLOR REFERENCE

**Primary Orange:** `#FF6B35` (RGB: 255, 107, 53)  
**Primary Blue:** `#4ECDC4` (RGB: 78, 205, 196)  
**Primary Green:** `#95E1D3` (RGB: 149, 225, 211)  
**Accent Yellow:** `#FFE66D` (RGB: 255, 230, 109)  
**Accent Pink:** `#FF8B94` (RGB: 255, 139, 148)  
**Neutral Dark:** `#2C3E50` (RGB: 44, 62, 80)  
**Neutral Light:** `#ECF0F1` (RGB: 236, 240, 241)

---

## ✅ SUCCESS CRITERIA

**Button Improvements:**
- ✅ Buttons are tasteful and visually appealing
- ✅ Buttons are in better position (not bottom-left)
- ✅ Buttons have consistent styling
- ✅ Buttons have smooth animations

**Overall Cohesion:**
- ✅ All UI elements work together
- ✅ Consistent color scheme
- ✅ Consistent typography
- ✅ Consistent spacing (8px grid)

**Kid-Friendly:**
- ✅ Colorful and playful
- ✅ Friendly language
- ✅ Smooth animations
- ✅ Clear visual hierarchy

---

## 🚀 NEXT STEPS

1. **Review this guide** with Unity project open
2. **Create button prefab** using ImprovedButton script
3. **Update landing page** scene with new buttons
4. **Test** on different screen sizes
5. **Iterate** based on feedback

---

**This guide provides everything needed to improve the Unity game landing page UI/UX!** 🎮✨
"""
    
    return guide

def main():
    """Main improvement process."""
    print_header("Unity Game Landing Page UI/UX Improvement")
    
    # ANALYZE
    issues = analyze_current_ui()
    
    # IDEATE
    improvements = ideate_improvements()
    
    # MODEL
    guide = create_unity_ui_improvement_guide()
    
    # Save guide
    guide_file = PROJECT_ROOT / "UNITY-LANDING-PAGE-UI-IMPROVEMENT-GUIDE.md"
    with open(guide_file, 'w', encoding='utf-8') as f:
        f.write(guide)
    
    print(f"\n💾 Guide saved: {guide_file}")
    
    # Create Unity C# script for improved buttons
    script_file = UNITY_SCRIPTS / "ImprovedButton.cs"
    improved_button_script = """using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using TMPro;

/// <summary>
/// Improved Button Component - Duolingo/Steve Jobs Inspired
/// Tasteful, kid-friendly buttons with smooth animations
/// </summary>
public class ImprovedButton : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler, IPointerClickHandler
{
    [Header("Button Style")]
    public ButtonType buttonType = ButtonType.Primary;
    public string buttonText = "Button";
    
    [Header("References")]
    public Image buttonBackground;
    public TextMeshProUGUI buttonTextComponent;
    public RectTransform buttonRect;
    
    [Header("Colors")]
    public Color primaryColor = new Color(1f, 0.42f, 0.21f); // Orange #FF6B35
    public Color secondaryColor = new Color(0.31f, 0.80f, 0.77f); // Blue #4ECDC4
    public Color successColor = new Color(0.18f, 0.80f, 0.44f); // Green #2ECC71
    
    [Header("Animation")]
    public float hoverScale = 1.05f;
    public float clickScale = 0.95f;
    public float animationDuration = 0.3f;
    
    public enum ButtonType
    {
        Primary,    // Orange, main action
        Secondary,  // Blue, secondary action
        Success     // Green, positive action
    }
    
    private Vector3 originalScale;
    private Color originalColor;
    
    void Start()
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
            _ => primaryColor
        };
        
        originalColor = buttonColor;
        buttonBackground.color = buttonColor;
        
        // Set text
        if (buttonTextComponent != null)
        {
            buttonTextComponent.text = buttonText;
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
    
    public void OnPointerEnter(PointerEventData eventData)
    {
        // Hover animation - scale up
        LeanTween.scale(buttonRect.gameObject, originalScale * hoverScale, animationDuration)
            .setEase(LeanTweenType.easeOutQuad);
        
        // Brighten color
        Color hoverColor = new Color(
            Mathf.Min(1f, originalColor.r * 1.2f),
            Mathf.Min(1f, originalColor.g * 1.2f),
            Mathf.Min(1f, originalColor.b * 1.2f)
        );
        LeanTween.color(buttonRect, hoverColor, animationDuration);
    }
    
    public void OnPointerExit(PointerEventData eventData)
    {
        // Return to normal
        LeanTween.scale(buttonRect.gameObject, originalScale, animationDuration)
            .setEase(LeanTweenType.easeOutQuad);
        LeanTween.color(buttonRect, originalColor, animationDuration);
    }
    
    public void OnPointerClick(PointerEventData eventData)
    {
        // Click animation - quick scale down then up
        LeanTween.scale(buttonRect.gameObject, originalScale * clickScale, 0.1f)
            .setEase(LeanTweenType.easeOutQuad)
            .setOnComplete(() => {
                LeanTween.scale(buttonRect.gameObject, originalScale, 0.1f)
                    .setEase(LeanTweenType.easeOutQuad);
            });
    }
}
"""
    
    with open(script_file, 'w', encoding='utf-8') as f:
        f.write(improved_button_script)
    
    print(f"💾 Unity script created: {script_file}")
    
    # Summary
    print_header("Improvement Guide Complete!")
    
    print("\n✅ Created:")
    print(f"   1. Comprehensive guide: {guide_file}")
    print(f"   2. Unity C# script: {script_file}")
    
    print("\n🎯 Next Steps:")
    print("   1. Open Unity project")
    print("   2. Read the guide: UNITY-LANDING-PAGE-UI-IMPROVEMENT-GUIDE.md")
    print("   3. Add ImprovedButton.cs to Unity project")
    print("   4. Create button prefab")
    print("   5. Update landing page scene")
    print("   6. Test and iterate")
    
    print("\n💡 The guide includes:")
    print("   - Button redesign (move from bottom-left)")
    print("   - Design system (colors, typography, spacing)")
    print("   - Unity C# script for improved buttons")
    print("   - Layout recommendations")
    print("   - Implementation steps")
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

