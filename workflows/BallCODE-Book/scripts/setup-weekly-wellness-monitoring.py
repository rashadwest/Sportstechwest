#!/usr/bin/env python3
"""
Setup Weekly Wellness Monitoring
Automates weekly wellness checks and tracking

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import subprocess
import json
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "documents"
DATA_DIR.mkdir(exist_ok=True)

WELLNESS_DATA = DATA_DIR / "system-wellness.json"
WELLNESS_HISTORY = DATA_DIR / "wellness-history.json"
MONITORING_REPORT = DOCS_DIR / "WEEKLY-WELLNESS-MONITORING.md"

def print_header(title):
    """Print formatted header."""
    print("\n" + "=" * 70)
    print(f"📊 {title}")
    print("=" * 70)

def load_wellness_history() -> List[Dict]:
    """Load wellness check history."""
    if WELLNESS_HISTORY.exists():
        with open(WELLNESS_HISTORY, 'r') as f:
            return json.load(f)
    return []

def save_wellness_history(history: List[Dict]):
    """Save wellness check history."""
    with open(WELLNESS_HISTORY, 'w') as f:
        json.dump(history, f, indent=2)

def run_wellness_check() -> Dict:
    """Run wellness check and return results."""
    print("🔍 Running wellness check...")
    subprocess.run(
        [sys.executable, PROJECT_ROOT / "scripts" / "system-wellness-check.py"],
        cwd=PROJECT_ROOT,
        check=False
    )
    
    if WELLNESS_DATA.exists():
        with open(WELLNESS_DATA, 'r') as f:
            return json.load(f)
    return {}

def analyze_trends(history: List[Dict]) -> Dict:
    """Analyze wellness trends over time."""
    if len(history) < 2:
        return {"status": "insufficient_data", "message": "Need at least 2 data points"}
    
    # Get latest scores
    scores = [h.get("overall_score", 0) for h in history[-10:]]  # Last 10 checks
    memory_usage = [h.get("memory_used_percent", 0) for h in history[-10:]]
    
    trends = {
        "score_trend": "improving" if scores[-1] > scores[0] else "declining" if scores[-1] < scores[0] else "stable",
        "score_change": scores[-1] - scores[0] if len(scores) > 1 else 0,
        "memory_trend": "improving" if memory_usage[-1] < memory_usage[0] else "declining" if memory_usage[-1] > memory_usage[0] else "stable",
        "memory_change": memory_usage[0] - memory_usage[-1] if len(memory_usage) > 1 else 0,
        "data_points": len(scores)
    }
    
    return trends

def generate_monitoring_report(history: List[Dict], trends: Dict, current: Dict) -> str:
    """Generate weekly monitoring report."""
    current_score = current.get("local_system", {})
    overall_score = sum([
        current_score.get("cpu", {}).get("score", 0),
        current_score.get("memory", {}).get("score", 0),
        current_score.get("disk", {}).get("score", 0),
        current_score.get("network", {}).get("score", 0),
        current_score.get("file_system", {}).get("score", 0),
        current_score.get("cursor_performance", {}).get("score", 0),
        current_score.get("git_performance", {}).get("score", 0)
    ]) / 7
    
    report = f"""# Weekly Wellness Monitoring Report

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** {datetime.now().strftime('%B %d, %Y')}  
**Week:** {datetime.now().strftime('%Y-W%V')}

---

## 📊 Current Status

**Overall Score:** {overall_score:.1f}/100  
**Target Score:** 90+/100  
**Gap:** {max(0, 90 - overall_score):.1f} points

### Key Metrics:
- **CPU:** {current_score.get('cpu', {}).get('score', 0):.1f}/100 ({current_score.get('cpu', {}).get('status', 'unknown')})
- **Memory:** {current_score.get('memory', {}).get('score', 0):.1f}/100 ({current_score.get('memory', {}).get('status', 'unknown')})
- **Disk:** {current_score.get('disk', {}).get('score', 0):.1f}/100 ({current_score.get('disk', {}).get('status', 'unknown')})
- **Git:** {current_score.get('git_performance', {}).get('score', 0):.1f}/100 ({current_score.get('git_performance', {}).get('status', 'unknown')})

---

## 📈 Trends Analysis

**Data Points:** {trends.get('data_points', 0)}  
**Score Trend:** {trends.get('score_trend', 'unknown')} ({trends.get('score_change', 0):+.1f} points)  
**Memory Trend:** {trends.get('memory_trend', 'unknown')} ({trends.get('memory_change', 0):+.1f}%)

"""
    
    if history:
        report += """### Historical Data (Last 10 Checks)

| Date | Score | Memory % | Status |
|------|-------|----------|--------|
"""
        for entry in history[-10:]:
            date = entry.get('timestamp', '')[:10] if entry.get('timestamp') else 'Unknown'
            score = entry.get('overall_score', 0)
            memory = entry.get('memory_used_percent', 0)
            status = "✅" if score >= 80 else "⚠️" if score >= 60 else "🔴"
            report += f"| {date} | {score:.1f} | {memory:.1f}% | {status} |\n"
    
    report += f"""
