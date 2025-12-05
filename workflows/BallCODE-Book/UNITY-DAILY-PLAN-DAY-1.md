# Unity Story Mode Setup - Day 1 Plan
## Foundation Setup (Phases 1-5)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** [Fill in date]  
**ONE DOMINO:** Get Story Mode scripts integrated and scene set up with audio ready  
**Why it matters:** Foundation must be solid before integration. Once scripts are in and scene works, everything else builds on this.  
**Success Metric:** Story Mode scene opens in Unity, scripts compile, audio files imported, Episode 1 data created

**Total Time:** 5-7 hours

---

## Pre-Work (5 minutes)

- [ ] Review today's phases
- [ ] Set Deep Work window
- [ ] Assess energy level
- [ ] Eliminate distractions

---

## Phase 1: Project Access and Assessment (30 minutes)

### Objective
Clone Unity project, assess structure, and document dependencies.

### Tasks

1. **Clone GitHub Repository:**
   ```bash
   cd ~/Projects  # or your preferred location
   git clone https://github.com/rashadwest/BTEBallCODE.git
   cd BTEBallCODE
   ```

2. **Open in Unity Hub:**
   - Launch Unity Hub
   - Click "Add" → Select the cloned project folder
   - Unity Hub will detect Unity version
   - Click "Open" to open project

3. **Document Unity Version:**
   - Note the Unity version shown in Unity Hub
   - Check `ProjectSettings/ProjectVersion.txt` if needed
   - Document: Unity version: ___________

4. **Run Assessment Script:**
   ```bash
   cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
   python3 assess-unity-project.py ~/Projects/BTEBallCODE
   ```
   - Review the assessment report
   - Note existing game mode managers
   - Note scene structure
   - Check for any existing Story Mode components

### Delegation to AI
- **Task:** Create project assessment script
- **Goal:** Generate structure report automatically
- **Success Metric:** Report shows all managers, scenes, and dependencies
- **Escalation:** If script fails, manual assessment

### Output
- [ ] Project cloned
- [ ] Unity version documented
- [ ] Assessment report generated
- [ ] Existing managers identified

### Notes
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## Phase 2: Script Integration (1 hour)

### Objective
Copy Story Mode scripts to Unity project and verify compilation.

### Tasks

1. **Run Setup Automation:**
   ```bash
   cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
   ./automate-unity-setup.sh ~/Projects/BTEBallCODE
   ```
   - Script will copy all Story Mode scripts
   - Script will create folder structure
   - Script will create story content folders

2. **Open Unity Project:**
   - Unity should automatically compile scripts
   - Check Unity Console for errors

3. **Verify Scripts:**
   - Open `Assets/Scripts/StoryMode/` in Unity
   - Verify these scripts exist:
     - [ ] StoryModeManager.cs
     - [ ] StoryData.cs
     - [ ] GameModeManager.cs
     - [ ] StoryEpisodeCreator.cs
     - [ ] BallCODEStarter.cs
     - [ ] MetricsCollector.cs

4. **Fix Compilation Errors (if any):**
   - Check Unity Console
   - Fix any namespace issues
   - Fix any missing references
   - Recompile

### Delegation to AI
- **Task:** Create script copy automation
- **Goal:** Automate copying `.cs` files and folder creation
- **Success Metric:** Scripts copied, folders created, compilation successful
- **Escalation:** If automation fails, manual copy

### Output
- [ ] Scripts copied to Unity project
- [ ] Folders created
- [ ] Scripts compile without errors
- [ ] Story content folders created

### Notes
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## Phase 3: Scene Setup (2-3 hours)

### Objective
Create Story Mode scene with UI Canvas and connect all references.

### Tasks

1. **Create Story Mode Scene:**
   - File → New Scene → Basic (Built-in)
   - Save as: `Assets/Scenes/StoryModeScene.unity`

2. **Set Up Main GameObjects:**
   - Create empty GameObject: `BallCODEStarter`
     - Add `BallCODEStarter` component
   - Create empty GameObject: `StoryModeManager`
     - Add `StoryModeManager` component
   - Create empty GameObject: `GameModeManager`
     - Add `GameModeManager` component

