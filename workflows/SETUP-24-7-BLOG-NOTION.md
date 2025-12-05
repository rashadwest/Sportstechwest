# Setup Instructions: 24/7 Server Blog Post in Notion

## ✅ What's Ready

1. **Blog Content Created**: `workflows/local-server-24-7-blog-content.md`
   - Full blog post content
   - Image prompts for 4 images
   - Social media excerpts
   - Properly formatted

2. **Python Script Ready**: `workflows/create-24-7-blog-notion.py`
   - Can create the Notion page automatically
   - Requires Notion API token

## 🚀 Option 1: Use MCP Commands (Recommended)

If MCP is connected in Cursor/Claude Desktop, use these commands:

### Step 1: Create Blog Post in Notion

```
Use Notion MCP to create a new page in the Blog Posts database with:

Title: "Why I Built a Local Server to Run 24/7"
Status: Draft
Date: 2025-10-29
Description: "Why I decided to build my own always-on infrastructure for automation, AI workflows, and continuous learning — and why it changed everything."
Tags: server, automation, docker, 24/7, local, infrastructure, mcp
Categories: Insights
Author: Rashad West

Then read the content from workflows/local-server-24-7-blog-content.md and add it to the page with proper formatting:
- Front Matter section as a collapsible toggle
- Blog Content sections with proper headers
- Image Prompts section
- Social Media Excerpts section
- Status checklist
```

### Step 2: Generate Images with Glif MCP

For each of the 4 image prompts in the blog content:

```
Use Glif MCP to generate an image with this prompt: [paste prompt from Image Prompts section]
```

The 4 images needed:
1. **24-7-server-hero.png** (Hero/thumbnail image)
2. **24-7-server-comparison.png** (Before/after comparison)
3. **24-7-server-architecture.png** (Infrastructure diagram)
4. **24-7-automation-workflows.png** (Workflows infographic)

### Step 3: Add Images to Notion

After generating each image:
```
Use Notion MCP to add the generated image URL to the blog post page at the appropriate location based on the "Location" specified in each image prompt.
```

### Step 4: Update Thumbnail

```
Use Notion MCP to update the blog post page's Thumbnail property with the URL of the 24-7-server-hero.png image
```

### Step 5: Update Status

```
Use Notion MCP to update the blog post Status to "Images Generated"
```

### Step 6: Get Notion Page Link

```
Use Notion MCP to get the URL of the blog post page titled "Why I Built a Local Server to Run 24/7"
```

---

## 🐍 Option 2: Use Python Script

### Step 1: Set Notion API Token

```bash
export NOTION_API_TOKEN="your-notion-api-token-here"
```

Or create a `.env` file in the workflows directory:
```
NOTION_API_TOKEN=your-token-here
```

### Step 2: Run the Script

```bash
cd /Users/rashadwest/Sportstechwest/workflows
python3 create-24-7-blog-notion.py
```

The script will:
- Find the Blog Posts database
- Create the page with all properties
- Add all content formatted properly
- Return the Notion page URL

### Step 3: Generate Images

After the page is created, use Glif MCP to generate the 4 images and update the Notion page with their URLs.

---

## 📋 Image Prompts Summary

All image prompts are in `local-server-24-7-blog-content.md` under "## Image Prompts". Here's a quick reference:

### Image 1: Hero/Thumbnail
- **Filename**: `24-7-server-hero.png`
- **Location**: Header/thumbnail
- **Prompt**: Modern Mac with "Always On" indicators, Docker containers, clock showing 3 AM, MCP server icons

### Image 2: Comparison
- **Filename**: `24-7-server-comparison.png`
- **Location**: After "The shift in mindset" section
- **Prompt**: Before/after showing cloud-dependent vs 24/7 local

### Image 3: Architecture
- **Filename**: `24-7-server-architecture.png`
- **Location**: After "What actually runs 24/7" section
- **Prompt**: Technical diagram showing Mac, Docker, MCP servers (Notion, Glif, n8n)

### Image 4: Workflows
- **Filename**: `24-7-automation-workflows.png`
- **Location**: After "What's running right now" section
- **Prompt**: Infographic showing workflows running 24/7 around a clock face

---

## ✅ Checklist

- [ ] Blog post created in Notion
- [ ] All content added with proper formatting
- [ ] 4 images generated with Glif MCP
- [ ] Images added to Notion page at correct locations
- [ ] Thumbnail property updated with hero image URL
- [ ] Status updated to "Images Generated"
- [ ] Notion page URL obtained
- [ ] Ready for review and publishing

---

## 🔗 Expected Output

Once complete, you should have:
- A Notion page titled "Why I Built a Local Server to Run 24/7"
- All blog content properly formatted
- 4 generated images embedded
- Social media excerpts ready
- Status: "Images Generated"

The Notion page URL can then be shared for review before pushing to Jekyll.

