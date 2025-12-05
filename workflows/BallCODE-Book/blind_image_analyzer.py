#!/usr/bin/env python3
"""
Blind Image Analyzer - AIMCODE Approach
Analyzes images programmatically without vision APIs or human assistance
Like a blind person would need to "see" images

AIMCODE Principles:
- Jobs: Simple, "it just works"
- Hassabis: Systematic, layer-by-layer analysis
- Resnick: Build understanding through exploration
- Reggio: Multiple ways to understand (text, structure, color, patterns)
- Zhang: Understand game to build better stories
"""

import os
import json
import cv2
import numpy as np
from pathlib import Path
from PIL import Image, ImageStat
from typing import Dict, List, Optional
from collections import defaultdict
import re

# Try to import OCR
try:
    import pytesseract
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False
    print("⚠️  pytesseract not available - text extraction limited")

# Try to import scikit-image
try:
    from skimage import filters, segmentation, color
    from skimage.feature import canny
    SKIMAGE_AVAILABLE = True
except ImportError:
    SKIMAGE_AVAILABLE = False
    print("⚠️  scikit-image not available - using basic OpenCV only")


class BlindImageAnalyzer:
    """Analyze images programmatically - like a blind person would need to 'see'"""
    
    def __init__(self):
        self.ocr_available = OCR_AVAILABLE
        self.skimage_available = SKIMAGE_AVAILABLE
    
    def analyze_image(self, image_path: str) -> Dict:
        """
        Comprehensive image analysis using multiple techniques
        Layer-by-layer approach (Alpha Evolve)
        """
        print(f"🔍 Analyzing: {os.path.basename(image_path)}")
        
        # Load image
        img = cv2.imread(image_path)
        if img is None:
            return {"error": "Could not load image"}
        
        pil_img = Image.open(image_path)
        
        result = {
            "filename": os.path.basename(image_path),
            "path": image_path,
            "layers": {}
        }
        
        # LAYER 1: Basic Properties
        result["layers"]["basic"] = self._analyze_basic(img, pil_img)
        
        # LAYER 2: Text Extraction (OCR)
        if self.ocr_available:
            result["layers"]["text"] = self._extract_text(img)
        else:
            result["layers"]["text"] = {"status": "OCR not available"}
        
        # LAYER 3: Visual Structure
        result["layers"]["structure"] = self._analyze_structure(img)
        
        # LAYER 4: Color Analysis
        result["layers"]["colors"] = self._analyze_colors(img, pil_img)
        
        # LAYER 5: Pattern Recognition
        result["layers"]["patterns"] = self._analyze_patterns(img)
        
        # LAYER 6: Synthesized Understanding
        result["layers"]["understanding"] = self._synthesize_understanding(result["layers"])
        
        return result
    
    def _analyze_basic(self, img: np.ndarray, pil_img: Image.Image) -> Dict:
        """Layer 1: Basic image properties"""
        height, width = img.shape[:2]
        file_size = os.path.getsize(pil_img.filename) / (1024 * 1024)  # MB
        
        return {
            "dimensions": {"width": width, "height": height},
            "aspect_ratio": round(width / height, 2),
            "file_size_mb": round(file_size, 2),
            "channels": img.shape[2] if len(img.shape) > 2 else 1,
            "format": pil_img.format,
            "mode": pil_img.mode
        }
    
    def _extract_text(self, img: np.ndarray) -> Dict:
        """Layer 2: Extract all text using OCR"""
        if not self.ocr_available:
            return {"status": "OCR not available"}
        
        try:
            # Preprocess for better OCR
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Enhance contrast
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            enhanced = clahe.apply(gray)
            
            # Try different preprocessing
            # Method 1: Direct OCR
            text1 = pytesseract.image_to_string(enhanced, config='--psm 6')
            
            # Method 2: Threshold
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            text2 = pytesseract.image_to_string(thresh, config='--psm 6')
            
            # Get detailed data with bounding boxes
            data = pytesseract.image_to_data(enhanced, output_type=pytesseract.Output.DICT)
            
            # Extract text with confidence
            texts = []
            for i in range(len(data['text'])):
                if int(data['conf'][i]) > 0:
                    text = data['text'][i].strip()
                    if text:
                        texts.append({
                            "text": text,
                            "confidence": int(data['conf'][i]),
                            "x": data['left'][i],
                            "y": data['top'][i],
                            "width": data['width'][i],
                            "height": data['height'][i]
                        })
            
            # Combine text
            combined_text = text1 + " " + text2
            combined_text = re.sub(r'\s+', ' ', combined_text).strip()
            
            return {
                "full_text": combined_text,
                "text_blocks": texts,
                "word_count": len(combined_text.split()),
                "text_regions": len(texts)
            }
        except Exception as e:
            return {"error": str(e), "status": "OCR failed"}
    
    def _analyze_structure(self, img: np.ndarray) -> Dict:
        """Layer 3: Analyze visual structure (edges, regions, layout)"""
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        height, width = gray.shape
        
        # Edge detection
        edges = cv2.Canny(gray, 50, 150)
        edge_density = np.sum(edges > 0) / (width * height)
        
        # Find contours (UI element boundaries)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filter significant contours
        significant_contours = [c for c in contours if cv2.contourArea(c) > 100]
        
        # Analyze layout regions (divide into grid)
        grid_regions = self._analyze_grid_regions(gray)
        
        return {
            "edge_density": round(edge_density, 4),
            "contour_count": len(contours),
            "significant_regions": len(significant_contours),
            "layout_grid": grid_regions,
            "has_clear_structure": edge_density > 0.1
        }
    
    def _analyze_grid_regions(self, gray: np.ndarray) -> Dict:
        """Divide image into grid regions and analyze each"""
        height, width = gray.shape
        
        # Divide into 3x3 grid
        grid = {"regions": []}
        region_h = height // 3
        region_w = width // 3
        
        for i in range(3):
            for j in range(3):
                y1 = i * region_h
                y2 = (i + 1) * region_h if i < 2 else height
                x1 = j * region_w
                x2 = (j + 1) * region_w if j < 2 else width
                
                region = gray[y1:y2, x1:x2]
                mean_brightness = np.mean(region)
                std_brightness = np.std(region)
                
                grid["regions"].append({
                    "position": f"{i},{j}",
                    "bounds": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
                    "mean_brightness": round(mean_brightness, 2),
                    "std_brightness": round(std_brightness, 2),
                    "has_content": std_brightness > 20  # High variation = content
                })
        
        return grid
    
    def _analyze_colors(self, img: np.ndarray, pil_img: Image.Image) -> Dict:
        """Layer 4: Analyze colors and visual themes"""
        # Convert to RGB for analysis
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Get dominant colors using k-means
        pixels = rgb_img.reshape(-1, 3)
        pixels = np.float32(pixels)
        
        # K-means clustering for dominant colors
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        k = 5  # Find 5 dominant colors
        _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        
        # Count color frequencies
        unique, counts = np.unique(labels, return_counts=True)
        color_freq = dict(zip(unique, counts))
        
        # Get dominant colors
        dominant_colors = []
        for i, center in enumerate(centers):
            freq = color_freq.get(i, 0)
            percentage = (freq / len(pixels)) * 100
            dominant_colors.append({
                "rgb": [int(c) for c in center],
                "percentage": round(percentage, 2)
            })
        
        # Sort by frequency
        dominant_colors.sort(key=lambda x: x["percentage"], reverse=True)
        
        # Get image statistics
        stat = ImageStat.Stat(pil_img)
        
        return {
            "dominant_colors": dominant_colors[:3],  # Top 3
            "mean_color": [int(c) for c in stat.mean],
            "brightness": round(np.mean(stat.mean), 2),
            "color_variance": round(np.mean(stat.stddev), 2),
            "is_dark": np.mean(stat.mean) < 128,
            "is_bright": np.mean(stat.mean) > 200
        }
    
    def _analyze_patterns(self, img: np.ndarray) -> Dict:
        """Layer 5: Recognize patterns (UI consistency, layout)"""
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        height, width = gray.shape
        
        # Detect horizontal and vertical lines (UI structure)
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
        vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))
        
        # Detect lines
        horizontal_lines = cv2.morphologyEx(gray, cv2.MORPH_OPEN, horizontal_kernel)
        vertical_lines = cv2.morphologyEx(gray, cv2.MORPH_OPEN, vertical_kernel)
        
        h_line_count = np.sum(horizontal_lines > 0) / (width * height)
        v_line_count = np.sum(vertical_lines > 0) / (width * height)
        
        # Detect buttons/UI elements (rectangular regions)
        edges = cv2.Canny(gray, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Find rectangular regions (potential buttons/UI elements)
        rectangles = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Significant size
                x, y, w, h = cv2.boundingRect(contour)
                aspect_ratio = w / h if h > 0 else 0
                # Button-like shapes (roughly rectangular)
                if 0.5 < aspect_ratio < 3.0:
                    rectangles.append({
                        "x": int(x), "y": int(y),
                        "width": int(w), "height": int(h),
                        "area": int(area)
                    })
        
        return {
            "has_horizontal_structure": h_line_count > 0.01,
            "has_vertical_structure": v_line_count > 0.01,
            "ui_elements_detected": len(rectangles),
            "ui_element_positions": rectangles[:10],  # Top 10
            "layout_type": self._classify_layout(h_line_count, v_line_count, len(rectangles))
        }
    
    def _classify_layout(self, h_lines: float, v_lines: float, elements: int) -> str:
        """Classify layout type based on patterns"""
        if h_lines > 0.02 and v_lines > 0.02:
            return "grid_layout"
        elif h_lines > 0.02:
            return "horizontal_layout"
        elif v_lines > 0.02:
            return "vertical_layout"
        elif elements > 5:
            return "ui_rich"
        else:
            return "simple_layout"
    
    def _synthesize_understanding(self, layers: Dict) -> Dict:
        """Layer 6: Synthesize all information into understanding"""
        understanding = {
            "description": "",
            "ui_elements": [],
            "text_content": "",
            "visual_theme": "",
            "game_state": "unknown"
        }
        
        # Extract text
        if "text" in layers and "full_text" in layers["text"]:
            understanding["text_content"] = layers["text"]["full_text"]
            understanding["description"] += f"Text found: {layers['text']['full_text'][:200]}... "
        
        # Extract UI elements
        if "patterns" in layers and "ui_element_positions" in layers["patterns"]:
            understanding["ui_elements"] = layers["patterns"]["ui_element_positions"]
            understanding["description"] += f"Detected {len(layers['patterns']['ui_element_positions'])} UI elements. "
        
        # Visual theme
        if "colors" in layers:
            colors = layers["colors"]
            if colors.get("is_dark"):
                understanding["visual_theme"] = "dark_theme"
            elif colors.get("is_bright"):
                understanding["visual_theme"] = "bright_theme"
            else:
                understanding["visual_theme"] = "medium_theme"
            understanding["description"] += f"Visual theme: {understanding['visual_theme']}. "
        
        # Layout
        if "patterns" in layers and "layout_type" in layers["patterns"]:
            understanding["description"] += f"Layout: {layers['patterns']['layout_type']}. "
        
        # Try to infer game state from text
        if understanding["text_content"]:
            text_lower = understanding["text_content"].lower()
            if any(word in text_lower for word in ["menu", "start", "play"]):
                understanding["game_state"] = "menu"
            elif any(word in text_lower for word in ["level", "tutorial", "complete"]):
                understanding["game_state"] = "gameplay"
            elif any(word in text_lower for word in ["settings", "options"]):
                understanding["game_state"] = "settings"
        
        return understanding
    
    def analyze_directory(self, directory: str, output_file: Optional[str] = None) -> List[Dict]:
        """Analyze all images in a directory"""
        folder = Path(directory)
        if not folder.exists():
            print(f"❌ Folder not found: {directory}")
            return []
        
        # Find all image files
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}
        images = sorted([
            f for f in folder.iterdir()
            if f.suffix.lower() in image_extensions
        ])
        
        if not images:
            print(f"⚠️  No images found in {directory}")
            return []
        
        print(f"📁 Found {len(images)} images")
        print(f"🔍 Starting blind analysis...\n")
        
        results = []
        for i, img_path in enumerate(images, 1):
            print(f"[{i}/{len(images)}] ", end="")
            try:
                result = self.analyze_image(str(img_path))
                results.append(result)
                print("✅")
            except Exception as e:
                print(f"❌ Error: {e}")
                results.append({
                    "filename": img_path.name,
                    "error": str(e)
                })
        
        if output_file:
            # Convert numpy types to native Python types for JSON serialization
            def convert_numpy(obj):
                if isinstance(obj, np.integer):
                    return int(obj)
                elif isinstance(obj, np.floating):
                    return float(obj)
                elif isinstance(obj, np.ndarray):
                    return obj.tolist()
                elif isinstance(obj, (np.bool_, bool)):
                    return bool(obj)
                elif isinstance(obj, dict):
                    return {key: convert_numpy(value) for key, value in obj.items()}
                elif isinstance(obj, list):
                    return [convert_numpy(item) for item in obj]
                return obj
            
            results_serializable = [convert_numpy(r) for r in results]
            
            with open(output_file, 'w') as f:
                json.dump(results_serializable, f, indent=2)
            print(f"\n💾 Results saved to: {output_file}")
        
        return results


if __name__ == "__main__":
    analyzer = BlindImageAnalyzer()
    
    folder_path = "/Users/rashadwest/Desktop/BallCODE screenshots"
    output_file = "ballcode_blind_analysis.json"
    
    print("=" * 60)
    print("BLIND IMAGE ANALYZER - AIMCODE Approach")
    print("Analyzing images like a blind person would need to 'see'")
    print("=" * 60)
    print()
    
    results = analyzer.analyze_directory(folder_path, output_file)
    
    print(f"\n✅ Analysis complete! Analyzed {len(results)} images")
    print(f"📄 Results saved to: {output_file}")

