import cv2 
import numpy as np
from PIL import ImageGrab
import pyautogui as pg
basePath = "Computer-Vision-py/DATA/"
purpHue = (255,0,255)
redHue = (55,0,255)


cam = cv2.VideoCapture(0)

# detect with harris | pass in grayscale version into image
def makeHarrisFrame(frame: np.ndarray, grayFrame: np.ndarray) -> np.ndarray:
    grayFrame = np.float32(grayFrame)
    cornerRes = cv2.cornerHarris(
        src=grayFrame,
        blockSize=3,
        ksize=3,
        k=0.04 # has an equation to find ( provided ) 
    )

    # mark real frame
    frame[cornerRes > 0.01*cornerRes.max()] = [255,0,255]

def myGoodFeaturesToTrack(frame: np.ndarray, grayFrame: np.ndarray):
    corners = cv2.goodFeaturesToTrack( # returns None for some odd reason
        image= grayFrame,
        maxCorners= 50,
        qualityLevel = 0.25,
        minDistance= 2
    )

    # must convert to int here ! need to find out y
    # if (corners == None):
    #      return frame
    
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()

        cv2.circle(
            frame,
            (x,y),
            2,
            redHue,
            2
        )

# uses webcam 
# while (1):
#     ret, frame = cam.read()

#     cv2.imshow("noFilterCamera",frame)
#     makeHarrisFrame(
#         frame,
#         cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#     )


#     # myGoodFeaturesToTrack(
#     #     frame,
#     #     cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#     # )
            
#     cv2.imshow("Camera",frame)
#     if ( cv2.waitKey(1) & 0xFF == 0x0000001B ):
#         break

# img = pg.screenshot()
# frame = np.asarray(img, np.uint8)
# print(frame.shape)
# shape = (img.height,img.width,3)
# frame = np.asarray(img.getdata(), dtype=np.uint8).reshape(shape)
# cv2.imshow("Screen", frame)
# cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 27 ) else None
# captures screen 

def grabScreenFrame() -> np.ndarray:
    img = pg.screenshot()
    return np.asarray(img, dtype=np.uint8)
    
capture = cv2.VideoCapture(0)
while (1):

    # grabs screenshot
    # frame = grabScreenFrame()

    # grab video
    ret, frame = capture.read()
    frame2 = frame.copy()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # cv2.imshow("noFilterCamera",frame)
    # makeHarrisFrame(
    #     frame,
    #     cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # )

    myGoodFeaturesToTrack(
        frame,
        cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    )

            
    cv2.imshow("Camera",frame)
    cv2.imshow("Camera2",frame2)
    if ( cv2.waitKey(1) & 0xFF == 0x0000001B ):
        break
cv2.destroyAllWindows()