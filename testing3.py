# python lybraries
import cv2
import math
import pandas
import numpy as np
import time as t
from matplotlib import pyplot as plt
from sklearn.cluster import MeanShift
from scipy.spatial.distance import cdist
import time

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

##########################################################################
def distance(cent1,cent2):
    d = math.sqrt((cent1[0] - cent2[0]) ** 2 + (cent1[1] - cent2[1]) ** 2)
    return d

def agrupar_contornos(contornos, r):
    centros = []
    for contorno in contornos:
        M = cv2.moments(contorno)
        centro = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        centros.append(centro)
    grupos = []
    visitados = set()
    for i in range(len(contornos)):
        if i in visitados:
            continue
        grupo = [i]
        visitados.add(i)
        for j in range(i+1, len(contornos)):
            if j in visitados:
                continue
            distancia = np.linalg.norm(np.array(centros[i]) - np.array(centros[j]))
            if distancia < r:
                grupo.append(j)
                visitados.add(j)
        grupos.append(grupo)
    grupos_contornos = []
    for grupo in grupos:
        contornos_grupo = [contornos[i] for i in grupo]
        grupos_contornos.append(contornos_grupo)
    return grupos_contornos

def joints(clist):
    js = []
    for conts in clist:
        j = contours.joint(conts)
        js.append(j)
    return js

def centroids(jlist):
    Jcent = []
    for list in jlist:
        cent = contours.centroid(list)
        Jcent.append(cent)
    return Jcent

def headings(Jlist):
    Jheading = []
    for list in Jlist:
        heading = contours.heading(list)
        Jheading.append(heading)
    return Jheading

def joint_ang_cent(centroids, angles):
    unifies = []
    for i in range(len(centroids)):
        centt = centroids[i]
        ang = angles[i]
        unify = [centt[0],centt[1],ang]
        unifies.append(unify)
    return unifies

def output_info(cents):
    letter = "||"
    for cent in cents:
        letter = letter+"x="+str(int(cent[0]))+",y="+str(int(cent[1]))+",theta="+str(int(cent[2]))+"||"
    print(letter)
    print("-------------------------------------")

##########################################################################

# Carga el video desde un archivo
cap = cv2.VideoCapture('Simulations/movie.mp4')
t1 = time.time()
s = 0
while(cap.isOpened()):
    # Lee un frame del video
    ret, frame = cap.read()
    s = s+1
    # Si se llega al final del video, se sale del bucle
    if not ret:
        break

    # Aplica algún procesamiento al frame (por ejemplo, cambiar a escala de grises)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.resize(gray, (500,500),interpolation = cv2.INTER_AREA)

    cont_img = contours.contours(gray,120,255)
    cont_img = contours.get_largest_contours(cont_img,20)
    cont_img = cont_img[1:20] # it remove the contour taking the square fo the image
    #cont_img = contours.get_largest_circularities(cont_img,0.18)
    img_c1 = contours.image_contours(cont_img,gray)
    img_c1 = cv2.resize(img_c1, (500,500),interpolation = cv2.INTER_AREA)
    # Muestra el frame procesado en una ventana
    cv2.imshow('Video', img_c1)
    ###########################
    cont_list = agrupar_contornos(cont_img,255)
    jointlist = joints(cont_list)
    Jcent = centroids(jointlist)
    Jheading = headings(jointlist)
    sout = joint_ang_cent(Jcent,Jheading)
    output_info(sout)
    ###########################

    # Espera por 25ms y verifica si se ha presionado la tecla 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
t2 = time.time()
t3 = t2-t1
print(t3)
print(s)
# Libera los recursos
cap.release()
cv2.destroyAllWindows() 