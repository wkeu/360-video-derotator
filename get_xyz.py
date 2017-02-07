# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 15:08:06 2017

@author: temp2015
"""
import numpy

a=[-1,-2,-3]
b=numpy.asarray(a,dtype=float,order = 'F')
a=numpy.append(a,[1,2,3])

a.append(4,5,6)

print(a)

a=(403.0, 187.0)
b=(156.0, 217.0)

c = numpy.asarray(a)
d = numpy.asarray(b)

f=numpy.column_stack((c,d))


g=numpy.empty([2,1])
g=numpy.column_stack((g,d))
