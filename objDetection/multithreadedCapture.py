import cv2 
import numpy as np
from threading import Thread
import multiprocessing
import time

def myGoodFeaturesToTrack(frame: np.ndarray, grayFrame: np.ndarray):
    corners = cv2.goodFeaturesToTrack( # returns None for some odd reason
        image= grayFrame,
        maxCorners= 50,
        qualityLevel = 0.01,
        minDistance= 2
    )


def normalCapture():
    capture = cv2.VideoCapture(0)
    while (1):

        # grabs screenshot
        # frame = grabScreenFrame()

        # grab video
        ret, frame = capture.read()
        frame2 = frame.copy()

        myGoodFeaturesToTrack(
            frame2,
            cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        )
        cv2.imshow("edge",frame2)
        cv2.imshow("normal",frame)
        if ( cv2.waitKey(1) & 0xFF == 0x1B ):
            break
    cv2.destroyWindow("normal") 

def edgeDetection():
    capture = cv2.VideoCapture(0)
    while (1):

        # grabs screenshot
        # frame = grabScreenFrame()

        # grab video
        ret, frame = capture.read()
        myGoodFeaturesToTrack(
            frame,
            cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        )
        cv2.imshow("edge",frame)
        if ( cv2.waitKey(2) & 0xFF == 119 ):
            break
    cv2.destroyWindow("edge") 

# thread1 = Thread(target= normalCapture)
# thread2 = Thread(target= edgeDetection)

# thread1.start()
# thread1.join()

# time.sleep(0.05)
# thread2.start()
# thread2.join()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    process1 = multiprocessing.Process(target= normalCapture)
    process2 = multiprocessing.Process(target= edgeDetection)

    process1.start()
    process2.start()

    process1.join()
    process2.join()


# cv2.destroyAllWindows() if ( cv2.waitKey(1) & 0xFF == 0x1B ) else None