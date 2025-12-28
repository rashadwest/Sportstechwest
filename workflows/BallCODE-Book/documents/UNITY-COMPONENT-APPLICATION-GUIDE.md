# Unity Component Application Guide

**Date:** December 24, 2025  
**Status:** Scripts pushed, ready to apply components

---

## ✅ COMPLETED

1. ✅ All fixed scripts pushed to Unity repository
2. ✅ Git pull successful in Unity project
3. ✅ Unity project has latest scripts

---

## 🎯 NEXT: Apply UI/UX Components

### **Option A: Manual Application (Recommended - Unity Editor Already Open)**

Since Unity Editor is already open, use the manual method:

1. **In Unity Editor:**
   - Open the Unity project (already open)
   - Wait for Unity to finish compiling (check Console for errors)
   - Once compilation is complete, Unity should exit Safe Mode

2. **Apply Components:**
   - **Method 1: Using Menu (If Available)**
     - Go to menu: `Tools` → `UI` → `Apply UI/UX Improvements to Selected Buttons`
     - Select buttons in Hierarchy first
   
   - **Method 2: Using Editor Script**
     - In Unity Editor, open `Assets/Editor/UIUXButtonSetupHelper.cs`
     - The script should have a menu item or can be run via Console
     - Or select buttons and use the context menu

3. **Select Buttons to Update:**
   - Exit button (top-left)
   - Feature buttons (Leaderboard, Settings)
   - Game mode buttons (Chess, Coding, Freeplay, Mathlete, Book)
   - Main action buttons (BallCode, Skins)

4. **Verify:**
   - Check that buttons have `ImprovedButton` or derived components
   - Test hover effects
   - Test click functionality

---

### **Option B: Automated Application (After Closing Unity)**

If you want to use the automated script:

1. **Close Unity Editor:**
   ```bash
   # Check if Unity is running
   ps aux | grep -i unity | grep -v grep
   
   # Close Unity Editor manually (File → Quit)
   ```

2. **Run Automated Script:**
   ```bash
   cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
   export UNITY_PROJECT_PATH=/Users/rashadwest/BTEBallCODE
   python3 scripts/garvis-apply-unity-components.py
   ```

3. **Expected Result:**
   - Unity Editor runs in headless mode
   - Components applied automatically
   - Unity Editor exits
   - Log file created: `unity-apply-components.log`

---

## 📝 MANUAL APPLICATION STEPS (Detailed)

### **Step 1: Verify Unity Compilation**

1. Open Unity Editor (already open)
2. Check Console window
3. Verify no compilation errors
4. Unity should exit Safe Mode automatically

### **Step 2: Locate Buttons in Hierarchy**

1. Open Hierarchy window
2. Find button GameObjects:
   - Exit button (usually in Main Menu scene)
   - Feature buttons (Leaderboard, Settings)
   - Game mode buttons (Chess, Coding, Freeplay, Mathlete, Book)
   - Main action buttons (BallCode, Skins)

### **Step 3: Apply Components**

**For each button type:**

1. **Exit Button:**
   - Select exit button GameObject
   - Remove existing `Button` component (if needed)
   - Add `ExitButton` component
   - Configure settings in Inspector

2. **Feature Buttons:**
   - Select Leaderboard/Settings button
   - Add `FeatureButton` component
   - Configure button type and icon

3. **Game Mode Buttons:**
   - Select game mode button (Chess, Coding, etc.)
   - Add `GameModeButton` component
   - Configure game mode type

4. **Main Action Buttons:**
   - Select BallCode/Skins button
   - Add `MainActionButton` component
   - Configure action type

### **Step 4: Save Scene**

1. Save scene: `File` → `Save Scene`
2. Or `Ctrl+S` / `Cmd+S`

### **Step 5: Test**

1. Press Play button
2. Test hover effects on buttons
3. Test click functionality
4. Verify animations work

---

## 🔧 TROUBLESHOOTING

### **Unity Editor Already Open Error**

**Error:** "It looks like another Unity instance is running with this project open"

**Solution:**
- Close Unity Editor first
- Then run automated script
- OR use manual application method

### **Components Not Applying**

**Check:**
1. Verify `UIUXButtonSetupHelper.cs` is in `Assets/Editor/` folder
2. Check Unity Console for errors
3. Verify button GameObjects exist in scene
4. Check that scripts compile without errors

### **Buttons Not Working**

**Check:**
1. Verify components are added to GameObjects
2. Check Inspector for component settings
3. Verify button references are set
4. Check Unity Console for errors

---

## ✅ SUCCESS CRITERIA

- [ ] Unity compiles without errors
- [ ] Components applied to buttons
- [ ] Buttons have correct component types
- [ ] Hover effects work
- [ ] Click functionality works
- [ ] Scene saved
- [ ] Ready to commit and push

---

## 🚀 AFTER COMPONENTS APPLIED

1. **Commit Scene Changes:**
   ```bash
   cd /Users/rashadwest/BTEBallCODE
   git add Assets/Scenes/*.unity
   git commit -m "Apply UI/UX improvements to buttons"
   git push origin main
   ```

2. **OR Use Garvis Push:**
   ```bash
   cd /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
   python3 scripts/garvis-push.py --game
   ```

3. **Trigger Build:**
   - GitHub Actions will automatically trigger Unity build
   - Monitor build status
   - Verify deployment to Netlify

---

**Current Status:** Unity Editor is open - use manual application method (Option A)


