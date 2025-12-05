# Blog & Social Media Workflow Documentation

This directory contains all documentation and configuration files for the automated blog post and social media creation workflow.

## Files

### Documentation

- **`blog-social-media-workflow-guide.md`** - Complete workflow guide covering all phases
- **`mcp-connection-guide.md`** - Setup guide for MCP connections (Glif and Notion)
- **`notion-blog-post-template.md`** - Template for creating blog posts in Notion

### n8n Workflows

- **`n8n-blog-publishing-workflow.json`** - Workflow for publishing blog posts from Notion to Jekyll
- **`n8n-social-media-workflow.json`** - Workflow for generating social media posts from published blogs

## Quick Start

1. **Set up MCP connections** (see `mcp-connection-guide.md`)
2. **Import n8n workflows** into your n8n instance
3. **Use Notion template** (see `notion-blog-post-template.md`) to create blog posts
4. **Follow workflow guide** (see `blog-social-media-workflow-guide.md`) for complete process

## Workflow Summary

1. Create blog draft in Notion using template
2. Use Claude via MCP to generate images with Glif
3. Mark post as "Ready to Publish" in Notion
4. n8n workflow automatically formats and publishes to Jekyll
5. Social media posts are auto-generated and sent for approval

## Requirements

- Docker MCP server with Glif and Notion connections
- n8n instance (local or cloud)
- Notion API integration
- Claude Desktop with MCP configured
- Jekyll site (this repository)

## Notes

- All workflows include approval steps for safety
- Images are generated via Glif MCP for better control
- Social media posts are generated but require manual approval before posting
- Workflows can be modified in n8n UI after import


