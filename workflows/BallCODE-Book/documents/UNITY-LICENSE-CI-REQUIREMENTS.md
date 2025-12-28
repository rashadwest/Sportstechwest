# Unity License Requirements for CI/CD (GitHub Actions)

**Date:** December 24, 2025  
**Important:** CI/CD License Requirements

---

## ⚠️ IMPORTANT: CI/CD LICENSE REQUIREMENTS

**According to Unity's documentation:**
- ❌ **Unity Personal license manual activation is NOT supported in CI/CD environments**
- ✅ **Unity Pro subscription is required for automated builds (CI/CD)**

**However, there may be workarounds or exceptions.**

---

## 🎯 YOUR OPTIONS

### **Option 1: Try Personal License First (May Work)**

**Some CI/CD setups can use Personal license:**
1. Upload activation file to Unity website
2. Get license file
3. Add to GitHub Secrets as `UNITY_LICENSE`
4. Try the build - it might work!

**Why it might work:**
- Some GitHub Actions workflows can use Personal license
- Unity's restrictions may not apply to all CI/CD setups
- Worth trying first!

---

### **Option 2: Use Unity Pro (If Option 1 Fails)**

**If Personal license doesn't work:**
- Unity Pro subscription required for CI/CD
- Cost: ~$2,040/year (or monthly subscription)
- Required for automated builds in CI/CD environments

**Unity's Official Policy:**
- Personal license: For individual use, not CI/CD
- Pro license: Required for automated builds/CI/CD

---

## 🔍 CHECK YOUR GITHUB ACTIONS WORKFLOW

**Let me check your workflow configuration:**

Your workflow uses `game-ci/unity-builder@v4` which may have specific license requirements.

**Common configurations:**
- `UNITY_LICENSE` - Full license file
- `UNITY_SERIAL` - Serial number
- `UNITY_EMAIL` + `UNITY_PASSWORD` - Unity account credentials

---

## 🎯 RECOMMENDED APPROACH

### **Step 1: Try Personal License First**

1. **Upload activation file:**
   - Go to: https://license.unity3d.com/
   - Upload: `Unity_v2021.3.10f1.alf`
   - Get license file

2. **Add to GitHub:**
   - Add as `UNITY_LICENSE` secret
   - Trigger build
   - See if it works!

3. **If it works:** ✅ You're done! Personal license is sufficient!

4. **If it fails:** ⚠️ You may need Unity Pro

---

### **Step 2: If Personal License Doesn't Work**

**Options:**
1. **Get Unity Pro subscription:**
   - Required for official CI/CD support
   - Cost: ~$2,040/year

2. **Use alternative build method:**
   - Build locally and upload
   - Use different CI/CD service
   - Manual builds

3. **Check for exceptions:**
   - Some workflows may work with Personal license
   - Depends on Unity version and workflow configuration

---

## 📊 LICENSE COMPARISON FOR CI/CD

| License Type | CI/CD Support | Cost |
|-------------|---------------|------|
| **Personal** | ❌ Not officially supported | Free |
| **Pro** | ✅ Officially supported | ~$2,040/year |
| **Plus** | ✅ Supported | Paid |
| **Enterprise** | ✅ Supported | Paid |

**Unity's Policy:** Personal license is for individual use, not automated builds.

---

## 🎯 NEXT STEPS

### **Try Personal License First:**

1. **Upload activation file** (you're doing this now)
2. **Get license file** from Unity website
3. **Add to GitHub Secrets** as `UNITY_LICENSE`
4. **Trigger build** and see if it works
5. **If it works:** ✅ Great! You're done!
6. **If it fails:** ⚠️ You'll need Unity Pro

---

## 💡 ALTERNATIVE: Local Builds

**If Personal license doesn't work and you don't want Pro:**

1. **Build locally:**
   - Build WebGL in Unity Editor
   - Upload build to Netlify manually
   - Or use n8n to trigger local builds

2. **Use different CI/CD:**
   - Some services may have different requirements
   - Or build on your own server

---

## ✅ SUMMARY

**Question:** Do I need Unity Pro for GitHub Actions?  
**Answer:** 
- **Officially:** Yes, Unity Pro is required for CI/CD
- **Practically:** Try Personal license first - it might work!
- **If it doesn't work:** Unity Pro subscription needed

**Recommendation:** Try Personal license first, then upgrade to Pro if needed.

---

**Continue with uploading the activation file - we'll see if Personal license works for your setup!**


