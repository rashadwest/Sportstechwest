# Where is the Actual License Number?

**Date:** December 26, 2025  
**Question:** Where is the license number/serial in the license file?

---

## 🔍 THE LICENSE NUMBER IS IN THE FILE

**Location in license file:**
- **Line 22:** `<SerialMasked Value="F4-UBEE-VV7Z-SSXU-DYHH-XXXX"/>`
- **Line 21:** `<DeveloperData Value="AQAAAEY0LVVCRUUtVlY3Wi1TU1hVLURZSEgtWDdCTQ=="/>`

**The full serial number is encoded in DeveloperData!**

---

## 📋 EXTRACTING THE SERIAL NUMBER

### **Method 1: From DeveloperData (Full Serial)**

**The DeveloperData field contains the full serial number (base64 encoded):**

```bash
# Extract and decode
cat /Library/Application\ Support/Unity/Unity_lic.ulf | \
  grep "DeveloperData" | \
  sed 's/.*Value="\([^"]*\)".*/\1/' | \
  base64 -d
```

**Result:** `F4-UBEE-VV7Z-SSXU-DYHH-X7BM`

**This is your FULL serial number!**

### **Method 2: From SerialMasked (Masked)**

**The SerialMasked field shows:**
- `F4-UBEE-VV7Z-SSXU-DYHH-XXXX` (last 4 digits hidden)

**This is NOT the full serial - it's masked!**

---

## ✅ WHAT YOU NEED FOR CI/CD

**For GitHub Actions, you have TWO options:**

### **Option 1: Use Full License File (Recommended)**

**What to use:**
- **Full license file content** (all 36 lines)
- **Location:** `/Library/Application Support/Unity/Unity_lic.ulf`
- **Add to GitHub Secrets as:** `UNITY_LICENSE`
- **This is the MOST RELIABLE method!**

**Why this is better:**
- Contains all license information
- Works for Unity Personal licenses
- Most reliable for CI/CD

### **Option 2: Use Serial Number**

**What to use:**
- **Serial number:** `F4-UBEE-VV7Z-SSXU-DYHH-X7BM`
- **Add to GitHub Secrets as:** `UNITY_SERIAL`
- **May work, but less reliable for Personal licenses**

**Why this might not work:**
- Personal licenses may need full file
- Serial alone may not activate in CI/CD

---

## 🎯 RECOMMENDED: Use Full License File

**For Unity Personal licenses in CI/CD:**
- ✅ **Use full license file content** (Option 1)
- ⚠️ Serial number may not work (Option 2)

**The full license file is at:**
```
/Library/Application Support/Unity/Unity_lic.ulf
```

**Copy the ENTIRE file content and add to GitHub Secrets → UNITY_LICENSE**

---

## 📋 QUICK REFERENCE

**Serial Number (if you need it):**
- **Full:** `F4-UBEE-VV7Z-SSXU-DYHH-X7BM`
- **Masked:** `F4-UBEE-VV7Z-SSXU-DYHH-XXXX`

**License File:**
- **Location:** `/Library/Application Support/Unity/Unity_lic.ulf`
- **Size:** 2,410 characters (36 lines)
- **Use:** Full content for `UNITY_LICENSE` secret

---

## ✅ SUMMARY

**License Number Location:**
- ✅ **Serial Number:** `F4-UBEE-VV7Z-SSXU-DYHH-X7BM` (from DeveloperData)
- ✅ **License File:** `/Library/Application Support/Unity/Unity_lic.ulf` (full content)

**For CI/CD:**
- ✅ **Use full license file content** (most reliable)
- ⚠️ Serial number may not work for Personal licenses

**I've already copied the full license file content to your clipboard - paste it into GitHub Secrets → UNITY_LICENSE!**


