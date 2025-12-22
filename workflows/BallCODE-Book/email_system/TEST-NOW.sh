#!/bin/bash

# Quick Test Script - Run this to test the email system

echo "🚀 Testing BallCODE Email System..."
echo ""

cd "$(dirname "$0")"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check if dependencies are installed
echo "📦 Checking dependencies..."
if ! python3 -c "import aiosmtpd" 2>/dev/null; then
    echo "⚠️  Installing dependencies..."
    pip3 install aiosmtpd click
else
    echo "✅ Dependencies installed"
fi

echo ""
echo "🧪 Running quick test..."
echo ""

# Run quick test
python3 quick_start.py

echo ""
echo "✅ Test complete!"
echo ""
echo "📧 To start the server:"
echo "   cd email_system"
echo "   python3 main.py start"
echo ""


