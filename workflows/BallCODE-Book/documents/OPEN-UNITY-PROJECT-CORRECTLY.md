# 🎮 How to Open Unity Project Correctly

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Issue:** `open /Users/rashadwest/BTEBallCODE` opens Finder, not Unity Editor

---

## ✅ CORRECT WAYS TO OPEN UNITY PROJECT

### **Method 1: Unity Hub (Recommended)**

1. Open Unity Hub application
2. Click "Open" or "Add" button
3. Navigate to `/Users/rashadwest/BTEBallCODE`
4. Select the folder
5. Unity Hub will open the project in Unity Editor

### **Method 2: Command Line (Direct Unity Editor)**

```bash
# Open Unity project directly in Unity Editor
/Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity \
  -projectPath /Users/rashadwest/BTEBallCODE
```

**Note:** This opens Unity Editor GUI (not headless mode)

### **Method 3: Double-Click Project File**

1. Navigate to `/Users/rashadwest/BTEBallCODE` in Finder
2. Look for any `.unity` scene file
3. Double-click it
4. macOS will ask which app to open with
5. Select Unity Editor

---

## 🚀 QUICK COMMAND FOR AUTOMATION

### **Open Unity Project in Unity Editor:**

```bash
# Method 1: Via Unity Hub (if installed)
open -a "Unity Hub" /Users/rashadwest/BTEBallCODE

# Method 2: Direct Unity Editor
/Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity \
  -projectPath /Users/rashadwest/BTEBallCODE &
```

**The `&` at the end runs it in background so you can continue using terminal.**

---

## 📋 WHAT TO DO AFTER UNITY OPENS

1. **Wait for Unity to load** (30-60 seconds)
2. **Check Console** for package resolution
3. **Wait for "Resolving packages..."** to complete
4. **Verify no errors** in Console
5. **Once packages resolved**, you can:
   - Close Unity Editor
   - Run automation script: `python3 scripts/garvis-apply-unity-components.py`

---

## ⚠️ IF PACKAGES DON'T AUTO-RESOLVE

1. In Unity Editor: **Window → Package Manager**
2. Check for any package errors (red indicators)
3. Click **"Resolve"** or **"Update"** buttons if available
4. Wait for packages to download
5. Check Console for "Packages resolved successfully"

---

**Status:** Unity Editor should now be opening with the project


