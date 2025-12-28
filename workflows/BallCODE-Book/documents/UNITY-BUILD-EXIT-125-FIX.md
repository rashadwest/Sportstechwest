# Unity Build Exit Code 125 - Fix Applied

**Date:** December 26, 2025 (1:04 AM)  
**Error:** Build failed with exit code 125  
**Issue:** License activation failing in game-ci/unity-builder

---

## 🔍 THE PROBLEM

**Error:**
- Exit code 125 (Unity license activation failure)
- Warning: "Library folder does not exist" (normal for first build)
- Build fails before Unity can start

**Root Cause:**
- `game-ci/unity-builder` needs `UNITY_EMAIL` and `UNITY_PASSWORD` in the `env` section
- Even with `UNITY_SERIAL`, it may need credentials for Personal license activation
- Missing credentials in env section causes activation to fail

---

## ✅ FIX APPLIED

**Updated workflow to include credentials in env:**

```yaml
env:
  UNITY_EMAIL: ${{ secrets.UNITY_EMAIL }}
  UNITY_PASSWORD: ${{ secrets.UNITY_PASSWORD }}
  UNITY_LICENSE: ${{ secrets.UNITY_LICENSE || '' }}
  UNITY_SERIAL: ${{ secrets.UNITY_SERIAL || '' }}
```

**Why this is needed:**
- `game-ci/unity-builder` uses credentials + serial for Personal license activation
- Credentials must be in `env` section (not just secrets)
- Serial number alone may not be sufficient

---

## 📋 WHAT WAS CHANGED

**Before:**
```yaml
env:
  UNITY_LICENSE: ${{ secrets.UNITY_LICENSE || '' }}
  UNITY_SERIAL: ${{ secrets.UNITY_SERIAL || '' }}
```

**After:**
```yaml
env:
  UNITY_EMAIL: ${{ secrets.UNITY_EMAIL }}
  UNITY_PASSWORD: ${{ secrets.UNITY_PASSWORD }}
  UNITY_LICENSE: ${{ secrets.UNITY_LICENSE || '' }}
  UNITY_SERIAL: ${{ secrets.UNITY_SERIAL || '' }}
```

**This ensures all credentials are available for license activation.**

---

## 🎯 NEXT STEPS

1. **Commit and push the fix:**
   ```bash
   cd /Users/rashadwest/BTEBallCODE
   git add .github/workflows/unity-webgl-build.yml
   git commit -m "Fix: Add UNITY_EMAIL and UNITY_PASSWORD to env for license activation"
   git push origin main
   ```

2. **Monitor the build:**
   - Check GitHub Actions for new build
   - Should succeed with all credentials in env

3. **Expected result:**
   - License activates successfully
   - Build completes
   - Deployment succeeds

---

## ✅ SUMMARY

**Problem:** Exit code 125 (license activation failure)  
**Cause:** Missing UNITY_EMAIL and UNITY_PASSWORD in env section  
**Fix:** Added credentials to env section  
**Status:** Ready to test

**The fix is applied - commit and push to test!**


