import numpy as np
import cv2 as cv

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        
        cv.imshow('image', img)
        points.append((x, y))
        print(len(points))
    if len(points) >= 2:
        cv.line(img, points[-1], points[-2], (233, 0, 0), 5)
        cv.imshow('image', img)

img = np.zeros([512, 512, 3], np.uint8)
cv.imshow('image', img)
points = []
cv.setMouseCallback('image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()