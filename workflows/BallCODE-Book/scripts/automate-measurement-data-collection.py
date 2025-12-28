#!/usr/bin/env python3
"""
Automate Measurement System Data Collection
Sets up tracking scripts and connects to measurement dashboard

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
MEASUREMENT_DATA = PROJECT_ROOT / "measurement-data.json"
TRACKING_JS = WEBSITE_DIR / "js" / "measurement-tracking.js"

# Ensure directories exist
(WEBSITE_DIR / "js").mkdir(parents=True, exist_ok=True)

def create_tracking_script():
    """Create JavaScript tracking script for website."""
    js_content = """/**
 * BallCODE Measurement Tracking
 * Automatically tracks user interactions and system performance
 */

(function() {
    'use strict';
    
    // Configuration
    const CONFIG = {
        endpoint: '/api/measurement',
        trackPageViews: true,
        trackClicks: true,
        trackPerformance: true,
        trackErrors: true
    };
    
    // Storage for metrics
    const metrics = {
        pageViews: [],
        clicks: [],
        performance: {},
        errors: [],
        sessionStart: new Date().toISOString()
    };
    
    // Track page load time
    if (CONFIG.trackPerformance && window.performance) {
        window.addEventListener('load', function() {
            const perfData = window.performance.timing;
            const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
            
            metrics.performance = {
                pageLoadTime: pageLoadTime,
                domContentLoaded: perfData.domContentLoadedEventEnd - perfData.navigationStart,
                firstPaint: perfData.responseEnd - perfData.navigationStart,
                timestamp: new Date().toISOString()
            };
            
            // Store in localStorage for later collection
            try {
                localStorage.setItem('ballcode_performance', JSON.stringify(metrics.performance));
            } catch (e) {
                console.warn('Could not store performance metrics:', e);
            }
        });
    }
    
    // Track page views
    if (CONFIG.trackPageViews) {
        const pageView = {
            url: window.location.href,
            path: window.location.pathname,
            timestamp: new Date().toISOString(),
            referrer: document.referrer
        };
        
        metrics.pageViews.push(pageView);
        
        // Store in localStorage
        try {
            const existing = JSON.parse(localStorage.getItem('ballcode_pageviews') || '[]');
            existing.push(pageView);
            localStorage.setItem('ballcode_pageviews', JSON.stringify(existing.slice(-50))); // Keep last 50
        } catch (e) {
            console.warn('Could not store page view:', e);
        }
    }
    
    // Track clicks on important elements
    if (CONFIG.trackClicks) {
        document.addEventListener('click', function(e) {
            const target = e.target;
            
            // Track exercise button clicks
            if (target.classList.contains('try-exercise-button') || 
                target.closest('.try-exercise-button')) {
                const clickData = {
                    type: 'exercise_button_click',
                    url: window.location.href,
                    timestamp: new Date().toISOString()
                };
                
                metrics.clicks.push(clickData);
                
                try {
                    const existing = JSON.parse(localStorage.getItem('ballcode_clicks') || '[]');
                    existing.push(clickData);
                    localStorage.setItem('ballcode_clicks', JSON.stringify(existing.slice(-100))); // Keep last 100
                } catch (e) {
                    console.warn('Could not store click:', e);
                }
            }
            
            // Track book navigation
            if (target.classList.contains('book-link') || 
                target.closest('.book-link')) {
                const clickData = {
                    type: 'book_navigation',
                    url: window.location.href,
                    target: target.href || target.closest('a')?.href,
                    timestamp: new Date().toISOString()
                };
                
                metrics.clicks.push(clickData);
            }
        });
    }
    
    // Track errors
    if (CONFIG.trackErrors) {
        window.addEventListener('error', function(e) {
            const errorData = {
                message: e.message,
                source: e.filename,
                line: e.lineno,
                column: e.colno,
                timestamp: new Date().toISOString()
            };
            
            metrics.errors.push(errorData);
            
            try {
                const existing = JSON.parse(localStorage.getItem('ballcode_errors') || '[]');
                existing.push(errorData);
                localStorage.setItem('ballcode_errors', JSON.stringify(existing.slice(-50))); // Keep last 50
            } catch (err) {
                console.warn('Could not store error:', err);
            }
        });
    }
    
    // Function to collect all metrics
    window.collectBallcodeMetrics = function() {
        try {
            const allMetrics = {
                pageViews: JSON.parse(localStorage.getItem('ballcode_pageviews') || '[]'),
                clicks: JSON.parse(localStorage.getItem('ballcode_clicks') || '[]'),
                performance: JSON.parse(localStorage.getItem('ballcode_performance') || '{}'),
                errors: JSON.parse(localStorage.getItem('ballcode_errors') || '[]'),
                sessionStart: metrics.sessionStart,
                collectedAt: new Date().toISOString()
            };
            
            return allMetrics;
        } catch (e) {
            console.error('Error collecting metrics:', e);
            return null;
        }
    };
    
    // Function to clear metrics (after sending to server)
    window.clearBallcodeMetrics = function() {
        try {
            localStorage.removeItem('ballcode_pageviews');
            localStorage.removeItem('ballcode_clicks');
            localStorage.removeItem('ballcode_performance');
            localStorage.removeItem('ballcode_errors');
        } catch (e) {
            console.warn('Error clearing metrics:', e);
        }
    };
    
    // Expose metrics object for debugging
    window.ballcodeMetrics = metrics;
    
    console.log('BallCODE measurement tracking initialized');
})();
"""
    
    with open(TRACKING_JS, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"✅ Created: {TRACKING_JS}")
    return TRACKING_JS

def update_measurement_data():
    """Update measurement data file with initial structure."""
    if MEASUREMENT_DATA.exists():
        with open(MEASUREMENT_DATA, 'r') as f:
            data = json.load(f)
    else:
        data = {
            "last_updated": datetime.now().isoformat(),
            "efficiency": {},
            "effectiveness": {},
            "history": []
        }
    
    # Initialize efficiency metrics structure
    if not data.get("efficiency"):
        data["efficiency"] = {
            "page_load_times": {},
            "game_performance": {},
            "integration_flow": {},
            "user_engagement": {},
            "error_rates": {}
        }
    
    # Initialize effectiveness metrics structure
    if not data.get("effectiveness"):
        data["effectiveness"] = {
            "student_completion": {},
            "learning_objectives": {},
            "user_retention": {},
            "school_adoption": {}
        }
    
    data["last_updated"] = datetime.now().isoformat()
    
    with open(MEASUREMENT_DATA, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Updated: {MEASUREMENT_DATA}")
    return MEASUREMENT_DATA

def add_tracking_to_html():
    """Add tracking script to HTML files."""
    html_files = [
        WEBSITE_DIR / "index.html",
        WEBSITE_DIR / "books" / "book1.html"
    ]
    
    tracking_script = '<script src="/js/measurement-tracking.js"></script>'
    
    for html_file in html_files:
        if not html_file.exists():
            print(f"⚠️  Skipping {html_file} (not found)")
            continue
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already added
        if 'measurement-tracking.js' in content:
            print(f"⚠️  {html_file.name} already has tracking script")
            continue
        
        # Add before closing </body> tag
        if '</body>' in content:
            content = content.replace('</body>', f'    {tracking_script}\n</body>')
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Added tracking to: {html_file.name}")
        else:
            print(f"⚠️  {html_file.name} has no </body> tag")
    
    return True

def create_data_collection_script():
    """Create Python script to collect and process metrics."""
    script_content = """#!/usr/bin/env python3
