# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 16:01:17 2017

@author: temp2015
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
        
        #Generate lonitude and lat value for
        xx = 2*(x+0.5) / width - 1.0
        yy = 2*(y+0.5)/ height - 1.0        
        lng = math.pi * xx
        lat = 0.5 * math.pi * yy

        Z = math.cos(lat) * math.cos(lng)
        Y = math.cos(lat) * math.sin(lng)
        X = -math.sin(lat)
        D = math.sqrt(X*X+Y*Y)
        
        lat2 = math.atan2(Z, D)
        lng2 = math.atan2(Y/X)


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