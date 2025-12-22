#!/bin/bash

# Deploy Build Monitor - Complete Setup
# This script sets up the independent build monitoring system

echo "🚀 DEPLOYING BUILD MONITOR"
echo "======================================================================"
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 not found"
    exit 1
fi

# Check if requests module is installed
if ! python3 -c "import requests" 2>/dev/null; then
    echo "⚠️  Installing requests module..."
    pip3 install requests
    if [ $? -ne 0 ]; then
        echo "❌ Error: Failed to install requests module"
        exit 1
    fi
fi

echo "✅ Python 3 and requests module ready"
echo ""

# Check environment variables
echo "🔍 CHECKING ENVIRONMENT VARIABLES:"
echo "----------------------------------------------------------------------"

MISSING_VARS=0

if [ -z "$GITHUB_TOKEN" ]; then
    echo "   ⚠️  GITHUB_TOKEN not set"
    MISSING_VARS=1
else
    echo "   ✅ GITHUB_TOKEN is set"
fi

if [ -z "$GITHUB_REPO_OWNER" ]; then
    echo "   ⚠️  GITHUB_REPO_OWNER not set"
    MISSING_VARS=1
else
    echo "   ✅ GITHUB_REPO_OWNER is set"
fi

if [ -z "$GITHUB_REPO_NAME" ]; then
    echo "   ⚠️  GITHUB_REPO_NAME not set"
    MISSING_VARS=1
else
    echo "   ✅ GITHUB_REPO_NAME is set"
fi

if [ -z "$GITHUB_WORKFLOW_FILE" ]; then
    echo "   ⚠️  GITHUB_WORKFLOW_FILE not set"
    MISSING_VARS=1
else
    echo "   ✅ GITHUB_WORKFLOW_FILE is set"
fi

# Support both token env var names used across the repo.
# Prefer NETLIFY_AUTH_TOKEN; fall back to NETLIFY_TOKEN.
if [ -z "$NETLIFY_AUTH_TOKEN" ] && [ -z "$NETLIFY_TOKEN" ]; then
    echo "   ⚠️  NETLIFY_AUTH_TOKEN (or NETLIFY_TOKEN) not set"
    MISSING_VARS=1
else
    if [ -n "$NETLIFY_AUTH_TOKEN" ]; then
        export NETLIFY_TOKEN="$NETLIFY_AUTH_TOKEN"
        echo "   ✅ NETLIFY_AUTH_TOKEN is set (using as NETLIFY_TOKEN)"
    else
        echo "   ✅ NETLIFY_TOKEN is set"
    fi
fi

if [ -z "$NETLIFY_SITE_ID" ]; then
    echo "   ⚠️  NETLIFY_SITE_ID not set"
    MISSING_VARS=1
else
    echo "   ✅ NETLIFY_SITE_ID is set"
fi

if [ -z "$BUILD_INTERVAL_HOURS" ]; then
    echo "   ⚠️  BUILD_INTERVAL_HOURS not set (defaulting to 1)"
    export BUILD_INTERVAL_HOURS=1
else
    echo "   ✅ BUILD_INTERVAL_HOURS is set to $BUILD_INTERVAL_HOURS"
fi

echo ""

if [ $MISSING_VARS -eq 1 ]; then
    echo "❌ Missing required environment variables"
    echo ""
    echo "📋 SETUP REQUIRED:"
    echo "----------------------------------------------------------------------"
    echo "Add these to ~/.zshrc (or ~/.bashrc):"
    echo ""
    echo "export GITHUB_TOKEN='your_github_token'"
    echo "export GITHUB_REPO_OWNER='your_github_username'"
    echo "export GITHUB_REPO_NAME='your_repo_name'"
    echo "export GITHUB_WORKFLOW_FILE='your_workflow_file.yml'"
    echo ""
    echo "export NETLIFY_AUTH_TOKEN='your_netlify_token'  # preferred"
    echo "# or (legacy) export NETLIFY_TOKEN='your_netlify_token'"
    echo "export NETLIFY_SITE_ID='your_netlify_site_id'"
    echo ""
    echo "export BUILD_INTERVAL_HOURS=1"
    echo ""
    echo "Then run: source ~/.zshrc"
    echo "Then run this script again"
    exit 1
fi

# Test the monitor script
echo "🧪 TESTING MONITOR SCRIPT:"
echo "----------------------------------------------------------------------"
cd "$PROJECT_DIR"
python3 "$SCRIPT_DIR/monitor-builds.py"
TEST_RESULT=$?

if [ $TEST_RESULT -eq 0 ] || [ $TEST_RESULT -eq 1 ]; then
    echo ""
    echo "✅ Monitor script works! (Exit code $TEST_RESULT)"
    if [ $TEST_RESULT -eq 1 ]; then
        echo "   ⚠️  Missed builds detected (this is expected on first run)"
    fi
else
    echo ""
    echo "❌ Monitor script failed (Exit code $TEST_RESULT)"
    exit 1
fi

echo ""

# Set up cron job
echo "⏰ SETTING UP CRON JOB:"
echo "----------------------------------------------------------------------"

CRON_CMD="0 * * * * cd $PROJECT_DIR && /usr/bin/python3 $SCRIPT_DIR/monitor-builds.py >> $PROJECT_DIR/build-monitor.log 2>&1"

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "monitor-builds.py"; then
    echo "   ⚠️  Cron job already exists"
    echo "   Current cron jobs:"
    crontab -l 2>/dev/null | grep "monitor-builds.py"
    echo ""
    read -p "   Replace existing cron job? (y/n): " REPLACE
    if [ "$REPLACE" = "y" ]; then
        # Remove existing cron job
        crontab -l 2>/dev/null | grep -v "monitor-builds.py" | crontab -
        # Add new cron job
        (crontab -l 2>/dev/null; echo "$CRON_CMD") | crontab -
        echo "   ✅ Cron job updated"
    else
        echo "   ℹ️  Keeping existing cron job"
    fi
else
    # Add new cron job
    (crontab -l 2>/dev/null; echo "$CRON_CMD") | crontab -
    echo "   ✅ Cron job added"
fi

echo ""
echo "📋 CRON JOB DETAILS:"
echo "   Runs: Every hour at :00 minutes"
echo "   Command: $CRON_CMD"
echo "   Log file: $PROJECT_DIR/build-monitor.log"
echo ""

# Create log file
touch "$PROJECT_DIR/build-monitor.log"
echo "✅ Log file created: $PROJECT_DIR/build-monitor.log"

echo ""
echo "======================================================================"
echo "✅ DEPLOYMENT COMPLETE!"
echo "======================================================================"
echo ""
echo "📊 MONITORING IS NOW ACTIVE:"
echo "   • Runs automatically every hour"
echo "   • Checks GitHub Actions builds"
echo "   • Checks Netlify deployments"
echo "   • Detects missed builds"
echo ""
echo "📋 USEFUL COMMANDS:"
echo "   • View logs: tail -f $PROJECT_DIR/build-monitor.log"
echo "   • Run manually: python3 $SCRIPT_DIR/monitor-builds.py"
echo "   • View report: cat build-monitor-report.txt"
echo "   • Check cron: crontab -l"
echo ""
echo "🎯 NEXT STEPS:"
echo "   1. Wait for first automated run (next hour)"
echo "   2. Check logs: tail -f $PROJECT_DIR/build-monitor.log"
echo "   3. Review report: cat build-monitor-report.txt"
echo ""

