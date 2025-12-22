#!/usr/bin/env python3
"""
BallCODE Analytics System
Analyzes progress data and measurement data to provide insights

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from collections import defaultdict
import statistics

PROJECT_ROOT = Path(__file__).parent.parent
PROGRESS_DATA_FILE = PROJECT_ROOT / "progress-data.json"
MEASUREMENT_DATA_FILE = PROJECT_ROOT / "measurement-data.json"
ANALYTICS_DATA_FILE = PROJECT_ROOT / "analytics-data.json"

def load_progress_data() -> Dict:
    """Load progress tracking data."""
    if PROGRESS_DATA_FILE.exists():
        with open(PROGRESS_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def load_measurement_data() -> Dict:
    """Load measurement data."""
    if MEASUREMENT_DATA_FILE.exists():
        with open(MEASUREMENT_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_analytics_data(data: Dict):
    """Save analytics data."""
    data["last_updated"] = datetime.now().isoformat()
    with open(ANALYTICS_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def analyze_student_engagement(progress_data: Dict) -> Dict:
    """Analyze student engagement patterns."""
    students = progress_data.get("students", {})
    
    if not students:
        return {"status": "no_data", "message": "No student data available"}
    
    # Calculate engagement metrics
    total_students = len(students)
    active_last_7d = 0
    active_last_30d = 0
    completion_rates = []
    time_to_completion = []
    
    now = datetime.now()
    
    for student_id, student_data in students.items():
        last_active = datetime.fromisoformat(student_data.get("last_active", "2000-01-01"))
        
        if (now - last_active).days <= 7:
            active_last_7d += 1
        if (now - last_active).days <= 30:
            active_last_30d += 1
        
        # Calculate completion rate
        books_completed = len(student_data.get("books_completed", []))
        games_completed = len(student_data.get("games_completed", []))
        total_activities = books_completed + games_completed
        completion_rates.append(total_activities)
    
    return {
        "total_students": total_students,
        "active_7d": active_last_7d,
        "active_30d": active_last_30d,
        "retention_7d": (active_last_7d / total_students * 100) if total_students > 0 else 0,
        "retention_30d": (active_last_30d / total_students * 100) if total_students > 0 else 0,
        "avg_completions_per_student": statistics.mean(completion_rates) if completion_rates else 0,
        "median_completions_per_student": statistics.median(completion_rates) if completion_rates else 0
    }

def analyze_learning_effectiveness(progress_data: Dict) -> Dict:
    """Analyze learning effectiveness metrics."""
    students = progress_data.get("students", {})
    
    if not students:
        return {"status": "no_data", "message": "No student data available"}
    
    # Analyze mastery progression
    concept_mastery = defaultdict(list)
    book_completion_by_concept = defaultdict(int)
    game_scores_by_level = defaultdict(list)
    
    for student_id, student_data in students.items():
        # Track curriculum mastery
        for mastery in student_data.get("curriculum_mastered", []):
            concept_id = mastery.get("concept_id")
            mastery_level = mastery.get("mastery_level", 0)
            concept_mastery[concept_id].append(mastery_level)
        
        # Track game performance
        for game in student_data.get("games_completed", []):
            level_id = game.get("level_id")
            score = game.get("score", 0)
            game_scores_by_level[level_id].append(score)
    
    # Calculate effectiveness metrics
    avg_mastery_by_concept = {
        concept: statistics.mean(levels) if levels else 0
        for concept, levels in concept_mastery.items()
    }
    
    avg_score_by_level = {
        level: statistics.mean(scores) if scores else 0
        for level, scores in game_scores_by_level.items()
    }
    
    return {
        "concepts_being_learned": len(concept_mastery),
        "avg_mastery_by_concept": avg_mastery_by_concept,
        "levels_being_played": len(game_scores_by_level),
        "avg_score_by_level": avg_score_by_level,
        "overall_effectiveness_score": statistics.mean(list(avg_mastery_by_concept.values())) * 100 if avg_mastery_by_concept else 0
    }

def analyze_system_performance(measurement_data: Dict) -> Dict:
    """Analyze system performance from measurement data."""
    efficiency = measurement_data.get("efficiency", {})
    
    if not efficiency:
        return {"status": "no_data", "message": "No measurement data available"}
    
    # Analyze page load times
    page_loads = efficiency.get("page_load_times", {})
    avg_page_load = statistics.mean([v for v in page_loads.values() if isinstance(v, (int, float))]) if page_loads else 0
    
    # Analyze game performance
    game_perf = efficiency.get("game_performance", {})
    avg_frame_rate = game_perf.get("frame_rate", 0)
    avg_load_time = game_perf.get("load_time", 0)
    
    # Analyze integration flow
    integration = efficiency.get("integration_flow", {})
    success_rate = integration.get("success_rate", 0)
    error_rate = integration.get("error_rate", 0)
    
    # Analyze user engagement
    engagement = efficiency.get("user_engagement", {})
    avg_session_time = engagement.get("avg_session_time", 0)
    pages_per_session = engagement.get("pages_per_session", 0)
    
    return {
        "avg_page_load_time": avg_page_load,
        "avg_frame_rate": avg_frame_rate,
        "avg_game_load_time": avg_load_time,
        "integration_success_rate": success_rate,
        "integration_error_rate": error_rate,
        "avg_session_time": avg_session_time,
        "avg_pages_per_session": pages_per_session,
        "performance_score": calculate_performance_score(avg_page_load, avg_frame_rate, success_rate)
    }

def calculate_performance_score(page_load: float, frame_rate: float, success_rate: float) -> float:
    """Calculate overall performance score (0-100)."""
    # Page load score (target: <3s, max score at 1s)
    page_score = max(0, 100 - (page_load - 1) * 20) if page_load > 1 else 100
    
    # Frame rate score (target: 60fps)
    frame_score = min(100, (frame_rate / 60) * 100) if frame_rate > 0 else 0
    
    # Success rate score
    success_score = success_rate if success_rate > 0 else 0
    
    # Weighted average
    return (page_score * 0.3 + frame_score * 0.3 + success_score * 0.4)

def identify_improvement_opportunities(progress_data: Dict, measurement_data: Dict) -> List[Dict]:
    """Identify areas for system improvement."""
    opportunities = []
    
    # Analyze progress data
    students = progress_data.get("students", {})
    if students:
        # Check completion rates
        avg_completions = statistics.mean([
            len(s.get("books_completed", [])) + len(s.get("games_completed", []))
            for s in students.values()
        ]) if students else 0
        
        if avg_completions < 2:
            opportunities.append({
                "area": "Student Engagement",
                "issue": "Low completion rate",
                "metric": f"Avg {avg_completions:.1f} completions per student",
                "recommendation": "Improve onboarding and make first completion easier",
                "priority": "high"
            })
        
        # Check retention
        now = datetime.now()
        active_7d = sum(1 for s in students.values() 
                       if (now - datetime.fromisoformat(s.get("last_active", "2000-01-01"))).days <= 7)
        retention_rate = (active_7d / len(students) * 100) if students else 0
        
        if retention_rate < 50:
            opportunities.append({
                "area": "User Retention",
                "issue": "Low 7-day retention",
                "metric": f"{retention_rate:.1f}% retention",
                "recommendation": "Add reminders, gamification, or progress tracking",
                "priority": "high"
            })
    
    # Analyze measurement data
    efficiency = measurement_data.get("efficiency", {})
    page_loads = efficiency.get("page_load_times", {})
    
    for page, load_time in page_loads.items():
        if isinstance(load_time, (int, float)) and load_time > 3.0:
            opportunities.append({
                "area": "Performance",
                "issue": f"Slow page load: {page}",
                "metric": f"{load_time:.2f}s load time",
                "recommendation": "Optimize page assets, enable caching, or reduce content",
                "priority": "medium"
            })
    
    integration = efficiency.get("integration_flow", {})
    error_rate = integration.get("error_rate", 0)
    
    if error_rate > 5:
        opportunities.append({
            "area": "Integration",
            "issue": "High error rate",
            "metric": f"{error_rate:.1f}% error rate",
            "recommendation": "Review error logs, improve error handling, add retry logic",
            "priority": "high"
        })
    
    return opportunities

def generate_analytics_report() -> str:
    """Generate comprehensive analytics report."""
    progress_data = load_progress_data()
    measurement_data = load_measurement_data()
    
    engagement = analyze_student_engagement(progress_data)
    effectiveness = analyze_learning_effectiveness(progress_data)
    performance = analyze_system_performance(measurement_data)
    opportunities = identify_improvement_opportunities(progress_data, measurement_data)
    
    report = f"""
