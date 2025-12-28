# How to Find Buttons in Unity Hierarchy

**Date:** December 24, 2025  
**Issue:** Buttons not visible in Hierarchy

---

## 🎯 SOLUTION: Open the Main Menu Scene

The buttons are in the **"Main Menu"** scene, not the default "Untitled" scene.

### **Step 1: Open Main Menu Scene**

1. **In Unity Editor:**
   - Go to `File` → `Open Scene`
   - Navigate to: `Assets/Scenes/Main Menu.unity`
   - Click "Open"

   **OR**

   - In the Project window, navigate to `Assets/Scenes/`
   - Double-click `Main Menu.unity`

### **Step 2: Find Buttons in Hierarchy**

Once the Main Menu scene is open, look for:

1. **Canvas GameObject** (UI elements are usually under a Canvas)
   - Look for "Canvas" in Hierarchy
   - Expand it (click the arrow) to see child objects

2. **Button GameObjects** (typically named):
   - Exit button (top-left)
   - Leaderboard button
   - Settings button
   - Game mode buttons: Chess, Coding, Freeplay, Mathlete, Book
   - Main action buttons: BallCode, Skins

3. **Common Locations:**
   - Under `Canvas` → `MainMenuPanel` → buttons
   - Or directly under `Canvas` → buttons
   - Or under `Canvas` → `UI` → buttons

### **Step 3: If Buttons Still Not Visible**

**Check:**
1. **Scene View vs Game View:**
   - Buttons are UI elements - they appear in Game View, not Scene View
   - Switch to Game View tab (top of Scene window)

2. **Canvas Settings:**
   - Select Canvas in Hierarchy
   - Check Inspector - Canvas should be set to "Screen Space - Overlay" or "Screen Space - Camera"

3. **Search in Hierarchy:**
   - Use the search bar at the top of Hierarchy window
   - Type "Button" to filter and find all buttons

---

## 🔍 ALTERNATIVE: Search for Buttons

**In Unity Editor:**

1. **Use Hierarchy Search:**
   - Click in the search bar at top of Hierarchy
   - Type: `Button` or `button`
   - All GameObjects with "Button" in the name will show

2. **Use Project Search:**
   - In Project window, search for button prefabs
   - Look for prefabs in `Assets/Prefabs/` folder

---

## 📝 QUICK CHECKLIST

- [ ] Opened "Main Menu" scene (not "Untitled")
- [ ] Looking in Hierarchy window (not Scene view)
- [ ] Expanded Canvas GameObject
- [ ] Used search bar to find "Button"
- [ ] Checked Game View (not Scene View)

---

## 🎯 EXPECTED RESULT

After opening Main Menu scene, you should see:
- Canvas GameObject
- Various button GameObjects (Exit, Leaderboard, Settings, Chess, Coding, etc.)
- These are the buttons you can select and apply UI/UX improvements to

---

**Next:** Once you find the buttons, select them and use `Tools` → `UI` → `Apply UI/UX Improvements to Selected Buttons`


