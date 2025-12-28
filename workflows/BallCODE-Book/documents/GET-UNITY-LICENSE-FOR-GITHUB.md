# How to Get Unity License for GitHub Actions

**Date:** December 24, 2025  
**Purpose:** Get Unity license file or serial number to configure GitHub Actions

---

## 🎯 METHOD 1: Get Unity License File (Recommended)

### **Step 1: Find License File on Mac**

**Location:**
```
~/Library/Application Support/Unity/Unity_lic.ulf
```

**Quick Command:**
```bash
# Check if license file exists
ls -la ~/Library/Application\ Support/Unity/Unity_lic.ulf

# If it exists, view it
cat ~/Library/Application\ Support/Unity/Unity_lic.ulf
```

**OR navigate manually:**
1. Open Finder
2. Press `Cmd + Shift + G` (Go to Folder)
3. Type: `~/Library/Application Support/Unity/`
4. Look for file: `Unity_lic.ulf`
5. Right-click → Open With → TextEdit (to view contents)

---

### **Step 2: Copy License File Contents**

1. **Open the license file:**
   - Double-click `Unity_lic.ulf`
   - It will open in TextEdit or your default text editor

2. **Copy all contents:**
   - Select All (`Cmd + A`)
   - Copy (`Cmd + C`)
   - The file contains XML-like content with your license info

---

### **Step 3: Add to GitHub Secrets**

1. **Go to GitHub Repository:**
   - Navigate to: https://github.com/rashadwest/BTEBallCODE
   - Click **Settings** (top right of repository page)

2. **Go to Secrets:**
   - In left sidebar, click **Secrets and variables**
   - Click **Actions**

3. **Add New Secret:**
   - Click **New repository secret** button
   - **Name:** `UNITY_LICENSE`
   - **Secret:** Paste the entire contents of `Unity_lic.ulf` file
   - Click **Add secret**

---

## 🎯 METHOD 2: Get Unity Serial Number (Alternative)

### **Step 1: Open Unity Hub**

1. **Launch Unity Hub:**
   - Open Unity Hub application
   - Or: `open -a "Unity Hub"`

2. **Go to Settings:**
   - Click **Settings** icon (gear icon, top right)
   - Or: Unity Hub menu → Preferences

3. **Go to Licenses:**
   - Click **Licenses** tab in left sidebar
   - You'll see your active license(s)

---

### **Step 2: Find Serial Number**

**In Unity Hub Licenses:**
- Look for your license (usually "Personal" license)
- The serial number is displayed next to the license type
- It looks like: `XXXX-XXXX-XXXX-XXXX-XXXX-XXXX`

**OR check license file:**
- Open `Unity_lic.ulf` file
- Look for `<Serial>` tag
- Copy the serial number value

---

### **Step 3: Add to GitHub Secrets**

1. **Go to GitHub Repository:**
   - Navigate to: https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions

2. **Add New Secret:**
   - Click **New repository secret**
   - **Name:** `UNITY_SERIAL`
   - **Secret:** Paste your Unity serial number
   - Click **Add secret**

---

## 🎯 METHOD 3: Generate License via Command Line (If File Not Found)

### **If License File Doesn't Exist:**

1. **Activate Unity License:**
   ```bash
   # Navigate to Unity Editor
   cd /Applications/Unity/Hub/Editor/2021.3.10f1
   
   # Run Unity with activation
   ./Unity.app/Contents/MacOS/Unity -batchmode -quit -createManualActivationFile
   ```

2. **This creates an activation file:**
   - Location: `Unity_v2021.3.10f1.alf`
   - Upload this to Unity website to get license file
   - Then follow Method 1 above

---

## 📋 QUICK REFERENCE

### **License File Location:**
```bash
~/Library/Application Support/Unity/Unity_lic.ulf
```

### **View License File:**
```bash
# Terminal
cat ~/Library/Application\ Support/Unity/Unity_lic.ulf

# Or open in Finder
open ~/Library/Application\ Support/Unity/
```

### **GitHub Secrets URL:**
```
https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
```

### **Secret Names:**
- `UNITY_LICENSE` (for license file contents)
- `UNITY_SERIAL` (for serial number only)

---

## ✅ VERIFICATION

**After adding secret:**

1. **Check GitHub Actions workflow:**
   - Go to: https://github.com/rashadwest/BTEBallCODE/actions
   - Trigger a new build
   - Check logs - should not see "Missing Unity License" error

2. **Test Build:**
   ```bash
   cd /Users/rashadwest/BTEBallCODE
   git commit --allow-empty -m "Test build with Unity license"
   git push origin main
   ```

---

## 🔍 TROUBLESHOOTING

### **License File Not Found:**

**Check alternative locations:**
```bash
# Check common locations
ls -la ~/Library/Application\ Support/Unity/
ls -la ~/.unity3d/
ls -la ~/Library/Preferences/com.unity3d.UnityEditor5.x.plist
```

**If still not found:**
- Use Unity Hub to view license
- Use Method 2 (Serial Number) instead
- Or generate new license file (Method 3)

### **License File Empty or Invalid:**

- Make sure you copied the entire file contents
- Check file isn't corrupted
- Try using serial number method instead

---

## 📝 STEP-BY-STEP CHECKLIST

- [ ] Open Finder
- [ ] Navigate to `~/Library/Application Support/Unity/`
- [ ] Find `Unity_lic.ulf` file
- [ ] Open file and copy all contents
- [ ] Go to GitHub repository settings
- [ ] Navigate to Secrets → Actions
- [ ] Add new secret: `UNITY_LICENSE`
- [ ] Paste license file contents
- [ ] Save secret
- [ ] Trigger new build to test

---

**Recommended:** Use Method 1 (License File) - it's the most reliable method.


