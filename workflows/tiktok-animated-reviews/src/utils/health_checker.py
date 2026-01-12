"""
Health Checker - JAEDS Framework
Proactive system health monitoring and issue detection

Based on research:
- Continuous monitoring and evaluation
- Proactive issue detection
- System health validation
"""

import os
import sys
import logging
from pathlib import Path
from typing import Dict, List, Optional
import subprocess

logger = logging.getLogger(__name__)


class HealthChecker:
    """
    Proactive health checker for system readiness.
    
    JAEDS Principles:
    - Jobs: Simple, clear health status
    - Alpha Evolve: Continuous monitoring
    - Demis: Research-backed health metrics
    - Superhero CV: Best practices from automation research
    """
    
    def __init__(self):
        """Initialize health checker."""
        self.checks = []
        self.issues = []
    
    def check_python_version(self) -> Dict:
        """Check Python version."""
        version = sys.version_info
        required = (3, 8)
        
        if version.major >= required[0] and version.minor >= required[1]:
            return {"status": "ok", "message": f"Python {version.major}.{version.minor}"}
        else:
            return {
                "status": "error",
                "message": f"Python {version.major}.{version.minor} (requires {required[0]}.{required[1]}+)"
            }
    
    def check_ffmpeg(self) -> Dict:
        """Check FFmpeg installation."""
        try:
            result = subprocess.run(
                ["ffmpeg", "-version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version_line = result.stdout.split('\n')[0]
                return {"status": "ok", "message": "FFmpeg installed"}
            else:
                return {"status": "error", "message": "FFmpeg not found"}
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return {"status": "error", "message": "FFmpeg not installed"}
    
    def check_dependencies(self) -> Dict:
        """Check Python dependencies."""
        required_packages = [
            "moviepy",
            "opencv-python",
            "elevenlabs"
        ]
        
        missing = []
        for package in required_packages:
            try:
                __import__(package.replace("-", "_"))
            except ImportError:
                missing.append(package)
        
        if missing:
            return {
                "status": "error",
                "message": f"Missing packages: {', '.join(missing)}"
            }
        else:
            return {"status": "ok", "message": "All dependencies installed"}
    
    def check_api_key(self) -> Dict:
        """Check if API key is set."""
        api_key = os.getenv("ELEVENLABS_API_KEY")
        if api_key:
            return {"status": "ok", "message": "API key set"}
        else:
            return {"status": "warning", "message": "API key not set in environment"}
    
    def check_character_files(self, config_path: Optional[str] = None) -> Dict:
        """Check if character files exist."""
        if not config_path:
            return {"status": "skip", "message": "No config provided"}
        
        try:
            import json
            with open(config_path, 'r') as f:
                config = json.load(f)
            
            characters = config.get("characters", {})
            missing = []
            
            for char_type, char_config in characters.items():
                file_path = char_config.get("file_path")
                if file_path and not Path(file_path).exists():
                    missing.append(f"{char_type}: {file_path}")
            
            if missing:
                return {
                    "status": "warning",
                    "message": f"Missing character files: {', '.join(missing)}"
                }
            else:
                return {"status": "ok", "message": "All character files found"}
        except Exception as e:
            return {"status": "error", "message": f"Error checking characters: {str(e)}"}
    
    def check_voice_sample(self) -> Dict:
        """Check if voice sample exists."""
        voice_sample = Path("assets/voice_samples/main_voice.mp3")
        if voice_sample.exists():
            return {"status": "ok", "message": "Voice sample found"}
        else:
            return {"status": "warning", "message": "Voice sample not found"}
    
    def check_output_directory(self) -> Dict:
        """Check if output directory is writable."""
        output_dir = Path("output/reviews")
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            test_file = output_dir / ".test_write"
            test_file.write_text("test")
            test_file.unlink()
            return {"status": "ok", "message": "Output directory writable"}
        except Exception as e:
            return {"status": "error", "message": f"Cannot write to output directory: {str(e)}"}
    
    def run_all_checks(self, config_path: Optional[str] = None) -> Dict:
        """
        Run all health checks.
        
        Returns comprehensive health report.
        """
        checks = {
            "Python Version": self.check_python_version(),
            "FFmpeg": self.check_ffmpeg(),
            "Dependencies": self.check_dependencies(),
            "API Key": self.check_api_key(),
            "Voice Sample": self.check_voice_sample(),
            "Output Directory": self.check_output_directory(),
        }
        
        if config_path:
            checks["Character Files"] = self.check_character_files(config_path)
        
        # Count statuses
        statuses = {"ok": 0, "warning": 0, "error": 0, "skip": 0}
        for check in checks.values():
            statuses[check["status"]] = statuses.get(check["status"], 0) + 1
        
        # Determine overall health
        if statuses["error"] > 0:
            overall = "unhealthy"
        elif statuses["warning"] > 0:
            overall = "degraded"
        else:
            overall = "healthy"
        
        return {
            "overall": overall,
            "checks": checks,
            "summary": statuses
        }
    
    def print_health_report(self, report: Dict):
        """Print formatted health report."""
        print("\n" + "=" * 70)
        print("  SYSTEM HEALTH CHECK")
        print("=" * 70)
        
        overall = report["overall"]
        status_icon = {
            "healthy": "✅",
            "degraded": "⚠️",
            "unhealthy": "❌"
        }
        
        print(f"\nOverall Status: {status_icon.get(overall, '❓')} {overall.upper()}\n")
        
        for check_name, check_result in report["checks"].items():
            status = check_result["status"]
            message = check_result["message"]
            
            icon = {
                "ok": "✅",
                "warning": "⚠️",
                "error": "❌",
                "skip": "⏭️"
            }.get(status, "❓")
            
            print(f"  {icon} {check_name}: {message}")
        
        print("\n" + "=" * 70 + "\n")
        
        # Recommendations
        if report["overall"] != "healthy":
            print("📋 Recommendations:")
            for check_name, check_result in report["checks"].items():
                if check_result["status"] == "error":
                    print(f"  - Fix: {check_name} - {check_result['message']}")
            print()


def main():
    """Run health check from command line."""
    import argparse
    
    parser = argparse.ArgumentParser(description="System Health Checker")
    parser.add_argument("--config", help="Path to config file")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level)
    
    # Run health check
    checker = HealthChecker()
    report = checker.run_all_checks(config_path=args.config)
    checker.print_health_report(report)
    
    # Exit with appropriate code
    if report["overall"] == "unhealthy":
        sys.exit(1)
    elif report["overall"] == "degraded":
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()

