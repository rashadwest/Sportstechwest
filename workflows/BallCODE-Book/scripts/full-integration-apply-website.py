#!/usr/bin/env python3
"""
Full Integration: Apply Website Updates
Takes AI-generated website updates and applies them to the website system.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
WEBSITE_DIR = PROJECT_ROOT / "BallCode"

def apply_website_updates(website_updates_json: str) -> dict:
    """Apply website updates from AI generation."""
    try:
        # Parse AI-generated JSON
        if isinstance(website_updates_json, str):
            try:
                updates = json.loads(website_updates_json)
            except json.JSONDecodeError:
                # Try to extract JSON from markdown or text
                import re
                json_match = re.search(r'\{[\s\S]*\}', website_updates_json)
                if json_match:
                    updates = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            updates = website_updates_json
        
        results = {
            "status": "success",
            "files_updated": [],
            "files_created": [],
            "errors": []
        }
        
        # Extract updates
        html_files = updates.get('htmlFiles', [])
        css_updates = updates.get('cssUpdates', [])
        js_updates = updates.get('jsUpdates', [])
        website_config = updates.get('websiteConfig', {})
        
        # Apply HTML files
        for html_file in html_files:
            try:
                file_path_str = html_file.get('path', '')
                content = html_file.get('content', '')
                
                if not file_path_str or not content:
                    results["errors"].append(f"Invalid HTML file data: missing path or content")
                    continue
                
                file_path = WEBSITE_DIR / file_path_str
                file_path.parent.mkdir(parents=True, exist_ok=True)
                
                file_existed = file_path.exists()
                file_path.write_text(content, encoding='utf-8')
                
                if file_existed:
                    results["files_updated"].append(str(file_path))
                else:
                    results["files_created"].append(str(file_path))
                    
            except Exception as e:
                results["errors"].append(f"Error applying HTML file {html_file.get('path', 'unknown')}: {str(e)}")
        
        # Apply CSS updates
        for css_update in css_updates:
            try:
                file_name = css_update.get('file', '')
                styles = css_update.get('styles', '')
                
                if not file_name or not styles:
                    results["errors"].append(f"Invalid CSS update data: missing file or styles")
                    continue
                
                file_path = WEBSITE_DIR / file_name
                
                if file_path.exists():
                    # Append to existing file
                    existing_content = file_path.read_text(encoding='utf-8')
                    file_path.write_text(f"{existing_content}\n\n/* Full Integration Update */\n{styles}", encoding='utf-8')
                    results["files_updated"].append(str(file_path))
                else:
                    # Create new file
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    file_path.write_text(styles, encoding='utf-8')
                    results["files_created"].append(str(file_path))
                    
            except Exception as e:
                results["errors"].append(f"Error applying CSS update {css_update.get('file', 'unknown')}: {str(e)}")
        
        # Apply JS updates
        for js_update in js_updates:
            try:
                file_name = js_update.get('file', '')
                code = js_update.get('code', '')
                
                if not file_name or not code:
                    results["errors"].append(f"Invalid JS update data: missing file or code")
                    continue
                
                file_path = WEBSITE_DIR / file_name
                
                if file_path.exists():
                    # Append to existing file
                    existing_content = file_path.read_text(encoding='utf-8')
                    file_path.write_text(f"{existing_content}\n\n/* Full Integration Update */\n{code}", encoding='utf-8')
                    results["files_updated"].append(str(file_path))
                else:
                    # Create new file
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    file_path.write_text(code, encoding='utf-8')
                    results["files_created"].append(str(file_path))
                    
            except Exception as e:
                results["errors"].append(f"Error applying JS update {js_update.get('file', 'unknown')}: {str(e)}")
        
        # Save website config if provided
        if website_config:
            try:
                config_path = WEBSITE_DIR / "data" / "website-config.json"
                config_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Merge with existing config if it exists
                if config_path.exists():
                    existing_config = json.loads(config_path.read_text(encoding='utf-8'))
                    existing_config.update(website_config)
                    website_config = existing_config
                
                config_path.write_text(json.dumps(website_config, indent=2), encoding='utf-8')
                results["files_updated"].append(str(config_path))
            except Exception as e:
                results["errors"].append(f"Error saving website config: {str(e)}")
        
        # Determine overall status
        if results["errors"]:
            results["status"] = "partial" if (results["files_updated"] or results["files_created"]) else "error"
        else:
            results["status"] = "success"
        
        results["summary"] = {
            "html_files": len(html_files),
            "css_updates": len(css_updates),
            "js_updates": len(js_updates),
            "files_updated_count": len(results["files_updated"]),
            "files_created_count": len(results["files_created"]),
            "errors_count": len(results["errors"])
        }
        
        # Deployment automation: Deploy website if updates were successful
        if results["status"] in ["success", "partial"] and (results["files_updated"] or results["files_created"]):
            try:
                import subprocess
                deploy_script = SCRIPTS_DIR / "garvis-deploy.py"
                if deploy_script.exists():
                    deploy_process = subprocess.run(
                        [sys.executable, str(deploy_script), "--website"],
                        capture_output=True,
                        text=True,
                        timeout=300,
                        encoding='utf-8'
                    )
                    if deploy_process.returncode == 0:
                        results["deployment"] = {
                            "status": "success",
                            "message": "Website deployed successfully"
                        }
                    else:
                        results["deployment"] = {
                            "status": "error",
                            "error": deploy_process.stderr or "Deployment failed",
                            "stdout": deploy_process.stdout
                        }
                        results["errors"].append(f"Website deployment failed: {deploy_process.stderr}")
                else:
                    results["deployment"] = {
                        "status": "skipped",
                        "message": "garvis-deploy.py not found"
                    }
            except subprocess.TimeoutExpired:
                results["deployment"] = {
                    "status": "error",
                    "error": "Deployment timeout"
                }
                results["errors"].append("Website deployment timeout")
            except Exception as e:
                results["deployment"] = {
                    "status": "error",
                    "error": str(e)
                }
                results["errors"].append(f"Website deployment error: {str(e)}")
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "files_updated": [],
            "files_created": [],
            "errors": [str(e)]
        }

if __name__ == "__main__":
    # Read from stdin or file argument
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        if input_path.exists():
            input_json = input_path.read_text(encoding='utf-8')
        else:
            input_json = sys.argv[1]  # Treat as JSON string
    else:
        input_json = sys.stdin.read()
    
    result = apply_website_updates(input_json)
    print(json.dumps(result, indent=2))
    
    # Exit with error code if failed
    if result.get("status") == "error":
        sys.exit(1)