3. **Create UI Canvas:**
   - GameObject → UI → Canvas
   - Name: `StoryModeCanvas`
   - Canvas Scaler: Scale With Screen Size
   - Reference Resolution: 1920x1080

4. **Create Page Turner Container:**
   - Right-click `StoryModeCanvas` → UI → Panel
   - Name: `PageTurnerContainer`
   - Add `CanvasGroup` component

5. **Create Left Page:**
   - Right-click `PageTurnerContainer` → UI → Panel
   - Name: `LeftPage`
   - Add child: UI → Image → Name: `LeftPageImage`
   - Add child: UI → Text - TextMeshPro → Name: `LeftPageText`
     - Font size: 20
     - Alignment: Top-Left
     - Word wrap: Enabled

6. **Create Right Page:**
   - Right-click `PageTurnerContainer` → UI → Panel
   - Name: `RightPage`
   - Add child: UI → Image → Name: `RightPageImage`
   - Add child: UI → Text - TextMeshPro → Name: `RightPageText`
     - Font size: 18
     - Alignment: Top-Left

7. **Create Navigation Panel:**
   - Right-click `StoryModeCanvas` → UI → Panel
   - Name: `NavigationPanel`
   - Position at bottom
   - Add buttons:
     - `PreviousButton` (Text: "← Previous")
     - `NextButton` (Text: "Next →")
     - `PlayExerciseButton` (Text: "Play Exercise", initially inactive)
   - Add `PageIndicator` text (Text: "Page 1 of 6")

8. **Connect References in Inspector:**
   - Select `StoryModeManager` GameObject
   - Drag references:
     - [ ] StoryModeCanvas
     - [ ] PageTurnerContainer
     - [ ] LeftPageImage
     - [ ] RightPageImage
     - [ ] LeftPageText
     - [ ] RightPageText
     - [ ] NextButton
     - [ ] PreviousButton
     - [ ] PlayExerciseButton
     - [ ] PageIndicator
   - Add `AudioSource` component to `StoryModeManager`
   - Drag AudioSource to "Narration Source"

9. **Connect BallCODEStarter:**
   - Select `BallCODEStarter` GameObject
   - Drag `StoryModeManager` to "Story Mode Manager"
   - Drag `GameModeManager` to "Game Mode Manager"
   - Enable "Auto Start Story Mode" for testing

### Delegation to AI
- **Task:** Create scene setup guide with step-by-step instructions
- **Goal:** Clear instructions for manual setup
- **Success Metric:** Scene created, all GameObjects set up, references connected
- **Escalation:** If unclear, provide screenshots/detailed steps

### Output
- [ ] Story Mode scene created
- [ ] All GameObjects set up
- [ ] UI Canvas created with all elements
- [ ] All references connected in Inspector
- [ ] Scene saves without errors

### Notes
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## Phase 4: Audio Integration (30 minutes)

### Objective
Import book narration audio files and assign to StoryModeManager.

### Tasks

1. **Locate Audio Files:**
   - Find book narration audio files
   - Note location: ___________

2. **Import Audio Files:**
   - In Unity, navigate to `Assets/StoryContent/Audio/`
   - Create folders: `Episode1/`, `Episode2/`, `Episode3/`
   - Import audio files:
     - Episode 1: `episode1_spread1.mp3`, `episode1_spread2.mp3`, etc.
     - Episode 2: `episode2_spread1.mp3`, etc.
     - Episode 3: `episode3_spread1.mp3`, etc.

3. **Configure Audio Import Settings:**
   - Select each audio file
   - Inspector → Audio Import Settings:
     - Audio Type: Audio Clip
     - Load Type: Streaming (for long narrations)
     - Compression Format: Vorbis
     - Quality: 70-80

4. **Assign Audio Clips to StoryModeManager:**
   - Select `StoryModeManager` GameObject
   - Set "Episode 1 Audio Clips" array size to number of spreads
   - Drag audio clips to array in order
   - Repeat for Episode 2 and Episode 3

