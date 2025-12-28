#!/usr/bin/env python3
"""
Garvis File Watcher
BallCODE Fully Integrated System

Purpose: Auto-detect GARVIS-REQUEST.md file changes and trigger Garvis execution
"""

import sys
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

WORKFLOW_DIR = Path(__file__).parent.parent
GARVIS_REQUEST_FILE = WORKFLOW_DIR / "GARVIS-REQUEST.md"
PROCESSED_MARKER = WORKFLOW_DIR / ".garvis-processed"

class GarvisFileHandler(FileSystemEventHandler):
    """Handle file changes for GARVIS-REQUEST.md"""
    
    def __init__(self):
        self.last_processed = self._get_last_processed_time()
    
    def _get_last_processed_time(self):
        """Get last processed timestamp"""
        if PROCESSED_MARKER.exists():
            try:
                return float(PROCESSED_MARKER.read_text().strip())
            except:
                return 0
        return 0
    
    def _mark_processed(self):
        """Mark file as processed"""
        PROCESSED_MARKER.write_text(str(time.time()))
    
    def on_modified(self, event):
        """Handle file modification"""
        if event.src_path.endswith('GARVIS-REQUEST.md'):
            file_path = Path(event.src_path)
            if file_path.exists():
                # Check if file was actually modified (not just accessed)
                mtime = file_path.stat().st_mtime
                if mtime > self.last_processed:
                    print(f"\n📋 Garvis detected GARVIS-REQUEST.md change")
                    print("🚀 Starting Garvis execution...\n")
                    
                    # Trigger Garvis
                    try:
                        result = subprocess.run(
                            ['python3', str(WORKFLOW_DIR / 'scripts' / 'garvis-command.py'), '--file', str(file_path)],
                            cwd=str(WORKFLOW_DIR),
                            capture_output=True,
                            text=True,
                            timeout=300
                        )
                        print(result.stdout)
                        if result.stderr:
                            print(result.stderr, file=sys.stderr)
                        
                        self._mark_processed()
                        self.last_processed = mtime
                    except Exception as e:
                        print(f"Error executing Garvis: {str(e)}", file=sys.stderr)

def main():
    """Main file watcher"""
    if not GARVIS_REQUEST_FILE.exists():
        print(f"GARVIS-REQUEST.md not found. Creating template...")
        template = """# Garvis Request

**ONE Thing:** [Your ONE thing here]

**Tasks:**
1. [Task 1]
2. [Task 2]
3. [Task 3]

**Context:** [Optional context]

**Success Criteria:** [How to measure success]
"""
        GARVIS_REQUEST_FILE.write_text(template)
        print(f"Created {GARVIS_REQUEST_FILE}")
        print("Edit the file and save to trigger Garvis execution.")
    
    event_handler = GarvisFileHandler()
    observer = Observer()
    observer.schedule(event_handler, str(WORKFLOW_DIR), recursive=False)
    observer.start()
    
    print(f"👀 Garvis file watcher started")
    print(f"   Watching: {GARVIS_REQUEST_FILE}")
    print(f"   Edit and save GARVIS-REQUEST.md to trigger execution")
    print(f"   Press Ctrl+C to stop\n")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n👋 File watcher stopped")
    
    observer.join()

if __name__ == "__main__":
    main()


