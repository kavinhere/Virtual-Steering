# Virtual-Steering

## Hand Gesture Steering with OpenCV, MediaPipe, and KeyInput

This project utilizes **OpenCV**, **MediaPipe**, and **KeyInput** libraries to detect hand gestures from webcam input. The program is designed to recognize hand landmarks and control key inputs based on hand positions.

## Features

- **Real-time Hand Detection**: Uses a webcam feed to detect hand landmarks using MediaPipe’s hand tracking solution.
- **Wrist Tracking**: Tracks the position of the wrist to calculate the average coordinates between two hands.
- **Key Input Control**: Sends key inputs (`W`, `A`, `S`, `D`) based on the position of the hands, enabling gesture-based movement control.
- **Custom Gestures**: Single-hand detection triggers a "keeping back" gesture, while two-hand detection calculates midpoint and orientation.
  
## Requirements

To run this project, ensure you have the following dependencies installed:

```bash
pip install opencv-python
```
```bash
pip install mediapipe 
```
```bash
pip install keyinput
```
## Libraries Used
 - **OpenCV**: Used for capturing webcam input and displaying video output.
- **MediaPipe**: Used for hand landmark detection.
- **KeyInput**: Used to simulate keyboard key presses and releases.
- **Math**: For mathematical operations like calculating slopes and midpoint.

## How It Works
### Hand Detection:

 - MediaPipe detects hand landmarks, particularly focusing on the wrist position.
 - The program processes frames from the webcam and extracts the coordinates of the wrists for both hands.
### Two-Hand Gesture Recognition:

 - If both hands are detected, the midpoint between their wrists is calculated.
 - A circle is drawn at the midpoint and a slope (m) is calculated based on the wrist positions.
 - This information can be used for additional gesture controls or visualizations.

## Single-Hand Gesture Detection:

If only one hand is detected, the program sends a "keeping back" command by pressing the 'S' key and releasing 'A', 'D', and 'W'.

## Key Inputs:

Depending on the gesture, the appropriate key is pressed or released using keyinput.press_key() or keyinput.release_key().

## Installation
### Clone the repository:
```bash
git clone https://github.com/kavinhere/Virtual-Steering.git
```

## Install dependencies:
```bash
pip install -r requirements.txt
```
## Run the program:
```bash
Python Hand gesture steering.py
```
## Usage
 - **Start the program**: When the program starts, it captures video from your default webcam.
 - **Gesture control**: Move your hands in front of the camera to trigger gesture recognition.
    Move both hands to control gestures for movement.
    Use a single hand to trigger "keeping back" mode.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
