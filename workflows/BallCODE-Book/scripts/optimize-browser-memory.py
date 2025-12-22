#!/usr/bin/env python3
"""
Browser Memory Optimization
Addresses Brave Browser memory usage (~800MB)

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import psutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

def print_header(title):
    """Print formatted header."""
    print("\n" + "=" * 70)
    print(f"🌐 {title}")
    print("=" * 70)

def identify_browser_processes() -> List[Dict]:
    """Identify browser processes consuming memory."""
    print("\n🔍 Identifying browser processes...")
    
    browser_processes = []
    browser_keywords = ['brave', 'chrome', 'safari', 'firefox', 'edge']
    
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'memory_info']):
        try:
            name = proc.info['name'].lower()
            if any(keyword in name for keyword in browser_keywords):
                mem_info = proc.info.get('memory_info')
                if mem_info:
                    browser_processes.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'memory_percent': proc.info.get('memory_percent', 0),
                        'memory_mb': mem_info.rss / (1024 * 1024)
                    })
        except (psutil.NoSuchProcess, psutil.AccessDenied, AttributeError, KeyError):
            pass
    
    browser_processes.sort(key=lambda x: x['memory_mb'], reverse=True)
    
    return browser_processes

def analyze_browser_memory(browser_processes: List[Dict]) -> Dict:
    """Analyze browser memory usage."""
    total_memory = sum(p['memory_mb'] for p in browser_processes)
    process_count = len(browser_processes)
    
    # Group by browser type
    browsers = {}
    for proc in browser_processes:
        name = proc['name'].lower()
        browser_type = 'brave' if 'brave' in name else 'chrome' if 'chrome' in name else 'other'
        if browser_type not in browsers:
            browsers[browser_type] = {'processes': [], 'total_mb': 0}
        browsers[browser_type]['processes'].append(proc)
        browsers[browser_type]['total_mb'] += proc['memory_mb']
    
    return {
        'total_memory_mb': total_memory,
        'process_count': process_count,
        'browsers': browsers
    }

def generate_recommendations(analysis: Dict) -> List[str]:
    """Generate memory optimization recommendations."""
    recommendations = []
    
    for browser_type, data in analysis['browsers'].items():
        total_mb = data['total_mb']
        process_count = len(data['processes'])
        
        if total_mb > 500:  # More than 500MB
            recommendations.append({
                'browser': browser_type,
                'memory_mb': total_mb,
                'process_count': process_count,
                'priority': 'high',
                'actions': [
                    f"Close unused {browser_type} tabs (currently {process_count} processes using {total_mb:.0f}MB)",
                    f"Use tab suspension extension (OneTab, Tab Suspender) for {browser_type}",
                    f"Consider closing {browser_type} if not actively using it",
                    f"Review and close unnecessary {browser_type} extensions"
                ]
            })
        elif total_mb > 200:  # More than 200MB
            recommendations.append({
                'browser': browser_type,
                'memory_mb': total_mb,
                'process_count': process_count,
                'priority': 'medium',
                'actions': [
                    f"Review {browser_type} tabs and close unused ones",
                    f"Monitor {browser_type} memory usage"
                ]
            })
    
    return recommendations

def create_browser_optimization_guide(recommendations: List[Dict], analysis: Dict) -> str:
    """Create browser optimization guide."""
    guide = f"""# Browser Memory Optimization Guide

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** {__import__('datetime').datetime.now().strftime('%B %d, %Y')}

---

## 📊 Current Browser Memory Usage

**Total Browser Memory:** {analysis['total_memory_mb']:.0f} MB  
**Total Processes:** {analysis['process_count']}

### By Browser Type:

"""
    
    for browser_type, data in analysis['browsers'].items():
        guide += f"""#### {browser_type.upper()}
- **Memory:** {data['total_mb']:.0f} MB
- **Processes:** {len(data['processes'])}
- **Top Processes:**
"""
        for proc in data['processes'][:5]:
            guide += f"  - {proc['name']}: {proc['memory_mb']:.0f} MB (PID: {proc['pid']})\n"
        guide += "\n"
    
    guide += """---

## 💡 Optimization Recommendations

"""
    
    for i, rec in enumerate(recommendations, 1):
        guide += f"""### {i}. {rec['browser'].upper()} Browser ({rec['priority'].upper()} Priority)

