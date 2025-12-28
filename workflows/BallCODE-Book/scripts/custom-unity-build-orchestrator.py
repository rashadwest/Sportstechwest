#!/usr/bin/env python3
"""
Custom Unity CI/CD Build Orchestrator
Reverse-engineered from Unity Build Automation architecture

Purpose: Coordinate Unity builds, deployment, and notifications
Cost: FREE (uses local Mac + existing Unity license)
"""

import subprocess
import sys
import os
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

# Configuration
UNITY_PATH = "/Applications/Unity/Hub/Editor/2021.3.45f2/Unity.app/Contents/MacOS/Unity"
PROJECT_PATH = "/Users/rashadwest/BTEBallCODE"
BUILD_PATH = f"{PROJECT_PATH}/Builds/WebGL"
NETLIFY_SITE_ID = os.getenv("NETLIFY_SITE_ID", "")
NETLIFY_AUTH_TOKEN = os.getenv("NETLIFY_AUTH_TOKEN", "")
# Optional: n8n webhook (can be disabled)
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")  # Empty = disabled

class UnityBuildOrchestrator:
    """Orchestrates Unity build, deployment, and notification pipeline"""
    
    def __init__(self):
        self.build_id = f"build-{int(time.time())}"
        self.status = {
            "build_id": self.build_id,
            "status": "pending",
            "started_at": datetime.now().isoformat(),
            "steps": {}
        }
    
    def log(self, message: str, level: str = "INFO"):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")
    
    def check_prerequisites(self) -> bool:
        """Check if all prerequisites are met"""
        self.log("Checking prerequisites...")
        
        # Check Unity Editor
        if not os.path.exists(UNITY_PATH):
            self.log(f"❌ Unity Editor not found: {UNITY_PATH}", "ERROR")
            return False
        self.log(f"✅ Unity Editor found: {UNITY_PATH}")
        
        # Check project
        if not os.path.exists(f"{PROJECT_PATH}/Assets"):
            self.log(f"❌ Unity project not found: {PROJECT_PATH}", "ERROR")
            return False
        self.log(f"✅ Unity project found: {PROJECT_PATH}")
        
        # Check Netlify CLI (optional)
        netlify_available = subprocess.run(
            ["which", "netlify"], 
            capture_output=True
        ).returncode == 0
        
        if netlify_available:
            self.log("✅ Netlify CLI available")
        else:
            self.log("⚠️  Netlify CLI not found (deployment will be skipped)", "WARNING")
        
        return True
    
    def build_unity(self) -> bool:
        """Build Unity WebGL project"""
        self.log("Starting Unity WebGL build...")
        self.status["steps"]["build"] = {"status": "running", "started_at": datetime.now().isoformat()}
        
        try:
            # Create build directory
            os.makedirs(BUILD_PATH, exist_ok=True)
            
            # Run Unity build
            log_file = f"{BUILD_PATH}/build-{self.build_id}.log"
            cmd = [
                UNITY_PATH,
                "-batchmode",
                "-quit",
                "-projectPath", PROJECT_PATH,
                "-buildTarget", "WebGL",
                "-buildPath", BUILD_PATH,
                "-logFile", log_file
            ]
            
            self.log(f"Executing: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Check build result
            if result.returncode == 0 and os.path.exists(f"{BUILD_PATH}/index.html"):
                self.log("✅ Unity build successful!")
                self.status["steps"]["build"] = {
                    "status": "success",
                    "completed_at": datetime.now().isoformat(),
                    "output": BUILD_PATH
                }
                return True
            else:
                self.log(f"❌ Unity build failed (exit code: {result.returncode})", "ERROR")
                if os.path.exists(log_file):
                    with open(log_file, 'r') as f:
                        log_content = f.read()
                        self.log(f"Build log (last 20 lines):\n{log_content[-1000:]}", "ERROR")
                
                self.status["steps"]["build"] = {
                    "status": "failed",
                    "completed_at": datetime.now().isoformat(),
                    "error": f"Exit code: {result.returncode}"
                }
                return False
                
        except Exception as e:
            self.log(f"❌ Build exception: {str(e)}", "ERROR")
            self.status["steps"]["build"] = {
                "status": "failed",
                "completed_at": datetime.now().isoformat(),
                "error": str(e)
            }
            return False
    
    def verify_build(self) -> bool:
        """Verify build output"""
        self.log("Verifying build output...")
        self.status["steps"]["verify"] = {"status": "running", "started_at": datetime.now().isoformat()}
        
        required_files = ["index.html", "Build/Build.loader.js"]
        missing_files = []
        
        for file in required_files:
            file_path = f"{BUILD_PATH}/{file}"
            if not os.path.exists(file_path):
                missing_files.append(file)
        
        if missing_files:
            self.log(f"❌ Missing required files: {missing_files}", "ERROR")
            self.status["steps"]["verify"] = {
                "status": "failed",
                "completed_at": datetime.now().isoformat(),
                "error": f"Missing files: {missing_files}"
            }
            return False
        
        # Calculate build size
        build_size = self._get_directory_size(BUILD_PATH)
        self.log(f"✅ Build verified! Size: {build_size}")
        
        self.status["steps"]["verify"] = {
            "status": "success",
            "completed_at": datetime.now().isoformat(),
            "size": build_size
        }
        return True
    
    def deploy_netlify(self) -> bool:
        """Deploy to Netlify"""
        if not NETLIFY_SITE_ID or not NETLIFY_AUTH_TOKEN:
            self.log("⚠️  Netlify credentials not configured, skipping deployment", "WARNING")
            self.status["steps"]["deploy"] = {
                "status": "skipped",
                "reason": "Credentials not configured"
            }
            return True
        
        self.log("Deploying to Netlify...")
        self.status["steps"]["deploy"] = {"status": "running", "started_at": datetime.now().isoformat()}
        
        try:
            cmd = [
                "netlify", "deploy",
                "--prod",
                "--dir", BUILD_PATH,
                "--site", NETLIFY_SITE_ID,
                "--auth", NETLIFY_AUTH_TOKEN
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Extract URL from output
                url = self._extract_netlify_url(result.stdout)
                self.log(f"✅ Deployment successful! URL: {url}")
                self.status["steps"]["deploy"] = {
                    "status": "success",
                    "completed_at": datetime.now().isoformat(),
                    "url": url
                }
                return True
            else:
                self.log(f"❌ Deployment failed: {result.stderr}", "ERROR")
                self.status["steps"]["deploy"] = {
                    "status": "failed",
                    "completed_at": datetime.now().isoformat(),
                    "error": result.stderr
                }
                return False
                
        except Exception as e:
            self.log(f"❌ Deployment exception: {str(e)}", "ERROR")
            self.status["steps"]["deploy"] = {
                "status": "failed",
                "completed_at": datetime.now().isoformat(),
                "error": str(e)
            }
            return False
    
    def notify_n8n(self) -> bool:
        """Send build status to n8n webhook (optional)"""
        if not N8N_WEBHOOK_URL or N8N_WEBHOOK_URL.strip() == "":
            self.log("ℹ️  n8n webhook not configured (optional), skipping notification", "INFO")
            return True
        
        self.log("Sending notification to n8n...")
        
        try:
            import requests
            response = requests.post(
                N8N_WEBHOOK_URL,
                json=self.status,
                timeout=10
            )
            
            if response.status_code == 200:
                self.log("✅ Notification sent successfully")
                return True
            else:
                self.log(f"⚠️  Notification failed: {response.status_code}", "WARNING")
                return False
                
        except ImportError:
            self.log("⚠️  'requests' library not installed, skipping notification", "WARNING")
            return True
        except Exception as e:
            self.log(f"⚠️  Notification error: {str(e)}", "WARNING")
            return False
    
    def _get_directory_size(self, path: str) -> str:
        """Get human-readable directory size"""
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.exists(filepath):
                    total += os.path.getsize(filepath)
        
        # Convert to human-readable
        for unit in ['B', 'KB', 'MB', 'GB']:
            if total < 1024.0:
                return f"{total:.2f} {unit}"
            total /= 1024.0
        return f"{total:.2f} TB"
    
    def _extract_netlify_url(self, output: str) -> str:
        """Extract Netlify URL from deployment output"""
        for line in output.split('\n'):
            if 'Website URL:' in line or 'Live URL:' in line:
                url = line.split('URL:')[1].strip()
                return url
        return "Unknown"
    
    def run(self) -> bool:
        """Run complete build pipeline"""
        self.log("=" * 60)
        self.log("Custom Unity CI/CD Build Orchestrator")
        self.log("=" * 60)
        
        # Check prerequisites
        if not self.check_prerequisites():
            self.status["status"] = "failed"
            self.status["completed_at"] = datetime.now().isoformat()
            return False
        
        # Build
        if not self.build_unity():
            self.status["status"] = "failed"
            self.status["completed_at"] = datetime.now().isoformat()
            self.notify_n8n()
            return False
        
        # Verify
        if not self.verify_build():
            self.status["status"] = "failed"
            self.status["completed_at"] = datetime.now().isoformat()
            self.notify_n8n()
            return False
        
        # Deploy
        deploy_success = self.deploy_netlify()
        
        # Update final status
        if deploy_success:
            self.status["status"] = "success"
        else:
            self.status["status"] = "partial"  # Build succeeded but deploy failed
        
        self.status["completed_at"] = datetime.now().isoformat()
        
        # Notify
        self.notify_n8n()
        
        # Print summary
        self.log("=" * 60)
        self.log("Build Pipeline Summary")
        self.log("=" * 60)
        self.log(f"Build ID: {self.build_id}")
        self.log(f"Status: {self.status['status']}")
        self.log(f"Duration: {self._calculate_duration()}")
        self.log("=" * 60)
        
        # Save status to file
        status_file = f"{BUILD_PATH}/build-status-{self.build_id}.json"
        with open(status_file, 'w') as f:
            json.dump(self.status, f, indent=2)
        self.log(f"Status saved to: {status_file}")
        
        return self.status["status"] == "success"
    
    def _calculate_duration(self) -> str:
        """Calculate build duration"""
        try:
            started = datetime.fromisoformat(self.status["started_at"])
            completed = datetime.fromisoformat(self.status["completed_at"])
            duration = completed - started
            return str(duration)
        except:
            return "Unknown"

if __name__ == "__main__":
    orchestrator = UnityBuildOrchestrator()
    success = orchestrator.run()
    sys.exit(0 if success else 1)

