import cv2 
import numpy as np
from PIL import ImageGrab
import win32gui
import win32ui
import win32con
import pygetwindow 
import pyautogui as pg
class gameWindow(object):

    def __init__(self, name, width = None, height = None) -> None:

        self.__windowInstance = None
        try:
            self.name = name
            self.__windowInstance = pygetwindow.getWindowsWithTitle(self.name)[0]
        except IndexError:
            raise ValueError(self.name + " Is not open ☠")
        
        validDimension = self.__isValid(width, height)
        
        if (not validDimension):
            self.__width, self.__height = self.__windowInstance.size
        else:
            self.__width = width
            self.__height = height
            print(self.__width, self.__height)
            self.__windowInstance.resizeTo(self.__width, self.__height)

    def __str__(self) -> str:
        f"{self.name} window ( {self.__width}, {self.__height} )"

    def __isValid(self, width: int, height: int) -> bool:

        if (not width or not height):
            return False
        elif (width <= 0):
            return False
        elif (height <= 0):
            return False
        
        return True

    def resize(self, width: int, height: int) -> bool:
        validDimension = self.__isValid(width, height)
        
        if (not validDimension):
            return False
        try:
            self.__windowInstance.resizeTo(width, height)
            return True
        except pygetwindow.PyGetWindowException:
            return False
    
    def getAllWindowDimensionData(self) -> dict:
        metaData = {
            "topL": (self.__windowInstance.topleft.x, self.__windowInstance.topleft.y),
            "topR": (self.__windowInstance.topright.x, self.__windowInstance.topright.y),
            "bottomL": (self.__windowInstance.bottomleft.x, self.__windowInstance.bottomleft.y),
            "bottomR": (self.__windowInstance.bottomright.x, self.__windowInstance.bottomright.y),
            "shape": (self.__windowInstance.size[0], self.__windowInstance.size[1])
        }

        return metaData


    def getDimension(self) -> tuple:
        return self.__windowInstance.size

class Tracker(object):

    def __init__(self) -> None:
        self.__mat = None
        self.__meanPoint = None

    @staticmethod
    def siftMaxtrix(matrix1: cv2.Mat = None, matrix2: cv2.Mat = None) -> None:
        # matrix3 = matrix2.copy()

        # make images grayscale
        # matrix1 = cv2.cvtColor(
        #     matrix1,
        #     cv2.COLOR_RGB2GRAY
        # )
        # matrix1 = cv2.cvtColor(
        #     matrix2,
        #     cv2.COLOR_RGB2GRAY
        # )

        # find matrix1 on matrix 2
        SIFT = cv2.SIFT_create()
        keyPoints1, descriptor1 = SIFT.detectAndCompute(matrix1, None)
        keyPoints2, descriptor2 = SIFT.detectAndCompute(matrix2, None)
        bruteForce = cv2.BFMatcher()
        matches = bruteForce.knnMatch(descriptor1, descriptor2, k = 2)
        goodMatches = []

        meanX, meanY = 0,0
        THRESHHOLD = 0.45
        count = 0

        for match1, match2 in matches:

            if match1.distance < THRESHHOLD * match2.distance:
                count += 1
                meanX += keyPoints2[match1.trainIdx].pt[0]
                meanY += keyPoints2[match1.trainIdx].pt[1]

        if (count):
            meanX, meanY = int(meanX / count), int(meanY / count)
            cv2.circle(
                matrix2,
                (meanX, meanY),
                50,
                (255,0,255),
                2
            )

            # reassign pointer
            # matrix2 = matrix3

        print(count, (meanX, meanY))
    @staticmethod
    def grabScreenFrame(region: tuple = None) -> np.ndarray:
        img = pg.screenshot(region = region)
        frame = np.asarray(img, dtype=np.uint8)
        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )
        return frame


def getAllWindows():
    windows = pygetwindow.getAllWindows()

    for window in windows:
        print(window.title)
