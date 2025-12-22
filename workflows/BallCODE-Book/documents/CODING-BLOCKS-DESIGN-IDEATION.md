# Coding Blocks Design Ideation
## Scratch-Style Block System for BallCODE

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Purpose:** Ideation document for coding block design - how blocks should look and work  
**Status:** Design Ideation

---

## 🎯 KEY DISTINCTION

### Tutorial Version (Current - Like Ava)
**How it works:**
1. Select a block (e.g., "Block 1")
2. Then select an action (e.g., "Pound Dribble")
3. Block + Action = Move

**Example:**
- Select: Block 1
- Then select: Pound Dribble
- Result: Block 1 performs Pound Dribble

### Coding Version (What We're Designing - Like Scratch)
**How it works:**
1. Select a dribble move (e.g., "Pound Dribble")
2. Then select direction (e.g., "S" for Straight)
3. Connect blocks together to create a program

**Example:**
- Select: Pound Dribble block
- Then select: Direction "S" (Straight)
- Connect: Multiple blocks together
- Result: Program that executes in sequence

---

## 🎨 BLOCK DESIGN CONCEPTS

### Core Principle
**Blocks should look like Scratch blocks** - visual, snap-together, intuitive

### Block Structure

#### 1. Action Block (Dribble Move)
```
┌─────────────────────────────┐
│  POUND DRIBBLE              │
│  [Direction: S ▼]           │
└─────────────────────────────┘
```

**Components:**
- **Top:** Block name (e.g., "POUND DRIBBLE")
- **Middle:** Direction dropdown/selector (S, R, L, B, DBL, DBR, DSR, DSL)
- **Bottom:** Connector to snap to next block

#### 2. START Block
```
┌─────────────────────────────┐
│  START                      │
└─────────────────────────────┘
        ↓ (connector)
```

**Components:**
- **Top:** "START" label
- **Bottom:** Connector (only bottom connector - nothing connects above)

#### 3. END Block
```
        ↑ (connector)
┌─────────────────────────────┐
│  END                        │
└─────────────────────────────┘
```

**Components:**
- **Top:** Connector (only top connector - nothing connects below)
- **Bottom:** "END" label

---

## 🎨 VISUAL DESIGN IDEAS

### Color Coding by Block Type

#### Option 1: By Dribble Type
- **Pound Dribble:** Blue
- **Crossover:** Orange
- **In & Out:** Yellow
- **Between Legs:** Green
- **Behind Back:** Purple
- **Half Spin:** Teal
- **Spin:** Red

#### Option 2: By Difficulty Level
- **Level 1 Blocks (Foundation):** Light Blue
- **Level 2 Blocks (Intermediate):** Medium Blue
- **Level 3 Blocks (Advanced):** Dark Blue

#### Option 3: By Function
- **Action Blocks (Dribbles):** Orange
- **Control Blocks (IF, LOOP):** Yellow
- **Data Blocks (Variables):** Green
- **Function Blocks:** Purple

**Recommendation:** Option 1 (By Dribble Type) - most intuitive for basketball context

### Block Shape

#### Scratch-Style (Recommended)
```
┌─────────────────────────────┐
│  POUND DRIBBLE              │
│  Direction: [S ▼]          │
└─────────────────────────────┘
```

**Features:**
- Rounded corners
- Snap connectors (top and bottom)
- Visual feedback when hovering
- Clear, readable text

#### Alternative: Basketball-Themed
```
╔═════════════════════════════╗
║  🏀 POUND DRIBBLE           ║
║  Direction: [S ▼]          ║
╚═════════════════════════════╝
```

**Features:**
- Basketball icon
- Court-themed colors
- More visual, less text-heavy

---

## 🔧 BLOCK FUNCTIONALITY

### Direction Selection

#### Option 1: Dropdown Menu
```
┌─────────────────────────────┐
│  POUND DRIBBLE              │
│  Direction: [S ▼]          │
│    S - Straight             │
│    R - Right                │
│    L - Left                 │
│    B - Back                 │
│    DSR - Diagonal Straight R│
│    DSL - Diagonal Straight L│
│    DBR - Diagonal Back R     │
│    DBL - Diagonal Back L    │
└─────────────────────────────┘
```

#### Option 2: Direction Buttons
```
┌─────────────────────────────┐
│  POUND DRIBBLE              │
│  [S] [R] [L] [B] [DSR] [DSL]│
│  [DBR] [DBL]                │
└─────────────────────────────┘
```

