# BallCODE Story Production Pipeline - Educational Focus (Code, Math, AI)

**Goal:** Automated, scalable system for producing educational stories that teach coding, math, and AI concepts through basketball

**Focus:** Code concepts, Math concepts, AI mechanics - all integrated seamlessly

---

## System Architecture

```
Content Creation → Automated Processing → Unity Integration → Game Deployment
     ↓                    ↓                      ↓                  ↓
  JSON/YAML         Image Generation      Asset Creation      Live Update
  Story Files       Voice Synthesis       ScriptableObjects   CDN/Server
  (Code/Math/AI)    (Educational Focus)   (Unity Assets)      (Game)
```

---

## Part 1: Enhanced JSON Schema for Educational Content

### Episode JSON Structure (Code/Math/AI Focus)

```json
{
  "episodeNumber": 1,
  "title": "The Tip-off Trial",
  "subtitle": "Learn how robots think—through the game you love",
  
  "educationalConcepts": {
    "codingConcept": {
      "name": "State",
      "description": "State (start/live/dead/outcome)",
      "keyPoints": [
        "States track what's happening in a program",
        "Only one state can be active at a time",
        "States transition based on events"
      ],
      "codeExample": "if (state == LIVE) { play(); }",
      "visualType": "state_diagram"
    },
    "mathConcept": {
      "name": "Possession Statistics",
      "description": "Possession count, turnovers (basic stats)",
      "keyPoints": [
        "Counting possessions",
        "Calculating turnover rate",
        "Basic statistics tracking"
      ],
      "mathExample": "Turnover Rate = Turnovers / Possessions",
      "visualType": "statistics_chart"
    },
    "aiConcept": {
      "name": "Vision Cues & State Detection",
      "description": "Vision cue detects state shifts; player confirms",
      "keyPoints": [
        "AI can detect patterns (vision cues)",
        "Human confirmation required",
        "Confidence scores indicate AI certainty"
      ],
      "aiExample": "AI detects: 'State shift detected (confidence: 95%)'",
      "visualType": "ai_interface"
    }
  },
  
  "learningObjectives": [
    "Identify the four states of possession",
    "Track state changes in basketball scenarios",
    "Understand state transitions and rules",
    "Apply state concepts to edge cases",
    "Use AI assistance effectively with human confirmation"
  ],
  
  "monsterName": "Shadow Press Scouts",
  "gameMode": "Training",
  "hasFinalExercise": true,
  
  "spreads": [
    {
      "spreadNumber": 1,
      "leftPage": {
        "text": "Story text...",
        "imagePrompt": "Image prompt with educational focus...",
        "imageStyle": "cover",
        "educationalHighlight": {
          "concept": "coding",
          "highlight": "State concept introduction"
        }
      },
      "rightPage": {
        "text": "",
        "imagePrompt": "Educational diagram...",
        "imageStyle": "educational_diagram",
        "educationalHighlight": {
          "concept": "coding",
          "highlight": "State diagram visualization"
        }
      },
      "audio": {
        "text": "Audio narration...",
        "voice": "narrator",
        "speed": 1.0,
        "emphasis": ["state", "code", "program"]
      },
      "hasExercise": false
    }
  ],
  
  "skillPitStop": {
    "title": "Understanding State in Code",
    "content": "Mini-lesson explaining state concept...",
    "codeExamples": [
      {
        "language": "pseudocode",
        "code": "if state == START:\n    wait for tip-off\nelif state == LIVE:\n    play basketball"
      }
    ],
    "mathExamples": [
      {
        "type": "calculation",
        "example": "Turnover Rate = 2 turnovers / 3 possessions = 66.7%"
      }
    ],
    "aiExamples": [
      {
        "type": "detection",
        "example": "AI detects state shift with 95% confidence, player confirms"
      }
    ]
  },
  
  "exercises": [
    {
      "exerciseNumber": 1,
      "type": "coding",
      "title": "Label States in a Play",
      "instructions": "Identify states in basketball scenario",
      "duration": 60,
      "codingFocus": "State identification",
      "mathFocus": "Counting",
      "aiFocus": null
    },
    {
      "exerciseNumber": 2,
      "type": "coding",
      "title": "Write State Transitions",
      "instructions": "Draw state transition diagram",
      "duration": 90,
      "codingFocus": "State transitions",
      "mathFocus": "Pattern recognition",
      "aiFocus": null
    },
    {
      "exerciseNumber": 3,
      "type": "ai",
      "title": "AI State Detection",
      "instructions": "Use AI to detect states, confirm results",
      "duration": 90,
      "codingFocus": "State management",
      "mathFocus": "Probability (confidence scores)",
      "aiFocus": "Vision cues, human-AI collaboration"
    }
  ]
}
```

