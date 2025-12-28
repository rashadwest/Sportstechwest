# Unity Build Prevention System

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** December 26, 2025  
**Purpose:** Prevent Unity build errors before they occur  
**Methodology:** AIMCODE (Systematic Prevention)

---

## 🛡️ PREVENTION LAYERS

### **Layer 1: Pre-Commit Validation**

**Workflow Validation Script:**
```bash
#!/bin/bash
# validate-unity-workflow.sh

WORKFLOW_FILE=".github/workflows/unity-webgl-build.yml"

echo "🔍 Validating Unity workflow..."

# Check YAML syntax
if ! yamllint "$WORKFLOW_FILE" 2>/dev/null; then
    echo "❌ YAML syntax error"
    exit 1
fi

# Check for duplicate parameters
if grep -c "unityVersion:" "$WORKFLOW_FILE" | grep -v "1"; then
    echo "❌ Duplicate unityVersion found"
    exit 1
fi

# Check for non-existent actions
if grep -q "game-ci/unity-setup" "$WORKFLOW_FILE"; then
    echo "❌ Non-existent action: game-ci/unity-setup"
    exit 1
fi

# Check secrets context in if conditions
if grep -q "if:.*secrets\." "$WORKFLOW_FILE"; then
    echo "⚠️ Warning: Secrets in if conditions may not work"
fi

echo "✅ Workflow validation passed"
```

**Usage:**
```bash
# Add to pre-commit hook or run manually
./scripts/validate-unity-workflow.sh
```

---

### **Layer 2: Pre-Flight Checks (In Workflow)**

**Enhanced Workflow Validation Step:**
```yaml
- name: Pre-Flight Validation
  run: |
    echo "🔍 Running pre-flight checks..."
    
    # Check required secrets
    MISSING_SECRETS=()
    for secret in UNITY_EMAIL UNITY_PASSWORD; do
      if [ -z "${{ secrets[secret] }}" ]; then
        MISSING_SECRETS+=("$secret")
      fi
    done
    
    if [ ${#MISSING_SECRETS[@]} -gt 0 ]; then
      echo "❌ Missing secrets: ${MISSING_SECRETS[*]}"
      exit 1
    fi
    
    # Validate UNITY_LICENSE format (if set)
    if [ -n "${{ secrets.UNITY_LICENSE }}" ]; then
      # Check if it's base64 (starts with valid base64 chars)
      LICENSE="${{ secrets.UNITY_LICENSE }}"
      if ! echo "$LICENSE" | grep -qE '^[A-Za-z0-9+/=]+$'; then
        echo "❌ UNITY_LICENSE is not valid base64"
        exit 1
      fi
      
      # Check if it ends with == (base64 padding)
      if ! echo "$LICENSE" | grep -qE '==$'; then
        echo "⚠️ Warning: UNITY_LICENSE may not be properly base64 encoded"
      fi
    fi
    
    # Verify project structure
    if [ ! -d "Assets" ] || [ ! -f "ProjectSettings/ProjectVersion.txt" ]; then
      echo "❌ Invalid Unity project structure"
      exit 1
    fi
    
    echo "✅ Pre-flight checks passed"
```

---

### **Layer 3: License Activation Verification**

**Enhanced License Activation Step:**
```yaml
- name: Activate Unity License
  run: |
    if [ -n "${{ secrets.UNITY_LICENSE }}" ]; then
      echo "Activating Unity license from secret..."
      mkdir -p ~/.local/share/unity3d
      
      # Decode and verify
      if echo "${{ secrets.UNITY_LICENSE }}" | base64 -d > ~/.local/share/unity3d/Unity_lic.ulf 2>/dev/null; then
        # Verify file was created and has content
        if [ -f ~/.local/share/unity3d/Unity_lic.ulf ] && [ -s ~/.local/share/unity3d/Unity_lic.ulf ]; then
          echo "✅ License file created successfully"
          echo "📊 License file size: $(wc -c < ~/.local/share/unity3d/Unity_lic.ulf) bytes"
        else
          echo "❌ License file creation failed"
          exit 1
        fi
      else
        echo "❌ Base64 decoding failed"
        exit 1
      fi
    else
      echo "⚠️ UNITY_LICENSE secret not set, using email/password activation"
    fi
```

---

### **Layer 4: Build Verification**

**Enhanced Build Verification:**
```yaml
- name: Verify Build Output
  run: |
    echo "🔍 Verifying build output..."
    
    REQUIRED_FILES=("Builds/WebGL/index.html" "Builds/WebGL/Build")
    MISSING_FILES=()
    
    for file in "${REQUIRED_FILES[@]}"; do
      if [ ! -e "$file" ]; then
        MISSING_FILES+=("$file")
      fi
    done
    
    if [ ${#MISSING_FILES[@]} -gt 0 ]; then
      echo "❌ Missing required files:"
      printf '  - %s\n' "${MISSING_FILES[@]}"
      echo ""
      echo "📋 Build directory contents:"
      ls -la Builds/WebGL/ 2>/dev/null || echo "  (directory does not exist)"
      exit 1
    fi
    
    BUILD_SIZE=$(du -sh Builds/WebGL 2>/dev/null | cut -f1)
    echo "✅ Build verified successfully"
    echo "📦 Build size: $BUILD_SIZE"
```

---

## 📋 PREVENTION CHECKLIST

### **Before Every Commit:**

- [ ] Run workflow validation script
- [ ] Check for duplicate parameters
- [ ] Verify action versions exist
- [ ] Test secrets context syntax
- [ ] Validate YAML syntax

### **Before Every Build:**

- [ ] Verify required secrets exist
- [ ] Check `UNITY_LICENSE` format (base64)
- [ ] Validate project structure
- [ ] Confirm Unity version matches
- [ ] Review workflow changes

### **After Every Failure:**

- [ ] Document error pattern
- [ ] Update prevention checklist
- [ ] Add validation if needed
- [ ] Test prevention measures
- [ ] Update documentation

---

## 🔄 AUTOMATED PREVENTION

**GitHub Actions Workflow Validation:**
- Pre-commit hook validates workflow
- CI check validates before merge
- Automated testing of workflow syntax
- Action existence verification

**Secret Validation:**
- Pre-flight checks in workflow
- Format validation (base64)
- Existence verification
- Automatic error reporting

**Build Monitoring:**
- Success rate tracking
- Error pattern detection
- Automatic alerting
- Diagnostic report generation

---

**Status:** ✅ **PREVENTION SYSTEM CREATED** - Multiple layers of defense

