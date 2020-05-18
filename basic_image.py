import cv2 as cv
import numpy as np

#img = np.zeros([512, 512, 3], np.uint8) #it will give a black image using numpy.
img = cv.imread('lena.jpg', 1) # it will give an image(given image inas parameter).
img = cv.line(img, (0, 0), (255, 255), (233, 0, 0), 5)
img = cv.arrowedLine(img, (0, 255), (255, 255), (0, 33, 0), 5)
img = cv.rectangle(img, (384, 0), (510, 128), (0, 0, 255),)
img = cv.circle(img, (447, 63), 63, (0, 255, 0), -1)
font = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, 'openCV', (10, 500), font, 4, (255, 255, 255), 10)

cv.imshow('image', img)
k = cv.waitKey(0)
if k == ord('q'):
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('lenacopy3.jpg', img)