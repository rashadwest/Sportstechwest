# Blog Pipeline Setup Checklist

Use this checklist to set up the complete blog pipeline.

## Prerequisites

- [ ] Node.js installed (v20+)
- [ ] Git repository cloned
- [ ] Notion account with API access
- [ ] Glif account (for automation)
- [ ] GitHub repository with Actions enabled

## Step 1: Install Dependencies

```bash
cd /Users/rashadwest/Sportstechwest
npm install
```

This installs:
- `@notionhq/client` - Notion API client
- `@types/node` - TypeScript types (dev)

## Step 2: Set Up Notion Database

- [ ] Create "Blog Posts" database in Notion
- [ ] Add required properties (see `workflows/BLOG-PIPELINE-README.md` for schema)
- [ ] Create Notion integration at https://www.notion.so/my-integrations
- [ ] Share database with integration
- [ ] Copy integration token and database ID

**Database Properties Required**:
- Title (Title)
- Slug (Rich text)
- Status (Select: Draft, Draft Complete, Images Generated, Ready to Publish, In Review, Published)
- Date (Date)
- Description (Rich text)
- Thumbnail (URL)
- Tags (Multi-select)
- Categories (Multi-select: Insights, Tutorial, News)
- Author (Rich text)
- Repo Path (Rich text)
- GitHub PR (URL)
- Blog URL (URL)

## Step 3: Configure Environment Variables

Create `.env` file in project root:

```bash
NOTION_API_TOKEN=secret_xxx
NOTION_DATABASE_ID=xxx
```

**Get values**:
- Token: From Notion integration settings
- Database ID: From database URL (32-char hex string)

## Step 4: Test Local Scripts

- [ ] Test draft creation:
  ```bash
  npm run init-draft "Test Post"
  ```
  Should create `.cursor/drafts/YYYY-MM-DD-test-post.json`

- [ ] Test Notion upsert (requires valid credentials):
  ```bash
  npm run notion-upsert .cursor/drafts/YYYY-MM-DD-test-post.json
  ```
  Should create/update Notion page

- [ ] Test validation:
  ```bash
  npm run validate-post _posts/2025-10-29-Why-I-Built-a-Local-Server-to-Run-24-7.md
  ```
  Should pass validation

## Step 5: Set Up Glif Workflow

- [ ] Review `workflows/GLIF-SETUP.md` for workflow structure
- [ ] Create Glif workflow with steps:
  1. Notion trigger (Status = "Ready to Publish")
  2. Fetch Notion page
  3. Process images
  4. Call Claude (second pass)
  5. Create GitHub PR
  6. Update Notion status

- [ ] Configure Glif secrets:
  - `NOTION_API_TOKEN`
  - `GITHUB_TOKEN` (repo write access)
  - `CLAUDE_API_KEY`
  - `NOTION_DATABASE_ID`

- [ ] Test Glif workflow with a test post

## Step 6: Verify GitHub Actions

- [ ] Check `.github/workflows/blog-validate.yml` exists
- [ ] Create a test PR to verify CI runs
- [ ] Ensure Jekyll build succeeds

## Step 7: Test End-to-End Flow

1. [ ] Create draft in Cursor:
   ```bash
   npm run init-draft "My Test Post"
   ```

2. [ ] Send to Claude (first pass) - use prompt from `workflows/NOTION-CLAUDE-PROMPT.md`

3. [ ] Create Notion page:
   ```bash
   npm run notion-upsert .cursor/drafts/YYYY-MM-DD-slug.json
   ```

4. [ ] Set Status to "Ready to Publish" in Notion

5. [ ] Verify Glif workflow triggers and creates PR

6. [ ] Review PR in Cursor

7. [ ] Merge PR (if validation passes)

8. [ ] Verify post appears at https://sportstechwest.com/blogs after 2-5 minutes

## Documentation Reference

- **Main README**: `workflows/BLOG-PIPELINE-README.md`
- **Claude Prompts**: `workflows/NOTION-CLAUDE-PROMPT.md`
- **Glif Setup**: `workflows/GLIF-SETUP.md`
- **Troubleshooting**: See README troubleshooting section

## Quick Commands Reference

```bash
# Create draft
npm run init-draft "Post Title"

# Create/update Notion page
npm run notion-upsert .cursor/drafts/YYYY-MM-DD-slug.json

# Validate post
npm run validate-post _posts/YYYY-MM-DD-slug.md
```

## Next Steps After Setup

1. Start creating blog posts using the workflow
2. Customize prompts in `workflows/NOTION-CLAUDE-PROMPT.md` if needed
3. Adjust Glif workflow based on your preferences
4. Monitor CI for any validation issues

## Support

If you encounter issues:
1. Check `workflows/BLOG-PIPELINE-README.md` troubleshooting section
2. Review script outputs for error messages
3. Verify environment variables are set correctly
4. Check Glif workflow logs






