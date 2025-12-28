# Unity Build Failure - Exit Code 125 Diagnosis

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Error:** Build failed with exit code 125  
**Workflow:** unity-webgl-build.yml

---

## 🎯 THE ERROR

**GitHub Actions Build Failed:**
- **Exit Code:** 125
- **Status:** Failure
- **Duration:** 3m 27s
- **Warning:** Library folder doesn't exist (caching - not critical)

**Exit Code 125 typically means:**
- Unity license authentication failed
- Unity setup/installation issue
- Project structure problem
- Missing Unity credentials

---

## 🔍 COMMON CAUSES & FIXES

### **Cause 1: Unity License Not Configured** ⚠️ MOST LIKELY

**Problem:** Unity builder can't authenticate without license.

**Check:**
1. **Go to:** https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
2. **Check for:**
   - `UNITY_EMAIL` - Your Unity account email
   - `UNITY_PASSWORD` - Your Unity account password
   - `UNITY_LICENSE` - Unity license file (if using personal license)

**Fix:**
- Add missing secrets
- OR use Unity Cloud Build (different approach)

---

### **Cause 2: Unity Version Mismatch**

**Problem:** Workflow uses different Unity version than project.

**Check workflow file:**
- What Unity version is specified?
- Does it match your project's Unity version?

**Fix:**
- Update workflow to match project Unity version
- OR update project to match workflow version

---

### **Cause 3: Project Structure Issue**

**Problem:** Unity builder can't find project files.

**Check:**
- Does repository have `Assets/` folder?
- Does repository have `ProjectSettings/` folder?
- Is project structure correct?

**Fix:**
- Ensure Unity project files are in repository root
- Verify project structure is correct

---

## ✅ DIAGNOSTIC STEPS

### **Step 1: Check GitHub Secrets**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
2. **Check for:**
   - `UNITY_EMAIL` ✅ or ❌
   - `UNITY_PASSWORD` ✅ or ❌
   - `UNITY_LICENSE` ✅ or ❌ (optional if using email/password)

**If missing:**
- Add the secrets
- Retry build

---

### **Step 2: Check Workflow File**

**Check Unity version in workflow:**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/blob/main/.github/workflows/unity-webgl-build.yml
2. **Look for:** `unityVersion:` or `unity-version:`
3. **Check:** Does it match your project's Unity version?

**If mismatch:**
- Update workflow to match project
- OR update project to match workflow

---

### **Step 3: Check Build Logs**

**Get detailed error from logs:**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/actions
2. **Click:** Failed workflow run
3. **Click:** "build" job
4. **Scroll to:** Error messages
5. **Look for:** Specific Unity error

**Common errors:**
- "License activation failed"
- "Unity not found"
- "Project structure invalid"
- "Missing dependencies"

---

## 🚀 QUICK FIXES

### **Fix 1: Add Unity Credentials (If Missing)**

**If secrets are missing:**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
2. **Click:** "New repository secret"
3. **Add:**
   - **Name:** `UNITY_EMAIL`
   - **Value:** Your Unity account email
4. **Add:**
   - **Name:** `UNITY_PASSWORD`
   - **Value:** Your Unity account password
5. **Save**
6. **Retry build**

---

### **Fix 2: Check Unity Version**

**Verify Unity version matches:**

1. **Check project Unity version:**
   - Open Unity project
   - Check: `ProjectSettings/ProjectVersion.txt`
   - Note the version (e.g., `2021.3.15f1`)

2. **Check workflow Unity version:**
   - Go to: `.github/workflows/unity-webgl-build.yml`
   - Look for: `unityVersion: 2021.3.15f1` (or similar)

3. **If mismatch:**
   - Update workflow to match project version
   - Commit and push

---

### **Fix 3: Use Unity Personal License (Alternative)**

**If you have Unity Personal license:**

1. **Generate license file:**
   - Open Unity Editor locally
   - Help → Manage License
   - Export license file

2. **Add to GitHub Secrets:**
   - Name: `UNITY_LICENSE`
   - Value: Contents of license file

3. **Update workflow:**
   - Use `UNITY_LICENSE` instead of email/password

---

## 📋 IMMEDIATE ACTION

**Check GitHub Secrets First:**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
2. **Check:** Do `UNITY_EMAIL` and `UNITY_PASSWORD` exist?
3. **If missing:** Add them
4. **If exist:** Check if they're correct
5. **Retry build**

**Then check build logs:**
1. **Go to:** https://github.com/rashadwest/BTEBallCODE/actions
2. **Click:** Failed workflow
3. **Click:** "build" job
4. **Read:** Error messages in logs

---

**Status:** 🔍 **DIAGNOSING** - Check GitHub Secrets and build logs

**Next:** Check Unity credentials in GitHub Secrets