---

## 🎯 Recommendations

"""
    
    if overall_score < 90:
        gap = 90 - overall_score
        report += f"- **Target:** Improve score by {gap:.1f} points to reach 90+\n"
    
    if current_score.get('memory', {}).get('used_percent', 0) > 70:
        report += f"- **Memory:** Reduce memory usage (currently {current_score.get('memory', {}).get('used_percent', 0):.1f}%)\n"
    
    if current_score.get('git_performance', {}).get('status_time_ms', 0) > 100:
        report += f"- **Git:** Optimize git performance (currently {current_score.get('git_performance', {}).get('status_time_ms', 0):.1f}ms)\n"
    
    report += """
---

## 📅 Next Check

**Scheduled:** Next week (same day)  
**Command:** `python3 scripts/setup-weekly-wellness-monitoring.py`

---

**Generated by:** Weekly Wellness Monitoring System  
**Status:** ✅ Active

---

**Copyright © 2025 Rashad West. All Rights Reserved.**
"""
    
    return report

def setup_weekly_schedule():
    """Set up weekly wellness check schedule."""
    print_header("Setting Up Weekly Wellness Monitoring")
    
    # Run initial wellness check
    print("\n1️⃣ Running initial wellness check...")
    current = run_wellness_check()
    
    # Extract key metrics
    local_system = current.get("local_system", {})
    overall_score = sum([
        local_system.get("cpu", {}).get("score", 0),
        local_system.get("memory", {}).get("score", 0),
        local_system.get("disk", {}).get("score", 0),
        local_system.get("network", {}).get("score", 0),
        local_system.get("file_system", {}).get("score", 0),
        local_system.get("cursor_performance", {}).get("score", 0),
        local_system.get("git_performance", {}).get("score", 0)
    ]) / 7
    
    # Create history entry
    history_entry = {
        "timestamp": datetime.now().isoformat(),
        "overall_score": overall_score,
        "memory_used_percent": local_system.get("memory", {}).get("used_percent", 0),
        "cpu_usage_percent": local_system.get("cpu", {}).get("usage_percent", 0),
        "git_status_time_ms": local_system.get("git_performance", {}).get("status_time_ms", 0),
        "metrics": {
            "cpu": local_system.get("cpu", {}).get("score", 0),
            "memory": local_system.get("memory", {}).get("score", 0),
            "disk": local_system.get("disk", {}).get("score", 0),
            "network": local_system.get("network", {}).get("score", 0),
            "file_system": local_system.get("file_system", {}).get("score", 0),
            "cursor": local_system.get("cursor_performance", {}).get("score", 0),
            "git": local_system.get("git_performance", {}).get("score", 0)
        }
    }
    
    # Load and update history
    history = load_wellness_history()
    history.append(history_entry)
    
    # Keep only last 52 weeks (1 year)
    if len(history) > 52:
        history = history[-52:]
    
    save_wellness_history(history)
    
    # Analyze trends
    print("\n2️⃣ Analyzing trends...")
    trends = analyze_trends(history)
    
    # Generate report
    print("\n3️⃣ Generating monitoring report...")
    report = generate_monitoring_report(history, trends, current)
    
    with open(MONITORING_REPORT, 'w') as f:
        f.write(report)
    
    print(f"\n✅ Monitoring report saved: {MONITORING_REPORT}")
    
    # Display summary
    print_header("Monitoring Summary")
    print(f"\n📊 Current Score: {overall_score:.1f}/100")
    print(f"🎯 Target: 90+/100")
    print(f"📈 Gap: {max(0, 90 - overall_score):.1f} points")
    print(f"\n📈 Trends:")
    print(f"   Score: {trends.get('score_trend', 'unknown')} ({trends.get('score_change', 0):+.1f} points)")
    print(f"   Memory: {trends.get('memory_trend', 'unknown')} ({trends.get('memory_change', 0):+.1f}%)")
    print(f"\n📅 Next Check: Next week")
    print(f"💾 History: {len(history)} data points")
    print(f"📄 Report: {MONITORING_REPORT}")
    
    # Create reminder script
    reminder_script = PROJECT_ROOT / "scripts" / "weekly-wellness-reminder.sh"
    with open(reminder_script, 'w') as f:
        f.write(f"""#!/bin/bash
# Weekly Wellness Check Reminder
# Run this weekly to track system health

cd "{PROJECT_ROOT}"
python3 scripts/setup-weekly-wellness-monitoring.py

echo ""
echo "✅ Weekly wellness check complete!"
echo "📄 Report: {MONITORING_REPORT}"
""")
    
    reminder_script.chmod(0o755)
    print(f"\n📝 Reminder script created: {reminder_script}")
    print(f"   Run weekly: ./scripts/weekly-wellness-reminder.sh")
    
    return True

def main():
    """Main function."""
    setup_weekly_schedule()

if __name__ == "__main__":
    main()


