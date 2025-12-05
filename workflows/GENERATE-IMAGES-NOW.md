# Generate Glif Images - Copy Each Command to Claude Desktop

Run these commands one at a time in Claude Desktop (with Docker MCP/Glif connected):

## Image 1: Hero Image
```
Use Glif MCP to generate an image with this prompt: sleek Mac computer on desk, glowing 'Always On' indicators, Docker container icons floating, clock showing 3:00 AM with 24/7 text overlay, network lines radiating, MCP server icons for Notion and Glif connected, dark professional tech background, blue and purple accent colors, modern clean design, text 'Always On. Always Learning.', professional tech illustration

After you get the image URL, download it and save it to: /Users/rashadwest/Sportstechwest/assets/images/blog-img/24-7-server-hero.png
```

## Image 2: Architecture Diagram
```
Use Glif MCP to generate an image with this prompt: technical architecture diagram, Mac computer at center labeled 'Local Server 24/7', Docker container wrapping services, three MCP server modules: Notion MCP purple for Content Automation, Glif MCP green for Image Generation, n8n workflows blue for Workflow Automation, clock icon with 24/7 and circular arrows, Always On indicators on components, flowing connection lines, subtle grid background, clean modern professional diagram style

After you get the image URL, download it and save it to: /Users/rashadwest/Sportstechwest/assets/images/blog-img/24-7-server-architecture.png
```

## Image 3: Automation Workflows
```
Use Glif MCP to generate an image with this prompt: infographic showing automation workflows, circular timeline around clock face 24 hours, different workflows: Blog Post Pipeline processing content, Email Automation analyzing drafting, Image Generation creating visuals, Social Media Scheduling posting content, each workflow as flowing process with checkpoints, 'While You Sleep' text overlay, Mac server icon center with Always On indicator, night dark blues purples transitioning to day lighter blues, modern clean professional radial circular layout

After you get the image URL, download it and save it to: /Users/rashadwest/Sportstechwest/assets/images/blog-img/24-7-automation-workflows.png
```

## Image 4: Comparison
```
Use Glif MCP to generate an image with this prompt: before and after comparison infographic, left side shows cloud services AWS Heroku with dollar signs and broken connections labeled 'Cloud-First Approach' in gray colors, right side shows Mac computer with Docker containers and glowing connections labeled 'Local-First 24/7' in blue purple colors, arrow between them showing transformation, clock showing 24/7, professional modern layout

After you get the image URL, download it and save it to: /Users/rashadwest/Sportstechwest/assets/images/blog-img/24-7-server-comparison.png
```

---

## After Generating All 4 Images

Once you have all 4 images downloaded and saved, run:

```bash
cd /Users/rashadwest/Sportstechwest
git add assets/images/blog-img/24-7-*.png
git commit -m "Replace placeholder images with Glif-generated images"
git push origin main
```

Then wait 2-5 minutes and check: https://sportstechwest.com/blog/Why-I-Built-a-Local-Server-to-Run-24-7/






