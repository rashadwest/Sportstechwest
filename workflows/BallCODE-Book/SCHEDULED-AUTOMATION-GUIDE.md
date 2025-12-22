# ⏰ Scheduled Automation Guide - Run Workflows Without You

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 17, 2025  
**Purpose:** How to enable scheduled automation so workflows run automatically  
**Status:** ✅ Complete Guide

---

## 🎯 YES - Workflows Can Run on Schedule!

**n8n supports scheduled triggers** that run workflows automatically without you being present.

---

## 📋 CURRENT STATUS

### **Orchestrator Workflow:**

**Has scheduled trigger:** ✅ YES  
**Currently:** ⏸️ **DISABLED** (for safety on dev Mac)

**The trigger:**
- **Type:** Scheduled Trigger (Hourly)
- **Schedule:** `0 * * * *` (runs every hour at :00)
- **Status:** Disabled (prevents accidental builds on dev Mac)
- **Location:** First node in workflow

**Why it's disabled:**
- Safety guardrail for dev Mac
- Prevents accidental scheduled builds
- Only enabled on production (Pi)

---

## 🚀 HOW TO ENABLE SCHEDULED AUTOMATION

### **Option 1: Enable in n8n UI** (Easiest)

1. **Open n8n UI:** `http://192.168.1.226:5678`
2. **Find workflow:** "AIMCODE (Demis) - Unity Build Orchestrator"
3. **Open the workflow**
4. **Find the node:** "Scheduled Trigger (Hourly) [DISABLED ON DEV]"
5. **Click on the node**
6. **Uncheck "Disabled"** checkbox
7. **Save the workflow**
8. **Activate the workflow** (toggle switch ON)

**Result:** Workflow will run automatically every hour!

---

### **Option 2: Enable via API** (Advanced)

```bash
# Get workflow
WORKFLOW_ID="QQxbDDdo2TCX9aA8"
curl -s -X GET "http://192.168.1.226:5678/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" > workflow.json

# Edit workflow.json to enable scheduled trigger
# (Set "disabled": false for scheduleTrigger node)

# Update workflow
curl -X PUT "http://192.168.1.226:5678/api/v1/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @workflow.json
```

---

## ⏰ SCHEDULE OPTIONS

### **Current Schedule: Hourly**

**Cron Expression:** `0 * * * *`
- Runs at: Every hour at :00 (1:00, 2:00, 3:00, etc.)
- Example times: 9:00 AM, 10:00 AM, 11:00 AM...

### **Other Schedule Options:**

#### **Every 6 Hours:**
```json
"cronExpression": "0 */6 * * *"
```
- Runs at: 12:00 AM, 6:00 AM, 12:00 PM, 6:00 PM

#### **Daily at 9 AM:**
```json
"cronExpression": "0 9 * * *"
```
- Runs at: 9:00 AM every day

#### **Every 30 Minutes:**
```json
"cronExpression": "*/30 * * * *"
```
- Runs at: :00 and :30 of every hour

#### **Weekdays at 8 AM:**
```json
"cronExpression": "0 8 * * 1-5"
```
- Runs at: 8:00 AM Monday-Friday

---

## 🔒 SAFETY GUARDRAILS

### **Current Setup (Dev Guardrails):**

**The workflow has built-in protection:**

1. **Environment Check:**
   - Checks `N8N_INSTANCE_ROLE` environment variable
   - If `N8N_INSTANCE_ROLE=dev` → Blocks scheduled builds
   - If `N8N_INSTANCE_ROLE=prod` → Allows scheduled builds

2. **Lock Mechanism:**
   - Prevents overlapping builds (55-minute lock)
   - If build is running, next scheduled run is skipped

3. **Manual Override:**
   - Set `ALLOW_SCHEDULED_BUILDS=1` to override dev protection

---

## 📊 WHAT HAPPENS WHEN SCHEDULED

### **Hourly Schedule Example:**

```
9:00 AM → Scheduled trigger fires
   ↓
9:00 AM → Workflow runs
   ↓
9:00 AM → Checks environment (prod? dev?)
   ↓
9:00 AM → Acquires lock
   ↓
9:00 AM → Dispatches GitHub build
   ↓
9:03 AM → Waits 3 minutes
   ↓
9:03 AM → Checks GitHub Actions status
   ↓
9:03 AM → Checks Netlify deployment
   ↓
9:03 AM → Releases lock
   ↓
9:03 AM → Workflow completes
```

