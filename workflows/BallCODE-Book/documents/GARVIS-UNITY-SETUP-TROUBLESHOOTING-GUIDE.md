# 🔧 Garvis Unity Setup Troubleshooting Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Purpose:** Garvis system memory for Unity CI/CD setup issues  
**Last Updated:** December 23, 2025  
**Status:** ✅ Active Reference Guide

---

## 🎯 QUICK REFERENCE

### **Common Error:**
```
Unable to resolve action game-ci/unity-setup, repository not found
```

### **Solution:**
Replace with `kuler90/setup-unity@v1`

### **Fix:**
```yaml
# OLD (deprecated):
- uses: game-ci/unity-setup@v1

# NEW (working):
- uses: kuler90/setup-unity@v1
  with:
    unity-version: 2021.3.15f1
```

---

## 📋 AIMCODE TROUBLESHOOTING PROCESS

### **When Unity Builds Fail:**

#### **Step 1: CLEAR Framework**
1. **Clarity:** What error is occurring?
   - Check GitHub Actions logs
   - Identify exact error message
   - Note which step is failing

2. **Logic:** What's the systematic approach?
   - Is it an action resolution issue?
   - Is it a Unity license issue?
   - Is it a build configuration issue?

3. **Examples:** What do others do?
   - Check GitHub Actions marketplace
   - Search for maintained alternatives
   - Review Unity CI/CD best practices

4. **Adaptation:** How do we remain flexible?
   - Try alternative actions
   - Update action versions
   - Use fallback methods

5. **Results:** What are measurable outcomes?
   - Build success rate
   - Build time
   - Deployment success

---

#### **Step 2: Alpha Evolve (Systematic Learning)**

