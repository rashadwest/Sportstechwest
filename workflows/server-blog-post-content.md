# Server Blog Post - Ready for Notion

## Front Matter (Jekyll)
---
layout: post
title: "How I Built My Own MCP Server: Docker, Notion, and Glif"
description: "A complete guide to building your own Model Context Protocol server using Docker, integrating Notion and Glif for automated workflows"
thumbnail: "/assets/images/blog-img/mcp-server-architecture.png"
badge_color: "text-bg-primary"
trending: true
simple_nav: true
date: 2025-11-06
tags: [server, docker, mcp, automation]
categories: [Insights]
author: "Rashad West"
---

## Blog Content

## Why I built my own server

Most developers rely on SaaS solutions. Zapier, Make, IFTTT. They work, but they're black boxes. You can't see inside them. You can't modify them. You can't learn from them.

I wanted something different. A server I could control. A system I could understand. A platform I could teach.

So I built my own MCP server. Not because it was easier, but because it was educational. Every line of code, every configuration, every connection taught me something new about how modern AI systems work.

For me, this isn't just infrastructure. It's a learning platform. Each component Docker, Notion, Glif becomes a building block for understanding how intelligence flows through a system.

---

## What is MCP? (The quick version)

MCP stands for Model Context Protocol. It's like a universal translator between AI assistants (like Claude) and external services (like Notion, Glif, n8n).

Think of it like this:
- Without MCP: Claude can only talk to you.
- With MCP: Claude can talk to your entire tech stack.

Instead of Claude just suggesting "Maybe you should update that Notion page," it can actually do it. Instead of saying "You could generate an image," it can generate one right now.

That's the power. AI that doesn't just advise, but acts.

---

## The architecture (what I actually built)

My setup connects three main pieces:

**1. Docker Gateway**
- Runs MCP servers as containers
- Isolates each service
- Easy to start, stop, and update
- No global installs cluttering my system

**2. Notion MCP Server**
- Lets Claude read and write to my Notion workspace
- Automates blog post creation
- Manages content pipeline
- Queries databases, creates pages, updates properties

**3. Glif MCP Server**
- Generates images from text prompts
- Creates visuals for blog posts
- Runs locally via Docker
- No external API dependencies

All of this runs on my Mac. Everything is local. Everything is private. Everything is mine.

<div class="text-center my-4">
  <img src="/assets/images/blog-img/mcp-server-architecture.png" alt="MCP server architecture diagram showing Docker, Notion, and Glif connections">
</div>

---

## The setup process (step by step)

### Step 1: Docker configuration

I needed Docker Desktop running first. This was straightforward:

```bash
# Check Docker is running
docker ps

# If not, start Docker Desktop
open -a Docker
```

The key insight here: Docker becomes my abstraction layer. I don't install packages globally. I run everything in containers. Clean. Isolated. Predictable.

### Step 2: API keys and integrations

**Notion:**
1. Went to notion.so/my-integrations
2. Created new integration
3. Copied the API token (starts with `secret_`)
4. Shared my databases with the integration

**Glif:**
1. Signed in to glif.app
2. Found API key in settings
3. Copied it

These keys are secrets. They never go in code. They go in environment variables. They stay private.

### Step 3: Config files (where the magic happens)

I configured two files:

