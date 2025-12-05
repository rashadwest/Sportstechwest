# How to Create a Blog Post: Complete Guide

This guide explains how to use the blog post specification templates to create content. Fill out the template, and AI will handle all the technical details.

---

## 🚀 Quick Start

### Option 1: Use the Quick-Fill JSON Template
1. Copy `workflows/BLOG-POST-QUICK-FILL.json`
2. Fill in the fields
3. Save as `.cursor/drafts/YYYY-MM-DD-slug.json`
4. Give it to AI with: "Create a blog post from this specification"

### Option 2: Use the Detailed Markdown Template
1. Open `workflows/BLOG-POST-SPECIFICATION-TEMPLATE.md`
2. Fill out all relevant sections
3. Give it to AI with: "Create a blog post from this specification"

---

## 📋 Understanding Each Field

### Basic Information

#### Title
- **What it is:** The main headline of your blog post
- **Example:** "Why I Built a Local Server to Run 24/7"
- **Tips:** Make it clear, engaging, and include keywords people might search for

#### Description (SEO)
- **What it is:** A 150-160 character summary that appears in search results
- **Example:** "Why I decided to build my own always-on infrastructure for automation, AI workflows, and continuous learning."
- **Tips:** Include your main keywords, make it compelling, stay within character limit

#### Desired Publication Date
- **What it is:** When you want the post to be published
- **Format:** `YYYY-MM-DD` (e.g., `2025-10-29`)
- **Rules:** 
  - Must be in 2025
  - Must be after your latest published post
  - Leave blank to auto-assign next available date

---

### Categorization

#### Category
- **What it is:** The type of content you're creating
- **Options:**
  - **Insights:** Personal experiences, thoughts, learnings
  - **Tutorial:** Step-by-step guides, how-tos
  - **News:** Updates, announcements, current events
- **Example:** For a post about building a server, use "Insights"

#### Tags
- **What it is:** Keywords that help organize and find your content
- **Available tags:** `automation`, `AI`, `basketball`, `server`, `docker`, `mcp`, `productivity`, `social-media`
- **Tips:** 
  - Use 3-7 relevant tags
  - You can add new tags if needed
  - Think about what someone would search for

---

### Content

#### Main Content / Notes
- **What it is:** Your initial thoughts, outline, or draft
- **You can provide:**
  - A rough outline with bullet points
  - Key points you want to cover
  - A full draft
  - Just notes and ideas
- **AI will:** Expand this into a complete, well-formatted blog post
- **Example:**
  ```
  I want to write about building a 24/7 server. Key points:
  - Why I built it (automation, always-on)
  - What I wanted to fix (downtime, manual work)
  - What runs on it (Docker, MCP servers, n8n)
  - Why local matters (privacy, control, cost)
  - How it works (Docker containers, auto-start)
  - What this changes (freedom, focus, leverage)
  ```

#### Key Points to Cover
- **What it is:** A list of main sections or topics
- **Purpose:** Helps AI structure the post logically
- **Example:**
  1. Why I built it
  2. What I wanted to fix
  3. What runs 24/7
  4. Why local matters
  5. How it works
  6. What this changes

---

### Images

#### Thumbnail Image
- **What it is:** The main featured image that appears in blog listings
- **Required:** Yes
- **Location:** `/assets/images/blog-img/`
- **Format:** PNG or JPG
- **What to provide:**
  - **Description:** What should the image show?
  - **Prompt:** Detailed description for AI image generation
  - **Filename:** Leave blank to auto-generate from slug

#### Additional Images
- **What it is:** Images that appear within the blog post content
- **Required:** No, but recommended (2-4 images work well)
- **For each image, provide:**
  - **Location:** Where in the post it should appear (e.g., "After 'Why local matters' section")
  - **Description:** What should this image show?
  - **Prompt:** Detailed image generation prompt for Glif/Claude
  - **Filename:** Leave blank to auto-generate

---

### Social Media

#### Twitter/X Excerpt
- **What it is:** A 280-character quote or insight for Twitter
- **Required:** No (AI can generate from content)
- **Tips:** Should be punchy, quotable, or share a key insight

#### LinkedIn Excerpt
- **What it is:** A longer excerpt (up to 3000 characters) for LinkedIn
- **Required:** No (AI can generate from content)
- **Tips:** More professional tone, can include context

#### Instagram Excerpt
- **What it is:** An engaging excerpt (up to 2200 characters) with hashtags
- **Required:** No (AI can generate from content)
- **Tips:** More visual/engaging language, include relevant hashtags

---

### Advanced Settings

