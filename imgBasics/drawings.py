import cv2 
import numpy as np
from PIL import Image, ImageShow

# img = cv2.imread("Computer-Vision-py/DATA/00-puppy.jpg")
# cv2.imshow("sU[p?]", img)
# cv2.waitKey()
dimensions = (1000,1000,3)
x, y, c = dimensions
# random array
# arr = np.array([
#     np.random.randint(0,128) for x in range(x*y*c)
# ], dtype=np.uint8).reshape((x,y,c))

# black array
arr = np.zeros(shape = dimensions, dtype=np.uint8)

# draw a rectangle by passing in the cordinates of the top left and the bottom right as tuples
topLeft = (200,350)
bottomRight = (900,999)
# cv2.rectangle(img=arr, pt1=topLeft, pt2=bottomRight, color=(80,0,80), thickness=1)
# img = Image.fromarray(arr)
# ImageShow.show(img)
print(arr)
# center rectangle
centerPoint = (
    dimensions[0] // 2,
    dimensions[1] // 2
)

offset = np.random.randint(100,800)
centerTopLeft = (
    centerPoint[0] - offset,
    centerPoint[1] - offset,
)

centerBottomRight = (
    centerPoint[0] + offset,
    centerPoint[1] + offset,
)

# center rectangle 
cv2.rectangle(arr, pt1=centerTopLeft, pt2=centerBottomRight, color=(80,0,80), thickness=1)
# img = Image.fromarray(arr)
# ImageShow.show(img)

# centering a circle in the middle 
cv2.circle(arr, center=centerPoint, radius=offset//2, color=(80,80,0), thickness=1)
print(centerPoint)

# centering a circle in the middle 
cv2.circle(arr, center=centerPoint, radius=offset//4, color=(80,80,60), thickness=-1)
print(centerPoint)

# create cross hair with 2 lines 
# vertical line 
cv2.line(arr, pt1=(centerPoint[0], centerPoint[0] - offset//4), pt2=(centerPoint[0], centerPoint[0] + offset//4), color=(80,0,80), thickness=2)
# horizontal
cv2.line(arr, pt1=(centerPoint[0] - offset//4, centerPoint[0]), pt2=(centerPoint[0] + offset//4, centerPoint[0]), color=(80,0,80), thickness=2)
img = Image.fromarray(arr)
ImageShow.show(img)