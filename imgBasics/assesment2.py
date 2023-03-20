import cv2 
import numpy as np

img = cv2.imread("Computer-Vision-py/DATA/dog_backpack.jpg")
imgBgr = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
cv2.imshow("imgBgr",imgBgr)
cv2.imshow("img",img)

upsideDownImg = cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow("upsideDownImg",upsideDownImg)

# red rectangle around dogs face 
cv2.rectangle(
    img,
    (175,350),
    (650,725),
    (0,0,255),
    thickness= 2
)

cv2.imshow("red_Rect",img)

# blue triangle
img = cv2.imread("Computer-Vision-py/DATA/dog_backpack.jpg")

verticies = [
    [425,300],
    [150,750],
    [825,750]
]

points = np.array(verticies, dtype=np.int32).reshape((-1,1,2))
cv2.polylines(
    img,
    [points],
    isClosed=True,
    color=(255,0,0),
    thickness= 3
)
cv2.imshow("blue_Tri",img)

red = (0,0,255)
# filled in triangle 
img = cv2.imread("Computer-Vision-py/DATA/dog_backpack.jpg")
cv2.fillPoly(
    img,
    [points],
    color=(255,0,0),
)

# draw circle 
def callBack(event, x,y, flags, params ):
    
    # if right click draw circle
    if (event == cv2.EVENT_RBUTTONDOWN):
        cv2.circle(
            img,
            (x,y),
            100,
            color=red,
            thickness=2
        )

cv2.namedWindow(winname='img_window')
cv2.setMouseCallback('img_window', callBack)
while (1):

    cv2.imshow("img_window", img)    
    # if esc key ius pressed 
    if (cv2.waitKey(20) & 0xFF == 27):
        break

cv2.destroyAllWindows()

cv2.imshow("filled_blue_Tri",img)
cv2.waitKey(0)