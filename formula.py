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

#Function to return rotational matrix of 45 degrees about y axis        
def y_axis_45():
    theta_U=(np.pi/2)
    Uy=np.matrix([ [np.cos(theta_U), 0, np.sin(theta_U)] , [0, 1, 0] , [-np.sin(theta_U), 0, np.cos(theta_U)] ])
    return Uy 

def y_axis(angle):
    theta_U= angle*(np.pi/180)
    Uy=np.matrix([ [np.cos(theta_U), 0, np.sin(theta_U)] , [0, 1, 0] , [-np.sin(theta_U), 0, np.cos(theta_U)] ])
    return Uy 
    
def x_axis_45():
    theta=(np.pi/2)
    Ux=np.matrix([ [1, 0, 0] , [0, np.cos(theta), -np.sin(theta)] , [0, np.sin(theta), np.cos(theta)] ])
    return Ux
def x_axis(angle):
    theta=angle*(np.pi/180)
    Ux=np.matrix([ [1, 0, 0] , [0, np.cos(theta), -np.sin(theta)] , [0, np.sin(theta), np.cos(theta)] ])
    return Ux
    
    
def z_axis_45():
    theta=(np.pi/2)
    Uz=np.matrix([ [np.cos(theta), -np.sin(theta), 0] , [np.sin(theta), np.cos(theta), 0] , [ 0, 0, 1] ])
    return Uz
        
def z_axis_180():
    theta=(np.pi)
    Uz=np.matrix([ [np.cos(theta), -np.sin(theta), 0] , [np.sin(theta), np.cos(theta), 0] , [ 0, 0, 1] ])
    return Uz   

def z_axis(angle):
    theta=angle*(np.pi/180)
    Uz=np.matrix([ [np.cos(theta), -np.sin(theta), 0] , [np.sin(theta), np.cos(theta), 0] , [ 0, 0, 1] ])
    return Uz   
#Used to rotate a point cloud
def point_cloud_multiplication(U,pc):
    
    x_cart=pc[:,0]
    y_cart=pc[:,1]
    z_cart=pc[:,2]
    
    x_cart_U=U[0,0]*x_cart+U[0,1]*y_cart+U[0,2]*z_cart
    y_cart_U=U[1,0]*x_cart+U[1,1]*y_cart+U[1,2]*z_cart
    z_cart_U=U[2,0]*x_cart+U[2,1]*y_cart+U[2,2]*z_cart
    
    xyz=np.column_stack((x_cart_U,y_cart_U,z_cart_U))
    
    return xyz   
    
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