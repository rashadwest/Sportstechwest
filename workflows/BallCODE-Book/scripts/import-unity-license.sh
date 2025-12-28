#!/bin/bash
# Import Unity License File (.ulf) - Mac Best Practices
# Based on Unity official documentation

echo "============================================================"
echo "  Import Unity License File"
echo "============================================================"

# Unity Editor path (2021.3.45f2)
UNITY_PATH="/Applications/Unity/Hub/Editor/2021.3.45f2/Unity.app/Contents/MacOS/Unity"

# License file path (check common locations)
LICENSE_FILE=""
if [ -f ~/Desktop/Unity_v2021.x.ulf ]; then
    LICENSE_FILE=~/Desktop/Unity_v2021.x.ulf
elif [ -f ~/Downloads/Unity_v2021.x.ulf ]; then
    LICENSE_FILE=~/Downloads/Unity_v2021.x.ulf
else
    # Try to find any .ulf file
    LICENSE_FILE=$(find ~/Desktop ~/Downloads -name "*.ulf" -type f 2>/dev/null | head -1)
fi

# Check if Unity Editor exists
if [ ! -f "$UNITY_PATH" ]; then
    echo "❌ Unity Editor not found at: $UNITY_PATH"
    echo "   Please install Unity 2021.3.45f2 in Unity Hub"
    exit 1
fi

# Check if license file exists
if [ -z "$LICENSE_FILE" ] || [ ! -f "$LICENSE_FILE" ]; then
    echo "❌ License file not found!"
    echo "   Please download the .ulf file and place it on Desktop or in Downloads"
    echo "   Or specify the path: $0 <path-to-ulf-file>"
    exit 1
fi

echo "✅ Found Unity Editor: $UNITY_PATH"
echo "✅ Found license file: $LICENSE_FILE"
echo ""
echo "📝 Activating license..."

# Activate license using Unity's recommended method
# -batchmode: Run without GUI
# -manualLicenseFile: Import the license file
# -quit: Exit after activation
# -logfile: Save log for troubleshooting

"$UNITY_PATH" \
    -batchmode \
    -manualLicenseFile "$LICENSE_FILE" \
    -quit \
    -logfile ~/Library/Logs/Unity/import-license.log

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ License activated successfully!"
    echo ""
    echo "Next steps:"
    echo "1. Open Unity Hub"
    echo "2. Check Settings → Licenses"
    echo "3. Verify your license is active"
    echo ""
    echo "Log file: ~/Library/Logs/Unity/import-license.log"
else
    echo ""
    echo "❌ License activation failed"
    echo "   Check log file: ~/Library/Logs/Unity/import-license.log"
    exit 1
fi


