# python lybraries
import cv2
import math
import pandas
import numpy as np
import time as t
from matplotlib import pyplot as plt

#classes, objects and functions

import contours
import filters
import geometry
import machine_vision
import init
import robotics
import odometry
import comparisons

# main program 

# reading the test images
img_read,img_angles,img_position = init.read_test()

# focusing the images in the desired position

img_focus = []
for i in range(0,len(img_read)):
    img_focus.append(filters.focus(img_read[i],img_position[i]))

# filtering this section

img_filter = []
for i in range(0,len(img_focus)):
    img_filter.append(filters.filter_img(img_focus[i]))

# extracting the contours from the image
cont = []
for i in range(0,len(img_filter)):
    contour = contours.contours(img_filter[i])
    cont.append(contour)

#filter contours
cont2 = []
for i in range(0,len(cont)):
    contour2 = contours.points_contours(cont[i])
    cont2.append(contour2)

# from this I have the parameters to find the heading

#test of weights
img_black = img_filter[8]
img_black = 255*img_black

cv2.drawContours(img_black, cont2[8], -1, (0, 255, 0), 2)

cv2.imshow('Contornos', img_black)
cv2.waitKey(0)
cv2.destroyAllWindows()

