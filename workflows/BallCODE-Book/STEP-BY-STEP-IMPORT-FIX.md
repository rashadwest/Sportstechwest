# Step-by-Step: Fix Import Error in n8n UI

**Date:** December 11, 2025  
**Error:** `propertyValues[itemName] is not iterable`  
**Solution:** Manual fix in n8n UI (most reliable)

---

## 🎯 WHY MANUAL FIX IS BEST

Since your **manual triggers already work**, your workflow is functional. The import error is likely:
- Version compatibility issue
- Credentials structure
- n8n parsing quirk

**Solution:** Fix the scheduled trigger manually (2 minutes) instead of importing.

---

## ✅ STEP-BY-STEP MANUAL FIX

### Step 1: Open Your Existing Workflow
1. Go to: http://192.168.1.226:5678
2. Open your "BallCODE Unity Workflow" (or current workflow name)
3. Workflow should already be there and working

### Step 2: Fix Scheduled Trigger Node
1. **Click on "Scheduled Trigger (Every 6 Hours)" node**
2. **Click "Parameters" tab**
3. **Find these fields:**
   - **"Hours Between Triggers"** - Should be `6` ✅
   - **"Trigger at Minute"** - This is likely empty or missing ❌
4. **Set "Trigger at Minute" to: `0`**
5. **Click "Save"** (or just click away, it auto-saves)

### Step 3: Set Workflow Timezone
1. **Click three dots (⋯)** in top right of workflow canvas
2. **Select "Settings"**
3. **Scroll to "Timezone" section**
4. **Select:** `America/New_York` (or your timezone)
5. **Click "Save"**

### Step 4: Verify Fix
1. **Click back on "Scheduled Trigger" node**
2. **Check:**
   - ✅ "Trigger at Minute" shows `0`
   - ✅ No warnings on the node
   - ✅ Workflow is "Active" (toggle ON)

**Done!** Your scheduled trigger is now fixed.

---

## 🔍 IF YOU STILL WANT TO IMPORT

### Option A: Import Minimal Version
1. Use: `n8n-unity-automation-workflow-MINIMAL.json` (on Desktop)
2. This has credentials simplified
3. You'll need to re-add credentials in n8n after import

### Option B: Export Current, Then Import
1. **Export your current workflow:**
   - Three dots (⋯) → Export
   - Save to Desktop
2. **I'll fix the exported version**
3. **Import the fixed version**

### Option C: Create New Workflow
1. Create new workflow in n8n
2. Copy nodes from current workflow one by one
3. Add scheduled trigger with correct settings

---

## 🚨 TROUBLESHOOTING

### If "Trigger at Minute" field doesn't exist:
- Your n8n version might be older
- Try updating n8n
- Or use cron expression instead of interval

### If workflow still has warnings:
- Check if workflow is Active (toggle ON)
- Verify schedule is configured
- Check n8n logs for errors

### If import still fails:
- Try importing to a fresh n8n instance
- Check n8n version compatibility
- Use manual fix instead (recommended)

---

## 📊 WHAT'S DIFFERENT

**Before Fix:**
- Scheduled trigger has 3 warnings
- Missing `triggerAtMinute` parameter
- Timezone not set

**After Fix:**
- No warnings on scheduled trigger
- Triggers every 6 hours at :00 (12:00, 6:00, etc.)
- Correct timezone

---

## ✅ RECOMMENDED APPROACH

**Since manual triggers work:**
1. ✅ Use manual fix (2 minutes) - FASTEST
2. ✅ Keeps your current workflow
3. ✅ No import issues
4. ✅ All functionality preserved

**Only import if:**
- You're setting up a new n8n instance
- You want to share the workflow
- You're backing up the workflow

---

**Status:** Manual fix recommended  
**Time:** 2 minutes  
**Result:** Scheduled trigger fixed, no import needed


