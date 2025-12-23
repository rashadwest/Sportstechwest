#!/usr/bin/env python3
"""
Garvis Deploy All - Complete Deployment Script
Deploys website and game levels seamlessly
"""

import sys
import json
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

import importlib.util
from pathlib import Path

# Load deployment module (handles hyphen in filename)
module_path = Path(__file__).parent / "garvis-deployment-module.py"
spec = importlib.util.spec_from_file_location("garvis_deployment_module", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
GarvisDeployment = module.GarvisDeployment

def main():
    """Deploy everything"""
    print("🚀 Garvis Complete Deployment")
    print("=" * 60)
    print()
    
    deployment = GarvisDeployment()
    
    # Deploy website
    print("📦 Step 1: Deploying website...")
    website_result = deployment.deploy_website("Garvis: Deploy all UI/UX improvements and blog enhancements")
    print(f"   Status: {website_result.get('github_push', {}).get('status', 'unknown')}")
    if 'netlify_deploy' in website_result:
        print(f"   Netlify: {website_result['netlify_deploy'].get('status', 'unknown')}")
    print()
    
    # Deploy game levels
    print("🎮 Step 2: Deploying game levels...")
    level_files = [
        "book1_foundation_block.json",
        "book2_decision_crossover.json",
        "book3_pattern_loop.json"
    ]
    game_result = deployment.deploy_game_levels(level_files, "Garvis: Add Book 1, 2, 3 levels with curriculum")
    print(f"   Status: {game_result.get('github_push', {}).get('status', 'unknown')}")
    if 'unity_build' in game_result:
        print(f"   Unity Build: {game_result['unity_build'].get('status', 'unknown')}")
    print()
    
    # Summary
    print("=" * 60)
    print("✅ Deployment Complete!")
    print()
    print("Results:")
    print(f"  Website: {json.dumps(website_result, indent=2)}")
    print(f"  Game: {json.dumps(game_result, indent=2)}")
    print()
    print("Next steps:")
    print("  1. Check Netlify dashboard for deployments")
    print("  2. Verify website is updated")
    print("  3. Verify game has new levels")

if __name__ == "__main__":
    main()

