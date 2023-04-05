# python lybraries
import cv2
import math
import pandas
import numpy as np
import time as t
from matplotlib import pyplot as plt
from sklearn.cluster import MeanShift
from scipy.spatial.distance import cdist

#classes, objects and functions

import contours
import filters
import geometry
import machine_vision
import init
import robotics
import odometry
import comparisons
import template_matching
import callibration
# main program 



##############################################
#Preparing Image avg
##############################################
img_t = []
img1 = cv2.imread('test4/background.jpg',0) # reading the test image
img1 = filters.filter_img(img1) # filtering the image
img1 = cv2.resize(img1, (1904,3065),interpolation = cv2.INTER_AREA) #resizing the image
img_t.append(img1)

img2 = cv2.imread('test4/base1.jpg',0) # reading the test image
img2 = filters.filter_img(img2) # filtering the image
img2 = cv2.resize(img2, (1904,3065),interpolation = cv2.INTER_AREA) #resizing the image
img_t.append(img2)

img3 = cv2.imread('test4/base2.jpg',0) # reading the test image
img3 = filters.filter_img(img3) # filtering the image
img3 = cv2.resize(img3, (1904,3065),interpolation = cv2.INTER_AREA) #resizing the image
img_t.append(img3)

img4 = cv2.imread('test4/test35.jpg',0) # reading the test image
img4 = filters.filter_img(img4) # filtering the image
img4 = cv2.resize(img4, (1904,3065),interpolation = cv2.INTER_AREA) #resizing the image
img_t.append(img4)

img5 = cv2.imread('test4/base4.jpg',0) # reading the test image
img5 = filters.filter_img(img5) # filtering the image
img5 = cv2.resize(img5, (1904,3065),interpolation = cv2.INTER_AREA) #resizing the image
img_t.append(img5)

img6 = cv2.imread('test4/base5.jpg',0) # reading the test image
img6 = filters.filter_img(img6) # filtering the image
img6 = cv2.resize(img6, (1904,3065),interpolation = cv2.INTER_AREA) #resizing the image
img_t.append(img6)

img_avg = comparisons.average_images(img_t)

###########################################################################################
# preparing test contours
###########################################################################################
img = cv2.imread('test4/base5.jpg',0) # reading the test image
img = filters.filter_img(img) # filtering the image
img = cv2.resize(img, (1904,3065),interpolation = cv2.INTER_AREA) #resizing the image
###########################################################################################
# testing the function
###########################################################################################
resize = [1904,3065]
cont_umbral = [100,255]
circular = 0.18
cent2 = callibration.extractUV(img_t,img,resize,cont_umbral,circular)
print(cent2)
###########################################################################################



#cv2.imshow('average img', img_focus)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
