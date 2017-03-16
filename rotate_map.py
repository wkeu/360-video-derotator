# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 14:36:37 2017

@author: temp2015
"""

import numpy as np
from formula import *
import timeit
from PIL import Image
import matplotlib.pyplot as plt

start = timeit.default_timer() #Timer for benchmarking

theta_U=(3*np.pi/2)   #Set rotation angle

#Rotation matrices for each axis
Ux=np.matrix([ [1, 0, 0] , [0, np.cos(theta_U), -np.sin(theta_U)] , [0, np.sin(theta_U), np.cos(theta_U)] ])
Uy=np.matrix([ [np.cos(theta_U), 0, np.sin(theta_U)] , [0, 1, 0] , [-np.sin(theta_U), 0, np.cos(theta_U)] ])
Uz=np.matrix([ [np.cos(theta_U), -np.sin(theta_U), 0] , [np.sin(theta_U), np.cos(theta_U), 0] , [ 0, 0, 1] ])

U=Uz  #Rotational Matrix

#file to rotate
fname="frame_1_low_res.png"

#Load Image
img = Image.open(fname)
img = img.convert('RGB')
pixel = img.load()
width, height = img.size

#x_map=np.arange(0,width)
img2 = img.copy()

#Create x,y axes corisponding to the image
x_map=np.matrix(np.arange(0,width)) 
y_map=np.matrix(np.arange(0,height)) 

#Create long and lat axes based on image
xx = 2*(x_map+0.01) / width - 1.0 #0.01 to prevent denominator of 0
yy = 2*(y_map+0.01)/ height - 1.0
lng = np.pi * xx
lat = - 0.5 * np.pi * yy

#Duplicate axes for every cordinate. Needed for element by element operators
lng=np.repeat(lng.T,height,axis=1)
lat=np.repeat(lat,width,axis=0)
        
#Convert spherical cordinate to cart
x_cart,y_cart,z_cart=arraysph2cart(1,lat,lng)

#apply matrix multiplication
x_U,y_U,z_U=arraymatrix_multiplication(U,x_cart,y_cart,z_cart)
        
#Convert cart cordinates to spherical
r_U, lat_U, lng_U=arraycart2sph(x_U,y_U,z_U)
        
#Convert long and lat (sperical) to image pixel location
ix = np.rint((0.5 * lng_U / np.pi + 0.5) * width - 0.5)
iy = np.rint((-lat_U/np.pi + 0.5) * height  - 0.5)

#If possible to vectorize this part of the code!! 
#Moves each pixel to new location
for y_map in xrange(height):
    for x_map in xrange(width):
        newpixel = pixel[ix[x_map,y_map], iy[x_map,y_map]]
        img2.putpixel([x_map, y_map], newpixel)      

#save result
img2.save("After_rotation_"+fname)
print("Finished o.O.o")

#Calculate Runtime
stop = timeit.default_timer()
total_time = stop - start

print("Run time:"+str(total_time))

"""
Heat_map 
plt.imshow(x_map.T, cmap='Blues', interpolation='nearest')
plt.colorbar()
plt.show()
plt.savefig('x_map_heat_map.png', dpi=500)
"""
