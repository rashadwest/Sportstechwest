# Unity DevOps Pricing Analysis

**Date:** December 26, 2025  
**User Question:** "It says start for free. I do not see anything that is free in perpetuity"

---

## 🆓 FREE TIER (Perpetual - No Expiration)

**These are FREE forever (as long as you stay within limits):**

### ✅ **DevOps Basic Seats**
- **Free:** 3 seats (forever)
- **Cost after:** $7.00 per seat (seats 4-15), $15.00 per seat (16+)

### ✅ **Windows Compute Minutes**
- **Free:** 200 Windows STANDARD minutes per month (resets monthly)
- **Cost after:** $0.02 per build minute (STANDARD) or $0.12 per build minute (PREMIUM)

### ✅ **Storage**
- **Free:** 5 GB (forever)
- **Cost after:** $0.14 per GB per month

### ✅ **Machine Concurrency**
- **Free:** 1 concurrent machine (forever)
- **Cost after:** $0.50 per machine/day (up to 3), $2.00 per machine/day (4+)

---

## 💰 COSTS MONEY (No Free Tier)

### ❌ **Mac Compute Minutes** ⚠️ **THIS IS YOUR PROBLEM**
- **Free tier:** **NONE** (0 minutes)
- **Cost:** $0.07 per build minute (STANDARD) or $0.12 per build minute (PREMIUM)
- **Your use case:** WebGL builds typically require **Mac Compute Minutes**
- **Estimated cost per build:** ~5-10 minutes = **$0.35 - $0.70 per build**

---

## 📊 COST BREAKDOWN FOR YOUR PROJECT

### **Your Situation:**
- **Project:** BTEBallCODE (Unity WebGL game)
- **Builds needed:** WebGL platform
- **Build frequency:** Hourly (via n8n automation) = ~720 builds/month

### **Cost Calculation:**

**Option 1: Mac Compute Minutes (Required for WebGL)**
- **Build time:** ~5-10 minutes per build
- **Cost per build:** $0.35 - $0.70
- **Monthly cost (720 builds):** **$252 - $504/month** 💰💰💰

**Option 2: Windows Compute Minutes (Free Tier)**
- **Free:** 200 minutes/month
- **Problem:** WebGL builds typically require Mac
- **Cost after free tier:** $0.02 per minute
- **Monthly cost (if WebGL works on Windows):** $0 (if under 200 min) or minimal

---

## 🎯 THE REALITY CHECK

**"Free to start" means:**
- ✅ You can set up and configure for free
- ✅ You get 200 Windows minutes free (but WebGL needs Mac)
- ✅ You get 5 GB storage free
- ❌ **WebGL builds cost money** (Mac compute minutes = $0.07/min)

**"Free in perpetuity" = Only if you:**
- Use Windows builds (not WebGL)
- Stay under 200 minutes/month
- Stay under 5 GB storage
- Use only 1 concurrent machine
- Have ≤3 team members

---

## 💡 ALTERNATIVES TO CONSIDER

### **Option 1: Use Windows Builds (If Possible)**
- **Check:** Can WebGL be built on Windows in Unity Build Automation?
- **If yes:** Use free 200 Windows minutes/month
- **If no:** Mac minutes required = costs money

### **Option 2: Reduce Build Frequency**
- **Current:** Hourly builds (720/month) = $252-504/month
- **Alternative:** Build only on push to `main` = ~10-20 builds/month = **$3.50 - $14/month**
- **Best practice:** Build on code changes, not on schedule

### **Option 3: Use GitHub Actions (Current Approach)**
- **Cost:** Free (if you can get license working)
- **Problem:** Unity Personal license activation in CI/CD is difficult
- **Status:** Currently blocked by license issues

### **Option 4: Local Builds + Manual Deployment**
- **Cost:** Free (uses your Mac)
- **Automation:** Can be scripted
- **Deployment:** Manual or via n8n

---

## ✅ RECOMMENDATION

**For your use case (WebGL builds, hourly automation):**

1. **Try Windows builds first** (if Unity Build Automation supports WebGL on Windows)
   - If yes → **FREE** (200 min/month)
   - If no → Mac required = costs money

2. **If Mac required, reduce build frequency:**
   - Build on push to `main` (not hourly)
   - ~10-20 builds/month = **$3.50 - $14/month** (much more reasonable)

3. **Continue troubleshooting GitHub Actions:**
   - If license issue resolved → **FREE** (no Unity DevOps needed)

---

## 📋 NEXT STEPS

1. **Check if WebGL can build on Windows** in Unity Build Automation
2. **If Mac required:** Calculate actual build frequency needed
3. **Consider:** Build on push (not hourly) to reduce costs
4. **Decision:** Proceed with Unity Build Automation or continue GitHub Actions troubleshooting?

---

## 💰 SUMMARY

**Free in perpetuity:**
- ✅ 3 seats
- ✅ 200 Windows minutes/month
- ✅ 5 GB storage
- ✅ 1 concurrent machine

**Costs money:**
- ❌ Mac compute minutes (required for WebGL) = $0.07/min
- ❌ Storage over 5 GB = $0.14/GB/month
- ❌ Additional seats = $7-15/seat

**Your situation:**
- WebGL builds = Mac required = **$0.35-0.70 per build**
- Hourly builds = **$252-504/month** 💰
- Build on push = **$3.50-14/month** ✅

---

**Bottom line:** Unity Build Automation is NOT free for WebGL builds. It costs ~$0.35-0.70 per build. For hourly builds, that's $252-504/month. Consider building on push instead (much cheaper) or continue troubleshooting GitHub Actions (free if license works).


