# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:23:04 2016

@author: glenn
"""

import numpy as np

def bilinear2x(arr):
    # Setup
    r_num = arr.shape[0]
    c_num = arr.shape[1]
    a = np.array([[1.0, 1.0, 1.0, 1.0],
                 [0.0, 0.0, 1.0, 1.0],
                 [1.0, 0.0, 1.0, 0.0],
                 [0.0, 0.0, 1.0, 0.0]]).T 
    output = np.zeros((2*r_num-1, 2*c_num-1))
 
    for r in range(r_num-1):
        for c in range(c_num-1):
    
            # Compute the coefficients, using a matrix ax=b
            b = np.array([arr[r+1][c],arr[r][c],arr[r+1][c+1], arr[r][c+1]])
            x = np.linalg.solve(a, b)

            # Interpolate the missing points    
            for j in range(9):
                if(j==0):
                    output[2*r][2*c] = arr[r][c]
                elif(j==2):
                    output[2*r][2*c+2] = arr[r][c+1]
                elif(j==6):
                    output[2*r+2][2*c] = arr[r+1][c]
                elif(j==8):
                    output[2*r+2][2*c+2] = arr[r+1][c+1]
                elif(j==1):
                    output[2*r][2*c+1] = x[0] + x[1]*0.5
                elif(j==3):
                    output[2*r+1][2*c] = x[0] + x[2]*0.5
                elif(j==4):
                    output[2*r+1][2*c+1] = x[0] + x[1]*0.5 + x[2]*0.5 + x[3]*0.25
                elif(j==5):
                    output[2*r+1][2*c+2] = x[0] + x[1]*0.5 + x[2] + x[3]*0.5
                elif(j==7):
                    output[2*r+2][2*c+1] = x[0] + x[1]*0.5 + x[2] + x[3]*0.5       
    return output