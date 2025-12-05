# Episode 1: The Tip-off Trial - Exercises

**Target Time:** 60-90 seconds per exercise  
**Age Range:** Grades 3-8

---

## Exercise A: Label States in a Play

**Time:** 60 seconds  
**Type:** Worksheet/Quick Check

### Instructions

Read the basketball scenario below and label each state change. Write START, LIVE, DEAD, or OUTCOME next to each step.

### Scenario

1. The referee throws the ball up for the tip-off. State: _______

2. Your teammate jumps and catches the ball. State: _______

3. Your teammate starts dribbling up the court. State: _______

4. The ball bounces out of bounds. The referee blows the whistle. State: _______

5. The other team inbounds the ball. State: _______

6. They make a basket and score 2 points. State: _______

### Answer Key

1. START (tip-off begins)
2. LIVE (your team has possession)
3. LIVE (still in play, still your team)
4. DEAD (play stopped, ball out of bounds)
5. LIVE (other team has possession now)
6. OUTCOME (play ended with points scored)

---

## Exercise B: Write State Transitions

**Time:** 90 seconds  
**Type:** Interactive/Coding Exercise

### Instructions

Draw arrows to show how states can transition (change from one to another). Use the states: START, LIVE, DEAD, OUTCOME.

### Part 1: Basic Transitions

Draw arrows showing:
- How START becomes LIVE
- How LIVE becomes DEAD
- How DEAD becomes LIVE again
- How LIVE becomes OUTCOME

### Part 2: Create Your Own Play

Write a short basketball play (3-5 steps) and label the state for each step.

**Example:**
1. Tip-off begins → START
2. We grab the ball → LIVE (us)
3. We pass the ball → LIVE (us) - still in play
4. We score! → OUTCOME

**Your Turn:**
1. ________________ → _______
2. ________________ → _______
3. ________________ → _______
4. ________________ → _______
5. ________________ → _______

### Answer Key (Part 1)

```
START → LIVE → DEAD → LIVE → OUTCOME
  ↑                        ↓
  └────────────────────────┘
```

**Explanation:**
- START → LIVE: When someone gets the ball
- LIVE → DEAD: When play stops (out of bounds, foul, etc.)
- DEAD → LIVE: When play resumes
- LIVE → OUTCOME: When the play ends (score, turnover, shot clock)

---

## Exercise C: Handle an Edge Case

**Time:** 90 seconds  
**Type:** Advanced Challenge

### Instructions

An "edge case" is a situation that doesn't happen often, but you still need to handle it correctly. Read the scenario and figure out what the state should be.

### Scenario: The Tied-Up Ball

During a game, two players grab the ball at the same time and neither can get it free. The referee stops play and calls a "jump ball."

**Question 1:** What state is the game in right now?
- A) START
- B) LIVE
- C) DEAD
- D) OUTCOME

**Question 2:** After the jump ball, what state does it become?
- A) START
- B) LIVE
- C) DEAD
- D) OUTCOME

**Question 3:** If the jump ball results in your team getting the ball, what state is it now?
- A) START
- B) LIVE (us)
- C) LIVE (opponent)
- D) DEAD

### Challenge Question

Can you think of another edge case in basketball? What happens to the state in that situation?

**Example Edge Cases:**
- Shot clock violation
- 24-second violation
- Technical foul
- Flagrant foul
- Overtime tip-off

### Answer Key

**Question 1:** C) DEAD
- The play has stopped. No one has clear possession. The state is DEAD.

**Question 2:** A) START
- A jump ball is like a mini tip-off. The state resets to START.

**Question 3:** B) LIVE (us)
- Your team got the ball. You now have possession, so the state is LIVE (us).

**Challenge Question - Example Answers:**
- **Shot clock violation:** LIVE → DEAD → OUTCOME (turnover)
- **Overtime tip-off:** OUTCOME (end of regulation) → START (overtime begins)
- **Technical foul:** LIVE → DEAD → LIVE (free throws) → DEAD → LIVE (play resumes)

---

## Teacher Guide

### Learning Objectives

After completing these exercises, students should be able to:
1. Identify the four states of possession (START, LIVE, DEAD, OUTCOME)
2. Track state changes in a basketball scenario
3. Understand state transitions and rules
4. Apply state concepts to edge cases

### Discussion Questions

1. Why can't you skip states? (You can't go from START directly to OUTCOME)
2. What happens if you lose track of the state? (You make mistakes, like Nova did at first)
3. How does tracking state help you in basketball? (You know what you can do next)
4. How does this relate to coding? (Programs use states to know what to do)

### Extension Activities

1. **State Tracker:** Have students watch a basketball game (live or video) and track the states for 5 possessions.
2. **Code It:** Have students write simple code or pseudocode showing state transitions:
   ```
   if state == START:
       wait for tip-off
   elif state == LIVE:
       play basketball
   elif state == DEAD:
       wait for play to resume
   elif state == OUTCOME:
       record result
   ```
3. **Create Your Own:** Have students create a state diagram for another activity (video game, cooking, etc.)

### Common Mistakes

- **Confusing LIVE and DEAD:** Remind students that LIVE means the ball is actively in play, DEAD means play has stopped.
- **Skipping States:** Students might try to go from START to OUTCOME. Remind them states must follow the transition rules.
- **Not Specifying Team:** When state is LIVE, students should specify LIVE (us) or LIVE (opponent).

### Assessment

- **Exercise A:** 6 points (1 point per correct label)
- **Exercise B:** 10 points (5 for transitions, 5 for play creation)
- **Exercise C:** 15 points (5 per question, 5 for challenge)

**Total:** 31 points

---

## Integration with Game

After completing these exercises, students can:
1. Scan the QR code to access the BallCODE game
2. Play the "State Tracker" exercise in Training Mode
3. Practice identifying states in real-time game scenarios
4. Earn points for correctly tracking state changes

**Game Link:** [To be generated]  
**QR Code:** [To be generated]

---

**Total Exercise Time:** ~4-5 minutes for all three exercises  
**Recommended:** Complete exercises after reading Episode 1 story and Skill Pit-Stop




