# 🚀 Unity Build Workflow - Quick Start

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 23, 2025

---

## ⚡ QUICK COMMANDS

### **Trigger Build:**
```bash
python scripts/garvis-unity-build-workflow.py --trigger
```

### **Monitor Build:**
```bash
python scripts/garvis-unity-build-workflow.py --monitor
```

### **Full Workflow (Recommended):**
```bash
python scripts/garvis-unity-build-workflow.py --full
```

---

## 📋 WHAT IT DOES

1. **Triggers** Unity build via n8n webhook
2. **Monitors** GitHub Actions build status
3. **Verifies** Netlify deployment
4. **Reports** status to `garvis_status.json`

---

## 🎯 INTEGRATION

### **With Garvis Deploy:**
After deploying game levels:
```bash
python scripts/garvis-deploy.py --game
python scripts/garvis-unity-build-workflow.py --full
```

### **Standalone:**
```bash
# Just trigger and monitor
python scripts/garvis-unity-build-workflow.py --full
```

---

## 📊 STATUS

Check status file:
```bash
cat garvis_status.json
```

---

**Status:** ✅ Ready to Use!


