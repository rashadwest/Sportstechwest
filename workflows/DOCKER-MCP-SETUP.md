# Docker MCP Setup - All Servers Through Docker

## Current Configuration

✅ **Docker MCP is working!** All MCP servers should be managed through Docker Desktop's MCP Toolkit, not via direct npx commands.

## What Changed

- **Removed:** Direct Notion and Glif npx configurations (they were causing errors)
- **Kept:** MCP_DOCKER gateway (this connects to Docker Desktop's MCP Toolkit)
- **Kept:** n8n-mac (local Node.js server, not managed by Docker)

## How It Works

1. **MCP_DOCKER** connects Claude Desktop to Docker Desktop's MCP Toolkit
2. **Docker Desktop** manages all MCP servers (Notion, Glif, etc.) as containers
3. **Claude Desktop** accesses them through the Docker MCP gateway

## Next Steps

### Add Notion and Glif to Docker Desktop

1. Open **Docker Desktop**
2. Go to **Models → MCP Toolkit**
3. Click the **"Catalog"** tab
4. Search for **"Notion"** and **"Glif"**
5. Add them as servers (they'll run as Docker containers)
6. Configure API keys through Docker Desktop's UI

### Current Config File

The Claude Desktop config now only includes:
- `MCP_DOCKER` - Gateway to Docker Desktop MCP Toolkit
- `n8n-mac` - Your local n8n server (not Docker-managed)

## Benefits

✅ All MCP servers managed in one place (Docker Desktop)  
✅ No direct npx dependencies  
✅ Better containerization and isolation  
✅ Easier to start/stop servers  
✅ Centralized configuration  

## Restart Required

**Fully quit and restart Claude Desktop** (Cmd+Q, then reopen) for the changes to take effect.

After restarting, Docker Desktop should recognize Claude Desktop and the Notion/Glif servers should work through Docker MCP!

