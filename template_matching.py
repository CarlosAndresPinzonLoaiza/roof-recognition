import cv2
import math
import pandas
import numpy as np
import time as t
from matplotlib import pyplot as plt

def rotation_image(img,angle): #function to rotate image
    heigh, width = img.shape[:2]
    M = cv2.getRotationMatrix2D((heigh/2, width/2), angle, 1)
    img_r = cv2.warpAffine(img, M, (heigh, width))
    return img_r

def creation_templates(img):
    templates = []
    angles = []
    for i in range(0,72):
        angle = 5*i
        img_r = rotation_image(img,angle)
        templates.append(img_r)
        angles.append(5*i)
    return templates,angles

def save_library(file_name,angles,templates):
    type = ".jpg"
    for i in range(0,len(angles)):
        name = file_name+str(angles[i])+type
        cv2.imwrite(name, templates[i])
    return 0

def upload_templates(file_name):
    angles = []
    for i in range(0,72):
        angle = 5*i
        angles.append(angle)
    type = ".jpg"
    templates = []
    for i in range(0,72):
        name = file_name+str(angles[i])+type
        template = cv2.imread(name,0)
        templates.append(template)
    return templates,angles

def compare_images(img1,img2):
    diff = cv2.absdiff(img1, img2)
    sum = diff.sum()
    return sum

def compare_templates(img,templates,angles):
    comp = [] #it can help me to graph the distribution of the template and to get some conclusions
    simil = 0 # variable to measure the minimum similitud
    ar = 0
    for i in range(0,len(templates)):
        sum = compare_images(img,templates[i])
        comp.append(sum)
        if sum >= simil:
            simil = sum
            ar = i
    angle = angles[ar]
    return angle,comp,simil
