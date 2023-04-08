from postDetectionTools import Tracker, GameWindow
import pygetwindow
import cv2
from time import sleep
def main() -> None:

    fifa_window = "FIFA 23"
    fifaWindow = GameWindow(fifa_window)
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
        frame = Tracker.grabScreenFrame(frameRegion)
        
        # deep track, is accurate but slow
        # Tracker.siftMaxtrix(goalPostMatrix,frame)
        
        # faster tracking 
        Tracker.flannMaxtrix(goalPostMatrix, frame)
        cv2.imshow("Tracker Window", frame)

        if (cv2.waitKey(1) & BITMASK == ESCKEY):
            cv2.destroyAllWindows()
            break
    

if __name__ == "__main__":
    main()