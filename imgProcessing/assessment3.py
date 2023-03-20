import cv2 
import numpy as np
basePath = "Computer-Vision-py/DATA/"

giraffes = cv2.imread(basePath + "giraffes.jpg")
grayGiraffes = cv2.imread(basePath + "giraffes.jpg", 0)
# giaraffes = cv2.cvtColor(giaraffes, c)
cv2.imshow("giraffes", giraffes)

# 2
t1, binaryThesh = cv2.threshold(
    grayGiraffes,
    giraffes.max() // 2,
    255,
    cv2.THRESH_BINARY
)
cv2.imshow("binaryThresh", binaryThesh)

# 3
hsvGiraffes = cv2.cvtColor(giraffes, cv2.COLOR_RGB2HSV)
cv2.imshow("hsvGiraffe", hsvGiraffes)

# 4
kernel = np.ones((4,4), np.float32) / 10
blurredGiraffe = cv2.filter2D(
    giraffes,
    -1,
    kernel
)
cv2.imshow("blurredGiraffe", blurredGiraffe)

# 5 
sobelX = cv2.Sobel(
    grayGiraffes,
    cv2.CV_64F,
    1,
    0,
    None,
    5
)
cv2.imshow("sobelX", sobelX)
cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 27 ) else None
