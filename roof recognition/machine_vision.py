# lybraries needed for this project
import cv2
import math
import pandas
import numpy as np
import time as t
from matplotlib import pyplot as plt

import filters
import contours

def contour_algorithm(): #I will organize this function later
    img_read = init.experiment_mouse()
    position = [[900,880],[960,1080],[1390,1090],[260,1220],[310,200],[680,480],[680,480],[820,880],[1060,560],[520,870],[1270,570],[1360,390],[1610,690],[450,1100],[300,580],[820,750],[1120,510],[680,1200],[350,1170],[1400,1430]]
    img1 = img_read[19]

    imgf_1 = filters.focus(img1,position[19])

    imgfi = filters.filter_img(imgf_1)
    contour1 = contours.contours(imgfi,50,170)
    contour2 = contours.points_contours(contour1,20)
    angle = contours.angles(contour2[0])
    angle_p = 89.2920
    angle_r = angle-angle_p
    cv2.drawContours(imgfi, contour2, -1, (0, 255, 0), 2)
    #print(angle_r)
    heading  = contours.heading(contour2)
    print(heading)

def template_matching():
    img_read = init.experiment_mouse()
    position = [[900,880],[960,1080],[1390,1090],[260,1220],[310,200],[680,480],[680,480],[820,880],[1060,560],[520,870],[1270,570],[1360,390],[1610,690],[450,1100],[300,580],[820,750],[1120,510],[680,1200],[350,1170],[1400,1430]]
    img1 = img_read[19]

    #focus and filter
    imgf_1 = filters.focus(img1,position[19])
    imgfi = filters.filter_img(imgf_1)

    #get black img
    contour1 = contours.contours(imgfi,50,170)
    contour2 = contours.points_contours(contour1,20)
    black = contours.image_contours(contour2,imgfi)

    #Read templates and compare
    file_name = "templates1/blacktest"
    templates, angles = template_matching.upload_templates(file_name)
    angle,comp,simil =template_matching.compare_templates(imgfi,templates,angles)

    #Second templates
    #black2 = template_matching.rotation_image(black,-270)

    file_name2 = "templates1/black2test"
    #templates2,angles2 = template_matching.creation_templates(black2) #Create imgs
    templates2, angles2 = template_matching.upload_templates(file_name2)
    angle2,comp2,simil2 =template_matching.compare_templates(imgfi,templates2,angles2)

    #third templates

    #black3 = template_matching.rotation_image(black,-90)
    file_name3 = "templates1/black3test"
    #templates3,angles3 = template_matching.creation_templates(black3)
    #k = template_matching.save_library(file_name3,angles3,templates3)
    templates3, angles3 = template_matching.upload_templates(file_name3)
    angle3,comp3,simil3 =template_matching.compare_templates(imgfi,templates3,angles3)
    print(angle)
    print(simil)
    print("--------")
    print(angle2)
    print(simil2)
    print("--------")
    print(angle3)
    print(simil3)
    cv2.imshow('original', imgfi)
    cv2.imshow('original2', black)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

def find_object():
    
    return 0
