# MCP Setup Instructions - Get It Working Today

## Quick Overview

MCP (Model Context Protocol) lets Cursor and Claude Desktop connect to external services like Notion and Glif. This guide will get you set up in about 10 minutes.

**What you'll need:**
- ✅ Docker Desktop installed and running
- ✅ Notion API key (we'll show you how to get it)
- ✅ Glif API key (optional, but recommended)
- ✅ Terminal access

---

## Step 1: Get Your API Keys

### Get Notion API Key (Required)

1. Go to https://www.notion.so/my-integrations
2. Click **"+ New integration"**
3. Name it "Blog Workflow" or "MCP Connection"
4. Select your workspace
5. Click **"Submit"**
6. **Copy the Internal Integration Token** (starts with `secret_`)
   - ⚠️ Keep this safe! You'll need it in a minute

### Get Glif API Key (Optional but Recommended)

1. Go to https://glif.app/
2. Sign up or log in
3. Go to your API settings
4. Generate a new API key
5. **Copy the API key**

---

## Step 2: Choose Your Setup Method

### Option A: Use the Automated Script (Easiest - Recommended)

1. **Open Terminal** (you can be anywhere)

2. **Navigate to your workflows folder:**
   ```bash
   cd /Users/rashadwest/Sportstechwest/workflows
   ```

3. **Make the script executable:**
   ```bash
   chmod +x setup-mcp-bridge.sh
   ```

4. **Run the script:**
   ```bash
   ./setup-mcp-bridge.sh
   ```

5. **Follow the prompts:**
   - Enter your Notion API key when asked
   - Enter your Glif API key (or press Enter to skip)
   - Enter your n8n API key (or press Enter to skip)

The script will:
- ✅ Check if Docker is running
- ✅ Backup existing configs
- ✅ Create the MCP configuration files
- ✅ Set everything up automatically

**Done! Skip to Step 3.**

---

### Option B: Manual Setup (If you prefer doing it yourself)

#### 2.1: Open Terminal
Open Terminal (you can be in any folder).

#### 2.2: Set Your API Keys
Replace the placeholders with your actual keys:

```bash
export NOTION_API_KEY="secret_your_notion_key_here"
export GLIF_API_KEY="your_glif_key_here"
```

#### 2.3: Create Config Directories
```bash
mkdir -p ~/.cursor
mkdir -p ~/Library/Application\ Support/Claude
```

#### 2.4: Backup Existing Configs (if they exist)
```bash
[ -f ~/.cursor/mcp.json ] && cp ~/.cursor/mcp.json ~/.cursor/mcp.json.backup
[ -f ~/Library/Application\ Support/Claude/claude_desktop_config.json ] && cp ~/Library/Application\ Support/Claude/claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json.backup
```

#### 2.5: Create Cursor Config
Copy and paste this entire block:

```bash
cat > ~/.cursor/mcp.json <<EOF
{
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"]
    },
    "Notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    },
    "Glif": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-glif"],
      "env": {
        "GLIF_API_KEY": "${GLIF_API_KEY}"
      }
    }
  }
}
EOF
```

#### 2.6: Create Claude Desktop Config
Copy and paste this entire block:

```bash
cat > ~/Library/Application\ Support/Claude/claude_desktop_config.json <<EOF
{
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"]
    },
    "Notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    },
    "Glif": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-glif"],
      "env": {
        "GLIF_API_KEY": "${GLIF_API_KEY}"
      }
    }
  }
}
EOF
```

**Note:** If you have an n8n MCP server, add this to the Claude Desktop config manually after the Glif section (add a comma after the closing brace of Glif):

```json
,
"n8n-mac": {
  "command": "node",
  "args": ["/Users/rashadwest/n8n-mcp-server/index.js"],
  "env": {
    "N8N_API_KEY": "your-n8n-api-key",
    "N8N_API_URL": "http://localhost:5678"
  }
}
```

---

## Step 3: Verify Configuration Files

Check that the files were created correctly:

```bash
cat ~/.cursor/mcp.json
```

You should see JSON with your API keys (the keys will be visible - this is normal).

```bash
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

You should see JSON with all your MCP servers configured.

---

## Step 4: Restart Applications

**⚠️ CRITICAL:** You must **completely quit** and restart both applications for the config to take effect.

### Quick Method (Terminal):
```bash
killall Cursor
killall Claude
```

Then manually reopen:
- Cursor
- Claude Desktop

### Manual Method:
1. **Cursor:** Press `Cmd + Q` (quit completely, don't just close window)
2. **Claude Desktop:** Press `Cmd + Q` (quit completely)
3. **Wait 5 seconds**
4. Reopen both applications

---

## Step 5: Test the Connection

After restarting, test in **Cursor**:

### Test Notion MCP:
Type this in Cursor:
```
Test Notion MCP: Search for databases in my Notion workspace
```

**Expected result:** You should see your Notion databases listed.

### Test Glif MCP (if configured):
Type this in Cursor:
```
Test Glif MCP: Generate a simple test image with prompt "a red circle on white background"
```

**Expected result:** You should get an image URL or see the generation process.

---

## Troubleshooting

### ❌ "Docker is not running"
**Solution:**
```bash
# Start Docker Desktop
open -a Docker

# Wait 30 seconds, then verify
docker ps
```

### ❌ "Notion MCP not working"
**Possible causes:**
1. **API key wrong** - Verify in Notion integrations page
2. **Database not shared** - In Notion, open your database → "..." → "Add connections" → Select your integration
3. **Config file malformed** - Run verification step again

**Fix:**
```bash
# Check your Notion API key is set correctly
cat ~/.cursor/mcp.json | grep NOTION_API_KEY
```

### ❌ "Glif MCP not working"
**Possible causes:**
1. **API key wrong** - Verify in Glif dashboard
2. **Config not saved** - Check file exists and has correct JSON

**Fix:**
```bash
# Verify Glif key is in config
cat ~/.cursor/mcp.json | grep GLIF_API_KEY
```

### ❌ "MCP tools not showing in Cursor"
**Solution:**
1. Make sure you **completely quit** Cursor (Cmd+Q, not just close window)
2. Wait 10 seconds
3. Reopen Cursor
4. Check if MCP servers are listed in Cursor's settings or MCP panel

### ❌ "JSON syntax error"
**Solution:**
The files must be valid JSON. If you see errors:
1. Use the automated script (Option A) instead
2. Or check for missing commas, brackets, or quotes

### ❌ "Need to restore backups"
If something went wrong and you want to restore:

```bash
cp ~/.cursor/mcp.json.backup ~/.cursor/mcp.json
cp ~/Library/Application\ Support/Claude/claude_desktop_config.json.backup ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Then restart the apps.

---

## Success Checklist

After setup, you should be able to:

- ✅ [ ] See Notion databases when using Notion MCP tools
- ✅ [ ] Generate images using Glif MCP tools
- ✅ [ ] See MCP servers listed in Cursor's MCP panel
- ✅ [ ] Use Claude Desktop with MCP connections

---

## Next Steps After MCP Setup

Once MCP is working:

1. **Set up Notion database** - Create your Blog Posts database
2. **Test image generation** - Generate a test image via Glif MCP
3. **Create your first blog post** - Use MCP to create posts in Notion
4. **Set up n8n workflow** - Automate publishing from Notion to Jekyll

See the other guides in the `/workflows/` folder for these next steps.

---

## Quick Reference

**Config file locations:**
- Cursor: `~/.cursor/mcp.json`
- Claude Desktop: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Key commands:**
- View Cursor config: `cat ~/.cursor/mcp.json`
- View Claude config: `cat ~/Library/Application\ Support/Claude/claude_desktop_config.json`
- Restart apps: `killall Cursor && killall Claude`

**API key locations:**
- Notion: https://www.notion.so/my-integrations
- Glif: https://glif.app/ (in API settings)

---

## Need Help?

If you're stuck:
1. Check the troubleshooting section above
2. Verify Docker is running: `docker ps`
3. Check config files are valid JSON: `cat ~/.cursor/mcp.json`
4. Make sure you fully restarted the apps (Cmd+Q, wait, reopen)

Good luck! 🚀








