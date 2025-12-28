# Book 3: Loops - Lesson Plan (Scratch-Style)
## Simple, Visual Teaching Approach

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 23, 2025  
**Book:** The Pattern (Loops)  
**Grade Levels:** 3-8  
**Duration:** 45-60 minutes  
**Style:** Scratch-inspired simplicity

---

## 🎯 LEARNING OBJECTIVES

**By the end of this lesson, students will be able to:**
1. Understand loops (repeating actions)
2. Create loops using visual blocks
3. Compare manual repetition vs. loops
4. Recognize Python loops that match their blocks

---

## 📋 MATERIALS NEEDED

- BallCODE game access (tablets/computers)
- Story: Book 3, Episode 1
- Visual block cards (optional, for hands-on)
- Whiteboard or projector
- Student worksheets (optional)

---

## ⏱️ LESSON STRUCTURE (45-60 minutes)

### Part 1: Introduction (5 minutes)

**Hook:**
"Have you ever had to do something over and over? Like brushing your teeth - you brush, rinse, brush, rinse, brush, rinse. That's repetition! Today, we're learning how to make computers repeat actions using loops!"

**Connection to Basketball:**
"Basketball players repeat moves all the time. Fake left, go right. Fake left, go right. Fake left, go right. That's a loop - repeating the same move! Let's see how this works in code!"

**Learning Goal:**
"Today, we're learning about loops - repeating actions in code."

---

### Part 2: Story Reading (10 minutes)

**Read:** Book 3, Episode 1 - "The Pattern"

**Key Moments to Pause:**

**After Act I:**
- "What move did the player repeat?"
- "How many times did they repeat it?"

**After Act II:**
- "Why did the player repeat the move?"
- "What pattern did they create?"

**After Act III:**
- "How did understanding loops help win the game?"

**Discussion Questions:**
1. What is a loop? (Repeating actions)
2. Why do we need loops? (To avoid repetition)
3. How is this like basketball? (Repeating moves)

---

### Part 3: Skill Pit-Stop (5 minutes)

**Mini-Lesson: Loops**

**Visual Demonstration:**
Draw on whiteboard:

**Manual Repetition (Before Loop):**
```
1. Fake Left
2. Go Right
3. Fake Left
4. Go Right
5. Fake Left
6. Go Right
```

**With Loop (After Loop):**
```
REPEAT 3 TIMES:
  1. Fake Left
  2. Go Right
```

**Explain:**
- "A loop repeats actions"
- "Instead of writing it 3 times, use REPEAT 3 TIMES"
- "Less code, same result!"

**Connect to Basketball:**
- "Repeating moves is a loop"
- "Fake left, go right - repeat 3 times"
- "Creates a pattern"

---

### Part 4: Visual Block Introduction (10 minutes)

**Scratch-Style Approach:**

**Step 1: Show Manual Repetition (3 minutes)**
Display on screen/board:
```
┌─────────────────────┐
│ START               │
├─────────────────────┤
│ FAKE LEFT           │  (Repeat 1)
├─────────────────────┤
│ GO RIGHT            │
├─────────────────────┤
│ FAKE LEFT           │  (Repeat 2)
├─────────────────────┤
│ GO RIGHT            │
├─────────────────────┤
│ FAKE LEFT           │  (Repeat 3)
├─────────────────────┤
│ GO RIGHT            │
└─────────────────────┘
```

**Ask:**
- "How many blocks do we have?" (6 blocks)
- "Is there a better way?" (Yes - use a loop!)

**Step 2: Show Loop (3 minutes)**
Display on screen/board:
```
┌─────────────────────┐
│ START               │
├─────────────────────┤
│ REPEAT 3 TIMES      │  (Yellow C-shaped block)
│   FAKE LEFT         │  (Inside loop)
│   GO RIGHT          │  (Inside loop)
└─────────────────────┘
```

**Explain:**
- "This is a REPEAT block - it's yellow"
- "It repeats the blocks inside 3 times"
- "Only 1 block instead of 6!"

