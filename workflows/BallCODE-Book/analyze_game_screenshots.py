#!/usr/bin/env python3
"""
BallCODE Game Screenshot Analysis Tool
Uses vision API to describe game screenshots and understand level mechanics

AIMCODE Approach:
- Jobs: Simple, "it just works" solution
- Hassabis: Systematic analysis of all levels
- Resnick: Building understanding through analysis
- Reggio: Multiple ways to understand (visual + text)
- Zhang: Understanding game to build better stories
"""

import os
import json
import base64
from pathlib import Path
from typing import List, Dict, Optional
import argparse

# Try to import OpenAI (if available)
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("⚠️  OpenAI library not installed. Install with: pip install openai")

# Try to import Anthropic (if available)
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("⚠️  Anthropic library not installed. Install with: pip install anthropic")


class GameScreenshotAnalyzer:
    """Analyze BallCODE game screenshots using vision APIs"""
    
    def __init__(self, api_type: str = "openai", api_key: Optional[str] = None):
        """
        Initialize analyzer with API type and key
        
        Args:
            api_type: "openai" or "anthropic"
            api_key: API key (or set OPENAI_API_KEY or ANTHROPIC_API_KEY env var)
        """
        self.api_type = api_type
        self.api_key = api_key or os.getenv(f"{api_type.upper()}_API_KEY")
        
        if not self.api_key:
            raise ValueError(f"API key required. Set {api_type.upper()}_API_KEY env var or pass api_key parameter")
        
        if api_type == "openai" and not OPENAI_AVAILABLE:
            raise ImportError("OpenAI library not installed. Run: pip install openai")
        if api_type == "anthropic" and not ANTHROPIC_AVAILABLE:
            raise ImportError("Anthropic library not installed. Run: pip install anthropic")
    
    def encode_image(self, image_path: str) -> str:
        """Encode image to base64"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def analyze_screenshot(self, image_path: str, context: str = "") -> Dict:
        """
        Analyze a single screenshot
        
        Args:
            image_path: Path to screenshot
            context: Additional context about the screenshot
            
        Returns:
            Dictionary with analysis results
        """
        print(f"📸 Analyzing: {os.path.basename(image_path)}")
        
        # Encode image
        base64_image = self.encode_image(image_path)
        
        # Prepare prompt
        prompt = self._create_analysis_prompt(context)
        
        # Call appropriate API
        if self.api_type == "openai":
            return self._analyze_with_openai(base64_image, prompt, image_path)
        elif self.api_type == "anthropic":
            return self._analyze_with_anthropic(base64_image, prompt, image_path)
    
    def _create_analysis_prompt(self, context: str) -> str:
        """Create detailed prompt for game screenshot analysis"""
        return f"""Analyze this BallCODE game screenshot in detail. 

BallCODE is a puzzle-based programming game (similar to LightBot) that teaches coding through basketball using a Scratch-style block coding system.

**Core Gameplay:** Like LightBot, players solve puzzles by arranging command blocks in sequence. Instead of a robot moving through a maze, players control a basketball player on a court. Each level is a puzzle with a specific basketball objective (score, pass sequence, defense rotation, etc.).

Key elements to identify and describe:

1. **Puzzle Structure** (Like LightBot):
   - What's the basketball goal/objective? (e.g., "Score from 3 positions", "Complete pass sequence")
   - What's the starting position? (Player location on court)
   - What constraints exist? (Defenders, court boundaries, shot clock, etc.)
   - What's the puzzle challenge?

2. **UI Elements**: 
   - Basketball court (with grid overlay if visible) - the "maze" where player moves
   - Block coding area (top right corner) - where blocks are arranged
   - Generated code display (below block code) - shows code equivalent
   - Navigation buttons (House/menu, Reverse/back, Delete)
   - Magnifying glass (video playback viewer)
   - Dribble tree system
   - Execute/Play button (to run the sequence)
   - Reset/Clear button