\"\"\"
Collect and Process Measurement Data
Collects metrics from localStorage and updates measurement dashboard

Copyright © 2025 Rashad West. All Rights Reserved.
\"\"\"

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
MEASUREMENT_DATA = PROJECT_ROOT / "measurement-data.json"

def process_metrics(metrics_json):
    \"\"\"Process collected metrics and update measurement data.\"\"\"
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
"""
    
    script_path = PROJECT_ROOT / "scripts" / "collect-metrics.py"
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    # Make executable
    os.chmod(script_path, 0o755)
    
    print(f"✅ Created: {script_path}")
    return script_path

def main():
    """Main function to set up measurement data collection."""
    print("=" * 60)
    print("📊 BallCODE Measurement Data Collection Setup")
    print("=" * 60)
    print()
    
    print("🔧 Setting up tracking system...")
    print()
    
    # Create tracking script
    create_tracking_script()
    
    # Update measurement data
    update_measurement_data()
    
    # Add tracking to HTML
    add_tracking_to_html()
    
    # Create collection script
    create_data_collection_script()
    
    print()
    print("=" * 60)
    print("✅ Measurement Data Collection Setup Complete!")
    print("=" * 60)
    print()
    
    print("📋 What Was Created:")
    print(f"  1. Tracking Script: {TRACKING_JS}")
    print(f"  2. Measurement Data: {MEASUREMENT_DATA}")
    print(f"  3. Collection Script: scripts/collect-metrics.py")
    print()
    
    print("🚀 Next Steps:")
    print("  1. Tracking script is now active on website")
    print("  2. Metrics are collected in browser localStorage")
    print("  3. Use collect-metrics.py to process collected data")
    print("  4. Run measurement-dashboard.py to update dashboard")
    print()
    
    print("💡 To Collect Metrics:")
    print("  1. Open browser console on website")
    print("  2. Run: collectBallcodeMetrics()")
    print("  3. Save output as JSON file")
    print("  4. Run: python3 scripts/collect-metrics.py <file.json>")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


