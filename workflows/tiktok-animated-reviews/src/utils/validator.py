"""
Input Validator - JAEDS Framework
Comprehensive validation with graceful degradation

Based on research:
- Input validation and sanitization
- Graceful degradation strategies
"""

import os
import json
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional

logger = logging.getLogger(__name__)


class Validator:
    """
    Comprehensive input validator with graceful degradation.
    
    JAEDS Principles:
    - Jobs: Simple, clear validation
    - Alpha Evolve: Adaptive validation rules
    - Demis: Research-backed validation patterns
    - Superhero CV: Best practices from automation research
    """
    
    @staticmethod
    def validate_config(config_path: str) -> Tuple[bool, List[str]]:
        """
        Validate configuration file.
        
        Returns: (is_valid, errors)
        """
        errors = []
        
        # Check file exists
        if not Path(config_path).exists():
            return False, [f"Config file not found: {config_path}"]
        
        # Check file is readable
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
        except json.JSONDecodeError as e:
            return False, [f"Invalid JSON in config: {str(e)}"]
        except Exception as e:
            return False, [f"Cannot read config: {str(e)}"]
        
        # Validate required fields
        required_fields = ["voice", "composition"]
        for field in required_fields:
            if field not in config:
                errors.append(f"Missing required field: {field}")
        
        # Validate voice configuration
        if "voice" in config:
            voice = config["voice"]
            if "provider" not in voice:
                errors.append("Voice provider not specified")
            if "api_key" not in voice and not os.getenv("ELEVENLABS_API_KEY"):
                errors.append("API key not found (set in config or environment)")
            if "voice_id" not in voice:
                errors.append("Voice ID not specified")
        
        # Validate characters
        if "characters" in config:
            characters = config["characters"]
            for char_type, char_config in characters.items():
                if "file_path" not in char_config:
                    errors.append(f"Character {char_type} missing file_path")
                elif not Path(char_config["file_path"]).exists():
                    errors.append(f"Character file not found: {char_config['file_path']}")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_video_file(video_path: str) -> Tuple[bool, List[str]]:
        """Validate video file exists and is readable."""
        errors = []
        
        if not Path(video_path).exists():
            errors.append(f"Video file not found: {video_path}")
            return False, errors
        
        # Check file extension
        valid_extensions = ['.mp4', '.avi', '.mov', '.mkv']
        if Path(video_path).suffix.lower() not in valid_extensions:
            errors.append(f"Invalid video format. Supported: {', '.join(valid_extensions)}")
        
        # Check file size (not empty)
        if Path(video_path).stat().st_size == 0:
            errors.append("Video file is empty")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_script_file(script_path: str) -> Tuple[bool, List[str]]:
        """Validate script file exists and has content."""
        errors = []
        
        if not Path(script_path).exists():
            errors.append(f"Script file not found: {script_path}")
            return False, errors
        
        # Check file has content
        with open(script_path, 'r') as f:
            content = f.read().strip()
            if not content:
                errors.append("Script file is empty")
            elif len(content) < 10:
                errors.append("Script too short (minimum 10 characters)")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_character_file(character_path: str) -> Tuple[bool, List[str]]:
        """Validate character file."""
        errors = []
        
        if not Path(character_path).exists():
            errors.append(f"Character file not found: {character_path}")
            return False, errors
        
        # Check file extension
        valid_extensions = ['.mp4', '.avi', '.mov', '.png', '.jpg', '.spine', '.cubism']
        ext = Path(character_path).suffix.lower()
        if ext not in valid_extensions:
            errors.append(f"Invalid character format. Supported: {', '.join(valid_extensions)}")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_all(
        config_path: Optional[str] = None,
        video_path: Optional[str] = None,
        script_path: Optional[str] = None,
        character_paths: Optional[Dict[str, str]] = None
    ) -> Tuple[bool, List[str]]:
        """
        Validate all inputs.
        
        Returns: (is_valid, all_errors)
        """
        all_errors = []
        
        if config_path:
            is_valid, errors = Validator.validate_config(config_path)
            all_errors.extend(errors)
        
        if video_path:
            is_valid, errors = Validator.validate_video_file(video_path)
            all_errors.extend(errors)
        
        if script_path:
            is_valid, errors = Validator.validate_script_file(script_path)
            all_errors.extend(errors)
        
        if character_paths:
            for char_type, char_path in character_paths.items():
                is_valid, errors = Validator.validate_character_file(char_path)
                all_errors.extend([f"{char_type}: {e}" for e in errors])
        
        return len(all_errors) == 0, all_errors

