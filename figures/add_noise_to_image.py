# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 16:36:38 2017

@author: temp2015
"""

import cv2
import numpy as np
from get_xyz import *
from calculate_rmsd import *
from rotate_map import *
import timeit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import timeit
import numpy as np
import random as random

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

        #rotate
def distance_two_points(p1,p2):
    distance = (p1[0,0]-p2[0,0])**2+(p1[0,1]-p2[0,1])**2+(p1[0,2]-p2[0,2])**2
    return distance
    
    
def test(U_test,query):
    #Initial setup for loop

    #downsample
    query = cv2.resize(query, (0,0), fx=0.25, fy=0.25) 
    a=np.sqrt(1.0/3.0)
    
    
    train= rotate_map(query,U_test) #test_image
    
    #add noise
    train = sp_noise(train,0.005) #salt and pepper noise
    train = cv2.blur(train,(3,3)) #blur the imag
    
    cv2.imshow("query",query)
    cv2.imshow("train",train)
    
    test_point_start=np.array([[a, a, a], [a, a, a]])
    
    control_point=point_cloud_multiplication(U_test,test_point_start)
    
    num_points=range(1,10)
    distance_list=list()
    
    for i in range(1,250):
        train_matched_pc,query_matched_pc =obtain_point_cloud(query,train,NUMBER_OF_POINTS=i)
        
        #rotational_matrix=kabsch(query_matched_pc, train_matched_pc)
        U=kabsch(train_matched_pc,query_matched_pc)
    
        test_point_end=point_cloud_multiplication(U,test_point_start)
        
        d=distance_two_points(test_point_end,control_point)
        distance_list.append(d)
    
    result=np.asarray(distance_list)
    print("o.O.o")
    return result

    
#Import Video
fname="Spin_clip_shed_hanging.mp4"
cap = cv2.VideoCapture(fname) #Open Video File, from current directory

#Obtain Rotation Matrices
#Using Train and Query image. Querbgby behind train ie Query=frame_n-1,train=frame_n
U_test=z_axis_45()

ret, query = cap.read()

d_x=test(x_axis_45(),query)
d_y=test(y_axis_45(),query)
d_z=test(z_axis_45(),query)

"""
for i in range(0,50):
    ret, query = cap.read()
    d_x2=test(x_axis_45(),query)
    d_y2=test(y_axis_45(),query)
    d_z2=test(z_axis_45(),query)
    
    d_x=(d_x+d_x2)/2.0
    d_y=(d_y+d_y2)/2.0
    d_x=(d_y+d_y2)/2.0
"""


nof=range(1,len(d_x)+1)
nof=np.asarray(nof)

fig = plt.figure(facecolor='White')
ax1 = plt.subplot(111)

ax1.plot(nof,d_z,antialiased=True,linewidth=2.0,c='r',alpha=0.5,label="z")
ax1.plot(nof,d_y,antialiased=True,linewidth=2.0,c='g',alpha=0.5,label="y")
ax1.plot(nof,d_x,antialiased=True,linewidth=2.0,c='b',alpha=0.5,label="x")



ax1.set_yscale("log")
ax1.legend()

ax1.set_ylabel("Error (Unit Distance)")
ax1.set_xlabel("Number of Feature Points")

plt.savefig("feature_pointswith_noise.pdf",dpi=500)
###############################################################################
#
###############################################################################