---

## Part 2: Educational Image Generation

### Enhanced Image Prompts for Code/Math/AI Concepts

The image generation script needs to understand educational context:

```python
# generate_educational_images.py
class EducationalImageGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_style = "Modern children's book illustration, educational focus, vibrant colors, clean lines, age-appropriate for grades 3-8"
        
        # Educational style modifiers
        self.style_modifiers = {
            "coding": "Include code-like elements, flowcharts, state diagrams, programming concepts",
            "math": "Include numbers, calculations, statistics, charts, mathematical visualizations",
            "ai": "Include AI interface elements, confidence scores, detection indicators, tech HUDs"
        }
    
    def generate_educational_image(self, prompt, concept_type, output_path):
        """Generate image with educational focus"""
        
        # Add educational context
        educational_context = self.style_modifiers.get(concept_type, "")
        full_prompt = f"{prompt}. {self.base_style}. {educational_context}. Educational content for teaching {concept_type} concepts through basketball."
        
        # Generate with API
        # ... (API call code)
        
        return output_path
    
    def generate_code_diagram(self, episode, spread):
        """Generate code-focused diagram"""
        if spread["educationalHighlight"]["concept"] == "coding":
            prompt = self.build_code_diagram_prompt(episode, spread)
            return self.generate_educational_image(prompt, "coding", output_path)
    
    def generate_math_chart(self, episode, spread):
        """Generate math-focused visualization"""
        if spread["educationalHighlight"]["concept"] == "math":
            prompt = self.build_math_chart_prompt(episode, spread)
            return self.generate_educational_image(prompt, "math", output_path)
    
    def generate_ai_interface(self, episode, spread):
        """Generate AI-focused interface"""
        if spread["educationalHighlight"]["concept"] == "ai":
            prompt = self.build_ai_interface_prompt(episode, spread)
            return self.generate_educational_image(prompt, "ai", output_path)
```

---

## Part 3: Educational Voice Synthesis

### Voice Generation with Educational Emphasis

```python
# generate_educational_voice.py
class EducationalVoiceGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.voice_map = {
            "narrator": "voice_id_narrator_educational",
            "nova": "voice_id_nova_tech",
            "coach": "voice_id_coach_mentor",
            "arc": "voice_id_ai_assistant"
        }
    
    def generate_with_emphasis(self, text, voice, emphasis_words, output_path):
        """Generate voice with emphasis on educational terms"""
        
        # Add SSML for emphasis (if API supports)
        emphasized_text = self.add_emphasis(text, emphasis_words)
        
        # Generate audio
        # ... (API call with emphasis)
        
        return output_path
    
    def add_emphasis(self, text, emphasis_words):
        """Add emphasis to educational terms"""
        for word in emphasis_words:
            text = text.replace(word, f"<emphasis>{word}</emphasis>")
        return text
```

---

## Part 4: Unity Integration with Educational Focus

### Enhanced Unity Script for Educational Content

