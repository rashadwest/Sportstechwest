#!/bin/bash

# Setup script for independent build monitoring
# This sets up a cron job to monitor builds outside of n8n

echo "🔧 SETTING UP BUILD MONITOR"
echo "======================================================================"
echo ""

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MONITOR_SCRIPT="$SCRIPT_DIR/monitor-builds.py"

# Check if monitor script exists
if [ ! -f "$MONITOR_SCRIPT" ]; then
    echo "❌ Error: monitor-builds.py not found at $MONITOR_SCRIPT"
    exit 1
fi

echo "📋 SETUP STEPS:"
echo "----------------------------------------------------------------------"
echo ""
echo "1. Set environment variables (add to ~/.zshrc or ~/.bashrc):"
echo ""
echo "   export GITHUB_TOKEN='your_github_token'"
echo "   export GITHUB_REPO_OWNER='your_github_username'"
echo "   export GITHUB_REPO_NAME='your_repo_name'"
echo "   export GITHUB_WORKFLOW_FILE='your_workflow_file.yml'"
echo ""
echo "   export NETLIFY_TOKEN='your_netlify_token'"
echo "   export NETLIFY_SITE_ID='your_site_id'"
echo ""
echo "   export BUILD_INTERVAL_HOURS=1  # How often builds should run"
echo ""
echo "2. Test the monitor script:"
echo "   python3 $MONITOR_SCRIPT"
echo ""
echo "3. Set up cron job (runs every hour):"
echo "   0 * * * * cd $SCRIPT_DIR && python3 monitor-builds.py >> build-monitor.log 2>&1"
echo ""
echo "   Or add to crontab:"
echo "   crontab -e"
echo "   Then add the line above"
echo ""
echo "4. Optional: Set up email alerts (if builds are missed)"
echo ""

# Check if environment variables are set
echo "🔍 CHECKING ENVIRONMENT VARIABLES:"
echo "----------------------------------------------------------------------"

if [ -z "$GITHUB_TOKEN" ]; then
    echo "   ⚠️  GITHUB_TOKEN not set"
else
    echo "   ✅ GITHUB_TOKEN is set"
fi

if [ -z "$GITHUB_REPO_OWNER" ]; then
    echo "   ⚠️  GITHUB_REPO_OWNER not set"
else
    echo "   ✅ GITHUB_REPO_OWNER is set"
fi

if [ -z "$GITHUB_REPO_NAME" ]; then
    echo "   ⚠️  GITHUB_REPO_NAME not set"
else
    echo "   ✅ GITHUB_REPO_NAME is set"
fi

if [ -z "$NETLIFY_TOKEN" ]; then
    echo "   ⚠️  NETLIFY_TOKEN not set"
else
    echo "   ✅ NETLIFY_TOKEN is set"
fi

if [ -z "$NETLIFY_SITE_ID" ]; then
    echo "   ⚠️  NETLIFY_SITE_ID not set"
else
    echo "   ✅ NETLIFY_SITE_ID is set"
fi

echo ""
echo "✅ Setup instructions displayed above"
echo "   Run this script again after setting environment variables"



