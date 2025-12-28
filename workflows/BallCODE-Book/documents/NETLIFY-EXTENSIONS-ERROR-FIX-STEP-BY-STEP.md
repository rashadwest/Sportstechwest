# Netlify Extensions Error - Step-by-Step Fix

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Error:** "Failed retrieving extensions for site"  
**Based on:** Netlify AI Diagnosis

---

## 🎯 THE PROBLEM

**Error:** Netlify cannot retrieve extensions/plugins for your site during build.

**Most Likely Causes:**
1. `netlify.toml` has invalid plugin/extension configuration
2. `site_id` in `netlify.toml` doesn't match your site
3. Repository connection needs refresh

---

## ✅ FIX STEPS (In Order)

### **Step 1: Check netlify.toml on GitHub** ⭐ FIRST

**Check the file in your repository:**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/blob/main/netlify.toml
2. **Look for:**
   - `[plugins]` or `[[plugins]]` sections
   - `site_id = "..."` entry
   - Any extension/plugin references

**Common Issues:**
- ❌ `site_id` that doesn't match your Netlify site
- ❌ Plugin names that don't exist
- ❌ Invalid plugin configuration

**If you find issues:**
- Remove or comment out `site_id` (Netlify auto-detects it)
- Remove invalid plugin sections
- Commit and push changes

---

### **Step 2: Quick Retry (Often Fixes Transient Errors)**

**Try this first - it often works:**

1. **Go to:** Netlify Dashboard → ballcode project
2. **Click:** "Deploys" tab
3. **Click:** "Trigger deploy" dropdown
4. **Select:** "Clear cache and deploy site"
5. **Wait:** 1-3 minutes

**This often fixes transient API errors.**

---

### **Step 3: Check Netlify Status**

**Rule out Netlify outage:**

1. **Go to:** https://www.netlifystatus.com/
2. **Check:** Are there any outages?
3. **If yes:** Wait for Netlify to fix it
4. **If no:** Continue with other fixes

---

### **Step 4: Reconnect Repository (If Step 1-3 Don't Work)**

**Refresh the GitHub connection:**

1. **Go to:** Netlify Dashboard → ballcode → Site Settings
2. **Go to:** Build & deploy → Continuous deployment
3. **Click:** "Manage repository"
4. **Click:** "Disconnect repository"
5. **Click:** "Link repository"
6. **Select:** `rashadwest/BTEBallCODE`
7. **Confirm:** Reconnect
8. **Retry deployment**

**This refreshes permissions and connection.**

---

### **Step 5: Check Site Settings for Plugins**

**Check if plugins are configured in Netlify UI:**

1. **Go to:** Netlify Dashboard → ballcode → Site Settings
2. **Go to:** Build & deploy → Build plugins (or "Plugins" tab)
3. **Check:** Are there any plugins installed?
4. **If yes:**
   - Remove plugins you don't need
   - OR verify they're correctly configured
5. **Retry deployment**

---

## 🚀 RECOMMENDED ACTION (Start Here)

**Step 1: Check netlify.toml on GitHub**

1. **Go to:** https://github.com/rashadwest/BTEBallCODE/blob/main/netlify.toml
2. **Check for:**
   - `site_id = "..."` → Remove this line (Netlify auto-detects)
   - `[plugins]` sections → Remove if not needed
   - Invalid plugin names → Fix or remove

**If netlify.toml has issues:**
- Edit the file on GitHub
- Remove problematic lines
- Commit changes
- Retry Netlify deployment

**If netlify.toml looks fine:**
- Try Step 2 (Clear cache and retry)
- Then Step 4 (Reconnect repository)

---

## 📋 COMMON netlify.toml ISSUES

### **Issue 1: site_id Mismatch**

**Problem:**
```toml
site_id = "wrong-site-id-here"
```

**Fix:**
- Remove the `site_id` line entirely
- Netlify will auto-detect the correct site ID

---

### **Issue 2: Invalid Plugins**

**Problem:**
```toml
[plugins]
  package = "@netlify/plugin-that-doesnt-exist"
```

**Fix:**
- Remove plugin sections if not needed
- OR verify plugin names are correct
- OR ensure plugins are in `package.json` if required

---

### **Issue 3: No netlify.toml Needed**

**If you don't use plugins:**
- You might not need `netlify.toml` at all
- Remove it or keep it minimal:
```toml
[build]
  publish = "Builds/WebGL"
```

---

## ✅ VERIFICATION

**After fixing, verify:**

1. **Check netlify.toml:**
   - No invalid `site_id`
   - No invalid plugins
   - Minimal configuration

2. **Retry Deployment:**
   - Clear cache and deploy
   - Should succeed now

3. **Check Deploy Log:**
   - Should pass "Reading and parsing configuration files" stage
   - Should continue to build

---

**Status:** 🔍 **CHECK NETLIFY.TOML FIRST** - Most likely the issue

**Next:** Check https://github.com/rashadwest/BTEBallCODE/blob/main/netlify.toml

