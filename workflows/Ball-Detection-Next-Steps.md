# Ball Detection Model — Next Steps

**Last Updated:** January 2025  
**Status:** Workflow Configured — Ready for Implementation  
**Focus:** Basketball and Player Detection (YOLOv8)

---

## Current Configuration Summary

✅ **Class Filter:** "basketball" and "player" classes active  
✅ **Visualization:** Bounding boxes with labels and confidence scores  
✅ **Color Coding:** Basketball (Orange #FFA500), Player (Teal #008080)  
✅ **Export Format:** YOLOv8, 640x640, 70/20/10 split  
✅ **Preprocessing:** Auto-orient and Resize enabled

---

## Phase 1: Dataset Preparation & Quality Assurance

### 1.1 Annotation Review & Quality Check

**Priority: High | Timeline: 1-2 weeks**

- [ ] **Review annotation coverage**
  - Verify minimum 100-200 annotated images per class (basketball, player)
  - Check for class imbalance (aim for balanced representation)
  - Ensure diverse scenarios: different angles, lighting, court positions

- [ ] **Quality validation**
  - Spot-check 10-15% of annotations for accuracy
  - Verify bounding boxes are tight (minimal padding)
  - Check for missing detections (false negatives)
  - Identify and fix mislabeled classes

- [ ] **Edge case identification**
  - Occluded basketballs (behind players, in hands)
  - Small basketballs (far from camera)
  - Multiple basketballs in frame (rare but possible)
  - Players partially out of frame
  - Different camera angles (sideline, baseline, overhead)

### 1.2 Dataset Augmentation Strategy

**Priority: Medium | Timeline: Ongoing**

- [ ] **Roboflow augmentation settings** (if using Roboflow training)
  - Rotation: ±15 degrees
  - Brightness: ±20%
  - Saturation: ±20%
  - Blur: 0-2px (simulate motion)
  - Mosaic: Enable (YOLOv8 default)

- [ ] **Manual augmentation considerations**
  - Different lighting conditions
  - Various court surfaces/colors
  - Different ball colors (if applicable)
  - Multiple camera perspectives

### 1.3 Dataset Export & Verification

**Priority: High | Timeline: 1 day**

- [ ] **Export from Roboflow**
  1. Navigate to project → Generate → New Version
  2. Apply settings:
     - Format: YOLOv8
     - Image Size: 640x640
     - Preprocessing: Auto-orient ✓, Resize ✓
     - Splits: 70% Train / 20% Val / 10% Test
  3. Download dataset
  4. Verify folder structure:
     ```
     dataset/
     ├── train/
     │   ├── images/
     │   └── labels/
     ├── valid/
     │   ├── images/
     │   └── labels/
     └── test/
         ├── images/
         └── labels/
     ```

- [ ] **Verify dataset integrity**
  - Check image-label pairing (same filenames)
  - Validate YOLO format (normalized coordinates 0-1)
  - Confirm class IDs match (basketball=0, player=1, or verify mapping)
  - Count images per split (should match 70/20/10 ratio)

---

## Phase 2: Model Training

### 2.1 Training Environment Setup

**Priority: High | Timeline: 1-2 days**

- [ ] **Install dependencies**
  ```bash
  pip install ultralytics
  # or
  pip install torch torchvision
  pip install yolov8
  ```

- [ ] **Verify GPU availability** (if using GPU)
  ```python
  import torch
  print(torch.cuda.is_available())
  print(torch.cuda.get_device_name(0))
  ```

- [ ] **Prepare training script**
  - Create `train_ball_detection.py` or use YOLOv8 CLI
  - Configure paths to train/valid directories
  - Set up logging and checkpoint saving

### 2.2 Initial Training Run

**Priority: High | Timeline: 2-4 hours (training time)**

- [ ] **Training configuration**
  ```python
  from ultralytics import YOLO
  
  model = YOLO('yolov8n.pt')  # or yolov8s.pt, yolov8m.pt
  
  results = model.train(
      data='path/to/dataset/data.yaml',
      epochs=100,
      imgsz=640,
      batch=16,  # Adjust based on GPU memory
      device=0,  # GPU device, or 'cpu'
      project='ball_detection',
      name='run1',
      save=True,
      plots=True
  )
  ```

- [ ] **Create data.yaml**
  ```yaml
  path: /path/to/dataset
  train: train/images
  val: valid/images
  test: test/images
  
  nc: 2  # number of classes
  names: ['basketball', 'player']
  ```

- [ ] **Monitor training**
  - Watch loss curves (train/val)
  - Check mAP50 and mAP50-95 metrics
  - Monitor for overfitting (val loss > train loss)
  - Save best model checkpoint

### 2.3 Hyperparameter Tuning

**Priority: Medium | Timeline: 1-2 weeks (iterative)**

- [ ] **Experiment with model sizes**
  - Start: YOLOv8n (nano) — fastest, least accurate
  - Try: YOLOv8s (small) — balanced
  - Try: YOLOv8m (medium) — better accuracy, slower
  - Choose based on speed/accuracy tradeoff

- [ ] **Adjust training parameters**
  - Learning rate: Start 0.01, try 0.001 or 0.0001
  - Batch size: Increase if GPU memory allows (16, 32, 64)
  - Epochs: 100-300 (stop early if validation plateaus)
  - Image size: 640 (current), try 1280 if accuracy needed

- [ ] **Use validation metrics to guide decisions**
  - mAP50 > 0.7 for basketball (target)
  - mAP50 > 0.8 for player (target)
  - Precision/Recall balance per class

---

## Phase 3: Model Evaluation & Validation

### 3.1 Test Set Evaluation

**Priority: High | Timeline: 1 day**

- [ ] **Run inference on test set**
  ```python
  model = YOLO('best.pt')  # Load best checkpoint
  results = model.val(data='path/to/dataset/data.yaml', split='test')
  ```

- [ ] **Analyze metrics**
  - Overall mAP50, mAP50-95
  - Per-class metrics (basketball, player)
  - Precision, Recall, F1-score per class
  - Confusion matrix

- [ ] **Visual inspection**
  - Sample 20-30 test images
  - Check for false positives (detections where no object exists)
  - Check for false negatives (missed detections)
  - Note failure patterns (occlusion, distance, angle)

### 3.2 Error Analysis

**Priority: High | Timeline: 2-3 days**

- [ ] **Categorize errors**
  - Basketball errors:
    - Missed when occluded
    - Missed when small/distant
    - False positives (circular objects mistaken for ball)
  - Player errors:
    - Missed partial players
    - Grouped multiple players as one
    - False positives (referees, coaches)

- [ ] **Create error dataset**
  - Collect 20-50 images with common errors
  - Re-annotate if needed
  - Add to training set for next iteration

### 3.3 Confidence Threshold Optimization

**Priority: Medium | Timeline: 1 day**

- [ ] **Test different confidence thresholds**
  - Default: 0.25
  - Try: 0.3, 0.4, 0.5 (higher = fewer false positives, more false negatives)
  - Plot Precision-Recall curve
  - Choose threshold based on use case:
    - High precision needed: 0.4-0.5
    - High recall needed: 0.25-0.3

---

## Phase 4: Model Deployment

### 4.1 Export for Deployment

**Priority: High | Timeline: 1 day**

- [ ] **Export model formats**
  ```python
  model = YOLO('best.pt')
  model.export(format='onnx')  # For cross-platform
  model.export(format='torchscript')  # For PyTorch
  model.export(format='tensorrt')  # For NVIDIA (if applicable)
  ```

- [ ] **Test exported model**
  - Verify inference speed
  - Check accuracy matches original
  - Test on target deployment hardware

### 4.2 Inference Pipeline Setup

**Priority: High | Timeline: 2-3 days**

- [ ] **Create inference script**
  - Load model
  - Apply class filter (basketball, player only)
  - Apply confidence threshold
  - Generate visualizations with color coding:
    - Basketball: Orange (#FFA500)
    - Player: Teal (#008080)

- [ ] **Batch processing**
  - Process video frames or image sequences
  - Save results (JSON, CSV, or annotated images)
  - Maintain frame/video metadata

- [ ] **Real-time processing** (if needed)
  - Optimize for FPS (frames per second)
  - Consider model quantization
  - Test on target hardware

### 4.3 Integration with Existing Systems

**Priority: Medium | Timeline: 1-2 weeks**

- [ ] **Connect to BallCODE game system** (if applicable)
  - Format detections for game input
  - Map detections to game logic
  - Test integration

- [ ] **API/Service setup** (if needed)
  - REST API for model inference
  - Input/output format specification
  - Error handling and logging

---

## Phase 5: Iteration & Improvement

### 5.1 Continuous Improvement Loop

**Priority: Ongoing**

- [ ] **Collect new data**
  - Identify failure cases in production
  - Gather diverse scenarios
  - Maintain annotation quality

- [ ] **Retrain periodically**
  - Add new annotated data
  - Fine-tune on specific failure cases
  - Monitor for model drift

- [ ] **A/B testing** (if applicable)
  - Compare model versions
  - Measure impact on downstream tasks
  - Roll out improvements gradually

### 5.2 Advanced Optimizations

**Priority: Low | Timeline: Future**

- [ ] **Model compression**
  - Quantization (INT8)
  - Pruning
  - Knowledge distillation

- [ ] **Multi-scale detection**
  - Test-time augmentation
  - Ensemble methods

- [ ] **Temporal consistency** (for video)
  - Track objects across frames
  - Smooth detections over time
  - Handle occlusions with tracking

---

## Success Metrics & Targets

### Minimum Viable Model
- [ ] Basketball mAP50 > 0.65
- [ ] Player mAP50 > 0.75
- [ ] Inference speed: >10 FPS on target hardware
- [ ] False positive rate < 5%

### Production-Ready Model
- [ ] Basketball mAP50 > 0.75
- [ ] Player mAP50 > 0.85
- [ ] Inference speed: >30 FPS on target hardware
- [ ] False positive rate < 2%
- [ ] Handles edge cases (occlusion, distance, angles)

---

## Quick Reference: Training Command

```bash
# Basic training
yolo detect train data=dataset/data.yaml model=yolov8n.pt epochs=100 imgsz=640

# With custom project name
yolo detect train data=dataset/data.yaml model=yolov8n.pt epochs=100 imgsz=640 project=ball_detection name=run1

# Validation only
yolo detect val data=dataset/data.yaml model=best.pt

# Inference on images
yolo detect predict model=best.pt source=path/to/images conf=0.25
```

---

## Resources & Documentation

- **YOLOv8 Documentation:** https://docs.ultralytics.com
- **Roboflow Export Guide:** https://docs.roboflow.com/exporting-data
- **YOLO Training Best Practices:** https://docs.ultralytics.com/modes/train/
- **Object Detection Metrics:** mAP, Precision, Recall explained

---

## Notes

- **Class Priority:** Both "basketball" and "player" are equally important for this workflow
- **Visualization:** Maintain color coding (Orange for basketball, Teal for player) in all outputs
- **Export Settings:** Must be configured in Roboflow UI (cannot be automated in workflow)
- **Iteration:** Plan for 2-3 training cycles before production deployment

---

*Last Updated: January 2025*  
*Next Review: After Phase 1 completion*





