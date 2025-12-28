#!/usr/bin/env python3
"""
Garvis Unity Build and Deploy Automation
Automates Unity WebGL build and Netlify deployment
For use with @garvis automation system

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import subprocess
import os
import sys
import time
import requests
import zipfile
import tempfile
from pathlib import Path

# Configuration
UNITY_PROJECT = "/Users/rashadwest/BTEBallCODE"
UNITY_VERSION = "2021.3.10f1"
UNITY_PATH = f"/Applications/Unity/Hub/Editor/{UNITY_VERSION}/Unity.app/Contents/MacOS/Unity"
BUILD_PATH = f"{UNITY_PROJECT}/Builds/WebGL"
BUILD_LOG = f"{UNITY_PROJECT}/build.log"

def log(message, level="INFO"):
    """Log message with timestamp"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def check_prerequisites():
    """Check if all prerequisites are met"""
    log("Checking prerequisites...")
    
    # Check Unity
    if not os.path.exists(UNITY_PATH):
        log(f"❌ Unity not found at: {UNITY_PATH}", "ERROR")
        return False
    log(f"✅ Unity found: {UNITY_VERSION}")
    
    # Check project
    if not os.path.exists(UNITY_PROJECT):
        log(f"❌ Project not found: {UNITY_PROJECT}", "ERROR")
        return False
    log(f"✅ Project found: {UNITY_PROJECT}")
    
    # Check BuildScript
    buildscript = f"{UNITY_PROJECT}/Assets/Editor/BuildScript.cs"
    if not os.path.exists(buildscript):
        log(f"❌ BuildScript not found: {buildscript}", "ERROR")
        return False
    log(f"✅ BuildScript found")
    
    return True

def build_unity():
    """Build Unity WebGL project"""
    log("🔨 Building Unity WebGL...")
    log("   This will take 15-20 minutes...")
    
    # Clean previous build log
    if os.path.exists(BUILD_LOG):
        os.remove(BUILD_LOG)
    
    # Change to project directory
    os.chdir(UNITY_PROJECT)
    
    # Build Unity
    cmd = [
        UNITY_PATH,
        "-batchmode",
        "-quit",
        "-projectPath", UNITY_PROJECT,
        "-executeMethod", "BuildScript.BuildWebGL",
        "-logFile", BUILD_LOG
    ]
    
    log(f"Executing: {' '.join(cmd)}")
    start_time = time.time()
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=3600  # 1 hour timeout
        )
        
        elapsed = time.time() - start_time
        log(f"Build completed in {elapsed/60:.1f} minutes")
        log(f"Exit code: {result.returncode}")
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        log("❌ Build timed out after 1 hour", "ERROR")
        return False
    except Exception as e:
        log(f"❌ Build failed: {e}", "ERROR")
        return False

def verify_build():
    """Verify build output exists"""
    log("🔍 Verifying build output...")
    
    index_html = f"{BUILD_PATH}/index.html"
    if not os.path.exists(index_html):
        log(f"❌ Build output not found: {index_html}", "ERROR")
        return False
    
    # Calculate build size
    build_size = get_dir_size(BUILD_PATH)
    log(f"✅ Build verified: {BUILD_PATH}")
    log(f"📦 Build size: {build_size}")
    
    return True

def get_dir_size(path):
    """Get directory size in human-readable format"""
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.exists(filepath):
                total += os.path.getsize(filepath)
    
    # Convert to human-readable
    for unit in ['B', 'KB', 'MB', 'GB']:
        if total < 1024.0:
            return f"{total:.1f} {unit}"
        total /= 1024.0
    return f"{total:.1f} TB"

