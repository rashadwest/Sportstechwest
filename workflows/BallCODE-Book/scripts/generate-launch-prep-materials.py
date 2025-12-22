#!/usr/bin/env python3
"""
Launch Prep Materials Generator
Generates demo script, one-pager, and launch announcement templates

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
from pathlib import Path
from datetime import datetime, timedelta

PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "documents" / "launch-prep"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LAUNCH_DATE = datetime(2025, 12, 15)  # Tomorrow
TODAY = datetime.now()

def generate_demo_script():
    """Generate demo script for launch presentation."""
    output_file = OUTPUT_DIR / "demo-script.md"
    
    content = f"""# BallCODE Launch Demo Script

**Launch Date:** {LAUNCH_DATE.strftime('%B %d, %Y')}  
**Duration:** ~4 minutes  
**Audience:** Schools, Partners, Educators

---

## 🎬 Demo Flow

### Opening (30 seconds)
"Hi, I'm Rashad West, and I'm excited to show you BallCODE - a program that teaches coding, math, and AI concepts through basketball.

BallCODE combines the excitement of basketball with hands-on STEM learning, designed specifically for grades 3-8. Today I'll show you how it works."

**Key Points:**
- Introduce yourself
- State the problem (engaging students in STEM)
- Present BallCODE as the solution

---

### Show Book 1 Page (1 minute)
"Let me show you Book 1: The Tip-off Trial. This is where students start their journey."

**Actions:**
1. Navigate to ballcode.co/books/book1
2. Show the story content
3. Point out learning objectives
4. Highlight the visual assets (if added)

**Key Talking Points:**
- "Each book tells a basketball story that teaches coding concepts"
- "Students learn sequences through Nova's journey"
- "The story connects directly to hands-on exercises"

---

### Show Game Exercise (1 minute)
"Now let's see the interactive exercise. Students click 'Try the Exercise' to practice what they learned."

**Actions:**
1. Click "Try the Exercise" button
2. Show game loading
3. Demonstrate the exercise (if possible)
4. Show completion flow

**Key Talking Points:**
- "60-90 second exercises keep students engaged"
- "Immediate feedback helps students learn"
- "The game reinforces concepts from the story"

---

### Show Learning Loop (30 seconds)
"Here's the complete learning loop: Story → Exercise → Understanding."

**Actions:**
1. Return to book page
2. Show "What You Learned" section
3. Show progression pathway

**Key Talking Points:**
- "Complete learning loop: read, practice, understand"
- "Clear progression from Book 1 to Book 2"
- "Students see their progress"

---

### Closing (30 seconds)
"BallCODE is ready for pilot programs. We're offering free pilot access to select schools, and I'd love to discuss how this could work for your students.

You can reach me at schools@ballcode.co or visit ballcode.co to learn more. Thank you!"

**Key Points:**
- Clear call-to-action
- Contact information
- Next steps

---

## 📝 Notes

**Practice Tips:**
- Time yourself (aim for 4 minutes)
- Practice transitions between sections
- Prepare for questions about:
  - Grade levels
  - Curriculum alignment
  - Pilot program details
  - Technical requirements

**Common Questions:**
- "What grade levels is this for?" → Grades 3-8
- "How long is each exercise?" → 60-90 seconds
- "What do we need to get started?" → Just internet access
- "Is there teacher training?" → Self-service onboarding available

---

**Generated:** {TODAY.strftime('%B %d, %Y at %I:%M %p')}  
**Launch Date:** {LAUNCH_DATE.strftime('%B %d, %Y')}
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Generated demo script: {output_file}")
    return output_file

def generate_one_pager():
    """Generate one-pager for launch."""
    output_file = OUTPUT_DIR / "one-pager.md"
    
    content = f"""# BallCODE - One-Pager

**What is BallCODE?**
BallCODE teaches coding, math, and AI concepts through basketball. Designed for grades 3-8, it combines story-based learning with hands-on interactive exercises.

---

## 🎯 What Students Learn

- **Coding Fundamentals:** Sequences, conditionals, loops, functions
- **Math Concepts:** Patterns, logic, problem-solving
- **AI Basics:** Decision-making, state management, algorithms
- **Basketball Skills:** Dribbling, passing, shooting, strategy

---

## 📚 How It Works

1. **Read the Story** - Students read a basketball story that introduces coding concepts
2. **Try the Exercise** - Interactive 60-90 second game exercises reinforce learning
3. **See Progress** - Clear learning objectives and progression pathway

**Complete Learning Loop:** Story → Exercise → Understanding

---

## 🚀 Getting Started

**For Schools:**
- Free pilot program available
- Self-service onboarding
- Complete Episode 1 content included
- Teacher resources provided

**Contact:** schools@ballcode.co

**Website:** ballcode.co

---

## 📊 Key Features

- ✅ Story-first learning approach
- ✅ Interactive game exercises
- ✅ Blocks → Bridge → Python progression
- ✅ Mobile-friendly
- ✅ No special equipment needed

---

## 🎓 Curriculum Alignment

- CSTA Computer Science Standards
- Common Core Math Standards
- NGSS Science Standards
- Physical Education Standards

---

## 📞 Contact Information

**General Inquiries:** info@ballcode.co  
**School Partnerships:** schools@ballcode.co  
**Website:** ballcode.co

**Response Time:** Within 24 hours

---

**Launch Date:** {LAUNCH_DATE.strftime('%B %d, %Y')}  
**Generated:** {TODAY.strftime('%B %d, %Y')}
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Generated one-pager: {output_file}")
    return output_file

def generate_launch_announcement():
    """Generate launch announcement templates."""
    output_file = OUTPUT_DIR / "launch-announcement-templates.md"
    
    content = f"""# Launch Announcement Templates

