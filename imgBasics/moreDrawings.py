import cv2 
import numpy as np
from PIL import Image, ImageShow


dimensions = (1000,1000,3)

arr = np.zeros(shape=dimensions, dtype=np.uint8)

# adding text 
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(arr,text="Hi there", org=(10,1000), fontFace=font, fontScale=5, color=(80,0,80), thickness=3, lineType=cv2.LINE_AA)
img = Image.fromarray(arr)
print(arr.reshape((-1,1,2)))
ImageShow.show(img)


# creating polygons 
arr2 = np.zeros(shape=dimensions, dtype=np.int32)

center = dimensions[0] // 2

# verticies for your pollygon
offset = 100
cordinates = [
    [0, center - offset],
    [center, center - offset],
    [center + offset, 1000],
    [1000, center + offset]
]

verticies = np.array(
    cordinates,
    dtype=np.int32
)

# open cv wante the values in 3d
points = verticies.reshape((-1,1,2))
print(verticies,"\n\n\n\n")
cv2.polylines(arr2, [points], isClosed=True, color=(255,255,255), thickness=3)
img = cv2.imwrite("tst.png",arr2)
imgIn = cv2.imread("tst.png")
cv2.imshow("img", imgIn)
cv2.waitKey(0)