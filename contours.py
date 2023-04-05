import cv2
import math
import pandas
import numpy as np
import time as t
from matplotlib import pyplot as plt
from sklearn.cluster import MeanShift
from scipy.spatial.distance import cdist

def squareclose(img,point): #function to detect my interest points
    x = point[0]
    y = point[1]
    img2 = img
    img2[x-20:x+20,y-20:y+20] = 0
    return img2 

def contours(img,a,b): #function to get the contours of an image
    ret, thresh = cv2.threshold(img, a, b, cv2.THRESH_BINARY) # threshold to binarize the image
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE) #funtion to find contours
    return contours

def get_largest_contours(contours,num_contours):
    # Calcula el área de cada contorno y crea una lista con los contornos y sus áreas
    contours_with_area = [(contour, cv2.contourArea(contour)) for contour in contours]

    # Ordena la lista en orden descendente según el área
    contours_with_area_sorted = sorted(contours_with_area, key=lambda x: x[1], reverse=True)

    # Selecciona los 'num_contours' contornos con las áreas más grandes
    largest_contours = [contour for contour, _ in contours_with_area_sorted[:num_contours]]

    return largest_contours

def points_contours(contours,c):#function to reduce the number of contours
    cont2 = []
    for j in range(0,len(contours)):
        s = len(contours[j])
        if s >=c:
            cont2.append(contours[j])
    cont3 = get_largest_contours(contours,4)
    return cont3[1:]

def circularity(contour): #function to obtain the circularity given a contour
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour,True)
    Circularity = (perimeter*perimeter)/(12.5663*area)
    return Circularity

def angles(contour): #function to obtain the angle of the main axe of a contour
    [vx,vy,x,y] = cv2.fitLine(contour, cv2.DIST_L2,0,0.01,0.01)
    angle = (360/(2*3.141592))*math.atan2(vy,vx)
    return angle

def get_angles(contours):
    anglesList = []
    for contour in contours:
        ang = angles(contour)
        anglesList.append(ang)
    return anglesList

def joint(contours):
    puntos = []
    for cnt in contours:
        for punto in cnt:
            puntos.append(punto.tolist())
    vector = np.array(puntos)
    return vector.tolist()

def centroid(joint):
    x = []
    y = []
    for i in range(len(joint)):
        s = joint[i]
        xn = s[0][0]
        yn = s[0][1]
        x.append(xn)
        y.append(yn)
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    cent = [x_bar,y_bar]
    return cent

def limits_square(joints):
    V = np.squeeze(joints)
    x = V[0][:]
    y = V[1][:]

    xmax = np.max(x)
    xmin = np.min(x)
    ymax = np.max(y)
    ymin = np.min(y)
    return xmax, xmin, ymax, ymin


def center_square(xmax,xmin,ymax,ymin):
    centerx = (xmax+xmin)/2
    centery = (ymax+ymin)/2
    center = [centerx,centery]
    return center

def heading(joints):
    cent = centroid(joints)
    xmax,xmin,ymax,ymin = limits_square(joints)
    center = center_square(xmax,xmin,ymax,ymin)
    vx = cent[0]-center[0]
    vy = cent[1]-center[1]
    angle_p = (360/(2*3.141592))*math.atan2(vy,vx)
    angle_r = 71.156163
    heading = angle_p-angle_r
    return heading

def image_contours(contours, img): 
    black_img = np.zeros_like(img)
    cv2.drawContours(black_img, contours, -1, 255, -1)
    return black_img

def get_centroids(contours):
    centroids = []
    for contour in contours:
        moments = cv2.moments(contour)
        if moments["m00"] != 0:
            cX = int(moments["m10"] / moments["m00"])
            cY = int(moments["m01"] / moments["m00"])
            centroids.append((cX, cY))
        else:
            centroids.append(None)
    return centroids

def get_areas(contours):
    areas = []
    for contour in contours:
        area = cv2.contourArea(contour)
        areas.append(area)
    return areas

def get_circularities(contours):
    circularities = []
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        area = cv2.contourArea(contour)
        if perimeter != 0:
            circularidad = (4 * np.pi * area) / (perimeter ** 2)
        else:
            circularidad = 0
        circularities.append(circularidad)
    return circularities

def get_largest_circularities(contours, min_circularity):
    contour_filter= []
    
    for contorno in contours:
        area = cv2.contourArea(contorno)
        perimetro = cv2.arcLength(contorno, True)
        circularidad = (4 * np.pi * area) / (perimetro**2)
        if circularidad >= min_circularity:
            contour_filter.append(contorno)
    return contour_filter
