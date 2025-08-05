# Face and Eye Tracker

A simple Python script to detect faces and eyes in real-time using OpenCV. The script alerts the user if their eyes stay closed for too long — perfect for basic drowsiness detection.

---

## Features

- Face detection with blue bounding box  
- Open eyes detection with green box  
- Closed eyes detection with red box and alert  
- Terminal print of eye-closed duration (>1 sec)  
- On-screen warning if eyes stay closed for 3+ seconds

---

Install dependencies:

```
pip install opencv-python
```

Run the Code:
```
python face.py
```
Press ```q``` to quit the window

---

## Use Cases
- Drowsiness detection
- Simple alertness tracker
- Prototype for eye-based control systems
