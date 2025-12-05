#!/usr/bin/env python3
"""
Create the 24/7 Server blog post in Notion
This script reads the blog content and creates a Notion page with all content formatted properly.
"""

import os
import sys
import re
from datetime import datetime
from notion_client import Client

# Get Notion API token from environment or prompt
NOTION_TOKEN = os.getenv("NOTION_API_TOKEN")
if not NOTION_TOKEN:
    NOTION_TOKEN = input("Enter your Notion Integration Token: ").strip()

if not NOTION_TOKEN:
    print("Error: NOTION_API_TOKEN is required")
    sys.exit(1)

notion = Client(auth=NOTION_TOKEN)

def parse_markdown_to_blocks(content):
    """Parse markdown content into Notion blocks"""
    blocks = []
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
            
        # Heading 1
        if line.startswith('# '):
            text = line[2:].strip()
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"type": "text", "text": {"content": text}}]
                }
            })
            i += 1
            
        # Heading 2
        elif line.startswith('## '):
            text = line[3:].strip()
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": text}}]
                }
            })
            i += 1
            
        # Heading 3
        elif line.startswith('### '):
            text = line[4:].strip()
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": text}}]
                }
            })
            i += 1
            
        # Horizontal rule
        elif line.startswith('---'):
            blocks.append({
                "object": "block",
                "type": "divider",
                "divider": {}
            })
            i += 1
            
        # Code block
        elif line.startswith('```'):
            code_lines = []
            i += 1
            language = line[3:].strip() if len(line) > 3 else ""
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # Skip closing ```
            
            code_text = '\n'.join(code_lines).strip()
            blocks.append({
                "object": "block",
                "type": "code",
                "code": {
                    "rich_text": [{"type": "text", "text": {"content": code_text}}],
                    "language": language if language else "plain text"
                }
            })
            
        # Bullet list
        elif line.startswith('- ') or line.startswith('* '):
            items = []
            while i < len(lines) and (lines[i].strip().startswith('- ') or lines[i].strip().startswith('* ')):
                item_text = lines[i].strip()[2:].strip()
                # Handle bold text in list items
                rich_text = parse_inline_formatting(item_text)
                items.append(rich_text)
                i += 1
            
            # Create bullet list blocks
            for item_text in items:
                blocks.append({
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {
                        "rich_text": item_text
                    }
                })
                
        # Regular paragraph (collect until next heading/block)
        else:
            para_lines = []
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('#') and not lines[i].strip().startswith('```') and not lines[i].strip().startswith('---'):
                para_lines.append(lines[i])
                i += 1
            
            para_text = ' '.join(para_lines).strip()
            if para_text:
                rich_text = parse_inline_formatting(para_text)
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": rich_text
                    }
                })
    
    return blocks

def parse_inline_formatting(text):
    """Parse inline markdown formatting (bold, italic) into Notion rich text"""
    rich_text = []
    i = 0
    
    while i < len(text):
        # Bold text **text**
        if text[i:i+2] == '**' and i+2 < len(text):
            end = text.find('**', i+2)
            if end != -1:
                rich_text.append({
                    "type": "text",
                    "text": {"content": text[i+2:end]},
                    "annotations": {"bold": True}
                })
                i = end + 2
                continue
        
        # Regular text
        start = i
        while i < len(text) and not (text[i:i+2] == '**' and i+1 < len(text)):
            i += 1
        
        if i > start:
            content = text[start:i]
            if content.strip():
                rich_text.append({
                    "type": "text",
                    "text": {"content": content}
                })
    
    if not rich_text:
        rich_text = [{"type": "text", "text": {"content": text}}]
    
    return rich_text

def find_database(name="Blog Posts"):
    """Find the Blog Posts database"""
    try:
        results = notion.search(query=name, filter={"property": "object", "value": "database"})
        for result in results.get("results", []):
            if result.get("object") == "database" and name.lower() in result.get("title", [{}])[0].get("plain_text", "").lower():
                return result
        return None
    except Exception as e:
        print(f"Error searching for database: {e}")
        return None

