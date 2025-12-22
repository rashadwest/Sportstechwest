# 🥧 Pi n8n URL Configuration - Memory

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 14, 2025

---

## 🎯 CRITICAL CONFIGURATION

**ALL n8n workflows should use Pi URL:**
- **Pi n8n URL:** `http://192.168.1.226:5678`
- **NOT localhost:** `http://localhost:5678`

**Production webhook URLs should be:**
- `http://192.168.1.226:5678/webhook/[path]`
- **NOT:** `http://localhost:5678/webhook-test/[path]`

---

## 📋 WORKFLOW CONFIGURATION

**When importing workflows to Pi:**
1. Use Pi IP: `192.168.1.226:5678`
2. Use production webhook path (not webhook-test)
3. All webhooks should be accessible at: `http://192.168.1.226:5678/webhook/[path]`

---

**Version:** 1.0  
**Created:** December 14, 2025  
**Status:** ✅ Memory Reference


