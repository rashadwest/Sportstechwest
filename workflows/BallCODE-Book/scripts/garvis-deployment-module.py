#!/usr/bin/env python3
"""
Garvis Deployment Module
Handles GitHub pushes, Netlify deployments, and game level deployments
All automated - no manual steps required
"""

import os
import sys
import subprocess
import requests
import json
from pathlib import Path
from typing import Dict, Optional, List
import logging

logger = logging.getLogger('garvis.deployment')

# Repository paths
WEBSITE_REPO_PATH = Path("/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/BallCode")
GAME_LEVELS_PATH = Path("/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts/Levels")

# Repository URLs
WEBSITE_REPO = "rashadwest/BallCode"
GAME_REPO = "rashadwest/BTEBallCODE"

# API endpoints
GITHUB_API_BASE = "https://api.github.com"
NETLIFY_API_BASE = "https://api.netlify.com/api/v1"

class GarvisDeployment:
    """Garvis Deployment Module - Handles all deployments"""
    
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN") or os.getenv("GITHUB_PAT")
        self.netlify_token = os.getenv("NETLIFY_AUTH_TOKEN")
        self.netlify_site_id_website = os.getenv("NETLIFY_SITE_ID_WEBSITE")
        self.netlify_site_id_game = os.getenv("NETLIFY_SITE_ID_GAME")
        self.n8n_url = os.getenv("N8N_BASE_URL", "http://192.168.1.226:5678")
    
    def deploy_website(self, commit_message: str = "Garvis: Deploy website updates") -> Dict:
        """Deploy website: Push to GitHub + Trigger Netlify"""
        logger.info("Starting website deployment...")
        results = {}
        
        # Step 1: Push to GitHub
        try:
            result = self._push_to_github(WEBSITE_REPO_PATH, WEBSITE_REPO, commit_message)
            results['github_push'] = result
            logger.info(f"GitHub push: {result['status']}")
        except Exception as e:
            logger.error(f"GitHub push failed: {str(e)}")
            results['github_push'] = {'status': 'error', 'error': str(e)}
            return results
        
        # Step 2: Trigger Netlify deployment
        if self.netlify_token and self.netlify_site_id_website:
            try:
                result = self._trigger_netlify_deploy(self.netlify_site_id_website)
                results['netlify_deploy'] = result
                logger.info(f"Netlify deploy: {result['status']}")
            except Exception as e:
                logger.error(f"Netlify deploy failed: {str(e)}")
                results['netlify_deploy'] = {'status': 'error', 'error': str(e)}
        else:
            logger.warning("Netlify credentials not available - relying on auto-deploy")
            results['netlify_deploy'] = {
                'status': 'skipped',
                'note': 'Netlify auto-deploy will handle if connected to GitHub'
            }
        
        return results
    
    def deploy_game_levels(self, levels: List[str], commit_message: str = "Garvis: Add book levels") -> Dict:
        """Deploy game levels: Push to Unity repo + Trigger build"""
        logger.info(f"Starting game deployment for levels: {levels}")
        results = {}
        
        # Step 1: Push levels to Unity repo via GitHub API
        try:
            result = self._push_levels_to_github(levels, commit_message)
            results['github_push'] = result
            logger.info(f"GitHub push: {result['status']}")
        except Exception as e:
            logger.error(f"GitHub push failed: {str(e)}")
            results['github_push'] = {'status': 'error', 'error': str(e)}
            return results
        
        # Step 2: Trigger Unity build via n8n
        try:
            result = self._trigger_unity_build()
            results['unity_build'] = result
            logger.info(f"Unity build trigger: {result['status']}")
        except Exception as e:
            logger.error(f"Unity build trigger failed: {str(e)}")
            results['unity_build'] = {'status': 'error', 'error': str(e)}
        
        return results
    
    def _push_to_github(self, repo_path: Path, repo_name: str, commit_message: str) -> Dict:
        """Push changes to GitHub repository"""
        try:
            # Check if there are changes
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=repo_path,
                capture_output=True,
                text=True
            )
            
            if not result.stdout.strip():
                return {
                    'status': 'skipped',
                    'message': 'No changes to commit'
                }
            
            # Add all changes
            subprocess.run(
                ["git", "add", "-A"],
                cwd=repo_path,
                check=True
            )
            
            # Commit
            subprocess.run(
                ["git", "commit", "-m", commit_message],
                cwd=repo_path,
                check=True
            )
            
            # Push
            push_result = subprocess.run(
                ["git", "push", "origin", "main"],
                cwd=repo_path,
                capture_output=True,
                text=True
            )
            
            if push_result.returncode == 0:
                return {
                    'status': 'success',
                    'message': f'Pushed to {repo_name}',
                    'output': push_result.stdout
                }
            else:
                return {
                    'status': 'error',
                    'error': push_result.stderr
                }
        except subprocess.CalledProcessError as e:
            return {
                'status': 'error',
                'error': str(e)
            }
    
    def _push_levels_to_github(self, levels: List[str], commit_message: str) -> Dict:
        """Push level files to Unity repository via GitHub API"""
        if not self.github_token:
            return {
                'status': 'error',
                'error': 'GitHub token not available'
            }
        
        # For now, use git commands if repo is cloned locally
        # In future, can use GitHub API to create files directly
        unity_repo_path = Path("/Users/rashadwest/Sportstechwest/workflows/BallCODE-Book/Unity-Scripts")
        
        # Check if we can push via git
        if (unity_repo_path / ".git").exists():
            # Copy level files to repo
            target_path = unity_repo_path / "Assets" / "StreamingAssets" / "Levels"
            target_path.mkdir(parents=True, exist_ok=True)
            
            for level_file in levels:
                source = GAME_LEVELS_PATH / level_file
                if source.exists():
                    import shutil
                    shutil.copy(source, target_path / level_file)
            
            # Push via git
            return self._push_to_github(unity_repo_path, GAME_REPO, commit_message)
        else:
            # Use GitHub API to create files
            return self._create_files_via_github_api(levels, commit_message)
    
    def _create_files_via_github_api(self, levels: List[str], commit_message: str) -> Dict:
        """Create files in GitHub repository via API"""
        results = []
        
        for level_file in levels:
            source_path = GAME_LEVELS_PATH / level_file
            if not source_path.exists():
                continue
            
            content = source_path.read_text()
            import base64
            content_b64 = base64.b64encode(content.encode()).decode()
            
            # GitHub API: Create or update file
            url = f"{GITHUB_API_BASE}/repos/{GAME_REPO}/contents/Assets/StreamingAssets/Levels/{level_file}"
            headers = {
                "Authorization": f"token {self.github_token}",
                "Accept": "application/vnd.github.v3+json"
            }
            
            # Check if file exists
            check_response = requests.get(url, headers=headers)
            
            data = {
                "message": commit_message,
                "content": content_b64,
                "branch": "main"
            }
            
            if check_response.status_code == 200:
                # File exists - update it
                existing_file = check_response.json()
                data["sha"] = existing_file["sha"]
                method = "PUT"
            else:
                # File doesn't exist - create it
                method = "PUT"
            
            response = requests.request(method, url, headers=headers, json=data)
            
            if response.status_code in [200, 201]:
                results.append({
                    'file': level_file,
                    'status': 'success'
                })
            else:
                results.append({
                    'file': level_file,
                    'status': 'error',
                    'error': response.text
                })
        
        return {
            'status': 'success' if all(r['status'] == 'success' for r in results) else 'partial',
            'results': results
        }
    
    def _trigger_netlify_deploy(self, site_id: str) -> Dict:
        """Trigger Netlify deployment via API"""
        if not self.netlify_token:
            return {
                'status': 'error',
                'error': 'Netlify token not available'
            }
        
        url = f"{NETLIFY_API_BASE}/sites/{site_id}/deploys"
        headers = {
            "Authorization": f"Bearer {self.netlify_token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "branch": "main"
        }
        
        try:
            response = requests.post(url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            
            deploy_data = response.json()
            return {
                'status': 'success',
                'deploy_id': deploy_data.get('id'),
                'deploy_url': deploy_data.get('deploy_url'),
                'message': 'Netlify deployment triggered'
            }
        except requests.exceptions.RequestException as e:
            return {
                'status': 'error',
                'error': str(e)
            }
    
    def _trigger_unity_build(self) -> Dict:
        """Trigger Unity build via n8n webhook"""
        url = f"{self.n8n_url}/webhook/unity-build"
        payload = {
            "request": "Build with Book 1, 2, 3 levels",
            "branch": "main",
            "source": "garvis"
        }
        
        try:
            response = requests.post(url, json=payload, timeout=30)
            response.raise_for_status()
            
            return {
                'status': 'success',
                'message': 'Unity build triggered',
                'response': response.json() if response.content else {}
            }
        except requests.exceptions.RequestException as e:
            return {
                'status': 'error',
                'error': str(e)
            }
    
    def deploy_all(self, website_commit: str = "Garvis: Deploy all updates", 
                   game_commit: str = "Garvis: Add book levels") -> Dict:
        """Deploy both website and game"""
        results = {
            'website': {},
            'game': {}
        }
        
        # Deploy website
        results['website'] = self.deploy_website(website_commit)
        
        # Deploy game levels
        level_files = [
            "book1_foundation_block.json",
            "book2_decision_crossover.json",
            "book3_pattern_loop.json"
        ]
        results['game'] = self.deploy_game_levels(level_files, game_commit)
        
        return results


