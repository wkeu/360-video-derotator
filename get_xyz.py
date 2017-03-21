# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 15:08:06 2017

@author: temp2015
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
from formula import *

def obtain_point_cloud(query_image,train_image):
    NUMBER_OF_POINTS=40 #Tested number which give good results

    #Read in the frames
    img1 = query_image # Frame0 (query image)
    img2 = train_image # Frame1 (train image)

    height, width, _ = img1.shape

    # Initiate SIFT detector
    orb = cv2.ORB_create() #Needed to be fixed

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    #Note this might only be apropriate for removing translational motion. But will work for now
    matches = sorted(matches, key = lambda x:x.distance)


    """
    Isolating the x,y (long,lat from the image) 
    """

    count=0
    points =matches[:NUMBER_OF_POINTS]

    #Messy essentially getting cordinates
    #Get index
    a=points[count].queryIdx #F0
    b=points[count].trainIdx #F1

    #Get point
    c=kp1[a].pt #query FO
    d=kp2[b].pt  #train F1 

    F0_points=np.asarray(c) #query FO
    F1_points=np.asarray(d) #train F1 

    count+=1

    while count < NUMBER_OF_POINTS:
    
        a=points[count].queryIdx #F0
        b=points[count].trainIdx #F1

        #Get point    
        c=kp1[a].pt #query FO
        d=kp2[b].pt  #train F1 
    
        F0_points=np.column_stack((F0_points,c))
        F1_points=np.column_stack((F1_points,d))
    
        count += 1

    #Sanity Check
    #results should be quite close and the points can be inspected
    F_diff=F1_points-F0_points

 

    """
    Converting the xy, to equivilent cartisian to gain point cloud
    """
    #deal with F0_pionts and F1_pionts seperatly

    y_poi_0 = F0_points[1].astype(int)
    x_poi_0 = F0_points[0].astype(int)

    y_poi_1 = F1_points[1].astype(int)
    x_poi_1 = F1_points[0].astype(int)


    xx_0 = 2*(x_poi_0+0.01) / width - 1.0 #0.01 is to prevent case where 
    yy_0 = 2*(y_poi_0+0.01)/ height - 1.0
    lng_0 = np.pi * xx_0
    lat_0 = - 0.5 * np.pi * yy_0
        
    #phi=lat tetha=lng sph2cart(r,theta,phi)
    x_cart_0,y_cart_0,z_cart_0=sph2cart(1,lat_0,lng_0)
        
    #This snippet of code should be refactored
    xx_1 = 2*(x_poi_1+0.01) / width - 1.0 #0.01 is to prevent case where 0 below the line
    yy_1 = 2*(y_poi_1+0.01)/ height - 1.0
    lng_1 = np.pi * xx_1
    lat_1 = - 0.5 * np.pi * yy_1
        
    #phi=lat tetha=lng sph2cart(r,theta,phi)
    x_cart_1,y_cart_1,z_cart_1=sph2cart(1,lat_1,lng_1)


    """
    #Exporting as an xyz file. 
    #Currently just running twice. Code should be refactored so it works for both quite easily
    """
    xyz_0=np.column_stack((x_cart_0,y_cart_0,z_cart_0))
    xyz_1=np.column_stack((x_cart_1,y_cart_1,z_cart_1))

    return xyz_0,xyz_1     
    