#!/bin/bash
# Weekly Wellness Check Reminder
# Run this weekly to track system health

cd "/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book"
python3 scripts/setup-weekly-wellness-monitoring.py

echo ""
echo "✅ Weekly wellness check complete!"
echo "📄 Report: /Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/documents/WEEKLY-WELLNESS-MONITORING.md"
