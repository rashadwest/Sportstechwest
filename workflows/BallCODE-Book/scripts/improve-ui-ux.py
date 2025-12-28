#!/usr/bin/env python3
"""
UI/UX Improvement Script
Implements kid-friendly, Duolingo/Notion-inspired improvements

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import re
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
CSS_FILE = PROJECT_ROOT / "BallCode" / "css" / "style.css"
HTML_FILE = PROJECT_ROOT / "BallCode" / "index.html"

def print_header(title):
    """Print formatted header."""
    print("\n" + "=" * 70)
    print(f"🎨 {title}")
    print("=" * 70)

def add_kid_friendly_colors(css_content):
    """Add kid-friendly color palette to CSS."""
    print("\n📝 Adding kid-friendly color palette...")
    
    # Find :root section
    root_pattern = r'(:root\s*\{[^}]*\})'
    
    # Kid-friendly colors (Duolingo-inspired)
    new_colors = """
  /* Kid-Friendly Colors (Duolingo-inspired) */
  --primary-orange: #FF6B35;      /* Energetic, fun */
  --primary-blue: #4ECDC4;         /* Calm, trustworthy */
  --primary-green: #95E1D3;       /* Success, growth */
  --accent-yellow: #FFE66D;       /* Joy, energy */
  --accent-pink: #FF8B94;         /* Playful, fun */
  --accent-purple: #A8DADC;       /* Creative, calm */
  --success: #2ECC71;              /* Green - success */
  --warning: #F39C12;              /* Orange - warning */
  --error: #E74C3C;                /* Red - error */
  --neutral-dark: #2C3E50;        /* Text, headings */
  --neutral-light: #ECF0F1;       /* Backgrounds */
  --neutral-white: #FFFFFF;       /* Cards, surfaces */
"""
    
    # Add colors after existing :root variables
    if ':root' in css_content:
        # Find the end of :root block
        root_match = re.search(r'(:root\s*\{[^}]*\})', css_content, re.DOTALL)
        if root_match:
            root_end = root_match.end()
            # Check if colors already exist
            if '--primary-orange' not in css_content:
                css_content = css_content[:root_end-1] + new_colors + "\n" + css_content[root_end-1:]
                print("   ✅ Added kid-friendly color palette")
            else:
                print("   ⚠️  Colors already exist, skipping")
        else:
            print("   ⚠️  Could not find :root block")
    else:
        print("   ⚠️  No :root block found")
    
    return css_content

def improve_button_styles(css_content):
    """Improve button styles - bigger, colorful, kid-friendly."""
    print("\n📝 Improving button styles...")
    
    # Button improvements (Duolingo-style)
    button_improvements = """
/* ============================================
   KID-FRIENDLY BUTTONS (Duolingo-Inspired)
   ============================================ */

/* Primary Button - Big, colorful, obvious */
.button-primary,
.header-cta,
.books-card-button,
.contact-form-btn {
  background: var(--primary-orange, #FF6B35) !important;
  color: white !important;
  padding: 16px 32px !important;
  border-radius: 12px !important;
  font-size: 1.125rem !important;
  font-weight: 700 !important;
  border: none !important;
  cursor: pointer !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3) !important;
  min-height: 48px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
}

.button-primary:hover,
.header-cta:hover,
.books-card-button:hover,
.contact-form-btn:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 16px rgba(255, 107, 53, 0.4) !important;
}

.button-primary:active,
.header-cta:active,
.books-card-button:active,
.contact-form-btn:active {
  transform: translateY(0) !important;
}

/* Secondary Button */
.button-secondary,
.header-top-cta {
  background: var(--primary-blue, #4ECDC4) !important;
  color: white !important;
  padding: 14px 28px !important;
  border-radius: 12px !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
  border: none !important;
  cursor: pointer !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 4px 12px rgba(78, 205, 196, 0.3) !important;
  min-height: 44px !important;
}

.button-secondary:hover,
.header-top-cta:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 16px rgba(78, 205, 196, 0.4) !important;
}

