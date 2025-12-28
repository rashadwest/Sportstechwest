#!/bin/bash
# Garvis Self-Healing System - Quick Setup Script
# Copyright © 2025 Rashad West. All Rights Reserved.

set -e

echo "🤖 Garvis Self-Healing System - Setup"
echo "======================================"
echo ""

# Check if we're in the right directory
if [ ! -f "scripts/garvis-auto-fix.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Make Python script executable
echo "📝 Making Python script executable..."
chmod +x scripts/garvis-auto-fix.py
echo "✅ Script is executable"

# Check if Python 3 is available
echo ""
echo "🐍 Checking Python 3..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Found: $PYTHON_VERSION"
else
    echo "❌ Error: Python 3 is not installed"
    echo "   Install Python 3 to use the self-healing system"
    exit 1
fi

# Check if requests library is available
echo ""
echo "📦 Checking Python dependencies..."
if python3 -c "import requests" 2>/dev/null; then
    echo "✅ requests library is available"
else
    echo "⚠️  Warning: requests library not found"
    echo "   Install with: pip3 install requests"
    echo "   Or: python3 -m pip install requests"
fi

# Check if workflow file exists
echo ""
echo "📄 Checking workflow file..."
if [ -f "n8n-garvis-self-healing-workflow.json" ]; then
    echo "✅ Workflow file found: n8n-garvis-self-healing-workflow.json"
else
    echo "❌ Error: Workflow file not found"
    exit 1
fi

# Check if error patterns file exists
echo ""
echo "📋 Checking error patterns file..."
if [ -f "scripts/garvis-error-patterns.json" ]; then
    echo "✅ Error patterns file found: scripts/garvis-error-patterns.json"
else
    echo "❌ Error: Error patterns file not found"
    exit 1
fi

# Display next steps
echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Next Steps:"
echo "1. Import workflow to n8n:"
echo "   - Open: http://192.168.1.226:5678"
echo "   - Go to: Workflows → Import from File"
echo "   - Select: n8n-garvis-self-healing-workflow.json"
echo ""
echo "2. Configure environment variables in n8n:"
echo "   - N8N_URL=http://192.168.1.226:5678"
echo "   - WORKFLOW_PATH=$(pwd)"
echo "   - N8N_API_KEY=your-api-key (optional)"
echo "   - NOTIFICATION_WEBHOOK_URL=your-webhook (optional)"
echo ""
echo "3. Activate the workflow in n8n"
echo ""
echo "📚 See: documents/GARVIS-SELF-HEALING-IMPLEMENTATION-GUIDE.md for details"
echo ""