**Step 3: Compare (2 minutes)**
- Show both side by side
- "Which is better?" (Loop - less code!)
- "Which is easier to change?" (Loop - change number once)

**Step 4: Students Try (2 minutes)**
- Students open BallCODE game
- Try manual repetition first
- Then try loop
- Compare results

---

### Part 5: Game Exercise (15 minutes)

**Exercise: In & Out Dribble Pattern**

**Instructions:**
1. Open the game exercise
2. First, try manual repetition (6 blocks)
3. Then, try using a loop (REPEAT 3 TIMES)
4. Compare: Which is better?
5. Test your loop
6. Debug if needed

**Scratch-Style Guidance:**
- Start with manual: See the repetition
- Then use loop: See the efficiency
- Compare: Which is better?
- Experiment: Change the number

**Success Criteria:**
- ✅ Created loop (REPEAT block)
- ✅ Blocks inside loop make sense
- ✅ Loop repeats correctly
- ✅ Student can explain why loops are better

**Differentiation:**
- **Struggling:** Provide starter loop, students modify number
- **On Track:** Students create their own loop
- **Advanced:** Students create nested loops (loop inside loop)

---

### Part 6: Code Connection (5 minutes)

**Show the Bridge:**

**Manual Repetition:**
```python
fake_left()
go_right()
fake_left()
go_right()
fake_left()
go_right()
```

**With Loop:**
```python
for i in range(3):
    fake_left()
    go_right()
```

**Explain:**
- "Manual repetition = 6 lines of code"
- "Loop = 3 lines of code"
- "Same result, less code!"

**Students See:**
- Manual repetition (many lines)
- Loop (few lines)
- The efficiency

---

### Part 7: Wrap-Up (5 minutes)

**Reflection Questions:**
1. What is a loop? (Repeating actions)
2. Why do we need loops? (To avoid repetition)
3. How is this like basketball? (Repeating moves)
4. What did you learn? (Share one thing)

**Extension:**
- "Create a loop for a different move"
- "What happens if you change the number?"
- "Try it at home: Find things you repeat - can you make a loop?"

**Next Steps:**
- "You've learned sequences, conditionals, and loops - the basics of coding!"
- "Next time, we'll learn about data - storing information!"

---

## 🎮 GAME EXERCISE DETAILS

### Exercise: In & Out Dribble Pattern

**Objective:** Create a loop to repeat the in & out dribble move

**Available Blocks:**
- `START` (green flag)
- `FAKE LEFT` (blue)
- `GO RIGHT` (blue)
- `REPEAT 3 TIMES` (yellow C-shaped)
- `REPEAT 5 TIMES` (yellow C-shaped)
- `REPEAT 10 TIMES` (yellow C-shaped)

**Challenge Levels:**

**Level 1 (Beginner):**
- Use REPEAT 3 TIMES
- Simple loop: FAKE LEFT → GO RIGHT
- Understand repetition

**Level 2 (Intermediate):**
- Use REPEAT 5 TIMES
- More complex loop
- Experiment with numbers

**Level 3 (Advanced):**
- Use REPEAT 10 TIMES
- Nested loops (loop inside loop)
- Complex patterns

**Success Feedback:**
- "Great loop! You created a pattern!"
- "Try a different number - what happens?"
- "Can you make the loop longer? Shorter?"

---

## 📊 ASSESSMENT

### Formative Assessment (During Lesson)

**Observation Checklist:**
- [ ] Student understands loop concept
- [ ] Student can create REPEAT block
- [ ] Student can explain why loops are better
- [ ] Student can debug (fix errors)

**Questions to Ask:**
- "What happens if you change the number?"
- "Why is a loop better than manual repetition?"
- "How many times does your loop repeat?"

### Summative Assessment (End of Lesson)

**Exercise Completion:**
- ✅ Created loop (REPEAT block)
- ✅ Loop works (repeats correctly)
- ✅ Can explain why loops are better
- ✅ Understands repetition

