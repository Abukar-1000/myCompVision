import cv2 
import numpy as np
import time
basePath = "Computer-Vision-py/DATA/"

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frameRate = cap.get(cv2.CAP_PROP_FRAME_COUNT) if ( cap.get(cv2.CAP_PROP_FRAME_COUNT) > 0 ) else 0x0000001E
x = int(width // 2)
y = int(height // 2)


xPos,yPos, frame = None, None, None
purpHue = (255,0,255)
redHue = (55,0,255)
radius = 200

pressedDown, released = False, False

def myCallBack(event, x,y, flags, param):
    """
    first grab the upper left point | left down click
    then create the rectangle with a right down click
    """
    global xPos,yPos, frame, pressedDown, released
    if (event == cv2.EVENT_LBUTTONDOWN):
        pressedDown = True
        released = False
        xPos, yPos = x,y
    elif (event == cv2.EVENT_LBUTTONUP):
        pressedDown = False
        released = True
def drawCrosshare(frame: np.ndarray) -> np.ndarray:
    x,y = xPos, yPos
    cv2.circle(
        frame,
        (x,y),
        radius,
        purpHue,
        2
    )
    # vertical
    cv2.line(
        frame,
        (x, y - radius),
        (x, y + radius),
        redHue,
        2
    )
    # horizontal
    cv2.line(
        frame,
        (x - radius, y),
        (x + radius, y),
        redHue,
        2
    )
    return frame

# connecting callback func
cv2.namedWindow(winname='camera')
cv2.setMouseCallback('camera', myCallBack)
while (1):
    ret, frame = cap.read()
    # frame = drawCrosshare(frame)
    # print(f"({width},{height}) @{0x0000001E}fps {0xFF}")

    if ( pressedDown and not released):
        frame = drawCrosshare(frame)
    
    cv2.imshow("camera", frame)
    if ( cv2.waitKey(1) & 0xFF == 27 ):
        break


cap.release()
cv2.destroyAllWindows()

