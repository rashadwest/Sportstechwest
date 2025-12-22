#!/usr/bin/env python3
"""
Measurement Dashboard System
Tracks system efficiency and effectiveness metrics for BallCODE

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import time

PROJECT_ROOT = Path(__file__).parent.parent
DASHBOARD_DIR = PROJECT_ROOT / "BallCode" / "dashboard"
DASHBOARD_DATA_FILE = PROJECT_ROOT / "measurement-data.json"
MEASUREMENT_HTML = DASHBOARD_DIR / "measurement.html"

# Ensure directories exist
DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)

# Efficiency Metrics
EFFICIENCY_METRICS = {
    "page_load_times": {
        "homepage": {"target": 3.0, "unit": "seconds"},
        "book_page": {"target": 3.0, "unit": "seconds"},
        "game_load": {"target": 5.0, "unit": "seconds"}
    },
    "game_performance": {
        "frame_rate": {"target": 60, "unit": "fps"},
        "load_time": {"target": 5.0, "unit": "seconds"},
        "response_time": {"target": 0.1, "unit": "seconds"}
    },
    "integration_flow": {
        "success_rate": {"target": 95.0, "unit": "percent"},
        "error_rate": {"target": 5.0, "unit": "percent"},
        "completion_rate": {"target": 95.0, "unit": "percent"}
    },
    "user_engagement": {
        "avg_session_time": {"target": 600, "unit": "seconds"},
        "pages_per_session": {"target": 5, "unit": "pages"},
        "return_rate": {"target": 50.0, "unit": "percent"}
    },
    "error_rates": {
        "total_errors": {"target": 0, "unit": "count"},
        "critical_errors": {"target": 0, "unit": "count"},
        "error_rate": {"target": 0.0, "unit": "percent"}
    }
}

# Effectiveness Metrics
EFFECTIVENESS_METRICS = {
    "student_completion": {
        "book_completion_rate": {"target": 70.0, "unit": "percent"},
        "exercise_completion_rate": {"target": 75.0, "unit": "percent"},
        "full_journey_completion": {"target": 70.0, "unit": "percent"}
    },
    "learning_objectives": {
        "objective_achievement_rate": {"target": 80.0, "unit": "percent"},
        "concept_mastery": {"target": 75.0, "unit": "percent"},
        "progress_tracking": {"target": 100.0, "unit": "percent"}
    },
    "user_retention": {
        "day_1_retention": {"target": 50.0, "unit": "percent"},
        "week_1_retention": {"target": 50.0, "unit": "percent"},
        "month_1_retention": {"target": 40.0, "unit": "percent"}
    },
    "school_adoption": {
        "schools_signed_up": {"target": 10, "unit": "count"},
        "students_onboarded": {"target": 0, "unit": "count"},
        "active_usage": {"target": 80.0, "unit": "percent"}
    }
}

def load_measurement_data() -> Dict:
    """Load existing measurement data."""
    if DASHBOARD_DATA_FILE.exists():
        with open(DASHBOARD_DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        "last_updated": datetime.now().isoformat(),
        "efficiency": {},
        "effectiveness": {},
        "history": []
    }

def save_measurement_data(data: Dict):
    """Save measurement data."""
    data["last_updated"] = datetime.now().isoformat()
    with open(DASHBOARD_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def calculate_efficiency_score(metrics: Dict) -> float:
    """Calculate overall efficiency score (0-100)."""
    scores = []
    
    # Page load times (weight: 20%)
    if "page_load_times" in metrics:
        page_metrics = metrics["page_load_times"]
        page_score = 0
        count = 0
        for page, target in EFFICIENCY_METRICS["page_load_times"].items():
            if page in page_metrics:
                actual = page_metrics[page]
                score = min(100, (target["target"] / actual) * 100) if actual > 0 else 0
                page_score += score
                count += 1
        if count > 0:
            scores.append((page_score / count) * 0.20)
    
    # Game performance (weight: 20%)
    if "game_performance" in metrics:
        game_metrics = metrics["game_performance"]
        game_score = 0
        count = 0
        for metric, target in EFFICIENCY_METRICS["game_performance"].items():
            if metric in game_metrics:
                actual = game_metrics[metric]
                if metric == "frame_rate":
                    score = min(100, (actual / target["target"]) * 100)
                else:
                    score = min(100, (target["target"] / actual) * 100) if actual > 0 else 0
                game_score += score
                count += 1
        if count > 0:
            scores.append((game_score / count) * 0.20)
    
    # Integration flow (weight: 30%)
    if "integration_flow" in metrics:
        integration_metrics = metrics["integration_flow"]
        integration_score = 0
        count = 0
        for metric, target in EFFICIENCY_METRICS["integration_flow"].items():
            if metric in integration_metrics:
                actual = integration_metrics[metric]
                if "rate" in metric:
                    score = min(100, (actual / target["target"]) * 100)
                else:
                    score = max(0, 100 - (actual / target["target"]) * 100)
                integration_score += score
                count += 1
        if count > 0:
            scores.append((integration_score / count) * 0.30)
    
    # User engagement (weight: 20%)
    if "user_engagement" in metrics:
        engagement_metrics = metrics["user_engagement"]
        engagement_score = 0
        count = 0
        for metric, target in EFFICIENCY_METRICS["user_engagement"].items():
            if metric in engagement_metrics:
                actual = engagement_metrics[metric]
                if "rate" in metric:
                    score = min(100, (actual / target["target"]) * 100)
                else:
                    score = min(100, (actual / target["target"]) * 100)
                engagement_score += score
                count += 1
        if count > 0:
            scores.append((engagement_score / count) * 0.20)
    
    # Error rates (weight: 10%)
    if "error_rates" in metrics:
        error_metrics = metrics["error_rates"]
        error_score = 100
        if "error_rate" in error_metrics:
            actual = error_metrics["error_rate"]
            target = EFFICIENCY_METRICS["error_rates"]["error_rate"]["target"]
            error_score = max(0, 100 - (actual / target) * 100) if target > 0 else 100
        scores.append(error_score * 0.10)
    
    return sum(scores) if scores else 0

def calculate_effectiveness_score(metrics: Dict) -> float:
    """Calculate overall effectiveness score (0-100)."""
    scores = []
    
    # Student completion (weight: 30%)
    if "student_completion" in metrics:
        completion_metrics = metrics["student_completion"]
        completion_score = 0
        count = 0
        for metric, target in EFFECTIVENESS_METRICS["student_completion"].items():
            if metric in completion_metrics:
                actual = completion_metrics[metric]
                score = min(100, (actual / target["target"]) * 100)
                completion_score += score
                count += 1
        if count > 0:
            scores.append((completion_score / count) * 0.30)
    
    # Learning objectives (weight: 30%)
    if "learning_objectives" in metrics:
        learning_metrics = metrics["learning_objectives"]
        learning_score = 0
        count = 0
        for metric, target in EFFECTIVENESS_METRICS["learning_objectives"].items():
            if metric in learning_metrics:
                actual = learning_metrics[metric]
                score = min(100, (actual / target["target"]) * 100)
                learning_score += score
                count += 1
        if count > 0:
            scores.append((learning_score / count) * 0.30)
    
    # User retention (weight: 25%)
    if "user_retention" in metrics:
        retention_metrics = metrics["user_retention"]
        retention_score = 0
        count = 0
        for metric, target in EFFECTIVENESS_METRICS["user_retention"].items():
            if metric in retention_metrics:
                actual = retention_metrics[metric]
                score = min(100, (actual / target["target"]) * 100)
                retention_score += score
                count += 1
        if count > 0:
            scores.append((retention_score / count) * 0.25)
    
    # School adoption (weight: 15%)
    if "school_adoption" in metrics:
        adoption_metrics = metrics["school_adoption"]
        adoption_score = 0
        count = 0
        for metric, target in EFFECTIVENESS_METRICS["school_adoption"].items():
            if metric in adoption_metrics:
                actual = adoption_metrics[metric]
                if "rate" in metric:
                    score = min(100, (actual / target["target"]) * 100)
                else:
                    score = min(100, (actual / target["target"]) * 100)
                adoption_score += score
                count += 1
        if count > 0:
            scores.append((adoption_score / count) * 0.15)
    
    return sum(scores) if scores else 0

def generate_measurement_html(data: Dict) -> str:
    """Generate HTML dashboard."""
    efficiency_score = calculate_efficiency_score(data.get("efficiency", {}))
    effectiveness_score = calculate_effectiveness_score(data.get("effectiveness", {}))
    overall_score = (efficiency_score + effectiveness_score) / 2
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BallCODE Measurement Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        .header {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        .header .subtitle {{
            color: #666;
            font-size: 14px;
        }}
        .scores {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}
        .score-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .score-card h3 {{
            color: #666;
            font-size: 14px;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .score-value {{
            font-size: 48px;
            font-weight: bold;
            color: #333;
            margin-bottom: 5px;
        }}
        .score-bar {{
            height: 8px;
            background: #e0e0e0;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 10px;
        }}
        .score-fill {{
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            transition: width 0.3s ease;
        }}
        .metrics-section {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .metrics-section h2 {{
            color: #333;
            margin-bottom: 20px;
            font-size: 24px;
        }}
        .metric-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 15px;
        }}
        .metric-item {{
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}
        .metric-item h4 {{
            color: #333;
            font-size: 14px;
            margin-bottom: 8px;
        }}
        .metric-value {{
            font-size: 24px;
            font-weight: bold;
            color: #667eea;
        }}
        .metric-target {{
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }}
        .status-badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
            margin-left: 10px;
        }}
        .status-good {{
            background: #d4edda;
            color: #155724;
        }}
        .status-warning {{
            background: #fff3cd;
            color: #856404;
        }}
        .status-critical {{
            background: #f8d7da;
            color: #721c24;
        }}
        .last-updated {{
            text-align: center;
            color: #666;
            font-size: 12px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 BallCODE Measurement Dashboard</h1>
            <div class="subtitle">System Efficiency & Effectiveness Tracking</div>
        </div>
        
        <div class="scores">
            <div class="score-card">
                <h3>Overall Score</h3>
                <div class="score-value">{overall_score:.1f}%</div>
                <div class="score-bar">
                    <div class="score-fill" style="width: {overall_score}%"></div>
                </div>
            </div>
            <div class="score-card">
                <h3>Efficiency Score</h3>
                <div class="score-value">{efficiency_score:.1f}%</div>
                <div class="score-bar">
                    <div class="score-fill" style="width: {efficiency_score}%"></div>
                </div>
            </div>
            <div class="score-card">
                <h3>Effectiveness Score</h3>
                <div class="score-value">{effectiveness_score:.1f}%</div>
                <div class="score-bar">
                    <div class="score-fill" style="width: {effectiveness_score}%"></div>
                </div>
            </div>
        </div>
        
        <div class="metrics-section">
            <h2>⚡ Efficiency Metrics</h2>
            <div class="metric-grid">
"""
    
    # Add efficiency metrics
    efficiency = data.get("efficiency", {})
    for category, metrics in EFFICIENCY_METRICS.items():
        category_data = efficiency.get(category, {})
        for metric_name, target_info in metrics.items():
            value = category_data.get(metric_name, 0)
            target = target_info["target"]
            unit = target_info["unit"]
            
            # Determine status
            if "rate" in metric_name or "percent" in unit:
                status = "good" if value >= target * 0.9 else "warning" if value >= target * 0.7 else "critical"
            else:
                if "frame_rate" in metric_name:
                    status = "good" if value >= target * 0.9 else "warning" if value >= target * 0.7 else "critical"
                else:
                    status = "good" if value <= target * 1.1 else "warning" if value <= target * 1.3 else "critical"
            
            html += f"""
                <div class="metric-item">
                    <h4>{metric_name.replace('_', ' ').title()}</h4>
                    <div class="metric-value">{value:.2f} {unit}</div>
                    <div class="metric-target">Target: {target} {unit} <span class="status-badge status-{status}">{status.upper()}</span></div>
                </div>
"""
    
    html += """
            </div>
        </div>
        
        <div class="metrics-section">
            <h2>🎯 Effectiveness Metrics</h2>
            <div class="metric-grid">
"""
    
    # Add effectiveness metrics
    effectiveness = data.get("effectiveness", {})
    for category, metrics in EFFECTIVENESS_METRICS.items():
        category_data = effectiveness.get(category, {})
        for metric_name, target_info in metrics.items():
            value = category_data.get(metric_name, 0)
            target = target_info["target"]
            unit = target_info["unit"]
            
            # Determine status
            if "rate" in metric_name or "percent" in unit:
                status = "good" if value >= target * 0.9 else "warning" if value >= target * 0.7 else "critical"
            else:
                status = "good" if value >= target * 0.9 else "warning" if value >= target * 0.7 else "critical"
            
            html += f"""
                <div class="metric-item">
                    <h4>{metric_name.replace('_', ' ').title()}</h4>
                    <div class="metric-value">{value:.2f} {unit}</div>
                    <div class="metric-target">Target: {target} {unit} <span class="status-badge status-{status}">{status.upper()}</span></div>
                </div>
"""
    
    html += f"""
            </div>
        </div>
        
        <div class="last-updated">
            Last Updated: {data.get('last_updated', 'Never')}
        </div>
    </div>
</body>
</html>
"""
    
    return html

