#!/usr/bin/env python3
"""
BallCODE Educational Story Production Pipeline
Automates image generation, voice synthesis, and Unity asset creation
for educational stories focused on code, math, and AI concepts.
"""

import json
import os
import requests
import base64
from pathlib import Path
from typing import Dict, List, Optional

class EducationalImageGenerator:
    """Generate images with educational focus (code, math, AI concepts)"""
    
    def __init__(self, api_key: str, provider: str = "stability"):
        self.api_key = api_key
        self.provider = provider
        self.base_style = "Modern children's book illustration, educational focus, vibrant colors, clean lines, age-appropriate for grades 3-8"
        
        # Educational style modifiers
        self.style_modifiers = {
            "coding": "Include code-like elements, flowcharts, state diagrams, programming concepts, pseudocode visualizations",
            "math": "Include numbers, calculations, statistics, charts, mathematical visualizations, percentage displays",
            "ai": "Include AI interface elements, confidence scores, detection indicators, tech HUDs, human-AI collaboration",
            "general": "Educational children's book style"
        }
    
    def generate_image(self, prompt: str, concept_type: str, output_path: str) -> str:
        """Generate image with educational context"""
        
        # Add educational context
        educational_context = self.style_modifiers.get(concept_type, "")
        full_prompt = f"{prompt}. {self.base_style}. {educational_context}. Educational content for teaching {concept_type} concepts through basketball."
        
        if self.provider == "stability":
            return self._generate_stability(full_prompt, output_path)
        elif self.provider == "replicate":
            return self._generate_replicate(full_prompt, output_path)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")
    
    def _generate_stability(self, prompt: str, output_path: str) -> str:
        """Generate using Stability AI API"""
        response = requests.post(
            "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "text_prompts": [{"text": prompt, "weight": 1.0}],
                "cfg_scale": 7,
                "width": 1024,
                "height": 768,
                "samples": 1,
                "steps": 30
            }
        )
        
        if response.status_code == 200:
            image_data = response.json()["artifacts"][0]["base64"]
            with open(output_path, "wb") as f:
                f.write(base64.b64decode(image_data))
            return output_path
        else:
            raise Exception(f"Image generation failed: {response.text}")
    
    def _generate_replicate(self, prompt: str, output_path: str) -> str:
        """Generate using Replicate API"""
        # Implementation for Replicate API
        # Similar structure to Stability AI
        pass


class EducationalVoiceGenerator:
    """Generate voice with educational emphasis"""
    
    def __init__(self, api_key: str, provider: str = "elevenlabs"):
        self.api_key = api_key
        self.provider = provider
        self.voice_map = {
            "narrator": "21m00Tcm4TlvDq8ikWAM",  # Default narrator voice ID
            "nova": "21m00Tcm4TlvDq8ikWAM",  # Tech-savvy voice
            "coach": "21m00Tcm4TlvDq8ikWAM",  # Mentor voice
            "arc": "21m00Tcm4TlvDq8ikWAM"  # AI assistant voice
        }
    
    def generate_audio(self, text: str, voice: str, output_path: str, 
                      speed: float = 1.0, emphasis_words: Optional[List[str]] = None) -> str:
        """Generate audio with emphasis on educational terms"""
        
        if emphasis_words:
            # Add emphasis to educational terms (SSML if supported)
            text = self._add_emphasis(text, emphasis_words)
        
        if self.provider == "elevenlabs":
            return self._generate_elevenlabs(text, voice, output_path, speed)
        elif self.provider == "google":
            return self._generate_google(text, voice, output_path, speed)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")
    
    def _add_emphasis(self, text: str, emphasis_words: List[str]) -> str:
        """Add emphasis to educational terms"""
        for word in emphasis_words:
            # Simple emphasis - can be enhanced with SSML
            text = text.replace(word, f"**{word}**")
        return text
    
    def _generate_elevenlabs(self, text: str, voice: str, output_path: str, speed: float) -> str:
        """Generate using ElevenLabs API"""
        voice_id = self.voice_map.get(voice, self.voice_map["narrator"])
        
        response = requests.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
            headers={"xi-api-key": self.api_key},
            json={
                "text": text,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75,
                    "speed": speed
                }
            }
        )
        
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            return output_path
        else:
            raise Exception(f"Voice generation failed: {response.text}")
    
    def _generate_google(self, text: str, voice: str, output_path: str, speed: float) -> str:
        """Generate using Google Cloud TTS"""
        # Implementation for Google TTS
        pass


