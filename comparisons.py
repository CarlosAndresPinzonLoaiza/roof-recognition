import math
import numpy as np
import cv2

def error(value1,value2):
    Error = (value1-value2)*(value1-value2)
    Error = math.sqrt(Error)
    return Error

def weight(values):
    tot = 0
    weights = []
    for i in range(0,len(values)):
        tot = tot+values[i]
    for i in range(0,len(values)):
        w = values[i]/tot
        weights.append(w)
    return weights

def inverse_weight(values):
    inv = []
    for i in range(0,len(values)):
        k = 1/values[i]
        inv.append(k)
    Winv = weight(inv)
    return Winv

def discart_outliers(centroids, desv_std):
    x_vals, y_vals = zip(*centroids)
    x_mean, y_mean = np.mean(x_vals), np.mean(y_vals)
    x_std, y_std = np.std(x_vals), np.std(y_vals)
    centroids_f = []
    for c in centroids:
        if (abs(c[0] - x_mean) <= desv_std * x_std) and (abs(c[1] - y_mean) <= desv_std * y_std):
            centroids_f.append(c)
    return centroids_f

def discart_centroids(centroids, areas, desviaciones_std):
    x_vals, y_vals = zip(*centroids)
    x_mean, y_mean = np.mean(x_vals), np.mean(y_vals)
    x_std, y_std = np.std(x_vals), np.std(y_vals)
    centroids_filt = []
    areas_filtradas = []
    for i, c in enumerate(centroids):
        if (abs(c[0] - x_mean) <= desviaciones_std * x_std) and (abs(c[1] - y_mean) <= desviaciones_std * y_std):
            centroids_filt.append(c)
            areas_filtradas.append(areas[i])
    return centroids_filt, areas_filtradas

def weighted_centroid(centroids,areas):
    x_vals,y_vals = zip(*centroids)
    sumx = 0
    sumy = 0
    sum2 = 0
    for i,c in enumerate(centroids):
        sumx = x_vals[i]*areas[i] + sumx
        sumy = y_vals[i]*areas[i] + sumy
        sum2 = areas[i] + sum2
    weight_x = sumx/sum2
    weight_y = sumy/sum2
    cent = [int(weight_y),int(weight_x)]
    return cent

def average_images(images):
    images = [np.asarray(image) for image in images]
    sum_image = np.sum(images, axis=0)
    avg_image = sum_image / len(images)
    avg_image = cv2.convertScaleAbs(avg_image)
    return avg_image

def average_perspective_matrix(perspective_matrices):
   
    matrices_array = np.array(perspective_matrices)
    
    avg_matrix = np.mean(matrices_array, axis=0)
    
    return avg_matrix