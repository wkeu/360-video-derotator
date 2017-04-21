# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:51:58 2017

@author: temp2015
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

import cv2
import numpy as np
from get_xyz import *
from calculate_rmsd import *
from rotate_map import *
import timeit


f_name='goround_screen_grab.png'
img = cv2.imread(f_name,cv2.IMREAD_COLOR)

img=rotate_map(img,y_axis_45())

# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)



# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,None,color=(0,0,255), flags=2)
img2=rotate_map(img2,-y_axis_45())

cv2.imshow("img2",img2)



cv2.imwrite('orb_feature_points_polar_put_back_1.png',img2)
"""
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]
        
        dst = cv2.cornerHarris(image,blockSize,ksize,k)
		
"""