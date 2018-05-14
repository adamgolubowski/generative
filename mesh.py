# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 19:32:02 2018

@author: AG
"""

import numpy as np
import matplotlib.pyplot as plt

space = range(50)

ma = []
for x in space:
    for y in space:
        x1 = x + np.random.uniform(-0.1,0.1)
        y1 = y + np.random.uniform(-0.1,0.1)
        ma.append([x1,y1])  

field = np.array(ma)

plt.figure(figsize=(5,5),dpi=200)
plt.axis("off")
plt.scatter(field[:,0],field[:,1],s=1,marker='o',color='black')
plt.savefig('distorted_mesh.png')
