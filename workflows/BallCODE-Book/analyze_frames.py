#!/usr/bin/env python3
import cv2
import numpy as np
import os

# Analyze key frames to understand the game
key_frames = [0, 10, 30, 60, 90, 120, 150]
frame_dir = "video_frames"

print("Analyzing key frames from BallCODE_Addy video...\n")

for frame_num in key_frames:
    frame_path = os.path.join(frame_dir, f"frame_{frame_num:04d}.png")
    
    if not os.path.exists(frame_path):
        continue
    
    img = cv2.imread(frame_path)
    if img is None:
        continue
    
    height, width = img.shape[:2]
    
    # Convert to grayscale for analysis
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect text regions (high contrast areas)
    edges = cv2.Canny(gray, 50, 150)
    text_regions = np.sum(edges > 0) / (width * height) * 100
    
    # Detect UI elements (rectangular regions)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rectangles = [c for c in contours if len(cv2.approxPolyDP(c, 0.02*cv2.arcLength(c, True), True)) == 4]
    
    # Color analysis
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    dominant_colors = []
    for i in range(0, width, width//10):
        for j in range(0, height, height//10):
            pixel = hsv[j, i]
            dominant_colors.append(pixel[0])  # Hue
    
    avg_hue = np.mean(dominant_colors)
    
    print(f"Frame {frame_num} ({frame_num}s):")
    print(f"  Resolution: {width}x{height}")
    print(f"  Text/UI density: {text_regions:.1f}%")
    print(f"  UI rectangles detected: {len(rectangles)}")
    print(f"  Dominant color (hue): {avg_hue:.0f}°")
    print()

print("\nAnalysis complete!")
print("\nTo see the actual frames, you can:")
print("1. Open the video_frames/ directory in Finder")
print("2. Or I can create a summary based on your description")




