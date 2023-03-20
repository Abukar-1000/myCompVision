import cv2 
import numpy as np
# from PIL import Image, ImageShow

# global variables 
drawing = False
initialX, initialY = (0,0)
# function 

def myCallBack(event, x,y, flags, param):
    global initialX, initialY, drawing

    if (event == cv2.EVENT_LBUTTONDOWN):
        cv2.line(imgArr, (x,y), (x + 100,y), (80,0,80), thickness=4)
    
    # 3 events below are for making a resizeable rectangle 
    elif (event == cv2.EVENT_RBUTTONDOWN):
        initialX = x
        initialY = y
        drawing = True
    elif (event == cv2.EVENT_MOUSEMOVE):
        if (drawing):
            cv2.rectangle(
                imgArr,
                (initialX,initialY),
                (x,y),
                (0,255,0),
                thickness=-1,
            )
    elif (event == cv2.EVENT_RBUTTONUP):
        drawing = False

    # for resizable circle 
    
# connect the callback function to the window
cv2.namedWindow(winname='imgWindow')
cv2.setMouseCallback('imgWindow', myCallBack)
# showing image with openCv 

imgArr = np.zeros(
    (1000,1000,3),
    np.int8
)

# connect a func to an image using the function name 
while (True):
    cv2.imshow('imgWindow', imgArr)


    if (cv2.waitKey(20) & 0xFF == 27):
        break

cv2.destroyAllWindows()