# Unity Build Quick Response Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Purpose:** Quick reference for responding to Unity build errors  
**Use When:** Build fails - follow this guide immediately

---

## 🚨 QUICK ERROR IDENTIFICATION

### **Error Type 1: Syntax Error (0-5 seconds)**

**Symptoms:**
- "Invalid workflow file"
- "Unrecognized named-value"
- "repository not found"
- Build fails immediately

**Quick Fix:**
1. Run: `./scripts/validate-unity-workflow.sh`
2. Check: Workflow file syntax
3. Fix: Errors reported by script
4. Commit: Fixed workflow
5. Retry: Build automatically triggers

**Prevention:**
- ✅ Run validation script before commit
- ✅ Check action existence
- ✅ Verify no duplicate parameters

---

### **Error Type 2: License Error (Exit Code 125)**

**Symptoms:**
- Exit code 125
- "License activation failed"
- Build fails in 1-5 minutes

**Quick Fix:**
1. Check: `UNITY_LICENSE` secret exists
   - Go to: https://github.com/rashadwest/BTEBallCODE/settings/secrets/actions
2. Verify: Format is base64 (starts with `PD94bWwg...`)
3. Test: Base64 decoding works
4. Update: Secret if needed
5. Retry: Build

**Prevention:**
- ✅ Pre-flight validation checks format
- ✅ License activation step verifies creation
- ✅ Automatic diagnostics report issues

---

### **Error Type 3: Build Error (Exit Code 1)**

**Symptoms:**
- Exit code 1
- "Build failed"
- Build runs 5-15 minutes before failing

**Quick Fix:**
1. Check: Build logs for specific error
2. Identify: Compilation error, missing asset, or version mismatch
3. Fix: Error in Unity project
4. Commit: Fixed code
5. Retry: Build

**Prevention:**
- ✅ Local build test before push
- ✅ Compilation check in workflow
- ✅ Project structure validation

---

## 🔄 AUTOMATED RESPONSE TRIGGERS

### **Trigger 1: Pre-Flight Validation**

**When:** Before every build
**Action:** Validates workflow, secrets, structure
**Result:** Prevents errors before they occur

**Manual Trigger:**
```bash
./scripts/validate-unity-workflow.sh
```

---

### **Trigger 2: Error Diagnostics**

**When:** Build fails
**Action:** Automatically diagnoses error type
**Result:** Specific fix suggestions

**Manual Trigger:**
- Check build logs
- Review diagnostic report in workflow summary
- Follow suggested fixes

---

### **Trigger 3: Auto-Retry**

**When:** Transient errors (network, temporary)
**Action:** Automatic retry with backoff
**Result:** Self-healing for temporary issues

**Manual Trigger:**
- Click "Re-run jobs" in GitHub Actions
- Or push empty commit to retry

---

## 📋 RESPONSE CHECKLIST

### **When Build Fails:**

1. **Identify Error Type:**
   - [ ] Check exit code
   - [ ] Check build duration
   - [ ] Review error message

2. **Follow Quick Fix:**
   - [ ] Syntax error → Run validation script
   - [ ] License error → Check secret format
   - [ ] Build error → Check logs

3. **Apply Fix:**
   - [ ] Fix identified issue
   - [ ] Commit changes
   - [ ] Monitor new build

4. **Verify Success:**
   - [ ] Check build completes
   - [ ] Verify deployment
   - [ ] Test game accessibility

---

## 🎯 PREVENTION CHECKLIST

### **Before Every Commit:**

- [ ] Run `./scripts/validate-unity-workflow.sh`
- [ ] Verify secrets are set correctly
- [ ] Test workflow syntax
- [ ] Check for duplicate parameters

### **Before Every Build:**

- [ ] Verify `UNITY_LICENSE` secret format
- [ ] Check project structure
- [ ] Confirm Unity version matches
- [ ] Review recent changes

---

## 📚 REFERENCE DOCUMENTS

**Complete Documentation:**
- `AIMCODE-UNITY-BUILD-END-TO-END-INVESTIGATION.md` - Full investigation
- `UNITY-BUILD-ERROR-CHAIN-ANALYSIS.md` - Error chain breakdown
- `UNITY-BUILD-PREVENTION-SYSTEM.md` - Prevention strategies
- `UNITY-BUILD-AUTO-RESPONSE-SYSTEM.md` - Automated responses
- `UNITY-BUILD-MONITORING-SYSTEM.md` - Monitoring setup

**Quick References:**
- This document (quick response)
- Validation script: `scripts/validate-unity-workflow.sh`

---

**Status:** ✅ **QUICK RESPONSE GUIDE READY** - Use when build fails

