# Unity Story Mode Setup - Day 2 Plan
## Integration and Deployment (Phases 6-9)

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** [Fill in date]  
**ONE DOMINO:** Get game integrated and deployed to Netlify  
**Why it matters:** Game must be live and functional. Once deployed, students can access it and you can start generating revenue.  
**Success Metric:** Story → Game → Story flow works, WebGL build deployed to Netlify, accessible via URL

**Total Time:** 5-6 hours

---

## Pre-Work (5 minutes)

- [ ] Review today's phases
- [ ] Review Day 1 completion status
- [ ] Set Deep Work window
- [ ] Assess energy level
- [ ] Eliminate distractions

---

## Phase 6: Game Mode Integration (2-3 hours)

### Objective
Integrate existing game mode managers with Story Mode system.

### Tasks

1. **Identify Existing Game Mode Managers:**
   - Review assessment report from Day 1
   - List existing managers:
     - Training Mode Manager: ___________
     - Prediction Mode Manager: ___________
     - Math Mode Manager: ___________
     - Other managers: ___________

2. **Update GameModeManager.cs:**
   - Open `Assets/Scripts/StoryMode/GameModeManager.cs`
   - Update manager references to match your existing managers:
     ```csharp
     [Header("Game Mode Managers")]
     public YourTrainingManager trainingMode;
     public YourPredictionManager predictionMode;
     public YourMathManager mathMode;
     ```
   - Update `LoadTrainingMode()`, `LoadPredictionMode()`, `LoadMathMode()` methods
   - Ensure methods call your existing manager's start methods

3. **Create Adapter Scripts (if needed):**
   - If your managers have different interfaces, create adapters
   - Example: `TrainingModeAdapter.cs`
   - Bridge Story Mode config to your game's format

4. **Implement Completion Callbacks:**
   - In each game mode manager, add completion handler:
     ```csharp
     public void OnExerciseComplete(bool success, float score)
     {
         // Your existing completion logic
         
         // Notify story mode
         if (GameModeManager.Instance != null)
         {
             GameModeManager.Instance.OnExerciseComplete(success, score);
         }
     }
     ```

5. **Connect References in Inspector:**
   - Select `GameModeManager` GameObject
   - Assign your game mode managers:
     - [ ] Training Mode Manager
     - [ ] Prediction Mode Manager
     - [ ] Math Mode Manager

6. **Test Integration:**
   - Play Story Mode scene
   - Navigate to Episode 1, spread with exercise
   - Click "Play Exercise" button
   - Verify game mode loads with correct parameters
   - Complete exercise
   - Verify return to Story Mode

### Delegation to AI
- **Task:** Analyze existing code and create integration guide
- **Goal:** Clear instructions for connecting game modes
- **Success Metric:** Game modes accept Story Mode config, transitions work
- **Escalation:** If integration fails, create adapter scripts

### Output
- [ ] Game mode managers identified
- [ ] GameModeManager.cs updated
- [ ] Adapter scripts created (if needed)
- [ ] Completion callbacks implemented
- [ ] References connected in Inspector
- [ ] Story → Game transition works
- [ ] Game → Story return works

### Notes
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## Phase 7: WebGL Build (1 hour)

### Objective
Build Unity project as WebGL and test locally.

### Tasks

1. **Configure Build Settings:**
   - File → Build Settings
   - Platform: WebGL
   - Click "Switch Platform" (if needed)
   - Player Settings:
     - Company Name: BallCODE
     - Product Name: BallCODE Story Mode
     - Default Icon: Set if you have one
     - Resolution and Presentation:
       - Default Canvas Width: 1920
       - Default Canvas Height: 1080
       - Run In Background: Enabled

2. **Configure Compression:**
   - Player Settings → Publishing Settings
   - Compression Format: Gzip (recommended)
   - Or: Brotli (smaller, but less compatible)

3. **Add Scenes to Build:**
   - File → Build Settings
   - Add Open Scenes
   - Ensure `StoryModeScene` is included
   - Set as first scene (index 0)

4. **Run Build Automation:**
   ```bash
   cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
   ./automate-unity-build.sh ~/Projects/BTEBallCODE ~/Builds/WebGL
   ```
   - Or build manually: File → Build Settings → Build
   - Select output folder: `~/Builds/WebGL`

5. **Test Build Locally:**
   ```bash
   cd ~/Builds/WebGL
   python3 -m http.server 8000
   ```
   - Open browser: http://localhost:8000
   - Test Story Mode loads
   - Test page navigation
   - Test audio playback (if applicable)
   - Test URL parameters: `?episode=1`

6. **Verify Build Output:**
   - Check for `index.html`
   - Check for `.wasm` files
   - Check for `.data` files
   - Check for `.js` files
   - Build size should be reasonable (< 50MB compressed)

### Delegation to AI
- **Task:** Create Unity build automation script
- **Goal:** Automate WebGL build process
- **Success Metric:** WebGL build created, tested locally, works in browser
- **Escalation:** If build fails, manual build with troubleshooting

### Output
- [ ] Build settings configured
- [ ] WebGL build created
- [ ] Build tested locally
- [ ] Story Mode works in browser
- [ ] URL parameters work
- [ ] Build size acceptable

### Notes
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## Phase 8: Netlify Setup and Deployment (1 hour)

### Objective
Deploy WebGL build to Netlify and make it accessible.

### Tasks

1. **Create Netlify Account (if needed):**
   - Go to https://netlify.com
   - Sign up or log in
   - Account created: [ ] Yes [ ] No

