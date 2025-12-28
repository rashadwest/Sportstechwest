#!/usr/bin/env python3
"""
Full Integration: Multi-tenant Support
Manages multiple users/projects with isolated contexts.

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Optional

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
TENANTS_DIR = PROJECT_ROOT / ".tenants"

def create_tenant(tenant_id: str, tenant_config_json: str) -> dict:
    """Create a new tenant with isolated context."""
    try:
        # Parse tenant config
        if isinstance(tenant_config_json, str):
            try:
                tenant_config = json.loads(tenant_config_json)
            except json.JSONDecodeError:
                import re
                json_match = re.search(r'\{[\s\S]*\}', tenant_config_json)
                if json_match:
                    tenant_config = json.loads(json_match.group(0))
                else:
                    raise ValueError("Could not parse JSON from input")
        else:
            tenant_config = tenant_config_json
        
        results = {
            "status": "success",
            "tenant_created": False,
            "tenant_id": tenant_id,
            "tenant_path": "",
            "errors": []
        }
        
        # Create tenant directory
        tenant_path = TENANTS_DIR / tenant_id
        tenant_path.mkdir(parents=True, exist_ok=True)
        
        # Create tenant config file
        config_file = tenant_path / "config.json"
        tenant_data = {
            "tenant_id": tenant_id,
            "created_at": tenant_config.get("created_at", ""),
            "config": tenant_config
        }
        config_file.write_text(json.dumps(tenant_data, indent=2), encoding='utf-8')
        
        # Create isolated directories
        (tenant_path / "memory").mkdir(exist_ok=True)
        (tenant_path / "logs").mkdir(exist_ok=True)
        (tenant_path / "data").mkdir(exist_ok=True)
        
        results["tenant_created"] = True
        results["tenant_path"] = str(tenant_path)
        
        return results
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "tenant_created": False,
            "errors": [str(e)]
        }

def get_tenant_context(tenant_id: str) -> dict:
    """Get tenant context and configuration."""
    try:
        tenant_path = TENANTS_DIR / tenant_id
        
        if not tenant_path.exists():
            return {
                "status": "error",
                "error": f"Tenant {tenant_id} not found",
                "tenant_id": tenant_id
            }
        
        # Load tenant config
        config_file = tenant_path / "config.json"
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                tenant_data = json.load(f)
        else:
            tenant_data = {"tenant_id": tenant_id, "config": {}}
        
        return {
            "status": "success",
            "tenant_id": tenant_id,
            "tenant_data": tenant_data,
            "tenant_path": str(tenant_path)
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "tenant_id": tenant_id
        }

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Multi-tenant Support")
    parser.add_argument("--create", help="Create tenant with ID")
    parser.add_argument("--config", help="Tenant config (JSON)")
    parser.add_argument("--get", help="Get tenant context for ID")
    
    args = parser.parse_args()
    
    if args.create:
        config_json = args.config if args.config else '{"created_at": ""}'
        result = create_tenant(args.create, config_json)
        print(json.dumps(result, indent=2))
        
        if result.get("status") == "error":
            sys.exit(1)
    
    elif args.get:
        result = get_tenant_context(args.get)
        print(json.dumps(result, indent=2))
        
        if result.get("status") == "error":
            sys.exit(1)
    
    else:
        print("Usage: --create <tenant_id> [--config <json>] or --get <tenant_id>")
        sys.exit(1)


