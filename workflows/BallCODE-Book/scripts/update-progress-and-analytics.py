#!/usr/bin/env python3
"""
Update Progress Tracking and Analytics
Combines progress tracking and analytics into unified system

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from progress_tracking_system import (
    load_progress_data, get_overall_stats, generate_progress_report
)
from analytics_system import (
    load_measurement_data, generate_analytics_report, save_analytics_data,
    analyze_student_engagement, analyze_learning_effectiveness,
    analyze_system_performance, identify_improvement_opportunities
)

def main():
    """Update both progress tracking and analytics."""
    print("=" * 60)
    print("📊 Updating Progress Tracking & Analytics")
    print("=" * 60)
    print()
    
    # Update progress tracking
    print("📈 Updating progress tracking...")
    progress_data = load_progress_data()
    stats = get_overall_stats()
    print(f"  ✅ Total students: {stats['total_students']}")
    print(f"  ✅ Active students (7d): {stats['active_students_7d']}")
    print(f"  ✅ Total books completed: {stats['total_books_completed']}")
    print(f"  ✅ Total games completed: {stats['total_games_completed']}")
    print()
    
    # Generate progress report
    progress_report = generate_progress_report()
    progress_file = Path(__file__).parent.parent / "PROGRESS-REPORT.md"
    with open(progress_file, 'w') as f:
        f.write(progress_report)
    print(f"  ✅ Progress report saved: {progress_file}")
    print()
    
    # Update analytics
    print("📊 Updating analytics...")
    measurement_data = load_measurement_data()
    
    analytics_data = {
        "engagement": analyze_student_engagement(progress_data),
        "effectiveness": analyze_learning_effectiveness(progress_data),
        "performance": analyze_system_performance(measurement_data),
        "opportunities": identify_improvement_opportunities(progress_data, measurement_data)
    }
    
    from analytics_system import save_analytics_data
    save_analytics_data(analytics_data)
    print(f"  ✅ Analytics data saved")
    print()
    
    # Generate analytics report
    analytics_report = generate_analytics_report()
    analytics_file = Path(__file__).parent.parent / "ANALYTICS-REPORT.md"
    with open(analytics_file, 'w') as f:
        f.write(analytics_report)
    print(f"  ✅ Analytics report saved: {analytics_file}")
    print()
    
    print("✅ Progress tracking and analytics updated successfully!")
    print()
    print("📋 Summary:")
    print(f"  - Progress Report: {progress_file}")
    print(f"  - Analytics Report: {analytics_file}")
    print()
    print("💡 Next Steps:")
    print("  1. Review reports to identify improvement opportunities")
    print("  2. Track more student progress to improve analytics")
    print("  3. Collect measurement data to improve performance insights")
    print()

if __name__ == "__main__":
    main()

