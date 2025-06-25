# 🛡 Protective Equipment (PPE) Detection System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![YOLOv5](https://img.shields.io/badge/YOLOv5-PPE--Detection-green.svg)](https://github.com/ultralytics/yolov5)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/aaryan2720/Protective-Equipment-PPE-detection-system)](https://github.com/aaryan2720/Protective-Equipment-PPE-detection-system/stargazers)
[![Forks](https://img.shields.io/github/forks/aaryan2720/Protective-Equipment-PPE-detection-system.svg)](https://github.com/aaryan2720/Protective-Equipment-PPE-detection-system/network/members)

> A real-time Personal Protective Equipment (PPE) detection system powered by *YOLOv5* and *OpenCV*. This tool detects safety gear like helmets and vests in videos to ensure workplace compliance.

---

## 📸 Demo Preview

![Demo of PPE Detection](https://github.com/aaryan2720/Protective-Equipment-PPE-detection-system/raw/main/demo-image.jpg)

> 📝 Replace the above image with a real screenshot from your video or output

---

## 📁 Project Structure

Protective-Equipment-PPE-detection-system/
├── .vscode/ # VSCode settings (optional)
├── Yolo-Weights/ # YOLOv5 model weights
│ └── ppe.pt # Trained PPE model
├── d.py # Main Python detection script
├── ppe-2.mp4 # Sample test video
├── requirement.txt # Python requirements

yaml
Copy
Edit

---

## 🚀 Features

- Detects multiple PPE items (e.g. helmets, vests)
- Real-time detection with bounding boxes
- Works on images, videos, or webcam feed
- Lightweight and fast with YOLOv5

---

## 🧠 Model Info

- Custom trained on PPE dataset
- Framework: *PyTorch*
- Detection backbone: *YOLOv5*
- Model file: ppe.pt

---

## 🛠 Setup & Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/aaryan2720/Protective-Equipment-PPE-detection-system.git
cd Protective-Equipment-PPE-detection-system
2️⃣ Create virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirement.txt
4️⃣ Download YOLOv5 (if not already)
bash
Copy
Edit
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
🎥 Usage
Run detection on video:

bash
Copy
Edit
python d.py
Make sure the model weights (ppe.pt) are correctly placed in the path referenced by the script.

📦 Requirements
Python 3.8+

OpenCV

torch

numpy

YOLOv5

Install everything using:

bash
Copy
Edit
pip install -r requirement.txt
