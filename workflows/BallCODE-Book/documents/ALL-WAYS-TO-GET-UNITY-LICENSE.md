# All Ways to Get Unity License for CI/CD

**Date:** December 24, 2025  
**Goal:** Get license file or serial number

---

## 🔍 WHAT I FOUND

**On your Mac:**
- ✅ Unity is activated (Personal license)
- ✅ Found entitlement license file (not usable for CI/CD)
- ⚠️ No `.ulf` file found (Personal licenses don't create them)
- ⚠️ Serial number partially visible: `F4-UBEE-VV7Z-SSXU-DYHH-XXXX` (last part masked)

---

## ✅ WAYS TO GET LICENSE

### **METHOD 1: Upload Activation File (Recommended - 5 minutes)**

**This is the ONLY reliable way for Personal licenses:**

1. **Go to:** https://license.unity3d.com/
2. **Upload:** `Unity_v2021.3.10f1.alf`
3. **Get:** License file (.ulf) OR Serial number
4. **Add:** To GitHub Secrets
5. **Done!**

**Why this works:**
- Unity processes the activation file
- Gives you a license file or serial
- Works for Personal licenses
- Takes 5 minutes

---

### **METHOD 2: Check Unity Hub for Serial**

**I opened Unity Hub for you:**

1. **In Unity Hub:**
   - Click **Settings** (gear icon, top right)
   - Click **Licenses** (left sidebar)
   - Click on your license
   - **Look for:** Serial Number

2. **If serial is visible:**
   - Copy it
   - Add to GitHub Secrets as `UNITY_SERIAL`
   - Done!

**Note:** Personal licenses might not show serial numbers in Unity Hub.

---

### **METHOD 3: Use Entitlement License (May Not Work)**

**I found:** `UnityEntitlementLicense.xml`

**This is Unity's new license format, but:**
- ⚠️ `game-ci/unity-builder` might not support it
- ⚠️ It's designed for Unity Hub, not CI/CD
- ⚠️ May not work in GitHub Actions

**If you want to try:**
1. Copy entire contents of `UnityEntitlementLicense.xml`
2. Add to GitHub Secrets as `UNITY_LICENSE`
3. Test build
4. **Likely won't work, but worth trying!**

---

### **METHOD 4: Extract Serial from Logs**

**I found partial serial:** `F4-UBEE-VV7Z-SSXU-DYHH-XXXX`

**The last part is masked. To get full serial:**
1. Check Unity Hub (Method 2)
2. OR Upload activation file (Method 1)
3. OR Check Unity Editor → About Unity

---

## 🎯 RECOMMENDED: Method 1

**Upload the activation file. It's:**
- ✅ Fastest (5 minutes)
- ✅ Most reliable
- ✅ Works for Personal licenses
- ✅ Guaranteed to work

---

## 📋 QUICK CHECKLIST

**Try these in order:**

1. [ ] **Check Unity Hub** (I opened it) → Settings → Licenses → Look for serial
2. [ ] **If no serial:** Upload `.alf` file to Unity website
3. [ ] **Get license file or serial** from Unity
4. [ ] **Add to GitHub Secrets**
5. [ ] **Test build**

---

## ✅ SUMMARY

**What I Found:**
- ✅ Unity is activated locally
- ✅ Entitlement license exists (may not work for CI/CD)
- ⚠️ No `.ulf` file (Personal licenses don't create them)
- ⚠️ Serial partially visible (last part masked)

**Best Solution:**
- 📝 Upload activation file → Get license/serial → Add to GitHub

**I opened Unity Hub for you - check if serial is visible there!**


