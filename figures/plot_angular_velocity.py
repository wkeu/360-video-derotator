# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 17:30:57 2017

@author: temp2015
"""

import cv2
import numpy as np
from get_xyz import *
from calculate_rmsd import *
from rotate_map import *
import timeit

###############################################################################
# Obtain Rotations
###############################################################################
start = timeit.default_timer()
#gh

#Import Video
fname="spin_clip_2.mp4"
cap = cv2.VideoCapture(fname) #Open Video File, from current directory

#Obtain Rotation Matrices
#Using Train and Query image. Query behind train ie Query=frame_n-1,train=frame_n

#Initial setup for loop
ret, train = cap.read()
U_stream=list()

while(cap.isOpened()):
    
    query=train 
    ret, train = cap.read()
    
    if ret==0:
        break
    
    #Definitly not the most efficient implemenation
    #Calculating Certain Values Twice
    query_matched_pc, train_matched_pc =obtain_point_cloud(query,train)
    
    #rotational_matrix=kabsch(query_matched_pc, train_matched_pc)
    U=kabsch(train_matched_pc,query_matched_pc) #Assume for the moment that this matrix is correct. 
    
    U_stream.append(U)
    
print("o.O.o\nRotational Matrix Stream Obtained")

###############################################################################
#Acumulate matrices
###############################################################################
n_frames=len(U_stream)

U_stream_acumilated=list()
U_stream_acumilated.append(U_stream[0])
U_acumilated=np.matrix(U_stream[0])

for n in range(1,n_frames):
    U_acumilated= U_acumilated*np.matrix(U_stream[n])
    U_stream_acumilated.append(U_acumilated)

print("o.O.o\nRotational Matrices Accumulated")

start_point= np.array([0,1,0])
point_position=np.zeros([len(U_stream_acumilated),3])

point_position[0,0]=start_point[0]
point_position[0,1]=start_point[1]
point_position[0,2]=start_point[2]

#concatinate
for i in range(1,len(U_stream_acumilated)): 
    x,y,z = arraymatrix_multiplication( U_stream_acumilated[i-1],start_point[0],start_point[1],start_point[2])

    point_position[i,0]=x
    point_position[i,1]=y
    point_position[i,2]=z
    
#for i in U_stream_acumilated:

#plot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fps=30

time=np.arange(0.0,float(len(U_stream_acumilated)/fps),(1/float(fps)))

fig = plt.figure()

plt.plot(time,point_position[0:180,0])

# Two subplots, the axes array is 1-d
ax1 = plt.subplot(311)
ax1.scatter([1, 2], [3, 4])
ax1.set_xlim([0, 5])
ax1.set_ylim([0, 5])


ax2 = plt.subplot(312)
ax2.scatter([1, 2],[3, 4])
ax2.set_xlim([0, 5])
ax2.set_ylim([0, 5])

f, axarr = plt.subplots(3, sharex=True,facecolor='White')
axarr[0].plot(time,point_position[0:180,0],label="x axis")
axarr[0].set_title('X axis')
axarr[0].set_ylim([-1.1,1.1])
axarr[0].yaxis.set_ticks(np.arange(-1, 1.1, 1))
axarr[1].plot(time,point_position[0:180,1],c='g',label="y axis")
axarr[1].set_ylim([-1.1,1.1])
axarr[1].yaxis.set_ticks(np.arange(-1, 1.1, 1))
axarr[1].set_title('Y axis')
axarr[2].plot(time,point_position[0:180,2],c='r',label="z axis")
axarr[2].set_ylim([-1.1,1.1])
axarr[2].yaxis.set_ticks(np.arange(-1, 1.1, 1))
axarr[2].set_title('Z axis')
axarr[2].set_xlabel("time (seconds)")
plt.savefig("angular_velocity_over_time_axis.png",dpi=500)


