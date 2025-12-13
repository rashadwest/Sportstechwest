#!/bin/bash
# n8n Restart Script
# Restarts n8n and verifies environment variables are loaded

echo "🔄 Restarting n8n..."

# Fix for "secure cookie / insecure URL / Safari" warning when running over HTTP (common on Pi/LAN)
export N8N_SECURE_COOKIE="${N8N_SECURE_COOKIE:-false}"

# Check if n8n is running
if curl -s http://localhost:5678/healthz > /dev/null 2>&1; then
    echo "✅ n8n is running locally"
    echo "⚠️  Please stop n8n manually first, then run this script again"
    echo "   Or stop it with: pkill -f n8n"
    exit 1
fi

# Start n8n
echo "🚀 Starting n8n..."
n8n start &

# Wait for n8n to start
echo "⏳ Waiting for n8n to start..."
sleep 5

# Check if it's running
if curl -s http://localhost:5678/healthz > /dev/null 2>&1; then
    echo "✅ n8n started successfully!"
    echo ""
    echo "📋 Environment variables should now be loaded"
    echo "   Check in n8n UI: Settings → Environment Variables"
else
    echo "⚠️  n8n may still be starting, or there was an issue"
    echo "   Check the n8n process: ps aux | grep n8n"
fi
