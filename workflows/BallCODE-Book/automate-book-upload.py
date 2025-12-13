#!/usr/bin/env python3
"""
Automated Book Upload Script (Python Version)
Automates the process of adding a new book to the website

Copyright © 2025 Rashad West. All Rights Reserved.
"""

import os
import sys
import re
import json
import argparse
import shutil
import subprocess
from pathlib import Path
from typing import List

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

def _resolve_optional_path(path_value, base_dir: Path) -> str:
    """Resolve a possibly-relative path string against base_dir."""
    if not path_value:
        return ""
    p = Path(path_value)
    if p.is_absolute():
        return str(p)
    return str((base_dir / p).resolve())

def load_book_packet(packet_path: str) -> dict:
    """Load a book packet JSON file."""
    if not packet_path:
        raise ValueError("packet_path is required")
    p = Path(packet_path)
    if not p.exists():
        raise FileNotFoundError(f"Book packet not found: {p}")
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Book packet JSON must be an object")
    return data

def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Automate adding a new BallCODE book to the website."
    )
    parser.add_argument(
        "--packet",
        help="Path to BOOK-PACKET JSON (see documents/BOOK-PACKET-TEMPLATE.json).",
    )

    # Back-compat positional arguments
    parser.add_argument("book_number", nargs="?", help="Book number (e.g. 2)")
    parser.add_argument("book_title", nargs="?", help="Book title (e.g. 'The Code of Flow')")
    parser.add_argument("description", nargs="?", help="Short description")
    parser.add_argument("gumroad_url", nargs="?", help="Purchase URL (Gumroad or other)")
    parser.add_argument("thumbnail_path", nargs="?", help="Optional thumbnail path")
    parser.add_argument("price", nargs="?", help="Optional price (default: 5)")
    return parser.parse_args(argv)

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
    
    args = parse_args(sys.argv[1:])
    script_dir = Path(__file__).parent

    if args.packet:
        try:
            packet = load_book_packet(args.packet)
        except Exception as e:
            print_error(str(e))
            sys.exit(1)

        book = packet.get("book", {}) if isinstance(packet.get("book"), dict) else {}
        commerce = packet.get("commerce", {}) if isinstance(packet.get("commerce"), dict) else {}
        consumer = commerce.get("consumer", {}) if isinstance(commerce.get("consumer"), dict) else {}
        assets = packet.get("assets", {}) if isinstance(packet.get("assets"), dict) else {}

        book_number = str(book.get("book_number", "")).strip()
        book_title = str(book.get("title", "")).strip()
        description = str(book.get("description", "")).strip()
        gumroad_url = str(consumer.get("purchase_url", "")).strip()
        thumbnail_path = _resolve_optional_path(assets.get("thumbnail_path", ""), script_dir)
        price = str(consumer.get("price_usd", "5")).strip() or "5"
    else:
        # Parse arguments (legacy mode)
        if not all([args.book_number, args.book_title, args.description, args.gumroad_url]):
            print_error("Missing required parameters")
            print("Usage:")
            print("  python3 automate-book-upload.py --packet documents/BOOK-PACKET-TEMPLATE.json")
            print("  OR")
            print("  python3 automate-book-upload.py <book-number> <book-title> <description> <gumroad-url> [thumbnail-path] [price]")
            print("\nExample:")
            print('  python3 automate-book-upload.py 2 "The Code of Flow" "Learn if/then logic" "https://gumroad.com/l/xyz" "./book2.png" 5')
            sys.exit(1)

        book_number = args.book_number
        book_title = args.book_title
        description = args.description
        gumroad_url = args.gumroad_url
        thumbnail_path = args.thumbnail_path
        price = args.price if args.price else "5"
    
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


