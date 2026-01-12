"""
TikTok Animated Review Pipeline - JAEDS Framework

This pipeline automates the creation of TikTok reaction videos with:
1. Animated character overlay
2. Voice synthesis (your voice)
3. Video composition
4. Lip-sync and timing

JAEDS = Jobs + Alpha Evolve + Demis + Superhero CV
"""

import os
import sys
import json
import logging
from pathlib import Path
from typing import Dict, Optional, Tuple
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from src.animation.character_animator import CharacterAnimator
from src.animation.lip_sync import LipSyncSystem
from src.voice.voice_synthesizer import VoiceSynthesizer
from src.composition.video_composer import VideoComposer
from src.composition.sync_manager import SyncManager
from src.utils.health_checker import HealthChecker
from src.utils.validator import Validator

logger = logging.getLogger(__name__)


class ReviewPipeline:
    """
    Main pipeline for creating animated TikTok reviews.
    
    JAEDS Principles:
    - Jobs: Simple, one-command execution
    - Alpha Evolve: Rapid iteration and testing
    - Demis: Research-backed implementation
    - Superhero CV: PhD-level video processing
    """
    
    def __init__(self, config_path: Optional[str] = None, skip_health_check: bool = False):
        """Initialize the review pipeline."""
        self.config = self._load_config(config_path)
        self.config_path = config_path
        self.output_dir = Path(self.config.get('output_dir', 'output/reviews'))
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize components (character animator will be set per character)
        self.character_animator = None  # Will be set when character is selected
        self.voice_synthesizer = VoiceSynthesizer(self.config.get('voice', {}))
        self.video_composer = VideoComposer(self.config.get('composition', {}))
        self.lip_sync = LipSyncSystem(self.config.get('lip_sync', {}))
        self.sync_manager = SyncManager()
        self.health_checker = HealthChecker()
        self.validator = Validator()
        
        # Run health check unless skipped
        if not skip_health_check:
            self._run_health_check()
        
        logger.info("✅ Review Pipeline initialized")
    
    def _run_health_check(self):
        """Run health check on initialization."""
        logger.info("🔍 Running system health check...")
        report = self.health_checker.run_all_checks(config_path=self.config_path)
        
        if report["overall"] == "unhealthy":
            logger.error("❌ System health check failed - critical issues found")
            for check_name, check_result in report["checks"].items():
                if check_result["status"] == "error":
                    logger.error(f"  ❌ {check_name}: {check_result['message']}")
            raise Exception("System health check failed - please fix issues before proceeding")
        elif report["overall"] == "degraded":
            logger.warning("⚠️  System health check shows warnings")
            for check_name, check_result in report["checks"].items():
                if check_result["status"] == "warning":
                    logger.warning(f"  ⚠️  {check_name}: {check_result['message']}")
        else:
            logger.info("✅ System health check passed")
    
    def _load_config(self, config_path: Optional[str]) -> Dict:
        """Load configuration from file or use defaults."""
        if config_path and Path(config_path).exists():
            with open(config_path, 'r') as f:
                return json.load(f)
        
        # Default config
        default_config_path = Path(__file__).parent.parent.parent / 'config' / 'default_config.json'
        if default_config_path.exists():
            with open(default_config_path, 'r') as f:
                return json.load(f)
        
        # Minimal default config
        return {
            'output_dir': 'output/reviews',
            'character': {},
            'voice': {},
            'composition': {},
            'lip_sync': {}
        }
    
    def auto_select_character(self, script_path: str, content_type: Optional[str] = None) -> str:
        """
        Auto-select character based on script content or content type.
        
        Args:
            script_path: Path to script file
            content_type: Optional content type hint ('youth', 'robot', 'adult')
        
        Returns:
            Character name ('youth', 'adult', or 'robot')
        """
        # If content type provided, use it
        if content_type:
            if content_type.lower() in ['youth', 'kid', 'student', 'young', 'teen']:
                return 'youth'
            elif content_type.lower() in ['robot', 'robotics', 'ai', 'automation', 'machine']:
                return 'robot'
            else:
                return 'adult'
        
        # Otherwise, analyze script text
        with open(script_path, 'r') as f:
            script_text = f.read().lower()
        
        return self.auto_select_character_from_text(script_text)
    
    def auto_select_character_from_text(self, script_text: str) -> str:
        """
        Auto-select character based on script text content.
        
        Args:
            script_text: Script text to analyze
        
        Returns:
            Character name ('youth', 'adult', or 'robot')
        """
        script_text = script_text.lower()
        
        character_selection = self.config.get('character_selection', {})
        youth_keywords = character_selection.get('youth_keywords', ['youth', 'kid', 'student', 'young', 'teen'])
        robot_keywords = character_selection.get('robot_keywords', ['robot', 'robotics', 'ai', 'automation', 'machine'])
        
        # Count keyword matches
        youth_count = sum(1 for keyword in youth_keywords if keyword in script_text)
        robot_count = sum(1 for keyword in robot_keywords if keyword in script_text)
        
        # Select character based on keyword matches
        if youth_count > robot_count and youth_count > 0:
            return 'youth'
        elif robot_count > youth_count and robot_count > 0:
            return 'robot'
        else:
            return 'adult'  # Default to adult
    
    def process(
        self,
        tiktok_video_path: str,
        script_path: str,
        output_path: Optional[str] = None,
        character: Optional[str] = None
    ) -> str:
        """
        Process a TikTok video with animated character and voice.
        
        Args:
            tiktok_video_path: Path to TikTok video file
            script_path: Path to reaction script text file
            output_path: Optional output path (auto-generated if not provided)
            character: Character to use ('youth', 'adult', 'robot') or None for auto-select
        
        Returns:
            Path to generated video file
        """
        logger.info("=" * 70)
        logger.info("🎬 PROCESSING ANIMATED REVIEW")
        logger.info("=" * 70)
        
        # Auto-select character if not provided
        if not character:
            character = self.auto_select_character(script_path)
            logger.info(f"🤖 Auto-selected character: {character}")
        else:
            logger.info(f"🎨 Using character: {character}")
        
        # Get character configuration
        characters_config = self.config.get('characters', {})
        if character not in characters_config:
            logger.warning(f"⚠️  Character '{character}' not found in config, using 'adult'")
            character = 'adult'
        
        character_config = characters_config[character]
        logger.info(f"📁 Character file: {character_config.get('file_path')}")
        
        # Update character animator with selected character
        self.character_animator = CharacterAnimator(character_config)
        
        # Validate inputs
        logger.info("🔍 Validating inputs...")
        is_valid, errors = self.validator.validate_all(
            config_path=self.config_path,
            video_path=tiktok_video_path,
            script_path=script_path,
            character_paths={k: v.get("file_path") for k, v in character_config.items() if v.get("file_path")}
        )
        
        if not is_valid:
            error_msg = "Validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
            logger.error(f"❌ {error_msg}")
            raise ValueError(error_msg)
        
        logger.info("✅ Input validation passed")
        
        # Load script
        with open(script_path, 'r') as f:
            script_text = f.read()
        
        # Generate output path if not provided
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            video_name = Path(tiktok_video_path).stem
            output_path = str(self.output_dir / f"review_{character}_{video_name}_{timestamp}.mp4")
        
        logger.info(f"📹 TikTok Video: {tiktok_video_path}")
        logger.info(f"📝 Script: {script_path}")
        logger.info(f"🎯 Output: {output_path}")
        
        # Step 1: Generate voice audio
        logger.info("\n🎤 Step 1: Generating voice audio...")
        audio_path = self._generate_voice(script_text, output_path)
        logger.info(f"✅ Voice audio generated: {audio_path}")
        
        # Step 2: Generate character animation
        logger.info("\n🎨 Step 2: Generating character animation...")
        animation_path = self._generate_animation(script_text, audio_path, output_path)
        logger.info(f"✅ Character animation generated: {animation_path}")
        
        # Step 3: Sync animation with audio (lip-sync)
        logger.info("\n👄 Step 3: Syncing lip-sync...")
        synced_animation_path = self._sync_lip_sync(animation_path, audio_path, output_path)
        logger.info(f"✅ Lip-sync complete: {synced_animation_path}")
        
        # Step 4: Compose final video
        logger.info("\n🎬 Step 4: Composing final video...")
        final_video_path = self._compose_video(
            tiktok_video_path,
            synced_animation_path,
            audio_path,
            output_path
        )
        logger.info(f"✅ Final video composed: {final_video_path}")
        
        logger.info("=" * 70)
        logger.info("✅ PROCESSING COMPLETE")
        logger.info("=" * 70)
        logger.info(f"📹 Output: {final_video_path}")
        
        return final_video_path
    
    def _generate_voice(self, script_text: str, output_base: str) -> str:
        """Generate voice audio from script."""
        audio_path = str(Path(output_base).with_suffix('.mp3'))
        self.voice_synthesizer.synthesize(script_text, audio_path)
        return audio_path
    
    def _generate_animation(self, script_text: str, audio_path: str, output_base: str) -> str:
        """Generate character animation from script and audio."""
        animation_path = str(Path(output_base).with_suffix('.animation.mp4'))
        self.character_animator.animate(script_text, audio_path, animation_path)
        return animation_path
    
    def _sync_lip_sync(self, animation_path: str, audio_path: str, output_base: str) -> str:
        """Apply lip-sync to animation."""
        synced_path = str(Path(output_base).with_suffix('.synced.mp4'))
        self.lip_sync.sync(animation_path, audio_path, synced_path)
        return synced_path
    
    def _compose_video(
        self,
        tiktok_video_path: str,
        character_animation_path: str,
        audio_path: str,
        output_path: str
    ) -> str:
        """Compose final video with TikTok video + character + audio."""
        self.video_composer.compose(
            tiktok_video_path,
            character_animation_path,
            audio_path,
            output_path
        )
        return output_path


def main():
    """Main function for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description="TikTok Animated Review Pipeline")
    parser.add_argument("--tiktok-video", required=True, help="Path to TikTok video")
    parser.add_argument("--script", required=True, help="Path to reaction script")
    parser.add_argument("--output", help="Output video path (auto-generated if not provided)")
    parser.add_argument("--config", help="Path to configuration file")
    parser.add_argument("--character", choices=['youth', 'adult', 'robot'], help="Character to use (youth/adult/robot)")
    parser.add_argument("--auto-select-character", action="store_true", help="Auto-select character based on script content")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create pipeline
    pipeline = ReviewPipeline(config_path=args.config)
    
    # Determine character
    character = None
    if args.auto_select_character:
        character = pipeline.auto_select_character(args.script)
        print(f"🤖 Auto-selected character: {character}")
    elif args.character:
        character = args.character
    
    # Process video
    output_path = pipeline.process(
        args.tiktok_video,
        args.script,
        args.output,
        character=character
    )
    
    print(f"\n✅ Review video generated: {output_path}")


if __name__ == "__main__":
    main()

