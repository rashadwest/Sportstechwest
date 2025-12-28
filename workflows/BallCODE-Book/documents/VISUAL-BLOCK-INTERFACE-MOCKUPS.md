# BallCODE Visual Block Interface Mockups
## Scratch-Style Design for Books 1-3

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 23, 2025  
**Purpose:** Visual block interface designs for Books 1-3  
**Style:** Scratch-inspired simplicity  
**Status:** Design Mockups Complete

---

## 🎨 DESIGN PRINCIPLES

### Scratch's Visual Design
- **Color-Coded Blocks:** Each category has a color
- **Snap-Together Blocks:** Blocks fit like puzzle pieces
- **Visual Shape:** Blocks have distinct shapes (C-shaped for conditionals, etc.)
- **Clear Labels:** Simple, readable text
- **Immediate Feedback:** See results instantly

### BallCODE Adaptation
- **Basketball-Themed Colors:** Court colors, team colors
- **Basketball Actions:** Move, pass, shoot, dribble
- **Visual Feedback:** Player executes on court
- **Simple Interface:** Clean, uncluttered

---

## 📐 INTERFACE LAYOUT

### Overall Structure

```
┌─────────────────────────────────────────────────────────┐
│  BALLCODE - Book 1: Sequences                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────┐ │
│  │   BLOCKS     │    │     CODE     │    │   COURT  │ │
│  │   PALETTE    │    │     AREA     │    │   VIEW   │ │
│  │              │    │              │    │          │ │
│  │  [Blocks]    │    │  [Your Code] │    │  [Game]  │ │
│  │  [Here]      │    │  [Here]      │    │  [Here]  │ │
│  └──────────────┘    └──────────────┘    └──────────┘ │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Three-Panel Design:**
1. **Left Panel:** Block Palette (available blocks)
2. **Center Panel:** Code Area (where blocks go)
3. **Right Panel:** Court View (game execution)

---

## 🟢 BOOK 1: SEQUENCES - BLOCK DESIGN

### Block Categories

#### 1. Event Blocks (Green - Like Scratch's "when clicked")

```
┌─────────────────────┐
│  🏀 START           │  (Green flag icon)
└─────────────────────┘
```

**Design:**
- Green color (like Scratch's event blocks)
- Basketball icon
- Rounded top (snaps to top of code area)

#### 2. Motion Blocks (Blue - Like Scratch's motion)

```
┌─────────────────────┐
│  MOVE FORWARD       │  (Blue block)
└─────────────────────┘

┌─────────────────────┐
│  MOVE BACKWARD      │  (Blue block)
└─────────────────────┘

┌─────────────────────┐
│  MOVE LEFT          │  (Blue block)
└─────────────────────┘

┌─────────────────────┐
│  MOVE RIGHT         │  (Blue block)
└─────────────────────┘

┌─────────────────────┐
│  PASS BALL          │  (Blue block)
└─────────────────────┘

┌─────────────────────┐
│  MOVE TO POSITION   │  (Blue block)
└─────────────────────┘
```

**Design:**
- Blue color (like Scratch's motion blocks)
- Simple, clear labels
- Rectangular shape (snaps together)

### Complete Sequence Example

```
┌─────────────────────┐
│  🏀 START           │  (Green - event)
├─────────────────────┤
│  MOVE FORWARD       │  (Blue - motion)
├─────────────────────┤
│  PASS BALL          │  (Blue - motion)
├─────────────────────┤
│  MOVE TO POSITION   │  (Blue - motion)
└─────────────────────┘
```

**Visual:**
- Blocks snap together vertically
- Clear visual connection
- Top to bottom execution

---

## 🟠 BOOK 2: CONDITIONALS - BLOCK DESIGN

### Conditional Blocks (Orange - Like Scratch's control)

#### IF Block (C-Shaped)

```
┌─────────────────────┐
│  IF DEFENDER NEAR   │  (Orange C-shaped)
│  ┌─────────────────┐│
│  │  THEN CROSSOVER ││  (Inside IF)
│  └─────────────────┘│
│  ┌─────────────────┐│
│  │  ELSE DRIVE     ││  (Else branch)
│  └─────────────────┘│
└─────────────────────┘
```

**Design:**
- Orange color (like Scratch's control blocks)
- C-shaped (opens to accept blocks inside)
- Clear THEN and ELSE branches

#### Condition Blocks (Light Blue - Hexagonal)

```
┌─────────────────────┐
│  DEFENDER NEAR?     │  (Light blue hexagon)
└─────────────────────┘

┌─────────────────────┐
│  BALL POSSESSION?    │  (Light blue hexagon)
└─────────────────────┘

