# Get Unity License for GitHub Actions

**Date:** December 24, 2025  
**Status:** ✅ License activated locally  
**Next Step:** Get license file/serial for GitHub Actions

---

## ✅ WHAT JUST HAPPENED

Your Unity license is now activated on your Mac! This means:
- ✅ Unity Editor can run on your computer
- ✅ You can build locally
- ✅ Unity Hub shows your license

---

## 🎯 NEXT STEP: GitHub Actions Needs License Too

**GitHub Actions runs on GitHub's servers** (not your Mac), so it needs its own license.

**You have 2 options:**

---

## OPTION 1: Get License File (Recommended)

### Step 1: Find Your License File

**I'm checking for it now...** (running command)

**If found, it will be at:**
```
~/Library/Application Support/Unity/Unity_lic.ulf
```

### Step 2: Get the Contents

**If the file exists:**
```bash
cat ~/Library/Application\ Support/Unity/Unity_lic.ulf
```

**Copy everything inside that file.**

### Step 3: Add to GitHub Secrets

1. Go to: https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
2. Click "New repository secret"
3. **Name:** `UNITY_LICENSE`
4. **Secret:** Paste the entire contents of the `.ulf` file
5. Click "Add secret"

---

## OPTION 2: Get Serial Number

### Step 1: Check Unity Hub

1. Open Unity Hub
2. Go to **Licenses** (left sidebar)
3. Click on your license
4. Look for **Serial Number** or **License Key**
5. Copy it (looks like: `SB-XXXX-XXXX-XXXX-XXXX-XXXX`)

### Step 2: Add to GitHub Secrets

1. Go to: https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
2. Click "New repository secret"
3. **Name:** `UNITY_SERIAL`
4. **Secret:** Paste the serial number
5. Click "Add secret"

---

## 🔍 CHECKING FOR LICENSE FILE NOW...

**I'm searching for your license file...**

If found, I'll show you how to get it.
If not found, we'll use Option 2 (Serial Number).

---

## ✅ AFTER YOU ADD THE SECRET

1. **Trigger a build** (push to main or manual trigger)
2. **Check if it works** - build should succeed!
3. **Done!** 🎉

---

## 📋 SUMMARY

**What you did:**
- ✅ Activated Unity license locally
- ✅ Script worked perfectly!

**What's next:**
- 🔍 Find license file or serial number
- 📝 Add to GitHub Secrets
- 🚀 Test the build!


