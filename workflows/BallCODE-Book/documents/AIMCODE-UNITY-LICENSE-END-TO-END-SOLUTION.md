# AIMCODE: Unity License End-to-End Solution

**Date:** December 26, 2025 (1:04 AM)  
**Methodology:** AIMCODE (CLEAR → Alpha Evolve → Research → Experts → Implementation)  
**Status:** 🔴 Critical - Exit Code 125 (License Activation Failure)

---

## 🎯 CLEAR FRAMEWORK

### **Clarity:**
- **Problem:** Exit code 125 - Unity license activation failing in GitHub Actions
- **Current State:** All secrets configured (UNITY_EMAIL, UNITY_PASSWORD, UNITY_SERIAL)
- **Root Cause:** Unity Personal licenses cannot use email/password in CI/CD (Unity policy)
- **Required:** Full license file content (`.ulf`) OR working serial activation method

### **Logic:**
- Unity Personal = Individual use only
- CI/CD = Automated builds (not individual use)
- Unity policy: Personal licenses need license file for CI/CD
- game-ci/unity-builder may need full `.ulf` file content, not just serial

### **Examples:**
- Exit code 125 = License activation failure
- "Library folder does not exist" = Normal warning (first build)
- Build fails before Unity starts = License issue

### **Adaptation:**
- Try full license file content instead of serial
- Research game-ci/unity-builder actual requirements
- Test different activation methods
- Find working solution through systematic testing

### **Results:**
- ✅ License activates successfully
- ✅ Build completes
- ✅ Deployment succeeds
- ✅ End-to-end test passes

---

## 🔬 ALPHA EVELVE (Systematic Deep Learning)

### **Layer 1: Understanding Exit Code 125**
- Exit code 125 = Unity license activation failure
- Happens before Unity Editor starts
- Indicates credentials/license not accepted

### **Layer 2: Unity Personal License Limitations**
- Personal licenses = Individual use only
- CI/CD = Automated (not individual)
- Unity policy: Requires license file for CI/CD
- Email/password = Interactive (doesn't work in CI/CD)

### **Layer 3: game-ci/unity-builder Requirements**
- Needs: License file content OR serial + credentials
- Personal licenses: May need full `.ulf` file content
- Serial alone may not work for Personal licenses

### **Layer 4: Solution Architecture**
- Extract full license file content
- Add to GitHub Secrets as `UNITY_LICENSE`
- Remove serial (use license file instead)
- Test end-to-end

---

## 📚 RESEARCH FINDINGS

**From Unity Documentation:**
- Unity Personal licenses cannot be activated with email/password in CI/CD
- Manual activation no longer supported for Personal licenses
- Requires license file (`.ulf`) for automated builds

**From game-ci Documentation:**
- `UNITY_LICENSE` = Full license file content (base64 or raw)
- `UNITY_SERIAL` = Serial number (may not work for Personal)
- Personal licenses may need full license file

**Key Insight:**
- We have serial number but may need full license file content
- License file at: `/Library/Application Support/Unity/Unity_lic.ulf`
- Need to extract full content and add to GitHub Secrets

---

## 👥 EXPERT CONSULTATION

**Unity Best Practices:**
- Personal licenses: Use full license file content for CI/CD
- Serial numbers: Work for Pro/Enterprise, may not work for Personal
- License file: Most reliable method for Personal licenses

**game-ci/unity-builder:**
- Prefers `UNITY_LICENSE` (full file content) over serial
- Can use serial but may fail for Personal licenses
- License file content = Most reliable

---

## ✅ IMPLEMENTATION: End-to-End Solution

### **Step 1: Extract Full License File Content**

**We have the license file at:**
- `/Library/Application Support/Unity/Unity_lic.ulf`

**Extract full content:**
```bash
cat /Library/Application\ Support/Unity/Unity_lic.ulf
```

**This is what we need to add to GitHub Secrets as `UNITY_LICENSE`**

### **Step 2: Update GitHub Secrets**

**Remove/Update:**
- Keep `UNITY_EMAIL` and `UNITY_PASSWORD` (may still be needed)
- Add/Update `UNITY_LICENSE` with full license file content
- Keep `UNITY_SERIAL` as backup (but use license file primarily)

### **Step 3: Update Workflow**

**Ensure workflow uses license file:**
```yaml
env:
  UNITY_EMAIL: ${{ secrets.UNITY_EMAIL }}
  UNITY_PASSWORD: ${{ secrets.UNITY_PASSWORD }}
  UNITY_LICENSE: ${{ secrets.UNITY_LICENSE }}
  UNITY_SERIAL: ${{ secrets.UNITY_SERIAL || '' }}
```

**Priority:**
1. `UNITY_LICENSE` (full file content) - Primary
2. `UNITY_SERIAL` - Fallback
3. `UNITY_EMAIL` + `UNITY_PASSWORD` - May be needed

### **Step 4: End-to-End Test**

**Create test script to verify:**
- License file extraction
- GitHub Secrets configuration
- Workflow configuration
- Build success

---

## 🎯 ACTION PLAN

1. **Extract license file content** (automated)
2. **Add to GitHub Secrets** (manual - one time)
3. **Update workflow** (if needed)
4. **Test build** (automated)
5. **Verify end-to-end** (automated)

---

## ✅ EXPECTED RESULT

**After applying solution:**
- ✅ License activates successfully
- ✅ Build completes
- ✅ Deployment succeeds
- ✅ End-to-end test passes

**This is the systematic, research-based solution using AIMCODE methodology.**


