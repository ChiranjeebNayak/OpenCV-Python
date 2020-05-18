import cv2 as cv
import numpy as np

img = cv.imread('messi5.jpg', 1)
img2 = cv.imread('opencv-logo.png', 1)
print(img.shape)
print(img.size)
print(img.dtype)
b, g, r = cv.split(img)
img = cv.merge((b, g, r))
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv.resize(img, (512, 512))
img2 = cv.resize(img2, (512, 512))
dst = cv.add(img, img2)
dst = cv.addWeighted(img, .2, img2, .5, 0)

cv.imshow('image', dst)
cv.waitKey(0)
cv.destroyAllWindows()
