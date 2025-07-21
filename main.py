import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

#create variable as width and height , by using GetSystemMetrics we pass the value from which our video starts.
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dim = (width,height)

#create a variable to tell in which format you are going to make a video
f = cv2.VideoWriter_fourcc(*"mp4v")

#create variable to store the output i.e video and give the location to store the video.
output = cv2.VideoWriter("test.mp4",f,30.0,dim)

now_start_time = time.time()
duration = 20 + 4
end_time = now_start_time + duration

#code for video recording
while True:
    image = pyautogui.screenshot()
    frame_1 =np.array(image)
    frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)

    output.write(frame)
    
    c_time = time.time()

    if c_time > end_time:
        break

output.release()

print("---END---")