```csharp
// EducationalStoryAssetGenerator.cs
using UnityEngine;
using UnityEditor;
using System.IO;
using Newtonsoft.Json;

[System.Serializable]
public class EducationalEpisodeData
{
    public int episodeNumber;
    public string title;
    public EducationalConcepts educationalConcepts;
    public LearningObjective[] learningObjectives;
    public EducationalSpread[] spreads;
    public SkillPitStop skillPitStop;
    public EducationalExercise[] exercises;
}

[System.Serializable]
public class EducationalConcepts
{
    public CodingConcept codingConcept;
    public MathConcept mathConcept;
    public AIConcept aiConcept;
}

[System.Serializable]
public class CodingConcept
{
    public string name;
    public string description;
    public string[] keyPoints;
    public string codeExample;
    public string visualType;
}

[System.Serializable]
public class MathConcept
{
    public string name;
    public string description;
    public string[] keyPoints;
    public string mathExample;
    public string visualType;
}

[System.Serializable]
public class AIConcept
{
    public string name;
    public string description;
    public string[] keyPoints;
    public string aiExample;
    public string visualType;
}

public class EducationalStoryAssetGenerator : EditorWindow
{
    [MenuItem("BallCODE/Generate Educational Story Assets")]
    public static void GenerateAssets()
    {
        string jsonPath = EditorUtility.OpenFilePanel("Select Episode JSON", "", "json");
        if (string.IsNullOrEmpty(jsonPath)) return;
        
        // Load and parse JSON
        string jsonContent = File.ReadAllText(jsonPath);
        EducationalEpisodeData episodeData = JsonConvert.DeserializeObject<EducationalEpisodeData>(jsonContent);
        
        // Create ScriptableObject with educational fields
        StoryEpisodeData episodeAsset = ScriptableObject.CreateInstance<StoryEpisodeData>();
        
        // Map educational concepts
        episodeAsset.codingConcept = episodeData.educationalConcepts.codingConcept.name;
        episodeAsset.mathConcept = episodeData.educationalConcepts.mathConcept.name;
        episodeAsset.aiConcept = episodeData.educationalConcepts.aiConcept.name;
        
        // Map learning objectives
        episodeAsset.learningObjectives = new string[episodeData.learningObjectives.Length];
        for (int i = 0; i < episodeData.learningObjectives.Length; i++)
        {
            episodeAsset.learningObjectives[i] = episodeData.learningObjectives[i].objective;
        }
        
        // Process spreads with educational highlights
        for (int i = 0; i < episodeData.spreads.Count; i++)
        {
            var spread = episodeData.spreads[i];
            
            // Load images based on educational concept type
            string imagePath = GetImagePathForConcept(
                episodeData.episodeNumber,
                i + 1,
                spread.educationalHighlight.concept
            );
            
            if (File.Exists(imagePath))
            {
                episodeAsset.spreads[i].rightPageImage = AssetDatabase.LoadAssetAtPath<Sprite>(imagePath);
            }
        }
        
        // Save asset
        string assetPath = $"Assets/StoryContent/Episodes/Episode{episodeData.episodeNumber}.asset";
        AssetDatabase.CreateAsset(episodeAsset, assetPath);
        AssetDatabase.SaveAssets();
        
        Debug.Log($"Generated educational story asset: {assetPath}");
    }
}
```

---

## Part 5: Complete Automation Pipeline

### Master Pipeline with Educational Focus

