import cv2 
import numpy as np

basePath = "Computer-Vision-py/DATA/"
img = cv2.imread(basePath + "pennies.jpg")

imgBlured = cv2.medianBlur(img, 45)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)


# apply otsu's method, works really well with thresholded images
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
thresh = thresh[1000:2500,:]

# you can optionally just remove the noise instead 
kernel = np.ones((3,3), np.uint8)
openning = cv2.morphologyEx(
    thresh,
    cv2.MORPH_OPEN,
    kernel,
    iterations= 2
)


# use distance transform to modify the center values of each matrix to make it brighter than the surrounding ones
# doing this allows you to use the brightest points ( center  ) as seeds in the watershed algorithm
background = cv2.dilate(openning, kernel, iterations= 3)
distanceTransform = cv2.distanceTransform(
    openning,
    cv2.DIST_L2,
    5
)

ret, forground = cv2.threshold(
    distanceTransform,
    0.7 * distanceTransform.max(),
    255,
    0
)
cv2.imshow("img", distanceTransform)


if cv2.waitKey(0) & 0xFF == 0x1B:
    cv2.destroyAllWindows()