**Cursor config** (`~/.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"]
    },
    "Notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "your-notion-key-here"
      }
    },
    "Glif": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-glif"],
      "env": {
        "GLIF_API_KEY": "your-glif-key-here"
      }
    }
  }
}
```

**Claude Desktop config** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
Similar structure, plus my n8n MCP server connection.

The critical detail: I had to fully quit and restart both applications. Not just close the window. Fully quit. This was the source of half my initial debugging headaches.

<div class="text-center my-4">
  <img src="/assets/images/blog-img/mcp-config-files.png" alt="Screenshot showing MCP configuration files structure">
</div>

---

## The breakthrough moment

When it worked, it was magical. Not because it was easy, but because I understood every piece.

I could say to Claude: "Create a new blog post in my Notion database about building MCP servers."

And it would:
1. Query my Notion database structure
2. Create a new page with proper front matter
3. Format content correctly
4. Set status to "Draft"
5. Report back: "Done. Created page with ID..."

Before MCP, I would get a 20-step checklist. Now, Claude just does it. One command. Seconds. Done.

The same with images. "Generate a hero image for this blog post." Claude calls Glif MCP, gets the image URL, embeds it in the Notion page. All without me touching a UI.

---

## Real use cases (what I'm doing with it)

**1. Blog post automation**
- Claude drafts posts in Notion
- Generates images via Glif
- Formats everything correctly
- Updates status when ready

**2. Content pipeline management**
- Tracks posts through stages (Draft → Ready → Published)
- Generates social media excerpts
- Manages image assets
- All automated, all visible

**3. Knowledge management**
- Claude reads my Notion databases
- Summarizes content
- Creates connections between pages
- Answers questions about my own notes

**4. Image generation workflow**
- Prompts created from blog content
- Images generated automatically
- URLs stored in Notion
- Optimized and uploaded locally

Each use case teaches me something new about how AI can interact with my workflow. It's not just automation. It's AI-assisted thinking.

---

## Lessons learned (the hard way)

**1. Restart everything**
Config changes require full application restarts. Not window closes. Full quits. This tripped me up more than once.

**2. API keys are environment variables**
Never hardcode secrets. Always use env variables. This is security 101, but it's easy to skip when you're moving fast.

**3. Docker isolation is powerful**
Running services in containers means I can experiment without breaking my system. Try something new? Spin up a container. Break it? Delete it. Start over.

**4. MCP is a learning platform**
Every tool I add teaches me something new. Every connection reveals another pattern. It's not just about automation. It's about understanding how systems communicate.

**5. Local-first matters**
Everything runs on my machine. No external dependencies. No cloud services watching. Just my code, my data, my control.

---

## The technical stack (plain English)

- **Docker**: Container platform. Runs services in isolation.
- **MCP (Model Context Protocol)**: Communication standard between AI and services.
- **Notion MCP Server**: Bridge between Claude and Notion API.
- **Glif MCP Server**: Bridge between Claude and Glif image generation.
- **Claude/Cursor**: AI assistants that use MCP to connect to everything.

Together, they form a local AI automation platform. No vendor lock-in. Full control. Complete understanding.

---

## Why this approach works

**Privacy**: Everything runs locally. Your data stays yours.

**Control**: You own the stack. Modify it. Extend it. Understand it.

**Learning**: Each component teaches you something. Docker teaches containerization. MCP teaches protocol design. Notion API teaches data modeling.

**Scalability**: Start simple. Add tools as needed. Each new MCP server opens new possibilities.

**Cost**: No monthly SaaS fees. Just your time and understanding.

---

## What's next

- **More MCP servers**: GitHub, Linear, Slack, Twitter
- **Custom workflows**: Blog post automation end-to-end
- **Social media automation**: Generate and schedule posts
- **Analytics integration**: Track content performance
- **Multi-agent coordination**: Multiple AI assistants working together

The platform is built. Now I can add capabilities as I need them. Each new server teaches me something new. Each new workflow reveals another pattern.

---

## The bottom line

Building your own MCP server isn't about being clever. It's about understanding how modern AI systems work.

You don't need to build everything yourself. But understanding the architecture, seeing how components connect, knowing how data flows this changes how you think about AI.

For me, this server isn't just infrastructure. It's a laboratory. Every experiment teaches me something. Every connection reveals another pattern. Every workflow shows me how AI can augment human creativity.

The future of AI isn't in the cloud. It's on your machine. It's in your control. It's yours to build, understand, and extend.

Start simple. Learn by doing. Build something that matters to you.

That's what I did. And this server is just the beginning.

---

## Image Prompts

### Image 1: MCP Server Architecture Diagram
**Location:** After "The architecture (what I actually built)" section
**Filename:** `mcp-server-architecture.png`
**Target path:** `/assets/images/blog-img/mcp-server-architecture.png`

**Prompt:**
```
Create a technical architecture diagram showing three connected components:

1. Docker Gateway (left side) - shown as a container/box labeled "Docker Gateway" with "MCP Servers" text inside
2. Notion MCP Server (center-top) - box labeled "Notion MCP" with "API Bridge" text
3. Glif MCP Server (center-bottom) - box labeled "Glif MCP" with "Image Generation" text
4. Claude/Cursor (right side) - shown as an AI brain icon or Claude logo connected to all three

Use arrows showing bidirectional communication between components. Style: clean, technical, modern. Color scheme: blue tones for Docker, purple for Notion, green for Glif, orange for Claude. White background. Professional diagram style.
```

### Image 2: MCP Configuration Files Screenshot
**Location:** After "The setup process (step by step)" section
**Filename:** `mcp-config-files.png`
**Target path:** `/assets/images/blog-img/mcp-config-files.png`

**Prompt:**
```
Create a visual representation of MCP configuration files. Show two side-by-side code editor windows:

Left window: Title "~/.cursor/mcp.json" showing JSON configuration with:
- MCP_DOCKER section
- Notion section with NOTION_API_KEY environment variable (value partially hidden with asterisks)
- Glif section with GLIF_API_KEY environment variable (value partially hidden)

Right window: Title "Claude Desktop Config" showing similar structure plus n8n-mac server

Style: Modern code editor (VS Code or Cursor style). Dark theme. Syntax highlighting for JSON. Clean, professional look. Show file paths at the top of each window.
```

### Image 3: Before and After MCP Comparison
**Location:** After "The breakthrough moment" section
**Filename:** `mcp-before-after.png`
**Target path:** `/assets/images/blog-img/mcp-before-after.png`

**Prompt:**
```
Create a before and after comparison visual:

Left side (Before MCP):
- Show Claude AI icon with a speech bubble saying "Here's a 20-step checklist to create a Notion page..."
- Below: Long list of manual steps (numbered 1-20) in gray/light colors
- Label: "Manual Process"

Right side (After MCP):
- Show Claude AI icon directly connected to Notion and Glif icons
- Speech bubble: "Done. Created page with ID..."
- Below: Simple arrow flow diagram showing automated process
- Label: "MCP Automation"

Style: Clean, modern comparison layout. Use color to distinguish (gray for before, green/blue for after). Professional infographic style.
```

---

## Social Media Excerpts

### Twitter/X (280 chars)
```
Built my own MCP server with Docker, Notion, and Glif. Now Claude can actually DO things instead of just suggesting them. Local-first. Private. Mine.

🧠 Understanding AI isn't about using tools. It's about building them.

#AI #Docker #MCP #Automation
```

### LinkedIn (3000 chars)
```
I built my own Model Context Protocol (MCP) server. Here's why it changed everything:

Most developers rely on SaaS automation tools. Zapier, Make, IFTTT. They work, but they're black boxes. You can't see inside them. You can't modify them. You can't learn from them.

So I built something different: a local MCP server running Docker, connecting Claude AI to Notion and Glif. Not because it was easier, but because it was educational.

The Result:
• Claude can now CREATE blog posts in Notion (not just suggest how)
• Generate images via Glif automatically
• Manage my entire content pipeline
• All running locally on my machine

Why this matters:
Every line of code taught me something new about how modern AI systems work. Every configuration revealed another pattern. Every connection showed me how intelligence flows through a system.

This isn't just infrastructure. It's a learning platform.

The future of AI isn't in the cloud. It's on your machine. It's in your control. It's yours to build, understand, and extend.

#AI #Docker #MCP #Automation #TechInnovation #LocalFirst
```

### Instagram (2200 chars)
```
I built my own MCP server and here's what I learned 🧠

Most automation tools are black boxes. You can't see inside them. You can't modify them. You can't learn from them.

So I built my own:
• Docker Gateway running locally
• Notion MCP Server for content automation
• Glif MCP Server for image generation
• All connected to Claude AI

The breakthrough?
Instead of Claude suggesting "Maybe you should update that Notion page," it actually does it.

One command. Seconds. Done.

Why this matters:
This isn't just about automation. It's about understanding how modern AI systems work. Each component teaches you something. Each connection reveals another pattern.

The future of AI isn't in the cloud.
It's on your machine.
It's in your control.
It's yours to build.

#AIAutomation #Docker #MCP #TechInnovation #LocalFirst #DeveloperLife #AITools #Automation #TechBlog #Innovation
```

