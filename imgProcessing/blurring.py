import cv2 
import numpy as np
basePath = "Computer-Vision-py/DATA/"

def loadImg():
    img = cv2.imread(basePath + "bricks.jpg").astype(np.float32) / 255
    # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

# gamma correction => controls the brightness of the img
# smaller values of gamma brighten the image, values above 1 darkens the img
img = loadImg()
gamma = 1/4
img = np.power(img,gamma)

img = loadImg()
font = cv2.FONT_HERSHEY_COMPLEX
centerX, CenterY = img.shape[0] // 2, img.shape[1] // 2
cv2.putText(
    img,
    "Bricks",
    (centerX - 400,CenterY),
    font,
    10,
    (0,0,255),
    4
)

# create kernel matrix for effect
kernel = np.ones(
    (5,5),
    np.float32
) / 25

# -1 depth makes output depth the same as the input depth
dst = cv2.filter2D(img, ddepth=-1, kernel=kernel)

# cv2.imshow("myImg", img)
# cv2.imshow("dst", dst)

# cv2 implements their own blur kernel for ease of access
blurred = cv2.blur(img, ksize=(5,5))
# cv2.imshow("cv2_Blured", blurred )

# gaussian blurr
img = loadImg()
cv2.putText(
    img,
    "Bricks",
    (centerX - 400,CenterY),
    font,
    10,
    (0,0,255),
    4
)


gaussianBlurr = cv2.GaussianBlur(
    img,
    (5,5),
    10
)
# cv2.imshow("gaussian", gaussianBlurr )


# median blurr | interesting because it removes noise from an image and kind of sharpens it
img = loadImg()
cv2.putText(
    img,
    "Bricks",
    (centerX - 400,CenterY),
    font,
    10,
    (0,0,255),
    4
)


medianBlurr = cv2.medianBlur(
    img,
    5
)
# cv2.imshow("medianBlurr", medianBlurr )

# application of a blurr
img = cv2.imread(basePath + "sammy.jpg")
noiseImg = cv2.imread(basePath + "sammy_noise.jpg")
noiseImg = cv2.cvtColor(noiseImg, cv2.COLOR_BGR2RGB)

fixed = cv2.medianBlur(
    noiseImg,
    5
)

cv2.imshow("normal", img )
cv2.imshow("noisy", noiseImg )
cv2.imshow("Fixed", fixed )
cv2.destroyAllWindows() if cv2.waitKey(0) & 0xFF == 27 else None
