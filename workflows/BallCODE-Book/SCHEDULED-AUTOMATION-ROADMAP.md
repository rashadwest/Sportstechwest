# ⏰ Scheduled Automation Roadmap

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 17, 2025  
**Status:** 📋 Roadmap - Future Implementation  
**Current:** Manual webhook triggers only

---

## 🎯 CURRENT STATE

**Orchestrator Workflow:**
- ✅ Has scheduled trigger node (hourly: `0 * * * *`)
- ⏸️ Currently **DISABLED** (safety for dev Mac)
- ✅ Manual webhook triggers working
- ✅ Lock mechanism functional

**Why Disabled:**
- Safety guardrail prevents accidental builds on dev Mac
- Only enabled on production (Pi) when ready

---

## 🗺️ ROADMAP: Enabling Scheduled Automation

### **Phase 1: Preparation** (When Ready)

**Prerequisites:**
- [ ] n8n running 24/7 on Pi (production)
- [ ] Environment variable set: `N8N_INSTANCE_ROLE=prod`
- [ ] All credentials configured
- [ ] Workflow tested and stable
- [ ] Lock mechanism verified working

**Timeline:** 1 day (verification only)

---

### **Phase 2: Enable Scheduled Trigger** (When Ready)

**Steps:**
1. [ ] Open n8n UI: `http://192.168.1.226:5678`
2. [ ] Find workflow: "AIMCODE (Demis) - Unity Build Orchestrator"
3. [ ] Open workflow
4. [ ] Find node: "Scheduled Trigger (Hourly) [DISABLED ON DEV]"
5. [ ] Click node → Uncheck "Disabled"
6. [ ] Save workflow
7. [ ] Verify workflow is Active (toggle ON)

**Result:** Workflow runs automatically every hour

**Timeline:** 5 minutes

---

### **Phase 3: Monitor & Adjust** (First Week)

**Week 1 Tasks:**
- [ ] Monitor scheduled executions daily
- [ ] Check for any issues
- [ ] Verify lock mechanism prevents overlaps
- [ ] Adjust schedule if needed (hourly → every 6 hours, etc.)

**Monitoring:**
- Check n8n Executions tab daily
- Review build success rates
- Check for any skipped runs (lock active)

**Timeline:** Ongoing monitoring

---

### **Phase 4: Optimize Schedule** (After Week 1)

**Options to Consider:**

#### **Option A: Keep Hourly** (Current)
- **Schedule:** `0 * * * *` (every hour)
- **Pros:** Frequent builds, fast iteration
- **Cons:** More GitHub Actions usage
- **Best for:** Active development

#### **Option B: Every 6 Hours**
- **Schedule:** `0 */6 * * *` (12 AM, 6 AM, 12 PM, 6 PM)
- **Pros:** Balanced frequency
- **Cons:** Less frequent updates
- **Best for:** Stable production

#### **Option C: Daily Morning Build**
- **Schedule:** `0 9 * * *` (9 AM daily)
- **Pros:** Once per day, predictable
- **Cons:** Slower iteration
- **Best for:** Production maintenance

#### **Option D: Weekdays Only**
- **Schedule:** `0 9 * * 1-5` (9 AM Mon-Fri)
- **Pros:** No weekend builds
- **Cons:** No weekend updates
- **Best for:** Business hours only

**Timeline:** Adjust after 1 week of monitoring

---

## 📊 SCHEDULE OPTIONS COMPARISON

| Schedule | Cron Expression | Frequency | Use Case |
|----------|----------------|----------|----------|
| **Hourly** | `0 * * * *` | Every hour | Active development |
| **Every 6 Hours** | `0 */6 * * *` | 4x per day | Balanced |
| **Daily Morning** | `0 9 * * *` | Once daily | Production |
| **Weekdays 9 AM** | `0 9 * * 1-5` | Weekdays only | Business hours |
| **Every 30 Min** | `*/30 * * * *` | 48x per day | Very active dev |

---

## 🔒 SAFETY FEATURES (Already Built-In)

### **1. Dev Guardrails**
- **Environment Check:** Blocks scheduled builds if `N8N_INSTANCE_ROLE=dev`
- **Override:** Set `ALLOW_SCHEDULED_BUILDS=1` to override
- **Status:** ✅ Already implemented

### **2. Lock Mechanism**
- **Prevents Overlaps:** 55-minute lock prevents concurrent builds
- **Auto-Skip:** If lock active, scheduled run is skipped
- **Status:** ✅ Already working

### **3. Manual Override**
- **Webhook Always Works:** Manual triggers bypass schedule
- **Can Trigger Anytime:** Not limited by schedule
- **Status:** ✅ Already working

---

## 🚀 ENABLEMENT CHECKLIST

**When you're ready to enable scheduled automation:**

### **Pre-Enablement:**
- [ ] n8n running 24/7 on Pi
- [ ] `N8N_INSTANCE_ROLE=prod` set on Pi
- [ ] All credentials configured
- [ ] Workflow tested and stable
- [ ] Lock mechanism verified

### **Enablement:**
- [ ] Open n8n UI
- [ ] Find orchestrator workflow
- [ ] Enable scheduled trigger (uncheck "Disabled")
- [ ] Activate workflow (toggle ON)
- [ ] Verify first scheduled run

### **Post-Enablement:**
- [ ] Monitor first 24 hours
- [ ] Check execution logs
- [ ] Verify builds are triggering
- [ ] Adjust schedule if needed

---

## 📋 FUTURE ENHANCEMENTS

### **Phase 5: Advanced Scheduling** (Future)

**Smart Scheduling:**
- [ ] Schedule based on code changes (only build when changes detected)
- [ ] Schedule based on time of day (avoid peak hours)
- [ ] Schedule based on day of week (weekdays only)
- [ ] Dynamic scheduling (adjust based on activity)

**Timeline:** Future enhancement

---

## 🎯 RECOMMENDED APPROACH

### **For Now (Current):**
- ✅ Keep scheduled trigger **DISABLED**
- ✅ Use manual webhook triggers
- ✅ Safe and controlled

### **When Ready:**
1. **Week 1:** Enable hourly schedule, monitor closely
2. **Week 2:** Review and optimize schedule
3. **Week 3+:** Adjust based on needs

### **Production Setup:**
- Enable on Pi only (not Mac)
- Set `N8N_INSTANCE_ROLE=prod`
- Monitor first week closely
- Adjust schedule as needed

---

## 📝 QUICK REFERENCE

### **Enable Scheduled Automation:**
1. Open n8n UI
2. Find workflow
3. Enable scheduled trigger
4. Activate workflow
5. Monitor first runs

### **Change Schedule:**
1. Open workflow
2. Click scheduled trigger node
3. Edit cron expression
4. Save workflow

### **Disable Scheduled Automation:**
1. Open workflow
2. Click scheduled trigger node
3. Check "Disabled"
4. Save workflow

---

## ✅ SUMMARY

**Current Status:**
- ✅ Scheduled trigger exists (hourly)
- ⏸️ Currently disabled (safety)
- ✅ Can be enabled anytime
- ✅ Safety guardrails in place

**Roadmap:**
- **Phase 1:** Preparation (when ready)
- **Phase 2:** Enable scheduled trigger (5 minutes)
- **Phase 3:** Monitor & adjust (first week)
- **Phase 4:** Optimize schedule (after week 1)

**When to Enable:**
- When n8n is running 24/7 on Pi
- When you want automated builds
- When workflow is stable
- When ready to monitor

---

**Status:** Roadmap complete  
**Action:** Enable when ready for automation

