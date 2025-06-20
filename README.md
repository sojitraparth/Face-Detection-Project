# 🧠 Face Detection Project using OpenCV

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-blue.svg)
![WebP Support](https://img.shields.io/badge/WebP-Supported-green)

A lightweight Python project that detects faces in images (including `.webp`) and real-time from a webcam using OpenCV’s Haar Cascade classifier.

---

## 🎯 Features

✅ Detect faces in images  
✅ Real-time webcam detection  
✅ WebP image support  
✅ Matplotlib-based result display  
✅ Simple, fast, and beginner-friendly

---

## 📂 Project Structure
Face-Detection-Project/
├── face_detection.py         # Main detection script
├── test.webp                 # Sample image
├── requirements.txt          # Dependencies
├── README.md                 # Project info
└── .gitignore

---

## 🚀 Quick Start

### 📦 Install Dependencies

```bash
pip install -r requirements.txt

🖼️ Run Face Detection on Image
python3 face_detection.py

📷 Enable Webcam Detection (Optional)

In face_detection.py, uncomment:
# detect_faces_webcam()
Then run:python3 face_detection.py

📸 Input Format

This project supports:
• .jpg, .png, .jpeg
• ✅ .webp (yes!)
• Live webcam input
💡 Built With
• OpenCV
• Matplotlib

📄 License

This project is licensed under the MIT License.
