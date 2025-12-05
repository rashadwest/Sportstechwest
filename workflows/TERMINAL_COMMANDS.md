# Terminal Commands for MCP Setup

## Quick Copy-Paste Commands

Replace `YOUR_NOTION_API_KEY` and `YOUR_GLIF_API_KEY` with your actual keys, then paste these commands into terminal:

### Step 1: Set Your API Keys as Variables

```bash
export NOTION_API_KEY="secret_your_actual_notion_key_here"
export GLIF_API_KEY="your_actual_glif_key_here"
export N8N_API_KEY="your_n8n_key_here"  # Optional, can skip if not needed
```

### Step 2: Backup Existing Configs

```bash
mkdir -p ~/.cursor
mkdir -p ~/Library/Application\ Support/Claude
[ -f ~/.cursor/mcp.json ] && cp ~/.cursor/mcp.json ~/.cursor/mcp.json.backup
[ -f ~/Library/Application\ Support/Claude/claude_desktop_config.json ] && cp ~/Library/Application\ Support/Claude/claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json.backup
```

### Step 3: Create Cursor Config

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

### Step 4: Create Claude Desktop Config

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
    },
    "n8n-mac": {
      "command": "node",
      "args": ["/Users/rashadwest/n8n-mcp-server/index.js"],
      "env": {
        "N8N_API_KEY": "${N8N_API_KEY}",
        "N8N_API_URL": "http://localhost:5678"
      }
    }
  }
}
EOF
```

### Step 5: Verify Configs Were Created

```bash
cat ~/.cursor/mcp.json
echo ""
echo "---"
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

---

## All-in-One Command (Replace Keys First!)

Copy this entire block, replace the keys, then paste:

```bash
export NOTION_API_KEY="secret_your_key_here"
export GLIF_API_KEY="your_glif_key_here"

mkdir -p ~/.cursor ~/Library/Application\ Support/Claude

cat > ~/.cursor/mcp.json <<'CURSOREOF'
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
CURSOREOF

cat > ~/Library/Application\ Support/Claude/claude_desktop_config.json <<'CLAUDEEOF'
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
CLAUDEEOF

echo "✅ Config files created! Restart Cursor and Claude Desktop."
```

---

## After Running Commands

1. **Restart Cursor:** `killall Cursor` then reopen
2. **Restart Claude Desktop:** `killall Claude` then reopen
3. **Test in Cursor:** "Test Notion MCP: Search for databases"

---

## Troubleshooting

If configs look wrong:
```bash
# View what was created
cat ~/.cursor/mcp.json
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Restore backups
cp ~/.cursor/mcp.json.backup ~/.cursor/mcp.json
```


