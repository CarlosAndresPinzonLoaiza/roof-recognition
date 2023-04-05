import cv2
import math
import pandas
import numpy as np
import time as t
from matplotlib import pyplot as plt

def remove_background(object_img, background_img): #function to remove background
    gray_obj = object_img#cv2.cvtColor(object_img, cv2.COLOR_BGR2GRAY)
    gray_back = background_img#cv2.cvtColor(background_img, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray_obj, gray_back) # computing the difference
    thresh = cv2.adaptiveThreshold(diff, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh_inv = cv2.bitwise_not(thresh) # binarize the image
    result = cv2.bitwise_and(object_img, object_img, mask=thresh_inv) # mask is applied to remove background
    #result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    #_, result_bw = cv2.threshold(result_gray, 10, 255, cv2.THRESH_BINARY)
    #result_final = cv2.bitwise_not(result_bw) # invert image to have the background white
    return result

def remove_salt_and_pepper_noise(image): # salt and pepper filter
    filtered_image = cv2.medianBlur(image, 5)
    filtered_image = cv2.medianBlur(filtered_image, 5)
    return filtered_image

def focus(img,position): #filter to focus the image to the square where the robot is
    x_position = position[1]
    y_position = position[0]
    print("x:"+str(x_position)+"y:"+str(y_position))
    x_min = x_position-200
    y_min = y_position-200
    x_max = x_position+200
    y_max = y_position+200
    if x_min <= 0:
        x_min = 0
    if x_max >= 1904:
        x_max = 1904
    if y_min <= 0:
        y_min = 0
    if y_max >= 3065:
        y_max = 3065
    img_focus = img[x_min:x_max,y_min:y_max]
    return img_focus # it returns the section of the image given the coordinates

def filter_img(img): #function to smooth the image, it will facilitate the extraction of contours
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_clahe = clahe.apply(img)
    blur_image = cv2.GaussianBlur(img_clahe, (5, 5), 0)
    #laplacian_image = cv2.Laplacian(blur_image, cv2.CV_16S, ksize=3)
    #canny_image = cv2.Canny(laplacian_image, 100, 200)
    img_filter = blur_image#laplacian_image#laplacian_image
    return img_filter # it returns the image filtered