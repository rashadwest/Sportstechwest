#!/bin/bash

# Quick script to help check for missed builds
# Run this to see expected schedule and what to check

echo "🔍 BUILD CHECK HELPER"
echo "======================================================================"
echo ""

# Get current time
NOW=$(date '+%Y-%m-%d %H:%M:%S')
echo "Current time: $NOW"
echo ""

echo "📅 EXPECTED SCHEDULE (If Hourly):"
echo "----------------------------------------------------------------------"
echo "Should run every hour at :00 minutes"
echo "Last 24 hours should have 24 executions"
echo ""

echo "📋 QUICK CHECK STEPS:"
echo "----------------------------------------------------------------------"
echo ""
echo "1. n8n Workflow Executions:"
echo "   - Open n8n UI → Your workflow → Executions tab"
echo "   - Check if executions are running hourly"
echo "   - Look for green checkmarks (success) or red X (failed)"
echo ""
echo "2. GitHub Actions Builds:"
echo "   - Open GitHub → Your repo → Actions tab"
echo "   - Check if builds are being triggered"
echo "   - Look for recent workflow runs"
echo ""
echo "3. Netlify Deployments:"
echo "   - Open Netlify → Your site → Deploys tab"
echo "   - Check if deployments are happening"
echo "   - Look for 'Published' status"
echo ""
echo "✅ If all three show recent activity → No missed builds"
echo "❌ If any are missing → Build was missed"
echo ""



