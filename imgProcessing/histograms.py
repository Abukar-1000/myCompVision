import cv2 
import numpy as np
basePath = "Computer-Vision-py/DATA/"

# histograms are used to see the frequency of something, in our case rgb values
showHorse = cv2.imread(basePath + "horse.jpg")
darkHorse = cv2.cvtColor(showHorse, cv2.COLOR_RGB2BGR)

showRainbow = cv2.imread(basePath + "rainbow.jpg")
rainbow = cv2.cvtColor(showRainbow, cv2.COLOR_RGB2BGR)

showBricks = cv2.imread(basePath + "bricks.jpg")
bricks = cv2.cvtColor(showBricks, cv2.COLOR_RGB2BGR)

# cv2.imshow("darkHorse", darkHorse)
# cv2.imshow("showHorse", showHorse)

# blue histogram for brick image | channel is blue here because mode = BGR
brickHist = cv2.calcHist(
    [darkHorse],
    channels=[0],
    mask=None,
    histSize=[256],
    ranges=[0,256]
)

# histogram equalizations
img = rainbow
width, height, _ = img.shape
mask = np.zeros((width, height), np.uint8)
# add white into mask
mask[300:400, 100:400] =  255
maskedImg = cv2.bitwise_and(img,img,mask=mask)
showMaskedImg = cv2.bitwise_and(showRainbow,showRainbow,mask=mask)

# cv2.imshow("maskedImg", maskedImg)
# cv2.imshow("showMaskedImg", showMaskedImg)

gorilla = cv2.imread(basePath + "gorilla.jpg",0)
gorilla = cv2.cvtColor(gorilla, cv2.COLOR_RGB2BGR)
gorillaHist = cv2.calcHist(
    [gorilla],
    [0],
    None,
    [256],
    [0,256]
)
# equalizedGorrilla = None
# equalizedGorrilla = cv2.equalizeHist(
#     gorilla,
#     equalizedGorrilla
# )

equalizedGorrilla = None
# equalizedGorrilla = cv2.equalizeHist(gorilla)
colorGorilla = cv2.imread(basePath + "gorilla.jpg")
hsvGorrila = cv2.cvtColor(colorGorilla, cv2.COLOR_RGB2HSV)
# grabbing value channel in hsv and equalizing it 
hsvGorrila[:,:,2] = cv2.equalizeHist(hsvGorrila[:,:,2])
equalizedGorrilla = cv2.cvtColor(hsvGorrila, cv2.COLOR_HSV2RGB)
cv2.imwrite("equalizedGorrilla.png",equalizedGorrilla)
equalizedGorrilla = cv2.imread("equalizedGorrilla.png")
# eqalized = cv2.equalizeHist
cv2.imshow("gorilla", colorGorilla)
cv2.imshow("EQgorilla", equalizedGorrilla)

cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 27) else None
