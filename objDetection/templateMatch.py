import cv2 
import numpy as np
from time import sleep
basePath = "Computer-Vision-py/DATA/"

fullImg = cv2.imread(basePath + "sammy.jpg")
faceImg = cv2.imread(basePath + "sammy_face.jpg")
purpHue = (255,0,255)
redHue = (55,0,255)

# for each of the methods eval will convert it to a function pointer 
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

topRight = None
bottomLeft = None

# squared difference methods MUST USE the min location
for method in methods:
    # copy over the full image since we will alter it
    fullCopy = fullImg.copy()
    func = eval(method)

    # arg layout: fullImg, subImg, func for comparison
    result = cv2.matchTemplate(fullCopy, faceImg, func)

    # this func return the min max values & their locations from the match result 
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    
    # assign topR and bottomL values for the rectangle 
    print(minLoc,maxLoc)

    # topR
    if func in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        topRight = minLoc
    else:
        topRight = maxLoc

    # bottomL essentially add the width and height to the max location of the match
    width, height, _ = faceImg.shape
    bottomLeft = (topRight[0] + width, topRight[1] + height)
    cv2.rectangle(
        fullCopy,
        topRight,
        bottomLeft,
        redHue,
        3   
    )

    cv2.imshow(method,fullCopy)

cv2.imshow("fullImg", fullImg)
cv2.imshow("faceImg", faceImg)
cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 27 ) else None