import cv2 
import numpy as np
from time import sleep
basePath = "Computer-Vision-py/DATA/"
purpHue = (255,0,255)
redHue = (55,0,255)

"""
What is a corner?
    A corner is the junction of two edges, where an edge is the sudden change in an images' brightness
"""
faltChessboard = cv2.imread(basePath + "flat_chessboard.png")
realChessboard = cv2.imread(basePath + "real_chessboard.jpg")
flatGrayChessboard = cv2.cvtColor(faltChessboard, cv2.COLOR_RGB2GRAY)
grayRealChessboard = cv2.cvtColor(realChessboard, cv2.COLOR_RGB2GRAY)

cv2.imshow("flatGrayChessboard1", flatGrayChessboard)

# corner harris detection algo | MUST CONVERT THE DATA TYPE OF PIXEL VALUES TO FLOAT
flatGrayChessboardFloat = np.float32(flatGrayChessboard)

cornerRes = cv2.cornerHarris(
    src=flatGrayChessboardFloat,
    blockSize=2,
    ksize=3,
    k=0.04 # has an equation to find ( provided ) 
)
# mark all corners red | must dialate first
cornerRes = cv2.dilate(cornerRes, None)

# wherever the of image had a pixel value that was greater than 0.01 of th corrisponding pixel in the result from the harris algo => mark it red 
faltChessboard[cornerRes > 0.01*cornerRes.max()] = [255,0,255]

# on real chessboard image | MUST BE GRAYSCALE & MUST BE FLOAT TYPE
realChessboardFloat = np.float32(grayRealChessboard)
realChessboardRes = cv2.cornerHarris(
    src=realChessboardFloat,
    blockSize= 2,
    ksize= 3,
    k= 0.04
)

realChessboardRes = cv2.dilate(realChessboardRes, None)
realChessboard[realChessboardRes > 0.01*realChessboardRes.max()] = [255,0,255]


# cv2.imshow("flatChess", faltChessboard)
# cv2.imshow("realChessboard", realChessboard)
# cv2.imshow("flatGrayChessboard", flatGrayChessboard)
# cv2.imshow("flatGrayChessboard", flatGrayChessboard)

# ________________________________________________________________________________________________________________________________________________________________________________
# shi detection algorithm called "good features to track" in cv


faltChessboard = cv2.imread(basePath + "flat_chessboard.png")
realChessboard = cv2.imread(basePath + "real_chessboard.jpg")
flatGrayChessboard = cv2.cvtColor(faltChessboard, cv2.COLOR_RGB2GRAY)
grayRealChessboard = cv2.cvtColor(realChessboard, cv2.COLOR_RGB2GRAY)


# algo starts here | if you dont want to limit the max corners detected => pass in a negative number
corners = cv2.goodFeaturesToTrack(
    image= flatGrayChessboard,
    maxCorners= 5,
    qualityLevel = 0.01,
    minDistance= 10
)

# must convert to int here ! need to find out y
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    print(i.ravel())

    cv2.circle(
        faltChessboard,
        (x,y),
        2,
        redHue,
        2
    )


# on real image
corners = cv2.goodFeaturesToTrack(
    image= grayRealChessboard,
    maxCorners= 100,
    qualityLevel = 0.01,
    minDistance= 10
)

# must convert to int here ! need to find out y
print(corners)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    # print(i.ravel())

    cv2.circle(
        realChessboard,
        (x,y),
        2,
        redHue,
        2
    )
cv2.imshow("flatChess", faltChessboard)
cv2.imshow("realChessboard", realChessboard)
cv2.imshow("flatGrayChessboard", flatGrayChessboard)
# cv2.imshow("flatGrayChessboard", flatGrayChessboard)

cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 27 ) else None