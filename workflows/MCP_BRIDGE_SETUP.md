# MCP Bridge Setup Guide

## Current Status

You already have MCP configured in:
- ✅ Cursor: `~/.cursor/mcp.json` (has MCP_DOCKER gateway and Notion)
- ✅ Claude Desktop: `~/Library/Application Support/Claude/claude_desktop_config.json` (has n8n-mcp-server and MCP_DOCKER)

## Step 1: Start Docker

First, make sure Docker is running:

```bash
# Check if Docker Desktop is running
open -a Docker

# Or start via command line
docker ps
```

If Docker isn't installed:
```bash
brew install --cask docker
```

## Step 2: Configure Notion MCP Connection

You have Notion configured via URL, but for full functionality, you'll want to use the API-based connection.

### Option A: Use MCP Toolkit (Easiest)

1. Your Notion is already showing in MCP Toolkit with 19 tools
2. It's likely already configured correctly
3. Just verify it's working

### Option B: Configure via Config File

If you need to configure manually:

**For Cursor** (`~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": [
        "mcp",
        "gateway",
        "run"
      ]
    },
    "Notion": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-notion"
      ],
      "env": {
        "NOTION_API_KEY": "your-notion-api-key-here"
      }
    },
    "Glif": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-glif"
      ],
      "env": {
        "GLIF_API_KEY": "your-glif-api-key-here"
      }
    }
  }
}
```

**For Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "n8n-mac": {
      "command": "node",
      "args": ["/Users/rashadwest/n8n-mcp-server/index.js"],
      "env": {
        "N8N_API_KEY": "your-n8n-api-key",
        "N8N_API_URL": "http://localhost:5678"
      }
    },
    "MCP_DOCKER": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"]
    },
    "Notion": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-notion"
      ],
      "env": {
        "NOTION_API_KEY": "your-notion-api-key-here"
      }
    },
    "Glif": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-glif"
      ],
      "env": {
        "GLIF_API_KEY": "your-glif-api-key-here"
      }
    }
  }
}
```

## Step 3: Get API Keys

### Notion API Key

1. Go to https://www.notion.so/my-integrations
2. Click "+ New integration"
3. Name it "MCP Blog Workflow"
4. Copy the **Internal Integration Token** (starts with `secret_`)
5. **Important:** Share your databases/pages with this integration

### Glif API Key

1. Go to https://glif.app
2. Sign in and go to settings
3. Get your API key
4. Copy it

## Step 4: Update Config Files

1. **Backup your current configs:**
   ```bash
   cp ~/.cursor/mcp.json ~/.cursor/mcp.json.backup
   cp ~/Library/Application\ Support/Claude/claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json.backup
   ```

2. **Edit Cursor config:**
   ```bash
   code ~/.cursor/mcp.json
   # or
   nano ~/.cursor/mcp.json
   ```

3. **Edit Claude Desktop config:**
   ```bash
   code ~/Library/Application\ Support/Claude/claude_desktop_config.json
   # or
   nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

4. **Replace with the configs above**, inserting your actual API keys

## Step 5: Restart Applications

**Important:** Fully quit and restart both applications:

```bash
# Quit Cursor completely
killall Cursor

# Quit Claude Desktop completely  
killall "Claude"

# Then reopen both apps
```

Or manually:
- Cursor: Cmd+Q to quit, then reopen
- Claude Desktop: Cmd+Q to quit, then reopen

## Step 6: Test Connections

### Test in Cursor

1. Open Cursor
2. Try these commands:

```
Test Notion MCP: Search for databases in my Notion workspace
```

```
Test Glif MCP: Generate a simple test image with prompt "a red circle on white background"
```

### Test in Claude Desktop

1. Open Claude Desktop
2. Try similar commands

## Step 7: Verify MCP Toolkit

1. Open MCP Toolkit (the interface you showed earlier)
2. Check that both Notion (19 tools) and Glif (10 tools) show as connected
3. If they show "SECRETS REQUIRED", add the API keys there

## Troubleshooting

### "Cannot connect to Docker"
- Make sure Docker Desktop is running
- Check: `docker ps` should work without errors

### "Notion MCP not working"
- Verify API key is correct (starts with `secret_`)
- Make sure you shared your database with the integration
- Check Notion integration page for errors

### "Glif MCP not working"
- Verify API key is correct
- Check Glif account is active
- Test Glif API directly: `curl https://api.glif.app/v1/models` (if available)

### "MCP tools not showing in Cursor"
- Fully quit and restart Cursor
- Check config file syntax (valid JSON)
- Look for errors in Cursor's console/logs

### "Config file not found"
- Create the directory if needed:
  ```bash
  mkdir -p ~/.cursor
  mkdir -p ~/Library/Application\ Support/Claude
  ```

## Quick Setup Script

I can create a setup script that:
1. Backs up current configs
2. Prompts for API keys
3. Updates both config files
4. Verifies Docker is running

Would you like me to create that?

## Next Steps After Setup

Once MCP is working:

1. ✅ Test Notion connection: Read/write to your workspace
2. ✅ Test Glif connection: Generate test images
3. ✅ Create Blog Posts database in Notion
4. ✅ Add blog posts via MCP
5. ✅ Generate images via Glif MCP
6. ✅ Set up n8n workflow for publishing


