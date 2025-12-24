# Professional Development Session Scripts (Scratch-Style)
## Simple, Hands-On Teacher Training

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 23, 2025  
**Purpose:** PD session scripts for Books 1-3  
**Style:** Scratch-inspired simplicity  
**Duration:** 60 minutes total (20 min per book)

---

## 🎯 OVERVIEW

### Session Structure

**Total Time:** 60 minutes
- **Introduction:** 5 minutes
- **Book 1 (Sequences):** 20 minutes
- **Book 2 (Conditionals):** 20 minutes
- **Book 3 (Loops):** 20 minutes
- **Wrap-Up:** 5 minutes

### Materials Needed
- BallCODE game access (for each teacher)
- Projector/screen
- Whiteboard
- Handouts (optional)

---

## 📝 SESSION 1: INTRODUCTION (5 minutes)

### Script

**Welcome (1 minute):**
"Welcome to BallCODE professional development! Today, we're going to learn how to teach coding through basketball - and it's going to be simple, just like Scratch makes coding simple."

**What is BallCODE? (2 minutes):**
"BallCODE teaches coding through basketball stories and games. Students read a story, learn a concept, then practice it in a game. Simple."

**Today's Goals (1 minute):**
"Today, you'll learn:
1. How to teach sequences (Book 1)
2. How to teach conditionals (Book 2)
3. How to teach loops (Book 3)

And you'll try it yourself - hands-on, just like your students will."

**Let's Start (1 minute):**
"Ready? Let's begin with Book 1 - Sequences!"

---

## 📝 SESSION 2: BOOK 1 - SEQUENCES (20 minutes)

### Part 1: Introduction (3 minutes)

**Script:**
"Book 1 is about sequences. A sequence is just steps in order - one thing after another."

**Demonstration:**
Draw on whiteboard:
```
1. Move Forward
2. Pass Ball
3. Move to Position
```

**Explain:**
"This is a sequence. In basketball, breaking the press is a sequence. In code, it's the same thing - steps in order."

**Connection:**
"Just like giving directions: 'First, go straight. Then, turn left. Finally, stop.' That's a sequence!"

### Part 2: Visual Blocks (5 minutes)

**Script:**
"Now let's see how this works with blocks. In BallCODE, we use visual blocks - just like Scratch."

**Show Blocks:**
Display on screen:
```
┌─────────────────────┐
│  🏀 START           │
├─────────────────────┤
│  MOVE FORWARD       │
├─────────────────────┤
│  PASS BALL          │
├─────────────────────┤
│  MOVE TO POSITION   │
└─────────────────────┘
```

**Explain:**
"These blocks snap together - just like LEGO. Each block is one instruction. The order matters - top to bottom."

**Key Points:**
- "Blocks are visual - no typing needed"
- "Order matters - can't pass before you move"
- "Simple - just drag and drop"

### Part 3: Hands-On Practice (10 minutes)

**Script:**
"Now it's your turn. Open BallCODE and try it yourself."

**Instructions:**
1. "Open the game"
2. "Drag START block to code area"
3. "Drag MOVE FORWARD below START"
4. "Drag PASS BALL below MOVE FORWARD"
5. "Click RUN and watch it work!"

**Circulate and Help:**
- "What happens if you change the order?"
- "What if you put PASS before MOVE?"
- "Does it still work?"

**After 5 minutes:**
"Great! Now try creating your own sequence. Use at least 3 blocks. What basketball move can you create?"

### Part 4: Code Connection (2 minutes)

**Script:**
"Now let's see how blocks become code."

**Show Side-by-Side:**
```
Blocks:              Python:
START               start()
  → MOVE FORWARD      move_forward()
  → PASS BALL         pass_ball()
  → MOVE TO POS       move_to_position()
```

**Explain:**
"Each block becomes one line of code. Same sequence, different language. Students see this connection in Phase 2."

**Key Point:**
"Students don't need to write Python yet - they see the connection. That's enough for Book 1."

---

## 📝 SESSION 3: BOOK 2 - CONDITIONALS (20 minutes)

### Part 1: Introduction (3 minutes)

**Script:**
"Book 2 is about conditionals - making decisions in code."

**Demonstration:**
Draw on whiteboard:
```
IF defender is near
  THEN crossover
ELSE
  drive to basket
```

**Explain:**
"This is a conditional. In basketball, reading defense is a conditional. In code, it's the same thing - if this, then that."

