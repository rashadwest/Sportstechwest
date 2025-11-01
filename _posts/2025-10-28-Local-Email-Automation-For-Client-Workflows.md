---
layout: post
title: "Local Email Automation: From Inbox to Action for Client Workflows"
description: "How I built a private, in-house email automation system to streamline client ops and help friends and colleagues automate theirs."
thumbnail: "/assets/images/blog-img/n8n-title-page.png"
badge_color: "text-bg-primary"
trending: true
simple_nav: true
date: 2025-10-28
tags: [automation, email, workflows, local, productivity]
categories: [Insights]
author: "Rashad West"
---

## How I built an AI assistant that handles my emails (but still asks permission)

Imagine having a really smart intern who reads your emails, drafts thoughtful replies, and then asks, “Do you want me to send this?”  
That's what I'm building, except the "intern" is AI, and it runs on my own computer.  

For me, this isn't just about automation. It's about *understanding* how AI thinks, how it learns patterns, and how I can use that understanding to build systems that think *with* me, not *for* me.  

---

## Why this matters for sports and innovation

In sports business, the inbox never sleeps:

- Partnership inquiries  
- Media requests  
- Sponsor communications  
- Fan engagement  
- Event coordination  

Most replies follow patterns, but every message still needs a human touch. My system handles the pattern work automatically and keeps me firmly in control.  

That control is key. Every time I teach AI to handle one more layer of work, I learn more about how intelligence can be trained, not just to save time, but to scale creativity. This same understanding powers how I'm building **BallCode**, my AI sports language that turns movement into logic and creativity into code.  

---

## The workflow

1. An email hits my inbox.  
2. AI reads it and figures out the intent.  
3. AI drafts a response in my voice.  
4. AI sends the draft to me: “Should I send this?”  
5. I approve, edit, or reject.  
6. Only then does it actually send.  

The key: I'm still the decision-maker. The AI is just really fast at drafting.  
It's not replacing my judgment. It's giving me space to think more deeply and respond more strategically.  

*Note: I tested this system extensively on my personal email before deploying it to my main inbox. Safety first, especially with automation.*  

<div class="text-center my-4">
  <img src="/assets/images/blog-img/n8n-email-workflow.png" alt="n8n email automation workflow">
</div>

---

## The tech setup (plain English)

- **n8n:** Like Zapier or IFTTT, but I own it. It’s open-source and runs locally on my Mac. It connects apps and automates workflows.  
- **Claude AI:** The “brain” that reads emails and writes responses. Advanced, reliable, and adaptable.  
- **MCP connection:** The new bridge that lets Claude not just suggest changes, but actually *make* the changes to my automations.  

The setup isn't just technical. It's educational. Each step is teaching me how modern AI systems think, how they interpret context, and how they can safely take action on my behalf.  

<div class="text-center my-4">
  <img src="/assets/images/blog-img/claude-mcp-n8n-setup.png" alt="Claude AI, MCP, and n8n architecture diagram">
</div>

---

## The messy middle: what I had to figure out

Early on, building and fixing automations felt like assembling LEGO while wearing mittens. Whenever something broke, I had to:

- Click through menus  
- Find the right setting  
- Make a change  
- Test it  
- Repeat  

It was slow. Really slow.  
But that struggle is part of the process. Each mistake helped me understand not just the tool, but the logic behind how AI sees a task, breaks it down, and learns to fix it.  

---

## The breakthrough: MCP as the bridge

I connected Claude to my local automation using MCP (Model Context Protocol). Now Claude can:

- See what’s broken  
- Fix it automatically  
- Test that it works  
- Report back: “Done.”  

Before: "Hey Claude, my email workflow is broken." I get a 10-step checklist.  
After: Same message. Claude fixes it in seconds and shows me exactly what changed.  

That's when I realized this isn't just about automating a process. It's about *teaching AI how to maintain and improve itself* while I stay in the driver's seat.  

