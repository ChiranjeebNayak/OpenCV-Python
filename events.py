import numpy as np
import cv2 as cv

#events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)


def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        text = 'x: '+str(x)+',y: '+str(y)
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, text, (x, y), font, 1, (255, 0, 0), 2)
        cv.imshow('image', img)
    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        text = str(blue)+','+str(green)+','+str(red)
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, text, (x, y), font, 1, (255, 230, 10), 2)
        cv.imshow('image', img)


img = cv.imread('lena.jpg', 1)
#img = np.zeros([512, 512, 3], np.uint8)
cv.imshow('image', img)
cv.setMouseCallback('image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()
