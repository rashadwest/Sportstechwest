# Unity License - Step-by-Step Instructions

**Date:** December 24, 2025  
**Complete Guide:** From activation file to GitHub Secrets

---

## 📋 STEP 1: Upload Activation File to Unity Website

### **What You Need:**
- Activation file: `Unity_v2021.3.10f1.alf`
- Location: `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/`

### **Instructions:**

1. **Open Unity License Website:**
   - Go to: https://license.unity3d.com/
   - Website will open in your browser

2. **Find Upload Section:**
   - Look for "Upload" or "Browse" button
   - Or "Manual License Activation" section
   - Click to upload file

3. **Select Activation File:**
   - Click "Browse" or "Choose File"
   - Navigate to: `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/`
   - Select file: `Unity_v2021.3.10f1.alf`
   - Click "Open"

4. **Upload File:**
   - Click "Upload" or "Submit" button
   - Wait for Unity to process (may take 10-30 seconds)

5. **Unity Will Process:**
   - Unity will analyze the activation file
   - You'll see a processing message
   - Wait for results

---

## 📋 STEP 2: Get License File or Serial Number

### **After Upload, Unity Will Give You ONE of These:**

---

### **Option A: License File (.ulf) - If You Get This:**

**What You'll See:**
- Download link for `.ulf` file
- Or file displayed on screen

**Instructions:**
1. **Download the `.ulf` file:**
   - Click download link
   - Save to Desktop or Downloads folder
   - Remember where you saved it

2. **Open the `.ulf` file:**
   - Double-click the downloaded file
   - It will open in TextEdit (or your default text editor)
   - You'll see XML-like content

3. **Copy ALL Contents:**
   - Select All: Press `Cmd + A`
   - Copy: Press `Cmd + C`
   - The file looks like:
     ```xml
     <License>
       <Serial>...</Serial>
       <LicenseVersion>...</LicenseVersion>
       ...
     </License>
     ```

4. **Keep This Copied:**
   - You'll paste it in Step 3
   - Don't close the file yet (or keep it copied)

---

### **Option B: Serial Number - If You Get This:**

**What You'll See:**
- Serial number displayed on screen
- Format: `XXXX-XXXX-XXXX-XXXX-XXXX-XXXX`
- May be labeled "Serial Number" or "License Serial"

**Instructions:**
1. **Copy the Serial Number:**
   - Select the serial number text
   - Copy: Press `Cmd + C`
   - Format should be: `XXXX-XXXX-XXXX-XXXX-XXXX-XXXX`

2. **Keep This Copied:**
   - You'll paste it in Step 3
   - Make sure you copied the entire serial number

---

## 📋 STEP 3: Add to GitHub Secrets

### **Go to GitHub Secrets Page:**

1. **Open GitHub:**
   - Go to: https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
   - Or navigate manually:
     - Go to: https://github.com/rashadwest/BTEBallCODE
     - Click "Settings" (top right of repository page)
     - Click "Secrets and variables" → "Actions"

---

### **If You Got License File (.ulf):**

**Add UNITY_LICENSE Secret:**

1. **Click "New repository secret"** button
   - Top right of the secrets page

2. **Fill in the form:**
   - **Name:** Type exactly: `UNITY_LICENSE`
   - **Secret:** Paste the entire contents of the `.ulf` file
     - Press `Cmd + V` to paste
     - Make sure you paste ALL of it (the entire XML content)

3. **Click "Add secret"**
   - Secret is now saved
   - You'll see it in the list

**✅ Done! Skip to Step 4.**

---

### **If You Got Serial Number:**

**Add UNITY_SERIAL Secret:**

1. **Click "New repository secret"** button
   - Top right of the secrets page

2. **Fill in the form:**
   - **Name:** Type exactly: `UNITY_SERIAL`
   - **Secret:** Paste the serial number
     - Press `Cmd + V` to paste
     - Format: `XXXX-XXXX-XXXX-XXXX-XXXX-XXXX`

3. **Click "Add secret"**
   - Secret is now saved
   - You'll see it in the list

**✅ Done! Skip to Step 4.**

---

## 📋 STEP 4: Push Workflow Update

**I already updated the workflow for you, but you need to push it:**

### **Instructions:**

1. **Open Terminal:**
   - Terminal app is already open
   - Or open new terminal window

2. **Navigate to Unity Project:**
   ```bash
   cd /Users/rashadwest/BTEBallCODE
   ```

3. **Check Changes:**
   ```bash
   git status
   ```
   - Should show: `.github/workflows/unity-webgl-build.yml` modified

4. **Add Changes:**
   ```bash
   git add .github/workflows/unity-webgl-build.yml
   ```

5. **Commit:**
   ```bash
   git commit -m "Add UNITY_LICENSE and UNITY_SERIAL support to workflow"
   ```

6. **Push:**
   ```bash
   git push origin main
   ```

7. **Verify:**
   - GitHub Actions will automatically trigger
   - Check: https://github.com/rashadwest/BTEBallCODE/actions
   - Build should start automatically

---

## ✅ VERIFICATION CHECKLIST

**After completing all steps:**

- [ ] ✅ Activation file uploaded to Unity website
- [ ] ✅ License file (.ulf) OR serial number obtained
- [ ] ✅ `UNITY_LICENSE` OR `UNITY_SERIAL` added to GitHub Secrets
- [ ] ✅ Workflow file updated and pushed
- [ ] ✅ New build triggered automatically
- [ ] ✅ Build succeeds (check GitHub Actions)

---

## 🎯 QUICK REFERENCE

**Activation File Location:**
```
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity_v2021.3.10f1.alf
```

**Unity License Website:**
```
https://license.unity3d.com/
```

**GitHub Secrets Page:**
```
https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
```

**Secret Names:**
- `UNITY_LICENSE` (for license file contents)
- `UNITY_SERIAL` (for serial number)

---

## 📝 SUMMARY

1. **Upload** `.alf` file to Unity website
2. **Get** license file OR serial number
3. **Add** to GitHub Secrets as `UNITY_LICENSE` or `UNITY_SERIAL`
4. **Push** workflow update
5. **Verify** build succeeds

**All steps are FREE - no payment required!**