#### Badge Color
- **What it is:** Visual styling for the post badge
- **Options:**
  - `text-bg-primary` (default, blue)
  - `text-bg-success` (green)
  - `text-bg-info` (light blue)
  - `text-bg-warning` (yellow/orange)
  - `text-bg-danger` (red)
- **Default:** `text-bg-primary`

#### Trending
- **What it is:** Whether to mark the post as trending
- **Options:** Yes / No
- **Default:** No
- **Use when:** Post is particularly timely or important

#### Simple Navigation
- **What it is:** Whether to use simplified navigation
- **Options:** Yes / No
- **Default:** Yes
- **Usually:** Leave as Yes

---

## 🎯 Step-by-Step Workflow

### Step 1: Fill Out the Template
Choose one:
- **Quick:** Copy `BLOG-POST-QUICK-FILL.json` and fill in fields
- **Detailed:** Use `BLOG-POST-SPECIFICATION-TEMPLATE.md` for more guidance

### Step 2: Give to AI
Say: "Create a blog post from this specification" and provide the filled template.

AI will:
1. Generate complete blog content
2. Format everything correctly
3. Create Notion database entry
4. Generate image prompts
5. Create social media excerpts

### Step 3: Review in Notion
- Content appears in your "Blog Posts" Notion database
- Review and edit if needed
- Set Status to "Draft Complete" when ready

### Step 4: Generate Images
- Set Status to "Images Generated" (or let Glif handle it)
- Images are created and placed in `/assets/images/blog-img/`

### Step 5: Publish
- Set Status to "Ready to Publish"
- Glif automation:
  - Creates GitHub PR
  - Validates formatting
  - Generates final Jekyll markdown

### Step 6: Review PR
- Check formatting, images, content
- Make any final edits
- Merge when ready

### Step 7: Live!
- Post appears at `sportstechwest.com/blogs` in 2-5 minutes
- Status updates to "Published" in Notion

---

## 📝 Formatting Rules (AI Handles This)

You don't need to worry about these, but here's what AI ensures:

### Content Structure
- ✅ Headers use `##` only (never `###`)
- ✅ Paragraphs separated with blank lines (no `<br>` tags)
- ✅ Section breaks use `---` on its own line
- ✅ Lists use standard markdown
- ✅ Bold/italic use markdown syntax

### Images
- ✅ All images wrapped in proper HTML div structure
- ✅ Images placed in `/assets/images/blog-img/`
- ✅ Alt text included for accessibility

### Front Matter
- ✅ All required fields present
- ✅ Date validated (2025, after latest post)
- ✅ Tags/categories in correct format
- ✅ Thumbnail path matches actual file

---

## 💡 Examples

### Minimal Example (Just the Essentials)
```json
{
  "title": "My New Blog Post",
  "description": "A brief description of what this post is about",
  "tags": ["tag1", "tag2"],
  "category": "Insights",
  "notes": "I want to write about X. Key points: 1) Point A, 2) Point B, 3) Point C"
}
```

### Complete Example
See `BLOG-POST-QUICK-FILL.json` for a full example with all fields.

---

## ❓ Common Questions

### Q: Do I need to fill out every field?
**A:** No! Only fill out what's relevant. AI can generate:
- Descriptions (if you provide good notes)
- Social media excerpts (from your content)
- Image prompts (from descriptions)
- Dates (next available date)

### Q: What if I don't know what images I want?
**A:** Just describe what the post is about, and AI can suggest relevant images and generate prompts.

### Q: Can I change things after AI generates?
**A:** Yes! You can edit in Notion, or ask AI to revise specific sections.

### Q: What if my date conflicts with an existing post?
**A:** AI will automatically suggest the next available date.

### Q: How do I know what tags to use?
**A:** Think about what someone would search for. Common tags: `automation`, `AI`, `server`, `docker`, `mcp`, `productivity`. You can add new ones.

---

## 🎨 Template Files

- **`BLOG-POST-SPECIFICATION-TEMPLATE.md`** - Detailed markdown template with explanations
- **`BLOG-POST-QUICK-FILL.json`** - Quick JSON template for programmatic use
- **`BLOG-PIPELINE-README.md`** - Technical pipeline documentation
- **`NOTION-CLAUDE-PROMPT.md`** - AI prompts (for reference)

---

## ✅ Checklist Before Submitting

- [ ] Title is clear and engaging
- [ ] Description is 150-160 characters (or let AI generate)
- [ ] Category selected (Insights, Tutorial, or News)
- [ ] At least 2-3 tags added
- [ ] Content/notes provided (even if just an outline)
- [ ] Thumbnail image description provided
- [ ] Desired date is in 2025 (or leave blank)

That's it! AI handles the rest.

---

**Remember:** The goal is to express your ideas clearly. AI will handle all the technical formatting, structure, and generation. Just focus on what you want to say!