<div class="text-center my-4">
  <img src="/assets/images/blog-img/n8n-mcp-breakthrough.png" alt="Before and after: MCP breakthrough showing slow manual fixes vs fast AI-powered automation">
</div>

---

## Setup process (what I actually did)

1. Generated an API key: Basically a backstage pass for Claude to talk to my automation.  
2. Built a small bridge program: A translator so Claude and n8n speak the same language.  
3. Configured Claude: Pointed it to my local system, added the API key, and connection details.  
4. Restarted everything: Fully quit and reopen. Don't just close windows. It matters.  

Each line of code was like building a muscle. I wasn't just setting up automation, I was *learning how intelligence moves through a system.*  

<div class="text-center my-4">
  <img src="/assets/images/blog-img/gmail-approval-1.png" alt="Gmail approval email interface showing AI draft and approval options">
</div>

<div class="text-center my-4">
  <img src="/assets/images/blog-img/gmail-approval-2.png" alt="Gmail approval step showing workflow in action">
</div>

---

## Real use cases I’m running

1. **Partnership responses**  
   - Incoming: “Interested in exploring a partnership?”  
   - AI draft: Professional, curious, requests key details  
   - Me: Approve or personalize based on the sender  

2. **Media requests**  
   - Incoming: “Can we interview you about [topic]?”  
   - AI draft: Checks my calendar, proposes times, keeps the tone on-brand  
   - Me: Approve or decline based on the outlet and topic  

3. **Fan engagement**  
   - Incoming: General questions, feedback, shout-outs  
   - AI draft: Friendly, aligned with our voice  
   - Me: Quick review and send  

4. **Event coordination**  
   - Incoming: Venue, logistics, timing  
   - AI draft: Pulls in our standard policies and preferences  
   - Me: Approve routine stuff; I handle exceptions  

Every one of these cases teaches me something about language, tone, and intent. All lessons I can apply to future AI projects.  

---

## Why I built it this way

- **Privacy:** Everything runs on my computer. No random cloud services touching my inbox.  
- **Control:** The AI never sends without my approval. It’s an assistant, not a replacement.  
- **Customization:** I own the stack. I can shape it around how I work, not how a SaaS product wants me to work.  
- **Learning:** As AI improves, my system improves with zero vendor lock-in.  

This isn’t just about efficiency. It’s about building *understanding*. By learning how AI interacts with my workflow, I’m learning how to build tools that can adapt, evolve, and scale with my creativity.  

---

## The real innovation

Email automation isn't new. The leap is giving AI the ability to build and fix its own automation.  
Instead of hiring someone for every tweak, I describe what I want and Claude does the heavy lifting.  
It's like having a technical co-founder who never sleeps.  

But the bigger breakthrough is what it's teaching me.  
Each project like this sharpens my ability to design systems that are not only smart but human-aware tools that respect boundaries, context, and creativity.  

---

## What’s next

- **Lead generation:** AI identifies and drafts outreach to potential partners and sponsors.  
- **Market intelligence:** Monitors news and sends me what actually matters.  
- **Meeting prep:** Reads my calendar and builds one-pagers before calls.  
- **Social media:** Drafts posts in my voice, still with approval.  

Same principle: AI does the work. I make the calls.  

The next evolution is connecting these systems: my AI assistant, BallCode, and future local agents into one intelligent network that learns *my rhythm.*  
Every experiment like this gets me closer to that.  

---

## The bottom line

We’re moving from “AI as a tool” to “AI as a partner.”  
For sports innovators, that means:  

- Faster execution on good ideas  
- More time for strategy and relationships  
- Less time on repetitive admin  
- Better consistency across communications  

Understanding AI on this level changes everything.  
It's not just about automation. It's about developing a new kind of fluency.  
The more I learn how to *teach* AI, the more I can build tools that think, move, and create like me.  

Everything here is local-first.  
The visuals above show the full workflow, approval steps, and the MCP bridge. You can see exactly how it all connects.  
Because innovation isn't just about what you build. It's about *what you learn while building it.*  


