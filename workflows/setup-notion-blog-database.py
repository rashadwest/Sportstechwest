#!/usr/bin/env python3
"""
Automated setup script for Notion Blog Posts database
Run this script to automatically create the database and template
"""

import os
import sys
from notion_client import Client
from datetime import datetime

# You'll need to set these environment variables or update them here
NOTION_TOKEN = os.getenv("NOTION_API_TOKEN") or input("Enter your Notion Integration Token: ")
PARENT_PAGE_ID = os.getenv("NOTION_PARENT_PAGE_ID") or input("Enter parent page ID (optional, press Enter to skip): ")

if not NOTION_TOKEN:
    print("Error: NOTION_API_TOKEN is required")
    sys.exit(1)

notion = Client(auth=NOTION_TOKEN)

def create_blog_database(parent_id=None):
    """Create the Blog Posts database with all required properties"""
    
    # Database properties schema
    properties = {
        "Title": {"title": {}},
        "Status": {
            "select": {
                "options": [
                    {"name": "Draft", "color": "gray"},
                    {"name": "Draft Complete", "color": "yellow"},
                    {"name": "Images Generated", "color": "blue"},
                    {"name": "Ready to Publish", "color": "orange"},
                    {"name": "Published", "color": "green"}
                ]
            }
        },
        "Date": {"date": {}},
        "Description": {"rich_text": {}},
        "Thumbnail": {"url": {}},
        "Tags": {"multi_select": {
            "options": [
                {"name": "automation", "color": "blue"},
                {"name": "AI", "color": "purple"},
                {"name": "basketball", "color": "red"},
                {"name": "server", "color": "green"},
                {"name": "docker", "color": "cyan"},
                {"name": "mcp", "color": "orange"},
                {"name": "productivity", "color": "pink"}
            ]
        }},
        "Categories": {"multi_select": {
            "options": [
                {"name": "Insights", "color": "blue"},
                {"name": "Tutorial", "color": "green"},
                {"name": "News", "color": "red"}
            ]
        }},
        "Author": {"rich_text": {}},
        "Slug": {"rich_text": {}},
        "Image URLs": {"rich_text": {}}
    }
    
    # Create database
    try:
        if parent_id:
            database = notion.databases.create(
                parent={"page_id": parent_id},
                title=[{"type": "text", "text": {"content": "Blog Posts"}}],
                properties=properties
            )
        else:
            # Create in workspace root
            database = notion.databases.create(
                parent={"type": "workspace"},
                title=[{"type": "text", "text": {"content": "Blog Posts"}}],
                properties=properties
            )
        
        print(f"✅ Database created successfully!")
        print(f"   Database ID: {database['id']}")
        print(f"   URL: {database.get('url', 'N/A')}")
        
        return database
        
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        return None

def create_template_page(database_id):
    """Create a template page in the database"""
    
    template_content = """
# Blog Post Template

## Front Matter (Jekyll)
---
layout: post
title: "Your Blog Post Title Here"
description: "SEO-friendly description (150-160 characters)"
thumbnail: "/assets/images/blog-img/filename.png"
badge_color: "text-bg-primary"
trending: true
simple_nav: true
date: YYYY-MM-DD
tags: [tag1, tag2, tag3]
categories: [Insights]
author: "Rashad West"
---

## Blog Content

[Write your blog post content here]

---

## Image Prompts

### Image 1: [Image Description]
**Location:** After "[Section Name]"  
**Filename:** `filename-1.png`  
**Target path:** `/assets/images/blog-img/filename-1.png`

**Prompt:**
```
[Detailed image generation prompt for Glif]
```

---

## Social Media Excerpts

### Twitter/X (280 chars)
[Extract key quote or insight for Twitter]

### LinkedIn (3000 chars)
[Longer excerpt or summary for LinkedIn]

### Instagram (2200 chars)
[Engaging excerpt with relevant hashtags]

---

## Status

- [ ] Draft Complete
- [ ] Images Generated
- [ ] Images Optimized
- [ ] Ready to Publish
- [ ] Published
- [ ] Social Media Scheduled
"""
    
    try:
        # Create page with template content
        page = notion.pages.create(
            parent={"database_id": database_id},
            properties={
                "Title": {
                    "title": [{"text": {"content": "Blog Post Template"}}]
                },
                "Status": {"select": {"name": "Draft"}},
                "Author": {"rich_text": [{"text": {"content": "Rashad West"}}]}
            },
            children=[
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": [{"type": "text", "text": {"content": "Blog Post Template"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": "This is your blog post template. Use this as a starting point for all new posts."}}]
                    }
                }
            ]
        )
        
        print(f"✅ Template page created!")
        print(f"   Page ID: {page['id']}")
        
        return page
        
    except Exception as e:
        print(f"❌ Error creating template: {e}")
        return None

def main():
    print("🚀 Setting up Notion Blog Posts Database...")
    print()
    
    # Create database
    database = create_blog_database(PARENT_PAGE_ID if PARENT_PAGE_ID else None)
    
    if not database:
        print("Failed to create database. Exiting.")
        sys.exit(1)
    
    database_id = database['id']
    
    # Create template page
    create_template_page(database_id)
    
    print()
    print("✅ Setup complete!")
    print()
    print("Next steps:")
    print("1. Share the database with your Notion integration")
    print("2. Save the database ID for n8n workflow configuration")
    print(f"3. Database ID: {database_id}")
    print(f"4. Database URL: {database.get('url', 'Check Notion')}")

if __name__ == "__main__":
    main()


