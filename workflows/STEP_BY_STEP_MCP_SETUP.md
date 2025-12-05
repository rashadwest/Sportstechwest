# Step-by-Step MCP Bridge Setup

## Understanding What We're Doing

These are **system configuration files**, not project files. They go in your home directory, not in your project folder.

- `~/.cursor/mcp.json` → Tells Cursor how to connect to MCP servers
- `~/Library/Application Support/Claude/claude_desktop_config.json` → Tells Claude Desktop how to connect to MCP servers

You can run these commands from **anywhere** in terminal - they use absolute paths.

---

## Step 1: Open Terminal

Open Terminal (you can be in any folder - doesn't matter).

---

## Step 2: Set Your API Keys as Variables

Type these commands one at a time, **replacing with your actual keys**:

```bash
export NOTION_API_KEY="secret_paste_your_notion_key_here"
```

Press Enter, then:

```bash
export GLIF_API_KEY="paste_your_glif_key_here"
```

Press Enter.

**To verify they're set:**
```bash
echo $NOTION_API_KEY
echo $GLIF_API_KEY
```

You should see your keys (don't worry, they're just in your current terminal session).

---

## Step 3: Create Directories (if they don't exist)

```bash
mkdir -p ~/.cursor
mkdir -p ~/Library/Application\ Support/Claude
```

Press Enter. This creates the folders if they don't exist.

---

## Step 4: Backup Existing Configs (if they exist)

```bash
[ -f ~/.cursor/mcp.json ] && cp ~/.cursor/mcp.json ~/.cursor/mcp.json.backup
[ -f ~/Library/Application\ Support/Claude/claude_desktop_config.json ] && cp ~/Library/Application\ Support/Claude/claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json.backup
```

Press Enter. This backs up your existing configs if they exist.

---

## Step 5: Create Cursor Config File

Copy this **entire block** and paste into terminal (it will create the file):

```bash
cat > ~/.cursor/mcp.json <<'EOF'
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
        "NOTION_API_KEY": "'${NOTION_API_KEY}'"
      }
    },
    "Glif": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-glif"],
      "env": {
        "GLIF_API_KEY": "'${GLIF_API_KEY}'"
      }
    }
  }
}
EOF
```

Press Enter. This creates the Cursor config file.

---

## Step 6: Create Claude Desktop Config File

Copy this **entire block** and paste into terminal:

```bash
cat > ~/Library/Application\ Support/Claude/claude_desktop_config.json <<'EOF'
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
        "NOTION_API_KEY": "'${NOTION_API_KEY}'"
      }
    },
    "Glif": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-glif"],
      "env": {
        "GLIF_API_KEY": "'${GLIF_API_KEY}'"
      }
    },
    "n8n-mac": {
      "command": "node",
      "args": ["/Users/rashadwest/n8n-mcp-server/index.js"],
      "env": {
        "N8N_API_KEY": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzMzAyMWQzZC1jOWE1LTQ3ZjEtYTkxNS02NTM0NTEyZTg0ZjYiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzU5NTI0MzE5LCJleHAiOjE3NjIwNTYwMDB9.hqrB10KbNkWYpDenr3BprLndebyVPbsWb0Bme_H7DNQ",
        "N8N_API_URL": "http://localhost:5678"
      }
    }
  }
}
EOF
```

Press Enter. This creates the Claude Desktop config file.

---

## Step 7: Verify Files Were Created

Check that the files exist and look correct:

```bash
cat ~/.cursor/mcp.json
```

Press Enter. You should see JSON with your Notion and Glif keys.

```bash
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Press Enter. You should see JSON with all three services.

---

## Step 8: Restart Applications

**Important:** You must fully quit and restart both apps for the config to take effect.

**In terminal, you can do:**

```bash
killall Cursor
killall Claude
```

Then manually reopen:
- Cursor
- Claude Desktop

**OR** manually:
- Cursor: Press Cmd+Q (quit completely)
- Claude Desktop: Press Cmd+Q (quit completely)
- Then reopen both apps

---

## Step 9: Test the Connection

After restarting Cursor, try this in Cursor:

```
Test Notion MCP: Search for databases in my Notion workspace
```

If it works, you'll see your Notion databases listed.

---

## Troubleshooting

### If files don't exist after running commands:
```bash
# Check if directories exist
ls -la ~/.cursor/
ls -la ~/Library/Application\ Support/Claude/

# Check if files were created
ls -la ~/.cursor/mcp.json
ls -la ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### If you need to restore backups:
```bash
cp ~/.cursor/mcp.json.backup ~/.cursor/mcp.json
cp ~/Library/Application\ Support/Claude/claude_desktop_config.json.backup ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### If JSON is malformed:
The `cat > file <<'EOF'` commands should create valid JSON. If there's an error, check:
- Did you copy the entire block including the `EOF` at the end?
- Are your API keys in quotes?
- Did you close all brackets?

---

## Summary

1. Set API keys as environment variables
2. Create config directories
3. Backup existing configs
4. Create Cursor config file
5. Create Claude Desktop config file
6. Verify files exist
7. Restart both applications
8. Test connection

**You can run all these commands from anywhere - they use absolute paths (`~/.cursor/` and `~/Library/`) so the current directory doesn't matter.**


