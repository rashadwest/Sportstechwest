#!/usr/bin/env python3
"""
Automated Notion blog post creation - reads MCP config and creates page directly
"""

import os
import json
import sys
from pathlib import Path

def get_notion_token_from_mcp_config():
    """Extract Notion API token from MCP config"""
    config_paths = [
        Path.home() / ".cursor" / "mcp.json",
        Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    ]
    
    for config_path in config_paths:
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    servers = config.get('mcpServers', {})
                    notion_config = servers.get('Notion', {})
                    env = notion_config.get('env', {})
                    token = env.get('NOTION_API_KEY') or env.get('NOTION_API_TOKEN')
                    if token:
                        return token
            except Exception as e:
                continue
    return None

# Get token from MCP config
NOTION_TOKEN = get_notion_token_from_mcp_config()

if not NOTION_TOKEN:
    NOTION_TOKEN = os.getenv("NOTION_API_TOKEN")

if not NOTION_TOKEN:
    print("❌ Could not find Notion API token.")
    print("   Please either:")
    print("   1. Set NOTION_API_TOKEN environment variable")
    print("   2. Ensure your ~/.cursor/mcp.json has NOTION_API_KEY in the Notion server config")
    sys.exit(1)

print(f"✅ Found Notion API token (length: {len(NOTION_TOKEN)})")
print("🚀 Creating Notion page...")

# Now import and run the main script
sys.path.insert(0, os.path.dirname(__file__))
from create_24_7_blog_notion import create_blog_post

# Override the token in the module
import create_24_7_blog_notion
create_24_7_blog_notion.notion = __import__('notion_client').Client(auth=NOTION_TOKEN)

# Create the page
url = create_blog_post()

if url:
    print(f"\n✅ Success! Notion Page URL: {url}")
else:
    print("\n❌ Failed to create page. Check the error above.")

