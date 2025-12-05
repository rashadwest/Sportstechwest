# Quick Start: Notion Blog Workflow Setup

## 🎯 Goal: Get Notion setup completed TODAY

## Option 1: Automated Setup via MCP (Recommended - 2 minutes)

Since Notion MCP is already connected, I can set it up automatically right now.

**Just say this in Cursor:**
```
Set up the Notion blog workflow: create the Blog Posts database with all properties, create the template page, and create my first blog post draft about building my server. Use the Notion MCP tools to do this automatically.
```

Or copy the commands from `setup-via-mcp-commands.md` and run them one by one.

---

## Option 2: Python Script Setup (5 minutes)

If you prefer a script:

1. **Install dependencies:**
   ```bash
   pip install notion-client
   ```

2. **Get your Notion API token:**
   - Go to https://www.notion.so/my-integrations
   - Create new integration (if needed)
   - Copy the Internal Integration Token

3. **Run the setup script:**
   ```bash
   cd /Users/rashadwest/Sportstechwest/workflows
   export NOTION_API_TOKEN="your-token-here"
   python3 setup-notion-blog-database.py
   ```

4. **Share database with integration:**
   - Open the created database in Notion
   - Click "..." → "Add connections"
   - Select your integration

---

## Option 3: Manual Setup (10 minutes)

If automated doesn't work:

1. **Create database in Notion:**
   - New page → Table database
   - Name: "Blog Posts"
   - Add properties from the plan

2. **Create template:**
   - New page in database
   - Copy content from `notion-blog-post-template.md`
   - Save as template

3. **Create first post:**
   - Use template
   - Fill in details about your server build

---

## What You Need

- ✅ Notion MCP already connected (19 tools available)
- ⚠️ Notion Integration token (if using script/manual)
- ⚠️ Share database with integration (one-time)

---

## After Setup

Once the database is created:

1. ✅ Database is ready
2. ✅ Template is ready
3. ✅ First blog post draft is started
4. Next: Generate images with Glif MCP
5. Next: Set up n8n workflow for auto-publishing

---

## Need Help?

- MCP commands: See `setup-via-mcp-commands.md`
- Python script: See `setup-notion-blog-database.py`
- Complete guide: See `blog-social-media-workflow-guide.md`


