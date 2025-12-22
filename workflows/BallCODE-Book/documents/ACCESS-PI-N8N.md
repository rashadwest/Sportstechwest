# 🥧 Access Pi n8n - Not Localhost

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025

---

## 🚨 THE PROBLEM

**You're accessing n8n on Mac (localhost), not Pi!**

**Current:**
- ❌ Mac n8n: `http://localhost:5678`
- ❌ Workflow imported on Mac
- ❌ Production URL shows localhost

**Needed:**
- ✅ Pi n8n: `http://192.168.1.226:5678`
- ✅ Workflow imported on Pi
- ✅ Production URL shows Pi IP

---

## ✅ THE FIX

### Step 1: Access Pi n8n (Not Mac)

**Open in browser:**
```
http://192.168.1.226:5678
```

**NOT:**
```
http://localhost:5678  ❌
```

---

### Step 2: Import Workflow on Pi

**If workflow is not on Pi:**

1. **Open Pi n8n:** `http://192.168.1.226:5678`
2. **Click "Workflows"** (left sidebar)
3. **Check if workflow exists:**
   - If YES: Open it and check webhook URL
   - If NO: Import it (see Step 3)

---

### Step 3: Import Workflow to Pi

**If workflow doesn't exist on Pi:**

1. **In Pi n8n:** `http://192.168.1.226:5678`
2. **Click "Workflows"** → **"Import from File"**
3. **Select from desktop:**
   - `~/Desktop/n8n-workflows-to-import/n8n-screenshot-to-fix-workflow.json`
4. **Click "Import"**
5. **Activate workflow** (toggle ON)
6. **Click "Save"**

---

### Step 4: Verify Production URL on Pi

**After importing on Pi:**

1. **Open the workflow in Pi n8n**
2. **Click webhook node**
3. **Check Production URL:**
   - Should show: `http://192.168.1.226:5678/webhook/screenshot-fix`
   - NOT: `http://localhost:5678/webhook-test/screenshot-fix`

---

## 🎯 QUICK CHECKLIST

- [ ] Accessing Pi n8n: `http://192.168.1.226:5678` (not localhost)
- [ ] Workflow imported on Pi (not Mac)
- [ ] Workflow activated on Pi (toggle ON)
- [ ] Production URL shows Pi IP (192.168.1.226)
- [ ] Production URL shows `/webhook/` (not `/webhook-test/`)

---

## 💡 KEY POINT

**You have TWO n8n instances:**
1. **Mac:** `http://localhost:5678` (for testing)
2. **Pi:** `http://192.168.1.226:5678` (for production)

**All workflows should be on Pi for production use!**

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Access Guide