/* Success Button (for celebrations) */
.button-success {
  background: var(--success, #2ECC71) !important;
  color: white !important;
  padding: 16px 32px !important;
  border-radius: 12px !important;
  font-size: 1.125rem !important;
  font-weight: 700 !important;
  border: none !important;
  cursor: pointer !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 4px 12px rgba(46, 204, 113, 0.3) !important;
  min-height: 48px !important;
}

/* All buttons - consistent spacing (8px grid) */
button,
a.button,
.books-card-button,
.header-cta,
.header-top-cta,
.contact-form-btn {
  margin: 8px !important;
  font-family: var(--montserrat-ff, 'Montserrat'), sans-serif !important;
}
"""
    
    # Check if button improvements already exist
    if 'KID-FRIENDLY BUTTONS' not in css_content:
        # Add at the end of file
        css_content += "\n" + button_improvements
        print("   ✅ Added kid-friendly button styles")
    else:
        print("   ⚠️  Button improvements already exist")
    
    return css_content

def add_progress_indicators(css_content):
    """Add progress indicators and gamification elements."""
    print("\n📝 Adding progress indicators...")
    
    progress_styles = """
/* ============================================
   PROGRESS INDICATORS (Duolingo-Inspired)
   ============================================ */

.progress-bar-container {
  width: 100%;
  background: var(--neutral-light, #ECF0F1);
  border-radius: 12px;
  height: 12px;
  overflow: hidden;
  margin: 16px 0;
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, var(--primary-orange, #FF6B35), var(--accent-yellow, #FFE66D));
  border-radius: 12px;
  transition: width 0.5s ease;
  box-shadow: 0 2px 4px rgba(255, 107, 53, 0.3);
}

.progress-text {
  font-size: 0.875rem;
  color: var(--neutral-dark, #2C3E50);
  margin-top: 8px;
  font-weight: 600;
}

/* Streak Counter */
.streak-counter {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--accent-yellow, #FFE66D);
  padding: 8px 16px;
  border-radius: 20px;
  font-weight: 700;
  color: var(--neutral-dark, #2C3E50);
  box-shadow: 0 2px 8px rgba(255, 230, 109, 0.3);
}

.streak-icon {
  font-size: 1.25rem;
}

/* Achievement Badge */
.achievement-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  background: var(--primary-green, #95E1D3);
  border-radius: 50%;
  font-size: 1.5rem;
  box-shadow: 0 4px 12px rgba(149, 225, 211, 0.3);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
}

/* Celebration Animation */
.celebration {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 9999;
  pointer-events: none;
}

.celebration-text {
  font-size: 3rem;
  font-weight: 800;
  color: var(--primary-orange, #FF6B35);
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  animation: celebrate 1s ease-out;
}

@keyframes celebrate {
  0% { transform: scale(0) rotate(0deg); opacity: 0; }
  50% { transform: scale(1.2) rotate(180deg); opacity: 1; }
  100% { transform: scale(1) rotate(360deg); opacity: 0; }
}
"""
    
    if 'PROGRESS INDICATORS' not in css_content:
        css_content += "\n" + progress_styles
        print("   ✅ Added progress indicators and gamification")
    else:
        print("   ⚠️  Progress indicators already exist")
    
    return css_content

def improve_typography(css_content):
    """Improve typography - better spacing, kid-friendly fonts."""
    print("\n📝 Improving typography...")
    
    typography_improvements = """
/* ============================================
   IMPROVED TYPOGRAPHY (Kid-Friendly)
   ============================================ */

/* Better line heights for readability */
h1, h2, h3, h4, h5, h6 {
  line-height: 1.3 !important;
  margin-bottom: 16px !important;
}

p {
  line-height: 1.6 !important;
  margin-bottom: 16px !important;
}

/* Friendly, encouraging language styling */
.encouraging-text {
  font-size: 1.125rem;
  color: var(--primary-orange, #FF6B35);
  font-weight: 600;
  text-align: center;
  padding: 16px;
  background: rgba(255, 107, 53, 0.1);
  border-radius: 8px;
  margin: 16px 0;
}

/* Better spacing (8px grid system) */
.books-card,
.about-card,
.contact-card {
  padding: 24px !important;
  margin: 16px 0 !important;
}

/* Consistent text alignment */
.books-card-text,
.about-text,
.contact-text {
  text-align: left !important;
  line-height: 1.6 !important;
}
"""
    
    if 'IMPROVED TYPOGRAPHY' not in css_content:
        css_content += "\n" + typography_improvements
        print("   ✅ Added typography improvements")
    else:
        print("   ⚠️  Typography improvements already exist")
    
    return css_content

def add_friendly_messages(html_content):
    """Add friendly, encouraging messages to HTML."""
    print("\n📝 Adding friendly messages...")
    
    # Check if encouraging messages already exist
    if 'encouraging-text' in html_content:
        print("   ⚠️  Friendly messages already exist")
        return html_content
    
    # Add encouraging message after books section
    books_section_pattern = r'(</section>\s*<!--\s*Books-Section\s*-->)'
    
    encouraging_html = """
    <!-- Encouraging Message (Kid-Friendly) -->
    <section class="encouraging-section" style="text-align: center; padding: 48px 16px; background: linear-gradient(135deg, rgba(255, 107, 53, 0.1), rgba(78, 205, 196, 0.1));">
      <div class="container">
        <p class="encouraging-text" style="font-size: 1.5rem; color: #FF6B35; font-weight: 700; margin-bottom: 16px;">
          🎉 You're doing amazing! 🎉
        </p>
        <p style="font-size: 1.125rem; color: #2C3E50; max-width: 600px; margin: 0 auto;">
          Keep going! Every step you take brings you closer to becoming a coding superstar! ⭐
        </p>
      </div>
    </section>
"""
    
    # Insert after books section
    if re.search(books_section_pattern, html_content):
        html_content = re.sub(
            books_section_pattern,
            r'\1' + encouraging_html,
            html_content
        )
        print("   ✅ Added encouraging message")
    else:
        print("   ⚠️  Could not find books section to add message")
    
    return html_content

def main():
    """Main improvement function."""
    print_header("UI/UX Improvement - Kid-Friendly Makeover")
    
    # Read files
    print("\n📖 Reading files...")
    try:
        with open(CSS_FILE, 'r', encoding='utf-8') as f:
            css_content = f.read()
        print(f"   ✅ Read CSS: {CSS_FILE}")
    except Exception as e:
        print(f"   ❌ Error reading CSS: {e}")
        return False
    
    try:
        with open(HTML_FILE, 'r', encoding='utf-8') as f:
            html_content = f.read()
        print(f"   ✅ Read HTML: {HTML_FILE}")
    except Exception as e:
        print(f"   ❌ Error reading HTML: {e}")
        return False
    
    # Apply improvements
    print("\n🎨 Applying improvements...")
    
    # 1. Add kid-friendly colors
    css_content = add_kid_friendly_colors(css_content)
    
    # 2. Improve button styles
    css_content = improve_button_styles(css_content)
    
    # 3. Add progress indicators
    css_content = add_progress_indicators(css_content)
    
    # 4. Improve typography
    css_content = improve_typography(css_content)
    
    # 5. Add friendly messages
    html_content = add_friendly_messages(html_content)
    
    # Save files
    print("\n💾 Saving files...")
    try:
        with open(CSS_FILE, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print(f"   ✅ Saved CSS: {CSS_FILE}")
    except Exception as e:
        print(f"   ❌ Error saving CSS: {e}")
        return False
    
    try:
        with open(HTML_FILE, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"   ✅ Saved HTML: {HTML_FILE}")
    except Exception as e:
        print(f"   ❌ Error saving HTML: {e}")
        return False
    
    # Summary
    print_header("Improvements Complete!")
    
    print("\n✅ What was improved:")
    print("   1. ✅ Kid-friendly color palette (Duolingo-inspired)")
    print("   2. ✅ Bigger, colorful buttons with hover effects")
    print("   3. ✅ Progress indicators and gamification elements")
    print("   4. ✅ Better typography and spacing")
    print("   5. ✅ Friendly, encouraging messages")
    
    print("\n🎯 Next steps:")
    print("   1. Test the website in browser")
    print("   2. Check button alignment and sizing")
    print("   3. Verify colors look playful and kid-friendly")
    print("   4. Test on mobile, tablet, desktop")
    
    print("\n💡 The UI/UX is now more kid-friendly and Duolingo-inspired!")
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


