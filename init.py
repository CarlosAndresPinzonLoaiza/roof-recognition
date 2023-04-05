import cv2
import math
import pandas
import numpy as np
import time as t
from matplotlib import pyplot as plt

def read_test(): #function to read the images and the angles for the test
    name1 = 'test3/test'
    name2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    name3 = '.jpg'
    img_read = [] # this variable will contains all the test images
    img_angles = [0,30,60,90,120,150,180,210,240,270,300,330,0] # angles to be obtained
    img_position = [[950,860],[1050,700],[1330,600],[1330,600],[1330,900],[1430,1350],[930,1250],[730,1300],[580,1230],[480,1150],[480,900],[480,800],[580,500]] #position obtained
    for i in range(0,len(name2)):
        name_read = name1+name2[i]+name3
        image_readt = cv2.imread(name_read,0)
        image_readt = cv2.resize(image_readt, (1904,3065),interpolation = cv2.INTER_AREA)
        img_read.append(image_readt)
    return img_read,img_angles,img_position 

def Experiment_box(): #function to run the first experiment with the box
    name1 = 'tests3/test'
    name2 =['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    name3 = '.jpg'
    img_read = [] # this variable will contains all the test images
    img_angles = [0,30,60,90,120,150,180,210,240,270,300,330,0] # angles to be obtained
    img_position = [[950,860],[1050,700],[1330,600],[1330,600],[1330,900],[1430,1350],[930,1250],[730,1300],[580,1230],[480,1150],[480,900],[480,800],[580,500]] #position obtained
    for i in range(0,len(name2)):
        name_read = name1+name2[i]+name3
        image_readt = cv2.imread(name_read,0)
        image_readt = cv2.resize(image_readt, (1904,3065),interpolation = cv2.INTER_AREA)
        img_read.append(image_readt)
    return img_read,img_angles,img_position 

#experiment mouse

def experiment_mouse():
    name1 = 'test3/test'
    name2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    name3 = '.jpg'
    img_read = [] # this variable will contains all the test images
    for i in range(0,len(name2)):
        name_read = name1+name2[i]+name3
        image_readt = cv2.imread(name_read,0)
        image_readt = cv2.resize(image_readt, (1904,3065),interpolation = cv2.INTER_AREA)
        img_read.append(image_readt)
    return img_read

def experiment_car(): # To do
    name1a = 'test5/background'
    name1b = 'test5/base'
    name2a = ['1','2','3','4','5','6','7','8','9']
    name2b = ['1','2','3','4','5','6','7','8','9','10']
    name3 = '.jpg'
    img_read1 = []
    for i in range(len(name2a)):
        name_read = name1a+name2a[i]+name3
        image_readt = cv2.imread(name_read,0)
        image_readt = cv2.resize(image_readt, (1904,3065),interpolation = cv2.INTER_AREA)
        img_read1.append(image_readt)
    img_read2 = []
    for i in range(len(name2b)):
        name_read = name1b+name2b[i]+name3
        image_readt = cv2.imread(name_read,0)
        image_readt = cv2.resize(image_readt, (1904,3065),interpolation = cv2.INTER_AREA)
        img_read2.append(image_readt)
    pos1 = [60,30,0]
    pos2 = [60,90,90]
    pos3 = [60,150,180]
    pos4 = [120,150,270]
    pos5 = [120,180,0]
    pos6 = [120,210,90]
    pos7 = [150,150,180]
    pos8 = [150,90,270]
    pos9 = [150,60,0]
    pos10 = [180,60,90]
    pos = []
    pos.append(pos1)
    pos.append(pos2)
    pos.append(pos3)
    pos.append(pos4)
    pos.append(pos5)
    pos.append(pos6)
    pos.append(pos7)
    pos.append(pos8)
    pos.append(pos9)
    pos.append(pos10)
    return img_read1,img_read2,pos


#def experiment_video(): #To do

