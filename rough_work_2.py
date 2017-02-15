import math
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx

width=640
height=320
theta=(np.pi/4)

Ux=np.matrix([ [1, 0, 0] , [0, np.cos(theta), -np.sin(theta)] , [0, np.sin(theta), np.cos(theta)] ])
Uy=np.matrix([ [np.cos(theta), 0, np.sin(theta)] , [0, 1, 0] , [-np.sin(theta), 0, np.cos(theta)] ])
Uz=np.matrix([ [np.cos(theta), -np.sin(theta), 0] , [np.sin(theta), np.cos(theta), 0] , [ 0, 0, 1] ])

U=Ux

lat = np.linspace(-180, 180, width) * np.pi/180            # Create Long axis
lng = np.linspace(-90, 90, height) * np.pi/180        # Create Lat axis 

#Loop for image will start here

#point on cordinate map x,y
pixel_pt=160,160

pt_lng=lng[pixel_pt[1]]
pt_lat=lat[pixel_pt[0]]

#Convert to long and lat to cart 
x = np.cos(pt_lat) * np.cos(pt_lng)
y = np.cos(pt_lat) * np.sin(pt_lng)
z = np.sin(pt_lat)

#Rotate 
pt_cart=np.matrix([ [x] , [y], [z] ])

pt_cart_rotated=np.matmul(U, pt_cart)

r_x = pt_cart_rotated[0]
r_y = pt_cart_rotated[1]
r_z = pt_cart_rotated[2]

#Convert back to long and lat
pt_lat_rotated=np.arcsin(r_z)
print("Latitude:\nRotated point:"+str(pt_lat_rotated)+"\nOrginal Point:"+str(pt_lat))

## Problem with this formula
pt_lng_rotated=np.arctan(r_y,r_x)
print("Longitude:\nRotated point:"+str(pt_lng_rotated)+"\nOrginal Point:"+str(pt_lng))

#Convert back to location on image
pixel_pt_rotated=(find_nearest(lat, pt_lat_rotated), find_nearest(lng, pt_lng_rotated))

print("Original Pixel Position"+str(pixel_pt))
print("Rotated Pixel Position"+str(pixel_pt_rotated))


"""
Plotting Map
"""

ax=plt.figure()
before=plt.plot(int(pixel_pt[0]), int(pixel_pt[1]),marker='o', markerfacecolor="red")
after=plt.plot(int(pixel_pt_rotated[0]), int(pixel_pt_rotated[1]),marker='o', markerfacecolor="green")

plt.xlim([0,640])
plt.ylim([0,320])
plt.show()
#plt.legend([before, after], ['before', 'after'])
plt.grid()