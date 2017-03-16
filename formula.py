# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 14:36:37 2017

@author: temp2015
"""

import numpy as np
import math as m

#Formular declarations
def cart2sph(x,y,z):
    r = np.sqrt(x**2 + y**2 +z**2)
    theta = np.arcsin(z/r) #*(180/np.pi)   # theta
    phi = np.arctan2(y,x) #*(180/np.pi)            # phi
    return r,theta,phi

def sph2cart(r,theta,phi):
    x=r*np.cos(theta)*np.cos(phi)
    y=r*np.cos(theta)*np.sin(phi)
    z=r*np.sin(theta)
    return x,y,z
    
#Formular declarations
def arraycart2sph(x,y,z):
    r = 1#np.sqrt(x**2 + y**2 +z**2)
    theta = np.arcsin(np.divide(z,r)) #*(180/np.pi)   # theta
    phi = np.arctan2(y,x) #*(180/np.pi)            # phi
    return r,theta,phi

def arraysph2cart(r,theta,phi):
    x=r*np.multiply(np.cos(theta),np.cos(phi))
    y=r*np.multiply(np.cos(theta),np.sin(phi))
    z=r*np.sin(theta)
    return x,y,z
    
    
def arraymatrix_multiplication(U,x_cart,y_cart,z_cart):
    
    x_cart_U=U[0,0]*x_cart+U[0,1]*y_cart+U[0,2]*z_cart
    y_cart_U=U[1,0]*x_cart+U[1,1]*y_cart+U[1,2]*z_cart
    z_cart_U=U[2,0]*x_cart+U[2,1]*y_cart+U[2,2]*z_cart
    
    return x_cart_U,y_cart_U,z_cart_U
#Check theta  
#Check the 2 quadrants
#plus and minus theta 45 degrees
"""
a,b,c=cart2sph(0, 0.70710, 0.70710)
sph2cart(a, b, c)

a,b,c=cart2sph(0, 0.70710, -0.70710)
sph2cart(a, b, c)

#plus and minus 
a,b,c=cart2sph(0, 0.866025, +0.5)
sph2cart(a, b, c)

a,b,c=cart2sph(0, 0.866025, -0.5)
sph2cart(a, b, c)

#Check the 4 quadrants
a,b,c=cart2sph(0.70710, 0.70710, 0)
sph2cart(a, b, c)

a,b,c=cart2sph(-0.70710, +0.70710, 0)
sph2cart(a, b, c)

a,b,c=cart2sph(-0.70710, -0.70710, 0)
sph2cart(a, b, c)

a,b,c=cart2sph(+0.70710, -0.70710, 0)
sph2cart(a, b, c)
"""