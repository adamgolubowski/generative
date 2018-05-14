# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 13:50:47 2018

@author: AG
"""

import matplotlib.pyplot as plt
import numpy as np
import math

# generate a rectangular matrix of random numbers
n = 2000
x = np.random.rand(n)
y = np.random.rand(n)
ma = list(zip(x,y))

# make a copy of the matrix and rotate it around the centre of the plot
def rotate(ma,th,centre=(0,0)): 
    x = ma[0] - centre[0]
    y = ma[1] - centre[1]
    theta = np.radians(th)
    cos_th = math.cos(theta)
    sin_th = math.sin(theta)
    x1 = (x * cos_th - y * sin_th)
    y1 = (x * sin_th + y * cos_th)
    x1 = x1 + centre[0]
    y1 = y1 + centre[1]
    return([x1,y1])

ma_centre = (np.mean(x),np.mean(y))
ma_rotated = [rotate(r,3,ma_centre) for r in ma]
ma_rotated_np = np.array(ma_rotated)
x_rotated = ma_rotated_np[:,0]
y_rotated = ma_rotated_np[:,1]

plt.figure(figsize=(5,5),dpi=200)
plt.axis("off")

plt.scatter(x,y,s=1,marker='o',c='black')
plt.scatter(x_rotated,y_rotated,s=1,marker='o', color = 'black')

plt.savefig('moire_pattern.png')
plt.show()

