# Visual Assets Generation Guide - Complete Instructions

**Date:** December 16, 2025  
**Status:** Ready for Generation  
**Time Required:** 2-3 hours

---

## 🎯 The 3 Visual Assets Needed

### 1. Court Map Visual
**File:** `episode1-court-map-v1.png`  
**Size:** 1920x1080px (16:9 ratio)  
**Format:** PNG with transparent background option

**Prompt:**
```
Create a basketball court diagram showing the center circle area. 
The court should be clean and professional, with the center circle prominently displayed. 
Integrate subtle tech elements like circuit patterns or code symbols around the circle perimeter. 
Style: Modern, clean, educational illustration. 
Colors: Orange (#eb6123) and blue (#0C72B3) as primary colors. 
Background: Light gray or white. 
Format: High resolution, suitable for print and web.
```

**Where to Use:**
- Book 1 page
- Website
- Curriculum materials

---

### 2. Shadow Press Scouts Character Art
**File:** `episode1-shadow-press-scouts-v1.png`  
**Size:** 1024x1024px (square format)  
**Format:** PNG with transparent background

**Prompt:**
```
Design a basketball character representing the Shadow Press Scouts team. 
The character should be dynamic and athletic, wearing a basketball uniform with team colors. 
Pose: Defensive stance, ready to press. 
Style: Modern, engaging, suitable for children's book. 
Colors: Dark blue/navy for team colors, with orange accents. 
Expression: Determined, focused. 
Background: Simple gradient or court background. 
Format: High resolution character illustration.
```

**Where to Use:**
- Book 1 page
- Character introduction
- Game assets

---

### 3. State Diagram Visualization
**File:** `episode1-state-diagram-v1.png`  
**Size:** 1920x1080px (16:9 ratio)  
**Format:** PNG with transparent background option

**Prompt:**
```
Create a visual representation of basketball possession state transitions. 
Show 4 states: START, LIVE, DEAD, OUTCOME. 
Use arrows to show transitions between states. 
Style: Clean flowchart or diagram. 
Colors: Orange (#eb6123) and blue (#0C72B3). 
Make it educational and easy to understand. 
Format: High resolution, suitable for print and web.
```

**Where to Use:**
- Book 1 page
- Episode 1 Preview
- Skill Pit-Stop section

---

## 🛠️ Generation Tools

### Option 1: Glif (glif.app) - RECOMMENDED
- **Cost:** Free tier available
- **Speed:** Fast
- **Quality:** Good
- **Best for:** Quick generation

### Option 2: DALL-E (OpenAI)
- **Cost:** Pay per image (~$0.04-0.08)
- **Speed:** Fast
- **Quality:** High
- **Best for:** Professional quality

### Option 3: Midjourney
- **Cost:** Paid subscription
- **Speed:** Medium
- **Quality:** Very high
- **Best for:** Artistic quality

### Option 4: Figma/Canva (Manual)
- **Cost:** Free/Paid
- **Speed:** Slow (manual work)
- **Quality:** Custom
- **Best for:** Full control

---

## 📋 Step-by-Step Instructions

### Step 1: Choose Your Tool
1. Go to your chosen tool (Glif, DALL-E, etc.)
2. Sign up/login if needed
3. Navigate to image generation

### Step 2: Generate Court Map
1. Copy the Court Map prompt above
2. Paste into tool
3. Generate 3-5 variations
4. Select best version
5. Download high-resolution version
6. Save as: `episode1-court-map-v1.png`
7. Save to: `BallCode/assets/images/`

### Step 3: Generate Shadow Press Scouts
1. Copy the Shadow Press Scouts prompt above
2. Paste into tool
3. Generate 3-5 variations
4. Select best version
5. Download high-resolution version
6. Save as: `episode1-shadow-press-scouts-v1.png`
7. Save to: `BallCode/assets/images/`

### Step 4: Generate State Diagram
1. Copy the State Diagram prompt above
2. Paste into tool
3. Generate 3-5 variations
4. Select best version
5. Download high-resolution version
6. Save as: `episode1-state-diagram-v1.png`
7. Save to: `BallCode/assets/images/`

### Step 5: Add to Website
1. Run: `python3 scripts/add-visuals-to-book1.py`
2. Script will automatically add visuals to Book 1 page
3. Verify on localhost

---

## ✅ Quality Checklist

Before saving each asset:

- [ ] Correct dimensions (1920x1080px or 1024x1024px)
- [ ] High resolution (300 DPI for print, 150 DPI for web)
- [ ] Kid-friendly and age-appropriate
- [ ] Colors match brand (#0C72B3, #eb6123)
- [ ] Professional appearance
- [ ] Matches style requirements
- [ ] File name is correct
- [ ] Saved to correct location

---

## 🚀 Quick Start

1. **Open Glif (glif.app)** or your chosen tool
2. **Generate Court Map** (30-45 min)
3. **Generate Shadow Press Scouts** (30-45 min)
4. **Generate State Diagram** (30-45 min)
5. **Save all files** to `BallCode/assets/images/`
6. **Run automation:** `python3 scripts/add-visuals-to-book1.py`
7. **Done!** ✅

---

**Total Time:** 2-3 hours  
**Result:** Professional visuals integrated into website

---

*Generated: December 16, 2025*
