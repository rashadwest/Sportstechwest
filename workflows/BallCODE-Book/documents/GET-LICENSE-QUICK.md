# Quick Guide: Get Unity License

**Date:** December 24, 2025  
**Your Situation:** License card in Unity Hub isn't clickable, but you have a Personal license

---

## 🎯 SOLUTION: Open Unity Editor to Generate License File

Since you have a Personal license in Unity Hub, opening Unity Editor will generate the license file automatically.

---

## 📋 STEP-BY-STEP

### **Step 1: Open Unity Project**

**I just opened it for you, but if you need to do it manually:**

1. **In Unity Hub:**
   - Click "Projects" tab
   - Find "BTEBallCODE" project
   - Click to open it

   **OR**

2. **Via Command:**
   ```bash
   open -a Unity\ Hub /Users/rashadwest/BTEBallCODE
   ```

---

### **Step 2: Wait for Unity to Load**

1. **Unity Editor will open**
2. **If prompted for license:**
   - Select "Personal" license
   - Click "Activate"
   - Unity will generate license file

3. **If no prompt:**
   - License is already activated
   - License file should exist (may be in different location)

---

### **Step 3: Find License File**

**After Unity Editor opens, check for license file:**

**Location 1:**
```
~/Library/Application Support/Unity/Unity_lic.ulf
```

**Location 2 (Check this one):**
```
~/.unity3d/Unity_lic.ulf
```

**To check:**
```bash
# Check location 1
ls -la ~/Library/Application\ Support/Unity/Unity_lic.ulf

# Check location 2
ls -la ~/.unity3d/Unity_lic.ulf

# Open both folders in Finder
open ~/Library/Application\ Support/Unity/
open ~/.unity3d/
```

---

### **Step 4: Copy License File Contents**

1. **If file exists:**
   - Double-click `Unity_lic.ulf`
   - Opens in TextEdit
   - Select All (`Cmd + A`)
   - Copy (`Cmd + C`)

2. **The file contains XML-like content:**
   - Looks like: `<License>...</License>`
   - Copy the entire file contents

---

### **Step 5: Add to GitHub Secrets**

1. **Go to:**
   ```
   https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
   ```

2. **Click "New repository secret"**

3. **Add:**
   - **Name:** `UNITY_LICENSE`
   - **Secret:** Paste entire contents of `Unity_lic.ulf` file
   - Click "Add secret"

---

## 🔍 ALTERNATIVE: If License File Still Not Found

### **Option 1: Check Unity Editor About**

1. **In Unity Editor:**
   - Unity menu → About Unity
   - May show license/serial info

### **Option 2: Generate Activation File**

1. **Run this command:**
   ```bash
   /Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity \
     -batchmode \
     -quit \
     -createManualActivationFile
   ```

2. **This creates:** `Unity_v2021.3.10f1.alf` in current directory

3. **Upload to Unity:**
   - Go to: https://license.unity3d.com/
   - Upload the `.alf` file
   - Download the `.ulf` license file
   - Save to: `~/Library/Application Support/Unity/Unity_lic.ulf`

---

## ✅ QUICK CHECKLIST

- [ ] Unity Editor is opening (I just opened it for you)
- [ ] Wait for Unity to fully load
- [ ] Check for license file in both locations
- [ ] Open license file and copy contents
- [ ] Add to GitHub Secrets as `UNITY_LICENSE`
- [ ] Trigger new build

---

**I just opened Unity Editor for you. Once it loads, the license file should be generated. Then check the locations above!**


