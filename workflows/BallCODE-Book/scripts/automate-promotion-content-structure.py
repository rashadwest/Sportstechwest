#!/usr/bin/env python3
"""
Automate Promotion Content Structure
Creates templates and structure for 2-week promotion content

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
from pathlib import Path
from datetime import datetime, timedelta

PROJECT_ROOT = Path(__file__).parent.parent
PROMOTION_DIR = PROJECT_ROOT / "documents" / "promotion-content"
TEASE_PLAN = PROJECT_ROOT / "TEASE-PROMOTION-PLAN.md"

# Ensure directory exists
PROMOTION_DIR.mkdir(parents=True, exist_ok=True)

def create_daily_content_templates():
    """Create templates for each day of promotion."""
    # Promotion period: Dec 31 - Jan 13 (14 days)
    start_date = datetime(2025, 12, 31)
    
    daily_templates = {}
    
    for day in range(14):
        current_date = start_date + timedelta(days=day)
        day_num = day + 1
        
        # Determine content type based on day
        if day_num == 1:
            content_type = "coming_soon_launch"
            title = "Coming Soon Launch"
            theme = "Story Launch - From NBA Courts to Classrooms"
        elif day_num <= 3:
            content_type = "story_tease"
            title = f"Story Tease - Day {day_num}"
            theme = "Your Journey & Vision"
        elif day_num <= 5:
            content_type = "system_tease"
            title = f"System Tease - Day {day_num}"
            theme = "How BallCODE Works"
        elif day_num <= 7:
            content_type = "value_proposition"
            title = f"Value Proposition - Day {day_num}"
            theme = "What Schools Get"
        elif day_num <= 10:
            content_type = "feature_deep_dive"
            title = f"Feature Deep Dive - Day {day_num}"
            theme = "System Features"
        elif day_num <= 13:
            content_type = "countdown"
            title = f"Countdown - {14 - day_num} Days Until Launch"
            theme = "Final Countdown"
        else:
            content_type = "launch_eve"
            title = "Launch Day Eve"
            theme = "Tomorrow We Launch"
        
        template = {
            "day": day_num,
            "date": current_date.strftime("%B %d, %Y"),
            "content_type": content_type,
            "title": title,
            "theme": theme,
            "channels": ["LinkedIn", "Twitter/X", "Email"],
            "content": {
                "headline": "",
                "body": "",
                "call_to_action": "",
                "hashtags": ["#BallCODE", "#CodingEducation", "#BasketballLearning"]
            },
            "visual_needed": False,
            "status": "draft"
        }
        
        daily_templates[f"day_{day_num}"] = template
    
    # Save templates
    templates_file = PROMOTION_DIR / "daily-content-templates.json"
    with open(templates_file, 'w') as f:
        json.dump(daily_templates, f, indent=2)
    
    print(f"✅ Created: {templates_file}")
    return templates_file

def create_email_templates():
    """Create email campaign templates."""
    email_templates = {
        "coming_soon": {
            "subject": "From NBA Courts to Classrooms - BallCODE is Coming",
            "preheader": "The most compelling educational system is launching January 14",
            "body_template": """Hi {name},

After years on NBA courts and in data science labs, I'm building something I wish existed when I was learning: BallCODE.

Coding through basketball.
Stories that teach.
Games that engage.
A system that works.

Coming January 14, 2026.

10 schools by New Year's. Let's go.

{signature}""",
            "cta": "Learn More",
            "cta_link": "https://ballcode.co"
        },
        "system_tease": {
            "subject": "See BallCODE in Action",
            "preheader": "What if coding felt like basketball?",
            "body_template": """Hi {name},

What if learning to code felt like learning to play basketball?

That's BallCODE.

Stories that make concepts click.
Games that make practice fun.
A system that actually works.

See how it works → {link}

{signature}""",
            "cta": "See How It Works",
            "cta_link": "https://ballcode.co/preview"
        },
        "school_outreach": {
            "subject": "Free Pilot Program: BallCODE for Your School",
            "preheader": "Complete Episode 1 content, ready to use this week",
            "body_template": """Hi {school_name} Team,

I'm reaching out because I think BallCODE could be a great fit for your students.

**What is BallCODE?**
A story-driven program that teaches coding through basketball. Students read engaging stories, then practice with interactive games.

**What You Get (Free Pilot):**
✅ Complete Episode 1 content
✅ Teacher resources and guides
✅ Student access
✅ Ongoing support

**Goal:** 10 schools by New Year's. Would you like to be one?

Interested? Let's schedule a quick 15-minute call.

{signature}""",
            "cta": "Schedule a Call",
            "cta_link": "https://calendly.com/ballcode/demo"
        },
        "countdown_3_days": {
            "subject": "3 Days Until Launch - Pre-Register Now",
            "preheader": "Get early access and priority onboarding",
            "body_template": """Hi {name},

3 days until BallCODE launches!

Pre-register now for:
✅ Early access
✅ Priority onboarding
✅ Exclusive resources

{pre_register_link}

See you on January 14!