┌─────────────────────┐
│  SCORE > 10?        │  (Light blue hexagon)
└─────────────────────┘
```

**Design:**
- Light blue color (like Scratch's sensing blocks)
- Hexagonal shape (fits in IF block)
- Question mark indicates condition

### Complete Conditional Example

```
┌─────────────────────┐
│  🏀 START           │  (Green - event)
├─────────────────────┤
│  MOVE FORWARD       │  (Blue - motion)
├─────────────────────┤
│  IF DEFENDER NEAR   │  (Orange C-shaped)
│  ┌─────────────────┐│
│  │  THEN CROSSOVER ││  (Inside IF)
│  └─────────────────┘│
│  ┌─────────────────┐│
│  │  ELSE DRIVE     ││  (Else branch)
│  └─────────────────┘│
└─────────────────────┘
```

**Visual:**
- IF block wraps around THEN/ELSE
- Clear visual separation
- Condition at top, actions inside

---

## 🟡 BOOK 3: LOOPS - BLOCK DESIGN

### Loop Blocks (Yellow - Like Scratch's control)

#### REPEAT Block (C-Shaped)

```
┌─────────────────────┐
│  REPEAT 3 TIMES     │  (Yellow C-shaped)
│  ┌─────────────────┐│
│  │  FAKE LEFT      ││  (Inside loop)
│  ├─────────────────┤│
│  │  GO RIGHT       ││  (Inside loop)
│  └─────────────────┘│
└─────────────────────┘
```

**Design:**
- Yellow color (like Scratch's control blocks)
- C-shaped (opens to accept blocks inside)
- Number input (3, 5, 10, etc.)

#### REPEAT FOREVER Block

```
┌─────────────────────┐
│  REPEAT FOREVER     │  (Yellow C-shaped)
│  ┌─────────────────┐│
│  │  MOVE FORWARD   ││  (Inside loop)
│  └─────────────────┘│
└─────────────────────┘
```

**Design:**
- Yellow color
- C-shaped
- No number input (repeats forever)

### Manual Repetition vs. Loop Comparison

**Manual Repetition (Before Loop):**
```
┌─────────────────────┐
│  🏀 START           │
├─────────────────────┤
│  FAKE LEFT          │  (Repeat 1)
├─────────────────────┤
│  GO RIGHT           │
├─────────────────────┤
│  FAKE LEFT          │  (Repeat 2)
├─────────────────────┤
│  GO RIGHT           │
├─────────────────────┤
│  FAKE LEFT          │  (Repeat 3)
├─────────────────────┤
│  GO RIGHT           │
└─────────────────────┘
```

**With Loop (After Loop):**
```
┌─────────────────────┐
│  🏀 START           │
├─────────────────────┤
│  REPEAT 3 TIMES     │  (Yellow C-shaped)
│  ┌─────────────────┐│
│  │  FAKE LEFT      ││  (Inside loop)
│  ├─────────────────┤│
│  │  GO RIGHT       ││  (Inside loop)
│  └─────────────────┘│
└─────────────────────┘
```

**Visual Comparison:**
- Side-by-side display
- Manual: 6 blocks
- Loop: 1 block
- Clear efficiency demonstration

---

## 🎨 COLOR SCHEME

### Block Colors (Scratch-Inspired)

| Category | Color | Hex Code | Example |
|----------|-------|----------|---------|
| **Events** | Green | #4C97FF | START |
| **Motion** | Blue | #4C97FF | MOVE FORWARD |
| **Control** | Orange | #FF8C1A | IF, REPEAT |
| **Sensing** | Light Blue | #4CBFE6 | DEFENDER NEAR? |
| **Variables** | Orange | #FF8C1A | SCORE, TIME |

### Basketball Theme Colors

| Element | Color | Hex Code | Usage |
|---------|-------|----------|-------|
| **Court** | Brown | #8B4513 | Background |
| **Lines** | White | #FFFFFF | Court markings |
| **Player** | Orange | #FF8C1A | Player sprite |
| **Ball** | Orange | #FF8C1A | Basketball |

---

## 🖥️ INTERFACE MOCKUPS

### Book 1: Sequences Interface

```
┌─────────────────────────────────────────────────────────┐
│  BALLCODE - Book 1: The Foundation Block                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────┐ │
│  │   BLOCKS     │    │     CODE     │    │   COURT  │ │
│  │              │    │              │    │          │ │
│  │  🏀 START    │    │  🏀 START    │    │    🏀    │ │
│  │              │    │  ├──────────┤    │          │ │
│  │  MOVE FORWARD│    │  │ MOVE     │    │   Player │ │
│  │  MOVE BACK   │    │  │ FORWARD  │    │   moves  │ │
│  │  MOVE LEFT   │    │  ├──────────┤    │   here   │ │
│  │  MOVE RIGHT  │    │  │ PASS     │    │          │ │
│  │  PASS BALL   │    │  │ BALL     │    │          │ │
│  │  MOVE TO POS │    │  ├──────────┤    │          │ │
│  │              │    │  │ MOVE TO  │    │          │ │
│  │              │    │  │ POSITION │    │          │ │
│  └──────────────┘    └──────────────┘    └──────────┘ │
│                                                         │
│  [RUN CODE]  [RESET]  [SAVE]                           │
└─────────────────────────────────────────────────────────┘
```

### Book 2: Conditionals Interface

```
┌─────────────────────────────────────────────────────────┐
│  BALLCODE - Book 2: The Code of Flow                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────┐ │
│  │   BLOCKS     │    │     CODE     │    │   COURT  │ │
│  │              │    │              │    │          │ │
│  │  🏀 START    │    │  🏀 START    │    │    🏀    │ │
│  │              │    │  ├──────────┤    │          │ │
│  │  MOVE FORWARD│    │  │ MOVE     │    │   IF     │ │
│  │  IF DEFENDER │    │  │ FORWARD  │    │   defender│ │
│  │  NEAR?       │    │  ├──────────┤    │   near:   │ │
│  │  THEN CROSS  │    │  │ IF       │    │   CROSSOVER│ │
│  │  ELSE DRIVE  │    │  │ DEFENDER │    │   else:  │ │
│  │              │    │  │ NEAR     │    │   DRIVE  │ │
│  │              │    │  │ THEN     │    │          │ │
│  │              │    │  │ CROSSOVER│    │          │ │
│  │              │    │  │ ELSE     │    │          │ │
│  │              │    │  │ DRIVE    │    │          │ │
│  └──────────────┘    └──────────────┘    └──────────┘ │
│                                                         │
│  [RUN CODE]  [RESET]  [SAVE]                           │
└─────────────────────────────────────────────────────────┘
```

### Book 3: Loops Interface

```
┌─────────────────────────────────────────────────────────┐
│  BALLCODE - Book 3: The Pattern                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────┐ │
│  │   BLOCKS     │    │     CODE     │    │   COURT  │ │
│  │              │    │              │    │          │ │
│  │  🏀 START    │    │  🏀 START    │    │    🏀    │ │
│  │              │    │  ├──────────┤    │          │ │
│  │  REPEAT 3    │    │  │ REPEAT   │    │   Loop   │ │
│  │  TIMES       │    │  │ 3 TIMES  │    │   repeats│ │
│  │  FAKE LEFT   │    │  │ ┌────────┤    │   3x:    │ │
│  │  GO RIGHT    │    │  │ │ FAKE   │    │   FAKE   │ │
│  │              │    │  │ │ LEFT   │    │   LEFT   │ │
│  │              │    │  │ ├────────┤    │   GO      │ │
│  │              │    │  │ │ GO    │    │   RIGHT  │ │
│  │              │    │  │ │ RIGHT  │    │          │ │
│  └──────────────┘    └──────────────┘    └──────────┘ │
│                                                         │
│  [RUN CODE]  [RESET]  [SAVE]                           │
└─────────────────────────────────────────────────────────┘
```

---

## 🎮 INTERACTIVE FEATURES

### Drag and Drop

**Scratch-Style:**
- Blocks snap together
- Visual feedback when dragging
- Highlight valid drop zones
- Sound effect on snap

**BallCODE Adaptation:**
- Blocks snap together
- Visual feedback (highlight)
- Basketball sound on snap
- Smooth animation

### Visual Feedback

**When Block is Selected:**
- Highlight in yellow
- Show tooltip with description
- Show Python code equivalent

**When Code Runs:**
- Blocks highlight in order (top to bottom)
- Court view shows player executing
- Progress indicator

### Error Handling

**Invalid Block Placement:**
- Red highlight
- Error message: "This block doesn't fit here"
- Suggestion: "Try a different block"

**Code Execution Error:**
- Stop execution
- Highlight error block
- Error message: "Player can't move there"

---

## 📱 RESPONSIVE DESIGN

### Desktop (Full Interface)
- Three-panel layout
- Large blocks (easy to click)
- Full court view

### Tablet (Adaptive Layout)
- Two-panel layout (blocks + code, court below)
- Medium blocks
- Scaled court view

### Mobile (Stacked Layout)
- Single column
- Small blocks
- Compact court view

---

## 🎨 VISUAL STYLE GUIDE

### Typography
- **Block Labels:** Sans-serif, bold, 14px
- **Interface Text:** Sans-serif, regular, 12px
- **Headings:** Sans-serif, bold, 18px

### Spacing
- **Block Padding:** 8px
- **Block Gap:** 4px
- **Panel Padding:** 16px

### Icons
- **Basketball Icon:** 🏀 (for START block)
- **Arrow Icons:** → (for direction)
- **Checkmark:** ✓ (for success)

---

## ✅ DESIGN CHECKLIST

### Book 1 (Sequences)
- [x] Event blocks (green)
- [x] Motion blocks (blue)
- [x] Snap-together design
- [x] Visual feedback
- [x] Court view

### Book 2 (Conditionals)
- [x] IF blocks (orange, C-shaped)
- [x] Condition blocks (light blue, hexagonal)
- [x] THEN/ELSE branches
- [x] Visual feedback
- [x] Court view

### Book 3 (Loops)
- [x] REPEAT blocks (yellow, C-shaped)
- [x] Manual vs. loop comparison
- [x] Number input
- [x] Visual feedback
- [x] Court view

---

**Status:** ✅ Visual Mockups Complete  
**Next:** PD Session Scripts  
**Style:** Scratch-inspired simplicity

---

**Copyright © 2025 Rashad West. All Rights Reserved.**