**Connection:**
"Just like making decisions: 'If it's raining, then I'll bring an umbrella. Else, I'll leave it at home.' That's a conditional!"

### Part 2: Visual Blocks (5 minutes)

**Script:**
"Now let's see how this works with blocks. The IF block is C-shaped - it opens to accept blocks inside."

**Show Blocks:**
Display on screen:
```
┌─────────────────────┐
│  🏀 START           │
├─────────────────────┤
│  MOVE FORWARD       │
├─────────────────────┤
│  IF DEFENDER NEAR   │  (Orange C-shaped)
│  ┌─────────────────┐│
│  │  THEN CROSSOVER ││
│  └─────────────────┘│
│  ┌─────────────────┐│
│  │  ELSE DRIVE     ││
│  └─────────────────┘│
└─────────────────────┘
```

**Explain:**
"The IF block checks a condition. If true, do THEN. If false, do ELSE. Simple!"

**Key Points:**
- "IF block is C-shaped - visual cue"
- "Condition goes at top (DEFENDER NEAR)"
- "THEN and ELSE are branches"

### Part 3: Hands-On Practice (10 minutes)

**Script:**
"Now it's your turn. Create a conditional for one-on-one."

**Instructions:**
1. "Open the game"
2. "Drag START block"
3. "Drag IF DEFENDER NEAR block"
4. "Drag THEN CROSSOVER inside IF"
5. "Drag ELSE DRIVE in else branch"
6. "Click RUN and watch it work!"

**Circulate and Help:**
- "What happens if defender is near?"
- "What happens if defender is not near?"
- "Can you add another IF block?"

**After 5 minutes:**
"Great! Now try creating your own conditional. What other decisions can a player make?"

### Part 4: Code Connection (2 minutes)

**Script:**
"Now let's see how blocks become code."

**Show Side-by-Side:**
```
Blocks:              Python:
START               start()
  → MOVE FORWARD      move_forward()
  → IF DEFENDER NEAR  if defender_near():
      THEN CROSSOVER    crossover()
      ELSE DRIVE      else:
                        drive()
```

**Explain:**
"IF block becomes if statement. THEN becomes code inside if. ELSE becomes else branch. Same logic, different language."

**Key Point:**
"Students see the connection. They don't need to write Python yet - understanding is enough for Book 2."

---

## 📝 SESSION 4: BOOK 3 - LOOPS (20 minutes)

### Part 1: Introduction (3 minutes)

**Script:**
"Book 3 is about loops - repeating actions in code."

**Demonstration:**
Draw on whiteboard:

**Manual Repetition:**
```
1. Fake Left
2. Go Right
3. Fake Left
4. Go Right
5. Fake Left
6. Go Right
```

**With Loop:**
```
REPEAT 3 TIMES:
  1. Fake Left
  2. Go Right
```

**Explain:**
"This is a loop. Instead of writing it 3 times, use REPEAT 3 TIMES. Less code, same result!"

**Connection:**
"Just like repeating tasks: 'Brush teeth, rinse, repeat 3 times.' That's a loop!"

### Part 2: Visual Comparison (5 minutes)

**Script:**
"Let's see the difference. First, manual repetition - 6 blocks."

**Show Manual:**
```
┌─────────────────────┐
│  🏀 START           │
├─────────────────────┤
│  FAKE LEFT          │
├─────────────────────┤
│  GO RIGHT           │
├─────────────────────┤
│  FAKE LEFT          │
├─────────────────────┤
│  GO RIGHT           │
├─────────────────────┤
│  FAKE LEFT          │
├─────────────────────┤
│  GO RIGHT           │
└─────────────────────┘
```

**Ask:**
"How many blocks? (6) Is there a better way? (Yes - use a loop!)"

**Show Loop:**
```
┌─────────────────────┐
│  🏀 START           │
├─────────────────────┤
│  REPEAT 3 TIMES     │  (Yellow C-shaped)
│  ┌─────────────────┐│
│  │  FAKE LEFT      ││
│  ├─────────────────┤│
│  │  GO RIGHT       ││
│  └─────────────────┘│
└─────────────────────┘
```

**Explain:**
"Only 1 block instead of 6! Same result, less code. That's why loops are powerful!"

**Key Points:**
- "Show manual first - builds understanding"
- "Then show loop - shows efficiency"
- "Clear comparison - students see the benefit"

### Part 3: Hands-On Practice (10 minutes)

**Script:**
"Now it's your turn. First, try manual repetition. Then, try a loop."

