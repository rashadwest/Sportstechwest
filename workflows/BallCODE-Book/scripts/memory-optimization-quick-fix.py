#!/usr/bin/env python3
"""
Memory Optimization Quick Fix
Immediate actions to improve memory usage (Hassabis + Jobs approach)

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import subprocess
import psutil
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
BALLCODE_DIR = PROJECT_ROOT / "BallCode"

def identify_memory_consumers():
    """Identify top memory consumers (Hassabis: systematic analysis)."""
    print("🔍 Identifying top memory consumers...")
    print("=" * 60)
    
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'memory_info']):
        try:
            processes.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'memory_percent': proc.info['memory_percent'],
                'memory_mb': proc.info['memory_info'].rss / (1024 * 1024)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Sort by memory usage
    processes.sort(key=lambda x: x['memory_percent'], reverse=True)
    
    print("\nTop 20 Memory Consumers:")
    print("-" * 60)
    print(f"{'PID':<8} {'Name':<30} {'Memory %':<12} {'Memory MB':<12}")
    print("-" * 60)
    
    total_memory = 0
    for proc in processes[:20]:
        print(f"{proc['pid']:<8} {proc['name']:<30} {proc['memory_percent']:>10.2f}% {proc['memory_mb']:>10.2f} MB")
        total_memory += proc['memory_mb']
    
    print("-" * 60)
    print(f"Total (Top 20): {total_memory:.2f} MB")
    print()
    
    return processes[:20]

def optimize_git_repository():
    """Optimize git repository (Jobs: simplicity, remove complexity)."""
    print("🔧 Optimizing git repository...")
    print("=" * 60)
    
    if not (BALLCODE_DIR / ".git").exists():
        print("❌ No git repository found in BallCode directory")
        return False
    
    try:
        # Check current git size
        print("\n1. Checking current git repository size...")
        result = subprocess.run(
            ['git', 'count-objects', '-vH'],
            cwd=BALLCODE_DIR,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        
        # Run git garbage collection
        print("\n2. Running git garbage collection...")
        result = subprocess.run(
            ['git', 'gc', '--aggressive', '--prune=now'],
            cwd=BALLCODE_DIR,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ Git garbage collection complete")
        else:
            print(f"⚠️ Git gc output: {result.stderr}")
        
        # Check size after optimization
        print("\n3. Checking git repository size after optimization...")
        result = subprocess.run(
            ['git', 'count-objects', '-vH'],
            cwd=BALLCODE_DIR,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        
        # Optimize git config
        print("\n4. Optimizing git configuration...")
        subprocess.run(['git', 'config', 'core.preloadindex', 'true'], cwd=BALLCODE_DIR)
        subprocess.run(['git', 'config', 'core.fscache', 'true'], cwd=BALLCODE_DIR)
        subprocess.run(['git', 'config', 'fetch.prune', 'true'], cwd=BALLCODE_DIR)
        subprocess.run(['git', 'config', 'fetch.pruneTags', 'true'], cwd=BALLCODE_DIR)
        print("✅ Git configuration optimized")
        
        return True
        
    except Exception as e:
        print(f"❌ Error optimizing git repository: {e}")
        return False

def check_memory_status():
    """Check current memory status."""
    print("📊 Current Memory Status:")
    print("=" * 60)
    
    mem = psutil.virtual_memory()
    
    print(f"Total Memory:     {mem.total / (1024**3):.2f} GB")
    print(f"Available:       {mem.available / (1024**3):.2f} GB")
    print(f"Used:             {mem.used / (1024**3):.2f} GB ({mem.percent:.1f}%)")
    print(f"Free:             {mem.free / (1024**3):.2f} GB")
    print()
    
    if mem.percent > 80:
        print("🔴 HIGH MEMORY USAGE - Action needed!")
    elif mem.percent > 70:
        print("⚠️  MODERATE MEMORY USAGE - Monitor closely")
    else:
        print("✅ Memory usage is healthy")
    
    print()
    return mem

def suggest_actions(processes, memory):
    """Suggest specific actions based on analysis (Hassabis: deep learning)."""
    print("💡 Recommended Actions:")
    print("=" * 60)
    
    # Check for common memory-intensive processes
    cursor_processes = [p for p in processes if 'cursor' in p['name'].lower() or 'code' in p['name'].lower()]
    chrome_processes = [p for p in processes if 'chrome' in p['name'].lower()]
    node_processes = [p for p in processes if 'node' in p['name'].lower()]
    
    if cursor_processes:
        total_cursor_memory = sum(p['memory_mb'] for p in cursor_processes)
        if total_cursor_memory > 500:
            print(f"\n1. Cursor IDE: Using {total_cursor_memory:.0f} MB")
            print("   → Consider closing unused tabs/windows")
            print("   → Restart Cursor if memory usage is high")
    
    if chrome_processes:
        total_chrome_memory = sum(p['memory_mb'] for p in chrome_processes)
        if total_chrome_memory > 1000:
            print(f"\n2. Chrome/Browser: Using {total_chrome_memory:.0f} MB")
            print("   → Close unused tabs")
            print("   → Consider using a lighter browser for development")
    
    if node_processes:
        total_node_memory = sum(p['memory_mb'] for p in node_processes)
        if total_node_memory > 500:
            print(f"\n3. Node.js Processes: Using {total_node_memory:.0f} MB")
            print("   → Review running node processes")
            print("   → Stop unused node servers/processes")
    
    if memory.percent > 80:
        print("\n4. General Memory Optimization:")
        print("   → Close unused applications")
        print("   → Restart system if needed")
        print("   → Review background processes")
    
    print()

def main():
    """Main execution (Jobs: simple, beautiful flow)."""
    print("🚀 Memory Optimization Quick Fix")
    print("=" * 60)
    print("AIMCODE Methodology: Hassabis (Systematic) + Jobs (Simplicity)")
    print()
    
    # Check current memory
    memory = check_memory_status()
    
    # Identify memory consumers
    processes = identify_memory_consumers()
    
    # Suggest actions
    suggest_actions(processes, memory)
    
    # Optimize git repository
    if memory.percent > 70:
        print("🔧 Running git repository optimization...")
        optimize_git_repository()
        print()
    
    # Final memory check
    print("📊 Final Memory Status:")
    print("=" * 60)
    final_memory = check_memory_status()
    
    improvement = memory.percent - final_memory.percent
    if improvement > 0:
        print(f"✅ Memory usage improved by {improvement:.1f}%")
    else:
        print("ℹ️  Run this script regularly to maintain optimal memory usage")
    
    print()
    print("💡 Next Steps:")
    print("   1. Review top memory consumers above")
    print("   2. Close unused applications")
    print("   3. Run weekly wellness check: python3 scripts/system-wellness-check.py")
    print("   4. Monitor memory patterns over time")
    print()

if __name__ == "__main__":
    main()


