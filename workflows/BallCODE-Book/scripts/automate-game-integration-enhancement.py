#!/usr/bin/env python3
"""
Automate Game Integration Enhancement
Enhances score tracking, progress measurement, and curriculum integration

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import re
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
BOOK1_HTML = WEBSITE_DIR / "books" / "book1.html"
INTEGRATION_JS = WEBSITE_DIR / "books" / "book-integration.js"
MEASUREMENT_DATA = PROJECT_ROOT / "measurement-data.json"

def enhance_integration_javascript():
    """Enhance integration JavaScript with score tracking and progress."""
    if not INTEGRATION_JS.exists():
        print("⚠️  Integration JavaScript not found, creating new...")
        js_content = ""
    else:
        with open(INTEGRATION_JS, 'r', encoding='utf-8') as f:
            js_content = f.read()
    
    # Check if enhancements already exist
    if 'scoreTracking' in js_content and 'progressMeasurement' in js_content:
        print("⚠️  Enhancements already exist in integration JavaScript")
        return True
    
    # Add enhanced tracking functions
    enhancements = """
// Enhanced Score Tracking
function trackExerciseScore(score, maxScore, exerciseId) {
    const scoreData = {
        score: score,
        maxScore: maxScore,
        percentage: (score / maxScore) * 100,
        exerciseId: exerciseId,
        timestamp: new Date().toISOString()
    };
    
    // Store in localStorage
    try {
        const existing = JSON.parse(localStorage.getItem('ballcode_scores') || '[]');
        existing.push(scoreData);
        localStorage.setItem('ballcode_scores', JSON.stringify(existing.slice(-50))); // Keep last 50
    } catch (e) {
        console.warn('Could not store score:', e);
    }
    
    // Track in measurement system
    if (window.collectBallcodeMetrics) {
        const metrics = window.collectBallcodeMetrics();
        if (metrics) {
            // Score is part of effectiveness metrics
            console.log('Score tracked:', scoreData);
        }
    }
    
    return scoreData;
}

// Enhanced Progress Measurement
function measureProgress(bookId, exerciseId, completed) {
    const progressData = {
        bookId: bookId,
        exerciseId: exerciseId,
        completed: completed,
        timestamp: new Date().toISOString(),
        sessionId: getSessionId()
    };
    
    // Store progress
    try {
        const existing = JSON.parse(localStorage.getItem('ballcode_progress') || '[]');
        existing.push(progressData);
        localStorage.setItem('ballcode_progress', JSON.stringify(existing.slice(-100))); // Keep last 100
    } catch (e) {
        console.warn('Could not store progress:', e);
    }
    
    // Update completion rate
    updateCompletionRate(bookId, exerciseId, completed);
    
    return progressData;
}

// Update completion rate
function updateCompletionRate(bookId, exerciseId, completed) {
    try {
        const key = `ballcode_completion_${bookId}_${exerciseId}`;
        const existing = JSON.parse(localStorage.getItem(key) || '{"attempts": 0, "completions": 0}');
        
        existing.attempts += 1;
        if (completed) {
            existing.completions += 1;
        }
        
        existing.completionRate = (existing.completions / existing.attempts) * 100;
        existing.lastUpdated = new Date().toISOString();
        
        localStorage.setItem(key, JSON.stringify(existing));
        
        return existing.completionRate;
    } catch (e) {
        console.warn('Could not update completion rate:', e);
        return 0;
    }
}

// Get or create session ID
function getSessionId() {
    let sessionId = localStorage.getItem('ballcode_session_id');
    if (!sessionId) {
        sessionId = 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
        localStorage.setItem('ballcode_session_id', sessionId);
    }
    return sessionId;
}

// Enhanced return flow with progress
function returnToBookWithProgress(bookId, exerciseId, score, completed) {
    // Track score
    if (score !== undefined) {
        trackExerciseScore(score, 100, exerciseId); // Assuming max score of 100
    }
    
    // Measure progress
    measureProgress(bookId, exerciseId, completed);
    
    // Return to book page
    const returnUrl = `/books/book${bookId}.html?exercise=${exerciseId}&completed=${completed}&score=${score || 0}`;
    window.location.href = returnUrl;
}

