#!/bin/bash
# Automated n8n Environment Variables Setup
# Run this on the Pi where n8n is running

echo "🤖 Setting up n8n environment variables..."

# Check if n8n service exists
if systemctl list-unit-files | grep -q n8n.service; then
    echo "📋 n8n is running as a service"
    echo ""
    echo "To set environment variables:"
    echo "1. Edit n8n service file:"
    echo "   sudo nano /etc/systemd/system/n8n.service"
    echo ""
    echo "2. Add Environment variables in [Service] section:"
    echo "   [Service]"
    echo "   Environment="GITHUB_REPO_OWNER=rashadwest""
    echo "   Environment="GITHUB_REPO_NAME=BTEBallCODE""
    echo "   Environment="GITHUB_WORKFLOW_FILE=unity-webgl-build.yml""
    echo "   Environment="NETLIFY_SITE_NAME=ballcode-game""
    echo "   Environment="N8N_INSTANCE_ROLE=prod""
    echo ""
    echo "3. Reload and restart:"
    echo "   sudo systemctl daemon-reload"
    echo "   sudo systemctl restart n8n"
else
    echo "📋 n8n is running manually"
    echo ""
    echo "Set environment variables in n8n UI:"
    echo "1. Open: http://192.168.1.226:5678"
    echo "2. Settings → Environment Variables"
    echo "3. Add each variable"
fi

echo ""
echo "✅ Setup instructions complete"
