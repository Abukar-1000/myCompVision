import postDetectionTools as pt
import pygetwindow
import cv2
from time import sleep
def main() -> None:

    fifa_window = "FIFA 23"
    pt.getAllWindows()
    fifaWindow = pt.gameWindow(fifa_window)
    # window = pygetwindow.getWindowsWithTitle(fifa_window)
    ESCKEY = 0x1B
    BITMASK = 0xFFFFFFFF

    windowData = fifaWindow.getAllWindowDimensionData()
    frameRegion = (
        windowData['topL'][0],
        windowData['topL'][1],
        windowData['shape'][0],
        windowData['shape'][1]
    )

    goalPostMatrix = cv2.imread("trackGoalPost/postImgs/1.png")

    while 1:
        frame = pt.Tracker.grabScreenFrame(frameRegion)
        
        pt.Tracker.siftMaxtrix(goalPostMatrix,frame)
        cv2.imshow("Tracker Window", frame)

        if (cv2.waitKey(1) & BITMASK == ESCKEY):
            cv2.destroyAllWindows()
            break
    

if __name__ == "__main__":
    main()