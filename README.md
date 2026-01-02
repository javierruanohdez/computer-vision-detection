# 🚗 Vehicle Detection & Counting with OpenCV

![OpenCV + Python](https://img.shields.io/badge/OpenCV-Python%203.13-blue?logo=opencv)

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

![Vehicle Detection Demo](demo_video.gif)

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

2. Create a virtual environment (optional but recommended):

```bash
python -m venv vehicle-env
vehicle-env\Scripts\activate      # Windows
source vehicle-env/bin/activate   # macOS/Linux
```

3. Install required Python packages:

```bash
pip install -r requirements.txt
```

4. Make sure you have a test video (e.g., `traffic_video.mp4`) in the repo folder.

---

## 🛠 Usage

Open the Jupyter Notebook `vehicle_detection.ipynb`:

1. Start Jupyter Notebook:

```bash
jupyter notebook
```

2. In the browser, navigate to `vehicle_detection.ipynb` and open it.
3. Run the notebook cells **in order**:

* The video will be read, vehicles will be detected and tracked, and counts for each lane will be displayed.

---

## 📂 Project Structure

```
computer-vision-detection/
│
├─ vehicle_detection.py    # Main detection script
├─ vehicle.py              # Vehicle class for tracking
├─ traffic_video.mp4       # Sample video (small resolution recommended)
├─ demo_video.gif          # Tracking demo
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
