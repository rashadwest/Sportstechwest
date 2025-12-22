#!/usr/bin/env python3
"""
n8n Wrapper Script for BallCODE Schema Updates
Outputs JSON format for n8n workflow integration

Copyright © 2025 Rashad West. All Rights Reserved.

Usage:
    python3 n8n-update-schema.py --type book --id 1 --data '{"title": "New Title"}'
    python3 n8n-update-schema.py --type curriculum --data '{"learningObjectives": [...]}'
    python3 n8n-update-schema.py --type exercise --book-id 1 --data '{"exerciseId": "ex1"}'
"""

import os
import sys
import json
import subprocess
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent
schema_script = script_dir / 'update_ballcode_schema.py'

def main():
    """Main function - calls update_ballcode_schema.py and outputs JSON for n8n."""
    if len(sys.argv) < 2:
        # If no args, return error JSON
        result = {
            'status': 'error',
            'message': 'Usage: n8n-update-schema.py --type <type> [--id <id>] [--book-id <id>] --data <json>',
            'error_type': 'MissingArguments'
        }
        print(json.dumps(result, indent=2))
        sys.exit(1)
    
    try:
        # Call the actual schema update script
        result = subprocess.run(
            [sys.executable, str(schema_script)] + sys.argv[1:],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Check if it was a dry-run (just preview)
        is_dry_run = '--dry-run' in sys.argv
        
        if result.returncode == 0:
            # Success - parse output to extract key info
            output = result.stdout
            
            # Try to extract schema info from output
            schema_result = {
                'status': 'success',
                'message': 'Schema updated successfully',
                'output': output,
                'dry_run': is_dry_run
            }
            
            # If dry-run, try to extract the preview JSON
            if is_dry_run and 'would update:' in output:
                try:
                    # Extract JSON from output (between "would update:" and next section)
                    json_start = output.find('would update:') + len('would update:')
                    json_end = output.find('\n\n✅', json_start)
                    if json_end == -1:
                        json_end = len(output)
                    json_str = output[json_start:json_end].strip()
                    schema_result['preview'] = json.loads(json_str)
                except:
                    pass
            
            print(json.dumps(schema_result, indent=2))
            sys.exit(0)
        else:
            # Error from script
            error_result = {
                'status': 'error',
                'message': result.stderr or result.stdout or 'Schema update failed',
                'error_type': 'SchemaUpdateError',
                'exit_code': result.returncode
            }
            print(json.dumps(error_result, indent=2))
            sys.exit(1)
            
    except subprocess.TimeoutExpired:
        error_result = {
            'status': 'error',
            'message': 'Schema update timed out after 30 seconds',
            'error_type': 'Timeout'
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)
    except Exception as e:
        error_result = {
            'status': 'error',
            'message': str(e),
            'error_type': type(e).__name__
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)

if __name__ == '__main__':
    main()

