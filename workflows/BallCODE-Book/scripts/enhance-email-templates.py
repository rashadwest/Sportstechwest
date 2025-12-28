#!/usr/bin/env python3
"""
Robot: Enhance Email Templates with @Seth Godin Purple Cow Messaging
Applies remarkable, value-first messaging principles to CES launch emails

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import json
import sys
from pathlib import Path
from typing import Dict

PROJECT_ROOT = Path(__file__).parent.parent
EMAIL_TEMPLATES_PATH = PROJECT_ROOT / "documents" / "promotion-content" / "email-templates.json"
ENHANCED_TEMPLATES_PATH = PROJECT_ROOT / "documents" / "promotion-content" / "email-templates-enhanced.json"

class EmailTemplateEnhancer:
    """Robot to enhance email templates with @Seth Godin principles"""
    
    def __init__(self):
        self.templates = self.load_templates()
    
    def load_templates(self) -> Dict:
        """Load current email templates"""
        if EMAIL_TEMPLATES_PATH.exists():
            with open(EMAIL_TEMPLATES_PATH, 'r') as f:
                return json.load(f)
        return {}
    
    def apply_purple_cow_principles(self, template: Dict, template_key: str) -> Dict:
        """Apply @Seth Godin Purple Cow principles to email template"""
        enhanced = template.copy()
        
        # @Seth Godin Principles:
        # 1. Remarkable (stand out)
        # 2. Value-first (give before asking)
        # 3. Permission marketing (earn attention)
        # 4. Tell remarkable stories
        # 5. Be a Purple Cow (be different)
        
        if template_key == "ces_launch_announcement":
            # Make subject line more remarkable
            enhanced["subject"] = "🎉 BallCODE Launches at CES 2026 - The First Sports-Based Coding Platform"
            
            # Make preheader more value-first
            enhanced["preheader"] = "10 pilot schools already seeing success. Be part of the story."
            
            # Enhance body with remarkable story and value-first approach
            enhanced["body_template"] = """Hi {contact_name},

**Something remarkable is happening at CES 2026.**

BallCODE is launching as the **first sports-based coding education platform** - and we're inviting {school_name} to be part of it.

**Here's what makes this different (the Purple Cow):**

Most coding education is abstract. Kids learn "if-then" statements without context.

BallCODE is different. We teach coding through basketball stories. Students learn:
- Coding logic by calling plays
- Math concepts by analyzing shots
- AI fundamentals by reading defenses

**The Remarkable Results:**
- 10 pilot schools already running
- Students actually understand coding (not just memorize)
- Teachers say it's the most engaging STEM program they've seen
- **Launching at CES 2026** (January 7-10)

**What You Get (Free Pilot - No Strings):**
- Complete Episode 1: "The Tip-off Trial"
- Teacher guide with learning objectives
- Interactive game exercises
- Student access (no login required)
- Ongoing support
- **Featured in our CES launch story** (if you want)

**Why This Matters:**
This isn't just another educational program. It's a new way to teach coding - through the language kids already speak: basketball.

**Limited Opportunity:**
We're accepting the next 50 schools for our pilot program. {school_name} could be one of them.

**No pressure, no commitment - just a remarkable opportunity.**

Interested? Let's schedule a quick 15-minute call to see if this fits your students.

Best,
Rashad West
Creator, BallCODE
{email}
{phone}

