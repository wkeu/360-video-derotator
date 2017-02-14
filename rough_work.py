
import math
from PIL import Image
import numpy as np

SCALE_FACTOR=2

width=640*SCALE_FACTOR
height=320*SCALE_FACTOR

x=320*SCALE_FACTOR
y=160*SCALE_FACTOR

"""
xx = 2*(x+0.5) / width - 1.0
yy = 2*(y+0.5)/ height - 1.0
lng = math.pi * xx
lat = 0.5 * math.pi * yy
"""
lat = np.linspace(-180, 180, width) * np.pi/180            # Create Long axis
lng = np.linspace(-90, 90, height) * np.pi/180        # Create Lat axis 

#x and y being the point to be moved
Z = np.cos(lat[x]) * np.cos(lng[y])
Y = np.cos(lat[x]) * np.sin(lng[y])
X = -np.sin(lat[x])
D = np.sqrt(X*X+Y*Y+Z*Z)


if D!=1:
    print("Error D should be 1, D="+str(D))

lat = math.atan2(Z, D)
lng = math.atan2(Y, X)

#ix and iy must be integers
ix = int((0.5 * lng / math.pi + 0.5) * width - 0.5)
iy = int((lat/math.pi + 0.5) * height  - 0.5)

#not sure of this part to remap the image
"""
newpixel = pixel[ix, iy]
img2.putpixel([x, y], newpixel)
#I tries as mentionned in the following code to invert x and y in the two previous lines but the index error out of range comes back 
"""
   



#Note cordinates in long and lat, can be converted to pi,-pi easily 

#point of intrest used as an example 
#poi = [lats[4],lons[576]]

# repeat code from one of the examples linked to in the question, except for specifying facecolors:
fig = plt.figure()
ax = fig.gca(projection='3d')

#convert long and lat to x and y

x = np.cos(lats[x_poi]) * np.cos(lons[y_poi])
y = np.cos(lats[x_poi]) * np.sin(lons[y_poi])
z = np.sin(lats[x_poi])
