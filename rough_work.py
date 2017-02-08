
width=640
height=320

xx = 2*(x+0.5) / width - 1.0
yy = 2*(y+0.5)/ height - 1.0
lng = math.pi * xx
lat = 0.5 * math.pi * yy

Z = math.cos(lat) * math.cos(lng)
Y = math.cos(lat) * math.sin(lng)
X = -math.sin(lat)
D = math.sqrt(X*X+Y*Y)

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
   