# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:52:28 2017

@author: temp2015
"""
import math
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

width=640
height=320
theta=np.pi/2

U=np.matrix([ [np.cos(theta), 0, np.sin(theta)] , [0, 1, 0] , [-np.sin(theta), 0, np.cos(theta)] ])

#point on cordinate map x,y
pt=320,160

lat = np.linspace(-180, 180, width) * np.pi/180            # Create Long axis
lng = np.linspace(-90, 90, height) * np.pi/180        # Create Lat axis 

pt_lng=lng[pt[1]]
pt_lat=lat[pt[0]]

#xConvert to cart. This can be refactored
Z = np.cos(pt_lat) * np.cos(pt_lng)
Y = np.cos(pt_lat) * np.sin(pt_lng)
X = -np.sin(pt_lat)
D = np.sqrt(X*X+Y*Y+Z*Z)

pt_cart=np.matrix([ [X] , [Y], [Z] ])

pt_cart_rotated=np.matmul(U, pt_cart)

"""
Plot before and after points
"""

# repeat code from one of the examples linked to in the question, except for specifying facecolors:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Plot the point(s)
#Original Point
before=ax.scatter(float(pt_cart[0]),float(pt_cart[1]),float(pt_cart[2]), c='g',marker='o',s=100)
#Rotated Point
after=ax.scatter(float(pt_cart_rotated[0]),float(pt_cart_rotated[1]),float(pt_cart_rotated[2]), c='r',marker='o',s=100)


#Set axes range 
ax.set_xlim3d(0, 1)
ax.set_ylim3d(0, 1)
ax.set_zlim3d(0, 1)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.legend([before, after], ['before', 'after'])
plt.show()
