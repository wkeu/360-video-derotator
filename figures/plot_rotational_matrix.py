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

#concatinate
for i in range(0,len(U_stream_acumilated)): 
    x,y,z = arraymatrix_multiplication( U_stream_acumilated[i],start_point[0],start_point[1],start_point[2])

    point_position[i,0]=x
    point_position[i,1]=y
    point_position[i,2]=z
    
#for i in U_stream_acumilated:

#plot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['legend.numpoints'] = 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

t=np.linspace(0,1,len(U_stream_acumilated))
nop=len(U_stream_acumilated) #number of points

#Startpoint
ax.scatter(point_position[0,0],point_position[0,1],point_position[0,2], color=plt.cm.cool(0),s=80,label="Startpoint")

for j in range(0,len(U_stream_acumilated)-2):
    ax.plot(point_position[j:j+2,0],point_position[j:j+2,1],point_position[j:j+2,2], color=plt.cm.cool(255*j/nop))

#Endpoint
ax.scatter(point_position[nop-1,0],point_position[nop-1,1],point_position[nop-1,2], color=plt.cm.cool(255),s=80,label="Endpoint")

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

ax.tick_params(axis='both', which='major', labelsize=8)
ax.legend( scatterpoints=1)
plt.savefig("plot_of_rotation_over_time.png",dpi=500)

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("equal")
ax.view_init(elev=14, azim=35)
plt.tight_layout()

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

plt.savefig("plot_of_rotation_over_time.png",dpi=500)


