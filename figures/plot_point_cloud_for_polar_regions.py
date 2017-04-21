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


#Import Video
fname="test1_raw_initial_test.mp4"
fout="test1_derotated_initial_test.avi"
cap = cv2.VideoCapture(fname) #Open Video File, from current directory
out_fps=8

#Obtain Rotation Matrices
#Using Train and Query image. Query behind train ie Query=frame_n-1,train=frame_n
#gg

#Initial setup for loop
ret, train = cap.read()
ret, query = cap.read()

query_pc,train_pc=obtain_point_cloud(train,query)

train_polar=rotate_map(train,y_axis_45())
query_polar=rotate_map(query,y_axis_45())

query_matched_pc_y_axis_45, train_matched_pc_y_axis_45 =obtain_point_cloud(query_polar,train_polar)
    
#Rotate points back 45 degrees about y axis
query_matched_pc_y_axis_45=point_cloud_multiplication(-y_axis_45(),query_matched_pc_y_axis_45)
pol_pc=query_matched_pc_y_axis_45

#cv2.imshow("train",train)
#cv2.imshow("train_polar",train_polar)
plt.rcParams['legend.numpoints'] = 1

#starting plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = 1
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0.0:pi:50j, 0.0:2.0*pi:50j]
x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)



ax.plot_surface(
    x, y, z,  rstride=1, cstride=1, color='w', alpha=0.1, linewidth=0)

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
ax.view_init(elev=14, azim=35)
plt.tight_layout()

#ax.scatter(query_pc[:,0], query_pc[:,1], query_pc[:,2], zdir='z', color='g',s=20, depthshade=True,label="Polar Feature Point")
ax.scatter(pol_pc[:,0], pol_pc[:,1], pol_pc[:,2], zdir='z', color='g',s=20, depthshade=True,label="Polar Feature Point")

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

ax.tick_params(axis='both', which='major', labelsize=8)
ax.legend( scatterpoints=1)
plt.savefig("scatter_plot_point_cloud_ploar_only.pdf",dpi=500)

#Create a scatter plot.


