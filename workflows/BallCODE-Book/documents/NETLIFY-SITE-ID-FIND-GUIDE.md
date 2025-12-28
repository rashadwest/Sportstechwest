# How to Find Netlify Site ID

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 27, 2025  
**Site:** ballcode.netlify.app

---

## 🎯 QUICK METHOD

**From Netlify Dashboard:**

1. **Go to:** https://app.netlify.com/sites/ballcode
2. **Click:** "Site configuration" or "Site settings" (gear icon)
3. **Click:** "General" tab
4. **Find:** "Site ID" section
5. **Copy:** The Site ID (looks like: `39ebfb47-c716-4f38-8f8b-7bfba36f3dc7`)

---

## 📋 STEP-BY-STEP WITH SCREENSHOTS

### **Step 1: Navigate to Site**
- Go to: https://app.netlify.com
- Click on: "ballcode" project

### **Step 2: Open Site Settings**
- Look for: "Site configuration" or gear icon ⚙️
- Click: "Site settings" or "Configuration"

### **Step 3: General Tab**
- Click: "General" tab (usually first tab)
- Scroll down to: "Site information" section

### **Step 4: Find Site ID**
- Look for: "Site ID" field
- Copy the value (UUID format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)

---

## 🔍 ALTERNATIVE METHODS

### **Method 1: From URL**
When viewing site settings, the URL may contain the site ID:
```
https://app.netlify.com/sites/[SITE_ID]/configuration/general
```

### **Method 2: Via Netlify API**
If you have `NETLIFY_AUTH_TOKEN`:
```bash
curl -H "Authorization: Bearer $NETLIFY_AUTH_TOKEN" \
     https://api.netlify.com/api/v1/sites | \
     jq '.[] | select(.name=="ballcode") | .site_id'
```

### **Method 3: From Deploy Logs**
Check recent deploy logs - Site ID may be in the URL or metadata.

---

## 📝 WHAT IT LOOKS LIKE

**Site ID Format:**
- UUID format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- Example: `39ebfb47-c716-4f38-8f8b-7bfba36f3dc7`
- Usually 36 characters (with hyphens)

**Where to Find:**
- Site Settings → General → Site ID
- Or: Site Settings → General → Site information → Site ID

---

## ✅ VERIFY YOU HAVE IT

**Test the Site ID:**
```bash
# Set the site ID
export NETLIFY_SITE_ID="your_site_id_here"

# Test with API (if you have token)
curl -H "Authorization: Bearer $NETLIFY_AUTH_TOKEN" \
     https://api.netlify.com/api/v1/sites/$NETLIFY_SITE_ID
```

**If it works:** You'll get site information back  
**If it fails:** Check that the Site ID is correct

---

## 🚀 SET IT UP FOR GARVIS

**Once you have the Site ID:**

```bash
# Add to environment (current session)
export NETLIFY_SITE_ID="your_site_id_here"

# Or add to ~/.zshrc for persistence
echo 'export NETLIFY_SITE_ID="your_site_id_here"' >> ~/.zshrc
source ~/.zshrc
```

**Then Garvis can use it automatically!**

---

## 📋 QUICK REFERENCE

**Site:** ballcode.netlify.app  
**Dashboard:** https://app.netlify.com/sites/ballcode  
**Settings:** Site Settings → General → Site ID  
**Format:** UUID (36 characters with hyphens)

---

**Status:** Follow the steps above to find your Site ID

