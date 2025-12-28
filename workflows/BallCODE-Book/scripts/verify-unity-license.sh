#!/bin/bash
# Verify Unity License Status - AIMCODE Automated Solution
# Checks license file location, format, and activation status

echo "============================================================"
echo "  Unity License Verification - AIMCODE Automated Check"
echo "============================================================"

# Check license file locations
echo ""
echo "📋 Checking license file locations..."

LICENSE_LOCATIONS=(
    "/Library/Application Support/Unity/Unity_lic.ulf"
    "$HOME/Library/Application Support/Unity/Unity_lic.ulf"
    "$HOME/Desktop/Unity_v2021.x.ulf"
    "$HOME/Downloads/Unity_v2021.x.ulf"
)

FOUND_LICENSE=""
for location in "${LICENSE_LOCATIONS[@]}"; do
    if [ -f "$location" ]; then
        echo "✅ Found: $location"
        FOUND_LICENSE="$location"
        ls -lh "$location"
    fi
done

if [ -z "$FOUND_LICENSE" ]; then
    echo "❌ No license file found in standard locations"
    exit 1
fi

# Check license file format
echo ""
echo "📋 Checking license file format..."

if grep -q "UnityPersonal\|Personal" "$FOUND_LICENSE" 2>/dev/null; then
    echo "✅ License type: Unity Personal"
elif grep -q "UnityPro\|Pro" "$FOUND_LICENSE" 2>/dev/null; then
    echo "✅ License type: Unity Pro"
else
    echo "⚠️  License type: Unknown"
fi

# Extract serial number if available
SERIAL=$(grep -i "SerialMasked\|Serial" "$FOUND_LICENSE" 2>/dev/null | head -1 | sed 's/.*Value="\([^"]*\)".*/\1/' || echo "")
if [ -n "$SERIAL" ]; then
    echo "✅ Serial found: $SERIAL"
else
    echo "⚠️  No serial number found in license file"
fi

# Check Unity Hub license status
echo ""
echo "📋 Checking Unity Hub license status..."

# Try to get license info from Unity Hub (if accessible)
if [ -d "/Applications/Unity Hub.app" ]; then
    echo "✅ Unity Hub installed"
    echo "   Please check: Unity Hub → Settings → Licenses"
else
    echo "⚠️  Unity Hub not found"
fi

# Check if license is in system location (required for Unity to use it)
SYSTEM_LICENSE="/Library/Application Support/Unity/Unity_lic.ulf"
if [ -f "$SYSTEM_LICENSE" ]; then
    echo "✅ License file in system location (required)"
else
    echo "⚠️  License file NOT in system location"
    echo "   Copying to system location..."
    sudo cp "$FOUND_LICENSE" "$SYSTEM_LICENSE" 2>/dev/null || {
        echo "   ⚠️  Could not copy to system location (may need sudo)"
        echo "   Manual step: Copy $FOUND_LICENSE to $SYSTEM_LICENSE"
    }
fi

# Check Unity Editor can access license
echo ""
echo "📋 Testing Unity Editor license access..."

UNITY_PATH="/Applications/Unity/Hub/Editor/2021.3.45f2/Unity.app/Contents/MacOS/Unity"
if [ -f "$UNITY_PATH" ]; then
    echo "✅ Unity Editor found: $UNITY_PATH"
    echo "   Testing license access..."
    
    # Run Unity in batch mode to check license
    "$UNITY_PATH" -batchmode -quit -projectPath /tmp -logfile /tmp/unity-license-check.log 2>&1 | grep -i "license\|entitlement" | head -5 || echo "   Check log: /tmp/unity-license-check.log"
else
    echo "⚠️  Unity Editor not found at expected location"
fi

# Summary
echo ""
echo "============================================================"
echo "  Summary"
echo "============================================================"
echo "License file: $FOUND_LICENSE"
echo "System location: $([ -f "$SYSTEM_LICENSE" ] && echo "✅ Present" || echo "❌ Missing")"
echo "Serial: ${SERIAL:-Not found}"
echo ""
echo "Next steps:"
echo "1. Check Unity Hub → Settings → Licenses"
echo "2. If license not showing, restart Unity Hub"
echo "3. If still not working, license file may need different format"
echo ""


