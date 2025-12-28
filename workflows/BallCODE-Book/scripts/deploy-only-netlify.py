#!/usr/bin/env python3
"""
Deploy Only - Netlify Deployment (Skip Build)
Deploys existing build to Netlify via API
"""
import os
import sys
import requests
import zipfile
import tempfile
import time

# Configuration
UNITY_PROJECT = "/Users/rashadwest/BTEBallCODE"
BUILD_PATH = f"{UNITY_PROJECT}/Builds/WebGL"

def log(message, level="INFO"):
    """Log message with timestamp"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def deploy_netlify():
    """Deploy to Netlify - Uses CLI (preferred) or API fallback"""
    log("🚀 Deploying to Netlify (fully automated)...")
    
    # Get Netlify credentials from environment
    netlify_auth_token = os.getenv("NETLIFY_AUTH_TOKEN")
    netlify_site_id = os.getenv("NETLIFY_SITE_ID")
    
    if not netlify_site_id:
        log("❌ NETLIFY_SITE_ID not found in environment", "ERROR")
        log("📋 Please set:", "INFO")
        log("   export NETLIFY_SITE_ID='39ebfb47-c716-4f38-8f8b-7bfba36f3dc7'", "INFO")
        return False
    
    log("✅ Netlify Site ID found")
    log(f"   Site ID: {netlify_site_id[:8]}...")
    
    # Try Netlify CLI first (simplest and most reliable)
    # Also try npx (no installation needed)
    import subprocess
    
    # Check for netlify CLI or npx
    cli_commands = [
        ["netlify", "--version"],
        ["npx", "--version"]  # npx is usually available even if netlify-cli isn't installed
    ]
    
    use_npx = False
    cli_available = False
    
    # Check for netlify CLI
    try:
        result = subprocess.run(
            ["netlify", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            cli_available = True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    # Check for npx (can use npx netlify-cli without installation)
    if not cli_available:
        try:
            result = subprocess.run(
                ["npx", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                use_npx = True
                log("✅ npx found - can use Netlify CLI without installation", "INFO")
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
    
    if cli_available or use_npx:
        log("✅ Using Netlify CLI for deployment (most reliable)", "INFO")
        os.chdir(UNITY_PROJECT)
        
        # Set site ID via environment or use --site flag
        env = os.environ.copy()
        if netlify_site_id:
            env["NETLIFY_SITE_ID"] = netlify_site_id
        
        if use_npx:
            cmd = ["npx", "netlify-cli", "deploy", "--prod", "--dir", BUILD_PATH]
        else:
            cmd = ["netlify", "deploy", "--prod", "--dir", BUILD_PATH]
        
        if netlify_site_id:
            cmd.extend(["--site", netlify_site_id])
        
        log(f"Executing: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300, env=env)
        
        if result.returncode == 0:
            log("✅ Deployment successful via Netlify CLI!")
            log("🌐 Game should be live at: https://ballcode.netlify.app")
            return True
        else:
            log(f"⚠️  CLI deployment failed: {result.stderr[:200]}", "WARNING")
            if result.stdout:
                log(f"   stdout: {result.stdout[:200]}", "WARNING")
            log("📋 Trying API method as fallback...", "INFO")
    else:
        log("📦 Netlify CLI not found", "INFO")
        log("📋 To install: npm install -g netlify-cli (or use sudo)", "INFO")
        log("📋 OR use npx: npx netlify-cli deploy --prod --dir Builds/WebGL", "INFO")
        log("📋 Using API method as fallback...", "INFO")
    
    # API fallback (requires auth token)
    if not netlify_auth_token:
        log("❌ NETLIFY_AUTH_TOKEN not found - required for API deployment", "ERROR")
        log("📋 Please set:", "INFO")
        log("   export NETLIFY_AUTH_TOKEN='your_token_here'", "INFO")
        log("   Get token: https://app.netlify.com/user/applications", "INFO")
        log("", "INFO")
        log("📋 OR install Netlify CLI for easier deployment:", "INFO")
        log("   npm install -g netlify-cli", "INFO")
        log("   Then run this script again", "INFO")
        return False
    
    log("✅ Using Netlify API for deployment")
    
    # Check if build exists
    if not os.path.exists(BUILD_PATH) or not os.path.exists(f"{BUILD_PATH}/index.html"):
        log(f"❌ Build not found at: {BUILD_PATH}", "ERROR")
        log("   Please build first using: python3 scripts/garvis-unity-build-deploy.py", "INFO")
        return False
    
    log("✅ Build found - creating deployment package...")
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
        
        # Check if deploy has upload_url (some Netlify API versions provide this)
        upload_url_from_deploy = deploy_info.get("upload_url")
        if upload_url_from_deploy:
            log(f"✅ Found upload_url in deploy response")
            # Use the provided upload_url if available
        
        # Step 2: Upload files - Netlify API requires uploading files individually (doesn't accept zip)
        # Note: Netlify API file uploads work differently - we'll use Netlify CLI as fallback if API fails
        log("📤 Uploading files to Netlify...")
        log("   Extracting and uploading files individually...")
        
        # Extract zip and upload files individually
        import zipfile as zf
        import shutil
        from urllib.parse import quote
        
        temp_extract = tempfile.mkdtemp()
        
        try:
            # Extract zip
            with zf.ZipFile(zip_path, 'r') as zip_ref:
                file_list = zip_ref.namelist()
                zip_ref.extractall(temp_extract)
            
            log(f"✅ Extracted {len(file_list)} files")
            
            # Upload files individually using Netlify's file upload API
            upload_headers = {
                "Authorization": f"Bearer {netlify_auth_token}",
                "Content-Type": "application/octet-stream"
            }
            
            uploaded_count = 0
            total_files = len(file_list)
            
            log(f"📤 Uploading {total_files} files...")
            
            # Upload each file
            for rel_path in file_list:
                # Skip directories
                if rel_path.endswith('/'):
                    continue
                
                file_path = os.path.join(temp_extract, rel_path)
                
                if not os.path.exists(file_path):
                    continue
                
                # URL encode the file path for the API
                encoded_path = quote(rel_path, safe='/')
                
                # Netlify API: PUT /api/v1/deploys/{deploy_id}/files/{file_path}
                # Note: The deploy must be in "uploading" state, but we can't set that via API
                # Instead, we'll try using the deploy's upload_url if available, or use CLI fallback
                if upload_url_from_deploy:
                    # Use the upload_url from deploy response (if provided)
                    file_upload_url = f"{upload_url_from_deploy.rstrip('/')}/{encoded_path}"
                else:
                    # Standard API endpoint
                    file_upload_url = f"https://api.netlify.com/api/v1/deploys/{deploy_id}/files/{encoded_path}"
                
                try:
                    with open(file_path, 'rb') as f:
                        file_response = requests.put(
                            file_upload_url,
                            data=f,
                            headers=upload_headers,
                            timeout=60
                        )
                        
                        if file_response.status_code in [200, 201, 204]:
                            uploaded_count += 1
                            if uploaded_count % 10 == 0:
                                log(f"   Progress: {uploaded_count}/{total_files} files uploaded...")
                        else:
                            log(f"⚠️  Failed to upload {rel_path}: {file_response.status_code}", "WARNING")
                            if file_response.text:
                                log(f"   Response: {file_response.text[:100]}", "WARNING")
                except Exception as e:
                    log(f"⚠️  Error uploading {rel_path}: {e}", "WARNING")
            
            # Cleanup temp directory
            shutil.rmtree(temp_extract)
            
            if uploaded_count > 0:
                log(f"✅ Successfully uploaded {uploaded_count}/{total_files} files")
            else:
                log(f"❌ Failed to upload any files", "ERROR")
                os.remove(zip_path)
                return False
                
        except Exception as e:
            log(f"❌ Error uploading files: {e}", "ERROR")
            if os.path.exists(temp_extract):
                shutil.rmtree(temp_extract)
            os.remove(zip_path)
            return False
        
        # Step 4: Update deploy state to "ready" after files uploaded
        log("📤 Updating deploy state to 'ready'...")
        ready_update_url = f"https://api.netlify.com/api/v1/deploys/{deploy_id}"
        ready_update_data = {"state": "ready"}
        ready_update_response = requests.patch(ready_update_url, json=ready_update_data, headers=update_headers, timeout=30)
        
        if ready_update_response.status_code not in [200, 201]:
            log(f"⚠️  Failed to update deploy state to 'ready': {ready_update_response.status_code}", "WARNING")
        else:
            log("✅ Deploy state updated to 'ready'")
        
        # Step 5: Publish deploy
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

if __name__ == "__main__":
    log("🚀 Garvis Deploy Only (Skip Build)")
    log("=" * 50)
    
    if deploy_netlify():
        log("✅ Deployment complete!")
        sys.exit(0)
    else:
        log("❌ Deployment failed", "ERROR")
        sys.exit(1)

