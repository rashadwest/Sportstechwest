# Blog & Social Media Creation Workflow Guide

## Overview

This guide documents the complete workflow for creating blog posts and social media content using n8n, MCP (Docker), Glif, and Notion.

## Architecture

```
User/Claude → Notion (Draft) → Claude (MCP) → Glif (MCP) → Notion (Images) 
                                                              ↓
                                                      n8n (Trigger)
                                                              ↓
                    Jekyll (_posts/) ← n8n (Format) ← Notion (Ready to Publish)
                                                              ↓
                                          Social Media Platforms ← n8n (Generate Posts)
```

## Phase 1: Content Creation (MCP + Claude)

### Step 1: Create Blog Draft in Notion

1. Use the Notion blog post template (see `notion-blog-post-template.md`)
2. Fill in all front matter fields
3. Write blog content
4. Add image prompts in the designated section
5. Set status to "Draft Complete"

### Step 2: Generate Images via MCP

In Claude, use this workflow:

```
1. Read the blog post draft from Notion:
   "Use Notion MCP to read the blog post titled '[Post Title]'"

2. Extract image prompts:
   "Based on this blog content, create detailed image generation prompts for each image needed. Format as JSON with filename and prompt."

3. Generate images with Glif:
   For each prompt:
   "Use Glif MCP to generate an image with this prompt: [prompt]"
   
4. Store image URLs in Notion:
   "Use Notion MCP to update the blog post with these image URLs: [list of URLs]"
```

### Step 3: Optimize and Review

1. Download generated images from Glif
2. Optimize images (compress, resize if needed)
3. Upload to `/assets/images/blog-img/` manually or via n8n
4. Update Notion with local image paths
5. Review entire post

## Phase 2: Publishing (n8n)

### Step 1: Mark as Ready

1. In Notion, set status to "Ready to Publish"
2. Ensure all images are uploaded and paths are correct
3. Review front matter one final time

### Step 2: n8n Workflow Triggers

The n8n workflow (see `n8n-blog-publishing-workflow.json`) will:

1. **Watch Notion** - Detects status change to "Ready to Publish"
2. **Get Full Content** - Retrieves complete page with images
3. **Format Markdown** - Converts Notion content to Jekyll markdown
4. **Write File** - Creates `.md` file in `_posts/` directory
5. **Update Notion** - Sets status to "Published"

### Step 3: Manual Verification

1. Check generated markdown file in `_posts/`
2. Verify front matter is correct
3. Check image paths
4. Test locally with Jekyll: `bundle exec jekyll serve`

## Phase 3: Social Media (n8n)

### Automated Social Post Generation

After blog is published, n8n workflow generates:

1. **Extract Key Points** - Pulls main insights/quotes from blog
2. **Generate Posts** - Creates platform-specific content:
   - Twitter/X: 280 characters, includes link
   - LinkedIn: 3000 characters, professional tone
   - Instagram: 2200 characters with hashtags
3. **Approval Step** - User reviews before posting
4. **Schedule or Post** - Publishes immediately or schedules

### Manual Social Creation

Use the social media excerpts from Notion template to manually create posts with:
- Key quotes
- Visual preview of blog thumbnail
- Link to blog post
- Relevant hashtags

## Workflow Best Practices

### Content Creation

- ✅ Write blog post first, then generate images (ensures images match content)
- ✅ Use descriptive image prompts with style guidance
- ✅ Generate multiple image variations for key visuals
- ✅ Review and approve all images before marking ready

### Publishing

- ✅ Test markdown locally before pushing to production
- ✅ Verify all image paths are correct
- ✅ Check front matter formatting (especially date and tags)
- ✅ Ensure SEO description is within 150-160 characters

### Social Media

- ✅ Extract 2-3 key insights for social posts
- ✅ Create platform-specific content (don't cross-post verbatim)
- ✅ Include call-to-action to read full post
- ✅ Use relevant hashtags (3-5 max on Twitter, more on Instagram)

## Troubleshooting

### MCP Connection Issues

- See `mcp-connection-guide.md` for setup and troubleshooting
- Verify Docker containers are running
- Check API keys are set correctly

### n8n Workflow Issues

- Check Notion integration permissions
- Verify database ID is correct
- Test workflow manually before automating
- Check n8n logs for errors

### Image Generation Issues

- Ensure Glif API key is valid
- Check image prompts are detailed enough
- Verify image formats (PNG/WebP recommended)
- Optimize large images before uploading

## Future Enhancements

- [ ] Automated image optimization in n8n workflow
- [ ] Scheduled social media posting
- [ ] A/B testing for social post variations
- [ ] Analytics integration to track blog performance
- [ ] Auto-generate meta descriptions from content