```python
# educational_pipeline.py
import json
import os
from generate_educational_images import EducationalImageGenerator
from generate_educational_voice import EducationalVoiceGenerator

class EducationalStoryPipeline:
    def __init__(self, config):
        self.config = config
        self.image_gen = EducationalImageGenerator(config["image_api_key"])
        self.voice_gen = EducationalVoiceGenerator(config["voice_api_key"])
    
    def process_episode(self, episode_json_path):
        """Complete pipeline for educational content"""
        
        with open(episode_json_path) as f:
            episode = json.load(f)
        
        episode_num = episode["episodeNumber"]
        base_dir = f"output/episode{episode_num}"
        
        print(f"Processing Episode {episode_num}: {episode['title']}")
        print(f"  Coding: {episode['educationalConcepts']['codingConcept']['name']}")
        print(f"  Math: {episode['educationalConcepts']['mathConcept']['name']}")
        print(f"  AI: {episode['educationalConcepts']['aiConcept']['name']}")
        
        # 1. Generate educational images
        print("Generating educational images...")
        self.generate_educational_images(episode, base_dir)
        
        # 2. Generate educational voice
        print("Generating educational voice...")
        self.generate_educational_voice(episode, base_dir)
        
        # 3. Generate code examples (if needed)
        print("Processing code examples...")
        self.process_code_examples(episode, base_dir)
        
        # 4. Generate math visualizations
        print("Processing math visualizations...")
        self.process_math_visualizations(episode, base_dir)
        
        # 5. Generate AI interface elements
        print("Processing AI interface elements...")
        self.process_ai_elements(episode, base_dir)
        
        # 6. Copy to Unity
        print("Copying to Unity project...")
        self.copy_to_unity(episode_num, base_dir)
        
        # 7. Generate Unity asset
        print("Generating Unity educational asset...")
        self.generate_unity_asset(episode_json_path)
        
        print(f"✅ Educational Episode {episode_num} complete!")
    
    def generate_educational_images(self, episode, base_dir):
        """Generate images with educational focus"""
        image_dir = f"{base_dir}/images"
        os.makedirs(image_dir, exist_ok=True)
        
        for spread in episode["spreads"]:
            # Determine concept type
            concept_type = spread["leftPage"].get("educationalHighlight", {}).get("concept", "general")
            
            # Generate left page
            if spread["leftPage"]["imagePrompt"]:
                left_path = f"{image_dir}/ep{episode['episodeNumber']}_spread{spread['spreadNumber']}_left.png"
                self.image_gen.generate_educational_image(
                    spread["leftPage"]["imagePrompt"],
                    concept_type,
                    left_path
                )
            
            # Generate right page
            if spread["rightPage"]["imagePrompt"]:
                right_path = f"{image_dir}/ep{episode['episodeNumber']}_spread{spread['spreadNumber']}_right.png"
                concept_type = spread["rightPage"].get("educationalHighlight", {}).get("concept", "general")
                self.image_gen.generate_educational_image(
                    spread["rightPage"]["imagePrompt"],
                    concept_type,
                    right_path
                )
    
    def process_code_examples(self, episode, base_dir):
        """Process code examples from Skill Pit-Stop"""
        if "skillPitStop" in episode and "codeExamples" in episode["skillPitStop"]:
            code_dir = f"{base_dir}/code_examples"
            os.makedirs(code_dir, exist_ok=True)
            
            for i, code_example in enumerate(episode["skillPitStop"]["codeExamples"]):
                # Generate syntax-highlighted code image
                code_image_path = f"{code_dir}/code_example_{i+1}.png"
                self.image_gen.generate_code_syntax_image(
                    code_example["code"],
                    code_example["language"],
                    code_image_path
                )
    
    def process_math_visualizations(self, episode, base_dir):
        """Process math visualizations"""
        if "skillPitStop" in episode and "mathExamples" in episode["skillPitStop"]:
            math_dir = f"{base_dir}/math_visualizations"
            os.makedirs(math_dir, exist_ok=True)
            
            for i, math_example in enumerate(episode["skillPitStop"]["mathExamples"]):
                # Generate math chart/diagram
                math_image_path = f"{math_dir}/math_example_{i+1}.png"
                self.image_gen.generate_math_visualization(
                    math_example,
                    math_image_path
                )
    
    def process_ai_elements(self, episode, base_dir):
        """Process AI interface elements"""
        if "skillPitStop" in episode and "aiExamples" in episode["skillPitStop"]:
            ai_dir = f"{base_dir}/ai_elements"
            os.makedirs(ai_dir, exist_ok=True)
            
            for i, ai_example in enumerate(episode["skillPitStop"]["aiExamples"]):
                # Generate AI interface mockup
                ai_image_path = f"{ai_dir}/ai_example_{i+1}.png"
                self.image_gen.generate_ai_interface(
                    ai_example,
                    ai_image_path
                )
```

