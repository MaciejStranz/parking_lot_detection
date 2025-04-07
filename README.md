# 🚗 Parking Spot Occupancy Analysis using YOLO and SSD

This project aims to analyze parking spot occupancy based on bird's-eye view images using state-of-the-art object detection methods – **YOLO** and **SSD**. Images of parking lots under various weather conditions and from different angles are processed, and the output is a visual representation of occupancy along with numerical information.

## 📌 Motivation

Efficient parking management directly impacts:
- traffic flow,
- air pollution,
- and residents' quality of life.

The goal of the project is to build a system that automatically detects and evaluates parking spot occupancy, and enables analysis of parking patterns.

---

## 🗂️ Input and Output Data

**Input Data:**
- Drone images (various angles and weather conditions)
- Dataset: **PKLot**

**Output Data:**
- Image with bounding boxes overlaid on parking spots
- Color indicators: `occupied` / `vacant`
- Numerical output showing count of occupied and free spots

---

## 🧾 Dataset: PKLot

The **PKLot** dataset includes:

- 12,416 JPEG images (1280×720 px)
- 695,335 manually labeled parking spots
  - 48.6% occupied
  - 51.4% vacant
- Data from two parking lots, three different angles
- Weather labels: `sunny`, `rainy`, `cloudy`
- Split:
  - 70% training
  - 20% validation
  - 10% test

Sample image from the dataset:

![PKLot example](original.jpg)

---

## ⚙️ Methods Used

### 🧠 You Only Look Once (YOLO)

YOLO is a fast, single-shot object detection network. It works by dividing the image into a grid, where each cell predicts object positions and classes.

#### YOLO Advantages:
- ⚡ Very fast (real-time)
- 🎯 High accuracy
- 🔄 Considers full image context
- 📉 Fewer false positives

#### Process:
1. Divide image into grid
2. Predict bounding boxes + class scores
3. Scale boxes
4. Apply Non-Maximum Suppression (NMS)

YOLO performs well in detecting parking spots in PKLot images – handling various angles, sizes, and complex backgrounds.

---

### 📦 Single Shot MultiBox Detector (SSD)

SSD is also a single-shot detector based on convolutional feature maps and default anchor boxes of various sizes and aspect ratios.

#### Architecture:
- Feature extractor (e.g., VGG16, ResNet)
- Multibox layers (predict class + bounding box offsets)

#### Process:
1. Extract feature maps
2. Apply anchors (default boxes)
3. Predict class scores and offsets
4. Apply Non-Maximum Suppression (NMS)

#### SSD Advantages:
- 🔥 Real-time performance
- 🧩 Detects objects at multiple scales
- 🛠️ Simple to implement

In this project, SSD effectively identifies parking spots regardless of scale or perspective, offering a good trade-off between speed and precision.

---

## 🧪 Dataset Split

| Set         | Number of Images | Percentage |
|-------------|------------------|------------|
| Training    | 6891             | 70%        |
| Validation  | 2483             | 20%        |
| Test        | 1242             | 10%        |

---

## 📊 YOLO Model Results

The **YOLO** model achieved high accuracy in detecting parking spots, especially for medium and large objects.

### Average Precision (AP):
- **AP (IoU=0.50:0.95)**: `0.833` – solid overall performance.
- **AP (IoU=0.50)**: `0.986` – excellent detection with looser IoU thresholds.
- **AP (IoU=0.75)**: `0.979` – maintains high precision under stricter thresholds.
- **AP (medium)**: `0.832` – good performance on medium-sized objects.
- **AP (large)**: `0.857` – effective detection of larger objects.

### Average Recall (AR):
- **AR (maxDets=1)**: `0.026` – limited recall for single detections.
- **AR (maxDets=10)**: `0.217` – improved with more detections.
- **AR (maxDets=100)**: `0.877` – strong recall at full detection scale.
- **AR (medium)**: `0.877`
- **AR (large)**: `0.889`

### Summary:
YOLO shows very high precision across different IoU thresholds and solid performance with larger detection counts. It's well-suited for real-world parking monitoring systems.

---

## 📊 SSD Model Results

The **SSD** model achieved even higher results in several metrics, especially for medium and large objects.

### Average Precision (AP):
- **AP (IoU=0.50:0.95)**: `0.904` – excellent overall accuracy.
- **AP (IoU=0.50)**: `0.984` – very high precision.
- **AP (IoU=0.75)**: `0.979` – consistent precision across thresholds.
- **AP (small)**: `0.834` – solid performance for small objects.
- **AP (medium)**: `0.931`
- **AP (large)**: `0.984`

### Average Recall (AR):
- **AR (maxDets=1)**: `0.028` – limited at single-object detection.
- **AR (maxDets=10)**: `0.231` – slight improvement.
- **AR (maxDets=100)**: `0.931` – excellent performance with full detections.
- **AR (small)**: `0.872`
- **AR (medium)**: `0.957`
- **AR (large)**: `0.992`

### Summary:
The SSD model shows **exceptional accuracy and recall**, particularly in detecting medium and large objects. Thanks to its high AP and AR values, it’s a strong candidate for precise parking detection applications.

---

## 🏁 Conclusion

Both models – **YOLO** and **SSD** – achieved very high performance in detecting parking spot occupancy. However:

- YOLO performs better across varying IoU values but has slightly lower recall.
- SSD excels in both precision and recall for medium and large objects.

The model choice depends on the specific use case: SSD may be preferred for highly accurate full-detection systems, while YOLO is ideal for fast, lightweight applications.

---
