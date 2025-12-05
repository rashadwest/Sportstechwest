# 3 Simple Questions for Developer - Let's Start Building!

**Hi! We're building Episode 1 of BallCODE and need your help to connect the story to the game.**

---

## Question 1: Can You Open the Unity Project?

**Simple question:** Can you open the BallCODE Unity project on your computer?

**What we need to know:**
- ✅ Can you open Unity and load the project? (Yes or No)
- ✅ What version of Unity is it? (Like "Unity 2021.3" or "Unity 2022.1")
- ✅ What game modes already exist? (For example: "Training Mode", "Prediction Mode", etc.)
- ✅ Are there scripts called `StoryModeManager.cs` or `GameModeManager.cs` in the project already?

**Why we're asking:**
We have some scripts ready to add, but we need to know what's already there so we don't duplicate anything.

**Example answers:**
- "Yes, I can open it. It's Unity 2021.3. I see Training Mode and Prediction Mode. I don't see those scripts yet."
- "I need access to the project first."

---

## Question 2: How Does Training Mode Work?

**Simple question:** Does Training Mode exist, and how do we add a new exercise to it?

**What we need to know:**
- ✅ Does Training Mode exist? If yes, what does it do right now?
- ✅ How do we add a new exercise? (For example: "Create a new script" or "Add to a list" or "I'm not sure yet")
- ✅ For Episode 1, we need an exercise where students:
  - Watch basketball video
  - Identify when the ball state changes (START → LIVE → DEAD → OUTCOME)
  - Fix mistakes a robot makes

**Why we're asking:**
Episode 1 needs a specific exercise that teaches "state tracking" (like tracking if the ball is in play or not).

**Example answers:**
- "Training Mode exists. It does [describe what it does]. To add a new exercise, we [describe how]."
- "Training Mode doesn't exist yet, so we'd need to build it."
- "I'm not sure yet, but I can look at the code and figure it out."

---

## Question 3: Can the Game Read URLs?

**Simple question:** When someone visits a website link like `ballcode.co/play?episode=1`, can the Unity game read that "episode=1" part?

**What we need to know:**
- ✅ Can the game read URL parameters? (Like `?episode=1` or `?mode=training`)
- ✅ Students need to play without logging in first - is that possible?
- ✅ Can we save progress in the browser (without needing a server)?

**Why we're asking:**
Students will scan QR codes from the book that link to the game. The game needs to know which episode to load from the URL. Also, teachers can't make students create accounts, so it needs to work without login.

**Example answers:**
- "Yes, Unity WebGL can read URLs. We can use [method]."
- "I'm not sure, but I can test it."
- "No-login should work - we can save to browser storage."

---

## What We Have Ready

**We're bringing:**
- ✅ Scripts ready to add (`StoryModeManager.cs`, `GameModeManager.cs`)
- ✅ Episode 1 story content
- ✅ Exercise instructions
- ✅ Step-by-step checklist

**We just need:**
- Your help connecting everything together!

---

## After the Meeting

**What we want to know by the end:**
- [ ] Can you open the project? (Yes or No)
- [ ] What game modes exist? (List them)
- [ ] How do we add the Episode 1 exercise? (Simple plan)
- [ ] When can we start building? (This week? Next week?)

**That's it!** We'll figure out the details as we go.

---

## Helpful Files (If You Want to Look)

**If you want to see what we're building:**
- `Unity-Scripts/StoryModeManager.cs` - Script for story mode
- `Unity-Scripts/GameModeManager.cs` - Script that connects story to game
- `Episode-1-Game-Integration-Spec.md` - What Episode 1 exercise should do
- `Unity-Scripts/QUICK-INTEGRATION-CHECKLIST.md` - Step-by-step guide

**Don't worry if you haven't looked at these yet!** We'll go through everything together.

---

**Goal:** Figure out if we can start building this week! 🚀