P.S. - This is completely free. No catch. We're looking for schools that want to try something different."""
            
            # Enhanced CTA
            enhanced["cta"] = "See If This Fits Your Students"
            enhanced["cta_link"] = "https://calendly.com/ballcode/demo"
        
        elif template_key == "cold_outreach":
            # Make it more remarkable
            enhanced["subject"] = "The First Sports-Based Coding Platform - Free Pilot for {school_name}"
            enhanced["preheader"] = "Teaching coding through basketball. It actually works."
            
            # Value-first approach
            enhanced["body_template"] = """Dear {contact_name},

I noticed {school_name} has {specific_program}, and I think you'd find this interesting.

**Here's what's different:**

Most coding education feels like work. Kids learn concepts they can't see or touch.

BallCODE is different. We teach coding through basketball stories. When students call a play, they're learning sequences. When they analyze a shot, they're learning probability. When they read a defense, they're learning pattern recognition.

**The Remarkable Part:**
Students don't realize they're learning coding. They think they're playing basketball.

**What You Get (Completely Free):**
- Episode 1: "The Tip-off Trial" (complete story + exercises)
- Teacher guide (ready to use, minimal prep)
- Interactive game components
- Student access (no login required)
- Ongoing support
- **Be part of our CES 2026 launch** (January 7-10)

**What We're Looking For:**
- 2-4 week pilot commitment
- Feedback on what works (and what doesn't)
- Optional: Testimonials (if you love it)
- Optional: Case study (anonymized if preferred)

**No pressure. No commitment. Just a remarkable opportunity.**

Would you be open to a quick 15-minute call to see if this could work for your students?

Best regards,
Rashad West
Creator, BallCODE
{email}
{phone}"""
        
        elif template_key == "warm_contact":
            # More personal, permission-based
            enhanced["subject"] = "Quick question about {school_name}'s STEM programs"
            enhanced["preheader"] = "Something remarkable I think you'd find interesting"
            
            enhanced["body_template"] = """Hi {contact_name},

I hope you're doing well!

I've been working on something I think you'd find interesting, and I'd love your perspective.

**The Remarkable Idea:**
What if we could teach coding through basketball? Not coding ABOUT basketball, but coding THROUGH basketball stories.

That's BallCODE. Students learn coding logic by calling plays. They learn math by analyzing shots. They learn AI by reading defenses.

**Why I'm Reaching Out:**
I know {school_name} has {specific_program}, and I think BallCODE could be a great fit. We're offering a **completely free pilot program** to select schools.

**What You Get:**
- Complete Episode 1 content
- Teacher resources (ready to use)
- Student access to interactive games
- Ongoing support
- **Be part of our CES 2026 launch** (January 7-10)

**No pressure - just a remarkable opportunity.**

I'd love to schedule a quick 15-minute call to see if this might work for your students. Would you be available for a brief conversation this week?

Thanks, and I hope to catch up soon!

Best,
Rashad West
Creator, BallCODE
{email}
{phone}"""
        
        return enhanced
    
    def enhance_all_templates(self) -> Dict:
        """Enhance all email templates"""
        enhanced = {}
        
        for key, template in self.templates.items():
            print(f"   Enhancing: {key}...")
            enhanced[key] = self.apply_purple_cow_principles(template, key)
        
        return enhanced
    
    def save_enhanced_templates(self, enhanced: Dict):
        """Save enhanced templates"""
        EMAIL_TEMPLATES_PATH.parent.mkdir(parents=True, exist_ok=True)
        
        # Save as enhanced version
        with open(ENHANCED_TEMPLATES_PATH, 'w') as f:
            json.dump(enhanced, f, indent=2)
        
        print(f"✅ Enhanced templates saved: {ENHANCED_TEMPLATES_PATH}")
        
        # Also update original (backup first)
        backup_path = EMAIL_TEMPLATES_PATH.with_suffix('.json.backup')
        if EMAIL_TEMPLATES_PATH.exists():
            import shutil
            shutil.copy(EMAIL_TEMPLATES_PATH, backup_path)
            print(f"✅ Backup created: {backup_path}")
        
        with open(EMAIL_TEMPLATES_PATH, 'w') as f:
            json.dump(enhanced, f, indent=2)
        
        print(f"✅ Original templates updated: {EMAIL_TEMPLATES_PATH}")


def main():
    """Main robot function"""
    print("\n" + "=" * 70)
    print("🤖 Robot: Enhance Email Templates with @Seth Godin Principles")
    print("=" * 70)
    
    enhancer = EmailTemplateEnhancer()
    
    print(f"\n📄 Loading templates from: {EMAIL_TEMPLATES_PATH}")
    print(f"   Found {len(enhancer.templates)} templates")
    
    print("\n🎨 Applying @Seth Godin Purple Cow Principles:")
    print("   - Remarkable (stand out)")
    print("   - Value-first (give before asking)")
    print("   - Permission marketing (earn attention)")
    print("   - Tell remarkable stories")
    print("   - Be a Purple Cow (be different)")
    
    enhanced = enhancer.enhance_all_templates()
    
    print(f"\n💾 Saving enhanced templates...")
    enhancer.save_enhanced_templates(enhanced)
    
    print("\n" + "=" * 70)
    print("✅ Email Templates Enhanced!")
    print("=" * 70)
    print("\n📋 Key Improvements:")
    print("   ✅ Subject lines more remarkable")
    print("   ✅ Preheaders value-first")
    print("   ✅ Body content tells remarkable story")
    print("   ✅ Permission marketing approach")
    print("   ✅ Purple Cow positioning emphasized")
    print("\n💡 Next Steps:")
    print("   1. Review enhanced templates")
    print("   2. Test email rendering")
    print("   3. Verify personalization variables")
    print("   4. Update n8n workflow with new templates")
    print("=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