**Instructions - Manual First:**
1. "Create 6 blocks: FAKE LEFT, GO RIGHT, repeat 3 times"
2. "Click RUN - see it work"
3. "Notice: Lots of blocks!"

**Instructions - Then Loop:**
1. "Delete those blocks"
2. "Drag REPEAT 3 TIMES block"
3. "Drag FAKE LEFT inside loop"
4. "Drag GO RIGHT inside loop"
5. "Click RUN - see it work"
6. "Notice: Only 1 block!"

**Circulate and Help:**
- "Which is better? (Loop!)"
- "What happens if you change the number?"
- "Can you make it repeat 5 times?"

**After 5 minutes:**
"Great! Now try creating your own loop. What move can you repeat?"

### Part 4: Code Connection (2 minutes)

**Script:**
"Now let's see how blocks become code."

**Show Side-by-Side:**
```
Manual:              Loop:
fake_left()         for i in range(3):
go_right()            fake_left()
fake_left()            go_right()
go_right()
fake_left()
go_right()
```

**Explain:**
"Manual repetition = 6 lines. Loop = 3 lines. Same result, less code. That's efficiency!"

**Key Point:**
"Students see the efficiency. They understand why loops matter - less code, same result."

---

## 📝 SESSION 5: WRAP-UP (5 minutes)

### Review (2 minutes)

**Script:**
"Let's review what we learned today."

**Ask Teachers:**
1. "What is a sequence?" (Steps in order)
2. "What is a conditional?" (If this, then that)
3. "What is a loop?" (Repeating actions)

**Key Takeaways:**
- "Sequences: Order matters"
- "Conditionals: Make decisions"
- "Loops: Repeat efficiently"

### Q&A (2 minutes)

**Common Questions:**

**Q: "Do I need to know Python?"**
A: "No! The blocks make it visual. You can learn alongside your students."

**Q: "What if students finish early?"**
A: "They can try Python code, create their own sequences, or help classmates."

**Q: "What if students struggle?"**
A: "The game provides hints. Students can work in pairs. You can provide one-on-one help."

**Q: "How do I grade this?"**
A: "Use the provided rubrics. Focus on effort and understanding, not perfection."

### Next Steps (1 minute)

**Script:**
"Next steps:
1. Try the game yourself (practice)
2. Read Book 1 with your class
3. Use the lesson plans we provided
4. Email us with questions

Remember: You've got this! BallCODE is designed to be simple. If you can drag blocks, you can teach coding!"

**Closing:**
"Thank you for your time today. You're ready to teach coding through basketball. Let's go!"

---

## 🎯 KEY TEACHING PRINCIPLES (Throughout)

### Scratch-Style Principles

**1. Start Simple:**
- Don't overwhelm
- One concept at a time
- Build complexity gradually

**2. Visual First:**
- Show, don't just tell
- Use blocks, not just words
- Let teachers see it work

**3. Hands-On:**
- Teachers must try it
- Don't just demonstrate
- Let them experiment

**4. Immediate Feedback:**
- Game shows results instantly
- Teachers see if it works
- Easy to debug

**5. Celebrate Mistakes:**
- "What did you learn?"
- "How can we fix it?"
- "Debugging is part of coding!"

---

## 📊 SESSION CHECKLIST

### Before Session
- [ ] Prepare materials (game access, projector)
- [ ] Test game exercises
- [ ] Prepare handouts (optional)
- [ ] Review script
- [ ] Set up room

### During Session
- [ ] Welcome and introduction (5 min)
- [ ] Book 1: Sequences (20 min)
- [ ] Book 2: Conditionals (20 min)
- [ ] Book 3: Loops (20 min)
- [ ] Wrap-up and Q&A (5 min)

### After Session
- [ ] Collect feedback
- [ ] Answer follow-up questions
- [ ] Provide resources
- [ ] Schedule follow-up (if needed)

---

## 💡 FACILITATOR TIPS

### Engagement
- Keep it interactive
- Ask questions
- Let teachers try it
- Celebrate successes

### Pacing
- Don't rush
- Give time to practice
- Check for understanding
- Adjust as needed

### Support
- Circulate during practice
- Help when needed
- Encourage experimentation
- Answer questions

---

**Status:** ✅ PD Scripts Complete  
**Next:** Implementation  
**Style:** Scratch-inspired simplicity

---

**Copyright © 2025 Rashad West. All Rights Reserved.**

