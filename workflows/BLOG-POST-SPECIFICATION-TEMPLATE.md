# Blog Post Specification Template

Fill out this template to create a complete blog post. AI will use this to generate all necessary content, formatting, and metadata.

---

## 📋 Basic Information

### Title
**Your blog post title here**
- Should be clear, engaging, and SEO-friendly
- Example: "Why I Built a Local Server to Run 24/7"

### Description (SEO)
**150-160 character description for search engines**
- Should summarize the post and include key terms
- Example: "Why I decided to build my own always-on infrastructure for automation, AI workflows, and continuous learning."

### Desired Publication Date
**YYYY-MM-DD** (must be in 2025 and after your latest post)
- Leave blank to auto-assign next available date
- Format: `2025-10-29`

---

## 🏷️ Categorization

### Category
**Select one:**
- [ ] Insights
- [ ] Tutorial
- [ ] News

### Tags
**List relevant tags (comma-separated):**
- Available tags: `automation`, `AI`, `basketball`, `server`, `docker`, `mcp`, `productivity`, `social-media`
- You can add new tags if needed
- Example: `server, automation, docker, mcp`

---

## ✍️ Content

### Main Content / Notes
**Your initial thoughts, outline, or draft content:**
```
[Write your blog post content here. This can be:
- A rough outline with bullet points
- Key points you want to cover
- A full draft
- Just notes and ideas

AI will expand this into a complete, well-formatted blog post.]
```

### Key Points to Cover
**List the main sections or topics:**
1. [Section 1 topic]
2. [Section 2 topic]
3. [Section 3 topic]
4. [Add more as needed]

---

## 🖼️ Images

### Thumbnail Image
**Main featured image for the blog post:**
- **Description:** [What should the thumbnail show?]
- **Prompt for AI image generation:** [Detailed description for Glif/Claude to generate]
- **Filename:** [Leave blank to auto-generate from slug]

### Additional Images
**List any images you want in the post:**

#### Image 1
- **Location in post:** After "[Section Name]"
- **Description:** [What should this image show?]
- **Prompt:** [Detailed image generation prompt]
- **Filename:** [Leave blank to auto-generate]

#### Image 2
- **Location in post:** After "[Section Name]"
- **Description:** [What should this image show?]
- **Prompt:** [Detailed image generation prompt]
- **Filename:** [Leave blank to auto-generate]

[Add more images as needed]

---

## 📱 Social Media

### Twitter/X Excerpt (280 characters)
**Key quote or insight for Twitter:**
```
[Leave blank for AI to generate based on content]
```

### LinkedIn Excerpt (3000 characters)
**Longer excerpt or summary for LinkedIn:**
```
[Leave blank for AI to generate based on content]
```

### Instagram Excerpt (2200 characters)
**Engaging excerpt with relevant hashtags:**
```
[Leave blank for AI to generate based on content]
```

---

## ⚙️ Advanced Settings

### Badge Color
**Select badge color for the post:**
- [ ] `text-bg-primary` (default)
- [ ] `text-bg-success`
- [ ] `text-bg-info`
- [ ] `text-bg-warning`
- [ ] `text-bg-danger`

### Trending
**Should this post be marked as trending?**
- [ ] Yes
- [ ] No (default)

### Simple Navigation
**Use simple navigation for this post?**
- [x] Yes (default)
- [ ] No

---

## 📝 Formatting Rules (For AI Reference)

### Content Structure
- **Headers:** Use `##` for section headers ONLY (never `###`)
- **Paragraphs:** Separate with blank lines only (NO `<br>` tags)
- **Section Breaks:** Use `---` on its own line between major sections
- **Lists:** Use standard markdown lists
- **Bold/Italic:** Use markdown syntax (`**bold**`, `*italic*`)

### Images
All images must be wrapped in this HTML structure:
```html
<div class="text-center my-4">
  <img src="/assets/images/blog-img/filename.png" alt="Description" class="img-fluid">
</div>
```

### Front Matter Format
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

---

## 🔄 Workflow Status

### Current Status
- [ ] Draft (Initial creation)
- [ ] Draft Complete (Content written)
- [ ] Images Generated (Images created)
- [ ] Images Optimized (Images processed)
- [ ] Ready to Publish (Triggers Glif automation)
- [ ] In Review (PR created, reviewing)
- [ ] Published (Live on blog)
- [ ] Social Media Scheduled (Social posts created)

---

## 📤 What Happens Next

1. **You fill out this template** → Save as `.cursor/drafts/YYYY-MM-DD-slug.json` or use directly
2. **AI processes the template** → Generates:
   - Complete blog content with proper formatting
   - Notion database entry
   - Jekyll markdown file with front matter
   - Image generation prompts
   - Social media excerpts
3. **Content goes to Notion** → Stored in "Blog Posts" database
4. **When Status = "Ready to Publish"** → Glif automation:
   - Generates images
   - Creates GitHub PR
   - Validates formatting
5. **You review PR** → Check formatting, images, content
6. **Merge PR** → Auto-deploys to blog at `sportstechwest.com/blogs`

---

## ✅ Validation Checklist (For AI)

Before finalizing, ensure:
- [ ] Title is clear and engaging
- [ ] Description is 150-160 characters
- [ ] Date is in 2025 and after latest post
- [ ] Tags are valid (from approved list or new ones)
- [ ] Category is one of: Insights, Tutorial, News
- [ ] Content has no `<br>` tags
- [ ] Headers use `##` only (no `###`)
- [ ] Images are wrapped in proper div structure
- [ ] Front matter has all required fields
- [ ] Thumbnail path matches actual image filename
- [ ] Social media excerpts are appropriate length

---

## 💡 Example: Filled Out Template

### Basic Information
- **Title:** "Why I Built a Local Server to Run 24/7"
- **Description:** "Why I decided to build my own always-on infrastructure for automation, AI workflows, and continuous learning."
- **Desired Date:** 2025-10-29

### Categorization
- **Category:** Insights
- **Tags:** server, automation, docker, mcp

### Content
- **Main Content:** "I wanted to build a system that keeps working even when I'm not. The goal was simple: automate the repetitive parts of my day..."
- **Key Points:** 
  1. Why I built it
  2. What I wanted to fix
  3. What runs 24/7
  4. Why local matters
  5. How it works
  6. What this changes

### Images
- **Thumbnail:** Hero image showing a 24/7 server setup
- **Image 1:** Architecture diagram after "What runs 24/7" section
- **Image 2:** Before/after comparison after "Why local matters" section

---

**Fill out this template, and AI will handle all the technical details, formatting, and generation!**




