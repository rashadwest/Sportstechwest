# Unity License File Solution - AIMCODE End-to-End

**Date:** December 26, 2025  
**Status:** 🔴 Exit Code 125 - Using Full License File Content  
**Solution:** Add full `.ulf` file content to GitHub Secrets

---

## 🎯 THE REAL SOLUTION

**Research Finding:**
- Unity Personal licenses **cannot** use email/password in CI/CD
- Serial number **may not work** for Personal licenses
- **Full license file content** is the most reliable method

**What We Have:**
- ✅ License file: `/Library/Application Support/Unity/Unity_lic.ulf`
- ✅ File size: 2,410 characters (36 lines)
- ✅ License type: Unity Personal
- ✅ Content ready to extract

---

## 📋 STEP-BY-STEP SOLUTION

### **Step 1: Extract License File Content**

**License file location:**
```
/Library/Application Support/Unity/Unity_lic.ulf
```

**Extract full content:**
```bash
cat /Library/Application\ Support/Unity/Unity_lic.ulf
```

**This is the complete license file - copy ALL of it!**

### **Step 2: Add to GitHub Secrets**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
   (I opened this for you)

2. **Edit or Add `UNITY_LICENSE`:**
   - If exists: Click edit (pencil icon)
   - If not: Click "New repository secret"
   - Name: `UNITY_LICENSE`
   - Value: Paste **ENTIRE** license file content (all 36 lines)
   - Click: "Update secret" or "Add secret"

3. **Keep other secrets:**
   - `UNITY_EMAIL` (keep)
   - `UNITY_PASSWORD` (keep)
   - `UNITY_SERIAL` (keep as backup)

### **Step 3: Verify Workflow**

**Workflow should have:**
```yaml
env:
  UNITY_EMAIL: ${{ secrets.UNITY_EMAIL }}
  UNITY_PASSWORD: ${{ secrets.UNITY_PASSWORD }}
  UNITY_LICENSE: ${{ secrets.UNITY_LICENSE }}
  UNITY_SERIAL: ${{ secrets.UNITY_SERIAL || '' }}
```

**Priority:**
1. `UNITY_LICENSE` (full file) - Primary method
2. `UNITY_SERIAL` - Fallback
3. `UNITY_EMAIL` + `UNITY_PASSWORD` - May be needed

### **Step 4: Test Build**

**After adding license file:**
1. Trigger GitHub Actions build
2. Should activate license successfully
3. Build should complete
4. Deployment should succeed

---

## ✅ WHY THIS WILL WORK

**From Research:**
- Unity Personal licenses require license file for CI/CD
- game-ci/unity-builder prefers `UNITY_LICENSE` (full file)
- Serial numbers work for Pro/Enterprise, may not for Personal
- Full license file = Most reliable method

**What We're Doing:**
- Using full license file content (not just serial)
- Adding to GitHub Secrets as `UNITY_LICENSE`
- Workflow already configured to use it
- This is the research-backed solution

---

## 📋 QUICK COPY COMMAND

**To copy license file content:**
```bash
cat /Library/Application\ Support/Unity/Unity_lic.ulf | pbcopy
```

**Then paste into GitHub Secrets → UNITY_LICENSE**

---

## ✅ SUMMARY

**Problem:** Exit code 125 (license activation failure)  
**Root Cause:** Unity Personal licenses need full license file for CI/CD  
**Solution:** Add full `.ulf` file content to GitHub Secrets as `UNITY_LICENSE`  
**Status:** Ready to implement

**This is the AIMCODE research-based solution that should work!**


