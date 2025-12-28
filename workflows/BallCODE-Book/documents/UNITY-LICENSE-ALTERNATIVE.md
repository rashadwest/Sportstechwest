# Alternative: Use Unity Serial Number Instead

**Date:** December 24, 2025  
**If License File Not Found:** Use Serial Number Method

---

## 🎯 ALTERNATIVE METHOD: Use Serial Number

If you can't find the license file, you can use your Unity serial number instead.

---

## 📋 STEP 1: Get Serial Number from Unity Editor

### **Once Unity Editor Opens:**

1. **In Unity Editor:**
   - Go to: **Unity** menu → **About Unity**
   - Serial number may be displayed here

2. **OR Check Console:**
   - Open Console window in Unity
   - Look for license/serial information in logs

3. **OR Check Unity Hub:**
   - In Unity Hub → Settings → Licenses
   - Serial number may be visible in license details

---

## 📋 STEP 2: Generate Activation File (If Needed)

### **If Serial Number Not Visible:**

1. **Run this command in Terminal:**
   ```bash
   /Applications/Unity/Hub/Editor/2021.3.10f1/Unity.app/Contents/MacOS/Unity \
     -batchmode \
     -quit \
     -createManualActivationFile
   ```

2. **This creates:** `Unity_v2021.3.10f1.alf` in your current directory

3. **Upload to Unity:**
   - Go to: https://license.unity3d.com/
   - Upload the `.alf` file
   - You'll get a serial number or license file

---

## 📋 STEP 3: Add Serial Number to GitHub

1. **Go to GitHub:**
   ```
   https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
   ```

2. **Add Secret:**
   - Click "New repository secret"
   - **Name:** `UNITY_SERIAL`
   - **Secret:** Paste your Unity serial number
   - Format: `XXXX-XXXX-XXXX-XXXX-XXXX-XXXX`
   - Click "Add secret"

---

## ✅ SIMPLEST: Wait for Unity to Generate License

**Since Unity Editor is opening:**

1. **Wait for Unity to fully load** (may take 1-2 minutes)

2. **After Unity loads, check for license file:**
   ```bash
   # Check if license file was created
   ls -la ~/Library/Application\ Support/Unity/Unity_lic.ulf
   
   # If found, open it
   open ~/Library/Application\ Support/Unity/Unity_lic.ulf
   ```

3. **If file exists:**
   - Copy entire contents
   - Add to GitHub as `UNITY_LICENSE` secret

---

## 🔍 CHECK LICENSE FILE NOW

**Run this command to check:**
```bash
# Check if license file exists
if [ -f ~/Library/Application\ Support/Unity/Unity_lic.ulf ]; then
  echo "✅ License file found!"
  cat ~/Library/Application\ Support/Unity/Unity_lic.ulf
else
  echo "⏳ License file not found yet"
  echo "Waiting for Unity Editor to generate it..."
  echo "Check again in 30 seconds"
fi
```

---

**I opened Unity Editor for you. Once it loads, check for the license file at:**
```
~/Library/Application Support/Unity/Unity_lic.ulf
```


