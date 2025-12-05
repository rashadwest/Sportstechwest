#!/bin/bash

# MCP Bridge Setup Script
# This script helps configure MCP connections for Cursor and Claude Desktop

set -e

echo "🔧 MCP Bridge Setup Script"
echo "=========================="
echo ""

# Check if Docker is running
echo "Checking Docker..."
if ! docker ps &> /dev/null; then
    echo "❌ Docker is not running!"
    echo "   Please start Docker Desktop and run this script again."
    exit 1
fi
echo "✅ Docker is running"
echo ""

# Backup existing configs
echo "Creating backups..."
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

# Get API keys
echo "📝 API Keys Setup"
echo "----------------"
echo ""
read -p "Enter your Notion API Key (starts with 'secret_'): " NOTION_API_KEY
read -p "Enter your Glif API Key (or press Enter to skip): " GLIF_API_KEY
read -p "Enter your n8n API Key (or press Enter to skip): " N8N_API_KEY

if [ -z "$NOTION_API_KEY" ]; then
    echo "❌ Notion API Key is required!"
    exit 1
fi

echo ""
echo "Creating Cursor config..."

# Create Cursor config
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
        "NOTION_API_KEY": "$NOTION_API_KEY"
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
        "GLIF_API_KEY": "$GLIF_API_KEY"
      }
    }
EOF
fi

cat >> ~/.cursor/mcp.json <<EOF
  }
}
EOF

echo "✅ Cursor config created"
echo ""

echo "Creating Claude Desktop config..."

# Create Claude Desktop config
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
        "NOTION_API_KEY": "$NOTION_API_KEY"
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
        "N8N_API_KEY": "$N8N_API_KEY",
        "N8N_API_URL": "http://localhost:5678"
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
        "GLIF_API_KEY": "$GLIF_API_KEY"
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
echo "✅ Setup complete!"
echo ""
echo "📋 Next Steps:"
echo "1. Fully quit and restart Cursor (Cmd+Q, then reopen)"
echo "2. Fully quit and restart Claude Desktop (Cmd+Q, then reopen)"
echo "3. Test connections in both apps"
echo ""
echo "Test commands:"
echo "  In Cursor: 'Test Notion MCP: Search for databases in my Notion workspace'"
if [ ! -z "$GLIF_API_KEY" ]; then
    echo "  In Cursor: 'Test Glif MCP: Generate a test image'"
fi
echo ""


