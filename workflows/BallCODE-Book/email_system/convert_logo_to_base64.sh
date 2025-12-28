#!/bin/bash

# Convert BallCODE logo to base64 for email signature embedding

echo "🖼️  BallCODE Logo to Base64 Converter"
echo ""

# Check if logo file exists
LOGO_FILE="assets/images/ballcode-logo.png"

if [ ! -f "$LOGO_FILE" ]; then
    echo "❌ Logo file not found: $LOGO_FILE"
    echo ""
    echo "📋 To use this script:"
    echo "1. Place your BallCODE logo PNG file at: $LOGO_FILE"
    echo "2. Run this script again"
    echo ""
    exit 1
fi

echo "✅ Found logo: $LOGO_FILE"
echo ""
echo "🔄 Converting to base64..."
echo ""

# Convert to base64
BASE64_OUTPUT=$(base64 -i "$LOGO_FILE" 2>/dev/null || base64 "$LOGO_FILE" 2>/dev/null)

if [ -z "$BASE64_OUTPUT" ]; then
    echo "❌ Error: Could not convert logo to base64"
    echo "   Make sure 'base64' command is available"
    exit 1
fi

# Save to file
echo "$BASE64_OUTPUT" > assets/images/logo_base64.txt

echo "✅ Conversion complete!"
echo ""
echo "📁 Base64 saved to: assets/images/logo_base64.txt"
echo ""
echo "📋 Next steps:"
echo "1. Open: signature_base64.html"
echo "2. Replace 'BASE64_LOGO_HERE' with the base64 string from logo_base64.txt"
echo "3. Copy the updated signature to your email client"
echo ""
echo "💡 Tip: The base64 string is very long. Copy the entire contents of logo_base64.txt"
echo ""



