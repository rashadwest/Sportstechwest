#!/bin/bash

# Check OpenAI Spending Before Build
# Use this to verify spending is within budget before triggering builds

echo "💰 CHECKING OPENAI SPENDING BEFORE BUILD"
echo "======================================================================"
echo ""

# Get API key from environment
OPENAI_API_KEY="${OPENAI_API_KEY:-}"

if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  OPENAI_API_KEY not set"
    echo "   Set it with: export OPENAI_API_KEY='your-key'"
    exit 1
fi

# Daily spending limit (in dollars)
DAILY_LIMIT="${DAILY_SPENDING_LIMIT:-0.50}"

echo "📊 SPENDING CHECK:"
echo "----------------------------------------------------------------------"
echo "Daily limit: \$$DAILY_LIMIT"
echo ""

# Note: OpenAI API doesn't provide real-time spending via API
# So we'll check the dashboard and provide guidance
echo "ℹ️  To check current spending:"
echo "   1. Go to: https://platform.openai.com/usage"
echo "   2. Check 'Current spend' for today"
echo "   3. Compare to daily limit: \$$DAILY_LIMIT"
echo ""

# Calculate remaining budget
echo "💡 RECOMMENDATION:"
echo "   • Check OpenAI dashboard before each build"
echo "   • If spending < \$$DAILY_LIMIT → Proceed with build"
echo "   • If spending >= \$$DAILY_LIMIT → Skip build or wait"
echo ""

# Estimate cost per build
ESTIMATED_COST=0.002
echo "📈 ESTIMATED COST PER BUILD:"
echo "   ~\$$ESTIMATED_COST per build (varies by request size)"
echo ""

# Calculate builds possible with remaining budget
if [ -n "$CURRENT_SPENDING" ]; then
    REMAINING=$(echo "$DAILY_LIMIT - $CURRENT_SPENDING" | bc)
    BUILDS_POSSIBLE=$(echo "$REMAINING / $ESTIMATED_COST" | bc)
    echo "💰 REMAINING BUDGET:"
    echo "   Current spending: \$$CURRENT_SPENDING"
    echo "   Remaining: \$$REMAINING"
    echo "   Builds possible: ~$BUILDS_POSSIBLE"
    echo ""
fi

echo "✅ Spending check complete"
echo "   Proceed with build if spending is within budget"


