<!-- 0ca49b8e-91a1-4716-9dc6-6407ff10bcde e3768788-2e2e-4b8e-b6c8-982534ea490d -->
# Notion Blog Workflow Setup & Execution Plan

## Phase 1: Notion Setup (Start Today)

### Step 1: Create Notion Database

1. Open Notion
2. Create new database (Table view)
3. Name it "Blog Posts" or "Content Pipeline"
4. Add the following properties:

- **Title** (Title type)
- **Status** (Select type) - Options: Draft, Draft Complete, Images Generated, Ready to Publish, Published
- **Date** (Date type)
- **Description** (Text type)
- **Thumbnail** (URL type)
- **Tags** (Multi-select type)
- **Categories** (Multi-select type)
- **Author** (Text type) - Default: "Rashad West"
- **Slug** (Text type) - Auto-generated from title
- **Image URLs** (Text type) - For storing Glif-generated image URLs

### Step 2: Create Template Page

1. In the database, create a new page
2. Copy content from `/workflows/notion-blog-post-template.md`
3. Format as Notion page with:

- Front Matter section (toggle/collapsible)
- Blog Content section
- Image Prompts section
- Social Media Excerpts section
- Status checklist

4. Save as template: Click "..." menu → "Templates" → "New template"
5. Name it "Blog Post Template"

### Step 3: Create First Blog Post (Your Server Build Post)

1. Click "New" in your Blog Posts database
2. Select "Blog Post Template"
3. Fill in front matter:

- Title: Your server build post title
- Date: Today's date (YYYY-MM-DD)
- Description: SEO-friendly description
- Tags: [server, docker, mcp, automation]
- Categories: [Insights]

4. Write blog content about building your server
5. Add image prompts for visuals you need
6. Set Status to "Draft"

---

## Phase 2: Notion API Integration (Today)

### Step 1: Create Notion Integration

1. Go to https://www.notion.so/my-integrations
2. Click "+ New integration"
3. Name it "Blog Workflow" or "Content Automation"
4. Choose workspace
5. Copy the **Internal Integration Token** (starts with `secret_`)
6. Click "Submit"

### Step 2: Share Database with Integration

1. Open your Blog Posts database in Notion
2. Click "..." menu (top right)
3. Click "Add connections" or "Connections"
4. Select your "Blog Workflow" integration
5. Click "Confirm"

### Step 3: Get Database ID

1. Open your Blog Posts database
2. Copy the URL from browser
3. Extract the database ID (the long string before the `?`)
4. Format: `https://www.notion.so/workspace/DATABASE_ID?v=...`
5. Save both Integration Token and Database ID securely

---

## Phase 3: MCP Server Configuration (Next)

### Step 1: Verify Docker Containers

1. Check if Glif container is running: `docker ps | grep glif`
2. Check if Notion MCP server is running: `docker ps | grep notion`
3. If not running, start containers using your Docker setup

### Step 2: Configure Claude Desktop MCP

1. Open Claude Desktop config file:

- Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. Add Notion MCP server config (see `/workflows/mcp-connection-guide.md`)
3. Add Glif MCP server config (if not already added)
4. Restart Claude Desktop completely

### Step 3: Test MCP Connections

1. In Claude, test Notion: "Use Notion MCP to read my blog posts database"
2. In Claude, test Glif: "Use Glif MCP to generate a simple test image"
3. Verify both connections work before proceeding

---

## Phase 4: Image Generation Workflow (After MCP Setup)

### Step 1: Generate Images for First Blog Post

1. In Claude, say: "Read my blog post draft titled '[Your Post Title]' from Notion"
2. Then: "Based on this content, create detailed image generation prompts for each image needed"
3. For each prompt, say: "Use Glif MCP to generate an image with this prompt: [prompt]"
4. Copy image URLs from Claude responses

### Step 2: Add Images to Notion

1. Open your blog post in Notion
2. Add image URLs to "Image URLs" property
3. Or embed images directly in the page
4. Download images locally for optimization
5. Upload optimized images to `/assets/images/blog-img/`

### Step 3: Update Status

