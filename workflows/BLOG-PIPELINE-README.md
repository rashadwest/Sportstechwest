# Blog Pipeline: Cursor → Claude → Notion → Glif → Claude → Cursor → GitHub → Jekyll

Complete documentation for the automated blog post pipeline.

## Overview

This pipeline automates the blog post creation process from initial draft to published post:

1. **Cursor**: Start here with draft intent
2. **Claude** (first pass): Generate Notion payload + Markdown outline
3. **Notion**: Store and manage content
4. **Glif**: Triggered automation when Status = "Ready to Publish"
5. **Claude** (second pass): Generate final Markdown with Jekyll front matter
6. **Cursor**: Review PR preview
7. **GitHub**: Validation and merge
8. **Jekyll**: Live blog post

## Prerequisites

### Required Setup

1. **Notion Database**: "Blog Posts" database with required properties (see below)
2. **Environment Variables**: Create `.env` file (optional, or use system env):
   ```bash
   NOTION_API_TOKEN=secret_xxx
   NOTION_DATABASE_ID=xxx
   ```
3. **Dependencies**: Install Node.js packages:
   ```bash
   npm install
   ```
4. **Notion Integration**: Create Notion integration and share database with it
5. **Glif Workflow**: Configure Glif to trigger on Notion Status changes

### Notion Database Schema

The "Blog Posts" database must have these properties:

- **Title** (Title)
- **Slug** (Rich text)
- **Status** (Select): Draft, Draft Complete, Images Generated, Ready to Publish, In Review, Published
- **Date** (Date)
- **Description** (Rich text)
- **Thumbnail** (URL)
- **Tags** (Multi-select)
- **Categories** (Multi-select): Insights, Tutorial, News
- **Author** (Rich text)
- **Body** (Page content blocks)
- **Repo Path** (Rich text, auto-filled)
- **GitHub PR** (URL, auto-filled)
- **Blog URL** (URL, auto-filled)

## Step-by-Step Workflow

### Step 1: Initiate in Cursor

Create a draft intent:

```bash
npm run init-draft "My Blog Post Title"
```

This creates `.cursor/drafts/YYYY-MM-DD-slug.json` with:
- Title
- Description
- Tags
- Category
- Notes
- Desired date

Edit the JSON file to add your content.

### Step 2: Claude First Pass (from Cursor)

In Cursor/Claude, send the draft intent with this prompt:

```
Transform this draft intent into a Notion payload and Markdown outline:

[PASTE_DRAFT_INTENT_JSON]

Generate:
1. A structured Notion payload JSON
2. A Markdown outline following the formatting rules from workflows/NOTION-CLAUDE-PROMPT.md
```

Claude will output:
- **Notion Payload**: JSON ready for Notion API
- **Markdown Outline**: Structured outline with `##` headers, no `<br>`, etc.

Save both outputs for traceability.

### Step 3: Write to Notion (from Cursor)

Create or update the Notion page:

```bash
npm run notion-upsert .cursor/drafts/YYYY-MM-DD-slug.json [notion-payload.json]
```

If you have a Claude-generated payload file, pass it as the second argument. Otherwise, the script uses the draft intent.

The script will:
- Create or update a Notion page in the "Blog Posts" database
- Set Status = "Draft"
- Add all properties and content
- Return the Notion page URL

### Step 4: Glif Triggers (Status Change)

In Notion, change the Status to **"Ready to Publish"**.

This triggers the Glif workflow which:
1. Fetches Notion page content and assets
2. Normalizes slug (kebab-case)
3. Enforces date rules (2025, after latest post)
4. Downloads images from Notion, renames to `slug-<shortid>.<ext>`
5. Places images in `assets/images/blog-img/`

### Step 5: Claude Second Pass (inside Glif)

Glif calls Claude with the prompt from `workflows/NOTION-CLAUDE-PROMPT.md` (Second Pass section).

Claude generates:
- Complete Jekyll markdown with front matter
- Properly formatted content (no `<br>`, `##` headers only, image div wrappers)
- Validated date (2025, after latest)

### Step 6: Cursor Review (PR Preview)

Glif creates/updates a GitHub PR on branch `notion/<notion-id>` with:
- `_posts/YYYY-MM-DD-<slug>.md`
- `assets/images/blog-img/<image-files>`

In Cursor:
1. Pull the PR branch
2. Review the generated markdown
3. Check formatting (use `npm run validate-post _posts/YYYY-MM-DD-slug.md`)
4. Optional: Ask Claude to review and suggest fixes

### Step 7: GitHub Validation & Merge

GitHub Actions automatically:
- Validates front matter schema
- Checks date is 2025 and after latest
- Verifies image paths exist
- Lints markdown
- Builds Jekyll site (dry-run for PRs)

When CI passes:
- Merge the PR
- GitHub Pages deploys automatically
- Post appears at `https://sportstechwest.com/blogs` in 2-5 minutes

### Step 8: Notion Status Sync

Glif webhook updates Notion:
- On PR open: Status → "In Review", GitHub PR URL set
- On PR merge: Status → "Published", Blog URL set

## Scripts Reference

### `cursor-init-draft.js`

Creates a draft intent JSON file.

```bash
node scripts/cursor-init-draft.js [title]
# or
npm run init-draft [title]
```

**Output**: `.cursor/drafts/YYYY-MM-DD-slug.json`

### `notion-upsert.js`

Creates or updates a Notion page from draft intent or Claude payload.

```bash
node scripts/notion-upsert.js <draft-file.json> [notion-payload.json]
# or
npm run notion-upsert <draft-file.json> [notion-payload.json]
```

