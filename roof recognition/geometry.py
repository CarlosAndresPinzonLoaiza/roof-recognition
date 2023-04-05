# lybraries needed for this project
import cv2
import math
import pandas
import numpy as np
import time as t
from matplotlib import pyplot as plt


def multiply_matrix(A,B): # I define function to multiply matrix
  global C
  if  A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
    for row in range(rows): 
        for col in range(cols):
            for elt in range(len(B)):
              C[row, col] += A[row, elt] * B[elt, col]
    return C

def extrinsic(Ax,Ay,Az,P): # function to get the extrinsic matric
    Rx = np.array((math.cos(Ax),math.sin(Ay),0),(-math.sin(Ax),math.cos(Ax),0),(0,0,1))
    Ry = np.array((math.cos(Ay),0,math.sin(Ay)),(0,1,0),(-math.sin(Ay),0,math.cos(Ay)))
    Rz = np.array((0,0,1),(0,math.cos(Az),math.sin(Az)),(0,-math.sin(Az),math.cos(Az)))
    
    R = multiply_matrix(Ry,Rz)
    R = multiply_matrix(Rx,R)

    T = np.array((R,P)(0,0,0,1))
    return T

def intrinsic(f,gama,u0,v0): #function to get the intrinsic matrix
    I = np.array((f,gama,u0),(0,f,v0),(0,0,1))
    return I

def Image_matrix(I,T): # function to get the image matrix
    L = multiply_matrix(I,T)
    return L

def perspective_transform(init_points,end_points): # function to get the perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(init_points,end_points)
    return matrix

def transform_image(img,matrix): #function to transform the image into eagle view
    rows, cols = img_read[2].shape[:2]
    perspective = cv2.warpPerspective(img,matrix,(640,480))
    perspective = cv2.resize(perspective, (640,480),interpolation = cv2.INTER_AREA)
    return perspective

def world_framework(u,v): # correlate the position in the picture with the real world
    rows, cols = img_read[2].shape[:2]
    perspective = cv2.warpPerspective(img,matrix,(640,480))
    perspective = cv2.resize(perspective, (640,480),interpolation = cv2.INTER_AREA)
    return perspective

def camera_framework(x,y,z): # correlate the position in the real world with the camera frame
    rows, cols = img_read[2].shape[:2]
    perspective = cv2.warpPerspective(img,matrix,(640,480))
    perspective = cv2.resize(perspective, (640,480),interpolation = cv2.INTER_AREA)
    return perspective

