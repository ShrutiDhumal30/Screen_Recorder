# Screen_Recorder
Screen Recorder using the python

📁 Features:

Records the full screen

Saves video in .mp4 or .avi format

Configurable frame rate

Easy to use and lightweight

⚙️ Requirements:
Python 3.10 or 3.11 (❗Avoid Python 3.13 for compatibility)
Required Python Libraries:
opencv-python
pyautogui
numpy
pillow
pyscreeze
pywin32 (for GetSystemMetrics on Windows)

#Install the following packages:
pip install opencv-python pyautogui numpy pillow pywin32

#How to run:
The screen will be recorded for 24 seconds by default.
The output file (test.mp4) will be saved in the project directory

📁 Output
By default, video is saved as:

test.mp4 (when using "mp4v" codec)
Or test.avi (when using "XVID" codec)

❗ Troubleshooting
If you encounter the error:
PyAutoGUIException: Unable to import pyscreeze or pillow
Make sure you're not using Python 3.13. Downgrade to Python 3.11 or install pre-release versions:

pip install pillow --pre
pip install pyscreeze --pre




