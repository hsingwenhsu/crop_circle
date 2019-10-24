import cv2
import numpy as np
import math

w, h = 500, 500
img1 = np.zeros((h, w)) # create a black image
img2 = np.ones((h, w))*255 # create a white image

r = 50 # the radius
cx1, cy1 = 250, 250 # the center of the circle on img1
cx2, cy2 = 250, 250 # the center of the circle on img2
for i in range(r):
    a = r-i
    if i==0:
        continue
    w_12 = int(math.sqrt(2*r*i-i*i))
    img2[cy2-r+i:cy2-r+i+1, cx2-w_12:cx2+w_12]=img1[cy1-r+i:cy1-r+i+1, cx1-w_12:cx1+w_12]
    img2[cy2+r-i-1:cy2+r-i, cx2-w_12:cx2+w_12]=img1[cy1+r-i-1:cy1+r-i, cx1-w_12:cx1+w_12]

cv2.imwrite('result.png', img2)
