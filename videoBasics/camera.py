import cv2 
import numpy as np
basePath = "Computer-Vision-py/DATA/"

# camera | 0 => grabs default camera 
cap = cv2.VideoCapture(0)

# returns a floating point
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frameCount = 0x0000001E

# frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# count2 = cap.get(cv2.CAP_PROP_XI_FRAMERATE)

print(f"{frameCount} fps")
"""
writter obj to save frames
VideoWriter_fourcc determines the codec based on user os, mappings:

    windows => *'DIVX'
    MacOs or Linux => *'XVID'

"""
writer = cv2.VideoWriter("videoBasics/vids/mycapture.mp4", cv2.VideoWriter_fourcc(*"DIVX"), frameCount, (width,height))
# display
while (True):
    # capture returns a series of images || all previous methods work, but just need to be done on individual frames 
    ret, frame = cap.read()

    # write to file writter
    writer.write(frame)
    cv2.imshow("Frame", frame)

    if ( cv2.waitKey(1) & 0xFF == 27 ):
        break

# release the capture & writter
cap.release()
writer.release()
cv2.destroyAllWindows()
