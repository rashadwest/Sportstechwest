# Developer Answers - Integration Plan Update

**Date:** Current  
**Status:** Answers Received - Integration Plan Updated  
**Unity Version:** 2021.3.31f

---

## Developer Answers Summary

### ✅ Question 1: Unity Project Access
- **Unity Version:** 2021.3.31f
- **Game Modes:** Mathlete mode, Freeplay mode
- **Managers:** BTEManager, BallcodeManager exist
- **Training Mode:** ❌ Does NOT exist
- **Alternative:** Mathlete mode can replace Training Mode with level creation

### ✅ Question 2: Training Mode / Exercise Creation
- **Training Mode:** ❌ Does not exist
- **Solution:** Use Mathlete mode with level creation for Episode 1
- **How to add exercise:** Create level in Mathlete mode system

### ✅ Question 3: URL Reading & No-Login
- **URL Reading:** ✅ Yes - Unity can read URLs with UnityWebRequests
- **No-Login Play:** ✅ Yes - Possible to play without logging in
- **Progress Storage:** Browser storage works, but server storage is better/more robust

---

## Updated Integration Plan

### Episode 1: The Tip-off Trial → Mathlete Mode

**Original Plan:** Episode 1 → Training Mode  
**Updated Plan:** Episode 1 → Mathlete Mode (with level creation)

**Why the Change:**
- Training Mode doesn't exist in the current game
- Mathlete mode can be configured with level creation
- Mathlete mode likely handles the mathematical/coding exercises we need

---

## Episode 1 Integration Strategy

### Option 1: Mathlete Mode with Level Creation (Recommended)

**Approach:**
1. Create Episode 1 level in Mathlete mode system
2. Level teaches state tracking (START → LIVE → DEAD → OUTCOME)
3. Students complete level to learn state concept
4. Return flow to story after completion

**What We Need:**
- Access to Mathlete mode level creation system
- Understanding of how to configure levels
- Episode 1 specific exercise parameters

**Questions for Developer:**
- How do we create a new level in Mathlete mode?
- Can we configure level parameters (difficulty, concepts, etc.)?
- How does Mathlete mode currently work? (What does it teach?)

---

### Option 2: Freeplay Mode Adaptation

**Approach:**
1. Use Freeplay mode as base
2. Add Episode 1 specific constraints/rules
3. Configure for state tracking exercise

**What We Need:**
- Understanding of Freeplay mode capabilities
- How to add constraints/rules to Freeplay
- Integration with Episode 1 learning objectives

**Questions for Developer:**
- What does Freeplay mode do currently?
- Can we add constraints or specific exercises to Freeplay?
- Is Freeplay suitable for Episode 1 state tracking?

---

## Updated URL Structure

### URL Format (Confirmed Working)
```
ballcode.co/play?episode=1&mode=mathlete&level=state-tracker&source=book
```

**Parameters:**
- `episode=1` - Episode 1 configuration
- `mode=mathlete` - Loads Mathlete mode (instead of training)
- `level=state-tracker` - Specific Episode 1 level
- `source=book` - Tracks that user came from book

**Implementation:**
- Use UnityWebRequests to read URL parameters
- Parse parameters in BTEManager or BallcodeManager
- Configure Mathlete mode with Episode 1 level

---

## No-Login Implementation

### Confirmed: Possible to Play Without Login

**Implementation Approach:**
1. First play: No account required
2. Game loads directly from QR code/URL
3. Progress tracked locally (browser storage) OR server (preferred)
4. After first success: Optional "Save Progress" prompt
5. Server storage is more robust (recommended by developer)

**User Flow:**
1. Student scans QR code from book
2. Game loads directly (no login screen)
3. Mathlete mode loads with Episode 1 level
4. Student completes level
5. Success screen: "Great job! Save your progress?"
6. Optional: Create account for cloud sync (not required)

**Storage Options:**
- **Browser Storage:** Works, but less robust
- **Server Storage:** Better, more robust (recommended)
- **Decision:** Use server storage if possible, browser as fallback

---

## Updated Episode-to-Mode Mapping