class EducationalStoryPipeline:
    """Complete pipeline for educational story production"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.image_gen = EducationalImageGenerator(
            config.get("image_api_key"),
            config.get("image_provider", "stability")
        )
        self.voice_gen = EducationalVoiceGenerator(
            config.get("voice_api_key"),
            config.get("voice_provider", "elevenlabs")
        )
    
    def process_episode(self, episode_json_path: str):
        """Complete pipeline: JSON → Images → Voice → Unity Assets"""
        
        # Load episode JSON
        with open(episode_json_path) as f:
            episode = json.load(f)
        
        episode_num = episode["episodeNumber"]
        base_dir = f"output/episode{episode_num}"
        os.makedirs(base_dir, exist_ok=True)
        
        print(f"\n{'='*60}")
        print(f"Processing Episode {episode_num}: {episode['title']}")
        print(f"{'='*60}")
        print(f"  Coding: {episode['educationalConcepts']['codingConcept']['name']}")
        print(f"  Math: {episode['educationalConcepts']['mathConcept']['name']}")
        print(f"  AI: {episode['educationalConcepts']['aiConcept']['name']}")
        print(f"{'='*60}\n")
        
        # 1. Generate educational images
        print("📸 Generating educational images...")
        self._generate_educational_images(episode, base_dir)
        
        # 2. Generate educational voice
        print("🎤 Generating educational voice...")
        self._generate_educational_voice(episode, base_dir)
        
        # 3. Process code examples
        print("💻 Processing code examples...")
        self._process_code_examples(episode, base_dir)
        
        # 4. Process math visualizations
        print("📊 Processing math visualizations...")
        self._process_math_visualizations(episode, base_dir)
        
        # 5. Process AI elements
        print("🤖 Processing AI interface elements...")
        self._process_ai_elements(episode, base_dir)
        
        # 6. Copy to Unity
        print("🎮 Copying to Unity project...")
        self._copy_to_unity(episode_num, base_dir)
        
        # 7. Generate manifest for Unity
        print("📝 Generating Unity manifest...")
        self._generate_unity_manifest(episode, base_dir)
        
        print(f"\n✅ Educational Episode {episode_num} pipeline complete!")
        print(f"   Output directory: {base_dir}")
    
    def _generate_educational_images(self, episode: Dict, base_dir: str):
        """Generate images with educational focus"""
        image_dir = f"{base_dir}/images"
        os.makedirs(image_dir, exist_ok=True)
        
        for spread in episode["spreads"]:
            spread_num = spread["spreadNumber"]
            
            # Generate left page
            if spread["leftPage"].get("imagePrompt"):
                concept_type = spread["leftPage"].get("educationalHighlight", {}).get("concept", "general")
                left_path = f"{image_dir}/ep{episode['episodeNumber']}_spread{spread_num}_left.png"
                print(f"  Generating left page {spread_num} ({concept_type})...")
                self.image_gen.generate_image(
                    spread["leftPage"]["imagePrompt"],
                    concept_type,
                    left_path
                )
            
            # Generate right page
            if spread["rightPage"].get("imagePrompt"):
                concept_type = spread["rightPage"].get("educationalHighlight", {}).get("concept", "general")
                right_path = f"{image_dir}/ep{episode['episodeNumber']}_spread{spread_num}_right.png"
                print(f"  Generating right page {spread_num} ({concept_type})...")
                self.image_gen.generate_image(
                    spread["rightPage"]["imagePrompt"],
                    concept_type,
                    right_path
                )
    
    def _generate_educational_voice(self, episode: Dict, base_dir: str):
        """Generate voice with educational emphasis"""
        audio_dir = f"{base_dir}/audio"
        os.makedirs(audio_dir, exist_ok=True)
        
        for spread in episode["spreads"]:
            if spread.get("audio"):
                spread_num = spread["spreadNumber"]
                audio_path = f"{audio_dir}/ep{episode['episodeNumber']}_spread{spread_num}.mp3"
                
                print(f"  Generating audio for spread {spread_num}...")
                self.voice_gen.generate_audio(
                    spread["audio"]["text"],
                    spread["audio"]["voice"],
                    audio_path,
                    spread["audio"].get("speed", 1.0),
                    spread["audio"].get("emphasis", [])
                )
    
    def _process_code_examples(self, episode: Dict, base_dir: str):
        """Process code examples from Skill Pit-Stop"""
        if "skillPitStop" in episode and "codeExamples" in episode["skillPitStop"]:
            code_dir = f"{base_dir}/code_examples"
            os.makedirs(code_dir, exist_ok=True)
            
            for i, code_example in enumerate(episode["skillPitStop"]["codeExamples"]):
                # Save code example as text file
                code_file = f"{code_dir}/code_example_{i+1}.txt"
                with open(code_file, "w") as f:
                    f.write(f"Language: {code_example['language']}\n\n")
                    f.write(code_example["code"])
                    if "explanation" in code_example:
                        f.write(f"\n\nExplanation:\n{code_example['explanation']}")
                
                print(f"  Saved code example {i+1}")
    
    def _process_math_visualizations(self, episode: Dict, base_dir: str):
        """Process math visualizations"""
        if "skillPitStop" in episode and "mathExamples" in episode["skillPitStop"]:
            math_dir = f"{base_dir}/math_visualizations"
            os.makedirs(math_dir, exist_ok=True)
            
            for i, math_example in enumerate(episode["skillPitStop"]["mathExamples"]):
                # Generate math visualization image
                math_prompt = f"Educational math visualization: {math_example['example']}. Clean chart or diagram showing the calculation. Kid-friendly, colorful, clear labels. Style: Modern children's book illustration, educational math chart style."
                
                math_image_path = f"{math_dir}/math_example_{i+1}.png"
                print(f"  Generating math visualization {i+1}...")
                self.image_gen.generate_image(math_prompt, "math", math_image_path)
    
    def _process_ai_elements(self, episode: Dict, base_dir: str):
        """Process AI interface elements"""
        if "skillPitStop" in episode and "aiExamples" in episode["skillPitStop"]:
            ai_dir = f"{base_dir}/ai_elements"
            os.makedirs(ai_dir, exist_ok=True)
            
            for i, ai_example in enumerate(episode["skillPitStop"]["aiExamples"]):
                # Generate AI interface mockup
                ai_prompt = f"AI interface mockup: {ai_example['example']}. Modern HUD display showing AI detection, confidence scores, human confirmation. Clean, kid-friendly tech interface. Style: Modern children's book illustration, tech interface but age-appropriate."
                
                ai_image_path = f"{ai_dir}/ai_example_{i+1}.png"
                print(f"  Generating AI interface {i+1}...")
                self.image_gen.generate_image(ai_prompt, "ai", ai_image_path)
    
    def _copy_to_unity(self, episode_num: int, source_dir: str):
        """Copy generated assets to Unity project"""
        unity_base = self.config.get("unity_project_path", "UnityProject")
        unity_image_dir = f"{unity_base}/Assets/StoryContent/Images/Episode{episode_num}/"
        unity_audio_dir = f"{unity_base}/Assets/StoryContent/Audio/Episode{episode_num}/"
        
        os.makedirs(unity_image_dir, exist_ok=True)
        os.makedirs(unity_audio_dir, exist_ok=True)
        
        import shutil
        
        # Copy images
        image_source = f"{source_dir}/images"
        if os.path.exists(image_source):
            for file in os.listdir(image_source):
                shutil.copy(f"{image_source}/{file}", unity_image_dir)
        
        # Copy audio
        audio_source = f"{source_dir}/audio"
        if os.path.exists(audio_source):
            for file in os.listdir(audio_source):
                shutil.copy(f"{audio_source}/{file}", unity_audio_dir)
        
        print(f"  Copied assets to Unity project")
    
    def _generate_unity_manifest(self, episode: Dict, base_dir: str):
        """Generate manifest file for Unity import"""
        manifest = {
            "episodeNumber": episode["episodeNumber"],
            "title": episode["title"],
            "educationalConcepts": episode["educationalConcepts"],
            "learningObjectives": episode["learningObjectives"],
            "spreadCount": len(episode["spreads"]),
            "imageCount": len([s for s in episode["spreads"] if s["leftPage"].get("imagePrompt")]) * 2,
            "audioCount": len([s for s in episode["spreads"] if s.get("audio")])
        }
        
        manifest_path = f"{base_dir}/manifest.json"
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)
        
        print(f"  Generated manifest: {manifest_path}")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="BallCODE Educational Story Pipeline")
    parser.add_argument("episode_json", help="Path to episode JSON file")
    parser.add_argument("--image-api-key", help="Image generation API key")
    parser.add_argument("--voice-api-key", help="Voice synthesis API key")
    parser.add_argument("--unity-path", help="Unity project path", default="UnityProject")
    parser.add_argument("--image-provider", choices=["stability", "replicate"], default="stability")
    parser.add_argument("--voice-provider", choices=["elevenlabs", "google"], default="elevenlabs")
    
    args = parser.parse_args()
    
    # Load config from environment or args
    config = {
        "image_api_key": args.image_api_key or os.getenv("STABILITY_API_KEY"),
        "voice_api_key": args.voice_api_key or os.getenv("ELEVENLABS_API_KEY"),
        "unity_project_path": args.unity_path,
        "image_provider": args.image_provider,
        "voice_provider": args.voice_provider
    }
    
    if not config["image_api_key"]:
        print("Error: Image API key required (--image-api-key or STABILITY_API_KEY env var)")
        return
    
    if not config["voice_api_key"]:
        print("Error: Voice API key required (--voice-api-key or ELEVENLABS_API_KEY env var)")
        return
    
    # Run pipeline
    pipeline = EducationalStoryPipeline(config)
    pipeline.process_episode(args.episode_json)


if __name__ == "__main__":
    main()