3. **Block Types Visible** (Command Palette):
   - START block (begin sequence)
   - DRIBBLE blocks (with clock timing if visible) - actions like move, pass, dribble
   - BUCKET block (shoot/complete)
   - Procedure blocks (reusable sequences, like LightBot's P1, P2)
   - Loop blocks (REPEAT X TIMES)
   - Conditional blocks (IF/THEN/ELSE)

4. **Current Solution** (Arranged Blocks):
   - What blocks are currently arranged in the sequence?
   - What order are they in?
   - Are there procedures defined?
   - Is the solution complete or partial?

5. **Game State**:
   - Is the sequence running? (Player executing blocks on court)
   - Is it paused/stopped?
   - Success state? (Goal achieved - basket scored, play completed)
   - Failure state? (Wrong sequence, timing off, error message)
   - What's happening on the court? (Player position, movements, animations)

6. **Learning Concept** (What's being taught):
   - Sequencing? (Simple block order)
   - Procedures? (Reusable sequences)
   - Loops? (Repetition)
   - Conditionals? (Decision making)
   - Combination? (Multiple concepts)

7. **Progression Indicators**:
   - Level name/number
   - Difficulty level
   - Instructions or guidance text
   - Progress indicators
   - Available blocks in palette (what player can use)

{context if context else ""}

Provide a detailed, structured description that will help understand:
- What puzzle is this level? (What basketball objective needs to be solved?)
- How does the puzzle work? (What's the challenge, constraints, goal?)
- What blocks are available? (Command palette)
- What's the current solution attempt? (Blocks arranged)
- What coding concept is being taught? (Sequencing, procedures, loops, conditionals)
- How does this fit into the learning progression? (Difficulty, what comes before/after)
- Is this similar to a LightBot level? (If so, which type?)
"""
    
    def _analyze_with_openai(self, base64_image: str, prompt: str, image_path: str) -> Dict:
        """Analyze using OpenAI GPT-4 Vision"""
        client = openai.OpenAI(api_key=self.api_key)
        
        response = client.chat.completions.create(
            model="gpt-4o",  # or "gpt-4-turbo" for vision
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1000
        )
        
        description = response.choices[0].message.content
        
        return {
            "image_path": image_path,
            "description": description,
            "api_type": "openai",
            "model": "gpt-4o"
        }
    
    def _analyze_with_anthropic(self, base64_image: str, prompt: str, image_path: str) -> Dict:
        """Analyze using Anthropic Claude Vision"""
        client = anthropic.Anthropic(api_key=self.api_key)
        
        # Read image data
        with open(image_path, "rb") as f:
            image_data = f.read()
        
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",  # or "claude-3-opus-20240229"
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": base64_image
                            }
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )
        
        description = message.content[0].text
        
        return {
            "image_path": image_path,
            "description": description,
            "api_type": "anthropic",
            "model": "claude-3-5-sonnet"
        }
    
    def analyze_directory(self, directory: str, output_file: Optional[str] = None) -> List[Dict]:
        """
        Analyze all screenshots in a directory
        
        Args:
            directory: Directory containing screenshots
            output_file: Optional JSON file to save results
            
        Returns:
            List of analysis results
        """
        screenshot_dir = Path(directory)
        if not screenshot_dir.exists():
            raise FileNotFoundError(f"Directory not found: {directory}")
        
        # Find all image files
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}
        screenshots = sorted([
            f for f in screenshot_dir.iterdir()
            if f.suffix.lower() in image_extensions
        ])
        
        if not screenshots:
            print(f"⚠️  No image files found in {directory}")
            return []
        
        print(f"📁 Found {len(screenshots)} screenshots in {directory}")
        print(f"🔍 Starting analysis...\n")
        
        results = []
        for i, screenshot in enumerate(screenshots, 1):
            print(f"[{i}/{len(screenshots)}] ", end="")
            try:
                result = self.analyze_screenshot(str(screenshot))
                results.append(result)
                print("✅ Complete\n")
            except Exception as e:
                print(f"❌ Error: {e}\n")
                results.append({
                    "image_path": str(screenshot),
                    "error": str(e)
                })
        
        # Save results if output file specified
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"💾 Results saved to: {output_file}")
        
        return results


def main():
    """Main function for command-line usage"""
    parser = argparse.ArgumentParser(
        description="Analyze BallCODE game screenshots using vision APIs"
    )
    parser.add_argument(
        "directory",
        help="Directory containing screenshots to analyze"
    )
    parser.add_argument(
        "--api",
        choices=["openai", "anthropic"],
        default="openai",
        help="Vision API to use (default: openai)"
    )
    parser.add_argument(
        "--output",
        help="Output JSON file for results (default: analysis_results.json)"
    )
    parser.add_argument(
        "--api-key",
        help="API key (or set OPENAI_API_KEY/ANTHROPIC_API_KEY env var)"
    )
    
    args = parser.parse_args()
    
    # Set default output file
    output_file = args.output or "analysis_results.json"
    
    try:
        # Initialize analyzer
        analyzer = GameScreenshotAnalyzer(
            api_type=args.api,
            api_key=args.api_key
        )
        
        # Analyze directory
        results = analyzer.analyze_directory(args.directory, output_file)
        
        print(f"\n✅ Analysis complete! Analyzed {len(results)} screenshots")
        print(f"📄 Results saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())

