# Setup Notion Blog Database via MCP Commands

Since Notion MCP is connected, you can use these commands directly in Cursor or Claude to set everything up automatically.

## Quick Setup Commands

Copy and paste these commands one at a time into Cursor/Claude:

### 1. Search for existing databases
```
Search my Notion workspace for any existing databases related to "blog" or "content"
```

### 2. Create Blog Posts Database
```
Use Notion MCP to create a new database called "Blog Posts" with these properties:
- Title (Title type)
- Status (Select type with options: Draft, Draft Complete, Images Generated, Ready to Publish, Published)
- Date (Date type)
- Description (Text type)
- Thumbnail (URL type)
- Tags (Multi-select type with options: automation, AI, basketball, server, docker, mcp, productivity)
- Categories (Multi-select type with options: Insights, Tutorial, News)
- Author (Text type, default: "Rashad West")
- Slug (Text type)
- Image URLs (Text type)
```

### 3. Create Template Page
```
Use Notion MCP to create a new page in the Blog Posts database titled "Blog Post Template" with the following content structure:

1. Heading: "Blog Post Template"
2. Toggle section: "Front Matter (Jekyll)" containing:
   - layout: post
   - title, description, thumbnail, badge_color, trending, simple_nav, date, tags, categories, author
3. Section: "Blog Content"
4. Section: "Image Prompts" 
5. Section: "Social Media Excerpts" with subsections for Twitter, LinkedIn, Instagram
6. Checklist: "Status" with items: Draft Complete, Images Generated, Images Optimized, Ready to Publish, Published, Social Media Scheduled

Set the Status property to "Draft"
```

### 4. Create First Blog Post (Server Build)
```
Use Notion MCP to create a new page in the Blog Posts database titled "How I Built My Own Server" with:
- Status: Draft
- Date: [today's date]
- Tags: server, docker, mcp, automation
- Categories: Insights
- Author: Rashad West
- Description: A guide to building and configuring a personal MCP server using Docker, Notion, and Glif

Add sections for:
1. Introduction about building the server
2. Architecture overview
3. Setup steps
4. Image prompts section
5. Social media excerpts section
```

## Alternative: One-Command Setup

If you want to do it all at once, try:

```
I need you to set up a complete blog workflow in Notion. Please:

1. Create a database called "Blog Posts" with properties: Title (title), Status (select with Draft/Draft Complete/Images Generated/Ready to Publish/Published), Date (date), Description (text), Thumbnail (url), Tags (multi-select), Categories (multi-select), Author (text), Slug (text), Image URLs (text)

2. Create a template page in that database with sections for Front Matter, Blog Content, Image Prompts, and Social Media Excerpts

3. Create a draft blog post titled "How I Built My Own Server" about setting up Docker MCP server with Notion and Glif

Let me know when each step is complete.
```

## Verification Commands

After setup, verify with:

```
Query the Blog Posts database and show me all pages
```

```
Read the Blog Post Template page content
```


