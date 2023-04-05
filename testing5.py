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


# reading information
backgrounds,bases,pos = init.experiment_car()

#getting UV
resize = [1904,3065]
cont_umbral = [100,255]
circular = 0.18
ct1 = callibration.extractUV(backgrounds,bases[0],resize,cont_umbral,circular)
ct2 = callibration.extractUV(backgrounds,bases[7],resize,cont_umbral,circular)
ct3 = callibration.extractUV(backgrounds,bases[1],resize,cont_umbral,circular)
ct4 = callibration.extractUV(backgrounds,bases[3],resize,cont_umbral,circular)
ct = [ct1,ct2,ct3,ct4]
ct = np.array(ct, dtype=np.float32)
print(ct)

ps1 = pos[0][0:2]
ps2 = pos[7][0:2]
ps3 = pos[1][0:2]
ps4 = pos[3][0:2]
ps = [ps1,ps2,ps3,ps4]
ps = np.array(ps, dtype=np.float32)
print(ps)

M = cv2.getPerspectiveTransform(ct, ps)
print(M)

# Convertir a matriz NumPy de tamaño (1,1,2)
U,V = 1378,480
point_px = np.array([[[U, V]]], dtype=np.float32)

# Aplicar transformación perspectiva
point_cm = cv2.perspectiveTransform(point_px, M)
point_cm = np.squeeze(point_cm)
print(point_cm)
#showing images
cv2.imshow('average img', bases[1])
cv2.waitKey(0)
cv2.destroyAllWindows()