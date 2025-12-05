#!/usr/bin/env python3
"""
Automated Book Upload Script (Python Version)
Automates the process of adding a new book to the website

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import re
import shutil
import subprocess
from pathlib import Path

# Colors for terminal output
class Colors:
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    NC = '\033[0m'  # No Color

def print_success(message):
    print(f"{Colors.GREEN}✓{Colors.NC} {message}")

def print_info(message):
    print(f"{Colors.BLUE}{message}{Colors.NC}")

def print_error(message):
    print(f"{Colors.RED}Error: {message}{Colors.NC}")

def print_warning(message):
    print(f"{Colors.YELLOW}⚠{Colors.NC} {message}")

def update_index_html(book_number, book_title, description, gumroad_url, price, thumbnail_name):
    """Update index.html with new book card"""
    script_dir = Path(__file__).parent
    index_file = script_dir / "BallCode" / "index.html"
    
    if not index_file.exists():
        print_error(f"index.html not found at {index_file}")
        return False
    
    # Read current content
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create book card HTML
    book_card = f'''              <!-- Book {book_number}: {book_title} -->
              <div class="books-card">
                <div class="books-card-thumbnail">
                  <img src="/assets/images/{thumbnail_name}" alt="Book {book_number}: {book_title}" />
                  <span class="books-card-badge">Available</span>
                  <span class="books-card-play">▶</span>
                </div>
                <div class="books-card-content">
                  <div class="books-card-title-wrapper">
                    <img src="/assets/images/{thumbnail_name}" 
                         alt="Book {book_number}: {book_title}" 
                         class="books-card-title-image"
                         onerror="this.style.display='none'; this.nextElementSibling.style.display='block';" />
                    <h3 class="books-card-title books-card-title-fallback" style="display: none;">Book {book_number}: {book_title}</h3>
                  </div>
                  <p class="books-card-text">{description}</p>
                  
                  <div class="books-card-includes">
                    <p class="books-card-includes-title">📚 What's Included:</p>
                    <ul class="books-card-includes-list">
                      <li>Interactive video book</li>
                      <li>Game access password (instant delivery)</li>
                      <li>Curriculum level #{book_number} unlock</li>
                    </ul>
                  </div>
                  
                  <p class="books-card-price">${price}</p>
                  <a href="{gumroad_url}" target="_blank" class="books-card-button">Buy Book {book_number} →</a>
                  
                  <details class="books-card-access-info">
                    <summary class="books-card-access-summary">🎮 How to Access After Purchase</summary>
                    <div class="books-card-access-details">
                      <ol>
                        <li>Get password instantly on thank you page</li>
                        <li>Click "Access Game Now" (or go to ballcode.netlify.app)</li>
                        <li>Sign up or log in to the game</li>
                        <li>Navigate to: <strong>Ballcode mode → Curriculum → Play → #{book_number}</strong></li>
                        <li>Enter your password to unlock the level</li>
                      </ol>
                    </div>
                  </details>
                </div>
              </div>'''
    
    # Try to find and replace "Coming Soon" placeholder
    coming_soon_pattern = rf'(<!-- Book {book_number}:.*?Coming Soon.*?</div>\s*</div>)'
    match = re.search(coming_soon_pattern, content, re.DOTALL)
    
    if match:
        # Replace Coming Soon placeholder
        content = re.sub(coming_soon_pattern, book_card, content, flags=re.DOTALL)
        print_info(f"Replaced 'Coming Soon' placeholder for Book {book_number}")
    else:
        # Add new book card before closing books-grid div
        books_grid_pattern = r'(</div>\s*</div>\s*</section>)'
        replacement = f'{book_card}\n            \\1'
        content = re.sub(books_grid_pattern, replacement, content, flags=re.DOTALL)
        print_info(f"Added new book card for Book {book_number}")
    
    # Write updated content
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print_success(f"Updated {index_file}")
    return True

def copy_thumbnail(thumbnail_path, book_number):
    """Copy thumbnail image to website assets"""
    script_dir = Path(__file__).parent
    images_dir = script_dir / "BallCode" / "assets" / "images"
    thumbnail_name = f"book{book_number}-title-page.png"
    dest_path = images_dir / thumbnail_name
    
    # Create images directory if it doesn't exist
    images_dir.mkdir(parents=True, exist_ok=True)
    
    if thumbnail_path and Path(thumbnail_path).exists():
        shutil.copy2(thumbnail_path, dest_path)
        print_success(f"Copied thumbnail to {dest_path}")
        return thumbnail_name
    else:
        print_warning(f"No thumbnail provided or file not found. Using fallback image.")
        return thumbnail_name

def git_commit_and_push(book_number, book_title, website_dir):
    """Commit and push changes to git"""
    os.chdir(website_dir)
    
    # Check if git is initialized
    if not Path('.git').exists():
        print_warning("Git not initialized. Skipping git operations.")
        return False
    
    # Check for changes
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, check=True)
        if not result.stdout.strip():
            print_info("No changes to commit")
            return False
    except subprocess.CalledProcessError:
        print_warning("Could not check git status")
        return False
    
    # Stage changes
    try:
        subprocess.run(['git', 'add', 'index.html'], check=True)
        subprocess.run(['git', 'add', 'assets/images/'], check=True)
        print_info("Staged changes")
    except subprocess.CalledProcessError:
        print_warning("Could not stage changes")
        return False
    
    # Commit
    try:
        commit_message = f"Add Book {book_number}: {book_title} to website"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print_success("Changes committed")
        return True
    except subprocess.CalledProcessError:
        print_warning("Could not commit changes")
        return False

def main():
    """Main function"""
    print(f"{Colors.BLUE}=== BallCODE Book Upload Automation ==={Colors.NC}\n")
    
    # Parse arguments
    if len(sys.argv) < 5:
        print_error("Missing required parameters")
        print("Usage: python3 automate-book-upload.py <book-number> <book-title> <description> <gumroad-url> [thumbnail-path] [price]")
        print("\nExample:")
        print('python3 automate-book-upload.py 2 "The Code of Flow" "Learn if/then logic" "https://gumroad.com/l/xyz" "./book2.png" 5')
        sys.exit(1)
    
    book_number = sys.argv[1]
    book_title = sys.argv[2]
    description = sys.argv[3]
    gumroad_url = sys.argv[4]
    thumbnail_path = sys.argv[5] if len(sys.argv) > 5 else None
    price = sys.argv[6] if len(sys.argv) > 6 else "5"
    
    print_info(f"Book Number: {book_number}")
    print_info(f"Book Title: {book_title}")
    print_info(f"Gumroad URL: {gumroad_url}")
    print_info(f"Price: ${price}\n")
    
    # Step 1: Copy thumbnail
    print_info("Step 1: Copying thumbnail image...")
    thumbnail_name = copy_thumbnail(thumbnail_path, book_number)
    print()
    
    # Step 2: Update index.html
    print_info("Step 2: Updating website HTML...")
    if not update_index_html(book_number, book_title, description, gumroad_url, price, thumbnail_name):
        print_error("Failed to update index.html")
        sys.exit(1)
    print()
    
    # Step 3: Git operations
    script_dir = Path(__file__).parent
    website_dir = script_dir / "BallCode"
    
    print_info("Step 3: Git operations...")
    if git_commit_and_push(book_number, book_title, website_dir):
        print()
        print_info("Ready to push. Run manually:")
        print(f"  cd {website_dir}")
        print("  git push origin main")
    print()
    
    # Summary
    print(f"{Colors.GREEN}=== Upload Complete ==={Colors.NC}")
    print_info(f"Book {book_number}: {book_title}")
    print_info(f"Status: Available")
    print_info(f"Price: ${price}")
    print_info(f"Gumroad: {gumroad_url}")
    print()
    print_info("Next Steps:")
    print("1. Review changes: git diff")
    print("2. Push to GitHub: git push origin main")
    print("3. Verify on live site")
    print("4. Test purchase flow")

if __name__ == "__main__":
    main()


