import cv2 
import numpy as np
basePath = "Computer-Vision-py/DATA/"

img = cv2.imread(basePath +  "sudoku.jpg", flags=0)
cv2.imshow("puzzle", img)

# depth is the precision of the pixel
sobelX = cv2.Sobel(img, cv2.CV_64F, 1,0, ksize=5)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0,1, ksize=5)

# lapausian derivitives => look into it | i like the output
lapausian = cv2.Laplacian(img, cv2.CV_64F)

# combining results
combined = cv2.addWeighted(
    sobelX,
    0.4,
    sobelY,
    0.6,
    0
)

cv2.imshow("sobelX", sobelX)
cv2.imshow("sobelY", sobelY)
cv2.imshow("lapausian", lapausian)
cv2.imshow("combined", combined)
cv2.destroyAllWindows() if cv2.waitKey(0) & 0xFF == 27 else None