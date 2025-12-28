# Block Curriculum: Simple Explanation (ELI10)
## How Block Coding Works - Explained Like You're 10

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025  
**Purpose:** Simple explanation of block curriculum for easy discussion  
**Status:** ELI10 Version

---

## 🎯 THE BIG PICTURE

Think of learning to code like learning to play basketball:

1. **First, you learn the basic moves** (like dribbling)
2. **Then you learn to combine moves** (like dribbling + shooting)
3. **Finally, you learn advanced strategies** (like team plays)

Block coding works the same way! We have **3 levels** with **3 books each** = **9 books total**.

---

## 📚 LEVEL 1: FOUNDATION BLOCKS (The Basics)

**Who it's for:** Kids in grades 3-5 (like you!)  
**How hard:** ⭐ Easy to ⭐⭐⭐ Medium  
**What you learn:** The building blocks of coding

### How It Works:
1. You read a basketball story
2. You learn a coding idea (like "do things in order")
3. You drag blocks to make a program
4. You see it work in a basketball game!
5. If you're really good, you can skip ahead!

---

## 📖 BOOK 1: SEQUENCES (Do Things in Order)

### What It's About:
**Think of it like:** Following a recipe step-by-step

**Basketball story:** You're breaking the press (getting past defenders) using foundation blocks (pound dribbles)

### ⚠️ Two Different Ways to Play:

**Tutorial Mode (What Ava Does - Already Works!):**
- Select a block number (like "Block 1")
- Then select what to do (like "Pound Dribble")
- This is how you learn each move!

