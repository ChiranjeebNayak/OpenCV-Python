import cv2 as cv
import numpy as np

img1 = np.zeros([250, 500, 3], np.uint8)
img1=cv.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=cv.imread('image_1.png',1)
#bitand=cv.bitwise_and(img1,img2)
#bitor=cv.bitwise_or(img1,img2)
bitnot=cv.bitwise_not(img1)
cv.imshow('image1',img1)
cv.imshow('image2',img2)
#cv.imshow('bitand',bitand)
#cv.imshow('bitor',bitor)
cv.imshow('bitnot',bitnot)

cv.waitKey(0)
cv.destroyAllWindows()