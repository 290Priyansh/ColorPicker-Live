# 🎨 ColorPicker-Live

An interactive real-time color detection tool using HSV color space.  
Click on any pixel in the webcam feed to instantly detect and highlight similar colors — no manual slider tuning needed!

---

## 🚀 Features

- 📸 **Live Webcam Feed**: Real-time image processing using OpenCV.
- 🎯 **Pixel-Based Color Picker**: Click on any pixel to auto-adjust HSV sliders.
- 🎚️ **Dynamic HSV Range Control**: Sliders for fine-tuning hue, saturation, and value.
- 🎭 **Color Masking**: Isolates and displays selected color range in real time.
- 🪞 **Mirrored Display**: Natural selfie-style viewing.
- 🧪 **Console Output**: Displays HSV values of the picked color.

---

## 🖱️ How It Works

- The webcam feed is split into two views:
  - **Left**: Original video.
  - **Right**: Only the selected color range.
- Use your mouse to click anywhere on the **left** side (original frame).
- The HSV sliders will **automatically update** based on that pixel's color.
- You can further refine detection using the sliders.

---
##🛠 Tech Stack
-Python 🐍.
-OpenCV 🎥.
-NumPy 🔢.

---
##🧠 Use Cases
-Live object color filtering.
-Simple color segmentation projects.
-Educational demos of HSV color space.
-Building blocks for AR, tracking, and visual detection tools.