{signature}""",
            "cta": "Pre-Register",
            "cta_link": "https://ballcode.co/pre-register"
        }
    }
    
    templates_file = PROMOTION_DIR / "email-templates.json"
    with open(templates_file, 'w') as f:
        json.dump(email_templates, f, indent=2)
    
    print(f"✅ Created: {templates_file}")
    return templates_file

def create_social_media_templates():
    """Create social media post templates."""
    social_templates = {
        "linkedin_story_post": {
            "platform": "LinkedIn",
            "type": "Long-form post",
            "template": """From NBA Courts to Classrooms

After years on NBA courts and in data science labs, I'm building something I wish existed when I was learning: BallCODE.

[Your story: Former professional basketball player → Data scientist → Educator]

Why BallCODE?
- Coding through basketball
- Stories that teach
- Games that engage
- A system that works

Coming January 14, 2026.

10 schools by New Year's. Let's go.

#BallCODE #CodingEducation #BasketballLearning #EdTech""",
            "length": "Long (500-1000 words)",
            "best_time": "Tuesday-Thursday, 8-10 AM"
        },
        "twitter_thread": {
            "platform": "Twitter/X",
            "type": "Thread",
            "template": """Thread: What if coding felt like basketball? 🧵

1/ That's BallCODE.

Stories that make concepts click.
Games that make practice fun.
A system that actually works.

2/ Coming January 14, 2026.

10 schools by New Year's. Let's go.

#BallCODE #CodingEducation""",
            "length": "Thread (5-10 tweets)",
            "best_time": "Monday-Friday, 9-11 AM or 1-3 PM"
        },
        "system_preview": {
            "platform": "All",
            "type": "Visual post",
            "template": """What if coding felt like basketball?

That's BallCODE.

[Image/Gif of system]

Stories → Games → Understanding

Like Duolingo, but for coding through basketball.

See how it works → ballcode.co/preview

#BallCODE #CodingEducation""",
            "length": "Short (100-200 words)",
            "visual_required": True
        }
    }
    
    templates_file = PROMOTION_DIR / "social-media-templates.json"
    with open(templates_file, 'w') as f:
        json.dump(social_templates, f, indent=2)
    
    print(f"✅ Created: {templates_file}")
    return templates_file

def create_coming_soon_page():
    """Create coming soon page HTML."""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coming Soon - BallCODE</title>
    <link rel="stylesheet" href="/css/style.css">
    <style>
        .coming-soon {
            max-width: 800px;
            margin: 0 auto;
            padding: 4rem 2rem;
            text-align: center;
        }
        .countdown {
            font-size: 3rem;
            font-weight: bold;
            color: #0C72B3;
            margin: 2rem 0;
        }
        .launch-date {
            font-size: 1.5rem;
            color: #666;
            margin-bottom: 2rem;
        }
        .pre-register-form {
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 8px;
            margin: 2rem 0;
        }
        .pre-register-form input {
            width: 100%;
            max-width: 400px;
            padding: 1rem;
            font-size: 1rem;
            border: 2px solid #0C72B3;
            border-radius: 4px;
            margin: 0.5rem 0;
        }
        .pre-register-form button {
            background: #0C72B3;
            color: white;
            padding: 1rem 2rem;
            font-size: 1.2rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 1rem;
        }
        .pre-register-form button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="coming-soon">
        <h1>🚀 BallCODE is Coming</h1>
        <p class="launch-date">January 14, 2026</p>
        
        <div class="countdown" id="countdown">
            <!-- Countdown will be calculated by JavaScript -->
        </div>
        
        <p style="font-size: 1.2rem; margin: 2rem 0;">
            From NBA Courts to Classrooms<br>
            The most compelling educational system
        </p>
        
        <div class="pre-register-form">
            <h2>Pre-Register for Early Access</h2>
            <form id="pre-register-form">
                <input type="email" placeholder="Your email" required>
                <input type="text" placeholder="School name (optional)">
                <button type="submit">Pre-Register</button>
            </form>
            <p style="font-size: 0.9rem; color: #666; margin-top: 1rem;">
                Get early access, priority onboarding, and exclusive resources
            </p>
        </div>
        
        <div style="margin-top: 3rem;">
            <h3>What is BallCODE?</h3>
            <p>
                BallCODE teaches coding through basketball. Students read engaging stories, 
                then practice with interactive games. A system that actually works.
            </p>
        </div>
    </div>
    
    <script>
        // Countdown timer
        function updateCountdown() {
            const launchDate = new Date('2026-01-14').getTime();
            const now = new Date().getTime();
            const distance = launchDate - now;
            
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            document.getElementById('countdown').innerHTML = 
                days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
            
            if (distance < 0) {
                document.getElementById('countdown').innerHTML = "LAUNCHED!";
            }
        }
        
        updateCountdown();
        setInterval(updateCountdown, 1000);
        
        // Pre-register form
        document.getElementById('pre-register-form').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you for pre-registering! We\'ll be in touch soon.');
            // TODO: Connect to email system or database
        });
    </script>
