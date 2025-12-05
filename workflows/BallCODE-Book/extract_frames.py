#!/usr/bin/env python3
import cv2
import os

# Video file path
video_path = "BallCODE_Addy.mov"
output_dir = "video_frames"

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    exit(1)

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps if fps > 0 else 0

print(f"Video info:")
print(f"  FPS: {fps:.2f}")
print(f"  Total frames: {total_frames}")
print(f"  Duration: {duration:.2f} seconds")
print(f"\nExtracting frames (1 per second)...")

frame_count = 0
saved_count = 0
target_fps = 1  # Extract 1 frame per second

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Save frame if it matches our target interval (1 per second)
    if frame_count % int(fps) == 0:
        output_path = os.path.join(output_dir, f"frame_{saved_count:04d}.png")
        cv2.imwrite(output_path, frame)
        saved_count += 1
        print(f"  Saved frame {saved_count} (at {frame_count/fps:.1f}s)")
    
    frame_count += 1

cap.release()
print(f"\nDone! Extracted {saved_count} frames to '{output_dir}/' directory")




