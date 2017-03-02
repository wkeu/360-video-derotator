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
    
#Check theta  
#Check the 2 quadrants
#plus and minus theta 45 degrees
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
import math
from PIL import Image

fname="world_map2.png"
f=open("logfile.txt","w")

img = Image.open(fname)
img = img.convert('RGB')
pixel = img.load()
width, height = img.size

img2 = img.copy()
for y in xrange(height):
    for x in xrange(width):
        xx = 2*(x_map+0.5) / width - 1.0
        yy = 2*(y_map+0.5)/ height - 1.0
        lng = math.pi * xx
        lat = - 0.5 * math.pi * yy
        
        #phi=lat tetha=lng
        x_cart,y_cart,z_cart=sph2cart(1,lng,lat)
        
        #Apply roation
        
        r_U, lng_U, lat_U=cart2sph(x_cart,y_cart,z_cart)
        
        #ix and iy must be integers
        #location frame will be moved
        ix = int((0.5 * lng2 / math.pi + 0.5) * width - 0.5)
        iy = int(round((lat2/math.pi + 0.5) * height  - 0.5))

        #not sure of this part to remap the image
        newpixel = pixel[ix, iy]
        img2.putpixel([x, y], newpixel)
        #I tries as mentionned in the following code to invert x and y in the two previous lines but the index error out of range comes back 
        
        if(x%200==0):
            f.write("Finished point x:"+str(x)+ " ix:" +str(ix) +" y:"+str(y) + " iy:" + str(iy)+ "\n")
        
img2.save("02_test_rotated_"+fname)

print("Finished o.O.o")
f.close()


"""