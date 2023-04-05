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

def extractUV(backgrounds,base_img,resize,cont_umbral,circular):
    # I read all the background outside of this function to make it more modular
    img_avg = comparisons.average_images(backgrounds)
    #preparing contour of the base
    img = cv2.resize(base_img, resize,interpolation = cv2.INTER_AREA) #resizing the image
    cont_img = contours.contours(img,cont_umbral[0],cont_umbral[1]) # it extract the contours under this umbrals
    cont_img = contours.get_largest_contours(cont_img,12)
    cont_img = cont_img[1:12] # it remove the contour taking the square fo the image
    cont_img = contours.get_largest_circularities(cont_img,circular)
    img_c1 = contours.image_contours(cont_img,img) # it graphs the contours
    #preparing contours of the backgrounds
    cont_img2 = contours.contours(img_avg,cont_umbral[0],cont_umbral[1]) # it extract the contours under this umbrals
    cont_img2 = contours.get_largest_contours(cont_img2,12)
    cont_img2 = cont_img2[1:12] # it remove the contour taking the square fo the image
    cont_img2 = contours.get_largest_circularities(cont_img2,circular)
    img_c2 = contours.image_contours(cont_img2,img) # it graphs the contours
    #getting the area inteseption to extract the object contour
    img_c = img_c1-img_c2
    cont_img3 = contours.contours(img_c,10,255) # it extract the contours under this umbrals
    cont_img3 = contours.get_largest_contours(cont_img3,3)
    cont_img3 = contours.get_largest_circularities(cont_img3,circular)
    cent = contours.get_centroids(cont_img3)
    output1 = cent[0]
    output = [output1[0],output1[1]]
    return output
