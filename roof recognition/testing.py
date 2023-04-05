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
# main program 

img = cv2.imread('test4/test1.jpg',0) # reading the test image
img = filters.filter_img(img) # filtering the image
img = cv2.resize(img, (1904,3065),interpolation = cv2.INTER_AREA) #resizing the image
#imgs = cv2.resize(img, (400,640),interpolation = cv2.INTER_AREA)
# Cargar imagen del fondo
background = cv2.imread('test4/background.jpg',0) # I do the same with a background image
background = filters.filter_img(background)
background = cv2.resize(background, (1904,3065),interpolation = cv2.INTER_AREA)

# Now, I want to do is to make a comparisons of getting contours with and without background removal

cont_img = contours.contours(img,100,255) # it extract the contours under this umbrals
cont_back = contours.contours(background,100,255)
cont_img = contours.get_largest_contours(cont_img,15)
cont_back = contours.get_largest_contours(cont_back,15)
cont_img = cont_img[1:15] # it remove the contour taking the square fo the image
cont_back = cont_back[1:15]

cont_img = contours.get_largest_circularities(cont_img,0.18)
cont_back = contours.get_largest_circularities(cont_back,0.18)

img_c1 = contours.image_contours(cont_img,img) # it graphs the contours
img_c2 = contours.image_contours(cont_back,background)

img_c = img_c1-img_c2


# it is not always the best choice to remove background, so I will keep working on the initial image
# now I want to create a function to find the position of the object in pixels

#centroids = contours.get_centroids(cont_img)
#areas = contours.get_areas(cont_img)
#circularities = contours.get_circularities(cont_img)
#print(areas)
#print(circularities)
#print(centroids)

# I want to discard outliers

#cen,ar = comparisons.discart_centroids(centroids,areas,1.2)
#print("-------------")
#print(cen)
#print(ar)
#print("-------------")
#cent = comparisons.weighted_centroid(cen,ar)
#print("cent"+str(cent))
# I will choose the object to put in the image

#img_focus = filters.focus(img_c1,cent)

img_c1 = cv2.resize(img_c1, (400,640),interpolation = cv2.INTER_AREA)
img_c2 = cv2.resize(img_c2, (400,640),interpolation = cv2.INTER_AREA)
img_c = cv2.resize(img_c, (400,640),interpolation = cv2.INTER_AREA)
#img_c1 = filters.remove_salt_and_pepper_noise(img_c1)

#pure = cv2.resize(pure, (400,640),interpolation = cv2.INTER_AREA)
#filter = cv2.resize(filter, (400,640),interpolation = cv2.INTER_AREA)

cv2.imshow('Imagen sin fondo', img_c1)
cv2.imshow('Imagen con fondo', img_c)
cv2.waitKey(0)
cv2.destroyAllWindows()

