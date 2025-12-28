# Unity License - Step-by-Step Instructions

**Date:** December 24, 2025  
**Status:** ✅ Activation file created!

---

## ✅ STEP 1: ACTIVATION FILE CREATED

**File Location:**
```
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity_v2021.3.10f1.alf
```

**I just opened this file location for you in Finder.**

---

## 📋 STEP 2: UPLOAD TO UNITY WEBSITE

### **I just opened the Unity license website for you!**

**If it didn't open, go to:**
```
https://license.unity3d.com/
```

### **On the Website:**

1. **Click "Upload" or "Browse" button**
2. **Select the file:** `Unity_v2021.3.10f1.alf`
   - Location: `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/`
   - Or check your Desktop/Finder
3. **Click "Upload" or "Submit"**
4. **Unity will process the file**

---

## 📋 STEP 3: DOWNLOAD LICENSE FILE

**After uploading:**

1. **Unity will generate a license file**
2. **Download the `.ulf` file** (Unity License File)
3. **Save it to your Desktop** (or anywhere easy to find)

---

## 📋 STEP 4: COPY LICENSE FILE CONTENTS

1. **Open the downloaded `.ulf` file:**
   - Double-click it
   - Opens in TextEdit
   - You'll see XML-like content

2. **Copy entire contents:**
   - Select All (`Cmd + A`)
   - Copy (`Cmd + C`)
   - The file looks like:
     ```xml
     <License>
       <Serial>...</Serial>
       <LicenseVersion>...</LicenseVersion>
       ...
     </License>
     ```

---

## 📋 STEP 5: ADD TO GITHUB SECRETS

1. **Go to GitHub:**
   ```
   https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
   ```

2. **Click "New repository secret"**

3. **Add Secret:**
   - **Name:** `UNITY_LICENSE`
   - **Secret:** Paste the entire contents of the `.ulf` file
   - Click "Add secret"

---

## ✅ ALTERNATIVE: USE SERIAL NUMBER (FASTER)

**If you want to skip the upload process:**

1. **After uploading the `.alf` file to Unity website:**
   - Unity will show you a serial number
   - Copy that serial number

2. **Add to GitHub as `UNITY_SERIAL` instead:**
   - Go to: https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
   - Add secret: `UNITY_SERIAL`
   - Paste serial number
   - Click "Add secret"

**This is faster than using the full license file!**

---

## 🎯 QUICK CHECKLIST

- [x] ✅ Activation file created (`Unity_v2021.3.10f1.alf`)
- [ ] ⏳ Upload `.alf` file to https://license.unity3d.com/
- [ ] ⏳ Download `.ulf` license file OR get serial number
- [ ] ⏳ Copy license file contents OR copy serial number
- [ ] ⏳ Add to GitHub Secrets as `UNITY_LICENSE` or `UNITY_SERIAL`
- [ ] ⏳ Trigger new build to test

---

## 📝 FILE LOCATIONS

**Activation File:**
```
/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity_v2021.3.10f1.alf
```

**License File (after download):**
- Save to Desktop or Downloads folder
- Then copy contents

**GitHub Secrets:**
```
https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
```

---

**Next Steps:**
1. Upload the `.alf` file to Unity website (I opened it for you)
2. Get the license file or serial number
3. Add to GitHub Secrets
4. Trigger build!


