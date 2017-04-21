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


def test(U_test,query):
    #Initial setup for loop

    #downsample

    a=np.sqrt(1.0/3.0)
    
    #rotate
    def distance_two_points(p1,p2):
        distance = (p1[0,0]-p2[0,0])**2+(p1[0,1]-p2[0,1])**2+(p1[0,2]-p2[0,2])**2
        return distance
    
    train= rotate_map(query,U_test) #test_image
    
    cv2.imshow("query",query)
    cv2.imshow("train",train)
    
    test_point_start=np.array([[a, a, a], [a, a, a]])
    
    control_point=point_cloud_multiplication(U_test,test_point_start)
    
    num_points=range(1,10)
    distance_list=list()
    
    train_matched_pc,query_matched_pc =obtain_point_cloud(query,train,NUMBER_OF_POINTS=50)
        
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


ret, query = cap.read()

"""
d_x=test(x_axis_45(),query)
d_y=test(y_axis_45(),query)
"""
#(1440p)2560x1440
accur_2560=test(z_axis(45)*x_axis(45)*y_axis(45),query)
res_2560=query.shape[0]*query.shape[1]

#(1080p)1920x1080
query_1920=cv2.resize(query, (0,0), fx=0.75, fy=0.75) 

accur_1920=test(z_axis(45)*x_axis(45)*y_axis(45),query_1920)
res_1920=query_1920.shape[0]*query_1920.shape[1]

#(720p)1280x720
query_1280 = cv2.resize(query, (0,0), fx=0.5, fy=0.5) 

accur_1280=test(z_axis(45)*x_axis(45)*y_axis(45),query_1280)
res_1280=query_1280.shape[0]*query_1280.shape[1]

#480p (854x480)
query_854 = cv2.resize(query, (0,0), fx=0.33, fy=0.33) 

accur_854=test(z_axis(45)*x_axis(45)*y_axis(45),query_854)
res_854=query_854.shape[0]*query_854.shape[1]

#360p (640x320)
query_640 = cv2.resize(query, (0,0), fx=0.25, fy=0.25) 

accur_640=test(z_axis(1.0)*x_axis(1.0)*y_axis(1.0),query_640)
res_640=query_640.shape[0]*query_640.shape[1]

#240p (426x240)
query_426 = cv2.resize(query, (0,0), fx=0.16, fy=0.16) 

accur_426=test(z_axis(1.0)*x_axis(1.0)*y_axis(1.0),query_426)
res_426=query_426.shape[0]*query_426.shape[1]


"""
d_z_270=test(z_axis(270.0),query)
d_z_180=test(z_axis(180.0),query)

d_z_45=test(z_axis(45.0),query)
d_z_135=test(z_axis(135.0),query)
d_z_225=test(z_axis(225.0),query)
"""

"""
for i in range(0,30):
    ret, query = cap.read()
    d_x2=test(x_axis_45(),query)
    d_y2=test(y_axis_45(),query)
    d_z2=test(z_axis_45(),query)
    
    d_x=(d_x+d_x2)/2.0
    d_y=(d_y+d_y2)/2.0
    d_x=(d_y+d_y2)/2.0
"""
"""
nof=range(1,len(d_z)+1)
nof=np.asarray(nof)
"""
fig = plt.figure(facecolor='White')
ax1 = plt.subplot(111)

plt.rcParams['legend.numpoints'] = 1

ax1.scatter(accur_2560, res_2560, s=80, c="r",label="1440p: 2560x1440",alpha=0.75)
ax1.scatter(accur_1920, res_1920, s=80, c="g",label="1080p: 1920x1080",alpha=0.75)
ax1.scatter(accur_1280, res_1280, s=80, c="b",label="720p: 1280x720",alpha=0.75)
ax1.scatter(accur_854, res_854, s=80, c="c",label="480p: 854x480",alpha=0.75)
ax1.scatter(accur_640, res_640, s=80, c="y",label="360p: 640x360",alpha=0.75)
ax1.scatter(accur_426, res_426, s=80, c="m",label="240p: 426x240",alpha=0.75)



ax1.set_yscale("log")
ax1.set_xscale('log',basex=10)

ax1.legend( scatterpoints=1)

ax1.set_ylim([0, 4e6])
ax1.set_xlim([1.5e-6,0.5e-4])

ax1.set_xlabel("Error (Unit Distance)")
ax1.set_ylabel("Number of Pixels")

plt.savefig("accuracy_for_different_resolutions.pdf")

#ax1.plot(nof,d_x,antialiased=True,linewidth=2.0,c='r',alpha=0.5,label="x")

#ax1.plot(nof,d_y,antialiased=True,linewidth=2.0,c='g',alpha=0.5,label="y")
#ax1.plot(nof,d_z_90,antialiased=True,linewidth=2.0,c='b',alpha=0.5,label="z_90")
"""
ax1.plot(nof,d_z_180,antialiased=True,linewidth=2.0,c='r',alpha=0.5,label="z_180")
ax1.plot(nof,d_z_270,antialiased=True,linewidth=2.0,c='g',alpha=0.5,label="z_270")

ax1.plot(nof,d_z_45,antialiased=True,linewidth=2.0,c='c',alpha=0.5,label="z_45")
ax1.plot(nof,d_z_135,antialiased=True,linewidth=2.0,c='m',alpha=0.5,label="z_135")
ax1.plot(nof,d_z_225,antialiased=True,linewidth=2.0,c='y',alpha=0.5,label="z_225")
"""
"""

ax1.legend()

ax1.set_ylabel("Error (Unit Distance)")
ax1.set_xlabel("Number of Feture Points")

#plt.savefig("plot_testing_feature_points_over_30_images.png",dpi=500)

im = np.empty((1000,1000), np.uint8)
cv2.randn(im,(0),(99))
"""