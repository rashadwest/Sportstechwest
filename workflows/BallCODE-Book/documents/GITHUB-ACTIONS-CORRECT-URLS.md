# GitHub Actions - Correct URLs

**Date:** December 24, 2025

---

## ✅ CORRECT URLS

### **Main Actions Page:**
```
https://github.com/rashadwest/BTEBallCODE/actions
```
- Shows all workflow runs
- Lists all workflows
- Can trigger workflows from here

### **Specific Workflow Page:**
```
https://github.com/rashadwest/BTEBallCODE/actions/workflows/unity-webgl-build.yml
```
- Shows runs for Unity build workflow only
- Has "Run workflow" button
- Best for triggering builds

### **Individual Run Page:**
```
https://github.com/rashadwest/BTEBallCODE/actions/runs/[RUN_ID]
```
- Shows details of one specific run
- Can only access if you have the run ID
- Use this to view logs of a specific build

---

## ❌ WRONG URL (404 Error)

**This doesn't work:**
```
https://github.com/rashadwest/BTEBallCODE/actions/runs
```
- Missing the run ID
- Results in 404 error
- Can't access without specific run number

---

## 🎯 HOW TO USE

### **To Trigger a Build:**
1. Go to: `https://github.com/rashadwest/BTEBallCODE/actions/workflows/unity-webgl-build.yml`
2. Click "Run workflow" button
3. Select "main" branch
4. Click "Run workflow"

### **To View All Runs:**
1. Go to: `https://github.com/rashadwest/BTEBallCODE/actions`
2. See all workflow runs
3. Click on any run to see details

### **To View Specific Run:**
1. Go to: `https://github.com/rashadwest/BTEBallCODE/actions`
2. Click on the run you want to see
3. Or use the run ID in the URL

---

## 📋 QUICK LINKS

**I'll open these for you:**
- ✅ Main Actions page (all workflows)
- ✅ Unity workflow page (to trigger builds)