### Episode 1: The Tip-off Trial → Mathlete Mode
- **Original:** Training Mode (doesn't exist)
- **Updated:** Mathlete Mode with state-tracking level
- **Learning:** State management (START/LIVE/DEAD/OUTCOME)

### Episode 2: The If/Then Fork → ?
- **Original:** Opponent Prediction Mode
- **Updated:** TBD - Need to confirm if this mode exists
- **Learning:** Conditional logic (if/then/else)

### Episode 3: Loop of the Rotating Guardians → Mathlete Mode
- **Original:** Math Version
- **Updated:** Mathlete Mode (likely already suitable)
- **Learning:** Loops and sequences

---

## Integration Points

### BTEManager Integration
- **Purpose:** Likely handles game mode management
- **Action:** Add Episode 1 level configuration
- **URL Reading:** Use UnityWebRequests to parse URL parameters
- **Level Loading:** Configure Mathlete mode with Episode 1 level

### BallcodeManager Integration
- **Purpose:** Likely handles BallCODE-specific game logic
- **Action:** Add Episode 1 state tracking logic
- **Exercise Configuration:** Set up state identification exercise
- **Return Flow:** Handle completion and return to story

---

## Next Steps

### Immediate (This Week)
1. **Clarify Mathlete Mode:**
   - How does Mathlete mode work?
   - How do we create levels?
   - What parameters can we configure?

2. **Update Integration Specs:**
   - Change Training Mode → Mathlete Mode
   - Update Episode 1 exercise design for Mathlete
   - Revise URL structure

3. **Test URL Reading:**
   - Implement UnityWebRequests URL parsing
   - Test with sample URLs
   - Verify parameter reading works

### Short Term (Next Week)
4. **Create Episode 1 Level:**
   - Design state-tracking exercise for Mathlete
   - Configure level parameters
   - Test exercise flow

5. **Implement No-Login Flow:**
   - Remove login requirement for first play
   - Set up progress storage (server preferred)
   - Test end-to-end flow

6. **Return Flow Implementation:**
   - Handle exercise completion
   - Return to story mode
   - Unlock next content

---

## Questions for Developer (Follow-Up)

### About Mathlete Mode:
1. How does Mathlete mode currently work?
2. How do we create a new level in Mathlete mode?
3. What parameters can we configure for a level?
4. Can we add Episode 1 specific exercises to Mathlete?
5. Does Mathlete mode support state tracking concepts?

### About Freeplay Mode:
1. What does Freeplay mode do?
2. Can we add constraints or specific exercises to Freeplay?
3. Would Freeplay work for Episode 1 state tracking?

### About Integration:
1. Where should we add URL reading code? (BTEManager? BallcodeManager?)
2. How do we configure Mathlete mode from URL parameters?
3. What's the best way to implement no-login first play?
4. Server storage - do you have a backend ready, or should we set one up?

### About Episode 1 Exercise:
1. What's the best way to implement state tracking in Mathlete mode?
2. Can we show basketball video/clips in Mathlete mode?
3. How do students identify state changes in the exercise?
4. What's the completion flow back to story mode?

---

## Updated Technical Specifications

### Unity Version
- **Version:** 2021.3.31f
- **Compatibility:** All scripts must be compatible with this version

### URL Reading Implementation
```csharp
// Example: Using UnityWebRequests to read URL
using UnityEngine.Networking;
using System;

string url = Application.absoluteURL;
Uri uri = new Uri(url);
string episode = UnityWebRequest.UnEscapeURL(uri.Query);
// Parse parameters and configure Mathlete mode
```

### Game Mode Configuration
- **Mode:** Mathlete (instead of Training)
- **Level:** Episode 1 state-tracking level
- **Parameters:** episode=1, level=state-tracker, source=book

### Progress Storage
- **Primary:** Server storage (more robust)
- **Fallback:** Browser storage (localStorage)
- **Implementation:** Use server if available, browser as backup

---

## Updated Files Needed

### Files to Update:
1. ✅ `Episode-1-Game-Integration-Spec.md` - Change Training → Mathlete
2. ✅ `Story-Mode-Integration-Plan.md` - Update mode mapping
3. ✅ `DEVELOPER-MEETING-PREP.md` - Mark questions as answered
4. ✅ `Unity-Scripts/BALLCODE-SPECIFIC-INTEGRATION.md` - Update for Mathlete

### New Files to Create:
1. `Mathlete-Mode-Episode-1-Integration.md` - Specific integration guide
2. `URL-Parsing-Implementation.md` - UnityWebRequests guide
3. `No-Login-Flow-Implementation.md` - First play without login

---

## Success Criteria

### Integration Complete When:
- [ ] Mathlete mode loads Episode 1 level from URL
- [ ] Episode 1 state-tracking exercise works in Mathlete
- [ ] No-login first play functions correctly
- [ ] Progress saves (server or browser)
- [ ] Return flow works (exercise → story)
- [ ] QR codes link correctly to Episode 1 level
- [ ] All URL parameters are parsed correctly

---

## Timeline Update

### Week 3: Integration & Implementation
- **Day 1-2:** Clarify Mathlete mode capabilities
- **Day 3-4:** Implement URL reading with UnityWebRequests
- **Day 5:** Create Episode 1 level in Mathlete mode

### Week 4: Testing & Refinement
- **Day 1-2:** Test no-login flow
- **Day 3-4:** Test Episode 1 exercise
- **Day 5:** Test return flow and progress saving

### Week 5: Final Polish
- **Day 1-2:** Fix any issues
- **Day 3-4:** Final testing
- **Day 5:** Production readiness

---

## Key Changes Summary

| Original Plan | Updated Plan | Status |
|-------------|--------------|--------|
| Training Mode | Mathlete Mode | ✅ Updated |
| Training Mode exists | Training Mode doesn't exist | ✅ Confirmed |
| URL reading (assumed) | UnityWebRequests confirmed | ✅ Confirmed |
| Browser storage only | Server storage preferred | ✅ Updated |
| No-login (assumed) | No-login confirmed possible | ✅ Confirmed |
| Unity version unknown | Unity 2021.3.31f | ✅ Confirmed |
| Game modes unknown | Mathlete, Freeplay | ✅ Confirmed |
| Managers unknown | BTEManager, BallcodeManager | ✅ Confirmed |

---

**Next Action:** Clarify Mathlete mode capabilities and level creation process with developer.