def main():
    """Main function to generate measurement dashboard."""
    print("=" * 60)
    print("📊 BallCODE Measurement Dashboard Generator")
    print("=" * 60)
    print()
    
    # Load existing data
    data = load_measurement_data()
    
    # Initialize with default structure if empty
    if not data.get("efficiency"):
        data["efficiency"] = {}
        for category in EFFICIENCY_METRICS.keys():
            data["efficiency"][category] = {}
    
    if not data.get("effectiveness"):
        data["effectiveness"] = {}
        for category in EFFECTIVENESS_METRICS.keys():
            data["effectiveness"][category] = {}
    
    # Generate HTML
    print("📝 Generating measurement dashboard HTML...")
    html = generate_measurement_html(data)
    
    # Save HTML
    with open(MEASUREMENT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Dashboard saved to: {MEASUREMENT_HTML}")
    print()
    
    # Calculate scores
    efficiency_score = calculate_efficiency_score(data.get("efficiency", {}))
    effectiveness_score = calculate_effectiveness_score(data.get("effectiveness", {}))
    overall_score = (efficiency_score + effectiveness_score) / 2
    
    print("📊 Current Scores:")
    print(f"  Overall: {overall_score:.1f}%")
    print(f"  Efficiency: {efficiency_score:.1f}%")
    print(f"  Effectiveness: {effectiveness_score:.1f}%")
    print()
    
    # Save data
    save_measurement_data(data)
    
    print("✅ Measurement dashboard generated successfully!")
    print()
    print("🚀 Next Steps:")
    print(f"  1. Open dashboard: {MEASUREMENT_HTML}")
    print("  2. Start collecting metrics data")
    print("  3. Update measurement-data.json with real values")
    print("  4. Run this script again to refresh dashboard")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