### Delegation to AI
- **Task:** Create audio import automation script
- **Goal:** Automate audio file organization and assignment
- **Success Metric:** Audio files imported, organized, assigned to StoryModeManager
- **Escalation:** If automation fails, manual import

### Output
- [ ] Audio files imported
- [ ] Audio files organized by episode
- [ ] Audio clips assigned to StoryModeManager arrays
- [ ] Audio import settings configured

### Notes
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## Phase 5: Episode Data Creation (1-2 hours)

### Objective
Create ScriptableObject assets for Episodes 1-3 with story content.

### Tasks

1. **Open Story Episode Creator:**
   - Unity Menu: BallCODE → Create Story Episode
   - Or: Right-click in Project → Create → BallCODE → Story Episode

2. **Create Episode 1:**
   - Name: `Episode1`
   - Episode Number: 1
   - Title: "The Tip-off Trial"
   - Subtitle: "Learn how robots think—through the game you love"
   - Coding Concept: "State"
   - Math Concept: "Possession Statistics"
   - AI Concept: "Vision Cues & State Detection"
   - Monster Name: "Shadow Press Scouts"
   - Game Mode: "Training"
   - Create spreads (6 spreads for Episode 1)
   - Add story text to each spread
   - Mark spreads with exercises

3. **Create Episode 2:**
   - Name: `Episode2`
   - Episode Number: 2
   - Title: "The If/Then Fork in the Key"
   - Coding Concept: "Conditionals"
   - Game Mode: "Prediction"
   - Create spreads and add story text

4. **Create Episode 3:**
   - Name: `Episode3`
   - Episode Number: 3
   - Title: "Loop of the Rotating Guardians"
   - Coding Concept: "Loops"
   - Game Mode: "Math"
   - Create spreads and add story text

5. **Assign Episodes to StoryModeManager:**
   - Select `StoryModeManager` GameObject
   - Set "Episodes" array size to 3
   - Drag `Episode1`, `Episode2`, `Episode3` assets to array

6. **Test Episode Data:**
   - Play scene
   - Verify Episode 1 loads
   - Verify story text displays
   - Verify page navigation works

### Delegation to AI
- **Task:** Enhance StoryEpisodeCreator tool to import from markdown
- **Goal:** Auto-create episode assets from story markdown files
- **Success Metric:** Episodes 1-3 created with story content
- **Escalation:** If tool doesn't work, manual creation

### Output
- [ ] Episode 1 ScriptableObject created
- [ ] Episode 2 ScriptableObject created
- [ ] Episode 3 ScriptableObject created
- [ ] Episodes assigned to StoryModeManager
- [ ] Story text displays correctly
- [ ] Page navigation works

### Notes
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## End of Day Review (15 minutes)

### Completion Checklist

- [ ] Phase 1: Project cloned and assessed
- [ ] Phase 2: Scripts integrated and compiling
- [ ] Phase 3: Scene created and set up
- [ ] Phase 4: Audio files imported and assigned
- [ ] Phase 5: Episode data created

### What Worked Well
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

### What Needs Improvement
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

### Tomorrow's ONE Domino
**Task:** Get game integrated and deployed to Netlify  
**Why it matters:** Game must be live and functional. Once deployed, students can access it and you can start generating revenue.

---

## Troubleshooting

### Scripts Not Compiling
- Check Unity Console for errors
- Verify all scripts are in `Assets/Scripts/StoryMode/`
- Check for missing using statements
- Verify Unity version compatibility

### Scene Not Loading
- Check that scene is saved
- Verify all GameObjects are active
- Check Console for errors
- Verify StoryModeManager has episodes assigned

### Audio Not Playing
- Check AudioSource is assigned
- Verify audio clips are assigned
- Check audio import settings
- Test audio clips individually

### Episode Data Not Showing
- Verify episodes are assigned to StoryModeManager
- Check that spreads have text content
- Verify UI text references are connected
- Check Console for errors

---

## Next Steps (Day 2)

1. Phase 6: Game Mode Integration
2. Phase 7: WebGL Build
3. Phase 8: Netlify Deployment
4. Phase 9: Testing and Verification


