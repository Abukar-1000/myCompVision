import cv2 
import numpy as np
from threading import Thread


basePath = "Computer-Vision-py/DATA/"

flat_chessboard = cv2.imread(basePath + "flat_chessboard.png")
copy = flat_chessboard.copy()

# finds chess like grid on the given frame
def findChessBoard(frame: cv2.Mat) -> cv2.Mat:
    gridDimensions = (4,4)
    found, corners = cv2.findChessboardCorners(
        image= frame,
        patternSize = gridDimensions
    )

    frame2 = frame.copy()
    cv2.drawChessboardCorners(
        frame2,
        gridDimensions,
        corners,
        found
    )

    return (found, frame2)
        # cv2.destroyWindow("corners")
        # cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 0x1B ) else None

# finds circle like image on a given frame, has multiple options for searching for circle
def findCircleGrid(frame: cv2.Mat) -> cv2.Mat:
    gridDimensions = (4,4)
    found, corners = cv2.findCirclesGrid(
        image= frame,
        patternSize = gridDimensions,
        flags= cv2.CALIB_CB_SYMMETRIC_GRID
    )

    frame2 = frame.copy()
    cv2.drawChessboardCorners(
        frame2,
        gridDimensions,
        corners,
        found
    )

    return (found, frame2)


def computeAndShow(imgSrc: cv2.Mat) -> None:
    gridDimensions = (7,7)
    found, corners = cv2.findChessboardCorners(
        image= imgSrc,
        patternSize = gridDimensions
    )

    if found:
        cv2.drawChessboardCorners(
            imgSrc,
            gridDimensions,
            corners,
            found
        )
        cv2.imshow("corners", imgSrc)

        # cv2.destroyWindow("corners")
        cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 0x1B ) else None

def func2(normal):
    cv2.imshow("normal", normal) 
    cv2.waitKey(0)

# thread1 = Thread(target = func2, args=(flat_chessboard,))
# thread2 = Thread(target = computeAndShow, args=(copy,))

# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# cv2.imshow("img", flat_chessboard)

cam = cv2.VideoCapture(0)
while 1:
    ret, frame = cam.read()
    found, frame2 = findChessBoard(frame)

    if (found):
        cv2.imshow("detected", frame2)
    cv2.imshow("corners", frame)

    if cv2.waitKey(1) & 0xFF == 0x1B:
        cv2.destroyAllWindows()
        break

# cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 0x1B ) else None