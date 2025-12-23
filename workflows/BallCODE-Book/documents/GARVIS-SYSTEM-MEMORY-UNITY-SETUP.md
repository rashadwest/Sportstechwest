# 🧠 Garvis System Memory: Unity Setup Process

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** Permanent memory for Garvis AI system  
**Category:** Unity CI/CD Setup  
**Status:** ✅ Active Memory  
**Last Updated:** December 23, 2025

---

## 🎯 CRITICAL KNOWLEDGE

### **Unity Setup Action (CRITICAL):**
- ❌ **DO NOT USE:** `game-ci/unity-setup@v1` (doesn't exist - 404)
- ✅ **USE:** `kuler90/setup-unity@v1` (maintained, working)

### **Why This Matters:**
- All Unity builds will fail if using deprecated action
- This is a common issue that will recur
- Garvis must remember this fix

---

## 🔧 STANDARD FIX PROCESS

### **When Unity Build Fails with "repository not found":**

1. **Check Action Existence:**
   ```bash
   gh api repos/[ORG]/[ACTION] --jq '.name'
   ```

2. **If 404 (doesn't exist):**
   - Action is deprecated
   - Find alternative in GitHub Actions marketplace
   - Update workflow file

3. **Replace in Workflow:**
   ```yaml
   # Replace this:
   - uses: game-ci/unity-setup@v1
   
   # With this:
   - uses: kuler90/setup-unity@v1
     with:
       unity-version: 2021.3.15f1
   ```

4. **Push and Test:**
   - Push updated workflow to Unity repo
   - Trigger build
   - Monitor for success

---

## 📋 WORKING CONFIGURATION

### **Unity Setup Step (WORKING):**
```yaml
- name: Setup Unity
  uses: kuler90/setup-unity@v1
  with:
    unity-version: 2021.3.15f1
```

### **Unity Build Step (WORKING):**
```yaml
- name: Build Unity WebGL
  uses: game-ci/unity-builder@v4
  env:
    UNITY_LICENSE: ${{ secrets.UNITY_LICENSE || '' }}
  with:
    targetPlatform: WebGL
    buildsPath: Builds/WebGL
    buildMethod: Default
```

---

## 🎯 GARVIS AUTO-FIX RULES

### **Rule 1: Action Repository Not Found**
**IF:** Error contains "Unable to resolve action" AND "repository not found"  
**THEN:**
1. Check if action exists: `gh api repos/[ORG]/[ACTION]`
2. If 404: Find alternative action
3. Update workflow file
4. Push to Unity repository
5. Report fix to user

### **Rule 2: Unity Setup Fails**
**IF:** Build fails at "Setup Unity" step  
**THEN:**
1. Check action version
2. Verify action exists
3. Try alternative action (`kuler90/setup-unity@v1`)
4. Update and test

### **Rule 3: Build Succeeds But No Deployment**
**IF:** Build succeeds but Netlify deployment fails  
**THEN:**
1. Check Netlify secrets
2. Verify build output exists
3. Check deployment step configuration
4. Verify site URL

---

## 🔍 QUICK DIAGNOSIS

### **Error: "repository not found"**
- **Cause:** Action doesn't exist (deprecated)
- **Fix:** Use `kuler90/setup-unity@v1`
- **Time:** 2 minutes

### **Error: "Unity license not activated"**
- **Cause:** Missing or invalid `UNITY_LICENSE` secret
- **Fix:** Set secret in GitHub repository settings
- **Time:** 1 minute

### **Error: "Build timeout"**
- **Cause:** Build takes longer than timeout
- **Fix:** Increase `timeout-minutes` in workflow
- **Time:** 1 minute

---

## 📊 SUCCESS METRICS

### **Build Success Indicators:**
- ✅ Unity setup step completes
- ✅ Unity build step completes
- ✅ Build artifacts uploaded
- ✅ Netlify deployment succeeds
- ✅ Site accessible at ballcode.netlify.app

### **Failure Indicators:**
- ❌ Action repository not found (404)
- ❌ Unity license error
- ❌ Build timeout
- ❌ No build output
- ❌ Deployment failure

---

## 🔄 MAINTENANCE REMINDERS

### **Monthly:**
- Check if actions are still maintained
- Update to latest versions
- Review build success rate

### **When Actions Fail:**
- Check action repository existence
- Find alternative if deprecated
- Update workflow immediately

---

## 📚 RELATED DOCUMENTS

- `UNITY-SETUP-AIMCODE-ASSESSMENT.md` - Full assessment
- `UNITY-SETUP-FIX-SUMMARY.md` - Quick reference
- `GARVIS-UNITY-SETUP-TROUBLESHOOTING-GUIDE.md` - Detailed guide
- `unity-webgl-build-FIXED.yml` - Working workflow

---

## ✅ MEMORY STATUS

**This Memory Is:**
- ✅ Active (use for all Unity build issues)
- ✅ Verified (tested and working)
- ✅ Complete (covers common scenarios)
- ✅ Maintained (updated December 23, 2025)

**Garvis Must:**
- ✅ Remember: `game-ci/unity-setup` doesn't exist
- ✅ Use: `kuler90/setup-unity@v1` instead
- ✅ Auto-fix: When this error occurs
- ✅ Report: Fix applied to user

---

**Memory Created:** December 23, 2025  
**Memory Status:** ✅ Permanent  
**Next Review:** When Unity build issues occur

