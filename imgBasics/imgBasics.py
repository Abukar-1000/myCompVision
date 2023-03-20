import numpy as np
import matplotlib.pyplot as mt
from PIL import Image, ImageShow
import time


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def randomDistort(image: Image) -> Image:
    arr = np.asarray(image)
    xDimension, yDimension, channels = arr.shape
    for itteration in range(np.random.randint(0,100)):
        randomCap = np.random.randint(0,20)
        randomXRange = (
            np.random.randint(0,100) % xDimension, 
            np.random.randint(0,100) % xDimension
        )
        randomYRange = (
            np.random.randint(0,100) % yDimension, 
            np.random.randint(0,100) % yDimension
        )

        channel = np.random.randint(0,channels)
        arr[randomXRange[0]:randomXRange[1],randomYRange[0]:randomYRange[1],channel] = np.random.randint(0,1000)

    result = Image.fromarray(arr)
    return result


"""
Additive color mixing allows us to produce a decent range of colors
the shape of the images are in (width , height, color channels)
    ex: (1280, 720, 3)

The computer itself does not know that an image is red, it just knows that there are 3 intensity channels
each channel is represented with a grayscale illustrating its relative intensity in an array
Then all the channels are added up to produce the final image

Numpy by itself can not open immage, you must also combine it with pillow (python immaging lib)
"""
pic = Image.open("Computer-Vision-py/DATA/00-puppy.jpg")
picArr = np.asarray(pic)
ImageShow.show(pic)
print(picArr)

# grab the red channel
# layout of np arr is row, col, channel | channels are in this order R G B
#                    [:,:,:]                                         0 1 2
redImg = picArr.copy()
redImg[:,:,1] = 0
redImg[:,:,2] = 0

# reImageProcessed = Image.fromarray(redImg)
# ImageShow.show(reImageProcessed) => marker

ranImg = randomDistort(pic)
ImageShow.show(ranImg) 
time.sleep(1)