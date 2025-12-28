#!/bin/bash

# Automated Email System Setup - One Command
# Run this to set up everything automatically

echo "🚀 Starting Automated Email System Setup..."
echo ""

cd "$(dirname "$0")"

python3 automated_setup.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "📧 Next steps:"
echo "   1. Start server: python3 main.py start"
echo "   2. Send email: python3 main.py send --to EMAIL --subject 'SUBJECT' --body 'BODY'"
echo "   3. Check emails: python3 main.py list"
echo ""



