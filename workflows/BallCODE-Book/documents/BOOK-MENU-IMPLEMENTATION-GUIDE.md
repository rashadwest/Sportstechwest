# Book Menu Implementation Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 23, 2025  
**Status:** ✅ Code Complete - Ready for Unity Setup

---

## ✅ What Was Added

### 1. **GameModeButton.cs** - Updated
- ✅ Added `Book` to `GameMode` enum
- ✅ Added special handling for Book mode to open BookMenuManager

### 2. **BookMenuManager.cs** - New Script
- ✅ Manages Book menu UI
- ✅ Shows Book 1, 2, 3 selection buttons
- ✅ Loads levels using `GameModeManager.LoadGameModeFromLevel()`
- ✅ Level IDs:
  - Book 1: `book1_foundation_block`
  - Book 2: `book2_decision_crossover`
  - Book 3: `book3_pattern_loop`

---

## 🎮 Unity Setup Instructions

### Step 1: Add Book Button to Main Menu

1. **In Unity Editor:**
   - Open your main menu scene
   - Find the game mode buttons (Chess, Coding, Freeplay, Mathlete)
   - Duplicate one of them to create a "Book" button

2. **Configure Book Button:**
   - Add `GameModeButton` component (if not already present)
   - Set `Game Mode` dropdown to **"Book"**
   - Set button text to **"Book"** or **"Book Lessons"**

3. **Position:**
   - Place Book button next to other game mode buttons
   - Suggested: Second row, next to Mathlete

---

### Step 2: Create Book Menu UI

1. **Create Book Menu Panel:**
   - Create new Canvas or use existing menu canvas
   - Create empty GameObject: `BookMenuPanel`
   - Add Image component (white background, semi-transparent)
   - Set RectTransform to fill screen or center panel

2. **Add Book Selection Buttons:**
   - Create 3 buttons: `Book1Button`, `Book2Button`, `Book3Button`
   - Style them similar to other game mode buttons
   - Add text labels: "Book 1", "Book 2", "Book 3"
   - Add descriptions (optional): Show book titles/descriptions

3. **Add Back Button:**
   - Create `BackButton` in BookMenuPanel
   - Position: Top-left or bottom of panel
   - Text: "Back" or "← Back"

4. **Hide Initially:**
   - Set `BookMenuPanel` to inactive (unchecked in Inspector)

---

### Step 3: Setup BookMenuManager

1. **Add BookMenuManager Component:**
   - Create empty GameObject: `BookMenuManager`
   - Add `BookMenuManager` component (drag script onto GameObject)

2. **Assign References in Inspector:**
   - **Book Menu Panel:** Drag `BookMenuPanel` GameObject
   - **Main Menu Panel:** Drag your main menu panel GameObject
   - **Back Button:** Drag `BackButton` GameObject
   - **Book 1 Button:** Drag `Book1Button` GameObject
   - **Book 2 Button:** Drag `Book2Button` GameObject
   - **Book 3 Button:** Drag `Book3Button` GameObject

3. **Book Info Text (Optional):**
   - If you have title/description text components, assign them:
     - `book1Title`, `book1Description`
     - `book2Title`, `book2Description`
     - `book3Title`, `book3Description`
   - If not assigned, default text will be used

---

### Step 4: Verify Level Files

1. **Check Level Files Exist:**
   - `Assets/StreamingAssets/Levels/book1_foundation_block.json`
   - `Assets/StreamingAssets/Levels/book2_decision_crossover.json`
   - `Assets/StreamingAssets/Levels/book3_pattern_loop.json`

2. **Verify LevelDataManager:**
   - Make sure `LevelDataManager` is in the scene
   - It should auto-load levels from StreamingAssets on Awake

3. **Verify GameModeManager:**
   - Make sure `GameModeManager` is in the scene
   - It should have `BlockCodingManager` assigned (for Book levels)

---

### Step 5: Test

1. **Play the game:**
   - Click "Book" button on main menu
   - Book menu should open
   - Click "Book 1", "Book 2", or "Book 3"
   - Level should load via `GameModeManager.LoadGameModeFromLevel()`

2. **Check Console:**
   - Should see: `[BookMenuManager] Loading Book X - Level ID: bookX_...`
   - Should see: `[GameModeManager] Loading level: bookX_...`
   - No errors should appear

---

## 📋 Level IDs Reference

**Book 1:**
- Level ID: `book1_foundation_block`
- File: `book1_foundation_block.json`
- Game Mode: `blockcoding`
- Concept: `basic_blocks_sequences`

**Book 2:**
- Level ID: `book2_decision_crossover`
- File: `book2_decision_crossover.json`
- Game Mode: `blockcoding`
- Concept: `conditionals`

**Book 3:**
- Level ID: `book3_pattern_loop`
- File: `book3_pattern_loop.json`
- Game Mode: `blockcoding`
- Concept: `loops`

---

## 🎨 UI/UX Suggestions

### Book Menu Layout:
```
┌─────────────────────────────────┐
│  [← Back]                       │
│                                 │
│  📚 BOOK LESSONS                │
│                                 │
│  ┌──────────┐  ┌──────────┐    │
│  │  BOOK 1  │  │  BOOK 2  │    │
│  │          │  │          │    │
│  │Foundation│  │ Decision │    │
│  │  Block   │  │Crossover │    │
│  └──────────┘  └──────────┘    │
│                                 │
│  ┌──────────┐                   │
│  │  BOOK 3  │                   │
│  │          │                   │
│  │ Pattern  │                   │
│  │   Loop   │                   │
│  └──────────┘                   │
└─────────────────────────────────┘
```

### Button Styling:
- Use same style as other game mode buttons
- Orange accent color when hovered
- Show book title and brief description
- Add book cover image (optional)

---

## ✅ Checklist

- [ ] Book button added to main menu
- [ ] BookMenuPanel created with Book 1, 2, 3 buttons
- [ ] BookMenuManager component added and configured
- [ ] All references assigned in Inspector
- [ ] Level files exist in StreamingAssets/Levels/
- [ ] LevelDataManager loads levels correctly
- [ ] GameModeManager has BlockCodingManager assigned
- [ ] Test: Book menu opens when Book button clicked
- [ ] Test: Book 1, 2, 3 buttons load correct levels
- [ ] Test: Back button returns to main menu

---

## 🐛 Troubleshooting

**Book menu doesn't open:**
- Check BookMenuManager is in scene
- Check Book button has GameModeButton component
- Check GameMode is set to "Book"
- Check console for errors

**Level doesn't load:**
- Check level files exist in StreamingAssets/Levels/
- Check LevelDataManager loaded levels (check console log)
- Check level ID matches exactly: `book1_foundation_block`
- Check GameModeManager has BlockCodingManager assigned

**Button click doesn't work:**
- Check button has Button component
- Check BookMenuManager references are assigned
- Check console for errors

---

**Status:** ✅ Code complete, ready for Unity setup

