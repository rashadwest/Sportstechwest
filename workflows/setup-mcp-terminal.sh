#!/bin/bash

# Terminal-based MCP Setup - Interactive
# This script will guide you through setting up MCP via terminal

echo "🔧 MCP Setup via Terminal"
echo "========================="
echo ""

# Step 1: Get API keys
echo "📝 Step 1: Enter your API keys"
echo "------------------------------"
echo ""

read -p "Enter your Notion API Key (starts with 'secret_'): " NOTION_API_KEY
read -p "Enter your Glif API Key (or press Enter to skip): " GLIF_API_KEY
read -p "Enter your n8n API Key (or press Enter to skip): " N8N_API_KEY
if [ ! -z "$N8N_API_KEY" ]; then
    read -p "Enter your n8n URL (e.g., http://192.168.1.100:5678 or http://raspberrypi.local:5678, or press Enter for localhost:5678): " N8N_API_URL
    N8N_API_URL=${N8N_API_URL:-"http://localhost:5678"}
fi

if [ -z "$NOTION_API_KEY" ]; then
    echo "❌ Notion API Key is required!"
    exit 1
fi

echo ""
echo "✅ Keys collected"
echo ""

# Step 2: Backup existing configs
echo "📦 Step 2: Backing up existing configs..."
echo "-----------------------------------------"

mkdir -p ~/.cursor
mkdir -p ~/Library/Application\ Support/Claude

if [ -f ~/.cursor/mcp.json ]; then
    cp ~/.cursor/mcp.json ~/.cursor/mcp.json.backup.$(date +%Y%m%d_%H%M%S)
    echo "✅ Backed up Cursor config"
fi

if [ -f ~/Library/Application\ Support/Claude/claude_desktop_config.json ]; then
    cp ~/Library/Application\ Support/Claude/claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json.backup.$(date +%Y%m%d_%H%M%S)
    echo "✅ Backed up Claude Desktop config"
fi

echo ""

# Step 3: Create Cursor config
echo "⚙️  Step 3: Creating Cursor config..."
echo "-------------------------------------"

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

if [ ! -z "$GLIF_API_KEY" ]; then
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

echo "✅ Cursor config created at ~/.cursor/mcp.json"
echo ""

# Step 4: Create Claude Desktop config
echo "⚙️  Step 4: Creating Claude Desktop config..."
echo "---------------------------------------------"

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

if [ ! -z "$N8N_API_KEY" ]; then
    cat >> ~/Library/Application\ Support/Claude/claude_desktop_config.json <<EOF
    ,
    "n8n-mac": {
      "command": "node",
      "args": ["/Users/rashadwest/n8n-mcp-server/index.js"],
      "env": {
        "N8N_API_KEY": "${N8N_API_KEY}",
        "N8N_API_URL": "${N8N_API_URL}"
      }
    }
EOF
fi

if [ ! -z "$GLIF_API_KEY" ]; then
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

echo "✅ Claude Desktop config created"
echo ""

# Step 5: Verify
echo "🔍 Step 5: Verifying configs..."
echo "-------------------------------"

echo ""
echo "Cursor config exists:"
ls -lh ~/.cursor/mcp.json

echo ""
echo "Claude Desktop config exists:"
ls -lh ~/Library/Application\ Support/Claude/claude_desktop_config.json

echo ""
echo "Config contents preview:"
echo "  Notion API Key: ${NOTION_API_KEY:0:20}..."
if [ ! -z "$GLIF_API_KEY" ]; then
    echo "  Glif API Key: ${GLIF_API_KEY:0:20}..."
fi
if [ ! -z "$N8N_API_KEY" ]; then
    echo "  n8n API Key: ${N8N_API_KEY:0:20}..."
    echo "  n8n URL: ${N8N_API_URL}"
fi

echo ""
echo "✅ Setup Complete!"
echo ""
echo "📋 Next Steps:"
echo "1. Restart Cursor: killall Cursor && open -a Cursor"
echo "2. Restart Claude Desktop: killall Claude && open -a Claude"
echo ""
echo "Or manually:"
echo "  - Press Cmd+Q in both apps to quit completely"
echo "  - Then reopen them"
echo ""
echo "Test commands after restart:"
echo "  In Cursor: 'Test Notion MCP: Search for databases in my Notion workspace'"
if [ ! -z "$GLIF_API_KEY" ]; then
    echo "  In Cursor: 'Test Glif MCP: Generate a test image'"
fi

