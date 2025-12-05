# Quick Integration Checklist

Use this checklist to integrate Story Mode with your existing BallCODE game.

## Pre-Integration

- [ ] Reviewed your existing game structure
- [ ] Identified your game mode managers
- [ ] Understood your scene architecture
- [ ] Backed up your project

## Step 1: Add Scripts

- [ ] Copied all scripts from `Unity-Scripts/` to `Assets/Scripts/StoryMode/`
- [ ] No compilation errors in Unity Console
- [ ] All scripts visible in Project window

## Step 2: Create Story Mode Scene/UI

- [ ] Created `StoryModeScene` (or added to existing scene)
- [ ] Created `StoryModeCanvas` with UI elements
- [ ] Set up page turner UI (left/right pages)
- [ ] Added navigation buttons (Previous/Next)
- [ ] Added "Play Exercise" button
- [ ] Added page indicator text

## Step 3: Set Up Managers

- [ ] Created `StoryModeManager` GameObject
- [ ] Assigned all UI references in Inspector
- [ ] Created `GameModeManager` GameObject
- [ ] Created `BallCODEStarter` GameObject (optional, for auto-setup)

## Step 4: Connect Game Modes

- [ ] Identified your Training Mode manager
- [ ] Identified your Prediction Mode manager
- [ ] Identified your Math Mode manager
- [ ] Identified your Block Coding manager (if exists)
- [ ] Assigned managers to `GameModeManager` in Inspector
- [ ] Updated manager methods to accept `*ModeConfig` parameters
- [ ] Added completion callbacks to notify story mode

## Step 5: Create Test Data

- [ ] Added `TestStoryDataHelper` to scene (for quick testing)
- [ ] OR created ScriptableObject assets for Episode 1
- [ ] Assigned episode data to `StoryModeManager.episodes`
- [ ] Verified episode data appears in Inspector

## Step 6: Test Basic Flow

- [ ] Story mode appears when scene starts (or button clicked)
- [ ] Can navigate pages (Previous/Next buttons work)
- [ ] Page indicator updates correctly
- [ ] "Play Exercise" button appears on exercise spreads
- [ ] Clicking "Play Exercise" transitions to game mode
- [ ] Game mode receives correct configuration
- [ ] Completing exercise returns to story mode
- [ ] Next spread/episode unlocks after completion

## Step 7: Test URL Parameters (WebGL)

- [ ] Built WebGL version
- [ ] Tested `?story&episode=1` URL parameter
- [ ] Correct episode loads from URL
- [ ] QR code links work (if applicable)

## Step 8: Polish

- [ ] Audio narration works (if implemented)
- [ ] Page turn animations smooth
- [ ] UI looks good on different screen sizes
- [ ] Error handling works (null checks, etc.)
- [ ] Console is clean (no errors/warnings)

## Integration Complete!

Once all items are checked, your Story Mode is integrated and ready to use.

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Managers not found | Check GameObject names and component assignments |
| Buttons don't work | Verify button references in Inspector |
| Game mode doesn't load | Check manager assignments and method signatures |
| Story doesn't appear | Verify episodes array is populated |
| Completion doesn't return | Check `OnExerciseComplete` callback is called |

