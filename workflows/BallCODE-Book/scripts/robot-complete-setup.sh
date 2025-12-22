#!/bin/bash
# Robot: Complete n8n Setup Automation
# Sets environment variables and tests everything

set -e

N8N_URL="http://192.168.1.226:5678"
N8N_HOST="192.168.1.226"

echo "======================================================================"
echo "🤖 Robot: Complete n8n Setup Automation"
echo "======================================================================"
echo ""

# Step 1: Create environment variables file for Pi
echo "📝 Step 1: Creating environment variables file..."
cat > /tmp/n8n-env-vars.txt << 'EOF'
# n8n Environment Variables
# Set these in n8n UI: Settings → Environment Variables

GITHUB_REPO_OWNER=rashadwest
GITHUB_REPO_NAME=BTEBallCODE
GITHUB_WORKFLOW_FILE=unity-webgl-build.yml
NETLIFY_SITE_ID=[SET_YOUR_NETLIFY_SITE_ID]
NETLIFY_SITE_NAME=ballcode-game
N8N_INSTANCE_ROLE=prod
WORKFLOW_PATH=/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book
EOF

echo "✅ Created: /tmp/n8n-env-vars.txt"
echo ""

# Step 2: Create setup script for Pi
echo "📝 Step 2: Creating Pi setup script..."
cat > scripts/setup-env-vars-on-pi.sh << 'EOFSCRIPT'
#!/bin/bash
# Run this on the Pi to set n8n environment variables

echo "🤖 Setting up n8n environment variables on Pi..."

# Check if n8n is running as service
if systemctl list-unit-files | grep -q n8n.service; then
    echo "📋 n8n is running as a service"
    echo ""
    echo "To set environment variables:"
    echo "1. Edit service file:"
    echo "   sudo nano /etc/systemd/system/n8n.service"
    echo ""
    echo "2. Add in [Service] section:"
    echo "   Environment=\"GITHUB_REPO_OWNER=rashadwest\""
    echo "   Environment=\"GITHUB_REPO_NAME=BTEBallCODE\""
    echo "   Environment=\"GITHUB_WORKFLOW_FILE=unity-webgl-build.yml\""
    echo "   Environment=\"NETLIFY_SITE_NAME=ballcode-game\""
    echo "   Environment=\"N8N_INSTANCE_ROLE=prod\""
    echo ""
    echo "3. Reload and restart:"
    echo "   sudo systemctl daemon-reload"
    echo "   sudo systemctl restart n8n"
else
    echo "📋 n8n is running manually or via PM2"
    echo ""
    echo "Set environment variables in n8n UI:"
    echo "1. Open: http://192.168.1.226:5678"
    echo "2. Settings → Environment Variables"
    echo "3. Add each variable from n8n-env-vars.txt"
fi
EOFSCRIPT

chmod +x scripts/setup-env-vars-on-pi.sh
echo "✅ Created: scripts/setup-env-vars-on-pi.sh"
echo ""

# Step 3: Test connectivity
echo "🔍 Step 3: Testing n8n connectivity..."
if curl -s "${N8N_URL}/healthz" > /dev/null 2>&1; then
    echo "✅ n8n is accessible"
else
    echo "❌ Cannot connect to n8n"
    exit 1
fi
echo ""

# Step 4: Run comprehensive tests
echo "🧪 Step 4: Running comprehensive tests..."
python3 scripts/robot-setup-n8n.py
echo ""

# Step 5: Summary
echo "======================================================================"
echo "✅ Robot Setup Complete!"
echo "======================================================================"
echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Set environment variables in n8n:"
echo "   - Open: ${N8N_URL}"
echo "   - Settings → Environment Variables"
echo "   - Copy variables from: /tmp/n8n-env-vars.txt"
echo ""
echo "2. Activate Full Integration workflow:"
echo "   - Open workflow in n8n"
echo "   - Click 'Active' toggle"
echo "   - Save"
echo ""
echo "3. Restart n8n (on Pi):"
echo "   ssh pi@${N8N_HOST}"
echo "   sudo systemctl restart n8n"
echo ""
echo "4. Re-run tests:"
echo "   python3 scripts/robot-setup-n8n.py"
echo ""

