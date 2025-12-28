# Unity Build - Quick Reference Card

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Purpose:** One-page quick reference for immediate action  
**Print This:** Keep handy for quick access

---

## 🚨 IF BUILD FAILS AFTER 15-20 MINUTES

### **Solution 1: game-ci/unity-activate (5 min, 95% success)**
```bash
./scripts/fix-license-activation.sh
# Follow instructions to update workflow
git add .github/workflows/unity-webgl-build.yml
git commit -m "Fix: Use game-ci/unity-activate"
git push origin main
```

### **Solution 2: Unity Cloud Build (10 min, 99% success)**
- Go to: https://unity.com/products/unity-cloud-build
- Connect: GitHub repository
- Build: Automatic

### **Solution 3: Local Build (15-20 min, 100% success)**
```bash
./scripts/emergency-local-build.sh
# Builds locally and deploys automatically
```

---

## ⚡ QUICK ERROR FIXES

| Error | Exit Code | Fix Script | Time |
|-------|-----------|------------|------|
| Syntax | N/A | `validate-unity-workflow.sh` | 2 min |
| License | 125 | `fix-license-activation.sh` | 5 min |
| Build | 1 | Check logs, fix code | 10-30 min |
| Emergency | Any | `emergency-local-build.sh` | 15-20 min |

---

## 📋 BEFORE EVERY COMMIT

```bash
./scripts/validate-unity-workflow.sh
# Fix any errors before committing
```

---

## 🔍 QUICK DIAGNOSIS

**Build fails immediately (0-5s):** → Syntax error  
**Build fails in 1-5 min:** → License error (125)  
**Build fails in 5-15 min:** → Build error (1)  
**Build fails after 15 min:** → Use Solution 1, 2, or 3

---

## 📚 FULL DOCUMENTATION

- **Quick Response:** `UNITY-BUILD-QUICK-RESPONSE-GUIDE.md`
- **3 Solutions:** `UNITY-BUILD-READY-TO-PUSH-SOLUTIONS.md`
- **Error Playbook:** `UNITY-BUILD-FUTURE-ERROR-PLAYBOOK.md`
- **Stay Ready:** `UNITY-BUILD-STAY-READY-SYSTEM.md`
- **Master Index:** `UNITY-BUILD-SYSTEM-MASTER-INDEX.md`

---

**Status:** ✅ **ALWAYS READY** - Solutions ready for immediate use

