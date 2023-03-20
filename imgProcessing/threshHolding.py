import cv2 
import numpy as np

basePath = "Computer-Vision-py/DATA/"

# the 0 flag will read in as a grawscale 
img = cv2.imread(basePath + "rainbow.jpg",flags=0)
cv2.imshow("img", img)

# any value below the threshold gets turned to 0 || above values get turned to 1 ( white ) || usually just choose the halfway value
ret, thresh1 = cv2.threshold(img, 255 // 2, 255, cv2.THRESH_BINARY)
retInv, threshInv1 = cv2.threshold(img, 255 // 2, 255, cv2.THRESH_BINARY_INV)

# the truncate threshold reduces the values to the max value if its greater than it, otherwise it keeps its value, in this case the threshold is 127
ret, threshTrunc = cv2.threshold(img, 255 // 2, 255, cv2.THRESH_TRUNC)

# keeps its value if it is greater than or equal to the threshold, otherwise 0
ret, threshToZero = cv2.threshold(img, 255 // 2, 255, cv2.THRESH_TOZERO)

# cv2.imshow("threshhold", thresh1)
# cv2.imshow("threshhold_Inverse", threshInv1)
# cv2.imshow("threshhold_To_Zero", threshToZero)

# using thresholding on real world data
img = cv2.imread(basePath + "crossword.jpg", flags=0)
cv2.imshow("img", img)

# grab ink section using binary threshold => terrable in general, there are a lot of compromises that have to be made
ret, thresh1 = cv2.threshold(img, 167, 255, cv2.THRESH_BINARY)

# adaptive threshhold | block size is the size of the pixel neighborhood to create a threshold for a particular pixel ( MUST BE ODD ) , c is the const that will be used when subtracting the mean
adaptiveThreshHold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize= 13, C= 8)

cv2.imshow("threshhold", thresh1)
cv2.imshow("Adaptive_threshhold", adaptiveThreshHold)
cv2.waitKey(0)