## Cursor on your fingers
This Python project allows you to control your computer's cursor using hand gestures. The index finger is used to move the cursor, and a pinch gesture (bringing the thumb and index finger together) is used to simulate a mouse click.
# Features
- Cursor Control: Move the cursor by moving your index finger in front of the camera.
- Click Simulation: Perform a left-click by pinching your thumb and index finger together.
# Requirements
- Python 3.6
- Web camera for capturing hand gestures
# Dependencies
The following Python libraries are required:
- `numpy`
- `opencv-python`
- `pyautogui`
- `mediapipe`
You can install these by using the requirement.txt file provided
## Installation
# 1.Clone the repository
```
git clone git@github.com:lordShandilya/Cursor-on-your-fingers.git
cd Cursor-on-your-fingers
```
# 2.Create and Activate a Virtual Environment (Optional but Recommended)
On Windows
```
python -m venv env
.\env\Scripts\activate
```
On Mac/Linux
```
python3 -m venv env
source env/bin/activate
```
# 3. Install the Dependencies
```
pip install -r requirements.txt
```
# 4.Run the script
```
python main.py
```
# How it works
* Hand Detection: The script uses MediaPipe to detect hands in the camera feed.
* Finger Tracking: The index finger's position is tracked in real-time to control the cursor.
* Click Detection: When the distance between the thumb and index finger decreases (a pinch gesture), the script simulates a mouse click using `pyautogui`.
# Usage
- Cursor Movement: Move your index finger in front of the camera to control the cursor.
- Click: Pinch your thumb and index finger together to click.
# Troubleshooting
- Ensure your web camera is working and accessible.
- If the cursor movement is laggy, reduce the camera resolution or ensure proper lighting.
- Install the correct version of Python (3.6+) and make sure all dependencies are installed.
# Contribution
If you want to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are welcome!
# Acknowledgments
- MediaPipe for hand tracking
- OpenCV for image processing
- PyAutoGUI for controlling the mouse cursor