1. Set Status to "Images Generated"
2. Review entire post one more time
3. Set Status to "Ready to Publish" when complete

---

## Phase 5: n8n Workflow Setup (Later)

### Step 1: Import Blog Publishing Workflow

1. Open n8n
2. Click "Workflows" → "Import from File"
3. Select `/workflows/n8n-blog-publishing-workflow.json`
4. Configure credentials:

- Add Notion API credentials (use Integration Token)
- Set `NOTION_DATABASE_ID` environment variable
- Configure file system path for `_posts/` directory

### Step 2: Test Workflow

1. Create a test blog post in Notion
2. Set status to "Ready to Publish"
3. Manually trigger n8n workflow
4. Verify markdown file is created in `_posts/`
5. Check formatting and image paths

### Step 3: Set Up Social Media Workflow (Optional)

1. Import `/workflows/n8n-social-media-workflow.json`
2. Configure Twitter, LinkedIn credentials (if automating posting)
3. Or use workflow to generate drafts for manual posting

---

## Phase 6: Daily Workflow (After Setup)

### Creating a New Blog Post:

1. In Notion, create new page from "Blog Post Template"
2. Fill in front matter and write content
3. Add image prompts
4. Set Status to "Draft"
5. Use Claude + MCP to generate images
6. Add images to Notion and upload to server
7. Set Status to "Ready to Publish"
8. n8n workflow auto-publishes to Jekyll
9. Social media posts generated (review and approve)

---

## Phase 7: BallCODE Book Project Setup

### Step 1: Create Book Projects Database in Notion

1. Open Notion
2. Create new database (Table view)
3. Name it "BallCODE Book Project" or "Book Development"
4. Add the following properties:

- **Title** (Title type) - Default: "BallCODE: Coding and Math for Basketball Programming"
- **Status** (Select type) - Options: Planning, Outline Complete, Chapter Draft, In Review, Edited, Final Review, Published
- **Chapter Number** (Number type)
- **Chapter Title** (Text type)
- **Word Count** (Number type)
- **Completion %** (Number type) - 0-100
- **Date Started** (Date type)
- **Date Completed** (Date type)
- **Tags** (Multi-select type) - [coding, math, basketball, exercises, examples]
- **Author** (Text type) - Default: "Rashad West"
- **Editor** (Text type)
- **Reviewer** (Text type)
- **Notes** (Text type)
- **Code Examples** (Text type) - For storing code snippet references
- **Image Prompts** (Text type) - For Glif-generated diagrams
- **Revision Count** (Number type)

### Step 2: Create Book Chapter Template

1. In the Book Projects database, create a new page
2. Create template with these sections:

- **Chapter Metadata** (collapsible toggle):
  - Chapter Number
  - Chapter Title
  - Word Count Target
  - Completion Status
  - Related Chapters

- **Chapter Content**:
  - Outline/Structure
  - Main Content
  - Code Examples
  - Math Concepts
  - Basketball Applications
  - Exercises/Problems

- **Visual Assets**:
  - Diagram Prompts (for Glif)
  - Code Visualization Needs
  - Basketball Play Diagrams

- **Review Checklist**:
  - [ ] Content Complete
  - [ ] Code Examples Tested
  - [ ] Math Verified
  - [ ] Basketball Examples Accurate
  - [ ] Exercises Reviewed
  - [ ] Images Generated
  - [ ] Technical Review Complete
  - [ ] Educational Review Complete
  - [ ] Copy Edited
  - [ ] Ready for Final Review

3. Save as template: "Book Chapter Template"

### Step 3: Create Book Outline Structure

**Use the complete setup guide:** `/workflows/SETUP-BALLCODE-BOOK-NOTION.md`

This guide provides two options:
1. **Automated setup** using Notion MCP commands (fastest)
2. **Manual setup** with step-by-step instructions

The guide will create:

1. **Book Overview Page**:
   - Project timeline
   - Financial breakdown (link to `/workflows/ballcode-book-financial-breakdown.md`)
   - Target audience
   - Learning objectives
   - Table of contents with links to all chapters