**Requirements**:
- `NOTION_API_TOKEN` environment variable
- `NOTION_DATABASE_ID` environment variable

**Output**: Notion page URL

### `validate-post.js`

Validates a Jekyll blog post file.

```bash
node scripts/validate-post.js <post-file.md>
# or
npm run validate-post <post-file.md>
```

**Checks**:
- Front matter schema (all required fields)
- Date is 2025 and after latest post
- Tags/categories format (arrays in brackets)
- Thumbnail path exists
- Image paths in content exist
- Markdown format (no `<br>`, `##` headers only)

**Exit codes**: 0 = pass, 1 = fail

## Formatting Rules

### Critical Rules (Enforced)

1. **No `<br>` tags**: Use blank lines between paragraphs
2. **Headers**: Use `##` only (not `###`)
3. **Section breaks**: Use `---` on its own line
4. **Images**: Wrap in `<div class="text-center my-4">` blocks
5. **Tags/Categories**: Must be arrays in brackets: `[tag1, tag2]`
6. **Date**: Must be 2025 and after latest post

### Front Matter Template

```yaml
---
layout: post
title: "Your Title Here"
description: "SEO-friendly description (150-160 characters)"
thumbnail: "/assets/images/blog-img/filename.png"
badge_color: "text-bg-primary"
trending: false
simple_nav: true
date: 2025-MM-DD
tags: [tag1, tag2, tag3]
categories: [Insights]
author: "Rashad West"
---
```

### Image Format

```html
<div class="text-center my-4">
  <img src="/assets/images/blog-img/filename.png" alt="Description" class="img-fluid">
</div>
```

## Troubleshooting

### Notion API Errors

**Error**: `NOTION_API_TOKEN not set`
- **Solution**: Create `.env` file or set environment variable
- **Check**: Integration has access to database

**Error**: `NOTION_DATABASE_ID not set`
- **Solution**: Get database ID from Notion URL (32-char hex string)
- **Format**: `https://notion.so/[database-id]`

### Date Validation Failures

**Error**: `Date must be after latest post date`
- **Solution**: Check latest post with `glob_file_search _posts/2025-*.md`
- **Fix**: Use a date after the latest post

**Error**: `Date year must be 2025`
- **Solution**: Ensure date is in 2025 (not 2024)

### Image Path Errors

**Error**: `Image not found: /assets/images/blog-img/filename.png`
- **Solution**: Ensure images are in `assets/images/blog-img/`
- **Check**: Image filenames match exactly (case-sensitive)

### Markdown Format Errors

**Error**: `Found <br> tags`
- **Solution**: Remove all `<br>` tags, use blank lines instead

**Error**: `Found ### headers`
- **Solution**: Change `###` to `##`

### Glif Workflow Issues

**Issue**: Glif not triggering
- **Check**: Notion Status is "Ready to Publish"
- **Check**: Glif webhook is configured correctly
- **Check**: Notion integration has proper permissions

**Issue**: PR not created
- **Check**: Glif has GitHub token with repo write access
- **Check**: Branch name doesn't conflict (uses Notion ID)

### CI Validation Failures

**Error**: `Jekyll build failed`
- **Check**: Front matter syntax (valid YAML)
- **Check**: Markdown syntax (no invalid characters)
- **Check**: All referenced images exist

**Error**: `Validation errors`
- **Run**: `npm run validate-post _posts/filename.md` locally
- **Fix**: Address all errors before pushing

## Idempotency

The pipeline is designed to be idempotent:

- **Notion Page ID** = immutable identity
- Branch name: `notion/<page-id>` (deterministic)
- PR title: `Post: <Title>` (deterministic)
- File paths: `_posts/YYYY-MM-DD-<slug>.md` (deterministic)

Re-running the flow updates the same branch/PR without creating duplicates.

## Environment Variables

Create `.env` file (or use system environment):

```bash
NOTION_API_TOKEN=secret_xxx
NOTION_DATABASE_ID=xxx
```

Optional (for dotenv support):
```bash
npm install dotenv
```

## File Structure

```
.
├── .cursor/
│   └── drafts/              # Draft intent JSON files
├── scripts/
│   ├── cursor-init-draft.js  # Create draft intent
│   ├── notion-upsert.js      # Create/update Notion page
│   └── validate-post.js      # Validate blog post
├── workflows/
│   ├── NOTION-CLAUDE-PROMPT.md  # Claude prompts (both passes)
│   └── BLOG-PIPELINE-README.md  # This file
├── .github/
│   └── workflows/
│       └── blog-validate.yml    # CI validation
└── _posts/                  # Published blog posts
```

## Quick Reference

### Start New Post
```bash
npm run init-draft "My Title"
# Edit .cursor/drafts/YYYY-MM-DD-slug.json
# Send to Claude (first pass)
npm run notion-upsert .cursor/drafts/YYYY-MM-DD-slug.json
```

### Validate Post
```bash
npm run validate-post _posts/2025-MM-DD-slug.md
```

### Check Latest Post Date
```bash
glob_file_search _posts/2025-*.md
```

### Update Notion Status
- In Notion: Change Status to "Ready to Publish" → triggers Glif
- Glif creates PR → review in Cursor
- Merge PR → auto-deploys to blog

## Support

For issues or questions:
1. Check troubleshooting section above
2. Review `workflows/NOTION-CLAUDE-PROMPT.md` for prompt details
3. Validate locally with `validate-post.js` before pushing
4. Check CI logs for validation errors






