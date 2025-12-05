# Developer Meeting - Quick Prep

**Meeting Goal:** Figure out if we can start building Episode 1 this week!

**Time Needed:** 30-45 minutes

---

## The 3 Questions We Need Answered

### Question 1: Can You Open the Unity Project?

**What we need:**
- ✅ Can you open Unity and load the BallCODE project? (Yes or No)
- ✅ What Unity version? (e.g., "Unity 2021.3")
- ✅ What game modes exist? (e.g., "Training Mode", "Prediction Mode")
- ✅ Do `StoryModeManager.cs` or `GameModeManager.cs` already exist?

**Why:** We have scripts ready to add, but need to know what's already there.

---

### Question 2: How Does Training Mode Work?

**What we need:**
- ✅ Does Training Mode exist? What does it do?
- ✅ How do we add a new exercise? (e.g., "Create new script" or "Add to list")
- ✅ For Episode 1, we need an exercise where students:
  - Watch basketball video
  - Identify ball state changes (START → LIVE → DEAD → OUTCOME)
  - Fix mistakes a robot makes

**Why:** Episode 1 needs a specific "state tracking" exercise.

---

### Question 3: Can the Game Read URLs?

**What we need:**
- ✅ Can Unity read URL parameters? (e.g., `ballcode.co/play?episode=1`)
- ✅ Can students play without logging in?
- ✅ Can we save progress in browser (no server needed)?

**Why:** Students scan QR codes from the book. Game needs to know which episode from the URL. No login required for teachers.

---

## What We're Bringing

✅ **Scripts ready to add:**
- `Unity-Scripts/StoryModeManager.cs`
- `Unity-Scripts/GameModeManager.cs`
- `Unity-Scripts/StoryData.cs`
- Other supporting scripts

✅ **Content ready:**
- Episode 1 story (complete)
- Exercise instructions
- Integration specs

✅ **Documentation:**
- `Unity-Scripts/QUICK-INTEGRATION-CHECKLIST.md` - Step-by-step guide
- `Episode-1-Game-Integration-Spec.md` - What Episode 1 needs to do
- `Unity-Scripts/BALLCODE-SPECIFIC-INTEGRATION.md` - Technical details

---

## Developer Answers (Received)

### ✅ Question 1: Unity Project Access
- **Unity Version:** 2021.3.31f ✅
- **Game Modes:** Mathlete mode, Freeplay mode ✅
- **Managers:** BTEManager, BallcodeManager exist ✅
- **Training Mode:** ❌ Does NOT exist
- **Alternative:** Mathlete mode can replace Training Mode with level creation ✅

### ✅ Question 2: Training Mode / Exercise Creation
- **Training Mode:** ❌ Does not exist
- **Solution:** Use Mathlete mode with level creation for Episode 1 ✅
- **How to add exercise:** Create level in Mathlete mode system ✅

### ✅ Question 3: URL Reading & No-Login
- **URL Reading:** ✅ Yes - Unity can read URLs with UnityWebRequests
- **No-Login Play:** ✅ Yes - Possible to play without logging in
- **Progress Storage:** Browser storage works, but server storage is better/more robust ✅

---

## Updated Integration Plan

**See:** `DEVELOPER-ANSWERS-INTEGRATION-PLAN.md` for complete updated plan.

**Key Changes:**
- Episode 1 → Mathlete Mode (instead of Training Mode)
- Use UnityWebRequests for URL reading
- Server storage preferred (browser as fallback)
- No-login confirmed possible

---

## What We Need From You (Follow-Up Questions)

**About Mathlete Mode:**
- [ ] How does Mathlete mode currently work?
- [ ] How do we create a new level in Mathlete mode?
- [ ] What parameters can we configure for a level?
- [ ] Can we add Episode 1 specific exercises to Mathlete?
- [ ] Does Mathlete mode support state tracking concepts?

**About Integration:**
- [ ] Where should we add URL reading code? (BTEManager? BallcodeManager?)
- [ ] How do we configure Mathlete mode from URL parameters?
- [ ] What's the best way to implement no-login first play?
- [ ] Server storage - do you have a backend ready, or should we set one up?

**About Episode 1 Exercise:**
- [ ] What's the best way to implement state tracking in Mathlete mode?
- [ ] Can we show basketball video/clips in Mathlete mode?
- [ ] How do students identify state changes in the exercise?
- [ ] What's the completion flow back to story mode?

---

## Files You Might Want to Look At (Optional)

**If you want to see what we're building before the meeting:**
- `Unity-Scripts/StoryModeManager.cs` - Story mode script
- `Unity-Scripts/GameModeManager.cs` - Connects story to game
- `Episode-1-Game-Integration-Spec.md` - Episode 1 requirements
- `Unity-Scripts/QUICK-INTEGRATION-CHECKLIST.md` - Integration steps

**Don't worry if you haven't looked yet!** We'll go through everything together.

---

## Next Steps After Meeting

Once we have answers to the 3 questions:
1. We'll know what's already built vs. what needs to be added
2. We'll create a simple integration plan
3. We'll start building Episode 1

**Goal:** Start building this week! 🚀

---

**Questions?** Just ask! This is a collaborative effort - we're here to make it work together.


