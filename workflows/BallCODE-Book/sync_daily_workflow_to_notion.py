#!/usr/bin/env python3
"""
Sync Daily Workflow files to Notion.

This script reads your local daily workflow markdown files and syncs them
to a Notion database for daily productivity tracking.

Requirements:
    pip install notion-client

Setup:
    1. Get Notion integration token from https://www.notion.so/my-integrations
    2. Share your Notion database/page with the integration
    3. Set NOTION_API_KEY environment variable or update the script
    4. Update DATABASE_ID with your Notion database ID
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

try:
    from notion_client import Client
except ImportError:
    print("Error: notion-client not installed. Run: pip install notion-client")
    exit(1)


# Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY", "your-notion-api-key-here")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID", "your-database-id-here")

# File paths
WORKFLOW_DIR = Path(__file__).parent
START_HERE_FILE = WORKFLOW_DIR / "START-HERE-DAILY-WORKFLOW.md"
DAILY_TEMPLATE_FILE = WORKFLOW_DIR / "DAILY-WORKFLOW-TEMPLATE.md"
PRE_WORK_FILE = WORKFLOW_DIR / "PRE-WORK-QUESTIONNAIRE.md"


def parse_markdown_file(file_path: Path) -> str:
    """Read and return markdown file content."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: File not found: {file_path}")
        return ""


def markdown_to_notion_blocks(markdown: str) -> List[Dict]:
    """Convert markdown content to Notion blocks."""
    blocks = []
    lines = markdown.split("\n")
    
    for line in lines:
        line = line.rstrip()
        
        if not line:
            continue
        
        # Headers
        if line.startswith("# "):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"type": "text", "text": {"content": line[2:].strip()}}]
                }
            })
        elif line.startswith("## "):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": line[3:].strip()}}]
                }
            })
        elif line.startswith("### "):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": line[4:].strip()}}]
                }
            })
        # Bullet points
        elif line.strip().startswith("- "):
            content = line.strip()[2:]
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"type": "text", "text": {"content": content}}]
                }
            })
        # Checkboxes
        elif line.strip().startswith("- [ ]"):
            content = line.strip()[5:].strip()
            blocks.append({
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": [{"type": "text", "text": {"content": content}}],
                    "checked": False
                }
            })
        elif line.strip().startswith("- [x]") or line.strip().startswith("- [X]"):
            content = line.strip()[5:].strip()
            blocks.append({
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": [{"type": "text", "text": {"content": content}}],
                    "checked": True
                }
            })
        # Horizontal rule
        elif line.strip() == "---":
            blocks.append({
                "object": "block",
                "type": "divider",
                "divider": {}
            })
        # Regular paragraph
        else:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": line}}]
                }
            })
    
    return blocks


def create_daily_workflow_page(notion: Client, database_id: str, date: datetime) -> Optional[str]:
    """Create a new daily workflow page in Notion."""
    title = f"Daily Workflow - {date.strftime('%Y-%m-%d')}"
    
    # Read template content
    template_content = parse_markdown_file(DAILY_TEMPLATE_FILE)
    blocks = markdown_to_notion_blocks(template_content)
    
    try:
        # Create page
        page = notion.pages.create(
            parent={"database_id": database_id},
            properties={
                "Date": {
                    "date": {
                        "start": date.strftime("%Y-%m-%d")
                    }
                },
                "Title": {
                    "title": [
                        {
                            "text": {
                                "content": title
                            }
                        }
                    ]
                }
            }
        )
        
        # Add content blocks
        if blocks:
            notion.blocks.children.append(
                block_id=page["id"],
                children=blocks
            )
        
        print(f"✅ Created page: {title}")
        print(f"   URL: {page.get('url', 'N/A')}")
        return page["id"]
    
    except Exception as e:
        print(f"❌ Error creating page: {e}")
        return None


def create_database_template(notion: Client, parent_page_id: str) -> Optional[str]:
    """Create the Daily Productivity System database in Notion."""
    try:
        # Create database
        database = notion.databases.create(
            parent={"page_id": parent_page_id},
            title=[{"type": "text", "text": {"content": "Daily Productivity System"}}],
            properties={
                "Date": {
                    "date": {}
                },
                "Title": {
                    "title": {}
                },
                "ONE System Focus": {
                    "rich_text": {}
                },
                "Deep Work Window": {
                    "rich_text": {}
                },
                "ONE Domino": {
                    "rich_text": {}
                },
                "Domino Why": {
                    "rich_text": {}
                },
                "Context Type": {
                    "select": {
                        "options": [
                            {"name": "Finance/Admin", "color": "blue"},
                            {"name": "Creative/Content", "color": "purple"},
                            {"name": "Technical/Development", "color": "green"},
                            {"name": "Communication", "color": "yellow"},
                            {"name": "Review/Planning", "color": "orange"}
                        ]
                    }
                },
                "Energy Level": {
                    "number": {}
                },
                "Focus Time Target": {
                    "number": {}
                },
                "Focus Time Actual": {
                    "number": {}
                },
                "Context Switches": {
                    "number": {}
                },
                "Delegations Created": {
                    "number": {}
                },
                "Domino Status": {
                    "select": {
                        "options": [
                            {"name": "Not Started", "color": "red"},
                            {"name": "In Progress", "color": "yellow"},
                            {"name": "Completed", "color": "green"}
                        ]
                    }
                },
                "Reflection Notes": {
                    "rich_text": {}
                },
                "Tomorrow Domino": {
                    "rich_text": {}
                }
            }
        )
        
        print(f"✅ Created database: Daily Productivity System")
        print(f"   Database ID: {database['id']}")
        print(f"   URL: {database.get('url', 'N/A')}")
        return database["id"]
    
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        return None


def main():
    """Main function to sync daily workflow to Notion."""
    print("🔄 Daily Workflow Notion Sync")
    print("=" * 50)
    
    # Check API key
    if NOTION_API_KEY == "your-notion-api-key-here":
        print("❌ Error: NOTION_API_KEY not set")
        print("   Set it as environment variable or update the script")
        print("   Get your key from: https://www.notion.so/my-integrations")
        return
    
    # Initialize Notion client
    try:
        notion = Client(auth=NOTION_API_KEY)
    except Exception as e:
        print(f"❌ Error initializing Notion client: {e}")
        return
    
    # Check database ID
    if DATABASE_ID == "your-database-id-here":
        print("⚠️  DATABASE_ID not set")
        print("   You need to:")
        print("   1. Create a page in Notion")
        print("   2. Share it with your integration")
        print("   3. Get the page ID from the URL")
        print("   4. Run this script to create the database")
        print("\n   Or set DATABASE_ID to an existing database ID")
        
        # Ask if user wants to create database
        response = input("\n   Do you have a parent page ID to create the database? (y/n): ")
        if response.lower() == "y":
            parent_id = input("   Enter parent page ID: ").strip()
            db_id = create_database_template(notion, parent_id)
            if db_id:
                print(f"\n   ✅ Save this DATABASE_ID: {db_id}")
                print(f"   Set it as: export NOTION_DATABASE_ID='{db_id}'")
        return
    
    # Create today's daily workflow page
    today = datetime.now()
    create_daily_workflow_page(notion, DATABASE_ID, today)
    
    print("\n✅ Sync complete!")


if __name__ == "__main__":
    main()



