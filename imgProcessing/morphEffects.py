import cv2 
import numpy as np
basePath = "Computer-Vision-py/DATA/"

def loadImg():
    blank = np.zeros((600,600))
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(
        blank,
        " Hi There ",
        (50,300),
        font,
        3,
        (255,255,255),
        10
    )

    return blank

def myShow(imgArr) -> None:
    cv2.imwrite("blank.png", imgArr)
    img = cv2.imread("blank.png")
    cv2.imshow("blank", img)


imgArr = loadImg()
myShow(imgArr)

# errosion | errods the border of the text to combine forground and background
kernel = np.ones((5,5), np.uint8)
# itterations reapplies the kernel to the image array | if you want more errosion, do more itterations
erroded = cv2.erode(imgArr, kernel=kernel, iterations=2)
myShow(erroded)

# opening which is errosion & dilation | helpfull in removing noise FROM BACKGROUND|  
# create white noise | just an array of either 0 or 255
whiteNoise = np.random.randint(0,2,(600,600))
whiteNoise *= 255

# apply noise to image
noiseImg = imgArr + whiteNoise
myShow(noiseImg)

# apply opening 
opening = cv2.morphologyEx(noiseImg,cv2.MORPH_OPEN,kernel)
myShow(opening)

# closing morphilogical | great for removing noise in the foreground of the image
# black noise
blackNoise = np.random.randint(0,2,(600,600))
blackNoise *= -255
blackNoise = imgArr + blackNoise
# if the pixel is less than 0, make it zero
blackNoise[blackNoise < 0] = 0
# apply closing 
closing = cv2.morphologyEx(blackNoise,cv2.MORPH_CLOSE,kernel)
myShow(closing) 

# gradient | useful for edge detection, will grab the edge of the text ( text border )| takes the difference between closing and openning 
gradient = cv2.morphologyEx(imgArr, cv2.MORPH_GRADIENT, kernel)
myShow(gradient) 

cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 27 ) else None