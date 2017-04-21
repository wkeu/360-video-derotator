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

#Import Video
fname="Spin_clip_shed_hanging.mp4"
cap = cv2.VideoCapture(fname) #Open Video File, from current directory

#Obtain Rotation Matrices
#Using Train and Query image. Querbgby behind train ie Query=frame_n-1,train=frame_n

#Initial setup for loop
ret, query = cap.read()


###############################################################################
# Obtain Rotations
###############################################################################

time=list()
number_of_pixels=list()

while (query.size)>350:
    start = timeit.default_timer()
    test1= rotate_map(query,y_axis_45())
    end= timeit.default_timer()
    
    time.append(end-start)
    number_of_pixels.append(query.size)
    
    print("Calculated for image with"+str(query.size)+"pixels")
    #Downsample
    query = cv2.resize(query, (0,0), fx=0.95, fy=0.95) 

x=time[:]
y=number_of_pixels[:]

x=np.asarray(x)
y=np.asarray(y,dtype=float)  

fig = plt.figure(facecolor='White')
ax1 = plt.subplot(111)

ax1.plot(x,y,antialiased=True,linewidth=2.0,c='g',alpha=0.5)
ax1.set_yscale("log")
ax1.set_ylabel("Number of Pixels")
ax1.set_xlabel("time (seconds)")

plt.savefig("plot_resolution_over_time.png",dpi=500)
