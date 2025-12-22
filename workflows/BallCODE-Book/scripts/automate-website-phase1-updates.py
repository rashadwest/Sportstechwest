#!/usr/bin/env python3
"""
BallCODE Website Phase 1 Updates Automation
Fixes critical website issues: navigation, contact info, sign-up button

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import re
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
WEBSITE_DIR = PROJECT_ROOT / "BallCode"
INDEX_HTML = WEBSITE_DIR / "index.html"

def update_navigation_menu():
    """Fix navigation menu - replace placeholder links with proper ones."""
    print("🔧 Updating navigation menu...")
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace placeholder navigation links
    nav_updates = {
        r'<a href="#" class="header-top-navlink">Media</a>': 
            '<a href="#about" class="header-top-navlink">About</a>',
        r'<a href="#" class="header-top-navlink">Section</a>': 
            '<a href="#contact" class="header-top-navlink">Contact</a>',
    }
    
    for old, new in nav_updates.items():
        if re.search(old, content):
            content = re.sub(old, new, content)
            print(f"  ✅ Updated: {old[:50]}...")
        else:
            print(f"  ⚠️  Not found: {old[:50]}...")
    
    return content

def fix_signup_button():
    """Fix sign-up button to link to contact section instead of external URL."""
    print("🔧 Fixing sign-up button...")
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix header sign-up button
    old_button = r'<a href="https://ballcode\.netlify\.app" class="header-top-cta" target="_blank">Sign Up</a>'
    new_button = '<a href="#contact" class="header-top-cta">Sign Up</a>'
    
    if re.search(old_button, content):
        content = re.sub(old_button, new_button, content)
        print("  ✅ Fixed header sign-up button")
    else:
        print("  ⚠️  Header sign-up button not found or already fixed")
    
    return content

def add_contact_information():
    """Add contact information display to contact section."""
    print("🔧 Adding contact information...")
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if contact info already exists
    if 'contact-info-display' in content:
        print("  ⚠️  Contact information already exists")
        return content
    
    # Add contact information after contact form
    contact_info_html = '''
            <div class="contact-info-display" style="margin-top: 40px; text-align: center; padding: 20px;">
              <h3 style="font-size: 1.5rem; margin-bottom: 20px; color: #333;">Get in Touch</h3>
              <div style="display: flex; flex-direction: column; gap: 15px; max-width: 500px; margin: 0 auto;">
                <p style="font-size: 1.1rem; color: #666;">
                  <strong>Email:</strong> <a href="mailto:info@ballcode.co" style="color: #eb6123; text-decoration: none;">info@ballcode.co</a>
                </p>
                <p style="font-size: 1.1rem; color: #666;">
                  <strong>For Schools:</strong> <a href="mailto:schools@ballcode.co" style="color: #eb6123; text-decoration: none;">schools@ballcode.co</a>
                </p>
                <p style="font-size: 0.95rem; color: #888; margin-top: 10px;">
                  We typically respond within 24 hours
                </p>
              </div>
            </div>
'''
    
    # Insert after contact form, before contact-socials
    pattern = r'(</form>\s*)(<div class="contact-socials">)'
    replacement = r'\1' + contact_info_html + r'\2'
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        print("  ✅ Added contact information display")
    else:
        print("  ⚠️  Could not find insertion point for contact info")
    
    return content

def update_contact_title():
    """Update contact section title to be more descriptive."""
    print("🔧 Updating contact section title...")
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update contact title
    old_title = r'<h2 class="contact-title">Contact Info</h2>'
    new_title = '<h2 class="contact-title">Get Updates & Free Resources</h2>'
    
    if re.search(old_title, content):
        content = re.sub(old_title, new_title, content)
        print("  ✅ Updated contact section title")
    else:
        print("  ⚠️  Contact title not found or already updated")
    
    return content

def main():
    """Run all website Phase 1 updates."""
    print("=" * 60)
    print("🤖 BallCODE Website Phase 1 Updates Automation")
    print("=" * 60)
    print()
    
    if not INDEX_HTML.exists():
        print(f"❌ Error: {INDEX_HTML} not found")
        return False
    
    try:
        # Read current content
        with open(INDEX_HTML, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply all updates
        content = update_navigation_menu()
        content = fix_signup_button()
        content = add_contact_information()
        content = update_contact_title()
        
        # Write updated content
        with open(INDEX_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print()
        print("=" * 60)
        print("✅ Website Phase 1 Updates Complete!")
        print("=" * 60)
        print()
        print("📋 Changes Made:")
        print("  ✅ Navigation menu updated (Media → About, Section → Contact)")
        print("  ✅ Sign-up button fixed (links to #contact)")
        print("  ✅ Contact information added (email addresses)")
        print("  ✅ Contact section title updated")
        print()
        print("🚀 Next Steps:")
        print("  1. Review changes in BallCode/index.html")
        print("  2. Test locally: cd BallCode && python3 -m http.server")
        print("  3. Deploy: cd BallCode && ../automate-deployment.sh 'Website Phase 1 updates'")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


