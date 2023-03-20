import cv2 
import numpy as np
import time
basePath = "Computer-Vision-py/DATA/"

"""
Using an existing video file
"""

# create a cap obj but just provide the file path instead of a 0.... for the capture device 
cap = cv2.VideoCapture(basePath + "hand_move.mp4")
frameRate = 0x00000014

# print(f"{frameRate} fps\n{cv2.CAP_PROP_FRAME_COUNT // 20}")

# check if you where able to open the file 
if ( not cap.isOpened() ):
    print("Unable to open video file")

while ( cap.isOpened() ):
    ret, frame = cap.read()

    # 20 fps || dont delay unless you want to view the frames
    time.sleep(1/frameRate)
    if ( ret ):
        cv2.imshow("frame", frame)

        if ( cv2.waitKey(1) & 0xFF == 27 ):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()