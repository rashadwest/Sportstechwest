# Unity Personal License for GitHub Actions

**Date:** December 24, 2025  
**License Type:** Unity Personal (Free)  
**Status:** ✅ Activated locally  
**Next:** Set up for GitHub Actions

---

## 🎯 THE SITUATION

**Unity Personal licenses work differently:**
- ✅ You activated it locally (done!)
- ⚠️ GitHub Actions needs to activate its own license
- ✅ `game-ci/unity-builder` can use email/password OR license file

---

## ✅ SOLUTION: Use Email + Password (Easiest!)

**Your workflow already has `UNITY_EMAIL` and `UNITY_PASSWORD` secrets!**

**Just need to add them to the workflow properly.**

---

## 📋 WHAT TO DO

### Step 1: Check GitHub Secrets

**Go to:** https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions

**You need these secrets:**
- ✅ `UNITY_EMAIL` (your Unity account email)
- ✅ `UNITY_PASSWORD` (your Unity account password)
- ⏳ `UNITY_LICENSE` (optional - only if you have a license file)

---

### Step 2: Add Secrets (If Missing)

**If `UNITY_EMAIL` or `UNITY_PASSWORD` are missing:**

1. Click **"New repository secret"**
2. **Name:** `UNITY_EMAIL`
3. **Secret:** Your Unity email (rashadlwest@gmail.com)
4. Click **"Add secret"**

5. Click **"New repository secret"** again
6. **Name:** `UNITY_PASSWORD`
7. **Secret:** Your Unity password
8. Click **"Add secret"**

---

### Step 3: Update Workflow (If Needed)

**The workflow should use email/password for activation.**

**Current workflow has:**
```yaml
env:
  UNITY_LICENSE: ${{ secrets.UNITY_LICENSE || '' }}
```

**It should also have:**
```yaml
env:
  UNITY_EMAIL: ${{ secrets.UNITY_EMAIL }}
  UNITY_PASSWORD: ${{ secrets.UNITY_PASSWORD }}
  UNITY_LICENSE: ${{ secrets.UNITY_LICENSE || '' }}
```

**The `game-ci/unity-builder` action will:**
- Try to use `UNITY_LICENSE` if provided
- If not, use `UNITY_EMAIL` + `UNITY_PASSWORD` to activate
- This works for Unity Personal!

---

## 🎯 NEXT STEPS

1. **Check GitHub Secrets** - Make sure `UNITY_EMAIL` and `UNITY_PASSWORD` are there
2. **Update workflow** (if needed) - Add email/password to env
3. **Test build** - Push or trigger manually
4. **Done!** 🎉

---

## ✅ SUMMARY

**What you did:**
- ✅ Activated Unity license locally
- ✅ Script worked!

**What's next:**
- 📝 Add `UNITY_EMAIL` and `UNITY_PASSWORD` to GitHub Secrets (if not there)
- 🔧 Update workflow to use email/password (if needed)
- 🚀 Test the build!

**For Unity Personal, email/password authentication works!**


