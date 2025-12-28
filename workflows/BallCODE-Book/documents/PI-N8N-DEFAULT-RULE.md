# 🥧 Pi n8n Default Rule - Saved to Memory

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025

---

## 🎯 CRITICAL RULE - SAVED TO MEMORY

**ALL n8n workflows, webhooks, and automation MUST use Pi n8n by default:**

- ✅ **Default:** `http://192.168.1.226:5678` (Pi n8n)
- ✅ **ALL workflows imported to Pi**
- ✅ **ALL webhook URLs use Pi IP**
- ✅ **ALL automation runs on Pi**

**Mac n8n (`localhost:5678`) ONLY when:**
- ⚠️ User explicitly requests "use Mac" or "use localhost"
- ⚠️ User explicitly requests testing on Mac
- ❌ NOT by default
- ❌ NOT for production

---

## 📋 IMPLEMENTATION

**Updated Files:**
- ✅ `.cursorrules` - Added rule section
- ✅ `setup-n8n-terminal.sh` - Default to Pi
- ✅ `scripts/test-all-webhooks.sh` - Default to Pi

**Rule Added:**
- ✅ "n8n Runtime Separation Rules" section updated
- ✅ Default behavior: Always use Pi unless explicitly requested

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Saved to Memory & Rules