// Expose functions globally
window.trackExerciseScore = trackExerciseScore;
window.measureProgress = measureProgress;
window.updateCompletionRate = updateCompletionRate;
window.returnToBookWithProgress = returnToBookWithProgress;
"""
    
    # Append enhancements
    if js_content and not js_content.endswith('\n'):
        js_content += '\n'
    
    js_content += enhancements
    
    with open(INTEGRATION_JS, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"✅ Enhanced: {INTEGRATION_JS}")
    return True

def add_progress_display_to_book1():
    """Add progress display section to Book 1."""
    if not BOOK1_HTML.exists():
        print("⚠️  Book 1 page not found")
        return False
    
    with open(BOOK1_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if progress display already exists
    if 'progress-display' in content or 'Exercise Progress' in content:
        print("⚠️  Progress display already exists")
        return True
    
    progress_html = '''
        <div id="progress-display" class="progress-display" style="background: #e7f3ff; padding: 1.5rem; border-radius: 8px; margin: 2rem 0; display: none;">
            <h3 style="color: #0C72B3; margin-bottom: 1rem;">📊 Exercise Progress</h3>
            <div id="progress-stats" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
                <div style="background: white; padding: 1rem; border-radius: 4px;">
                    <div style="font-size: 0.9rem; color: #666;">Completion Rate</div>
                    <div id="completion-rate" style="font-size: 1.5rem; font-weight: bold; color: #0C72B3;">--</div>
                </div>
                <div style="background: white; padding: 1rem; border-radius: 4px;">
                    <div style="font-size: 0.9rem; color: #666;">Average Score</div>
                    <div id="average-score" style="font-size: 1.5rem; font-weight: bold; color: #eb6123;">--</div>
                </div>
                <div style="background: white; padding: 1rem; border-radius: 4px;">
                    <div style="font-size: 0.9rem; color: #666;">Attempts</div>
                    <div id="attempts-count" style="font-size: 1.5rem; font-weight: bold; color: #28a745;">--</div>
                </div>
            </div>
        </div>
        
        <script>
        // Load and display progress
        (function() {
            try {
                const bookId = 1;
                const exerciseId = 'foundation-block';
                const key = `ballcode_completion_${bookId}_${exerciseId}`;
                const progress = JSON.parse(localStorage.getItem(key) || '{"attempts": 0, "completions": 0, "completionRate": 0}');
                
                const scores = JSON.parse(localStorage.getItem('ballcode_scores') || '[]');
                const exerciseScores = scores.filter(s => s.exerciseId === exerciseId);
                const avgScore = exerciseScores.length > 0 
                    ? exerciseScores.reduce((sum, s) => sum + s.percentage, 0) / exerciseScores.length 
                    : 0;
                
                if (progress.attempts > 0) {
                    document.getElementById('progress-display').style.display = 'block';
                    document.getElementById('completion-rate').textContent = progress.completionRate.toFixed(0) + '%';
                    document.getElementById('average-score').textContent = avgScore.toFixed(0) + '%';
                    document.getElementById('attempts-count').textContent = progress.attempts;
                }
            } catch (e) {
                console.warn('Could not load progress:', e);
            }
        })();
        </script>
'''
    
    # Insert before exercise section or after curriculum section
    insertion_points = [
        (r'(<div class="exercise-section">)', progress_html + r'\n        \1'),
        (r'(</section>\s*<div class="exercise-section">)', r'\1' + progress_html),
        (r'(id="curriculum-section".*?</section>)', r'\1' + progress_html),
    ]
    
    added = False
    for pattern, replacement in insertion_points:
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            added = True
            print("✅ Added progress display to Book 1")
            break
    
    if added:
        with open(BOOK1_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        print("⚠️  Could not find insertion point for progress display")
        return False

def integrate_with_measurement_system():
    """Integrate game metrics with measurement system."""
    if not MEASUREMENT_DATA.exists():
        print("⚠️  Measurement data file not found")
        return False
    
    with open(MEASUREMENT_DATA, 'r') as f:
        data = json.load(f)
    
    # Add game performance metrics
    if 'efficiency' not in data:
        data['efficiency'] = {}
    
    if 'game_performance' not in data['efficiency']:
        data['efficiency']['game_performance'] = {
            "frame_rate": 0,
            "load_time": 0,
            "response_time": 0
        }
    
    # Add exercise completion to effectiveness
    if 'effectiveness' not in data:
        data['effectiveness'] = {}
    
    if 'student_completion' not in data['effectiveness']:
        data['effectiveness']['student_completion'] = {
            "exercise_completion_rate": 0.0,
            "exercise_success_rate": 0.0
        }
    
    data['last_updated'] = datetime.now().isoformat()
    
    with open(MEASUREMENT_DATA, 'w') as f:
        json.dump(data, f, indent=2)
    
    print("✅ Integrated game metrics with measurement system")
    return True

def main():
    """Main function."""
    print("=" * 60)
    print("🎮 Game Integration Enhancement Automation")
    print("=" * 60)
    print()
    
    # Enhance integration JavaScript
    print("🔧 Enhancing integration JavaScript...")
    enhance_integration_javascript()
    print()
    
    # Add progress display
    print("📊 Adding progress display...")
    add_progress_display_to_book1()
    print()
    
    # Integrate with measurement
    print("📈 Integrating with measurement system...")
    integrate_with_measurement_system()
    print()
    
    print("=" * 60)
    print("✅ Game Integration Enhancement Complete!")
    print("=" * 60)
    print()
    
    print("🚀 Next Steps:")
    print("  1. Test score tracking in browser console")
    print("  2. Verify progress display shows on Book 1")
    print("  3. Test exercise completion flow")
    print("  4. Check measurement dashboard for game metrics")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

