# MCP Connection Setup Guide

## Overview

This guide covers setting up MCP (Model Context Protocol) connections for Glif and Notion in your Docker MCP server environment.

## Prerequisites

- Docker MCP server running
- Glif API access configured
- Notion API key and integration
- Claude Desktop or compatible MCP client

## Glif MCP Connection

### Configuration

1. **Verify Glif is accessible via Docker:**
   ```bash
   docker ps | grep glif
   ```

2. **MCP Server Config** (in Claude Desktop `claude_desktop_config.json`):
   ```json
   {
     "mcpServers": {
       "glif": {
         "command": "docker",
         "args": [
           "exec",
           "glif-container",
           "glif-mcp-server"
         ],
         "env": {
           "GLIF_API_KEY": "your-api-key-here"
         }
       }
     }
   }
   ```

3. **Test Connection:**
   - In Claude, use: "Generate an image using Glif with this prompt: [your prompt]"
   - Should return image URL or base64 data

### Available MCP Tools

- `generate_image`: Generate image from text prompt
- `list_models`: List available Glif models
- `get_image_status`: Check generation status

## Notion MCP Connection

### Configuration

1. **Create Notion Integration:**
   - Go to https://www.notion.so/my-integrations
   - Create new integration
   - Copy API key
   - Share your database with the integration

2. **MCP Server Config:**
   ```json
   {
     "mcpServers": {
       "notion": {
         "command": "docker",
         "args": [
           "exec",
           "notion-container",
           "notion-mcp-server"
         ],
         "env": {
           "NOTION_API_KEY": "your-notion-api-key",
           "NOTION_DATABASE_ID": "your-database-id"
         }
       }
     }
   }
   ```

3. **Test Connection:**
   - In Claude: "Read my latest blog post draft from Notion"
   - Should return page content

### Available MCP Tools

- `read_page`: Read Notion page content
- `create_page`: Create new Notion page
- `update_page`: Update existing page
- `query_database`: Query Notion database
- `search_pages`: Search Notion pages

## Workflow Integration

### Using MCP in Claude

1. **Read Blog Draft:**
   ```
   Use Notion MCP to read the blog post draft titled "[Post Title]"
   ```

2. **Generate Image Prompts:**
   ```
   Based on this blog content, create 3 detailed image generation prompts for Glif
   ```

3. **Generate Images:**
   ```
   Use Glif MCP to generate an image with this prompt: [prompt]
   ```

4. **Store in Notion:**
   ```
   Use Notion MCP to update the blog post with the generated image URLs
   ```

## Troubleshooting

### Glif Connection Issues

- **Check Docker container status:** `docker logs glif-container`
- **Verify API key:** Ensure GLIF_API_KEY is set correctly
- **Test API directly:** Use curl to test Glif API outside Docker

### Notion Connection Issues

- **Check integration permissions:** Ensure integration has access to database
- **Verify database ID:** Use Notion API explorer to confirm database ID
- **Check rate limits:** Notion API has rate limits, implement retry logic

## Next Steps

1. Test both MCP connections separately
2. Test combined workflow: Read from Notion → Generate with Glif → Update Notion
3. Set up n8n workflow to monitor Notion changes
4. Configure automated image download and processing


