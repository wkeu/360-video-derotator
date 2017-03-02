# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 14:36:37 2017

@author: temp2015
"""

import numpy as np
import math as m
from formula import *
  

import math
from PIL import Image

theta_U=(3*np.pi/2)

Ux=np.matrix([ [1, 0, 0] , [0, np.cos(theta_U), -np.sin(theta_U)] , [0, np.sin(theta_U), np.cos(theta_U)] ])
Uy=np.matrix([ [np.cos(theta_U), 0, np.sin(theta_U)] , [0, 1, 0] , [-np.sin(theta_U), 0, np.cos(theta_U)] ])
Uz=np.matrix([ [np.cos(theta_U), -np.sin(theta_U), 0] , [np.sin(theta_U), np.cos(theta_U), 0] , [ 0, 0, 1] ])

U=Ux

fname="world_map2.png"
f1=open("logfile_pixel.txt","w")
f2=open("logfile_sphere_cart_conversion.txt","w")

img = Image.open(fname)
img = img.convert('RGB')
pixel = img.load()
width, height = img.size


img2 = img.copy()
for y_map in xrange(height):
    for x_map in xrange(width):
        xx = 2*(x_map+0.01) / width - 1.0 #0.01 is to prevent case where 
        yy = 2*(y_map+0.01)/ height - 1.0
        lng = math.pi * xx
        lat = - 0.5 * math.pi * yy
        
        #phi=lat tetha=lng sph2cart(r,theta,phi)
        x_cart,y_cart,z_cart=sph2cart(1,lat,lng)
        
        #Apply roation
        pt_cart=np.matrix([ [x_cart] , [y_cart], [z_cart] ])

        pt_cart_U=np.matmul(U, pt_cart)

        x_U = pt_cart_U[0]
        y_U = pt_cart_U[1]
        z_U = pt_cart_U[2]
        
        #r,theta,phi
        r_U, lat_U, lng_U=cart2sph(x_U,y_U,z_U)
        
        #ix and iy must be integers
        #location frame will be moved
        ix = int((0.5 * lng_U / math.pi + 0.5) * width - 0.5)
        iy = int(round((-lat_U/math.pi + 0.5) * height  - 0.5))

        #Prevents the image from being out of bounds
        if iy>=height:
            iy=height-1
            
        if ix>=width:
            ix=width-1
            
        newpixel = pixel[ix, iy]
        img2.putpixel([x_map, y_map], newpixel)
        #I tries as mentionned in the following code to invert x and y in the two previous lines but the index error out of range comes back 
        
        if(x_map%20==0):
            f1.write("Finished point x:"+str(x_map)+ " ix:" +str(ix) +" y:"+str(y_map) + " iy:" + str(iy)+ "\n")
            f2.write("Lat:"+str(float(lat))+" ULat:"+str(float(lat_U))+"\nLng:"+str(float(lng))+" ULng:"+str(float(lng_U))+ "\n")
            print("Finished point x:"+str(x_map)+ " ix:" +str(ix) +" y:"+str(y_map) + " iy:" + str(iy)+ "\n")
         
img2.save("05_test_rotated_"+fname)

print("Finished o.O.o")
f.close() #close the logfile


