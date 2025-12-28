#!/bin/bash
# Unity Workflow Validation Script
# Prevents common workflow errors before commit

set -e

WORKFLOW_FILE=".github/workflows/unity-webgl-build.yml"
ERRORS=0
WARNINGS=0

echo "🔍 Validating Unity workflow: $WORKFLOW_FILE"
echo ""

# Check if workflow file exists
if [ ! -f "$WORKFLOW_FILE" ]; then
    echo "❌ Workflow file not found: $WORKFLOW_FILE"
    exit 1
fi

# Check YAML syntax (if yamllint available)
if command -v yamllint &> /dev/null; then
    if ! yamllint "$WORKFLOW_FILE" > /dev/null 2>&1; then
        echo "❌ YAML syntax error detected"
        yamllint "$WORKFLOW_FILE"
        ((ERRORS++))
    else
        echo "✅ YAML syntax valid"
    fi
else
    echo "⚠️  yamllint not installed (optional check skipped)"
fi

# Check for duplicate unityVersion
UNITY_VERSION_COUNT=$(grep -c "unityVersion:" "$WORKFLOW_FILE" || echo "0")
if [ "$UNITY_VERSION_COUNT" -gt 1 ]; then
    echo "❌ Duplicate unityVersion found ($UNITY_VERSION_COUNT times)"
    grep -n "unityVersion:" "$WORKFLOW_FILE"
    ((ERRORS++))
else
    echo "✅ No duplicate unityVersion"
fi

# Check for non-existent actions
if grep -q "game-ci/unity-setup" "$WORKFLOW_FILE"; then
    echo "❌ Non-existent action found: game-ci/unity-setup"
    echo "   This action doesn't exist. Use game-ci/unity-builder@v4 with unityVersion instead."
    ((ERRORS++))
else
    echo "✅ No deprecated actions found"
fi

# Check for secrets in if conditions (warning only)
if grep -qE "if:\s*secrets\." "$WORKFLOW_FILE"; then
    echo "⚠️  Warning: Secrets used in if conditions (may not work)"
    echo "   Use: if [ -n \"\${{ secrets.NAME }}\" ] inside run scripts instead"
    grep -n "if:.*secrets\." "$WORKFLOW_FILE"
    ((WARNINGS++))
else
    echo "✅ No secrets in if conditions"
fi

# Check for required secrets in workflow
REQUIRED_SECRETS=("UNITY_EMAIL" "UNITY_PASSWORD")
for secret in "${REQUIRED_SECRETS[@]}"; do
    if ! grep -q "secrets.$secret" "$WORKFLOW_FILE"; then
        echo "⚠️  Warning: $secret secret not referenced in workflow"
        ((WARNINGS++))
    fi
done

# Summary
echo ""
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo "✅ Workflow validation passed!"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo "⚠️  Validation passed with $WARNINGS warning(s)"
    exit 0
else
    echo "❌ Validation failed with $ERRORS error(s) and $WARNINGS warning(s)"
    exit 1
fi

