# Get Unity License for CI/CD - FINAL SOLUTION

**Date:** December 24, 2025  
**Problem:** Email/password not working in CI/CD  
**Solution:** Get license file or serial number

---

## 🔍 THE PROBLEM

**Error:** "Missing Unity License File and no Serial was found"

**Why:**
- `game-ci/unity-builder` may not support email/password for Personal licenses in CI/CD
- Unity Personal licenses might need a license file or serial for CI/CD
- Email/password works locally but not in automated builds

---

## ✅ SOLUTION: Upload Activation File

**You already have the activation file!** Upload it to get a license file or serial number.

---

## 📋 STEP-BY-STEP (5 Minutes)

### **Step 1: Upload Activation File**

1. **Go to Unity License Website:**
   ```
   https://license.unity3d.com/
   ```
   (I'll open this for you)

2. **Find the Upload Button:**
   - Look for "Upload" or "Browse" button
   - Click it

3. **Select Your File:**
   - Navigate to: `/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/`
   - Select: `Unity_v2021.3.10f1.alf`
   - Click "Open"

4. **Upload:**
   - Click "Upload" or "Submit"
   - Wait 10-30 seconds

---

### **Step 2: Get License Info**

**Unity will give you ONE of these:**

**Option A: License File (.ulf)**
- Unity will show a download link
- Click "Download"
- Open the downloaded `.ulf` file in TextEdit
- Copy ALL contents (everything inside)
- That's your license!

**Option B: Serial Number**
- Unity will display numbers like: `XXXX-XXXX-XXXX-XXXX-XXXX-XXXX`
- Copy those numbers
- That's your serial number!

---

### **Step 3: Add to GitHub Secrets**

**Go to:** https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
(I'll open this for you)

**If you got License File (.ulf):**
1. Click "New repository secret"
2. **Name:** `UNITY_LICENSE`
3. **Secret:** Paste the entire contents of the `.ulf` file
4. Click "Add secret"

**OR If you got Serial Number:**
1. Click "New repository secret"
2. **Name:** `UNITY_SERIAL`
3. **Secret:** Paste the serial number
4. Click "Add secret"

---

### **Step 4: Test Build**

**After adding the secret:**
1. Trigger a new build (push a change or use "Run workflow")
2. Build should activate license successfully
3. Build should complete!

---

## 🎯 SUMMARY

**What to do:**
1. ✅ Upload `.alf` file to Unity website
2. ✅ Get license file or serial number
3. ✅ Add to GitHub Secrets
4. ✅ Test build

**Time:** ~5 minutes

**This should fix the license activation issue!**


