"""
Garvis Status Reporter Module
Central status tracking and reporting

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import time
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

# Status file location
STATUS_FILE = Path(__file__).parent.parent.parent / "garvis_status.json"

class StatusReporter:
    """Unified status reporting system"""
    
    def __init__(self, status_file: Path = STATUS_FILE):
        self.status_file = status_file
        self._ensure_status_file()
    
    def _ensure_status_file(self):
        """Ensure status file exists"""
        if not self.status_file.exists():
            self.status_file.parent.mkdir(parents=True, exist_ok=True)
            self._write_status({
                "last_updated": datetime.now().isoformat(),
                "components": {},
                "overall": "unknown"
            })
    
    def _read_status(self) -> Dict:
        """Read status from file"""
        try:
            with open(self.status_file, 'r') as f:
                return json.load(f)
        except Exception:
            return {
                "last_updated": datetime.now().isoformat(),
                "components": {},
                "overall": "unknown"
            }
    
    def _write_status(self, status: Dict):
        """Write status to file (thread-safe with retry)"""
        import fcntl
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                with open(self.status_file, 'w') as f:
                    fcntl.flock(f, fcntl.LOCK_EX)  # Lock file
                    json.dump(status, f, indent=2)
                    fcntl.flock(f, fcntl.LOCK_UN)  # Unlock
                return
            except (IOError, OSError) as e:
                if attempt < max_retries - 1:
                    time.sleep(0.1 * (attempt + 1))
                    continue
                # Fallback: write without lock (better than failing)
                with open(self.status_file, 'w') as f:
                    json.dump(status, f, indent=2)
    
    def report(self, component: str, status: Dict):
        """Report status for a component"""
        current = self._read_status()
        
        current["components"][component] = {
            **status,
            "last_updated": datetime.now().isoformat()
        }
        
        # Update overall status
        current["overall"] = self._calculate_overall_status(current["components"])
        current["last_updated"] = datetime.now().isoformat()
        
        self._write_status(current)
    
    def get_status(self, component: Optional[str] = None) -> Dict:
        """Get status for a component or overall status"""
        current = self._read_status()
        
        if component:
            return current["components"].get(component, {})
        
        return current
    
    def _calculate_overall_status(self, components: Dict) -> str:
        """Calculate overall system status from components"""
        if not components:
            return "unknown"
        
        statuses = [comp.get("status", "unknown") for comp in components.values()]
        
        if "error" in statuses or "failed" in statuses:
            return "error"
        elif "in_progress" in statuses or "pending" in statuses:
            return "in_progress"
        elif all(s == "success" for s in statuses):
            return "success"
        else:
            return "partial"