def create_blog_post():
    """Create the blog post in Notion"""
    
    # Read blog content
    content_file = "/Users/rashadwest/Sportstechwest/workflows/local-server-24-7-blog-content.md"
    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find Blog Posts database
    print("🔍 Searching for Blog Posts database...")
    database = find_database("Blog Posts")
    
    if not database:
        print("❌ Blog Posts database not found. Please create it first.")
        print("   You can use the setup-notion-blog-database.py script or create it manually in Notion.")
        sys.exit(1)
    
    database_id = database['id']
    print(f"✅ Found database: {database.get('url', 'N/A')}")
    
    # Extract front matter
    front_matter_match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
    front_matter = {}
    if front_matter_match:
        for line in front_matter_match.group(1).split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                front_matter[key] = value
    
    # Extract main content (after ## Blog Content)
    content_start = content.find('## Blog Content')
    if content_start != -1:
        main_content = content[content_start + len('## Blog Content'):]
        # Remove Image Prompts and Social Media Excerpts sections for main content
        main_content = main_content.split('## Image Prompts')[0].strip()
    else:
        main_content = content
    
    # Parse content into blocks
    print("📝 Parsing content into Notion blocks...")
    blocks = []
    
    # Add Front Matter as toggle
    front_matter_text = "```\n" + "\n".join([f"{k}: {v}" for k, v in front_matter.items() if k != 'layout']) + "\n```"
    blocks.append({
        "object": "block",
        "type": "toggle",
        "toggle": {
            "rich_text": [{"type": "text", "text": {"content": "Front Matter (Jekyll)"}}],
            "children": [{
                "object": "block",
                "type": "code",
                "code": {
                    "rich_text": [{"type": "text", "text": {"content": front_matter_text.strip()}}],
                    "language": "yaml"
                }
            }]
        }
    })
    
    # Add main blog content blocks
    content_blocks = parse_markdown_to_blocks(main_content)
    blocks.extend(content_blocks)
    
    # Add Image Prompts section
    if '## Image Prompts' in content:
        image_prompts_start = content.find('## Image Prompts')
        image_prompts_end = content.find('---', image_prompts_start + len('## Image Prompts'))
        if image_prompts_end == -1:
            image_prompts_end = content.find('## Social Media Excerpts', image_prompts_start)
        
        if image_prompts_end != -1:
            image_prompts_content = content[image_prompts_start:image_prompts_end]
            image_blocks = parse_markdown_to_blocks(image_prompts_content)
            blocks.extend(image_blocks)
    
    # Add Social Media Excerpts section
    if '## Social Media Excerpts' in content:
        social_start = content.find('## Social Media Excerpts')
        social_content = content[social_start:]
        social_blocks = parse_markdown_to_blocks(social_content)
        blocks.extend(social_blocks)
    
    # Prepare properties
    date_str = front_matter.get('date', '2025-10-29')
    try:
        post_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except:
        post_date = datetime(2025, 10, 29).date()
    
    tags = front_matter.get('tags', 'server, automation, docker, 24/7, local, infrastructure, mcp')
    tags_list = [tag.strip().strip('[').strip(']') for tag in tags.split(',')]
    
    properties = {
        "Title": {
            "title": [{"text": {"content": front_matter.get('title', 'Why I Built a Local Server to Run 24/7')}}]
        },
        "Status": {"select": {"name": "Draft"}},
        "Date": {"date": {"start": post_date.isoformat()}},
        "Description": {
            "rich_text": [{"text": {"content": front_matter.get('description', '')}}]
        },
        "Thumbnail": {"url": front_matter.get('thumbnail', '')},
        "Tags": {
            "multi_select": [{"name": tag} for tag in tags_list]
        },
        "Categories": {
            "multi_select": [{"name": front_matter.get('categories', 'Insights').strip('[').strip(']')}]
        },
        "Author": {
            "rich_text": [{"text": {"content": front_matter.get('author', 'Rashad West')}}]
        }
    }
    
    # Create the page
    print("🚀 Creating Notion page...")
    try:
        # Note: Notion API has limits on block count per request (100 blocks)
        # We'll need to create the page first, then add blocks in batches
        page = notion.pages.create(
            parent={"database_id": database_id},
            properties=properties
        )
        
        page_id = page['id']
        print(f"✅ Page created! Page ID: {page_id}")
        
        # Add blocks in batches of 100
        batch_size = 100
        for i in range(0, len(blocks), batch_size):
            batch = blocks[i:i+batch_size]
            notion.blocks.children.append(
                block_id=page_id,
                children=batch
            )
            print(f"   Added {len(batch)} blocks (batch {i//batch_size + 1})")
        
        # Get page URL
        page_url = page.get('url', '').replace('https://www.notion.so/', 'https://notion.so/')
        
        print(f"\n✅ Blog post created successfully!")
        print(f"   Page URL: {page_url}")
        print(f"   Title: {front_matter.get('title', 'Why I Built a Local Server to Run 24/7')}")
        print(f"\n📋 Next steps:")
        print(f"   1. Generate images using Glif MCP")
        print(f"   2. Update image URLs in the Notion page")
        print(f"   3. Update Thumbnail property with hero image URL")
        print(f"   4. Change Status to 'Images Generated' when ready")
        
        return page_url
        
    except Exception as e:
        print(f"❌ Error creating page: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    url = create_blog_post()
    if url:
        print(f"\n🔗 Notion Page: {url}")

