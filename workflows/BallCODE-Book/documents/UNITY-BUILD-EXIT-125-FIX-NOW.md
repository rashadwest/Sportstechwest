# Unity Build Exit Code 125 - Fix Now

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Error:** Build failed with exit code 125  
**Status:** 🔴 **CRITICAL - License Authentication Failed**

---

## 🎯 THE PROBLEM

**GitHub Actions Build Failed:**
- **Exit Code:** 125 (License activation failure)
- **Error:** Unity cannot authenticate license
- **Root Cause:** Unity Personal licenses **cannot** use email/password in CI/CD

**Why This Happens:**
- Unity Personal licenses require a **license file (.ulf)** or **serial number** for automated builds
- Email/password authentication works locally but **NOT in GitHub Actions**
- This is a Unity policy limitation, not a workflow bug

---

## ✅ THE FIX

**You need to add ONE of these to GitHub Secrets:**

### **Option 1: Unity License File (.ulf) - RECOMMENDED**

**If you have a `.ulf` file:**

1. **Get license file content:**
   ```bash
   cat ~/Library/Application\ Support/Unity/Unity_lic.ulf
   ```
   (Or check: `/Library/Application Support/Unity/Unity_lic.ulf`)

2. **Copy ENTIRE file content** (all lines)

3. **Add to GitHub Secrets:**
   - Go to: https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
   - Click "New repository secret" (or edit if exists)
   - **Name:** `UNITY_LICENSE`
   - **Value:** Paste **ENTIRE** license file content
   - Click "Add secret" or "Update secret"

---

### **Option 2: Unity Serial Number**

**If you have a serial number:**

1. **Get serial number from:**
   - Unity Hub → Settings → Licenses → Your License → Serial Number
   - OR from Unity Editor → About Unity

2. **Add to GitHub Secrets:**
   - Go to: https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
   - Click "New repository secret" (or edit if exists)
   - **Name:** `UNITY_SERIAL`
   - **Value:** Your serial number (format: `XXXX-XXXX-XXXX-XXXX-XXXX-XXXX`)
   - Click "Add secret" or "Update secret"

---

### **Option 3: Upload Activation File**

**If you have an `.alf` file:**

1. **Go to:** https://license.unity3d.com/
2. **Upload:** Your `.alf` file (e.g., `Unity_v2021.3.15f1.alf`)
3. **Wait:** 10-30 seconds
4. **Get:** Unity will give you either:
   - A `.ulf` file to download → Use Option 1
   - A serial number → Use Option 2

---

## 📋 CHECK YOUR GITHUB SECRETS

**Go to:** https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions

**Check if these exist:**
- ✅ `UNITY_EMAIL` (should exist)
- ✅ `UNITY_PASSWORD` (should exist)
- ❓ `UNITY_LICENSE` (check if it exists and has content)
- ❓ `UNITY_SERIAL` (check if it exists and has content)

**Priority:**
1. **`UNITY_LICENSE`** (full `.ulf` file content) - **BEST**
2. **`UNITY_SERIAL`** (serial number) - **GOOD**
3. `UNITY_EMAIL` + `UNITY_PASSWORD` - **NOT SUFFICIENT** (won't work alone)

---

## 🚀 AFTER ADDING SECRET

**Once you add `UNITY_LICENSE` or `UNITY_SERIAL`:**

1. **Retry the build:**
   - Go to: https://github.com/rashadwest/BTEBallCODE/actions
   - Click on the failed workflow
   - Click "Re-run jobs" → "Re-run all jobs"

2. **OR push a new commit:**
   ```bash
   cd /Users/rashadwest/BTEBallCODE
   git commit --allow-empty -m "Retry build with license"
   git push origin main
   ```

3. **Monitor:**
   - Check GitHub Actions for new build
   - Should succeed with license authentication

---

## ⚠️ IMPORTANT NOTES

**Unity Personal License Limitations:**
- ❌ **Cannot use email/password alone in CI/CD**
- ✅ **Must use license file or serial number**
- ⚠️ **This is Unity's policy, not a bug**

**Workflow Configuration:**
- ✅ Workflow is already configured correctly
- ✅ Will use `UNITY_LICENSE` if available
- ✅ Will use `UNITY_SERIAL` if available
- ✅ Will try email/password as fallback (but won't work for Personal)

---

## 📊 EXPECTED RESULT

**After adding license file or serial:**

1. ✅ License activates successfully
2. ✅ Unity build starts
3. ✅ Build completes (5-15 minutes)
4. ✅ Deploys to Netlify
5. ✅ Game goes live at ballcode.netlify.app

---

**Status:** 🔴 **ACTION REQUIRED** - Add `UNITY_LICENSE` or `UNITY_SERIAL` to GitHub Secrets

**Next:** Check GitHub Secrets and add license file or serial number