**Layer 1: Understand the Error**
- Read error message carefully
- Identify which action/step is failing
- Check if repository exists (404 = doesn't exist)

**Layer 2: Understand the System**
- Unity setup → Unity build → Artifact upload → Deploy
- Each step has dependencies
- Failure in one step blocks all subsequent steps

**Layer 3: Understand Integration**
- n8n → GitHub Actions → Unity → Netlify
- Each system has requirements
- Verify all connections

**Layer 4: Build Solution**
- Start with simplest fix
- Test incrementally
- Document what works

---

#### **Step 3: Research**

**Check Action Existence:**
```bash
gh api repos/[ORG]/[ACTION] --jq '.name, .full_name'
```

**If 404 (doesn't exist):**
- Action is deprecated or moved
- Find alternative in GitHub Actions marketplace
- Check Unity CI/CD documentation

**Verify Alternative:**
- Check stars/usage
- Check last updated date
- Check documentation

---

#### **Step 4: Expert Consultation**

**Hassabis (Systems Thinking):**
- Build understanding layer by layer
- Test each layer before moving forward
- Don't skip steps

**Jobs (Simplicity):**
- Use simplest solution that works
- Remove unnecessary complexity
- Focus on what works

**Resnick (Constructionist):**
- Build incrementally
- Test each piece
- Learn by doing

---

## 🔍 COMMON ISSUES & SOLUTIONS

### **Issue 1: Action Repository Not Found (404)**

**Symptoms:**
- Error: "Unable to resolve action [org]/[action], repository not found"
- Build fails at setup step

**Diagnosis:**
```bash
gh api repos/[ORG]/[ACTION] --jq '.name'
# If 404: Repository doesn't exist
```

**Solution:**
1. Find alternative action in GitHub Actions marketplace
2. Check Unity CI/CD documentation
3. Update workflow file with alternative
4. Test build

**Example Fix:**
```yaml
# Deprecated:
- uses: game-ci/unity-setup@v1

# Fixed:
- uses: kuler90/setup-unity@v1
  with:
    unity-version: 2021.3.15f1
```

---

### **Issue 2: Unity License Activation**

**Symptoms:**
- Build fails with license error
- "Unity license not activated"

**Solution:**
- Ensure `UNITY_LICENSE` secret is set in GitHub
- Use Unity Personal license (free, 2 machines)
- Or use Unity Professional license (paid, unlimited)

**Workflow:**
```yaml
env:
  UNITY_LICENSE: ${{ secrets.UNITY_LICENSE || '' }}
```

---

### **Issue 3: Build Timeout**

**Symptoms:**
- Build runs but times out
- No error, just stops

**Solution:**
- Increase timeout in workflow:
```yaml
timeout-minutes: 60  # Increase from default 30
```

---

### **Issue 4: Build Output Not Found**

**Symptoms:**
- Build completes but no output
- Deployment fails

**Solution:**
- Verify build path in workflow:
```yaml
buildsPath: Builds/WebGL
```

- Check build verification step
- Ensure Unity build actually creates output

---

## 📊 VERIFICATION CHECKLIST

### **Before Pushing Workflow Changes:**

- [ ] Action repository exists (check with `gh api`)
- [ ] Action version is correct
- [ ] Unity version matches project
- [ ] Secrets are configured in GitHub
- [ ] Build path is correct
- [ ] Timeout is sufficient

### **After Build Completes:**

- [ ] Build succeeded (check GitHub Actions)
- [ ] Build artifacts uploaded
- [ ] Netlify deployment succeeded
- [ ] Site is accessible
- [ ] Game loads correctly
- [ ] Levels are accessible

---

## 🔄 MAINTENANCE PROCESS

### **Monthly Review:**
1. Check if actions are still maintained
2. Update to latest versions if available
3. Review build success rate
4. Optimize build time if needed

### **When Actions Fail:**
1. Check if action repository exists
2. Check if new version available
3. Find alternative if deprecated
4. Update workflow and test

---

## 📚 REFERENCE RESOURCES

### **Unity CI/CD Actions:**
- `kuler90/setup-unity@v1` - Unity setup (recommended)
- `game-ci/unity-builder@v4` - Unity build
- GitHub Actions Marketplace: https://github.com/marketplace

### **Unity Documentation:**
- Unity CI/CD: https://docs.unity.com/build-automation
- Unity Build Automation: https://docs.unity.com/build-automation

### **Troubleshooting:**
- GitHub Actions logs: Check workflow runs
- Unity build logs: Check build step output
- Netlify logs: Check deployment logs

---

## 🎯 GARVIS AUTOMATION INTEGRATION

### **When Garvis Encounters Unity Build Failures:**

1. **Auto-Diagnose:**
   - Check error message
   - Identify failing step
   - Check action repository existence

2. **Auto-Fix (if possible):**
   - Update action version
   - Replace deprecated actions
   - Update workflow file

3. **Report:**
   - Document issue
   - Document solution
   - Update this guide

### **Garvis Commands:**
```bash
# Check Unity build status
python scripts/garvis-unity-build-workflow.py --monitor

# Trigger Unity build
python scripts/garvis-unity-build-workflow.py --trigger

# Full workflow
python scripts/garvis-unity-build-workflow.py --full
```

---

## ✅ SUCCESS PATTERNS

### **Working Unity Setup:**
```yaml
- name: Setup Unity
  uses: kuler90/setup-unity@v1
  with:
    unity-version: 2021.3.15f1

- name: Build Unity WebGL
  uses: game-ci/unity-builder@v4
  env:
    UNITY_LICENSE: ${{ secrets.UNITY_LICENSE || '' }}
  with:
    targetPlatform: WebGL
    buildsPath: Builds/WebGL
```

### **Working Build Verification:**
```yaml
- name: Verify Build Output
  run: |
    if [ ! -d "Builds/WebGL" ]; then
      echo "❌ Build directory not found"
      exit 1
    fi
    if [ ! -f "Builds/WebGL/index.html" ]; then
      echo "❌ index.html not found"
      exit 1
    fi
    echo "✅ Build verified"
```

---

## 🚨 ESCALATION RULES

### **If Auto-Fix Fails:**
1. Document issue in detail
2. Research alternative solutions
3. Try manual fixes
4. Escalate to user if needed

### **If Build Consistently Fails:**
1. Review entire workflow
2. Check Unity project structure
3. Verify all dependencies
4. Consider alternative CI/CD approach

---

## 📝 UPDATE LOG

### **December 23, 2025:**
- ✅ Identified root cause: `game-ci/unity-setup` doesn't exist
- ✅ Fixed with `kuler90/setup-unity@v1`
- ✅ Created comprehensive troubleshooting guide
- ✅ Documented AIMCODE process

---

**Guide Status:** ✅ Active  
**Last Verified:** December 23, 2025  
**Next Review:** January 2026


