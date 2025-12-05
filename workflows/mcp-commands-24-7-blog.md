# MCP Commands to Create 24/7 Server Blog Post in Notion

## Step 1: Verify Database Exists

Run in Cursor/Claude:
```
Use Notion MCP to search for a database called "Blog Posts". If it exists, show me its properties. If it doesn't exist, create it with these properties:
- Title (Title type)
- Status (Select type: Draft, Draft Complete, Images Generated, Ready to Publish, Published)
- Date (Date type)
- Description (Rich text)
- Thumbnail (URL)
- Tags (Multi-select: server, automation, docker, 24/7, local, infrastructure, mcp)
- Categories (Multi-select: Insights, Tutorial, News)
- Author (Rich text)
- Slug (Rich text)
- Image URLs (Rich text)
```

## Step 2: Create Blog Post in Notion

Run in Cursor/Claude:
```
Use Notion MCP to create a new page in the Blog Posts database with:

Title: "Why I Built a Local Server to Run 24/7"
Status: Draft
Date: 2025-10-29
Description: "Why I decided to build my own always-on infrastructure for automation, AI workflows, and continuous learning — and why it changed everything."
Tags: server, automation, docker, 24/7, local, infrastructure, mcp
Categories: Insights
Author: Rashad West
Thumbnail: (will be updated after image generation)

Then add the blog content from the file workflows/local-server-24-7-blog-content.md, formatting it properly with:
- Front Matter section as a collapsible/toggle
- Blog Content sections with proper headers (## for main sections)
- Image Prompts section
- Social Media Excerpts section
- Status checklist
```

## Step 3: Generate Images with Glif MCP

For each image prompt, run:
```
Use Glif MCP to generate an image with this prompt: [paste the prompt from Image Prompts section]

Then use Notion MCP to add the generated image URL to the blog post page.
```

Image prompts are in the blog content file under "## Image Prompts" section.

## Step 4: Update Thumbnail

After generating the hero image:
```
Use Notion MCP to update the blog post page's Thumbnail property with the URL of the first generated image (24-7-server-hero.png)
```

## Step 5: Update Status

```
Use Notion MCP to update the blog post Status to "Images Generated" once all images are created
```

## Step 6: Get Notion Page Link

```
Use Notion MCP to get the URL of the blog post page titled "Why I Built a Local Server to Run 24/7"
```

---

## Alternative: One-Command Approach

If you want to do it all at once:
```
I need you to create a blog post in Notion using MCP:

1. Verify or create "Blog Posts" database
2. Create a new page titled "Why I Built a Local Server to Run 24/7" with:
   - Status: Draft
   - Date: 2025-10-29
   - Description: "Why I decided to build my own always-on infrastructure for automation, AI workflows, and continuous learning — and why it changed everything."
   - Tags: server, automation, docker, 24/7, local, infrastructure, mcp
   - Categories: Insights
   - Author: Rashad West
3. Add all content from workflows/local-server-24-7-blog-content.md with proper formatting
4. Generate 4 images using Glif MCP based on the prompts in the Image Prompts section
5. Add image URLs to the Notion page and update Thumbnail property
6. Generate social media excerpts and add them to the page
7. Update Status to "Images Generated"
8. Give me the Notion page URL

Let me know when each step is complete.
```