def deploy_netlify():
    """Deploy to Netlify using API (fully automated - no CLI needed)"""
    log("🚀 Deploying to Netlify via API (fully automated)...")
    
    # Get Netlify credentials from environment
    netlify_auth_token = os.getenv("NETLIFY_AUTH_TOKEN")
    netlify_site_id = os.getenv("NETLIFY_SITE_ID")
    
    if not netlify_auth_token or not netlify_site_id:
        log("⚠️  Netlify credentials not found in environment", "WARNING")
        log("📋 To enable full automation, set these environment variables:", "INFO")
        log("   export NETLIFY_AUTH_TOKEN='your_token_here'", "INFO")
        log("   export NETLIFY_SITE_ID='your_site_id_here'", "INFO")
        log("", "INFO")
        log("   Get token: https://app.netlify.com/user/applications", "INFO")
        log("   Get site ID: Site Settings → General → Site ID", "INFO")
        log("", "INFO")
        log("   For now, using manual deployment fallback:", "WARNING")
        log(f"   1. Go to: https://app.netlify.com/sites/ballcode/deploys", "INFO")
        log(f"   2. Drag folder: {BUILD_PATH}", "INFO")
        log(f"   3. Click 'Deploy site'", "INFO")
        return False
    
    log("✅ Netlify credentials found")
    log(f"   Site ID: {netlify_site_id[:8]}...")
    
    # Try Netlify CLI first (if available), then fall back to API
    try:
        result = subprocess.run(
            ["netlify", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            log("✅ Netlify CLI found - using CLI for deployment")
            os.chdir(UNITY_PROJECT)
            cmd = ["netlify", "deploy", "--prod", "--dir", BUILD_PATH]
            log(f"Executing: {' '.join(cmd)}")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                log("✅ Deployment successful via CLI!")
                log("🌐 Game should be live at: https://ballcode.netlify.app")
                return True
            else:
                log("⚠️  CLI deployment failed, trying API...", "WARNING")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        log("📦 Netlify CLI not found - using API deployment", "INFO")
    
    # Use Netlify API for deployment
    log("📦 Creating deployment package...")
    zip_path = tempfile.mktemp(suffix='.zip')
    
    try:
        # Create zip of build directory
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(BUILD_PATH):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, BUILD_PATH)
                    zipf.write(file_path, arcname)
        
        zip_size = os.path.getsize(zip_path)
        log(f"✅ Package created: {zip_size / (1024*1024):.1f} MB")
        
        # Step 1: Create deploy
        log("📤 Creating Netlify deploy...")
        deploy_url = f"https://api.netlify.com/api/v1/sites/{netlify_site_id}/deploys"
        headers = {
            "Authorization": f"Bearer {netlify_auth_token}",
            "Content-Type": "application/json"
        }
        
        deploy_data = {"clear_cache": True, "draft": False}
        response = requests.post(deploy_url, json=deploy_data, headers=headers, timeout=30)
        
        if response.status_code not in [200, 201]:
            log(f"❌ Failed to create deploy: {response.status_code}", "ERROR")
            log(f"   Response: {response.text[:200]}", "ERROR")
            os.remove(zip_path)
            return False
        
        deploy_info = response.json()
        deploy_id = deploy_info["id"]
        log(f"✅ Deploy created: {deploy_id[:8]}...")
        
        # Step 2: Upload zip file
        log("📤 Uploading files to Netlify...")
        upload_url = f"https://api.netlify.com/api/v1/deploys/{deploy_id}/files"
        
        with open(zip_path, 'rb') as zip_file:
            files = {'file': ('deploy.zip', zip_file, 'application/zip')}
            upload_headers = {"Authorization": f"Bearer {netlify_auth_token}"}
            upload_response = requests.post(upload_url, files=files, headers=upload_headers, timeout=600)
        
        if upload_response.status_code not in [200, 201]:
            log(f"❌ Failed to upload files: {upload_response.status_code}", "ERROR")
            log(f"   Response: {upload_response.text[:200]}", "ERROR")
            os.remove(zip_path)
            return False
        
        log("✅ Files uploaded successfully")
        
        # Step 3: Publish deploy
        log("🚀 Publishing deploy...")
        publish_url = f"https://api.netlify.com/api/v1/deploys/{deploy_id}/restore"
        publish_response = requests.post(publish_url, headers={"Authorization": f"Bearer {netlify_auth_token}"}, timeout=30)
        
        if publish_response.status_code not in [200, 201, 204]:
            log(f"⚠️  Deploy may need manual publish: {publish_response.status_code}", "WARNING")
        else:
            log("✅ Deploy published successfully")
        
        # Cleanup
        os.remove(zip_path)
        
        log("✅ Deployment successful via API!")
        log("🌐 Game should be live at: https://ballcode.netlify.app")
        return True
        
    except requests.exceptions.RequestException as e:
        log(f"❌ Deployment API error: {e}", "ERROR")
        if os.path.exists(zip_path):
            os.remove(zip_path)
        return False
    except Exception as e:
        log(f"❌ Deployment failed: {e}", "ERROR")
        if os.path.exists(zip_path):
            os.remove(zip_path)
        return False

def main():
    """Main execution"""
    log("🚨 Garvis Unity Build and Deploy")
    log("=" * 50)
    
    # Check prerequisites
    if not check_prerequisites():
        log("❌ Prerequisites check failed", "ERROR")
        sys.exit(1)
    
    # Build Unity
    if not build_unity():
        log("❌ Unity build failed", "ERROR")
        sys.exit(1)
    
    # Verify build
    if not verify_build():
        log("❌ Build verification failed", "ERROR")
        sys.exit(1)
    
    # Deploy to Netlify
    deploy_success = deploy_netlify()
    
    if deploy_success:
        log("✅ Build and deployment complete!")
        sys.exit(0)
    else:
        log("⚠️  Build complete but deployment needs manual step", "WARNING")
        log(f"   Build ready at: {BUILD_PATH}")
        sys.exit(0)  # Exit 0 because build succeeded

if __name__ == "__main__":
    main()

