# Netlify Extensions Authentication Error - Fix Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Error:** "Failed retrieving extensions for site" - Authentication issue

---

## 🎯 THE ERROR

**Error Message:**
```
Failed during stage 'Reading and parsing configuration files': 
Failed retrieving extensions for site 39ebfb47-c716-4f38-8f8b-7bfba36f3dc7: 
fetch failed. Double-check your login status with 'netlify status' or contact support.
```

**What This Means:**
- Netlify is trying to fetch extensions/plugins for your site
- Authentication/authorization is failing
- This is blocking the deployment

---

## ✅ QUICK FIXES (Try in Order)

### **Fix 1: Check Netlify Extensions (Most Likely)** ⭐

**Problem:** Site might have extensions configured that are causing issues.

**Steps:**
1. **Go to:** https://app.netlify.com
2. **Select site:** ballcode
3. **Go to:** Site Settings → **Extensions**
4. **Check:** Are there any extensions installed?
5. **If yes:**
   - Try disabling them temporarily
   - OR remove extensions that aren't needed
   - Retry deployment

**Common Extensions:**
- Build plugins
- Analytics extensions
- Form handlers
- Other third-party extensions

---

### **Fix 2: Check Site Configuration File**

**Problem:** `netlify.toml` or `netlify.yaml` might have extension references.

**Check for configuration file:**
```bash
# In your game repository
cd /path/to/BTEBallCODE
ls -la | grep netlify
```

**If `netlify.toml` exists:**
- Check for `[plugins]` or `[[plugins]]` sections
- Comment them out temporarily
- Retry deployment

**Example of what to look for:**
```toml
[plugins]
  package = "@netlify/plugin-name"
```

**Fix:** Comment out or remove plugin sections if not needed.

---

### **Fix 3: Re-authenticate Netlify CLI (If Using CLI)**

**If you're using Netlify CLI for builds:**

```bash
# Check Netlify status
netlify status

# If not logged in, login
netlify login

# Link to site
netlify link
```

**But this is likely not the issue** since you're using GitHub integration.

---

### **Fix 4: Check Build Settings**

**Problem:** Build settings might reference extensions that don't exist.

**Steps:**
1. **Go to:** Netlify Dashboard → ballcode → Site Settings
2. **Go to:** Build & deploy → Build settings
3. **Check:**
   - Build command (should be empty for Unity game)
   - Publish directory (should be `Builds/WebGL`)
   - Are there any plugin/extension references?

**Fix:** Clear any extension/plugin references in build settings.

---

### **Fix 5: Disable Extensions Temporarily**

**Quick test to see if extensions are the problem:**

1. **Go to:** Netlify Dashboard → ballcode → Site Settings
2. **Go to:** Extensions
3. **Disable all extensions** (if any)
4. **Retry deployment**
5. **If it works:** Extensions were the problem
6. **Re-enable one by one** to find the culprit

---

## 🚀 RECOMMENDED ACTION

**Start with Fix 1 (Check Extensions):**

1. **Go to:** https://app.netlify.com
2. **Select:** ballcode project
3. **Go to:** Site Settings → **Extensions**
4. **Check:** What extensions are installed?
5. **Action:**
   - If extensions exist → Disable them temporarily
   - If no extensions → Check `netlify.toml` file (Fix 2)

**Then retry deployment.**

---

## 📋 VERIFICATION

**After fixing, verify:**

1. **Check Extensions:**
   - Site Settings → Extensions
   - Should be empty or only needed ones

2. **Check Configuration:**
   - Look for `netlify.toml` in repository
   - Remove/comment plugin sections if not needed

3. **Retry Deployment:**
   - Netlify Dashboard → Deploys
   - Click "Retry"
   - Should succeed now

---

## 🔍 DIAGNOSTIC COMMANDS

**If you want to check locally:**

```bash
# Navigate to game repository
cd /path/to/BTEBallCODE

# Check for Netlify config
ls -la | grep netlify

# If netlify.toml exists, check contents
cat netlify.toml
```

**Look for:**
- `[plugins]` sections
- Extension references
- Build plugin configurations

---

**Status:** 🔍 **DIAGNOSING** - Check Netlify Extensions first

**Next:** Go to Site Settings → Extensions and check what's installed

