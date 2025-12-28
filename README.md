# 🖐️ Jetson Hand Gesture Recognition

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-NVIDIA%20Jetson%20%7C%20Windows-green)
![Library](https://img.shields.io/badge/Library-MediaPipe-orange)

A lightweight, real-time hand gesture recognition system optimized for **NVIDIA Jetson** devices (Nano, Orin) using MediaPipe and OpenCV.

## ✨ Features
- **Real-time Detection**: Extremely fast hand tracking using MediaPipe's lightweight model.
- **Gesture Classification**: Detects basic gestures:
  - ✋ **Open Hand** (Hello)
  - ✊ **Fist** (Closed)
  - ✌️ **Peace** (Victory)
  - ☝️ **Pointing** (Index finger)
- **Jetson Optimized**: Configured to run smoothly on ARM64 architecture with low resource usage.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Webcam

> **No Hardware?** Read [How to Practice without Jetson](docs/NHUNG_DIEU_CAN_BIET.md#6-lộ-trình-thực-hành-khi-chưa-có-jetson).

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/JetsonHandGesture.git
   cd JetsonHandGesture
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: This uses specific versions of MediaPipe and Protobuf to ensure compatibility with Jetson/ARM64 and avoid Numpy 2.0 conflicts).*

### Usage
Run the main script:
```bash
python src/hand_gesture.py
```
- Press **'q'** to exit the application.

## 📖 Deployment on Jetson
For detailed instructions on setting up your NVIDIA Jetson device (installing system dependencies, performance tuning), please read the [Deployment Guide](docs/deployment_guide.md).

## 🛠️ Tech Stack
- **OpenCV**: Image capture and drawing.
- **MediaPipe**: Hand landmark detection.
- **Python**: Core logic.

---
*Created for the Edge AI community.*