---

## Part 6: Educational Content Validation

### Validation Script for Educational Content

```python
# validate_educational_content.py
def validate_episode(episode_json):
    """Validate educational content completeness"""
    errors = []
    warnings = []
    
    # Check educational concepts
    if "educationalConcepts" not in episode_json:
        errors.append("Missing educationalConcepts section")
    else:
        concepts = episode_json["educationalConcepts"]
        
        # Validate coding concept
        if "codingConcept" not in concepts:
            errors.append("Missing codingConcept")
        else:
            coding = concepts["codingConcept"]
            if not coding.get("codeExample"):
                warnings.append("Coding concept missing code example")
        
        # Validate math concept
        if "mathConcept" not in concepts:
            errors.append("Missing mathConcept")
        else:
            math = concepts["mathConcept"]
            if not math.get("mathExample"):
                warnings.append("Math concept missing math example")
        
        # Validate AI concept
        if "aiConcept" not in concepts:
            errors.append("Missing aiConcept")
        else:
            ai = concepts["aiConcept"]
            if not ai.get("aiExample"):
                warnings.append("AI concept missing AI example")
    
    # Check learning objectives
    if "learningObjectives" not in episode_json:
        warnings.append("Missing learningObjectives")
    
    # Check exercises have educational focus
    if "exercises" in episode_json:
        for exercise in episode_json["exercises"]:
            if not exercise.get("codingFocus") and not exercise.get("mathFocus") and not exercise.get("aiFocus"):
                warnings.append(f"Exercise {exercise.get('exerciseNumber')} missing educational focus")
    
    return errors, warnings
```

---

## Part 7: Educational Analytics Integration

### Track Educational Progress

```python
# educational_analytics.py
class EducationalAnalytics:
    def track_concept_mastery(self, episode_number, concept_type, user_id):
        """Track which concepts users master"""
        # Coding concept mastery
        # Math concept mastery
        # AI concept mastery
        
    def generate_progress_report(self, user_id):
        """Generate educational progress report"""
        return {
            "codingConcepts": ["State", "Conditionals", "Loops"],
            "mathConcepts": ["Statistics", "Probability", "EV"],
            "aiConcepts": ["Vision Cues", "Confidence Scores"],
            "masteryLevel": "intermediate"
        }
```

---

## Part 8: Implementation Checklist

### Setup Steps

1. **Create JSON Schema** ✅
   - Enhanced with code/math/AI fields
   - Educational concept structure
   - Learning objectives

2. **Set Up APIs**
   - Image generation (Stability AI/Replicate)
   - Voice synthesis (ElevenLabs/Google TTS)
   - Code syntax highlighting (if needed)

3. **Write Automation Scripts**
   - Educational image generator
   - Educational voice generator
   - Code example processor
   - Math visualization generator
   - AI interface generator

4. **Create Unity Integration**
   - Enhanced ScriptableObject structure
   - Educational concept fields
   - Learning objective tracking

5. **Test with Episode 1**
   - Full pipeline test
   - Educational content validation
   - Unity integration test

6. **Scale to All Episodes**
   - Automated production
   - Educational consistency
   - Quality validation

---

## Benefits for Educational Focus

✅ **Code Concepts:** Visualized through diagrams, code examples, flowcharts  
✅ **Math Concepts:** Visualized through charts, calculations, statistics  
✅ **AI Concepts:** Visualized through interfaces, confidence scores, detection cues  
✅ **Learning Objectives:** Tracked and validated  
✅ **Educational Consistency:** All episodes follow same educational structure  
✅ **Scalable:** Add new educational episodes easily  
✅ **Automated:** No manual educational content creation  

---

**This system ensures every story teaches code, math, and AI concepts effectively!**




