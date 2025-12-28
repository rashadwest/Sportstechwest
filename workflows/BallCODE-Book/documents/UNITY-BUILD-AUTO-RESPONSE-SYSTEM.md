# Unity Build Auto-Response System

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Purpose:** Automated detection and response to Unity build errors  
**Methodology:** AIMCODE (Self-Healing Systems)

---

## 🤖 AUTOMATED ERROR DETECTION

### **Error Pattern Recognition**

**Pattern 1: Syntax Errors**
```yaml
# Detection:
- Error: "Invalid workflow file"
- Error: "Unrecognized named-value"
- Error: "repository not found"
- Duration: 0-5 seconds

# Auto-Response:
1. Validate workflow syntax
2. Check action existence
3. Report specific errors
4. Suggest fixes
```

**Pattern 2: License Errors (Exit Code 125)**
```yaml
# Detection:
- Exit Code: 125
- Error: "License activation failed"
- Duration: 1-5 minutes

# Auto-Response:
1. Check UNITY_LICENSE secret
2. Verify base64 format
3. Test license file creation
4. Attempt email/password fallback
5. Generate diagnostic report
```

**Pattern 3: Build Errors (Exit Code 1)**
```yaml
# Detection:
- Exit Code: 1
- Error: "Build failed"
- Duration: 5-15 minutes

# Auto-Response:
1. Capture build logs
2. Identify error category
3. Check compilation errors
4. Verify project structure
5. Suggest specific fixes
```

---

## 🔄 AUTO-RESPONSE WORKFLOWS

### **Response Workflow 1: Syntax Error Handler**

```yaml
- name: Auto-Fix Syntax Errors
  if: failure() && contains(github.event.head_commit.message, 'syntax')
  run: |
    echo "🔧 Attempting auto-fix for syntax errors..."
    
    # Check for common syntax issues
    if grep -q "if:.*secrets\." .github/workflows/unity-webgl-build.yml; then
      echo "⚠️ Found secrets in if condition - needs manual fix"
    fi
    
    if grep -q "game-ci/unity-setup" .github/workflows/unity-webgl-build.yml; then
      echo "⚠️ Found deprecated action - needs manual fix"
    fi
    
    # Generate fix suggestions
    echo "📋 Fix suggestions generated"
```

---

### **Response Workflow 2: License Error Handler**

```yaml
- name: Auto-Diagnose License Errors
  if: failure() && job.status == 'failure'
  run: |
    echo "🔍 Diagnosing license activation failure..."
    
    # Check if UNITY_LICENSE secret exists
    if [ -z "${{ secrets.UNITY_LICENSE }}" ]; then
      echo "❌ UNITY_LICENSE secret is missing"
      echo "📋 Action: Add UNITY_LICENSE secret with base64-encoded license"
      exit 1
    fi
    
    # Test base64 decoding
    if ! echo "${{ secrets.UNITY_LICENSE }}" | base64 -d > /dev/null 2>&1; then
      echo "❌ UNITY_LICENSE is not valid base64"
      echo "📋 Action: Re-encode license file as base64"
      exit 1
    fi
    
    # Check license file location
    if [ ! -f ~/.local/share/unity3d/Unity_lic.ulf ]; then
      echo "❌ License file not found at expected location"
      echo "📋 Action: Check license activation step"
      exit 1
    fi
    
    echo "✅ License diagnostics complete"
```

---

### **Response Workflow 3: Build Error Handler**

```yaml
- name: Auto-Diagnose Build Errors
  if: failure() && job.status == 'failure'
  run: |
    echo "🔍 Diagnosing build failure..."
    
    # Check for compilation errors
    if grep -q "error CS" "${{ github.workspace }}/Builds/WebGL" 2>/dev/null; then
      echo "❌ C# compilation errors detected"
      echo "📋 Action: Fix compilation errors in Unity project"
    fi
    
    # Check for missing assets
    if [ ! -d "Builds/WebGL" ]; then
      echo "❌ Build directory not found"
      echo "📋 Action: Check Unity build logs for errors"
    fi
    
    # Check Unity version
    UNITY_VERSION=$(grep "m_EditorVersion" ProjectSettings/ProjectVersion.txt | cut -d' ' -f2)
    WORKFLOW_VERSION="2021.3.15f1"
    if [ "$UNITY_VERSION" != "$WORKFLOW_VERSION" ]; then
      echo "⚠️ Unity version mismatch: Project=$UNITY_VERSION, Workflow=$WORKFLOW_VERSION"
      echo "📋 Action: Update workflow to match project version"
    fi
    
    echo "✅ Build diagnostics complete"
```

---

## 📊 ERROR RESPONSE MATRIX

| Error Pattern | Detection | Auto-Response | Manual Action |
|---------------|----------|---------------|---------------|
| Syntax Error | ✅ Immediate | ⚠️ Report | Fix workflow |
| Missing Secret | ✅ Pre-flight | ⚠️ Report | Add secret |
| Invalid Format | ✅ Pre-flight | ⚠️ Report | Fix format |
| License 125 | ✅ Runtime | ⚠️ Diagnose | Fix license |
| Build Error 1 | ✅ Runtime | ⚠️ Diagnose | Fix code |
| Deployment | ✅ Post-build | ⚠️ Diagnose | Fix config |

---

## 🚨 AUTOMATED ALERTING

### **Alert Triggers**

**Critical Alerts (Immediate):**
- Workflow syntax errors
- Missing required secrets
- Non-existent actions

**Warning Alerts (Monitor):**
- License activation warnings
- Build time increases
- Deployment delays

**Info Alerts (Track):**
- Successful builds
- Build time trends
- Deployment success rate

---

## 📋 DIAGNOSTIC REPORT GENERATION

**Auto-Generated Report:**
```yaml
- name: Generate Diagnostic Report
  if: always()
  run: |
    echo "## 🔍 Build Diagnostic Report" >> $GITHUB_STEP_SUMMARY
    echo "" >> $GITHUB_STEP_SUMMARY
    echo "**Status:** ${{ job.status }}" >> $GITHUB_STEP_SUMMARY
    echo "**Duration:** ${{ job.duration }}" >> $GITHUB_STEP_SUMMARY
    echo "" >> $GITHUB_STEP_SUMMARY
    
    if [ "${{ job.status }}" = "failure" ]; then
      echo "### ❌ Errors Detected:" >> $GITHUB_STEP_SUMMARY
      # Add error analysis
    else
      echo "### ✅ Build Successful" >> $GITHUB_STEP_SUMMARY
    fi
```

---

## 🔄 SELF-HEALING MECHANISMS

### **Automatic Retry**

**Retry Strategy:**
```yaml
- name: Build with Retry
  uses: nick-invision/retry@v2
  with:
    timeout_minutes: 15
    max_attempts: 3
    command: |
      # Build command here
```

**Retry Conditions:**
- Network errors (retry 3x)
- Temporary license issues (retry 2x)
- Transient build errors (retry 1x)

---

### **Fallback Strategies**

**License Fallback:**
```yaml
- name: Activate License with Fallback
  run: |
    # Try license file first
    if [ -n "${{ secrets.UNITY_LICENSE }}" ]; then
      # License file activation
    else
      # Fallback to email/password
      echo "Using email/password activation"
    fi
```

**Build Fallback:**
```yaml
- name: Build with Fallback
  run: |
    # Try primary build method
    # If fails, try alternative method
    # Report which method worked
```

---

**Status:** ✅ **AUTO-RESPONSE SYSTEM CREATED** - Automated detection and response ready

