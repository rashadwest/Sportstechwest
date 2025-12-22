#!/usr/bin/env python3
"""
Collect and Process Measurement Data
Collects metrics from localStorage and updates measurement dashboard

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
MEASUREMENT_DATA = PROJECT_ROOT / "measurement-data.json"

def process_metrics(metrics_json):
    """Process collected metrics and update measurement data."""
    if not MEASUREMENT_DATA.exists():
        print("⚠️  Measurement data file not found. Run measurement-dashboard.py first.")
        return False
    
    with open(MEASUREMENT_DATA, 'r') as f:
        data = json.load(f)
    
    # Process page load times
    if metrics_json.get('performance'):
        perf = metrics_json['performance']
        if 'pageLoadTime' in perf:
            page_path = metrics_json.get('pageViews', [{}])[0].get('path', 'unknown')
            if 'page_load_times' not in data['efficiency']:
                data['efficiency']['page_load_times'] = {}
            
            # Calculate average if multiple measurements
            if page_path in data['efficiency']['page_load_times']:
                existing = data['efficiency']['page_load_times'][page_path]
                data['efficiency']['page_load_times'][page_path] = (existing + perf['pageLoadTime']) / 2
            else:
                data['efficiency']['page_load_times'][page_path] = perf['pageLoadTime']
    
    # Process error rates
    if metrics_json.get('errors'):
        error_count = len(metrics_json['errors'])
        if 'error_rates' not in data['efficiency']:
            data['efficiency']['error_rates'] = {}
        
        if 'total_errors' in data['efficiency']['error_rates']:
            data['efficiency']['error_rates']['total_errors'] += error_count
        else:
            data['efficiency']['error_rates']['total_errors'] = error_count
    
    # Process user engagement
    if metrics_json.get('pageViews'):
        session_time = 0
        if metrics_json.get('sessionStart') and metrics_json.get('collectedAt'):
            from dateutil import parser
            start = parser.parse(metrics_json['sessionStart'])
            end = parser.parse(metrics_json['collectedAt'])
            session_time = (end - start).total_seconds()
        
        if 'user_engagement' not in data['efficiency']:
            data['efficiency']['user_engagement'] = {}
        
        # Update average session time
        if 'avg_session_time' in data['efficiency']['user_engagement']:
            existing = data['efficiency']['user_engagement']['avg_session_time']
            data['efficiency']['user_engagement']['avg_session_time'] = (existing + session_time) / 2
        else:
            data['efficiency']['user_engagement']['avg_session_time'] = session_time
        
        # Update pages per session
        pages = len(metrics_json['pageViews'])
        if 'pages_per_session' in data['efficiency']['user_engagement']:
            existing = data['efficiency']['user_engagement']['pages_per_session']
            data['efficiency']['user_engagement']['pages_per_session'] = (existing + pages) / 2
        else:
            data['efficiency']['user_engagement']['pages_per_session'] = pages
    
    data['last_updated'] = datetime.now().isoformat()
    
    with open(MEASUREMENT_DATA, 'w') as f:
        json.dump(data, f, indent=2)
    
    print("✅ Metrics processed and saved")
    return True

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        metrics_file = Path(sys.argv[1])
        if metrics_file.exists():
            with open(metrics_file, 'r') as f:
                metrics = json.load(f)
            process_metrics(metrics)
        else:
            print(f"❌ Metrics file not found: {metrics_file}")
    else:
        print("Usage: python3 collect-metrics.py <metrics.json>")
