import cv2 

img = cv2.imread("Computer-Vision-py/DATA/00-puppy.jpg")
cv2.imshow("sU[p?]", img)
cv2.waitKey()

# proper way to display || uses q to close the windows
while (1):
    cv2.imshow("sU[p?]", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
# creating shapes on images