**Rubric:**

**Excellent (4):**
- Creates complex loop (nested loops)
- Explains why loops are efficient
- Can debug and fix errors
- Connects to basketball context

**Good (3):**
- Creates loop (REPEAT block)
- Understands repetition
- Can fix simple errors
- Understands basketball connection

**Developing (2):**
- Creates simple loop
- Needs help understanding repetition
- Struggles with debugging
- Limited basketball connection

**Needs Improvement (1):**
- Cannot create loop
- Doesn't understand repetition
- Cannot debug
- No basketball connection

---

## 🎯 DIFFERENTIATION STRATEGIES

### For Struggling Students

**Support:**
- Provide starter loop (REPEAT 3 TIMES)
- Students add blocks inside
- Use visual aids (loop card)
- Pair with stronger student
- One-on-one guidance

**Modifications:**
- Simpler exercise (REPEAT 2 TIMES)
- More time to practice
- Step-by-step guidance
- Visual examples

### For Advanced Students

**Extensions:**
- Create nested loops (loop inside loop)
- Experiment with different numbers
- Create loops for different moves
- Write Python code for their loops
- Help other students

**Challenges:**
- "Can you create a loop that repeats 10 times?"
- "What's the longest loop that still works?"
- "Create a loop for a different move pattern"

### For English Language Learners

**Support:**
- Visual blocks (no text needed)
- Gestures and demonstrations
- Pair with native speaker
- Use simple language
- Provide vocabulary support

---

## 💡 TEACHER TIPS

### Scratch-Style Teaching Tips

**1. Show Comparison First:**
- Start with manual repetition
- Then show loop
- Compare efficiency
- Students see the benefit

**2. Visual First:**
- Show REPEAT block shape (C-shaped)
- Use whiteboard/projector
- Let students see it work

**3. Hands-On:**
- Students must try both
- Don't just demonstrate
- Let them experiment

**4. Immediate Feedback:**
- Game shows results immediately
- Students see repetition
- Easy to debug

**5. Celebrate Mistakes:**
- "What did you learn from that?"
- "How can we fix it?"
- "Debugging is part of coding!"

---

## 🔗 CONNECTIONS

### To Previous Learning
- Book 1: Sequences (order of steps)
- Book 2: Conditionals (if/then decisions)
- Repetition in daily life

### To Future Learning
- Nested loops (loop inside loop)
- Real coding: All programs use loops
- Complex patterns

### To Real World
- Repeating tasks (loops)
- Patterns in nature (loops)
- Music: Repeating beats (loops)

---

## 📚 RESOURCES

### For Teachers
- Book 3 Teacher Guide
- Video tutorial: "Teaching Loops"
- Block reference card
- Answer key for exercises

### For Students
- Book 3 Story
- Game exercises
- Block reference card
- Practice worksheets

### Extension Activities
- Create loop for different move
- Write patterns using loops
- Draw loop diagram
- Share loops with classmates

---

## ✅ LESSON CHECKLIST

**Before Lesson:**
- [ ] Read Book 3, Episode 1
- [ ] Test game exercise
- [ ] Prepare visual aids
- [ ] Set up devices
- [ ] Review differentiation strategies

**During Lesson:**
- [ ] Hook students (5 min)
- [ ] Read story (10 min)
- [ ] Skill pit-stop (5 min)
- [ ] Block introduction (10 min)
- [ ] Game exercise (15 min)
- [ ] Code connection (5 min)
- [ ] Wrap-up (5 min)

**After Lesson:**
- [ ] Assess student work
- [ ] Note who struggled/excelled
- [ ] Plan follow-up activities
- [ ] Reflect on what worked
- [ ] Adjust for next time

---

**Status:** ✅ Lesson Plan Complete  
**Next:** Visual Block Interface Mockups  
**Style:** Scratch-inspired simplicity

---

**Copyright © 2025 Rashad West. All Rights Reserved.**


