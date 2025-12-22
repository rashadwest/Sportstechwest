#!/usr/bin/env python3
"""
Comprehensive Website Improvement Script
Fixes navigation, contact info, FAQ, and adds improvements

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
INDEX_HTML = WEBSITE_DIR / "index.html"

def fix_navigation_menu():
    """Fix navigation menu - replace Media and Section with About and Contact."""
    print("🔧 Fixing navigation menu...")
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace placeholder navigation links
    nav_updates = [
        (r'<a href="#" class="header-top-navlink">Media</a>', 
         '<a href="#about" class="header-top-navlink">About</a>'),
        (r'<a href="#" class="header-top-navlink">Section</a>', 
         '<a href="#contact" class="header-top-navlink">Contact</a>'),
    ]
    
    changes_made = 0
    for old, new in nav_updates:
        if re.search(old, content):
            content = re.sub(old, new, content)
            print(f"  ✅ Updated navigation: {old[:30]}... → {new[:30]}...")
            changes_made += 1
        else:
            # Check if already updated
            if "About" in content and "Contact" in content:
                print(f"  ⚠️  Navigation already updated or pattern not found")
    
    if changes_made > 0:
        with open(INDEX_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Navigation menu fixed ({changes_made} changes)")
        return True
    else:
        print("  ⚠️  No navigation changes needed")
        return False

def add_contact_information_display():
    """Add contact information display to contact section."""
    print("📧 Adding contact information display...")
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if contact info already exists
    if 'contact-info-display' in content or 'info@ballcode.co' in content:
        print("  ⚠️  Contact information already exists")
        return False
    
    # Contact information HTML
    contact_info_html = '''
            <div class="contact-info-display" style="margin-top: 40px; text-align: center; padding: 30px 20px; background: rgba(255, 255, 255, 0.05); border-radius: 12px; max-width: 600px; margin-left: auto; margin-right: auto;">
              <h3 style="font-size: 1.5rem; margin-bottom: 20px; color: #fff;">Get in Touch</h3>
              <div style="display: flex; flex-direction: column; gap: 15px;">
                <p style="font-size: 1.1rem; color: rgba(255, 255, 255, 0.9);">
                  <strong style="color: #FF6B35;">Email:</strong> 
                  <a href="mailto:info@ballcode.co" style="color: #0C72B3; text-decoration: none; font-weight: 500;">info@ballcode.co</a>
                </p>
                <p style="font-size: 1.1rem; color: rgba(255, 255, 255, 0.9);">
                  <strong style="color: #FF6B35;">For Schools:</strong> 
                  <a href="mailto:schools@ballcode.co" style="color: #0C72B3; text-decoration: none; font-weight: 500;">schools@ballcode.co</a>
                </p>
                <p style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.7); margin-top: 10px;">
                  We typically respond within 24 hours
                </p>
              </div>
            </div>
'''
    
    # Insert after contact form, before contact-socials
    pattern = r'(</form>\s*)(<div class="contact-socials">)'
    
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1' + contact_info_html + r'\2', content)
        with open(INDEX_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        print("  ✅ Added contact information display")
        return True
    else:
        print("  ⚠️  Could not find insertion point for contact info")
        return False

def fix_faq_content():
    """Fix repetitive FAQ content with proper answers."""
    print("❓ Fixing FAQ content...")
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # FAQ updates
    faq_updates = [
        {
            'question': 'How to play?',
            'old_answer': r'To play, simply create an account and start exploring the game\s+modes available\.',
            'new_answer': 'BallCODE combines basketball stories with interactive coding exercises. Start by reading Book 1, then click "Try the Exercise" to practice what you learned in the game. Each book teaches coding concepts through basketball!'
        },
        {
            'question': 'How do I sign up?',
            'old_answer': r'To play, simply create an account and start exploring the game\s+modes available\.',
            'new_answer': 'For individual access, purchase Book 1 on Gumroad and you\'ll receive instant access. For schools, use the contact form above to request a pilot program. We offer free pilot programs to select schools!'
        },
        {
            'question': 'How do I access the social community?',
            'old_answer': r'To play, simply create an account and start exploring the game\s+modes available\.',
            'new_answer': 'Follow us on Instagram (@ballc0de), Twitter/X (@ballc0de), and TikTok (@ballc0de) for updates, student success stories, and coding tips. Join our community of educators and students learning coding through basketball!'
        }
    ]
    
    changes_made = 0
    for faq in faq_updates:
        # Find the FAQ item
        question_pattern = rf'<span>{re.escape(faq["question"])}</span>'
        if re.search(question_pattern, content):
            # Replace the answer
            old_pattern = rf'<div class="faq-answer">\s*{faq["old_answer"]}\s*</div>'
            new_answer = f'<div class="faq-answer">\n                  {faq["new_answer"]}\n                </div>'
            
            if re.search(old_pattern, content, re.DOTALL):
                content = re.sub(old_pattern, new_answer, content, flags=re.DOTALL)
                print(f"  ✅ Updated FAQ: {faq['question']}")
                changes_made += 1
            else:
                print(f"  ⚠️  Could not find answer pattern for: {faq['question']}")
    
    if changes_made > 0:
        with open(INDEX_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ FAQ content fixed ({changes_made} FAQs updated)")
        return True
    else:
        print("  ⚠️  No FAQ changes made")
        return False

def add_book1_link():
    """Add link to Book 1 page from homepage book card."""
    print("📚 Adding Book 1 page link...")
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if link already exists
    if 'books/book1.html' in content or 'href="book1' in content:
        print("  ⚠️  Book 1 link may already exist")
        return False
    
    # Find Book 1 card and add link to title or image
    # Look for Book 1 card pattern
    book1_pattern = r'(<div class="books-card">.*?<h3 class="books-card-title-large">BOOK 1: THE<br>FOUNDATION<br>BLOCK</h3>)'
    
    if re.search(book1_pattern, content, re.DOTALL):
        # Add link wrapper around the title or make the card clickable
        # For now, let's add a "Read Book 1" button or link
        link_html = '<a href="./books/book1.html" style="display: inline-block; margin-top: 1rem; color: #0C72B3; text-decoration: none; font-weight: 600;">Read Book 1 →</a>'
        
        # Insert after the Gumroad link
        gumroad_pattern = r'(<a href="https://9768426137106\.gumroad\.com/l/gxgzv"[^>]*>Get Book 1 \(Individual\) →</a>)'
        if re.search(gumroad_pattern, content):
            content = re.sub(gumroad_pattern, r'\1' + '\n                  ' + link_html, content)
            with open(INDEX_HTML, 'w', encoding='utf-8') as f:
                f.write(content)
            print("  ✅ Added Book 1 page link")
            return True
        else:
            print("  ⚠️  Could not find insertion point for Book 1 link")
            return False
    else:
        print("  ⚠️  Book 1 card not found")
        return False

def add_about_section():
    """Add a basic About section if it doesn't exist."""
    print("ℹ️  Checking for About section...")
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if About section exists
    if 'id="about"' in content or 'section.*about' in content.lower():
        print("  ⚠️  About section may already exist")
        return False
    
    # Add About section before contact section
    about_html = '''
        <!-- About-Section -->
        <section class="about" id="about" style="padding: 80px 0; background: linear-gradient(135deg, #0C72B3 0%, #1a4d7a 100%);">
          <div class="container">
            <div style="max-width: 900px; margin: 0 auto; text-align: center; color: #fff;">
              <h2 style="font-size: 2.5rem; margin-bottom: 1.5rem; color: #fff;">About BallCODE</h2>
              <p style="font-size: 1.2rem; line-height: 1.8; margin-bottom: 2rem; color: rgba(255, 255, 255, 0.9);">
                BallCODE teaches coding, math, and AI concepts through basketball. Designed for grades 3-8, 
                we combine the excitement of basketball with hands-on STEM learning.
              </p>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 3rem;">
                <div style="background: rgba(255, 255, 255, 0.1); padding: 2rem; border-radius: 12px;">
                  <h3 style="color: #FF6B35; margin-bottom: 1rem;">Story-First Learning</h3>
                  <p style="color: rgba(255, 255, 255, 0.9);">Each book tells a basketball story that teaches coding concepts naturally.</p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.1); padding: 2rem; border-radius: 12px;">
                  <h3 style="color: #FF6B35; margin-bottom: 1rem;">Interactive Exercises</h3>
                  <p style="color: rgba(255, 255, 255, 0.9);">60-90 second game challenges reinforce what students learn in the story.</p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.1); padding: 2rem; border-radius: 12px;">
                  <h3 style="color: #FF6B35; margin-bottom: 1rem;">Clear Progression</h3>
                  <p style="color: rgba(255, 255, 255, 0.9);">Blocks → Bridge → Python pathway guides students from beginner to advanced.</p>
                </div>
              </div>
            </div>
          </div>
        </section>
'''
    
    # Insert before contact section
    pattern = r'(<!-- Contact-Section -->)'
    if re.search(pattern, content):
        content = re.sub(pattern, about_html + r'\n\n        \1', content)
        with open(INDEX_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        print("  ✅ Added About section")
        return True
    else:
        print("  ⚠️  Could not find insertion point for About section")
        return False

def main():
    """Run all website improvements."""
    print("=" * 60)
    print("🚀 Comprehensive Website Improvement Script")
    print("=" * 60)
    print()
    
    if not INDEX_HTML.exists():
        print(f"❌ Error: {INDEX_HTML} not found")
        return False
    
    results = {}
    
    # Run all improvements
    results["Navigation Menu"] = fix_navigation_menu()
    print()
    
    results["Contact Information"] = add_contact_information_display()
    print()
    
    results["FAQ Content"] = fix_faq_content()
    print()
    
    results["Book 1 Link"] = add_book1_link()
    print()
    
    results["About Section"] = add_about_section()
    print()
    
    # Summary
    successful = sum(1 for r in results.values() if r)
    total = len(results)
    
    print("=" * 60)
    print(f"✅ Website Improvements Complete: {successful}/{total} successful")
    print("=" * 60)
    print()
    print("📋 Changes Made:")
    for name, success in results.items():
        status = "✅" if success else "⚠️"
        print(f"  {status} {name}")
    print()
    print("🚀 Next Steps:")
    print("  1. Review changes in BallCode/index.html")
    print("  2. Test locally: cd BallCode && python3 -m http.server")
    print("  3. Verify navigation, contact info, and FAQ")
    print("  4. Deploy: cd BallCode && ../automate-deployment.sh 'Website improvements'")
    print()
    
    return successful > 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

