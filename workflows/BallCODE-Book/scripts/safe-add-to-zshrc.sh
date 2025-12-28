#!/bin/bash
# Safe Add to ~/.zshrc
# Adds environment variables to ~/.zshrc without duplicates
# Usage: ./safe-add-to-zshrc.sh VARIABLE_NAME "value"

VARIABLE_NAME="$1"
VARIABLE_VALUE="$2"
ZSHRC_FILE="$HOME/.zshrc"

if [ -z "$VARIABLE_NAME" ] || [ -z "$VARIABLE_VALUE" ]; then
    echo "Usage: $0 VARIABLE_NAME 'value'"
    echo "Example: $0 NETLIFY_SITE_ID '39ebfb47-c716-4f38-8f8b-7bfba36f3dc7'"
    exit 1
fi

# Check if variable already exists
if grep -q "^export $VARIABLE_NAME=" "$ZSHRC_FILE" 2>/dev/null; then
    echo "⚠️  $VARIABLE_NAME already exists in ~/.zshrc"
    echo "   Current value:"
    grep "^export $VARIABLE_NAME=" "$ZSHRC_FILE" | head -1
    echo ""
    read -p "Replace it? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        # Remove old line
        sed -i.bak "/^export $VARIABLE_NAME=/d" "$ZSHRC_FILE"
        # Add new line at end
        echo "export $VARIABLE_NAME=\"$VARIABLE_VALUE\"" >> "$ZSHRC_FILE"
        echo "✅ Updated $VARIABLE_NAME in ~/.zshrc"
    else
        echo "❌ Skipped - keeping existing value"
        exit 0
    fi
else
    # Add new variable at end
    echo "" >> "$ZSHRC_FILE"
    echo "# Added by safe-add-to-zshrc.sh on $(date)" >> "$ZSHRC_FILE"
    echo "export $VARIABLE_NAME=\"$VARIABLE_VALUE\"" >> "$ZSHRC_FILE"
    echo "✅ Added $VARIABLE_NAME to ~/.zshrc"
fi

echo ""
echo "📋 To use immediately, run:"
echo "   source ~/.zshrc"
echo ""
echo "   Or open a new terminal window"

