import math
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

width=640
height=320
theta=np.pi/2

U=np.matrix([ [np.cos(theta), 0, np.sin(theta)] , [0, 1, 0] , [-np.sin(theta), 0, np.cos(theta)] ])

#point on cordinate map x,y
pt=320,160

lat = np.linspace(-180, 180, width) * np.pi/180            # Create Long axis
lng = np.linspace(-90, 90, height) * np.pi/180        # Create Lat axis 

pt_lng=lng[pt[1]]
pt_lat=lat[pt[0]]

#xConvert to cart. 
Z = np.cos(pt_lat) * np.cos(pt_lng)
Y = np.cos(pt_lat) * np.sin(pt_lng)
X = -np.sin(pt_lat)
D = np.sqrt(X*X+Y*Y)

#Rotate 

#Convert back to long and lat
theta=np.arctan2(Z,X)
phi=np.arctan2(D,Z)
