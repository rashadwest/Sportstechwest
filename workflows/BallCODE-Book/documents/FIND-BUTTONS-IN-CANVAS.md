# How to Find Buttons in Canvas Hierarchy

**Date:** December 24, 2025  
**Issue:** Buttons not visible even though Canvas is expanded

---

## 🔍 BUTTONS ARE NESTED INSIDE PARENT OBJECTS

The buttons are **inside** the parent GameObjects you see. You need to **expand** those parent objects to see the buttons.

---

## 📋 STEP-BY-STEP INSTRUCTIONS

### **Step 1: Expand "Menu Panel"**

1. In Hierarchy, find **"Menu Panel"** (under Canvas)
2. Click the **arrow/disclosure triangle** next to "Menu Panel" to expand it
3. Look for buttons inside:
   - Exit button
   - Game mode buttons (Chess, Coding, Freeplay, Mathlete, Book)
   - Main action buttons (BallCode, Skins)

### **Step 2: Expand "Main Menu Navigation"**

1. Find **"Main Menu Navigation"** (under Canvas)
2. Click the **arrow** to expand it
3. Look for navigation buttons inside

### **Step 3: Expand Other UI Containers**

Try expanding these parent objects:
- **"Settings Manager"** - might contain Settings button
- **"Ballcode Levels Spawner"** - might contain game mode buttons
- **"Curriculum Levels Spawner"** - might contain curriculum buttons

### **Step 4: Use Search to Find Buttons**

**Easier Method:**
1. Click in the **search bar** at the top of Hierarchy window
2. Type: `Button`
3. This will show **all** GameObjects with "Button" in the name, regardless of nesting level

**OR search for specific buttons:**
- Type: `Exit` - finds exit button
- Type: `Coding` - finds coding button
- Type: `BallCode` - finds BallCode button
- Type: `Leaderboard` - finds leaderboard button
- Type: `Settings` - finds settings button

---

## 🎯 QUICKEST METHOD: Use Hierarchy Search

**Instead of manually expanding, use search:**

1. **Click the search bar** at top of Hierarchy (magnifying glass icon)
2. **Type:** `Button`
3. **Result:** All button GameObjects will appear, even if nested deep

**Then:**
- Select the buttons you want (hold `Cmd` to select multiple)
- Use menu: `Tools` → `UI` → `Apply UI/UX Improvements to Selected Buttons`

---

## 📝 WHAT TO LOOK FOR

Buttons are typically named:
- `ExitButton` or `Exit`
- `LeaderboardButton` or `Leaderboard`
- `SettingsButton` or `Settings`
- `CodingButton` or `Coding`
- `ChessButton` or `Chess`
- `FreeplayButton` or `Freeplay`
- `MathleteButton` or `Mathlete`
- `BookButton` or `Book`
- `BallCodeButton` or `BallCode`
- `SkinsButton` or `Skins`

---

## ✅ EXPECTED RESULT

After using search or expanding parent objects, you should see:
- Multiple button GameObjects
- Each button should have a `Button` component in Inspector
- These are the buttons you can apply UI/UX improvements to

---

**Try the search method first - it's the fastest way to find all buttons!**


