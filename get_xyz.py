# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 15:08:06 2017

@author: temp2015
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
from formula import *

NUMBER_OF_POINTS=40 #Tested number which give good results

fname1='world_map2.png'
fname2='world_map2.png'

#Read in the frames
img1 = cv2.imread(fname1,0) # Frame0 (query image)
img2 = cv2.imread(fname2,0) # Frame1 (train image)

height, width = img1.shape

# Initiate SIFT detector
orb = cv2.ORB_create() #Needed to be fixed

# find the keypoints and descriptors with SIFT

kp1, des1 = orb.detectAndCompute(img1,None)

kp2, des2 = orb.detectAndCompute(img2,None)

"""

Next we create a BFMatcher object with distance measurement cv2.NORM_HAMMING 
(since we are using ORB) and crossCheck is switched on for better results. 
Then we use Matcher.match() method to get the best matches in two images. 
We sort them in ascending order of their distances so that best matches 
(with low distance) come to front. Then we draw only first 10 matches (Just for 
sake of visibility. You can increase it as you like)

"""

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
#Note this might only be apropriate for removing translational motion. But will work for now
matches = sorted(matches, key = lambda x:x.distance)

"""
Sanity Check
# Draw first 10 matches.
"""
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:2],None, flags=2)

#cv2.imshow("Matched Image",img3)

cv2.imwrite("Matched"+fname2,img3)


"""
Isolating the x,y (long,lat from the image) 
"""

count=0

points =matches[:NUMBER_OF_POINTS]

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

#resukt should be quite close and the points can be inspected
F_diff=F1_points-F0_points

#Possible sanity check would be to plot these points on top of both images to enure they allign

"""
Converting the xy, to equivilent cartisian to gain point cloud
"""
#deal with F0_pionts and F1_pionts seperatly

y_poi_0 = F0_points[1].astype(int)
x_poi_0 = F0_points[0].astype(int)

y_poi_1 = F1_points[1].astype(int)
x_poi_1 = F1_points[0].astype(int)


# coordinates of the image - don't know if this is entirely accurate, but probably close
lats = np.linspace(-180, 180, img1.shape[1]) * np.pi/180            # Create Long axis
lons = np.linspace(-90, 90, img1.shape[0])[::-1] * np.pi/180        # Create Lat axis 


#Note cordinates in long and lat, can be converted to pi,-pi easily 

#point of intrest used as an example 
#poi = [lats[4],lons[576]]

"""

# repeat code from one of the examples linked to in the question, except for specifying facecolors:
fig = plt.figure()
ax = fig.gca(projection='3d')

#convert long and lat to x and y
"""
#cart2sph(x,y,z):

#sph2cart(r,theta,phi):

x_0 = np.cos(lats[x_poi_0]) * np.cos(lons[y_poi_0])
y_0 = np.cos(lats[x_poi_0]) * np.sin(lons[y_poi_0])
z_0 = np.sin(lats[x_poi_0])

x_1 = np.cos(lats[x_poi_1]) * np.cos(lons[y_poi_1])
y_1 = np.cos(lats[x_poi_1]) * np.sin(lons[y_poi_1])
z_1 = np.sin(lats[x_poi_1])


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

#Plot the point(s)
#ax.scatter(x, y, z, c='g',marker='o')

#Set axes range 
#ax.set_xlim3d(-1, 1)
#ax.set_ylim3d(-1, 1)
#ax.set_zlim3d(-1, 1)

plt.show()
"""

#Exporting as an xyz file. 
#Currently just running twice. Code should be refactored so it works for both quite easily
"""
xyz_0=np.column_stack((x_cart_0,y_cart_0,z_cart_0))
xyz_1=np.column_stack((x_cart_1,y_cart_1,z_cart_1))
np.savetxt('frame_0.xyz', xyz_0)
np.savetxt('frame_1.xyz', xyz_1)

print("Point Clouds Retrieved")