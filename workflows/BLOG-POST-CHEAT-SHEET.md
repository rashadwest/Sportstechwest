# Blog Post Creation Cheat Sheet

## 🎯 Quick Reference

### Required Fields (Minimum)
- ✅ **Title** - Your blog post headline
- ✅ **Category** - Insights / Tutorial / News
- ✅ **Tags** - 2-3 relevant tags
- ✅ **Content/Notes** - What you want to write about

### Optional but Recommended
- 📝 **Description** - SEO summary (150-160 chars) or let AI generate
- 📅 **Date** - YYYY-MM-DD in 2025, or leave blank for auto
- 🖼️ **Thumbnail** - Image description or let AI suggest
- 📱 **Social Media** - Let AI generate from content

---

## 📋 Quick-Fill Template

```json
{
  "title": "Your Title Here",
  "description": "",
  "tags": ["tag1", "tag2"],
  "category": "Insights",
  "notes": "Your content outline or draft here",
  "desiredDate": "",
  "images": [
    {
      "type": "thumbnail",
      "description": "What should the thumbnail show?",
      "prompt": ""
    }
  ]
}
```

---

## 🏷️ Available Tags

`automation`, `AI`, `basketball`, `server`, `docker`, `mcp`, `productivity`, `social-media`

Add new tags as needed.

---

## 📂 Categories

- **Insights** - Personal experiences, thoughts, learnings
- **Tutorial** - Step-by-step guides, how-tos  
- **News** - Updates, announcements, events

---

## 🚀 Workflow

1. **Fill template** → Copy `BLOG-POST-QUICK-FILL.json` and fill in
2. **Give to AI** → "Create a blog post from this specification"
3. **Review in Notion** → Edit if needed, set Status to "Ready to Publish"
4. **Glif automates** → Images generated, PR created
5. **Review PR** → Check formatting, merge when ready
6. **Live!** → Post appears at `sportstechwest.com/blogs`

---

## 📝 Content Tips

### What to Provide
- ✅ Outline with bullet points
- ✅ Key points you want to cover
- ✅ Rough draft
- ✅ Just notes and ideas

### What AI Generates
- ✅ Complete, well-formatted blog post
- ✅ Proper markdown structure
- ✅ Image prompts
- ✅ Social media excerpts
- ✅ SEO-optimized description

---

## 🖼️ Image Guidelines

### Thumbnail (Required)
- Main featured image
- Appears in blog listings
- Describe what it should show

### Content Images (Optional)
- 2-4 images work well
- Place after key sections
- Describe what each should show

**AI will:** Generate detailed prompts and place images correctly

---

## ⚙️ Settings (Defaults Usually Fine)

- **Badge Color:** `text-bg-primary` (default)
- **Trending:** `false` (default)
- **Simple Nav:** `true` (default)

---

## ✅ Validation (AI Handles This)

- ✅ No `<br>` tags
- ✅ Headers use `##` only
- ✅ Images wrapped in proper divs
- ✅ Date is 2025 and after latest post
- ✅ Front matter complete
- ✅ Tags/categories in brackets format

---

## 📚 Full Documentation

- **Quick Start:** `HOW-TO-CREATE-A-BLOG-POST.md`
- **Detailed Template:** `BLOG-POST-SPECIFICATION-TEMPLATE.md`
- **JSON Template:** `BLOG-POST-QUICK-FILL.json`
- **Technical Details:** `BLOG-PIPELINE-README.md`

---

## 💡 Example

```json
{
  "title": "Why I Built a Local Server",
  "description": "",
  "tags": ["server", "automation", "docker"],
  "category": "Insights",
  "notes": "I want to write about building a 24/7 server. Key points: 1) Why I built it, 2) What runs on it, 3) Why local matters",
  "desiredDate": "",
  "images": [
    {
      "type": "thumbnail",
      "description": "Hero image showing a 24/7 server setup",
      "prompt": ""
    }
  ]
}
```

**That's it!** AI handles the rest.




