# Notion Sync Quick Start

**Two ways to sync your Daily Workflow to Notion:**

---

## Option 1: Notion MCP (Recommended for Cursor)

**Best for:** Real-time syncing, interactive commands in Cursor chat

### Setup Steps:
1. **Get Notion Integration Token**
   - Go to https://www.notion.so/my-integrations
   - Create new integration: "Cursor MCP Integration"
   - Copy the token (starts with `secret_`)

2. **Configure MCP in Cursor**
   - See `NOTION-MCP-SETUP-GUIDE.md` for detailed steps
   - Add Notion MCP server to Cursor settings

3. **Use Commands**
   - Once configured, you can use commands like:
     ```
     Use Notion MCP to create a new database...
     Use Notion MCP to create a new page...
     ```

**Full Guide:** See `NOTION-MCP-SETUP-GUIDE.md`

---

## Option 2: Python Script (Easier Setup)

**Best for:** One-time setup, automated daily syncs

### Setup Steps:

1. **Install dependencies:**
   ```bash
   pip install notion-client
   ```

2. **Get Notion Integration Token:**
   - Go to https://www.notion.so/my-integrations
   - Create new integration: "Daily Workflow Sync"
   - Copy the token

3. **Set environment variable:**
   ```bash
   export NOTION_API_KEY="secret_your_token_here"
   ```

4. **Create a parent page in Notion:**
   - Create a new page in Notion
   - Share it with your integration (Settings → Connections)
   - Copy the page ID from the URL

5. **Run the script to create database:**
   ```bash
   python sync_daily_workflow_to_notion.py
   ```
   - Follow prompts to create the database
   - Save the DATABASE_ID it gives you

6. **Set database ID:**
   ```bash
   export NOTION_DATABASE_ID="your_database_id_here"
   ```

7. **Run daily:**
   ```bash
   python sync_daily_workflow_to_notion.py
   ```

**Script:** `sync_daily_workflow_to_notion.py`

---

## Which Should You Use?

- **Use MCP** if you want to interactively create/update pages in Cursor chat
- **Use Python script** if you want automated daily syncs or prefer command-line

Both work! Choose based on your workflow preference.

---

## Quick Reference

- **Notion Integrations:** https://www.notion.so/my-integrations
- **Notion MCP Docs:** https://developers.notion.com/docs/mcp
- **Setup Guide:** `NOTION-MCP-SETUP-GUIDE.md`
- **Python Script:** `sync_daily_workflow_to_notion.py`



