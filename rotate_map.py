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

def rotate_map(frame,U):

    #Convert frame to PIL image
    cv2_im = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2_im)

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

    #convert img2 to openCV format
    img2_cv = np.array(img2)
    img2_cv=cv2.cvtColor(img2_cv,cv2.COLOR_RGB2BGR)
    
    return img2_cv