# How to Get License from Unity Hub (When Card Isn't Clickable)

**Date:** December 24, 2025  
**Issue:** License card in Unity Hub isn't clickable

---

## 🎯 SOLUTION: Get License File Directly

Since the license card in Unity Hub isn't clickable, we'll find the license file on your computer.

---

## 📍 METHOD 1: Find License File on Your Mac

### **Step 1: Check Common Locations**

**Location 1 (Most Common):**
```bash
~/Library/Application Support/Unity/Unity_lic.ulf
```

**Location 2 (Alternative):**
```bash
~/.unity3d/Unity_lic.ulf
```

**Location 3 (Older Versions):**
```bash
~/Library/Preferences/com.unity3d.UnityEditor5.x.plist
```

---

### **Step 2: Open in Finder**

**Option A: Terminal Command:**
```bash
# Open the Unity folder in Finder
open ~/Library/Application\ Support/Unity/
```

**Option B: Manual Navigation:**
1. Open Finder
2. Press `Cmd + Shift + G` (Go to Folder)
3. Type: `~/Library/Application Support/Unity/`
4. Press Enter
5. Look for file: `Unity_lic.ulf`

---

### **Step 3: Open License File**

1. **If file exists:**
   - Double-click `Unity_lic.ulf`
   - It will open in TextEdit
   - Select All (`Cmd + A`)
   - Copy (`Cmd + C`)
   - This is your license file contents

2. **If file doesn't exist:**
   - You may need to activate Unity first
   - See Method 2 below

---

## 📍 METHOD 2: Activate Unity to Generate License

### **If License File Doesn't Exist:**

1. **Open Unity Editor:**
   ```bash
   open -a Unity\ Hub /Users/rashadwest/BTEBallCODE
   ```

2. **Unity will prompt for activation:**
   - If first time, Unity will ask to activate license
   - Choose "Personal" license
   - Follow activation steps
   - License file will be created automatically

3. **After activation:**
   - License file created at: `~/Library/Application Support/Unity/Unity_lic.ulf`
   - Copy file contents

---

## 📍 METHOD 3: Get Serial Number from Unity Editor

### **If You Can't Find License File:**

1. **Open Unity Editor:**
   ```bash
   open -a Unity\ Hub /Users/rashadwest/BTEBallCODE
   ```

2. **Check About Unity:**
   - Unity menu → About Unity
   - Serial number may be displayed here

3. **OR Check License File (if it exists):**
   - Open `Unity_lic.ulf` in TextEdit
   - Look for `<Serial>` tag
   - Copy the serial number value

---

## 📍 METHOD 4: Use Unity Command Line

### **Generate Activation File:**

1. **Run Unity in batch mode:**
   ```bash
   /Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity \
     -batchmode \
     -quit \
     -createManualActivationFile
   ```

2. **This creates:**
   - File: `Unity_v2021.3.10f1.alf`
   - Location: Current directory

3. **Upload to Unity:**
   - Go to: https://license.unity3d.com/
   - Upload the `.alf` file
   - Download the `.ulf` license file
   - Save it to: `~/Library/Application Support/Unity/Unity_lic.ulf`

---

## 🎯 QUICKEST METHOD: Check if License File Exists

**Run this command:**
```bash
# Check if license file exists
if [ -f ~/Library/Application\ Support/Unity/Unity_lic.ulf ]; then
  echo "✅ License file found!"
  open ~/Library/Application\ Support/Unity/Unity_lic.ulf
else
  echo "❌ License file not found - need to activate Unity"
  echo "Opening Unity Editor to activate..."
  open -a Unity\ Hub /Users/rashadwest/BTEBallCODE
fi
```

---

## 📋 ADD TO GITHUB SECRETS

**Once you have the license:**

1. **Go to GitHub:**
   ```
   https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
   ```

2. **Add Secret:**
   - Click "New repository secret"
   - **Name:** `UNITY_LICENSE`
   - **Secret:** Paste entire contents of `Unity_lic.ulf` file
   - Click "Add secret"

---

## ✅ NEXT STEPS

1. **Find license file** (use commands above)
2. **Copy license file contents**
3. **Add to GitHub Secrets** as `UNITY_LICENSE`
4. **Trigger new build**

---

**Let me check if the license file exists on your system...**


