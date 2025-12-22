#!/usr/bin/env python3
"""
Create Soccer Routes - Automated Infrastructure Setup
Creates /soccer route structure on ballcode.co website
"""

import os
import json
import shutil
from pathlib import Path

# Paths
BALLCODE_DIR = Path(__file__).parent.parent / "BallCode"
SOCCER_DIR = BALLCODE_DIR / "soccer"
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"

def create_soccer_directory_structure():
    """Create soccer directory structure"""
    directories = [
        SOCCER_DIR,
        SOCCER_DIR / "books",
        SOCCER_DIR / "assets",
        SOCCER_DIR / "css",
        SOCCER_DIR / "js",
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {directory}")

def create_soccer_index():
    """Create soccer landing page (Coming Soon)"""
    index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soccer Version - Coming Soon | BallCODE</title>
    <link rel="stylesheet" href="/css/main.css">
    <style>
        .world-cup-countdown {
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, #1a5f1a 0%, #2d8f2d 100%);
            color: white;
            margin: 2rem 0;
            border-radius: 8px;
        }
        .countdown-timer {
            font-size: 2rem;
            font-weight: bold;
            margin: 1rem 0;
        }
        .coming-soon-content {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        .email-capture {
            margin: 2rem 0;
            padding: 1.5rem;
            background: #f5f5f5;
            border-radius: 8px;
        }
        .email-capture input {
            padding: 0.75rem;
            width: 300px;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin-right: 0.5rem;
        }
        .email-capture button {
            padding: 0.75rem 1.5rem;
            background: #1a5f1a;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="coming-soon-content">
        <h1>⚽ Soccer Version - Coming Soon!</h1>
        <p>Get ready for World Cup 2026! We're building a soccer version of BallCODE that teaches coding through soccer skills.</p>
        
        <div class="world-cup-countdown">
            <h2>World Cup 2026 Countdown</h2>
            <div class="countdown-timer" id="countdown">Loading...</div>
            <p>June - July 2026 | United States, Mexico, Canada</p>
        </div>
        
        <div class="email-capture">
            <h3>Get Early Access</h3>
            <p>Be the first to know when the soccer version launches!</p>
            <form id="early-access-form">
                <input type="email" placeholder="Enter your email" required>
                <button type="submit">Sign Up</button>
            </form>
        </div>
        
        <h2>What to Expect</h2>
        <ul>
            <li>✅ Learn coding through soccer skills (dribbling, passing, shooting)</li>
            <li>✅ World Cup 2026 themed content</li>
            <li>✅ Same proven framework as basketball version</li>
            <li>✅ Enhanced 2.0 experience</li>
        </ul>
        
        <p><a href="/">← Back to Basketball Version</a></p>
    </div>
    
    <script>
        // World Cup 2026 Countdown
        const worldCupDate = new Date('2026-06-11T00:00:00');
        
        function updateCountdown() {
            const now = new Date();
            const diff = worldCupDate - now;
            
            if (diff <= 0) {
                document.getElementById('countdown').textContent = 'World Cup 2026 is here!';
                return;
            }
            
            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            
            document.getElementById('countdown').textContent = 
                `${days} days, ${hours} hours, ${minutes} minutes`;
        }
        
        updateCountdown();
        setInterval(updateCountdown, 60000); // Update every minute
        
        // Email capture form
        document.getElementById('early-access-form').addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            // TODO: Integrate with email capture system
            alert('Thanks for signing up! We\'ll notify you when the soccer version launches.');
            this.reset();
        });
    </script>
</body>
</html>"""
    
    index_file = SOCCER_DIR / "index.html"
    index_file.write_text(index_content)
    print(f"✅ Created: {index_file}")

def create_book_template(book_number, book_title, book_slug):
    """Create book page template"""
    book_dir = SOCCER_DIR / "books" / book_slug
    book_dir.mkdir(parents=True, exist_ok=True)
    
    book_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{book_title} | BallCODE Soccer</title>
    <link rel="stylesheet" href="/css/main.css">
</head>
<body>
    <div class="book-page">
        <h1>Book {book_number}: {book_title}</h1>
        <p class="coming-soon-badge">Coming Soon - March 2026</p>
        
        <div class="book-content">
            <p>This book is currently in development. Check back in March 2026!</p>
            <p><a href="/soccer/">← Back to Soccer Home</a></p>
        </div>
    </div>
</body>
</html>"""
    
    index_file = book_dir / "index.html"
    index_file.write_text(book_content)
    print(f"✅ Created: {index_file}")

def create_soccer_books():
    """Create placeholder pages for Books 1-3"""
    books = [
        (1, "The Foundation Pass", "book-1-foundation-pass"),
        (2, "The Code of Flow", "book-2-code-of-flow"),
        (3, "The Pattern", "book-3-pattern"),
    ]
    
    for book_num, title, slug in books:
        create_book_template(book_num, title, slug)

def update_main_navigation():
    """Update main site navigation to include soccer link"""
    # This would update the main site's navigation
    # Implementation depends on site structure
    print("ℹ️  Note: Update main navigation manually to include /soccer link")

def main():
    """Main execution"""
    print("🚀 Creating Soccer Route Structure...")
    print("=" * 50)
    
    create_soccer_directory_structure()
    create_soccer_index()
    create_soccer_books()
    update_main_navigation()
    
    print("=" * 50)
    print("✅ Soccer route structure created!")
    print(f"📁 Location: {SOCCER_DIR}")
    print("\nNext steps:")
    print("1. Review and customize index.html")
    print("2. Update main site navigation")
    print("3. Deploy to ballcode.co")

if __name__ == "__main__":
    main()

