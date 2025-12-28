#!/usr/bin/env python3
"""
n8n Wrapper Script for GitHub Actions Status Check
Outputs JSON format for n8n workflow integration

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import json
from pathlib import Path

# Add parent directory to path to import monitor-builds functions
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

try:
    from monitor_builds import get_github_status_json
except ImportError:
    # Fallback: try importing as module
    import importlib.util
    spec = importlib.util.spec_from_file_location("monitor_builds", script_dir / "monitor-builds.py")
    monitor_builds = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(monitor_builds)
    get_github_status_json = monitor_builds.get_github_status_json

def main():
    """Main function - outputs JSON for n8n."""
    try:
        result = get_github_status_json()
        # Output JSON to stdout (n8n will capture this)
        print(json.dumps(result, indent=2))
        # Exit with error code if status is error
        sys.exit(0 if result.get('status') == 'success' else 1)
    except Exception as e:
        # Return JSON error response
        error_result = {
            'status': 'error',
            'message': str(e),
            'error_type': type(e).__name__
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)

if __name__ == '__main__':
    main()


