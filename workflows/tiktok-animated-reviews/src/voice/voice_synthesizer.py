"""
Voice Synthesis System - JAEDS Framework

Generates voice audio from text using voice cloning technology.
Supports multiple providers: ElevenLabs, Google Cloud TTS, Azure, OpenAI.

JAEDS Principles:
- Jobs: Simple API, natural-sounding output
- Alpha Evolve: Rapid iteration on voice quality
- Demis: Research-backed voice synthesis
- Superhero CV: Best practices from audio processing research
"""

import os
import logging
from typing import Dict, Optional
from pathlib import Path

logger = logging.getLogger(__name__)


class VoiceSynthesizer:
    """
    Voice synthesis system with support for multiple providers.
    
    Providers:
    - ElevenLabs (recommended for voice cloning)
    - Google Cloud TTS (alternative)
    - Azure Cognitive Services (enterprise)
    - OpenAI TTS (new voice cloning)
    """
    
    def __init__(self, config: Dict):
        """Initialize voice synthesizer with configuration."""
        self.config = config
        self.provider = config.get('provider', 'elevenlabs')
        self.api_key = config.get('api_key') or os.getenv('ELEVENLABS_API_KEY')
        self.voice_id = config.get('voice_id')
        self.settings = config.get('settings', {})
        
        # Initialize provider-specific client
        self.client = self._initialize_provider()
        
        logger.info(f"✅ Voice Synthesizer initialized (provider: {self.provider})")
    
    def _initialize_provider(self):
        """Initialize provider-specific client."""
        if self.provider == 'elevenlabs':
            return self._init_elevenlabs()
        elif self.provider == 'google':
            return self._init_google()
        elif self.provider == 'azure':
            return self._init_azure()
        elif self.provider == 'openai':
            return self._init_openai()
        else:
            raise ValueError(f"Unknown provider: {self.provider}")
    
    def _init_elevenlabs(self):
        """Initialize ElevenLabs client."""
        try:
            from elevenlabs import generate, set_api_key, Voice, VoiceSettings
            
            if self.api_key:
                set_api_key(self.api_key)
            
            # Create voice settings
            voice_settings = VoiceSettings(
                stability=self.settings.get('stability', 0.75),
                similarity_boost=self.settings.get('similarity_boost', 0.75),
                style=self.settings.get('style', 0.0),
                use_speaker_boost=self.settings.get('use_speaker_boost', True)
            )
            
            return {
                'generate': generate,
                'voice_settings': voice_settings,
                'voice_id': self.voice_id
            }
        except ImportError:
            logger.error("❌ ElevenLabs library not installed. Install with: pip install elevenlabs")
            raise
    
    def _init_google(self):
        """Initialize Google Cloud TTS client."""
        try:
            from google.cloud import texttospeech
            
            client = texttospeech.TextToSpeechClient()
            return {
                'client': client,
                'voice_id': self.voice_id
            }
        except ImportError:
            logger.error("❌ Google Cloud TTS library not installed. Install with: pip install google-cloud-texttospeech")
            raise
    
    def _init_azure(self):
        """Initialize Azure Cognitive Services client."""
        try:
            import azure.cognitiveservices.speech as speechsdk
            
            speech_config = speechsdk.SpeechConfig(
                subscription=self.api_key,
                region=self.config.get('region', 'eastus')
            )
            
            return {
                'speech_config': speech_config,
                'voice_id': self.voice_id
            }
        except ImportError:
            logger.error("❌ Azure Speech SDK not installed. Install with: pip install azure-cognitiveservices-speech")
            raise
    
    def _init_openai(self):
        """Initialize OpenAI TTS client."""
        try:
            from openai import OpenAI
            
            client = OpenAI(api_key=self.api_key)
            return {
                'client': client,
                'voice_id': self.voice_id or 'alloy'  # Default voice
            }
        except ImportError:
            logger.error("❌ OpenAI library not installed. Install with: pip install openai")
            raise
    
    def synthesize(self, text: str, output_path: str) -> str:
        """
        Synthesize voice audio from text.
        
        Args:
            text: Text to synthesize
            output_path: Path to save audio file
        
        Returns:
            Path to generated audio file
        """
        logger.info(f"🎤 Synthesizing voice audio...")
        logger.debug(f"   Text length: {len(text)} characters")
        logger.debug(f"   Provider: {self.provider}")
        
        # Ensure output directory exists
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Generate audio based on provider
        if self.provider == 'elevenlabs':
            audio_data = self._synthesize_elevenlabs(text)
        elif self.provider == 'google':
            audio_data = self._synthesize_google(text)
        elif self.provider == 'azure':
            audio_data = self._synthesize_azure(text)
        elif self.provider == 'openai':
            audio_data = self._synthesize_openai(text)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")
        
        # Save audio file
        with open(output_path, 'wb') as f:
            f.write(audio_data)
        
        logger.info(f"✅ Voice audio saved: {output_path}")
        return str(output_path)
    
    def _synthesize_elevenlabs(self, text: str) -> bytes:
        """Synthesize using ElevenLabs."""
        from elevenlabs import generate
        
        audio = generate(
            text=text,
            voice=self.voice_id,
            model="eleven_multilingual_v2",
            voice_settings=self.client['voice_settings']
        )
        
        # Convert generator to bytes
        audio_bytes = b''.join(audio)
        return audio_bytes
    
    def _synthesize_google(self, text: str) -> bytes:
        """Synthesize using Google Cloud TTS."""
        from google.cloud import texttospeech
        
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name=self.voice_id or "en-US-Wavenet-D"
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        
        response = self.client['client'].synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )
        
        return response.audio_content
    
    def _synthesize_azure(self, text: str) -> bytes:
        """Synthesize using Azure Cognitive Services."""
        import azure.cognitiveservices.speech as speechsdk
        
        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.client['speech_config']
        )
        
        result = synthesizer.speak_text_async(text).get()
        
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return result.audio_data
        else:
            raise Exception(f"Azure TTS failed: {result.reason}")
    
    def _synthesize_openai(self, text: str) -> bytes:
        """Synthesize using OpenAI TTS."""
        response = self.client['client'].audio.speech.create(
            model="tts-1",
            voice=self.client['voice_id'],
            input=text
        )
        
        return response.content


def create_voice_clone(voice_sample_path: str, provider: str = 'elevenlabs') -> str:
    """
    Create a voice clone from a sample audio file.
    
    Args:
        voice_sample_path: Path to voice sample audio file
        provider: Voice cloning provider
    
    Returns:
        Voice ID for use in synthesis
    """
    if provider == 'elevenlabs':
        from elevenlabs import clone, set_api_key
        
        api_key = os.getenv('ELEVENLABS_API_KEY')
        if not api_key:
            raise ValueError("ELEVENLABS_API_KEY environment variable not set")
        
        set_api_key(api_key)
        
        # Clone voice
        voice = clone(
            name="My Voice Clone",
            files=[voice_sample_path]
        )
        
        return voice.voice_id
    else:
        raise ValueError(f"Voice cloning not supported for provider: {provider}")