# 📈 BallCODE Analytics Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🎯 Student Engagement

"""
    
    if engagement.get("status") == "no_data":
        report += "⚠️ No student data available yet. Start tracking progress to see engagement metrics.\n\n"
    else:
        report += f"""
- **Total Students:** {engagement['total_students']}
- **Active (7 days):** {engagement['active_7d']} ({engagement['retention_7d']:.1f}% retention)
- **Active (30 days):** {engagement['active_30d']} ({engagement['retention_30d']:.1f}% retention)
- **Avg Completions/Student:** {engagement['avg_completions_per_student']:.2f}
- **Median Completions/Student:** {engagement['median_completions_per_student']:.2f}

"""
    
    report += "## 📚 Learning Effectiveness\n\n"
    
    if effectiveness.get("status") == "no_data":
        report += "⚠️ No learning data available yet.\n\n"
    else:
        report += f"""
- **Concepts Being Learned:** {effectiveness['concepts_being_learned']}
- **Levels Being Played:** {effectiveness['levels_being_played']}
- **Overall Effectiveness Score:** {effectiveness['overall_effectiveness_score']:.1f}%

### Top Concepts by Mastery:
"""
        sorted_concepts = sorted(
            effectiveness.get('avg_mastery_by_concept', {}).items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        
        for concept, mastery in sorted_concepts:
            report += f"- **{concept}**: {mastery:.1%} mastery\n"
        
        report += "\n### Top Levels by Score:\n"
        sorted_levels = sorted(
            effectiveness.get('avg_score_by_level', {}).items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        
        for level, score in sorted_levels:
            report += f"- **{level}**: {score:.1f} avg score\n"
    
    report += "\n## ⚡ System Performance\n\n"
    
    if performance.get("status") == "no_data":
        report += "⚠️ No performance data available yet. Start collecting measurement data.\n\n"
    else:
        report += f"""
