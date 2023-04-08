import cv2 
import numpy as np
from PIL import ImageGrab
import win32gui
import win32ui
import win32con
import pygetwindow

shape = (1440, 2560, 3)
activeWindowName = pygetwindow.getActiveWindow().title
handle = win32gui.FindWindow(None, activeWindowName)
window = win32gui.GetWindowDC(handle)
dcObj=win32ui.CreateDCFromHandle(window)
cDC=dcObj.CreateCompatibleDC()
dataBitMap = win32ui.CreateBitmap()
dataBitMap.CreateCompatibleBitmap(dcObj, shape[1], shape[0])
cDC.SelectObject(dataBitMap)

cDC.BitBlt((0,0),(shape[1], shape[0]) , dcObj, (0,0), win32con.SRCCOPY)
dataBitMap.SaveBitmapFile(cDC, "sc.bmp")

# Free Resources
dcObj.DeleteDC()
cDC.DeleteDC()
win32gui.ReleaseDC(handle, window)
win32gui.DeleteObject(dataBitMap.GetHandle())

frame = cv2.imread("sc.bmp")
cv2.imshow("Screen", frame)
cv2.destroyAllWindows() if ( cv2.waitKey(0) & 0xFF == 27 ) else None
print("")