#### Option 3: Arrow Selector
```
┌─────────────────────────────┐
│  POUND DRIBBLE              │
│         ↑                   │
│    ←  [S]  →                │
│         ↓                   │
└─────────────────────────────┘
```

**Recommendation:** Option 1 (Dropdown) - clearest, most accessible

### Block Connection

#### Visual Connection
- **Top connector:** Receives block above
- **Bottom connector:** Connects to block below
- **Visual feedback:** Highlight when blocks can connect
- **Snap sound:** Audio feedback when blocks connect

#### Connection Rules
- START block: Only connects at bottom
- END block: Only connects at top
- Action blocks: Connect top and bottom
- Control blocks (IF, LOOP): Have special connectors for nested blocks

---

## 📚 BLOCK TYPES BY BOOK

### Book 1: Sequences (Foundation Blocks)

#### Available Blocks:
1. **START Block**
   ```
   ┌──────────┐
   │  START   │
   └──────────┘
   ```

2. **POUND DRIBBLE Block**
   ```
   ┌─────────────────────────────┐
   │  POUND DRIBBLE               │
   │  Direction: [S ▼]           │
   └─────────────────────────────┘
   ```

3. **BUCKET Block (Bucket = Score)**
   ```
   ┌─────────────────────────────┐
   │  BUCKET                     │
   │  Type: [LAYUP ▼]           │
   └─────────────────────────────┘
   ```
   
   **Bucket Types Available:**
   - Layup
   - Dunk
   - Step Back
   - Floater
   - Pull Up Jump Shot
   - (Other bucket types)

4. **END Block**
   ```
   ┌──────────┐
   │  END     │
   └──────────┘
   ```

#### Example Program:
```
┌──────────┐
│  START   │
└──────────┘
     ↓
┌─────────────────────────────┐
│  POUND DRIBBLE              │
│  Direction: [S ▼]          │
└─────────────────────────────┘
     ↓
┌─────────────────────────────┐
│  POUND DRIBBLE              │
│  Direction: [S ▼]          │
└─────────────────────────────┘
     ↓
┌─────────────────────────────┐
│  POUND DRIBBLE              │
│  Direction: [S ▼]          │
└─────────────────────────────┘
     ↓
┌─────────────────────────────┐
│  BUCKET                     │
│  Type: [LAYUP ▼]           │
└─────────────────────────────┘
     ↓
┌──────────┐
│  END     │
└──────────┘
```

**Note:** Sequences should end with a BUCKET (score) to complete the play. Bucket = Score, with different types available: Layup, Dunk, Step Back, Floater, Pull Up Jump Shot, and others.

### Book 2: Conditionals (Decision Blocks)

#### Additional Blocks:
4. **IF Block**
   ```
   ┌─────────────────────────────┐
   │  IF [defender goes left]    │
   │  THEN                        │
   │  ┌─────────────────────────┐ │
   │  │  CROSSOVER DRIBBLE      │ │
   │  │  Direction: [R ▼]      │ │
   │  └─────────────────────────┘ │
   │  ELSE                        │
   │  ┌─────────────────────────┐ │
   │  │  CROSSOVER DRIBBLE      │ │
   │  │  Direction: [L ▼]       │ │
   │  └─────────────────────────┘ │
   └─────────────────────────────┘
   ```

### Book 3: Loops (Repetition Blocks)

#### Additional Blocks:
5. **REPEAT Block**
   ```
   ┌─────────────────────────────┐
   │  REPEAT [3] TIMES           │
   │  ┌─────────────────────────┐ │
   │  │  IN & OUT DRIBBLE       │ │
   │  │  Direction: [L ▼]       │ │
   │  └─────────────────────────┘ │
   └─────────────────────────────┘
   ```

---

## 🎨 DESIGN SPECIFICATIONS

### Block Dimensions
- **Width:** 200-250px (adjustable based on text)
- **Height:** 60-80px (standard action block)
- **Padding:** 10-15px internal padding
- **Border Radius:** 8-12px (rounded corners)

### Typography
- **Block Name:** Bold, 16-18px
- **Direction Label:** Regular, 12-14px
- **Font Family:** Sans-serif (clear, readable)

### Colors
- **Background:** Light (white/light gray)
- **Border:** 2-3px, darker shade
- **Text:** Dark (black/dark gray)
- **Hover State:** Slightly lighter background
- **Selected State:** Highlighted border

### Interaction States
1. **Default:** Normal appearance
2. **Hover:** Slightly lighter, cursor changes
3. **Dragging:** Semi-transparent, follows cursor
4. **Can Connect:** Green highlight on connector
5. **Cannot Connect:** Red highlight on connector
6. **Connected:** Solid connection line

