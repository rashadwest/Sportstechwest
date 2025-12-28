# Update n8n Schedule to Every 3 Hours
## Cost-Conscious Build Schedule

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Purpose:** Reduce OpenAI API spending by building every 3 hours instead of hourly  
**Status:** 🎯 Ready to Update

---

## 🎯 CHANGES NEEDED

### Current Schedule:
- **Frequency:** Every hour (24 builds per day)
- **Cron:** `0 * * * *` (runs at :00 of every hour)

### New Schedule:
- **Frequency:** Every 3 hours (8 builds per day)
- **Cron:** `0 */3 * * *` (runs at :00 of every 3rd hour)
- **Times:** 12:00 AM, 3:00 AM, 6:00 AM, 9:00 AM, 12:00 PM, 3:00 PM, 6:00 PM, 9:00 PM

---

## 📋 HOW TO UPDATE IN n8n

### Step 1: Open Workflow
1. Open n8n UI
2. Go to your workflow: "Unity AI Automation - HOURLY BUILD"
3. Click on the workflow to edit

### Step 2: Update Scheduled Trigger
1. **Click on "Scheduled Trigger (Hourly)" node**
2. **Find "Cron Expression" field**
3. **Change from:** `0 * * * *`
4. **Change to:** `0 */3 * * *`
5. **Update node name** (optional): "Scheduled Trigger (Every 3 Hours)"
6. **Save the node**

### Step 3: Add Spending Check (Optional but Recommended)
1. **Add a Code node** before "AI Analyze Request"
2. **Name it:** "Check Spending Before AI"
3. **Add logic to:**
   - Check if spending is within budget
   - Skip AI call if spending too high
   - Log spending check

---

## 💰 COST SAVINGS

### Before (Hourly):
- **Builds per day:** 24
- **Estimated OpenAI cost per build:** ~$0.001-0.002
- **Daily cost:** ~$0.024-0.048
- **Monthly cost:** ~$0.72-1.44

### After (Every 3 Hours):
- **Builds per day:** 8
- **Estimated OpenAI cost per build:** ~$0.001-0.002
- **Daily cost:** ~$0.008-0.016
- **Monthly cost:** ~$0.24-0.48

### Savings:
- **67% reduction** in build frequency
- **67% reduction** in OpenAI API costs
- **Still covers** all important times of day

---

## ✅ VERIFICATION

### After Update:
1. **Check schedule:** Verify cron expression is `0 */3 * * *`
2. **Test trigger:** Wait for next 3-hour mark or trigger manually
3. **Monitor spending:** Check OpenAI dashboard after first run
4. **Verify builds:** Check that builds still happen correctly

---

## 🔍 MONITORING SPENDING

### Check After Each Build:
1. Go to: https://platform.openai.com/usage
2. Check recent usage
3. Verify spending is within budget
4. Adjust if needed

### Set Up Alerts (Optional):
- Set spending limit in OpenAI dashboard
- Get notified when approaching budget
- Pause workflow if spending too high

---

## 📊 BUILD SCHEDULE

### New Schedule Times:
- **12:00 AM** (Midnight)
- **3:00 AM**
- **6:00 AM**
- **9:00 AM**
- **12:00 PM** (Noon)
- **3:00 PM**
- **6:00 PM**
- **9:00 PM**

**Total:** 8 builds per day (down from 24)

---

## 🎯 RECOMMENDED ADDITIONS

### 1. Spending Check Node (Before AI):
```javascript
// Check if we should proceed with AI call
const dailySpendingLimit = 0.50; // $0.50 per day max
const currentSpending = 0.39; // Get from OpenAI API or track manually

if (currentSpending >= dailySpendingLimit) {
  return {
    json: {
      ...$input.item.json,
      skipAI: true,
      reason: 'Daily spending limit reached',
      shouldProceed: false
    }
  };
}

return {
  json: {
    ...$input.item.json,
    skipAI: false,
    shouldProceed: true
  }
};
```

### 2. Conditional AI Call:
- Add IF node after spending check
- Only call AI if spending is OK
- Skip AI if spending too high

---

## ✅ UPDATE CHECKLIST

- [ ] Update cron expression to `0 */3 * * *`
- [ ] Update node name (optional)
- [ ] Test schedule works
- [ ] Monitor first few builds
- [ ] Check spending after first day
- [ ] Adjust if needed

---

**Version:** Cost-Conscious Schedule Update  
**Created:** December 12, 2025  
**Status:** Ready to Apply



