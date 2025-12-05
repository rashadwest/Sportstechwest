#!/usr/bin/env python3
"""
Basic BallCODE Screenshot Analysis
Extracts metadata and identifies patterns without vision API
"""

import os
import json
from pathlib import Path
from PIL import Image
from collections import defaultdict
import re

def analyze_screenshot_folder(folder_path):
    """Analyze all images in folder and identify patterns"""
    
    folder = Path(folder_path)
    if not folder.exists():
        print(f"❌ Folder not found: {folder_path}")
        return None
    
    # Find all image files
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}
    images = sorted([
        f for f in folder.iterdir()
        if f.suffix.lower() in image_extensions
    ])
    
    if not images:
        print(f"⚠️  No image files found in {folder_path}")
        return None
    
    print(f"📁 Found {len(images)} images in {folder_path}\n")
    
    # Analyze each image
    results = []
    patterns = defaultdict(list)
    
    for img_path in images:
        try:
            # Get basic file info
            file_size = img_path.stat().st_size
            file_size_mb = file_size / (1024 * 1024)
            
            # Get image dimensions
            with Image.open(img_path) as img:
                width, height = img.size
                format_type = img.format
                mode = img.mode
            
            # Analyze filename patterns
            filename = img_path.name
            base_name = img_path.stem
            
            # Categorize by filename patterns
            category = categorize_image(filename)
            
            result = {
                "filename": filename,
                "path": str(img_path),
                "file_size_mb": round(file_size_mb, 2),
                "dimensions": {"width": width, "height": height},
                "format": format_type,
                "mode": mode,
                "category": category,
                "aspect_ratio": round(width / height, 2) if height > 0 else 0
            }
            
            results.append(result)
            patterns[category].append(filename)
            
            print(f"✅ {filename}: {width}x{height}, {file_size_mb:.2f}MB, Category: {category}")
            
        except Exception as e:
            print(f"❌ Error analyzing {img_path.name}: {e}")
            results.append({
                "filename": img_path.name,
                "error": str(e)
            })
    
    # Summary
    print(f"\n📊 ANALYSIS SUMMARY")
    print(f"=" * 50)
    print(f"Total Images: {len(results)}")
    print(f"\nCategories Found:")
    for category, files in sorted(patterns.items()):
        print(f"  - {category}: {len(files)} images")
    
    # Dimension analysis
    dimensions = [(r['dimensions']['width'], r['dimensions']['height']) for r in results if 'dimensions' in r]
    if dimensions:
        unique_dims = set(dimensions)
        print(f"\nUnique Dimensions: {len(unique_dims)}")
        dim_counts = defaultdict(int)
        for w, h in dimensions:
            dim_counts[f"{w}x{h}"] += 1
        for dim, count in sorted(dim_counts.items()):
            print(f"  - {dim}: {count} images")
    
    # File size analysis
    sizes = [r['file_size_mb'] for r in results if 'file_size_mb' in r]
    if sizes:
        print(f"\nFile Sizes:")
        print(f"  - Min: {min(sizes):.2f}MB")
        print(f"  - Max: {max(sizes):.2f}MB")
        print(f"  - Avg: {sum(sizes)/len(sizes):.2f}MB")
    
    return {
        "total_images": len(results),
        "categories": dict(patterns),
        "images": results
    }

def categorize_image(filename):
    """Categorize image based on filename patterns"""
    filename_lower = filename.lower()
    
    # Main menu and navigation
    if any(word in filename_lower for word in ['main menu', 'menu', 'section', 'settings', 'leaderboard', 'skins']):
        return "UI_Navigation"
    
    # Tutorial mode
    if 'tutorial' in filename_lower:
        if 'mode' in filename_lower or 'start' in filename_lower:
            return "Tutorial_Mode_Select"
        elif re.search(r'tutorial_\d+', filename_lower):
            match = re.search(r'tutorial_(\d+)', filename_lower)
            if match:
                return f"Tutorial_Level_{match.group(1)}"
        return "Tutorial"
    
    # Coding mode
    if 'coding' in filename_lower:
        if 'mode' in filename_lower:
            return "Coding_Mode_Select"
        elif 'gameplay' in filename_lower:
            return "Coding_Gameplay"
        return "Coding"
    
    # Mathlete mode
    if 'mathlete' in filename_lower:
        if 'mode' in filename_lower:
            return "Mathlete_Mode_Select"
        elif 'gameplay' in filename_lower:
            return "Mathlete_Gameplay"
        return "Mathlete"
    
    # Freeplay mode
    if 'freeplay' in filename_lower:
        if 'mode' in filename_lower:
            return "Freeplay_Mode_Select"
        elif 'gameplay' in filename_lower:
            return "Freeplay_Gameplay"
        return "Freeplay"
    
    # Chess mode
    if 'chess' in filename_lower:
        if any(word in filename_lower for word in ['choose', 'pick', 'player']):
            return "Chess_Player_Select"
        elif 'switch' in filename_lower:
            return "Chess_Switch"
        elif 'play' in filename_lower or 'gameplay' in filename_lower:
            return "Chess_Gameplay"
        return "Chess"
    
    return "Other"

if __name__ == "__main__":
    folder_path = "/Users/rashadwest/Desktop/BallCODE screenshots"
    
    print("🔍 Analyzing BallCODE Screenshots...")
    print("=" * 50)
    
    results = analyze_screenshot_folder(folder_path)
    
    if results:
        # Save results
        output_file = "ballcode_screenshots_metadata.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n💾 Results saved to: {output_file}")
        
        # Create organized summary
        summary_file = "BALLCODE-SCREENSHOTS-PATTERN-ANALYSIS.md"
        with open(summary_file, 'w') as f:
            f.write("# BallCODE Screenshots - Pattern Analysis\n\n")
            f.write("**Copyright © 2025 Rashad West. All Rights Reserved.**\n\n")
            f.write("**Generated:** Automated analysis of image metadata and patterns\n\n")
            f.write("---\n\n")
            f.write(f"## 📊 Summary\n\n")
            f.write(f"- **Total Images:** {results['total_images']}\n")
            f.write(f"- **Categories Found:** {len(results['categories'])}\n\n")
            f.write("## 📁 Images by Category\n\n")
            
            for category, files in sorted(results['categories'].items()):
                f.write(f"### {category} ({len(files)} images)\n\n")
                for filename in sorted(files):
                    # Find image details
                    img_data = next((r for r in results['images'] if r['filename'] == filename), None)
                    if img_data and 'dimensions' in img_data:
                        f.write(f"- `{filename}` - {img_data['dimensions']['width']}x{img_data['dimensions']['height']}, {img_data['file_size_mb']}MB\n")
                    else:
                        f.write(f"- `{filename}`\n")
                f.write("\n")
        
        print(f"📄 Summary saved to: {summary_file}")