**Next run:** 10:00 AM (if lock expired)

---

## ⚙️ HOW TO CONFIGURE

### **Step 1: Enable Scheduled Trigger**

**In n8n UI:**
1. Open workflow
2. Find "Scheduled Trigger (Hourly) [DISABLED ON DEV]"
3. Click node
4. Uncheck "Disabled"
5. Save workflow

### **Step 2: Set Environment Variable**

**On Pi (production):**
```bash
export N8N_INSTANCE_ROLE=prod
```

**On Mac (dev):**
```bash
export N8N_INSTANCE_ROLE=dev
# Scheduled builds will be blocked (safety)
```

### **Step 3: Activate Workflow**

- Toggle "Active" switch ON in n8n UI
- Workflow will now run on schedule!

---

## 🎯 RECOMMENDED SETUP

### **For Production (Pi):**

1. ✅ Enable scheduled trigger
2. ✅ Set `N8N_INSTANCE_ROLE=prod`
3. ✅ Activate workflow
4. ✅ Workflow runs hourly automatically

### **For Development (Mac):**

1. ⏸️ Keep scheduled trigger disabled (safety)
2. ✅ Use manual webhook triggers only
3. ✅ Prevents accidental builds

---

## 📋 SCHEDULE EXAMPLES

### **Example 1: Hourly Builds**
```json
{
  "rule": {
    "cronExpression": "0 * * * *"
  }
}
```
**Runs:** Every hour at :00

### **Example 2: Daily Morning Build**
```json
{
  "rule": {
    "cronExpression": "0 9 * * *"
  }
}
```
**Runs:** 9:00 AM every day

### **Example 3: Every 6 Hours**
```json
{
  "rule": {
    "cronExpression": "0 */6 * * *"
  }
}
```
**Runs:** 12:00 AM, 6:00 AM, 12:00 PM, 6:00 PM

---

## 🔍 CHECKING IF IT'S RUNNING

### **Check Workflow Executions:**

**In n8n UI:**
1. Open workflow
2. Click "Executions" tab
3. See all scheduled runs

**Via API:**
```bash
curl -s -X GET "http://192.168.1.226:5678/api/v1/executions" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  python3 -c "import sys, json; data=json.load(sys.stdin); print(f\"Total executions: {len(data.get('data', []))}\")"
```

---

## ⚠️ IMPORTANT NOTES

### **Scheduled Triggers Require:**

1. ✅ **Workflow must be ACTIVE** (toggle switch ON)
2. ✅ **Scheduled trigger must be ENABLED** (not disabled)
3. ✅ **n8n server must be running** (24/7 on Pi)
4. ✅ **Environment variables set** (for guardrails)

### **What Happens If:**

- **n8n server stops:** Scheduled runs won't execute
- **Workflow inactive:** Scheduled runs won't execute
- **Trigger disabled:** Scheduled runs won't execute
- **Lock active:** Scheduled run is skipped (prevents overlap)

---

## 🚀 QUICK ENABLE COMMANDS

### **Enable Scheduled Automation:**

1. **Open n8n UI:** `http://192.168.1.226:5678`
2. **Find workflow:** "AIMCODE (Demis) - Unity Build Orchestrator"
3. **Enable scheduled trigger** (uncheck "Disabled")
4. **Activate workflow** (toggle ON)
5. **Done!** Workflow runs automatically

---

## 📊 MONITORING SCHEDULED RUNS

### **Check Recent Executions:**

**In n8n UI:**
- Workflows → Click workflow → "Executions" tab
- See all scheduled and manual runs

**Via Command:**
```bash
# Check last 5 executions
curl -s -X GET "http://192.168.1.226:5678/api/v1/executions?limit=5" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" | \
  python3 -m json.tool
```

---

## ✅ SUMMARY

**Yes, workflows can run on schedule!**

**To enable:**
1. Enable scheduled trigger in n8n UI
2. Set `N8N_INSTANCE_ROLE=prod` (on Pi)
3. Activate workflow
4. Workflow runs automatically!

**Current status:**
- ✅ Scheduled trigger exists
- ⏸️ Currently disabled (safety)
- ✅ Can be enabled anytime
- ✅ Has safety guardrails

---

**Status:** Ready to enable  
**Next:** Enable scheduled trigger when ready for automation