- **Avg Page Load Time:** {performance['avg_page_load_time']:.2f}s
- **Avg Frame Rate:** {performance['avg_frame_rate']:.1f} fps
- **Integration Success Rate:** {performance['integration_success_rate']:.1f}%
- **Integration Error Rate:** {performance['integration_error_rate']:.1f}%
- **Avg Session Time:** {performance['avg_session_time']:.0f}s
- **Performance Score:** {performance['performance_score']:.1f}/100

"""
    
    report += "## 🚀 Improvement Opportunities\n\n"
    
    if not opportunities:
        report += "✅ No critical issues identified. System is performing well!\n\n"
    else:
        for i, opp in enumerate(opportunities, 1):
            priority_emoji = "🔴" if opp['priority'] == "high" else "🟡" if opp['priority'] == "medium" else "🟢"
            report += f"""
### {i}. {priority_emoji} {opp['area']}: {opp['issue']}

- **Metric:** {opp['metric']}
- **Recommendation:** {opp['recommendation']}
- **Priority:** {opp['priority'].upper()}

"""
    
    return report

def main():
    """Main function for CLI usage."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python analytics-system.py report          # Generate analytics report")
        print("  python analytics-system.py analyze         # Run full analysis")
        return
    
    command = sys.argv[1]
    
    if command == "report":
        report = generate_analytics_report()
        print(report)
        
        # Save report
        report_file = PROJECT_ROOT / "ANALYTICS-REPORT.md"
        with open(report_file, 'w') as f:
            f.write(report)
        print(f"\n✅ Report saved to: {report_file}")
        
        # Save analytics data
        progress_data = load_progress_data()
        measurement_data = load_measurement_data()
        
        analytics_data = {
            "engagement": analyze_student_engagement(progress_data),
            "effectiveness": analyze_learning_effectiveness(progress_data),
            "performance": analyze_system_performance(measurement_data),
            "opportunities": identify_improvement_opportunities(progress_data, measurement_data)
        }
        
        save_analytics_data(analytics_data)
        print(f"✅ Analytics data saved to: {ANALYTICS_DATA_FILE}")
    
    elif command == "analyze":
        print("🔍 Running analytics analysis...")
        
        progress_data = load_progress_data()
        measurement_data = load_measurement_data()
        
        print("\n📊 Engagement Analysis:")
        engagement = analyze_student_engagement(progress_data)
        print(json.dumps(engagement, indent=2))
        
        print("\n📚 Effectiveness Analysis:")
        effectiveness = analyze_learning_effectiveness(progress_data)
        print(json.dumps(effectiveness, indent=2))
        
        print("\n⚡ Performance Analysis:")
        performance = analyze_system_performance(measurement_data)
        print(json.dumps(performance, indent=2))
        
        print("\n🚀 Improvement Opportunities:")
        opportunities = identify_improvement_opportunities(progress_data, measurement_data)
        print(json.dumps(opportunities, indent=2))
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()

