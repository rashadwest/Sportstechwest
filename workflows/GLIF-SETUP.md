# Glif Workflow Setup

This document describes how to configure the Glif workflow for the blog pipeline.

## Overview

The Glif workflow is triggered when a Notion page Status changes to "Ready to Publish". It:
1. Fetches Notion page content and assets
2. Normalizes slug and enforces date rules
3. Downloads and renames images
4. Calls Claude (second pass) to generate final markdown
5. Creates/updates GitHub PR
6. Syncs status back to Notion

## Prerequisites

1. **Glif Account**: Access to Glif platform
2. **Notion Integration**: Connected to your Notion workspace
3. **GitHub Token**: Personal access token with repo write access
4. **Claude API Key**: For content generation (second pass)

## Glif Workflow Steps

### 1. Trigger: Notion Status Change

**Trigger Type**: Notion Webhook / Database Change

**Condition**: 
- Database: "Blog Posts"
- Property: Status
- Value: "Ready to Publish"

**Configuration**:
- Notion Integration Token
- Database ID

### 2. Fetch Notion Page

**Action**: Get Notion Page Content

**Inputs**:
- Page ID (from trigger)
- Include blocks (true)
- Include properties (true)

**Output**: Page object with properties and blocks

### 3. Extract and Normalize Data

**Action**: Transform Data (JavaScript/Node)

**Script**:
```javascript
const title = page.properties.Title.title[0].plain_text;
const slug = page.properties.Slug?.rich_text[0]?.plain_text || 
  title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');

const date = page.properties.Date?.date?.start || new Date().toISOString().split('T')[0];
// Ensure date is 2025 and after latest post
const latestPostDate = getLatestPostDate(); // Implement this
const postDate = ensureDateAfterLatest(date, latestPostDate);

const tags = page.properties.Tags?.multi_select?.map(t => t.name) || [];
const category = page.properties.Categories?.multi_select?.[0]?.name || 'Insights';
const description = page.properties.Description?.rich_text[0]?.plain_text || '';
const thumbnail = page.properties.Thumbnail?.url || '';
```

### 4. Download and Process Images

**Action**: Download Images from Notion

**Steps**:
1. Extract image URLs from page blocks
2. Download each image
3. Rename to: `slug-<shortid>.<ext>`
4. Store temporarily for upload

**Output**: Array of image objects with:
- Original URL
- New filename
- Local path

### 5. Call Claude (Second Pass)

**Action**: Claude API Call

**Model**: claude-3-5-sonnet-20241022 (or latest)

**System Prompt**: Use prompt from `workflows/NOTION-CLAUDE-PROMPT.md` (Second Pass section)

**User Prompt**:
```
Transform this Notion content into a Jekyll blog post:

Title: {{title}}
Description: {{description}}
Tags: {{tags}}
Category: {{category}}
Date: {{postDate}}
Thumbnail: {{thumbnail}}
Body Content:
{{bodyContent}}

Generate the complete markdown file with front matter following ALL formatting rules.
```

**Output**: Complete markdown string

### 6. Create/Update GitHub PR

**Action**: GitHub API / Git Operations

**Branch**: `notion/{{pageId}}` (use Notion page ID)

**Steps**:
1. Check if branch exists
2. Create or checkout branch
3. Write markdown to `_posts/YYYY-MM-DD-{{slug}}.md`
4. Upload images to `assets/images/blog-img/`
5. Commit changes
6. Push branch
7. Create or update PR

**PR Title**: `Post: {{title}}`
**PR Body**: 
```
Auto-generated from Notion page: {{notionUrl}}

Status: Ready for review
```

### 7. Update Notion Status

**Action**: Update Notion Page

**Updates**:
- Status: "In Review"
- GitHub PR: PR URL
- Repo Path: `_posts/YYYY-MM-DD-{{slug}}.md`

### 8. Handle PR Merge (Webhook)

**Trigger**: GitHub Webhook (PR merged event)

**Action**: Update Notion Page

**Updates**:
- Status: "Published"
- Blog URL: `https://sportstechwest.com/blogs`

## Date Validation Logic

```javascript
function getLatestPostDate() {
  // Query GitHub API or use cached data
  // Get all files in _posts/2025-*.md
  // Parse dates from front matter
  // Return latest date
}

function ensureDateAfterLatest(date, latestDate) {
  const postDate = new Date(date);
  const latest = latestDate ? new Date(latestDate) : new Date('2025-01-01');
  
  if (postDate.getFullYear() !== 2025) {
    postDate.setFullYear(2025);
  }
  
  if (postDate <= latest) {
    // Set to next day after latest
    postDate.setDate(latest.getDate() + 1);
  }
  
  return postDate.toISOString().split('T')[0];
}
```

## Image Processing

```javascript
function processImages(blocks, slug) {
  const images = [];
  const shortId = nanoid(8); // or use timestamp
  
  for (const block of blocks) {
    if (block.type === 'image') {
      const url = block.image.file?.url || block.image.external?.url;
      const ext = url.split('.').pop().split('?')[0] || 'png';
      const filename = `${slug}-${shortId}-${images.length}.${ext}`;
      
      images.push({
        url,
        filename,
        path: `assets/images/blog-img/${filename}`
      });
    }
  }
  
  return images;
}
```

## Error Handling

**Validation Errors**:
- If date is invalid, set to next available date
- If images fail to download, continue without them (log warning)
- If Claude call fails, retry up to 3 times
- If GitHub PR fails, update Notion with error status

**Status Updates**:
- On error: Set Notion Status to "Draft" with error note
- On success: Set Status to "In Review"

## Secrets Configuration

In Glif, configure these secrets:
- `NOTION_API_TOKEN`: Notion integration token
- `GITHUB_TOKEN`: GitHub personal access token (repo write)
- `CLAUDE_API_KEY`: Anthropic API key
- `NOTION_DATABASE_ID`: Blog Posts database ID

## Testing

1. Create test post in Notion
2. Set Status to "Ready to Publish"
3. Monitor Glif workflow execution
4. Verify PR created correctly
5. Check validation passes
6. Test merge and deployment

## Troubleshooting

**Glif not triggering**:
- Check Notion webhook configuration
- Verify Status value matches exactly "Ready to Publish"
- Check Glif logs for errors

**PR not created**:
- Verify GitHub token has repo write access
- Check branch name doesn't conflict
- Review Glif error logs

**Images not uploaded**:
- Check image download permissions
- Verify file paths are correct
- Ensure GitHub token has write access

**Date validation fails**:
- Check latest post date logic
- Verify date format (YYYY-MM-DD)
- Ensure year is 2025

## Notes

- The actual Glif workflow configuration must be done in the Glif UI
- This document provides the structure and logic, not the exact Glif nodes
- Adapt the steps to your Glif workflow builder interface
- Test thoroughly before deploying to production






