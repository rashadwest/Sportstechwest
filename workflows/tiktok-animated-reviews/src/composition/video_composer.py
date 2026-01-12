"""
Video Composition System - JAEDS Framework

Composes final video by combining TikTok video + animated character + voice audio.
Handles layout, positioning, and synchronization.

JAEDS Principles:
- Jobs: Clean, professional composition
- Alpha Evolve: Rapid testing of layouts
- Demis: Research-backed composition techniques
- Superhero CV: Video processing algorithms
"""

import logging
from typing import Dict, Optional
from pathlib import Path

logger = logging.getLogger(__name__)


class VideoComposer:
    """
    Video composition system for combining multiple video sources.
    
    Layouts:
    - side_by_side: TikTok video on left, character on right
    - picture_in_picture: Character overlay on TikTok video
    - split_screen: Equal split between TikTok and character
    - custom: User-defined layout
    """
    
    def __init__(self, config: Dict):
        """Initialize video composer with configuration."""
        self.config = config
        self.layout = config.get('layout', 'side_by_side')
        self.character_position = config.get('character_position', 'right')
        self.character_size = config.get('character_size', '40%')
        self.output_config = config.get('output', {})
        
        logger.info(f"✅ Video Composer initialized (layout: {self.layout})")
    
    def compose(
        self,
        tiktok_video_path: str,
        character_video_path: str,
        audio_path: str,
        output_path: str
    ) -> str:
        """
        Compose final video from TikTok video, character, and audio.
        
        Args:
            tiktok_video_path: Path to TikTok source video
            character_video_path: Path to character animation video
            audio_path: Path to voice audio file
            output_path: Path to save final composed video
        
        Returns:
            Path to composed video
        """
        logger.info(f"🎬 Composing final video...")
        logger.debug(f"   TikTok video: {tiktok_video_path}")
        logger.debug(f"   Character video: {character_video_path}")
        logger.debug(f"   Audio: {audio_path}")
        logger.debug(f"   Layout: {self.layout}")
        
        # Ensure output directory exists
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Compose based on layout
        if self.layout == 'side_by_side':
            final_video = self._compose_side_by_side(
                tiktok_video_path,
                character_video_path,
                audio_path
            )
        elif self.layout == 'picture_in_picture':
            final_video = self._compose_picture_in_picture(
                tiktok_video_path,
                character_video_path,
                audio_path
            )
        elif self.layout == 'split_screen':
            final_video = self._compose_split_screen(
                tiktok_video_path,
                character_video_path,
                audio_path
            )
        else:
            raise ValueError(f"Unknown layout: {self.layout}")
        
        # Write final video
        final_video.write_videofile(
            str(output_path),
            codec='libx264',
            audio_codec='aac',
            fps=self.output_config.get('fps', 30),
            preset='medium'
        )
        
        # Clean up
        final_video.close()
        
        logger.info(f"✅ Final video composed: {output_path}")
        return str(output_path)
    
    def _compose_side_by_side(
        self,
        tiktok_video_path: str,
        character_video_path: str,
        audio_path: str
    ):
        """Compose side-by-side layout."""
        from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
        
        # Load videos
        tiktok_video = VideoFileClip(tiktok_video_path)
        character_video = VideoFileClip(character_video_path)
        audio = AudioFileClip(audio_path)
        
        # Get target resolution (TikTok format: 1080x1920)
        target_width = self.output_config.get('width', 1080)
        target_height = self.output_config.get('height', 1920)
        
        # Resize videos to fit side-by-side
        # TikTok video takes 60% of width, character takes 40%
        tiktok_width = int(target_width * 0.6)
        character_width = int(target_width * 0.4)
        
        # Resize TikTok video
        tiktok_video = tiktok_video.resize(width=tiktok_width)
        tiktok_video = tiktok_video.set_position(('left', 'center'))
        
        # Resize character video
        character_video = character_video.resize(width=character_width)
        character_video = character_video.set_position((tiktok_width, 'center'))
        
        # Create composite
        final_video = CompositeVideoClip(
            [tiktok_video, character_video],
            size=(target_width, target_height)
        )
        
        # Set audio
        final_video = final_video.set_audio(audio)
        
        # Set duration to match audio
        final_video = final_video.set_duration(audio.duration)
        
        # Clean up
        tiktok_video.close()
        character_video.close()
        audio.close()
        
        return final_video
    
    def _compose_picture_in_picture(
        self,
        tiktok_video_path: str,
        character_video_path: str,
        audio_path: str
    ):
        """Compose picture-in-picture layout."""
        from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
        
        # Load videos
        tiktok_video = VideoFileClip(tiktok_video_path)
        character_video = VideoFileClip(character_video_path)
        audio = AudioFileClip(audio_path)
        
        # Get target resolution
        target_width = self.output_config.get('width', 1080)
        target_height = self.output_config.get('height', 1920)
        
        # Resize TikTok video to full size
        tiktok_video = tiktok_video.resize((target_width, target_height))
        tiktok_video = tiktok_video.set_position(('center', 'center'))
        
        # Resize character video (smaller, overlay)
        character_size = self._parse_size(self.character_size, target_width)
        character_video = character_video.resize(width=character_size)
        
        # Position character (default: bottom-right)
        if self.character_position == 'right':
            position = (target_width - character_size - 20, target_height - character_size - 20)
        elif self.character_position == 'left':
            position = (20, target_height - character_size - 20)
        elif self.character_position == 'center':
            position = ('center', target_height - character_size - 20)
        else:
            position = (target_width - character_size - 20, target_height - character_size - 20)
        
        character_video = character_video.set_position(position)
        
        # Create composite
        final_video = CompositeVideoClip(
            [tiktok_video, character_video],
            size=(target_width, target_height)
        )
        
        # Set audio
        final_video = final_video.set_audio(audio)
        
        # Set duration
        final_video = final_video.set_duration(audio.duration)
        
        # Clean up
        tiktok_video.close()
        character_video.close()
        audio.close()
        
        return final_video
    
    def _compose_split_screen(
        self,
        tiktok_video_path: str,
        character_video_path: str,
        audio_path: str
    ):
        """Compose split-screen layout."""
        from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
        
        # Load videos
        tiktok_video = VideoFileClip(tiktok_video_path)
        character_video = VideoFileClip(character_video_path)
        audio = AudioFileClip(audio_path)
        
        # Get target resolution
        target_width = self.output_config.get('width', 1080)
        target_height = self.output_config.get('height', 1920)
        
        # Split screen: each video takes 50% of width
        split_width = target_width // 2
        
        # Resize and position TikTok video (left half)
        tiktok_video = tiktok_video.resize(width=split_width)
        tiktok_video = tiktok_video.set_position(('left', 'center'))
        
        # Resize and position character video (right half)
        character_video = character_video.resize(width=split_width)
        character_video = character_video.set_position((split_width, 'center'))
        
        # Create composite
        final_video = CompositeVideoClip(
            [tiktok_video, character_video],
            size=(target_width, target_height)
        )
        
        # Set audio
        final_video = final_video.set_audio(audio)
        
        # Set duration
        final_video = final_video.set_duration(audio.duration)
        
        # Clean up
        tiktok_video.close()
        character_video.close()
        audio.close()
        
        return final_video
    
    def _parse_size(self, size_str: str, reference: int) -> int:
        """Parse size string (e.g., '40%', '200px') to pixels."""
        if size_str.endswith('%'):
            percentage = float(size_str[:-1]) / 100.0
            return int(reference * percentage)
        elif size_str.endswith('px'):
            return int(size_str[:-2])
        else:
            # Assume pixels
            return int(size_str)