2. **Install Netlify CLI (if needed):**
   ```bash
   npm install -g netlify-cli
   ```

3. **Login to Netlify:**
   ```bash
   netlify login
   ```
   - Follow browser authentication

4. **Run Deployment Automation:**
   ```bash
   cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
   ./automate-netlify-deploy.sh ~/Builds/WebGL ballcode-game
   ```
   - Script will create site (if new)
   - Script will deploy build
   - Script will provide site URL

5. **Verify Deployment:**
   - Visit site URL provided
   - Test Story Mode loads
   - Test page navigation
   - Test URL parameters: `?episode=1`
   - Test on mobile device (if applicable)

6. **Configure Custom Domain (optional):**
   - Netlify Dashboard → Site Settings → Domain Management
   - Add custom domain: `game.ballcode.co` (or your choice)
   - Follow DNS configuration instructions

### Delegation to AI
- **Task:** Create Netlify deployment automation
- **Goal:** Automate deployment to Netlify
- **Success Metric:** Site created, build deployed, accessible via URL
- **Escalation:** If deployment fails, manual deployment

### Output
- [ ] Netlify account created
- [ ] Netlify CLI installed and logged in
- [ ] Site created on Netlify
- [ ] Build deployed successfully
- [ ] Site accessible via URL
- [ ] Story Mode works on deployed site
- [ ] Custom domain configured (if applicable)

### Notes
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## Phase 9: Testing and Verification (1 hour)

### Objective
Test complete integration end-to-end and verify all functionality.

### Tasks

1. **Test Story Mode Flow:**
   - [ ] Story Mode loads correctly
   - [ ] Episode 1 displays
   - [ ] Page navigation works (Previous/Next)
   - [ ] Audio narration plays (if set up)
   - [ ] Page indicator updates correctly

2. **Test Story → Game Transition:**
   - [ ] Navigate to Episode 1, spread with exercise
   - [ ] "Play Exercise" button appears
   - [ ] Click "Play Exercise"
   - [ ] Game mode loads with correct parameters
   - [ ] Game mode displays Episode 1 content
   - [ ] Game mode shows correct concept (State)

3. **Test Game → Story Return:**
   - [ ] Complete exercise in game mode
   - [ ] Exercise completion triggers callback
   - [ ] Return to Story Mode
   - [ ] Next spread/episode unlocks
   - [ ] Progress saved correctly

4. **Test URL Parameters (WebGL):**
   - [ ] `?episode=1` loads Episode 1
   - [ ] `?episode=2` loads Episode 2
   - [ ] `?episode=3` loads Episode 3
   - [ ] Invalid episode handles gracefully

5. **Test All Episodes:**
   - [ ] Episode 1 complete flow works
   - [ ] Episode 2 complete flow works
   - [ ] Episode 3 complete flow works

6. **Test on Different Devices:**
   - [ ] Desktop browser (Chrome, Firefox, Safari)
   - [ ] Mobile browser (if applicable)
   - [ ] Tablet (if applicable)

7. **Performance Check:**
   - [ ] Load time acceptable (< 10 seconds)
   - [ ] Page transitions smooth
   - [ ] Audio playback smooth
   - [ ] No console errors

### Delegation to AI
- **Task:** Create testing checklist
- **Goal:** Comprehensive test coverage
- **Success Metric:** All tests pass, flow works end-to-end
- **Escalation:** If tests fail, debug and fix

### Output
- [ ] All Story Mode tests pass
- [ ] Story → Game transition works
- [ ] Game → Story return works
- [ ] URL parameters work
- [ ] All episodes work
- [ ] Cross-device testing complete
- [ ] Performance acceptable
- [ ] No critical bugs found

### Notes
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## End of Day Review (15 minutes)

### Completion Checklist

- [ ] Phase 6: Game modes integrated
- [ ] Phase 7: WebGL build created and tested
- [ ] Phase 8: Deployed to Netlify
- [ ] Phase 9: All tests pass

### What Worked Well
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

### What Needs Improvement
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

### Next Steps
- [ ] Generate QR codes for physical books
- [ ] Test QR code deep linking
- [ ] Create marketing materials
- [ ] Plan next book release

---

## Troubleshooting

### Game Mode Not Loading
- Check GameModeManager has managers assigned
- Verify managers implement required methods
- Check Console for errors
- Verify episode-to-game-mode mapping

### Build Fails
- Check Unity Console for errors
- Verify all scenes are added to build
- Check build output folder permissions
- Verify WebGL platform is selected

### Deployment Fails
- Check Netlify CLI is logged in
- Verify build folder contains index.html
- Check Netlify site limits
- Review Netlify deployment logs

### URL Parameters Not Working
- Verify WebGL build (not Editor)
- Check URL parameter parsing code
- Test in different browsers
- Check browser console for errors

---

## Success Criteria

### Day 2 Complete When:
- [ ] Story Mode → Game Mode transition works
- [ ] Game Mode → Story Mode return works
- [ ] WebGL build deployed to Netlify
- [ ] Site accessible via URL
- [ ] All episodes functional
- [ ] URL parameters work
- [ ] End-to-end flow tested

### Ready for Production When:
- [ ] All tests pass
- [ ] Performance acceptable
- [ ] No critical bugs
- [ ] Custom domain configured
- [ ] QR codes generated
- [ ] Marketing materials ready

---

## Celebration! 🎉

You've completed the Unity Story Mode integration! The game is now live and ready for students to access.

**Next:** Generate QR codes, create marketing materials, and start promoting your books!


