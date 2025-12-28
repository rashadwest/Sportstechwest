#!/usr/bin/env python3
"""
System Wellness Check - Local vs Cloud Performance Analysis
Applies AIMCODE methodology with Demis Hassabis (systematic deep learning) 
and Steve Jobs (simplicity, beautiful design) principles

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import json
import time
import subprocess
import psutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

WELLNESS_DATA = DATA_DIR / "system-wellness.json"
WELLNESS_REPORT = PROJECT_ROOT / "documents" / "SYSTEM-WELLNESS-REPORT.md"

class SystemWellnessChecker:
    """Comprehensive system wellness check using AIMCODE methodology."""
    
    def __init__(self):
        self.metrics = {
            "timestamp": datetime.now().isoformat(),
            "local_system": {},
            "cloud_comparison": {},
            "performance_gaps": [],
            "improvement_opportunities": []
        }
    
    def check_local_system(self) -> Dict[str, Any]:
        """Check local system performance metrics (Hassabis: systematic analysis)."""
        print("🔍 Checking local system performance...")
        
        local_metrics = {
            "cpu": self._check_cpu(),
            "memory": self._check_memory(),
            "disk": self._check_disk(),
            "network": self._check_network(),
            "file_system": self._check_file_system(),
            "cursor_performance": self._check_cursor_performance(),
            "git_performance": self._check_git_performance(),
            "n8n_performance": self._check_n8n_performance()
        }
        
        return local_metrics
    
    def _check_cpu(self) -> Dict[str, Any]:
        """Check CPU performance."""
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()
        
        return {
            "usage_percent": cpu_percent,
            "core_count": cpu_count,
            "frequency_mhz": cpu_freq.current if cpu_freq else None,
            "status": "healthy" if cpu_percent < 80 else "high_load",
            "score": 100 - cpu_percent  # Lower usage = higher score
        }
    
    def _check_memory(self) -> Dict[str, Any]:
        """Check memory performance."""
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        return {
            "total_gb": round(mem.total / (1024**3), 2),
            "available_gb": round(mem.available / (1024**3), 2),
            "used_percent": mem.percent,
            "swap_total_gb": round(swap.total / (1024**3), 2),
            "swap_used_percent": swap.percent,
            "status": "healthy" if mem.percent < 80 else "high_usage",
            "score": 100 - mem.percent
        }
    
    def _check_disk(self) -> Dict[str, Any]:
        """Check disk performance."""
        disk = psutil.disk_usage('/')
        
        return {
            "total_gb": round(disk.total / (1024**3), 2),
            "used_gb": round(disk.used / (1024**3), 2),
            "free_gb": round(disk.free / (1024**3), 2),
            "used_percent": round((disk.used / disk.total) * 100, 2),
            "status": "healthy" if (disk.used / disk.total) * 100 < 85 else "low_space",
            "score": 100 - round((disk.used / disk.total) * 100, 2)
        }
    
    def _check_network(self) -> Dict[str, Any]:
        """Check network connectivity and latency."""
        try:
            # Test localhost latency
            start = time.time()
            subprocess.run(['ping', '-c', '1', 'localhost'], 
                         capture_output=True, timeout=2)
            local_latency = (time.time() - start) * 1000
            
            # Test external connectivity
            start = time.time()
            result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], 
                                  capture_output=True, timeout=3)
            external_latency = (time.time() - start) * 1000 if result.returncode == 0 else None
            
            return {
                "local_latency_ms": round(local_latency, 2),
                "external_latency_ms": round(external_latency, 2) if external_latency else None,
                "connectivity": "connected" if external_latency else "disconnected",
                "status": "healthy" if external_latency and external_latency < 100 else "slow",
                "score": 100 - (external_latency or 0) if external_latency else 0
            }
        except Exception as e:
            return {
                "error": str(e),
                "status": "error",
                "score": 0
            }
    
    def _check_file_system(self) -> Dict[str, Any]:
        """Check file system performance (Jobs: simplicity check)."""
        project_path = PROJECT_ROOT
        
        # Count files
        file_count = sum(1 for _ in project_path.rglob('*') if _.is_file())
        
        # Check for large files (>10MB)
        large_files = []
        for file_path in project_path.rglob('*'):
            if file_path.is_file():
                try:
                    size = file_path.stat().st_size
                    if size > 10 * 1024 * 1024:  # 10MB
                        large_files.append({
                            "path": str(file_path.relative_to(project_path)),
                            "size_mb": round(size / (1024**2), 2)
                        })
                except:
                    pass
        
        # Check git repository size
        git_dir = project_path / ".git"
        git_size = 0
        if git_dir.exists():
            git_size = sum(f.stat().st_size for f in git_dir.rglob('*') if f.is_file())
        
        return {
            "total_files": file_count,
            "large_files_count": len(large_files),
            "large_files": large_files[:10],  # Top 10
            "git_size_mb": round(git_size / (1024**2), 2),
            "status": "healthy" if len(large_files) < 20 else "needs_cleanup",
            "score": max(0, 100 - len(large_files) * 2)
        }
    
    def _check_cursor_performance(self) -> Dict[str, Any]:
        """Check Cursor IDE performance indicators."""
        cursor_cache = Path.home() / ".cursor" / "cache"
        cursor_logs = Path.home() / ".cursor" / "logs"
        
        cache_size = 0
        logs_size = 0
        
        if cursor_cache.exists():
            cache_size = sum(f.stat().st_size for f in cursor_cache.rglob('*') if f.is_file())
        
        if cursor_logs.exists():
            logs_size = sum(f.stat().st_size for f in cursor_logs.rglob('*') if f.is_file())
        
        return {
            "cache_size_mb": round(cache_size / (1024**2), 2),
            "logs_size_mb": round(logs_size / (1024**2), 2),
            "total_size_mb": round((cache_size + logs_size) / (1024**2), 2),
            "status": "healthy" if (cache_size + logs_size) < 500 * 1024**2 else "needs_cleanup",
            "score": max(0, 100 - ((cache_size + logs_size) / (1024**2)) / 10)
        }
    
    def _check_git_performance(self) -> Dict[str, Any]:
        """Check Git repository performance."""
        project_path = PROJECT_ROOT
        
        try:
            # Check git status speed
            start = time.time()
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  cwd=project_path, capture_output=True, timeout=5)
            status_time = (time.time() - start) * 1000
            
            # Check remote connectivity
            start = time.time()
            result = subprocess.run(['git', 'ls-remote', '--heads', 'origin'], 
                                  cwd=project_path, capture_output=True, timeout=5)
            remote_time = (time.time() - start) * 1000 if result.returncode == 0 else None
            
            return {
                "status_time_ms": round(status_time, 2),
                "remote_time_ms": round(remote_time, 2) if remote_time else None,
                "status": "healthy" if status_time < 1000 and (not remote_time or remote_time < 3000) else "slow",
                "score": max(0, 100 - (status_time / 10) - ((remote_time or 0) / 30))
            }
        except Exception as e:
            return {
                "error": str(e),
                "status": "error",
                "score": 0
            }
    
    def _check_n8n_performance(self) -> Dict[str, Any]:
        """Check n8n performance (local and Pi)."""
        n8n_checks = {
            "local": self._check_n8n_instance("localhost", 5678),
            "pi": self._check_n8n_instance("192.168.1.226", 5678)
        }
        
        return n8n_checks
    
    def _check_n8n_instance(self, host: str, port: int) -> Dict[str, Any]:
        """Check specific n8n instance."""
        try:
            import urllib.request
            url = f"http://{host}:{port}/healthz"
            
            start = time.time()
            with urllib.request.urlopen(url, timeout=2) as response:
                response_time = (time.time() - start) * 1000
                status_code = response.getcode()
                
                return {
                    "url": url,
                    "response_time_ms": round(response_time, 2),
                    "status_code": status_code,
                    "status": "healthy" if status_code == 200 and response_time < 500 else "slow",
                    "score": max(0, 100 - (response_time / 5))
                }
        except Exception as e:
            return {
                "url": f"http://{host}:{port}",
                "error": str(e),
                "status": "unavailable",
                "score": 0
            }
    
    def compare_with_cloud(self, local_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Compare local performance with cloud expectations (Jobs: simplicity benchmark)."""
        print("☁️ Comparing with cloud performance benchmarks...")
        
        # Cloud performance benchmarks (typical values)
        cloud_benchmarks = {
            "response_time_ms": 200,  # Cloud API response time
            "latency_ms": 50,  # Network latency
            "availability_percent": 99.9,  # Cloud uptime
            "scalability": "unlimited",  # Cloud scaling
            "cost_per_month": "variable"  # Cloud costs
        }
        
        # Local advantages
        local_advantages = {
            "zero_network_latency": True,  # No round-trip to cloud
            "privacy": True,  # All data local
            "no_rate_limits": True,  # Unlimited requests
            "offline_capable": True,  # Works without internet
            "custom_optimization": True  # Optimized for this hardware
        }
        
        # Performance gaps
        gaps = []
        
        # Check if local is faster than cloud
        if local_metrics.get("network", {}).get("external_latency_ms", 0) < cloud_benchmarks["latency_ms"]:
            gaps.append({
                "metric": "network_latency",
                "local": local_metrics.get("network", {}).get("external_latency_ms"),
                "cloud": cloud_benchmarks["latency_ms"],
                "advantage": "local",
                "improvement": "Local is faster - maintain advantage"
            })
        else:
            gaps.append({
                "metric": "network_latency",
                "local": local_metrics.get("network", {}).get("external_latency_ms"),
                "cloud": cloud_benchmarks["latency_ms"],
                "advantage": "cloud",
                "improvement": "Optimize network stack"
            })
        
        return {
            "cloud_benchmarks": cloud_benchmarks,
            "local_advantages": local_advantages,
            "performance_gaps": gaps,
            "overall": "local_competitive" if len([g for g in gaps if g["advantage"] == "local"]) > len([g for g in gaps if g["advantage"] == "cloud"]) else "cloud_better"
        }
    
    def generate_improvements(self, local_metrics: Dict[str, Any], comparison: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate improvement recommendations (Hassabis: systematic optimization)."""
        print("💡 Generating improvement recommendations...")
        
        improvements = []
        
        # CPU optimizations
        if local_metrics.get("cpu", {}).get("usage_percent", 0) > 70:
            improvements.append({
                "category": "cpu",
                "priority": "high",
                "title": "Optimize CPU Usage",
                "description": "CPU usage is high. Consider reducing background processes.",
                "hassabis_approach": "Systematic analysis: Identify CPU-intensive processes and optimize or defer them.",
                "jobs_approach": "Simplicity: Remove unnecessary processes. Keep only what's essential.",
                "action": "Review running processes and disable non-essential services."
            })
        
        # Memory optimizations
        if local_metrics.get("memory", {}).get("used_percent", 0) > 80:
            improvements.append({
                "category": "memory",
                "priority": "high",
                "title": "Optimize Memory Usage",
                "description": "Memory usage is high. Consider clearing caches or closing unused applications.",
                "hassabis_approach": "Deep learning: Analyze memory patterns and implement smart caching strategies.",
                "jobs_approach": "Beautiful design: Clean, efficient memory management. No waste.",
                "action": "Clear Cursor cache, close unused apps, implement memory-efficient patterns."
            })
        
        # Disk optimizations
        disk_used = local_metrics.get("disk", {}).get("used_percent", 0)
        if disk_used > 85:
            improvements.append({
                "category": "disk",
                "priority": "high",
                "title": "Free Up Disk Space",
                "description": f"Disk usage is {disk_used}%. Free up space for better performance.",
                "hassabis_approach": "Systems thinking: Identify large files and implement automated cleanup.",
                "jobs_approach": "Simplicity: Remove what's not needed. Keep system lean.",
                "action": "Run disk cleanup, remove large unused files, optimize storage."
            })
        
        # File system optimizations
        large_files = local_metrics.get("file_system", {}).get("large_files", [])
        if len(large_files) > 10:
            improvements.append({
                "category": "file_system",
                "priority": "medium",
                "title": "Optimize Large Files",
                "description": f"Found {len(large_files)} large files. Consider compression or removal.",
                "hassabis_approach": "Systematic optimization: Analyze file usage patterns and implement smart storage.",
                "jobs_approach": "Beautiful organization: Clean file structure. No clutter.",
                "action": "Review large files, compress if needed, remove unused files."
            })
        
        # Cursor performance optimizations
        cursor_size = local_metrics.get("cursor_performance", {}).get("total_size_mb", 0)
        if cursor_size > 500:
            improvements.append({
                "category": "cursor",
                "priority": "medium",
                "title": "Clear Cursor Cache",
                "description": f"Cursor cache is {cursor_size}MB. Clearing will improve performance.",
                "hassabis_approach": "Deep learning: Understand cache patterns and implement smart cache management.",
                "jobs_approach": "Simplicity: Clean cache regularly. Keep it minimal.",
                "action": "Clear Cursor cache and logs, optimize file watcher settings."
            })
        
        # Git performance optimizations
        git_status_time = local_metrics.get("git_performance", {}).get("status_time_ms", 0)
        if git_status_time > 1000:
            improvements.append({
                "category": "git",
                "priority": "medium",
                "title": "Optimize Git Performance",
                "description": f"Git status takes {git_status_time}ms. Optimize repository.",
                "hassabis_approach": "Systematic optimization: Analyze git operations and optimize repository structure.",
                "jobs_approach": "Simplicity: Clean git history, optimize for speed.",
                "action": "Run git gc, review .gitignore, optimize repository structure."
            })
        
        # Network optimizations
        network_latency = local_metrics.get("network", {}).get("external_latency_ms", 0)
        if network_latency > 100:
            improvements.append({
                "category": "network",
                "priority": "low",
                "title": "Optimize Network Connection",
                "description": f"Network latency is {network_latency}ms. Check connection quality.",
                "hassabis_approach": "Systems thinking: Analyze network patterns and optimize routing.",
                "jobs_approach": "Simplicity: Fast, reliable connection. No unnecessary hops.",
                "action": "Check network connection, optimize DNS, review network settings."
            })
        
        return improvements
    
    def save_results(self):
        """Save wellness check results."""
        self.metrics["local_system"] = self.check_local_system()
        self.metrics["cloud_comparison"] = self.compare_with_cloud(self.metrics["local_system"])
        self.metrics["improvement_opportunities"] = self.generate_improvements(
            self.metrics["local_system"],
            self.metrics["cloud_comparison"]
        )
        
        # Save JSON data
        with open(WELLNESS_DATA, 'w') as f:
            json.dump(self.metrics, f, indent=2)
        
        print(f"✅ Wellness data saved to: {WELLNESS_DATA}")
        return self.metrics
    
    def generate_report(self) -> str:
        """Generate comprehensive wellness report (Jobs: beautiful, simple format)."""
        report = f"""# System Wellness Report
## Local vs Cloud Performance Analysis

**Copyright © 2025 Rashad West. All Rights Reserved.**

**Date:** {datetime.now().strftime('%B %d, %Y')}  
**Methodology:** AIMCODE (Hassabis + Jobs Principles)

---

## 🎯 Executive Summary

**Overall System Health:** {self._calculate_overall_health()}  
**Local vs Cloud:** {self.metrics['cloud_comparison'].get('overall', 'unknown')}

### Key Findings:
- ✅ **Local Advantages:** {len([a for a in self.metrics['cloud_comparison'].get('local_advantages', {}).values() if a])} identified
- ⚠️ **Performance Gaps:** {len(self.metrics.get('performance_gaps', []))} areas need attention
- 💡 **Improvement Opportunities:** {len(self.metrics.get('improvement_opportunities', []))} recommendations

---

## 📊 Local System Performance

### CPU Performance
- **Usage:** {self.metrics['local_system'].get('cpu', {}).get('usage_percent', 0)}%
- **Cores:** {self.metrics['local_system'].get('cpu', {}).get('core_count', 0)}
- **Status:** {self.metrics['local_system'].get('cpu', {}).get('status', 'unknown')}
- **Score:** {self.metrics['local_system'].get('cpu', {}).get('score', 0)}/100

### Memory Performance
- **Total:** {self.metrics['local_system'].get('memory', {}).get('total_gb', 0)} GB
- **Available:** {self.metrics['local_system'].get('memory', {}).get('available_gb', 0)} GB
- **Used:** {self.metrics['local_system'].get('memory', {}).get('used_percent', 0)}%
- **Status:** {self.metrics['local_system'].get('memory', {}).get('status', 'unknown')}
- **Score:** {self.metrics['local_system'].get('memory', {}).get('score', 0)}/100

### Disk Performance
- **Total:** {self.metrics['local_system'].get('disk', {}).get('total_gb', 0)} GB
- **Used:** {self.metrics['local_system'].get('disk', {}).get('used_gb', 0)} GB ({self.metrics['local_system'].get('disk', {}).get('used_percent', 0)}%)
- **Free:** {self.metrics['local_system'].get('disk', {}).get('free_gb', 0)} GB
- **Status:** {self.metrics['local_system'].get('disk', {}).get('status', 'unknown')}
- **Score:** {self.metrics['local_system'].get('disk', {}).get('score', 0)}/100

### Network Performance
- **Local Latency:** {self.metrics['local_system'].get('network', {}).get('local_latency_ms', 0)} ms
- **External Latency:** {self.metrics['local_system'].get('network', {}).get('external_latency_ms', 'N/A')} ms
- **Status:** {self.metrics['local_system'].get('network', {}).get('status', 'unknown')}
- **Score:** {self.metrics['local_system'].get('network', {}).get('score', 0)}/100

### File System
- **Total Files:** {self.metrics['local_system'].get('file_system', {}).get('total_files', 0)}
- **Large Files:** {self.metrics['local_system'].get('file_system', {}).get('large_files_count', 0)}
- **Git Size:** {self.metrics['local_system'].get('file_system', {}).get('git_size_mb', 0)} MB
- **Status:** {self.metrics['local_system'].get('file_system', {}).get('status', 'unknown')}
- **Score:** {self.metrics['local_system'].get('file_system', {}).get('score', 0)}/100

### Cursor Performance
- **Cache Size:** {self.metrics['local_system'].get('cursor_performance', {}).get('cache_size_mb', 0)} MB
- **Logs Size:** {self.metrics['local_system'].get('cursor_performance', {}).get('logs_size_mb', 0)} MB
- **Total:** {self.metrics['local_system'].get('cursor_performance', {}).get('total_size_mb', 0)} MB
- **Status:** {self.metrics['local_system'].get('cursor_performance', {}).get('status', 'unknown')}
- **Score:** {self.metrics['local_system'].get('cursor_performance', {}).get('score', 0)}/100

### Git Performance
- **Status Time:** {self.metrics['local_system'].get('git_performance', {}).get('status_time_ms', 0)} ms
- **Remote Time:** {self.metrics['local_system'].get('git_performance', {}).get('remote_time_ms', 'N/A')} ms
- **Status:** {self.metrics['local_system'].get('git_performance', {}).get('status', 'unknown')}
- **Score:** {self.metrics['local_system'].get('git_performance', {}).get('score', 0)}/100

### n8n Performance
"""
        
        # Add n8n performance details
        n8n_perf = self.metrics['local_system'].get('n8n_performance', {})
        for instance, data in n8n_perf.items():
            report += f"""
#### {instance.upper()} n8n Instance
- **URL:** {data.get('url', 'N/A')}
- **Response Time:** {data.get('response_time_ms', 'N/A')} ms
- **Status:** {data.get('status', 'unknown')}
- **Score:** {data.get('score', 0)}/100
"""
        
        report += f"""
---

## ☁️ Cloud Comparison

### Cloud Benchmarks
- **Response Time:** {self.metrics['cloud_comparison'].get('cloud_benchmarks', {}).get('response_time_ms', 0)} ms
- **Latency:** {self.metrics['cloud_comparison'].get('cloud_benchmarks', {}).get('latency_ms', 0)} ms
- **Availability:** {self.metrics['cloud_comparison'].get('cloud_benchmarks', {}).get('availability_percent', 0)}%

### Local Advantages
"""
        
        for advantage, value in self.metrics['cloud_comparison'].get('local_advantages', {}).items():
            if value:
                report += f"- ✅ **{advantage.replace('_', ' ').title()}:** {value}\n"
        
        report += f"""
### Performance Gaps
"""
        
        for gap in self.metrics.get('performance_gaps', []):
            report += f"""
- **{gap.get('metric', 'unknown')}:**
  - Local: {gap.get('local', 'N/A')}
  - Cloud: {gap.get('cloud', 'N/A')}
  - Advantage: {gap.get('advantage', 'unknown')}
  - Improvement: {gap.get('improvement', 'N/A')}
"""
        
        report += f"""
---

## 💡 Improvement Recommendations (AIMCODE Methodology)

### Demis Hassabis Approach: Systematic Deep Learning
- **Layer-by-layer analysis:** Build understanding systematically
- **Systems thinking:** Connect all components
- **Deep optimization:** Understand root causes, not symptoms

### Steve Jobs Approach: Simplicity & Beautiful Design
- **Remove complexity:** Keep only what's essential
- **Beautiful organization:** Clean, efficient systems
- **User experience first:** Fast, responsive, delightful

### Recommendations:
"""
        
        # Sort by priority
        improvements = sorted(
            self.metrics.get('improvement_opportunities', []),
            key=lambda x: {'high': 3, 'medium': 2, 'low': 1}.get(x.get('priority', 'low'), 0),
            reverse=True
        )
        
        for i, improvement in enumerate(improvements, 1):
            report += f"""
#### {i}. {improvement.get('title', 'Unknown')} ({improvement.get('priority', 'unknown').upper()})

**Description:** {improvement.get('description', 'N/A')}

**Hassabis Approach:** {improvement.get('hassabis_approach', 'N/A')}

**Jobs Approach:** {improvement.get('jobs_approach', 'N/A')}

**Action:** {improvement.get('action', 'N/A')}

---
"""
        
        report += f"""
---

## 🎯 Next Steps

1. **Review recommendations** - Prioritize high-priority items
2. **Implement improvements** - Start with highest impact items
3. **Monitor progress** - Run wellness check weekly
4. **Iterate** - Apply AIMCODE Build-Measure-Learn cycle

---

## 📊 Performance Scores Summary

| Category | Score | Status |
|----------|-------|--------|
| CPU | {self.metrics['local_system'].get('cpu', {}).get('score', 0)}/100 | {self.metrics['local_system'].get('cpu', {}).get('status', 'unknown')} |
| Memory | {self.metrics['local_system'].get('memory', {}).get('score', 0)}/100 | {self.metrics['local_system'].get('memory', {}).get('status', 'unknown')} |
| Disk | {self.metrics['local_system'].get('disk', {}).get('score', 0)}/100 | {self.metrics['local_system'].get('disk', {}).get('status', 'unknown')} |
| Network | {self.metrics['local_system'].get('network', {}).get('score', 0)}/100 | {self.metrics['local_system'].get('network', {}).get('status', 'unknown')} |
| File System | {self.metrics['local_system'].get('file_system', {}).get('score', 0)}/100 | {self.metrics['local_system'].get('file_system', {}).get('status', 'unknown')} |
| Cursor | {self.metrics['local_system'].get('cursor_performance', {}).get('score', 0)}/100 | {self.metrics['local_system'].get('cursor_performance', {}).get('status', 'unknown')} |
| Git | {self.metrics['local_system'].get('git_performance', {}).get('score', 0)}/100 | {self.metrics['local_system'].get('git_performance', {}).get('status', 'unknown')} |

**Overall Score:** {self._calculate_overall_score()}/100

---

**Generated by:** System Wellness Check (AIMCODE Methodology)  
**Report Location:** `{WELLNESS_REPORT}`  
**Data Location:** `{WELLNESS_DATA}`
"""
        
        return report
    
    def _calculate_overall_health(self) -> str:
        """Calculate overall system health."""
        scores = [
            self.metrics['local_system'].get('cpu', {}).get('score', 0),
            self.metrics['local_system'].get('memory', {}).get('score', 0),
            self.metrics['local_system'].get('disk', {}).get('score', 0),
            self.metrics['local_system'].get('network', {}).get('score', 0),
            self.metrics['local_system'].get('file_system', {}).get('score', 0),
            self.metrics['local_system'].get('cursor_performance', {}).get('score', 0),
            self.metrics['local_system'].get('git_performance', {}).get('score', 0)
        ]
        
        avg_score = sum(scores) / len(scores) if scores else 0
        
        if avg_score >= 80:
            return "✅ Excellent"
        elif avg_score >= 60:
            return "⚠️ Good (needs optimization)"
        elif avg_score >= 40:
            return "🔴 Fair (needs attention)"
        else:
            return "🚨 Poor (critical issues)"
    
    def _calculate_overall_score(self) -> int:
        """Calculate overall performance score."""
        scores = [
            self.metrics['local_system'].get('cpu', {}).get('score', 0),
            self.metrics['local_system'].get('memory', {}).get('score', 0),
            self.metrics['local_system'].get('disk', {}).get('score', 0),
            self.metrics['local_system'].get('network', {}).get('score', 0),
            self.metrics['local_system'].get('file_system', {}).get('score', 0),
            self.metrics['local_system'].get('cursor_performance', {}).get('score', 0),
            self.metrics['local_system'].get('git_performance', {}).get('score', 0)
        ]
        
        return int(sum(scores) / len(scores) if scores else 0)
    
    def run_full_check(self):
        """Run complete wellness check and generate report."""
        print("🚀 Starting System Wellness Check...")
        print("=" * 60)
        
        # Run checks
        self.save_results()
        
        # Generate report
        report = self.generate_report()
        
        # Save report
        with open(WELLNESS_REPORT, 'w') as f:
            f.write(report)
        
        print(f"✅ Wellness report saved to: {WELLNESS_REPORT}")
        print("=" * 60)
        print("\n📊 Quick Summary:")
        print(f"   Overall Health: {self._calculate_overall_health()}")
        print(f"   Overall Score: {self._calculate_overall_score()}/100")
        print(f"   Improvements Needed: {len(self.metrics.get('improvement_opportunities', []))}")
        print("\n✅ Wellness check complete!")
        
        return report


def main():
    """Main entry point."""
    checker = SystemWellnessChecker()
    checker.run_full_check()


if __name__ == "__main__":
    main()