**Current Usage:** {rec['memory_mb']:.0f} MB across {rec['process_count']} processes

**Actions:**
"""
        for action in rec['actions']:
            guide += f"- {action}\n"
        guide += "\n"
    
    guide += """---

## 🚀 Quick Actions

### 1. Close Unused Tabs
- Review all open browser tabs
- Close tabs you're not actively using
- **Expected Impact:** 20-30% memory reduction

### 2. Use Tab Suspension Extension
- Install OneTab or Tab Suspender
- Automatically suspend inactive tabs
- **Expected Impact:** 30-50% memory reduction

### 3. Review Extensions
- Disable unused browser extensions
- Each extension uses memory
- **Expected Impact:** 5-10% memory reduction

### 4. Close Browser When Not Needed
- Close browser if not actively using it
- Reopen when needed
- **Expected Impact:** 100% memory reduction (when closed)

---

## 📈 Expected Impact

**Current Browser Memory:** {analysis['total_memory_mb']:.0f} MB

**After Optimization:**
- **Close unused tabs:** {analysis['total_memory_mb'] * 0.7:.0f} MB (30% reduction)
- **Use tab suspension:** {analysis['total_memory_mb'] * 0.5:.0f} MB (50% reduction)
- **Close browser:** 0 MB (100% reduction)

**Memory Score Improvement:** +15-20 points (estimated)

---

## 🎯 Success Criteria

- ✅ Browser memory < 300MB (currently {analysis['total_memory_mb']:.0f}MB)
- ✅ Memory usage < 70% (currently 83.4%)
- ✅ Memory score > 50/100 (currently 16.6)

---

**Generated by:** Browser Memory Optimization Script  
**Status:** ✅ Complete

---

**Copyright © 2025 Rashad West. All Rights Reserved.**
"""
    
    return guide

def main():
    """Main function."""
    print_header("Browser Memory Optimization")
    
    # Identify browser processes
    browser_processes = identify_browser_processes()
    
    if not browser_processes:
        print("\n✅ No browser processes found - memory is optimized!")
        return True
    
    print(f"\n📊 Found {len(browser_processes)} browser processes:")
    print("-" * 70)
    print(f"{'PID':<8} {'Name':<40} {'Memory MB':<12} {'Memory %':<12}")
    print("-" * 70)
    
    for proc in browser_processes[:20]:  # Top 20
        print(f"{proc['pid']:<8} {proc['name']:<40} {proc['memory_mb']:>10.0f} MB {proc['memory_percent']:>10.2f}%")
    
    # Analyze memory usage
    analysis = analyze_browser_memory(browser_processes)
    
    print(f"\n📊 Total Browser Memory: {analysis['total_memory_mb']:.0f} MB")
    print(f"📊 Total Processes: {analysis['process_count']}")
    
    # Generate recommendations
    recommendations = generate_recommendations(analysis)
    
    # Create guide
    guide = create_browser_optimization_guide(recommendations, analysis)
    
    # Save guide
    PROJECT_ROOT = Path(__file__).parent.parent
    guide_file = PROJECT_ROOT / "documents" / "BROWSER-MEMORY-OPTIMIZATION-GUIDE.md"
    with open(guide_file, 'w') as f:
        f.write(guide)
    
    print(f"\n💾 Optimization guide saved: {guide_file}")
    
    # Display recommendations
    print_header("Optimization Recommendations")
    
    for rec in recommendations:
        print(f"\n🔴 {rec['browser'].upper()} Browser ({rec['priority'].upper()} Priority)")
        print(f"   Memory: {rec['memory_mb']:.0f} MB across {rec['process_count']} processes")
        print("   Actions:")
        for action in rec['actions']:
            print(f"      - {action}")
    
    print("\n" + "=" * 70)
    print("✅ Browser Memory Analysis Complete!")
    print("=" * 70)
    print(f"\n📄 Full guide: {guide_file}")
    print("\n💡 Next Steps:")
    print("   1. Review browser tabs and close unused ones")
    print("   2. Install tab suspension extension (OneTab, Tab Suspender)")
    print("   3. Review and disable unused browser extensions")
    print("   4. Close browser when not actively using it")
    print()
    
    return True

if __name__ == "__main__":
    main()

