import numpy as np
import cv2 as cv


def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        
        cv.circle(img, (x, y), 3, (0, 0, 255), -1)
        colorimg = np.zeros([512, 512, 3], np.uint8)
        
        colorimg[:] = [blue,  green, red]
        cv.imshow('color', colorimg)


img = cv.imread('lena.jpg', 1)
cv.imshow('image', img)
cv.setMouseCallback('image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()