**Coding Mode (What We're Building - Like Scratch!):**
- Select a dribble move (like "Pound Dribble")
- Then select direction (like "S" for Straight)
- Connect blocks together to make a program!
- This is how you learn to code!

**Right now:** Tutorial mode works! Coding mode needs designers to create the blocks.

### The Blocks You Get:
```
┌─────────────────┐
│ START           │  ← This starts your program
└─────────────────┘
      ↓
┌─────────────────┐
│ BLOCK_1_POUND   │  ← This is a pound dribble
│      S          │  ← Direction code: S = Straight (forward/up)
└─────────────────┘
      ↓
┌─────────────────┐
│ BLOCK_1_POUND   │  ← You can use it again!
│      S          │  ← Each block has its own direction code
└─────────────────┘
      ↓
┌─────────────────┐
│ BLOCK_1_POUND   │  ← The code tells it where to go!
│      S          │
└─────────────────┘
      ↓
┌─────────────────┐
│ BUCKET          │  ← Score! Complete the play!
│ [Type: LAYUP ▼]│  ← Different types of buckets
└─────────────────┘
```

**Bucket Types (Bucket = Score!):**
- **LAYUP** - Close-range bucket
- **DUNK** - Powerful close-range bucket
- **STEP BACK** - Create space and bucket
- **FLOATER** - Soft bucket over defender
- **PULL UP JUMP SHOT** - Stop and bucket

**Direction Codes (Easy to Remember!):**
- **R** = Right
- **L** = Left  
- **S** = Straight (forward/up)
- **B** = Back (backward/down)
- **D** = Diagonal (for diagonal moves)
- **DBL** = Diagonal Back Left
- **DBR** = Diagonal Back Right
- **DSR** = Diagonal Straight Right (diagonal forward right)
- **DSL** = Diagonal Straight Left (diagonal forward left)

**Important:** Each block has a direction code (like S, R, L, B) that shows which way it moves. There's no separate "ADVANCE" block - the movement is built right into each block!

### What You Do:
1. **Drag blocks** from the left side
2. **Snap them together** like LEGO pieces
3. **Each block has a direction code** (S, R, L, B, etc.) that shows which way it moves
4. **Click "Run"** to see your player do the moves
5. **Watch it work!** Your player dribbles and moves in the direction code's direction!

### Example Program:
```
START
  → BLOCK_1_POUND (S - moves straight/forward while dribbling)
  → BLOCK_1_POUND (S - moves straight/forward while dribbling)
  → BLOCK_1_POUND (S - moves straight/forward while dribbling)
  → BUCKET [LAYUP] (score! complete the play!)
```

**What happens:** Your player does 3 pound dribbles moving straight forward, then scores with a bucket (layup)!

### Three Ways to Learn (3 Phases):

**Phase 1: Blocks (What you do now)**
- Drag blocks to make a program
- No typing needed!
- See it work in the game

**Phase 2: Bridge (Coming soon)**
- See blocks next to real code
- Learn: "Oh! Blocks = Code!"

**Phase 3: Python (Later)**
- Write real code like grown-ups
- Same ideas, just typing instead of dragging

### The Game Exercise:
- **What you do:** Break the press using sequences
- **How:** Drag blocks to make your player dribble 3 times, then advance
- **If you pass:** You unlock the next book!
- **If you're really good:** You can skip to Book 2!

### Current Status:
✅ **DONE!** You can read the story, watch the video, and play the game right now!

---

## 📖 BOOK 2: CONDITIONALS (Making Decisions)

### What It's About:
**Think of it like:** "If this happens, then do that"

**Basketball story:** You're creating space with crossover dribbles. If the defender goes left, you go right!

### The Blocks You Get:
```
┌─────────────────────┐
│ IF [defender left]  │
│ THEN [go right]     │
└─────────────────────┘

┌─────────────────────┐
│ IF [defender left]  │
│ THEN [go right]     │
│ ELSE [go left]      │
└─────────────────────┘
```

### What You Do:
1. **Check what's happening** (is defender going left?)
2. **Decide what to do** (if yes, go right; if no, go left)
3. **Watch your player** make the smart move!

### Example Program:
```
START
  → IF [defender goes left]
  → THEN [crossover right]
  → ELSE [crossover left]
  → END
```

**What happens:** Your player looks at the defender and makes the right move!

### Current Status:
🔄 **ALMOST DONE!** The game exercise is ready, but we need to finish the story.

---

## 📖 BOOK 3: LOOPS (Doing Things Over and Over)

### What It's About:
**Think of it like:** Repeating a pattern (like doing jumping jacks 10 times)

**Basketball story:** You're creating a pattern with fake moves, then breaking it at the right moment!

### The Blocks You Get:
```
┌─────────────────────┐
│ REPEAT 3 TIMES      │
│   [fake left]       │
└─────────────────────┘

┌─────────────────────┐
│ WHILE [condition]   │
│   [do action]       │
└─────────────────────┘
```

### What You Do:
1. **Tell the program:** "Do this 3 times"
2. **Watch it repeat:** Your player fakes left 3 times
3. **Then break the pattern:** Go right when the defender is fooled!

### Example Program:
```
START
  → REPEAT 3 TIMES
  →   [fake left]
  → [go right]
  → END
```

**What happens:** Your player fakes left 3 times, then goes right when the defender is confused!

### Current Status:
🔄 **IN PROGRESS!** We're working on the story and video.

---

## 📚 LEVEL 2: INTERMEDIATE BLOCKS (Getting Better)

**Who it's for:** Kids in grades 6-8 (middle school)  
**How hard:** ⭐⭐⭐ Medium to ⭐⭐⭐⭐ Hard  
**What you learn:** More advanced coding ideas

### Books 4-6:
- **Book 4: Functions** - Save your favorite moves to use again
- **Book 5: Variables** - Keep track of your score
- **Book 6: Arrays** - Keep track of your whole team

### Current Status:
❌ **NOT YET MADE** - But we know what we want to teach!

---

## 📚 LEVEL 3: ADVANCED BLOCKS (Really Hard Stuff)

**Who it's for:** High school students (grades 9-12)  
**How hard:** ⭐⭐⭐⭐⭐ Really Hard  
**What you learn:** The most advanced coding ideas

### Books 7-9:
- **Book 7: Algorithms** - Find the best way to do things
- **Book 8: AI Integration** - Use smart computers to help
- **Book 9: Python Bridge** - Get ready for real coding!

### Current Status:
❌ **NOT YET MADE** - We're planning these for later!

---

## 🔄 SKIP FUNCTIONALITY (How to Skip Ahead)

### How It Works:
**Think of it like:** A test to see if you already know the stuff

1. **You finish a book** (or think you know it already)
2. **You take a skip test** (5-10 questions)
3. **If you get 80% or higher:** You can skip to the next book!
4. **If you don't pass:** No problem! You can try again or just do the book

### Why It's Cool:
- **Fast learners** don't get bored
- **Everyone else** can take their time
- **You can always go back** if you skipped something

### Current Status:
✅ **PLANNED!** We know how it should work, but we need to build it.

---

## 📊 PROGRESS TRACKING (Your Dashboard)

### What It Shows:
**Think of it like:** A report card for coding

- ✅ **Books you finished** (with checkmarks!)
- ⏭️ **Books you skipped** (with your test score)
- 🔄 **Books you're working on** (with how much you've done)
- ⏳ **Books that are locked** (you haven't unlocked them yet)

### Example:
```
Level 1: Foundation Blocks
  ✅ Book 1: Sequences (Done!)
  ⏭️  Book 2: Conditionals (Skipped - Got 85%!)
  🔄 Book 3: Loops (60% done)
```

### Current Status:
✅ **PLANNED!** We know what it should look like, but we need to build it.

---

## 🎮 GAME INTEGRATION (How Blocks Work in the Game)

### How It Works:
**Think of it like:** Your blocks become real basketball moves!

1. **You drag blocks** to make a program
2. **You click "Run"**
3. **Your player in the game** does exactly what your blocks say!
4. **You see it happen** right away!

### Example:
- **Block:** `BLOCK_1_POUND`
- **Game:** Your player does a pound dribble!
- **Block:** `BLOCK_1_POUND (S)` - The code (S) shows it moves straight/forward
- **Game:** Your player dribbles AND moves straight forward at the same time!

### Current Status:
✅ **WORKING!** Book 1's game exercise is ready to play!

---

## 🎯 THREE-PHASE LEARNING (Blocks → Bridge → Python)

### How It Works:
**Think of it like:** Learning to ride a bike

**Phase 1: Training Wheels (Blocks)**
- Drag blocks (easy!)
- No typing needed
- See it work right away

**Phase 2: Learning to Balance (Bridge)**
- See blocks next to code
- Learn: "Oh! Blocks = Code!"
- Start understanding real code

**Phase 3: Riding Solo (Python)**
- Write real code
- No blocks needed
- You're a real programmer!

### Current Status:
- ✅ **Phase 1:** Working for Book 1!
- ❌ **Phase 2:** Not built yet
- ❌ **Phase 3:** Not built yet

---

## 📋 ASSESSMENTS (How We Know You're Learning)

### During Learning (Formative):
**Think of it like:** Practice problems
- **Block exercises** - Try making programs
- **Game challenges** - See if your code works
- **Questions** - Check if you understand

### End of Book (Summative):
**Think of it like:** A final test
- **Final challenges** - Harder problems
- **Skip test** (optional) - Try to skip ahead
- **Show what you know** - Prove you learned it!

### Current Status:
✅ **PLANNED!** We know what assessments should look like.

---

## 👨‍🏫 TEACHER STUFF (For Your Teachers)

### What Teachers Get:
- **Learning goals** - What you should learn
- **Block guide** - All the blocks explained
- **Example programs** - Sample solutions
- **Progress reports** - See how everyone is doing
- **Can help you** - If you're stuck or want to skip

### Current Status:
❌ **NOT MADE YET** - But we're planning it!

---

## 🚀 WHAT'S DONE VS. WHAT'S COMING

### ✅ What's Working Right Now:
1. **Book 1 is COMPLETE!**
   - ✅ Story you can read
   - ✅ Video you can watch
   - ✅ Game exercise you can play
   - ✅ You can buy it on Gumroad

2. **The Plan is Ready!**
   - ✅ We know what all 9 books should teach
   - ✅ We know how skip tests should work
   - ✅ We know how the dashboard should look

### 🔄 What We're Working On:
1. **Books 2-3**
   - 🔄 Need to finish the stories
   - 🔄 Need to make videos
   - 🔄 Game exercises are almost ready

2. **The Block Interface**
   - 🔄 Need to build the drag-and-drop screen
   - 🔄 Need to make it look like Scratch (but with basketball!)

3. **Skip System**
   - 🔄 Need to build the test system
   - 🔄 Need to make the dashboard

### ❌ What's Coming Later:
1. **Books 4-9**
   - ❌ Need to write all the stories
   - ❌ Need to make all the videos
   - ❌ Need to build all the exercises

2. **Phase 2 & 3**
   - ❌ Need to build the Bridge (blocks → code view)
   - ❌ Need to build the Python learning part

---

## 🎯 KEY THINGS TO REMEMBER

### How the System Works:
1. **Start Easy** - Book 1 is the easiest
2. **Get Harder** - Each book gets a little harder
3. **Skip if You're Good** - Take a test to skip ahead
4. **Always Can Go Back** - Never stuck!
5. **See It Work** - Your blocks become real game moves!

### What You Can Do Now:
- ✅ **Read Book 1** - The story is ready!
- ✅ **Watch Book 1 Video** - It's available!
- ✅ **Play Book 1 Game** - The exercise works!
- ✅ **Buy Book 1** - It's on Gumroad!

### What's Coming:
- 🔄 **Books 2-3** - Almost ready!
- 🔄 **Block Interface** - Being built!
- ❌ **Books 4-9** - Coming later!

---

## 💡 SIMPLE SUMMARY

**Block coding is like:**
- **LEGO blocks** - You snap pieces together
- **A recipe** - You follow steps in order
- **A video game** - You see your code work!

**You learn:**
- **Book 1:** Do things in order (sequences)
- **Book 2:** Make decisions (if/then)
- **Book 3:** Repeat patterns (loops)
- **Books 4-9:** More advanced stuff!

**Right now:**
- ✅ Book 1 is ready to use!
- 🔄 Books 2-3 are almost ready
- ❌ Books 4-9 are coming later

**The cool part:**
- You can skip ahead if you're good!
- You can always go back if you need to!
- You see your code work in a real game!

---

**Version:** 1.0 (ELI10)  
**Created:** December 14, 2025  
**Status:** Simple Explanation for Discussion


