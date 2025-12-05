# Episode 1: The Tip-off Trial - Game Integration Specification

**Status:** Planning Complete  
**Date:** Week 2, Wednesday  
**Target:** Training Mode Integration

---

## Integration Overview

**Episode:** Episode 1 - The Tip-off Trial  
**Game Mode:** Mathlete Mode (with level creation) - **UPDATED: Training Mode doesn't exist**  
**Coding Concept:** State (start/live/dead/outcome)  
**Learning Objective:** Track possession states and maintain state through transitions

**Note:** Original plan was Training Mode, but developer confirmed Training Mode doesn't exist. Using Mathlete mode with level creation instead.

---

## Flow: Story → Skill Pit-Stop → Game Exercise → Return

### Step 1: Story Reading
- User reads Episode 1 story (all 3 acts)
- Story introduces state concept through narrative
- Story shows Nova learning to track states

### Step 2: Skill Pit-Stop
- User reads Skill Pit-Stop mini-lesson
- Explains state concept in kid-friendly terms
- Provides examples and connections to coding

### Step 3: QR Code / Short URL
- User scans QR code or clicks short URL
- Links to: `ballcode.co/play?mode=mathlete&episode=1&level=state-tracker&source=book`
- Pre-configures Mathlete Mode with Episode 1 level

### Step 4: Game Exercise (Mathlete Mode)
- User plays state-tracking exercise in Mathlete Mode
- Exercise: Watch game footage → Identify state changes → Correct robot mistakes
- No-login required for first play (confirmed by developer)
- 60-90 second exercise duration

### Step 5: Return to Story
- Exercise completion unlocks next content
- User returns to story or continues to next episode
- Progress is saved (prompt after first success)

---

## Mathlete Mode Exercise Design (Updated)

### Exercise: State Tracker

**Objective:** Identify and track state changes in basketball footage

**Mode:** Mathlete Mode (with Episode 1 level creation)

**Process:**
1. Watch 10-15 second basketball clip
2. Identify current state (START, LIVE, DEAD, OUTCOME)
3. Identify state transitions as they occur
4. Correct robot mistakes (robot misidentifies states)
5. Complete 3-5 state identification challenges

**Note:** This exercise will be created as a level in the Mathlete mode system. Need to clarify with developer how level creation works.

**Scoring:**
- Correct state identification: +10 points
- Correct transition identification: +15 points
- Robot correction: +20 points
- Perfect run: Bonus +50 points

**Difficulty Levels:**
- Easy: Clear state changes, slow pace
- Medium: Faster pace, some ambiguous moments
- Hard: Fast pace, multiple rapid state changes

---

## QR Code / URL Structure

### Short URL Format (Updated)
```
ballcode.co/play?mode=mathlete&episode=1&level=state-tracker&source=book
```

### Parameters:
- `mode=mathlete` - Loads Mathlete Mode (Training Mode doesn't exist)
- `episode=1` - Episode 1 configuration
- `level=state-tracker` - Episode 1 level in Mathlete mode
- `source=book` - Tracks that user came from book

### URL Reading Implementation:
- Use UnityWebRequests to read URL parameters (confirmed by developer)
- Parse in BTEManager or BallcodeManager
- Configure Mathlete mode with Episode 1 level

### QR Code Generation
- Generate QR code for each episode
- Include in Episode 1 PDF/document
- Place after Skill Pit-Stop section
- Also include at end of story for "Continue in-game" link

---

## Unity Integration Points

### StoryModeManager.cs Integration
- Episode 1 maps to Mathlete Mode (needs update - was Training Mode)
- `TransitionToGame()` method handles episode-to-mode mapping
- `OnExerciseComplete()` handles return flow

### BTEManager / BallcodeManager Integration
- `LoadGameMode("Mathlete", 1, "State", "Shadow Press Scouts")` called
- Mathlete Mode receives episode parameters via URL
- Level is pre-configured with Episode 1 content

### Mathlete Mode Level Creation Needed
- Create Episode 1 state-tracking level in Mathlete system
- Configure for Episode 1 learning objectives
- Add state identification UI elements
- Implement state transition tracking
- **Need to clarify:** How does level creation work in Mathlete mode?

---

## No-Login First Play

### Implementation
- First play: No account required
- Progress tracked locally (browser storage)
- After first success: Prompt to save progress
- "Save Progress" button appears
- Optional account creation for cloud sync

### User Flow
1. User scans QR code
2. Game loads directly (no login screen)
3. User plays exercise
4. Exercise completes
5. Success screen shows: "Great job! Save your progress?"
6. User can continue without saving or create account

---

## Return Flow

### After Exercise Completion
1. `OnExerciseComplete(success, score)` called in StoryModeManager
2. If success:
   - Unlock next spread (if more content)
   - Show completion notification
   - Offer to continue story or play again
3. Return to story mode UI
4. Progress saved (if user opted in)

### Completion Rewards
- Episode 1 completion badge
- Unlock Episode 2 preview
- Show stats: "You correctly identified 8/10 state changes!"

---

## Technical Specifications

### URL Handling (Updated)
- WebGL build: Use UnityWebRequests to read URL (confirmed by developer)
- Parse URL parameters to determine episode, mode, and level
- Implementation: Use `UnityWebRequest.UnEscapeURL()` to parse query parameters
- Parse in BTEManager or BallcodeManager
- Fallback to default if parameters missing

### Exercise Configuration
- Episode 1 exercise: State Tracker
- Duration: 60-90 seconds
- Difficulty: Adaptive (starts easy, increases)
- Feedback: Immediate (correct/incorrect indicators)

### Progress Tracking (Updated)
- **Primary:** Server storage (more robust - recommended by developer)
- **Fallback:** Browser localStorage (works but less robust)
- Cloud sync: Optional (requires account)
- Track: Completion status, score, time spent
- **Note:** Server storage preferred, but browser storage works as fallback

---

## Testing Checklist

- [ ] QR code generates correctly
- [ ] Short URL redirects properly
- [ ] Training Mode loads with Episode 1 configuration
- [ ] State-tracking exercise works correctly
- [ ] No-login first play functions
- [ ] Return flow works (exercise → story)
- [ ] Progress tracking saves correctly
- [ ] Completion unlocks next content
- [ ] All state transitions are identifiable
- [ ] Exercise is age-appropriate (grades 3-8)

---

## Implementation Notes

### Priority
1. **High:** QR code generation and URL structure
2. **High:** Training Mode exercise configuration
3. **Medium:** Return flow implementation
4. **Medium:** Progress tracking
5. **Low:** Advanced features (cloud sync, analytics)

### Dependencies (Updated)
- Unity StoryModeManager.cs (exists)
- BTEManager (exists - confirmed by developer)
- BallcodeManager (exists - confirmed by developer)
- Mathlete Mode level creation system (needs clarification)
- UnityWebRequests for URL reading (confirmed available)
- QR code generation tool/service
- Server storage backend (preferred) or browser storage (fallback)

### Timeline
- Week 2: Planning and specification (this document)
- Week 3: Unity integration and exercise implementation
- Week 4: Testing and refinement
- Week 5: Final polish and production readiness

---

## Next Steps

1. ✅ Integration spec created (this document)
2. [ ] Review with Unity developer/team
3. [ ] Create Episode 1 Training Mode exercise variant
4. [ ] Implement QR code generation
5. [ ] Test end-to-end flow
6. [ ] Document for production