---

## 🔄 BLOCK PALETTE LAYOUT

### Left Sidebar (Block Palette)
```
┌─────────────────────┐
│  BLOCK PALETTE      │
├─────────────────────┤
│  Control            │
│  ┌──────────┐       │
│  │  START   │       │
│  └──────────┘       │
│  ┌──────────┐       │
│  │  END     │       │
│  └──────────┘       │
│                     │
│  Dribbles           │
│  ┌──────────────┐   │
│  │ POUND DRIBBLE│   │
│  └──────────────┘   │
│  ┌──────────────┐   │
│  │ CROSSOVER    │   │
│  └──────────────┘   │
│  ┌──────────────┐   │
│  │ IN & OUT     │   │
│  └──────────────┘   │
│                     │
│  Control Flow       │
│  ┌──────────────┐   │
│  │ IF...THEN    │   │
│  └──────────────┘   │
│  ┌──────────────┐   │
│  │ REPEAT       │   │
│  └──────────────┘   │
└─────────────────────┘
```

### Center Workspace
```
┌─────────────────────────────────────┐
│  WORKSPACE                          │
│                                     │
│  [Drag blocks here to build]       │
│                                     │
│  ┌──────────┐                      │
│  │  START   │                      │
│  └──────────┘                      │
│       ↓                             │
│  ┌──────────────┐                  │
│  │ POUND DRIBBLE│                  │
│  └──────────────┘                  │
│                                     │
└─────────────────────────────────────┘
```

### Right Sidebar (Game Preview)
```
┌─────────────────────┐
│  GAME PREVIEW       │
├─────────────────────┤
│                     │
│  [Basketball Court] │
│                     │
│  [Run] [Reset]      │
│                     │
└─────────────────────┘
```

---

## 🎯 DESIGN DECISIONS NEEDED

### 1. Block Visual Style
- [ ] Scratch-style (rounded, simple)
- [ ] Basketball-themed (icons, court colors)
- [ ] Hybrid (Scratch-style with basketball accents)

### 2. Direction Selection Method
- [ ] Dropdown menu
- [ ] Direction buttons
- [ ] Arrow selector
- [ ] Other: _______________

### 3. Color Coding System
- [ ] By dribble type
- [ ] By difficulty level
- [ ] By function type
- [ ] Other: _______________

### 4. Block Size
- [ ] Compact (smaller, more fit on screen)
- [ ] Standard (medium, readable)
- [ ] Large (easier to see, less fit on screen)

### 5. Connection Visual
- [ ] Simple line
- [ ] Highlighted connection
- [ ] Animated connection
- [ ] Other: _______________

---

## 🚀 IMPLEMENTATION PRIORITIES

### Phase 1: Foundation Blocks (Book 1)
1. START block
2. POUND DRIBBLE block (with direction selector)
3. END block
4. Basic connection system

### Phase 2: Control Blocks (Book 2)
1. IF...THEN block
2. IF...THEN...ELSE block
3. CROSSOVER DRIBBLE block

### Phase 3: Loop Blocks (Book 3)
1. REPEAT block
2. WHILE block
3. IN & OUT DRIBBLE block

### Phase 4: Advanced Blocks (Books 4-9)
1. Function blocks
2. Variable blocks
3. Array blocks
4. Algorithm blocks
5. AI blocks

---

## 📝 DESIGNER NOTES

### Key Requirements:
1. **Accessibility:** Blocks must be readable and clear
2. **Intuitiveness:** Should feel natural to drag and connect
3. **Visual Feedback:** Clear indication of connection points
4. **Basketball Context:** Should feel connected to basketball
5. **Scalability:** Design system that works for all 9 books

### Questions for Designers:
1. How do we make direction selection intuitive?
2. Should blocks have icons or just text?
3. How do we show nested blocks (in IF, LOOP)?
4. What's the best way to show connection points?
5. How do we handle blocks that don't fit on screen?
6. Should we have different block styles for different books?

---

## 🎨 INSPIRATION REFERENCES

### Scratch Blocks
- Visual, drag-and-drop
- Clear connection system
- Color-coded by function
- Intuitive for kids

### Blockly (Google)
- Similar to Scratch
- More customizable
- Used in many educational tools

### Code.org Blocks
- Educational focus
- Clear visual design
- Good for beginners

### Basketball Game UI
- Court-themed colors
- Sports iconography
- Action-oriented design

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** Design Ideation - Ready for Designer Review  
**Next Steps:** Designer feedback and iteration

