#!/bin/bash

# Direct Terminal Commands for MCP Setup
# Replace YOUR_NOTION_API_KEY and YOUR_GLIF_API_KEY with your actual keys

# Set your API keys here (replace the placeholders)
NOTION_API_KEY="YOUR_NOTION_API_KEY"
GLIF_API_KEY="YOUR_GLIF_API_KEY"
N8N_API_KEY="YOUR_N8N_API_KEY"  # Optional, leave empty if not needed

# Backup existing configs
echo "Backing up existing configs..."
mkdir -p ~/.cursor
mkdir -p ~/Library/Application\ Support/Claude

[ -f ~/.cursor/mcp.json ] && cp ~/.cursor/mcp.json ~/.cursor/mcp.json.backup.$(date +%Y%m%d_%H%M%S)
[ -f ~/Library/Application\ Support/Claude/claude_desktop_config.json ] && cp ~/Library/Application\ Support/Claude/claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json.backup.$(date +%Y%m%d_%H%M%S)

# Create Cursor config
echo "Creating Cursor MCP config..."
cat > ~/.cursor/mcp.json <<EOF
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
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    }
EOF

# Add Glif if key provided
if [ ! -z "$GLIF_API_KEY" ] && [ "$GLIF_API_KEY" != "YOUR_GLIF_API_KEY" ]; then
    cat >> ~/.cursor/mcp.json <<EOF
    ,
    "Glif": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-glif"
      ],
      "env": {
        "GLIF_API_KEY": "${GLIF_API_KEY}"
      }
    }
EOF
fi

cat >> ~/.cursor/mcp.json <<EOF
  }
}
EOF

# Create Claude Desktop config
echo "Creating Claude Desktop MCP config..."
cat > ~/Library/Application\ Support/Claude/claude_desktop_config.json <<EOF
{
  "mcpServers": {
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
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    }
EOF

# Add n8n if key provided
if [ ! -z "$N8N_API_KEY" ] && [ "$N8N_API_KEY" != "YOUR_N8N_API_KEY" ]; then
    cat >> ~/Library/Application\ Support/Claude/claude_desktop_config.json <<EOF
    ,
    "n8n-mac": {
      "command": "node",
      "args": ["/Users/rashadwest/n8n-mcp-server/index.js"],
      "env": {
        "N8N_API_KEY": "${N8N_API_KEY}",
        "N8N_API_URL": "http://localhost:5678"
      }
    }
EOF
fi

# Add Glif if key provided
if [ ! -z "$GLIF_API_KEY" ] && [ "$GLIF_API_KEY" != "YOUR_GLIF_API_KEY" ]; then
    cat >> ~/Library/Application\ Support/Claude/claude_desktop_config.json <<EOF
    ,
    "Glif": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-glif"
      ],
      "env": {
        "GLIF_API_KEY": "${GLIF_API_KEY}"
      }
    }
EOF
fi

cat >> ~/Library/Application\ Support/Claude/claude_desktop_config.json <<EOF
  }
}
EOF

echo "✅ Config files created!"
echo ""
echo "📋 Next: Restart Cursor and Claude Desktop to load the new MCP configuration"


