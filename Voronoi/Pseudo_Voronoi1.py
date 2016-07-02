# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:08:18 2016

@author: glenn
"""

import numpy as np
from random import uniform
from math import log10

def linf(input):
    return max(input.real, input.imag)

def l1(input):
    return abs(input.real) + abs(input.imag)

def rand_pts(n):
    return [complex(uniform(Xmin,Xmax), uniform(Ymin,Ymax)) for n in range(npt)]

# Bounds, initial defaults
Xmin = -2.5
Xmax = 1.5
Ymin = -2
Ymax = 2
gridSpc = 0.5
maxRad = 3.0
npt = 25
points = []
radius = 2.0

# Calculate the separate coordinates of the pixels to output
xCoords = np.arange(Xmin, Xmax, gridSpc)
yCoords = np.arange(Ymin, Ymax, gridSpc)

# Create an array to output the data to
arr = np.zeros(( len(xCoords), len(yCoords) ))

# Create random points for centers
points = rand_pts(npt)

#For all grid points
for y in yCoords:
    yindex = int((Ymax - y) / gridSpc )
    for x in xCoords:
        xindex = int((Xmax - x) / gridSpc )
        z = complex(x,y)
        arr[yindex-1][xindex-1] = min([l1(z-pt) for pt in points])