2. **All Chapter Pages** (12 chapters + Appendices):
   - Chapter 1: Introduction to BallCODE
   - Chapter 2: Basketball as Logic - If/Then Statements
   - Chapter 3: Loops and Repetition - Defensive Rotations
   - Chapter 4: Pattern Recognition - Reading the Court
   - Chapter 5: Variables and Data - Player Stats
   - Chapter 6: Functions - Offensive Sets
   - Chapter 7: Arrays and Lists - Team Rosters
   - Chapter 8: Math Foundations - Shooting Percentages
   - Chapter 9: Algorithms - Play Execution
   - Chapter 10: Debugging - Analyzing Mistakes
   - Chapter 11: Advanced Concepts - Complex Plays
   - Chapter 12: Building Your First BallCODE Program
   - Appendices: Reference Guide, Exercise Solutions

3. **Daily Work Views**:
   - Current Work View (filtered by active chapters)
   - Progress View (grouped by completion %)
   - All Chapters View (complete overview)

4. **Template Structure**:
   - Each chapter includes: Outline, Content, Code Examples, Math Concepts, Basketball Applications, Exercises, Visual Assets, Review Checklist

All chapters are pre-structured and ready for daily work. Simply open any chapter from Notion and start writing.

### Step 4: Set Up Book Development Workflow

1. Create weekly sprints in Notion:
   - Week 1: Outline and planning
   - Week 2-4: Chapter 1-3 drafts
   - Week 5-7: Chapter 4-6 drafts
   - Continue weekly milestones

2. Use Status field to track progress:
   - Planning → Outline Complete → Chapter Draft → In Review → Edited → Final Review → Published

3. Set up Notion automation (if available):
   - When Status = "Chapter Draft", create task in review queue
   - When Completion % = 100, update Status to "In Review"

### Step 5: Integrate with Existing Workflow

1. Use same Notion integration for book database
2. Use Claude + MCP to:
   - Generate code examples
   - Create math explanations
   - Develop basketball analogies
   - Generate image prompts for diagrams

3. Use Glif MCP to generate:
   - Code syntax diagrams
   - Basketball play visualizations
   - Math concept illustrations
   - Flow charts for algorithms

4. Track book progress alongside blog posts in weekly reviews

### Step 6: Financial Tracking

1. Create "Budget & Expenses" page in Notion
2. Link to financial breakdown: `/workflows/ballcode-book-financial-breakdown.md`
3. Track actual expenses vs. budget:
   - Time spent (hours × rate)
   - External costs (editing, design, etc.)
   - Revenue from pre-sales/launch

4. Update monthly with progress reports

---

## Quick Start Checklist for Today

- [ ] Create Notion database with required properties
- [ ] Create and save blog post template
- [ ] Create first blog post (server build) as draft
- [ ] Create Notion integration and get API token
- [ ] Share database with integration
- [ ] Get database ID from URL
- [ ] Test manually creating a blog post entry

## Resources

- Notion Template: `/workflows/notion-blog-post-template.md`
- MCP Setup Guide: `/workflows/mcp-connection-guide.md`
- Complete Workflow Guide: `/workflows/blog-social-media-workflow-guide.md`
- BallCODE Book Financial Breakdown: `/workflows/ballcode-book-financial-breakdown.md`
- **BallCODE Book Notion Setup Guide:** `/workflows/SETUP-BALLCODE-BOOK-NOTION.md` ⭐ **START HERE for book setup**

---

## BallCODE Book Project Notes

Yes, you can push this plan to Notion to keep developing. The workflow supports:

1. **Tracking book development** in a dedicated Notion database
2. **Using same automation tools** (Claude + MCP, Glif) for content generation
3. **Managing chapters** with the same template-based approach as blog posts
4. **Financial tracking** integrated with the project timeline

The Notion database structure allows you to:
- Track chapter progress independently
- Generate code examples and diagrams using existing MCP tools
- Maintain consistency across all content (blog posts + book)
- Review and edit using the same workflow patterns

See Phase 7 above for complete setup instructions. 