</body>
</html>
"""
    
    html_file = PROJECT_ROOT / "BallCode" / "coming-soon.html"
    with open(html_file, 'w') as f:
        f.write(html_content)
    
    print(f"✅ Created: {html_file}")
    return html_file

def create_school_outreach_automation():
    """Create school outreach automation structure."""
    outreach_structure = {
        "target_schools": {
            "total": 50,
            "criteria": [
                "Grades 3-8",
                "STEM focus",
                "Coding/computer science interest",
                "Basketball programs"
            ],
            "research_fields": [
                "School name",
                "Contact email",
                "Contact name",
                "Grade levels",
                "Student count",
                "STEM programs",
                "Basketball programs"
            ]
        },
        "outreach_templates": {
            "initial_email": {
                "subject": "Free Pilot Program: BallCODE for Your School",
                "personalization_fields": ["school_name", "contact_name", "grade_levels"],
                "template_file": "email-templates.json"
            },
            "follow_up_email": {
                "subject": "Following up: BallCODE Pilot Program",
                "days_after_initial": 3,
                "template_file": "email-templates.json"
            }
        },
        "tracking": {
            "spreadsheet_template": "school-outreach-tracker.csv",
            "fields": [
                "School Name",
                "Contact Name",
                "Email",
                "Status",
                "Date Contacted",
                "Response",
                "Next Action",
                "Notes"
            ]
        }
    }
    
    # Create CSV template
    csv_content = "School Name,Contact Name,Email,Status,Date Contacted,Response,Next Action,Notes\n"
    csv_file = PROMOTION_DIR / "school-outreach-tracker.csv"
    with open(csv_file, 'w') as f:
        f.write(csv_content)
    
    # Save structure
    structure_file = PROMOTION_DIR / "school-outreach-structure.json"
    with open(structure_file, 'w') as f:
        json.dump(outreach_structure, f, indent=2)
    
    print(f"✅ Created: {csv_file}")
    print(f"✅ Created: {structure_file}")
    return structure_file, csv_file

def create_content_calendar():
    """Create promotion content calendar."""
    start_date = datetime(2025, 12, 31)
    
    calendar = []
    
    for day in range(14):
        current_date = start_date + timedelta(days=day)
        day_num = day + 1
        
        if day_num == 1:
            content = {
                "date": current_date.strftime("%Y-%m-%d"),
                "day": day_num,
                "theme": "Coming Soon Launch",
                "content": [
                    "LinkedIn: Long-form story post",
                    "Twitter: Thread announcement",
                    "Email: Coming soon campaign"
                ],
                "visuals": ["Your photo", "BallCODE logo"],
                "cta": "Pre-register"
            }
        elif day_num <= 7:
            content = {
                "date": current_date.strftime("%Y-%m-%d"),
                "day": day_num,
                "theme": "System Tease",
                "content": [
                    f"Social: Day {day_num} teaser",
                    "Email: System preview"
                ],
                "visuals": ["System screenshot"],
                "cta": "Learn More"
            }
        else:
            days_remaining = 14 - day_num
            content = {
                "date": current_date.strftime("%Y-%m-%d"),
                "day": day_num,
                "theme": f"{days_remaining} Days Until Launch",
                "content": [
                    f"Social: Countdown post",
                    "Email: Pre-registration reminder"
                ],
                "visuals": ["Countdown graphic"],
                "cta": "Pre-Register"
            }
        
        calendar.append(content)
    
    calendar_file = PROMOTION_DIR / "content-calendar.json"
    with open(calendar_file, 'w') as f:
        json.dump(calendar, f, indent=2)
    
    print(f"✅ Created: {calendar_file}")
    return calendar_file

def main():
    """Main function."""
    print("=" * 60)
    print("📢 Promotion Content Structure Automation")
    print("=" * 60)
    print()
    
    print("📅 Creating daily content templates...")
    create_daily_content_templates()
    print()
    
    print("📧 Creating email templates...")
    create_email_templates()
    print()
    
    print("📱 Creating social media templates...")
    create_social_media_templates()
    print()
    
    print("🌐 Creating coming soon page...")
    create_coming_soon_page()
    print()
    
    print("🏫 Creating school outreach structure...")
    create_school_outreach_automation()
    print()
    
    print("📆 Creating content calendar...")
    create_content_calendar()
    print()
    
    print("=" * 60)
    print("✅ Promotion Content Structure Complete!")
    print("=" * 60)
    print()
    
    print("📋 Created Files:")
    print(f"  1. Daily content templates: {PROMOTION_DIR / 'daily-content-templates.json'}")
    print(f"  2. Email templates: {PROMOTION_DIR / 'email-templates.json'}")
    print(f"  3. Social media templates: {PROMOTION_DIR / 'social-media-templates.json'}")
    print(f"  4. Coming soon page: BallCode/coming-soon.html")
    print(f"  5. School outreach structure: {PROMOTION_DIR / 'school-outreach-structure.json'}")
    print(f"  6. Content calendar: {PROMOTION_DIR / 'content-calendar.json'}")
    print()
    
    print("🚀 Next Steps:")
    print("  1. Review templates and customize")
    print("  2. Fill in daily content using templates")
    print("  3. Personalize email templates")
    print("  4. Create visuals for social media")
    print("  5. Start school outreach using tracker")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