**Launch Date:** {LAUNCH_DATE.strftime('%B %d, %Y')}

---

## 📧 Email Template

**Subject:** Introducing BallCODE - Coding Through Basketball

**Body:**
```
Hi [NAME],

I'm excited to share that BallCODE is launching today!

BallCODE teaches coding, math, and AI concepts through basketball - making STEM learning engaging and accessible for grades 3-8.

What makes BallCODE unique:
• Story-first learning approach
• Interactive 60-90 second exercises
• Complete learning loop: read, practice, understand
• No special equipment needed

We're offering free pilot programs to select schools. If you know any educators who might be interested, I'd love an introduction.

Learn more: ballcode.co
Contact: schools@ballcode.co

Thanks!
Rashad West
Creator, BallCODE
```

---

## 📱 Social Media Template (Twitter/X)

**Post 1:**
```
🚀 Launching today: BallCODE - coding through basketball!

Teach coding, math & AI to grades 3-8 using the excitement of basketball. Story-first learning + interactive exercises.

Free pilot programs available for schools.

Learn more: ballcode.co
```

**Post 2:**
```
🎯 BallCODE combines:
✅ Basketball stories
✅ Interactive exercises
✅ Coding fundamentals
✅ Math concepts
✅ AI basics

All in one engaging platform for grades 3-8.

Try it: ballcode.co
```

---

## 📱 Social Media Template (LinkedIn)

**Post:**
```
I'm excited to announce the launch of BallCODE - a program that teaches coding, math, and AI concepts through basketball.

After seeing how hard it is to engage students in STEM subjects, I created BallCODE to combine the excitement of basketball with hands-on learning.

What makes BallCODE different:
• Story-first approach - students read basketball stories that teach coding
• Interactive exercises - 60-90 second game challenges reinforce concepts
• Complete learning loop - read, practice, understand
• Designed for grades 3-8
• No special equipment needed

We're offering free pilot programs to select schools. If you know educators who might be interested, I'd love to connect.

Learn more: ballcode.co
Contact: schools@ballcode.co

#EdTech #STEMEducation #CodingForKids #Basketball
```

---

## 📧 Follow-Up Email Template (7 Days After Launch)

**Subject:** Following up: BallCODE Launch

**Body:**
```
Hi [NAME],

I wanted to follow up on my launch announcement last week about BallCODE.

We've had great initial interest from schools, and I wanted to see if you or anyone you know might be interested in our free pilot program.

BallCODE teaches coding through basketball - perfect for grades 3-8. The pilot includes complete Episode 1 content, teacher resources, and ongoing support.

If you're interested, I'd love to schedule a quick 15-minute call to discuss.

Thanks!
Rashad West
Creator, BallCODE
```

---

**Generated:** {TODAY.strftime('%B %d, %Y at %I:%M %p')}
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Generated launch announcement templates: {output_file}")
    return output_file

def main():
    """Generate all launch prep materials."""
    print("=" * 60)
    print("📝 Launch Prep Materials Generator")
    print("=" * 60)
    print()
    
    demo_script = generate_demo_script()
    one_pager = generate_one_pager()
    announcement = generate_launch_announcement()
    
    print()
    print("=" * 60)
    print("✅ Launch Prep Materials Generated!")
    print("=" * 60)
    print()
    print("📁 Files Created:")
    print(f"  ✅ {demo_script}")
    print(f"  ✅ {one_pager}")
    print(f"  ✅ {announcement}")
    print()
    print("🚀 Next Steps:")
    print("  1. Review and customize demo script")
    print("  2. Practice demo (aim for 4 minutes)")
    print("  3. Customize one-pager with your details")
    print("  4. Schedule launch announcement posts")
    print("  5. Send launch emails to your network")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

