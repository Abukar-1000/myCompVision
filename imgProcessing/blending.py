import cv2 
import numpy as np

def formatPath(inputStr: str) -> str:
    startIndex = inputStr.index('Computer-Vision-py')
    inputStr = inputStr[startIndex:]
    result = ''
    for char in inputStr:
        if char == '\\':
            result += '/'
        else:
            result += char

    return result

basePath = "Computer-Vision-py/DATA/"
img1 = cv2.imread(basePath + 'dog_backpack.png')
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread(basePath + 'watermark_no_copy.png')
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# blending images of the same size

# resize images
img1 = cv2.resize(img1, (1200, 1200))
img2 = cv2.resize(img2, (1200, 1200))

blended = cv2.addWeighted(
    src1= img1,
    alpha= 0.92,
    src2= img2,
    beta= 0.08,
    gamma = 0
)

# overlaying a small image on top of a large image
img1 = cv2.imread(basePath + 'dog_backpack.png')
img2 = cv2.imread(basePath + 'watermark_no_copy.png')

img2NewDimensions = (600,600)
img2 = cv2.resize(img2, img2NewDimensions)

img1Arr = np.asarray(img1, dtype=np.int32)
img2Arr = np.asarray(img2, dtype=np.int32)

img1MaxX, img1MaxY, _ = img1.shape

# reduce the transparancy by 1/4
# img2Arr[:,:,3] = 255 // 4
print(img2Arr.shape)
img1Arr[
    img1MaxX - img2NewDimensions[0]: img1MaxX,
    img1MaxY - img2NewDimensions[1]: img1MaxY
] = img2Arr

# cv2.imshow("im1", img1)
# cv2.imshow("im2", img2)
# cv2.imshow("blended_Img", blended)
cv2.imwrite('combined.png',img1Arr)
imgCombined = cv2.imread('combined.png')
cv2.imshow("combined", imgCombined)


# blending images of different sizes using the resized image

cordinatesOfIntrest = (
    (img1MaxX - img2NewDimensions[0], img1MaxX),
    (img1MaxY - img2NewDimensions[1], img1MaxY),
)



img1 = cv2.imread(basePath + 'dog_backpack.png')
# cv2.imshow("normImg1", img1)
img1Arr = np.asarray(img1, dtype=np.int32)

regionOfIntrestOnArr = img1Arr[
    cordinatesOfIntrest[0][0]:cordinatesOfIntrest[0][1],
    cordinatesOfIntrest[1][0]:cordinatesOfIntrest[1][1]
]
# quick look at the region of interest on the array
cv2.imwrite('region.png',regionOfIntrestOnArr)
regionOfIntrest = cv2.imread('region.png')
cv2.imshow("region_of_intrest", regionOfIntrest)

# create a mask on the region of intrest 
img2Gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
# the mask will be the inverse of the grayscale image bc regions that are white in the grayscale we want hidden so black in the normal image afterwards
# bitwise not will inverse the image | all whites become black and all blacks become white
imgMask = cv2.bitwise_not(img2Gray)

# now we must make the mask have 3 color channels sice its shape is ( width, height ) currently 
whiteBg = np.full(
    (600,600,3),
    255,
    dtype= np.uint8
)

bg = cv2.bitwise_or(whiteBg,whiteBg,mask=imgMask)
# cv2.imshow("mask", completeMask)

# grab do not copy region from img 2 
img2Region = cv2.bitwise_or(img2Arr,img2Arr,mask=imgMask)

# anything in white shines through on the mask and all black is hidden
blendedArr = cv2.bitwise_or(
    regionOfIntrestOnArr,
    img2Region
)

# overwriting noraml arr to insert masked region and saving as an image
completeBlendedArr = img1Arr.copy()
completeBlendedArr[
    cordinatesOfIntrest[0][0]:cordinatesOfIntrest[0][1],
    cordinatesOfIntrest[1][0]:cordinatesOfIntrest[1][1]
] = blendedArr

print("blended shape", blended.shape)
cv2.imwrite("blended.png", completeBlendedArr)
blended = cv2.imread("blended.png")
cv2.imshow("blended", blended)
cv2.waitKey(0)