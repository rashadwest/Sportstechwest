# Workflow Skip Behavior - Understanding
## Why Workflows Skip and How to Control It

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 12, 2025  
**Status:** ✅ Working as Designed

---

## 🔍 WHAT HAPPENED

### Your Workflow Output Shows:
- **Status:** `skipped`
- **Message:** "Workflow skipped: No build, edits, or deploy needed based on action plan"
- **Action Plan:**
  - `needsUnityEdits: false`
  - `needsBuild: false`
  - `needsDeploy: false`
- **Result:** `shouldProceed: false`

### This Means:
✅ **Workflow is working correctly!**
- AI analyzed the request
- Determined no changes needed
- Skipped unnecessary build/deploy
- Saved time and costs

---

## 🎯 WHY IT SKIPS

### The Workflow Skips When:
1. **No Unity edits needed** (`needsUnityEdits: false`)
2. **No build needed** (`needsBuild: false`)
3. **No deploy needed** (`needsDeploy: false`)

### This Happens When:
- Request is unclear or empty
- Request doesn't require code changes
- Request is informational only
- AI determines no action needed

---

## ✅ IS THIS CORRECT?

### Yes, if:
- ✅ You want to save costs (no unnecessary builds)
- ✅ You want efficiency (only build when needed)
- ✅ Request didn't actually need changes

### No, if:
- ❌ You want to build every time regardless
- ❌ Request should have triggered a build
- ❌ You want to test builds regularly

---

## 🔧 HOW TO CONTROL SKIP BEHAVIOR

### Option 1: Always Build (Remove Skip Logic)

**If you want builds every time:**

1. **Find "Parse AI Response" node** in workflow
2. **Modify the code** to always set `shouldProceed: true`:

```javascript
// Force shouldProceed to true (always build)
return {
  json: {
    ...$('Normalize Input').item.json,
    actionPlan: actionPlan,
    shouldProceed: true,  // ← Force to true
    needsUnityEdits: actionPlan.needsUnityEdits || false,
    needsBuild: true,  // ← Force build
    needsDeploy: true  // ← Force deploy
  }
};
```

**Result:** Workflow will always proceed, even if AI says no action needed

---

### Option 2: Make AI More Sensitive (Adjust AI Prompt)

**If you want AI to detect more cases that need builds:**

1. **Find "AI Analyze Request" node**
2. **Modify the system prompt** to be more sensitive:

```
You are a Unity development assistant. Analyze development requests and create a structured action plan.

IMPORTANT: If the request is unclear, default to needing a build to verify current state.
Only skip if you are CERTAIN no changes are needed.

Return JSON with:
- needsUnityEdits: boolean
- needsBuild: boolean (default to true if uncertain)
- needsDeploy: boolean (default to true if uncertain)
```

**Result:** AI will be more likely to trigger builds

---

### Option 3: Check Request Content (Better Detection)

**If you want to detect empty/unclear requests:**

1. **Find "Normalize Input" node**
2. **Add validation** for request content:

```javascript
// Check if request is meaningful
const request = body.request || body.head_commit?.message || 'Automated build from scheduled trigger';

// If request is too generic, force a build
const isGenericRequest = request.toLowerCase().includes('unknown') || 
                         request.toLowerCase().includes('scheduled') ||
                         request.trim().length < 10;

if (isGenericRequest) {
  // Force a build for scheduled/unknown requests
  return {
    json: {
      request: 'Scheduled verification build',
      triggerType: triggerType,
      timestamp: new Date().toISOString(),
      branch: branch,
      commitMessage: 'Scheduled build',
      forceBuild: true  // Flag to force build
    }
  };
}
```

**Result:** Scheduled/unknown requests will trigger builds

---

## 📊 CURRENT BEHAVIOR

### What Your Workflow Does:
1. ✅ Receives request (or scheduled trigger)
2. ✅ AI analyzes request
3. ✅ AI determines if action needed
4. ✅ If no action → Skip (save costs)
5. ✅ If action needed → Build/Deploy

### Your Current Output:
- **Request:** "Unknown request" (from scheduled trigger)
- **AI Analysis:** No action needed
- **Result:** Skipped (correct behavior)

---

## 🎯 RECOMMENDATIONS

### For Scheduled Builds (Every 3 Hours):

**Option A: Always Build on Schedule**
- Modify to force `shouldProceed: true` for scheduled triggers
- Ensures regular builds even if no changes
- Good for: Testing, verification, regular updates

**Option B: Smart Skip (Current)**
- Only build when AI detects need
- Saves costs and time
- Good for: Cost-conscious, efficient builds

**Option C: Hybrid Approach**
- Scheduled triggers → Always build
- Manual/webhook triggers → Smart skip
- Best of both worlds

---

## 🔧 QUICK FIX: Force Builds on Schedule

### If You Want Scheduled Builds to Always Run:

**Modify "Parse AI Response" node:**

```javascript
// Parse AI response
const aiResponse = $input.item.json.choices?.[0]?.message?.content || '{}';
let actionPlan;

try {
  const jsonMatch = aiResponse.match(/\{[\s\S]*\}/);
  actionPlan = JSON.parse(jsonMatch ? jsonMatch[0] : aiResponse);
} catch (e) {
  actionPlan = {
    needsUnityEdits: false,
    needsBuild: true,  // Default to build
    needsDeploy: true,
    estimatedTime: '15 minutes',
    priority: 'medium'
  };
}

// Check trigger type - force build for scheduled
const triggerType = $('Normalize Input').item.json.triggerType;
const isScheduled = triggerType === 'scheduled';

// Force build for scheduled triggers
const shouldProceed = isScheduled ? true : (actionPlan.needsBuild || actionPlan.needsUnityEdits || actionPlan.needsDeploy);

return {
  json: {
    ...$('Normalize Input').item.json,
    actionPlan: actionPlan,
    shouldProceed: shouldProceed,
    needsUnityEdits: actionPlan.needsUnityEdits || false,
    needsBuild: isScheduled ? true : (actionPlan.needsBuild || false),
    needsDeploy: isScheduled ? true : (actionPlan.needsDeploy || false)
  }
};
```

**Result:** Scheduled builds will always run, manual/webhook builds will still be smart

---

## ✅ SUMMARY

### Current Status:
- ✅ Workflow is working correctly
- ✅ AI analyzed request
- ✅ Determined no action needed
- ✅ Skipped to save costs

### Your Options:
1. **Keep current behavior** (smart skip - saves costs)
2. **Force builds always** (always build regardless)
3. **Hybrid approach** (force scheduled, smart for manual)

### Recommendation:
**Hybrid approach** - Force builds on scheduled triggers (every 3 hours), but keep smart skip for manual/webhook triggers. This gives you regular builds while still saving costs on unnecessary manual builds.

---

**Version:** Workflow Skip Behavior Guide  
**Created:** December 12, 2025  
**Status:** Ready to Use



