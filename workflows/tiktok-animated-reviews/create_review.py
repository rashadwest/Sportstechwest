#!/usr/bin/env python3
"""
One-Command Review Creator - JAEDS Framework
Everything flows from a single prompt/command

Usage:
    python3 create_review.py "TikTok video URL or path" "What to say in the reaction"
    
Example:
    python3 create_review.py "https://tiktok.com/@user/video/123" "This is really cool tech for youth athletes!"
"""

import sys
import os
import argparse
import logging
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.pipeline.review_pipeline import ReviewPipeline
from src.utils.health_checker import HealthChecker
from src.utils.validator import Validator

logger = logging.getLogger(__name__)


def download_tiktok_video(url_or_path: str) -> str:
    """
    Download TikTok video if URL provided, or return path if file path.
    
    TODO: Implement TikTok downloader
    For now, assumes local file path.
    """
    # If it's a URL, download it
    if url_or_path.startswith(('http://', 'https://', 'www.')):
        # TODO: Use yt-dlp or similar to download
        logger.warning("⚠️  URL download not yet implemented - please provide local file path")
        logger.info("   You can download videos using: yt-dlp <url>")
        raise NotImplementedError("TikTok URL download not yet implemented - use local file path")
    
    # Otherwise, assume it's a file path
    if not Path(url_or_path).exists():
        raise FileNotFoundError(f"Video file not found: {url_or_path}")
    
    return url_or_path


def create_script_from_prompt(prompt: str, output_path: str) -> str:
    """
    Create reaction script from user prompt.
    
    For now, uses prompt directly as script.
    TODO: Could enhance with AI to expand prompt into full script.
    """
    script_path = Path(output_path)
    script_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(script_path, 'w') as f:
        f.write(prompt)
    
    return str(script_path)


def main():
    """Main function - everything flows from here."""
    parser = argparse.ArgumentParser(
        description="Create animated TikTok review from a single prompt",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # From local video file
  python3 create_review.py video.mp4 "This tech is amazing for youth athletes!"
  
  # With auto character selection
  python3 create_review.py video.mp4 "Robots are changing sports analytics" --auto
  
  # Specify character
  python3 create_review.py video.mp4 "Kids love this!" --character youth
        """
    )
    
    parser.add_argument(
        "video",
        help="TikTok video URL or local file path"
    )
    parser.add_argument(
        "prompt",
        help="What to say in the reaction (script text)"
    )
    parser.add_argument(
        "--config",
        default="config/my_config.json",
        help="Config file path (default: config/my_config.json)"
    )
    parser.add_argument(
        "--character",
        choices=['youth', 'adult', 'robot'],
        help="Character to use (default: auto-select based on prompt)"
    )
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Auto-select character based on prompt content"
    )
    parser.add_argument(
        "--output",
        help="Output video path (auto-generated if not provided)"
    )
    parser.add_argument(
        "--skip-health-check",
        action="store_true",
        help="Skip system health check"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose logging"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    print("\n" + "=" * 70)
    print("  🎬 ONE-COMMAND REVIEW CREATOR")
    print("=" * 70 + "\n")
    
    try:
        # Step 1: Get video file
        logger.info("📹 Step 1: Getting video...")
        video_path = download_tiktok_video(args.video)
        logger.info(f"   ✅ Video: {video_path}")
        
        # Step 2: Create script from prompt
        logger.info("📝 Step 2: Creating script from prompt...")
        script_path = create_script_from_prompt(
            args.prompt,
            "temp/script.txt"
        )
        logger.info(f"   ✅ Script created: {script_path}")
        
        # Step 3: Initialize pipeline
        logger.info("🤖 Step 3: Initializing pipeline...")
        pipeline = ReviewPipeline(
            config_path=args.config,
            skip_health_check=args.skip_health_check
        )
        
        # Step 4: Determine character
        character = None
        if args.character:
            character = args.character
            logger.info(f"   🎨 Using character: {character}")
        elif args.auto:
            character = pipeline.auto_select_character(script_path)
            logger.info(f"   🤖 Auto-selected character: {character}")
        else:
            # Default: auto-select
            character = pipeline.auto_select_character(script_path)
            logger.info(f"   🤖 Auto-selected character: {character}")
        
        # Step 5: Process video
        logger.info("🎬 Step 4: Processing video...")
        logger.info("   (This may take a few minutes...)")
        
        output_path = pipeline.process(
            tiktok_video_path=video_path,
            script_path=script_path,
            output_path=args.output,
            character=character
        )
        
        # Step 6: Done!
        print("\n" + "=" * 70)
        print("  ✅ SUCCESS!")
        print("=" * 70)
        print(f"\n📹 Your review video is ready:")
        print(f"   {output_path}\n")
        print("🎉 You can now upload it to TikTok, YouTube, or wherever you want!\n")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Cancelled by user")
        return 1
    except Exception as e:
        logger.error(f"\n❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

