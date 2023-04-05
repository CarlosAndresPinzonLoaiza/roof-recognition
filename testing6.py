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

#Main function

#1- read images 

backgrounds,bases,pos = init.experiment_car()

#2- get point of the bases 

#3- get perspective transformation

#4- get test points

#5- check and validate

#6- graphs 

cv2.imshow('average img', backgrounds[1])
cv2.waitKey(0)
cv2.destroyAllWindows()

