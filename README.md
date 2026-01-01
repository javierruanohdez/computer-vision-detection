# 🚗 Vehicle Detection & Counting with OpenCV

![Vehicle Detection](https://img.shields.io/badge/OpenCV-Python-blue?logo=opencv) ![Python](https://img.shields.io/badge/Python-3.10-green?logo=python)

A **real-time vehicle detection and counting system** using OpenCV. This project tracks vehicles across multiple lanes, highlights anomalous vehicles, and visualizes traffic flow in videos with clear overlays. Perfect for **traffic analysis, AI experimentation, and computer vision learning**.

---

## 🔍 Features

* ✅ Detects vehicles in traffic videos using **background subtraction and contour detection**
* ✅ Tracks vehicles and assigns unique IDs to each
* ✅ Counts vehicles crossing multiple lanes and detects anomalies
* ✅ Visualizes traffic lanes, polygons, and detected vehicles with colored bounding boxes
* ✅ Real-time processing and display (works on local videos)

---

## 🎬 Demo

**Example usage**:

![Vehicle Detection Demo](https://user-images.githubusercontent.com/placeholder/demo.gif)

* Blue, green, yellow lanes count vehicles separately
* Red boxes indicate anomalous or special vehicles
* Overlay polygons highlight areas of interest

---

## ⚙️ Installation

1. Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/vehicle-detection.git
cd vehicle-detection
```

2. Install required Python packages:

```bash
pip install -r requirements.txt
```

3. Make sure you have a test video (e.g., `traffic_video.mp4`) in the repo folder.

---

## 🛠 Usage

Run the main detection script:

```bash
python vehicle_detection.py
```

* The script will read the video, detect and track vehicles, and display real-time counts on screen.
* Press **Esc** to exit the video window.

---

## 📂 Project Structure

```
computer-vision-detection/
│
├─ vehicle_detection.py    # Main detection script
├─ vehicle.py              # Vehicle class for tracking
├─ traffic_video.mp4       # Sample video (small resolution recommended)
├─ requirements.txt        # Dependencies
└─ README.md
```

---

## 💡 How It Works

1. **Background Subtraction:** Detect moving objects in the video
2. **Contour Detection:** Identify bounding boxes around vehicles
3. **Vehicle Tracking:** Assign unique IDs and track centroids across frames
4. **Counting Logic:** Count vehicles crossing predefined lines for each lane
5. **Anomaly Detection:** Detect vehicles that cross certain zones or lanes abnormally

---

## 🏗 Future Improvements

* Integrate **YOLO or other deep learning detectors** for higher accuracy
* Add **speed estimation** of vehicles
* Support **live camera streams**
* Export traffic counts to CSV or JSON for analysis

---

## 📌 References

* [OpenCV Documentation](https://opencv.org/)
* [Python](https://www.python.org/)
* [Background Subtraction Techniques](https://docs.opencv.org/4.x/d1/dc5/tutorial_background_subtraction.html)

---

## 🚀 Contribution

Feel free to fork this repository, suggest improvements, or submit pull requests!
