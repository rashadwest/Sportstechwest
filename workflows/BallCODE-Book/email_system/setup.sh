#!/bin/bash

# BallCODE Local Email System Setup Script

echo "🚀 Setting up BallCODE Local Email System..."
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python version: $python_version"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Create emails directory
mkdir -p emails
echo "✅ Created emails directory"

# Initialize database (will be created on first run)
echo "✅ Database will be created on first run"

echo ""
echo "✅ Setup complete!"
echo ""
echo "📧 To start the email server:"
echo "   python3 -m email_system.cli start"
echo ""
echo "📧 To send an email:"
echo "   python3 -m email_system.cli send --to info@ballcode.co --subject 'Test' --body 'Hello'"
echo ""
echo "📧 To list emails:"
echo "   python3 -m email_system.cli list"
echo ""



