import cv2 
import numpy as np

# grabs both contors
def drawContourOnFrame(frame: cv2.Mat) -> cv2.Mat:

    # returns external and internal contours
    contours, heirarchy = cv2.findContours(
        image = frame,
        mode= cv2.RETR_CCOMP,
        method= cv2.CHAIN_APPROX_SIMPLE
    )

    # print(heirarchy.max())
    frame2 = np.zeros(frame.shape)
    for i in range(len(contours)):
        if heirarchy[0][i][3] == -1:
            cv2.drawContours(
                frame2,
                contours,
                i,
                (255),
                -1
            )
    return frame2

def drawContourOnFrame4ForgroundObj(frame: cv2.Mat) -> cv2.Mat:

    # returns external and internal contours
    contours, heirarchy = cv2.findContours(
        image = frame,
        mode= cv2.RETR_CCOMP,
        method= cv2.CHAIN_APPROX_SIMPLE
    )

    frame2 = np.zeros(frame.shape)
    for i in range(len(contours)):
        if heirarchy[0][i][3] != -1:
            cv2.drawContours(
                frame2,
                contours,
                i,
                (255),
                -1
            )
    return frame2


basePath = "Computer-Vision-py/DATA/"

countourImg = cv2.imread(basePath + "internal_external.png")
countourImg
# cv2.imshow("img", countourImg)
# countourImg = cv2.cvtColor(countourImg, cv2.COLOR_RGB2GRAY)
# frame2 = drawContourOnFrame(countourImg)
# cv2.imshow("img2", frame2)
# if cv2.waitKey(0) & 0xFF == 27:
#     cv2.destroyAllWindows()

# grabs eternal feturs of a given camera frame
cam = cv2.VideoCapture(0)
while 1:
    ret, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ret, grayFrame = cv2.threshold(grayFrame, 255 // 2.9, 255, cv2.THRESH_TOZERO)
    foreground = drawContourOnFrame4ForgroundObj(grayFrame)
    contour = drawContourOnFrame(
        grayFrame
    )

    # print(contour.shape, frame.shape)
    frameMask = cv2.bitwise_not(grayFrame)

    # contour = frameMask.copy()
    ret, frameMask = cv2.threshold(frameMask, 255 // 2.5, 255, cv2.THRESH_TOZERO)
    # print(contour.max() // contour.mean())
    frameMask = cv2.bitwise_or(frame, frame, mask=frameMask)
    # ret, frameMask = cv2.threshold(frameMask, 255 // 5.5, 255, cv2.THRESH_TOZERO)
    # ret, frameMask = cv2.threshold(frameMask, 255 // 10.5, 255, cv2.THRESH_TOZERO)
    cv2.imshow("Normal", frame)
    cv2.imshow("Blended", frameMask)
    cv2.imshow("Contour", contour)
    cv2.imshow("foreground", foreground)
    

    if cv2.waitKey(1) & 0xFF == 27:
        cv2.destroyAllWindows()
        break