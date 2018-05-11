# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 18:30:55 2018

@author: kfgf831
"""

import matplotlib.pyplot as plt
import numpy as np

def step(origin):
    x = origin[0]
    y = origin[1]
    step_x = np.random.uniform(-10,10)
    step_y = np.random.uniform(-10,10)
    #step_x = np.random.vonmises(0,5)
    #step_y = np.random.vonmises(0,5)
    #step_x = np.random.triangular(-5,0,5)
    #step_y = np.random.triangular(-5,0,5)
    new_x = x + step_x
    new_y = y + step_y
    return([new_x,new_y])

def walk(n_steps = 20, start=(0,0)):
    location = start
    path = []
    for x in range(n_steps):
        new_location = step(location)
        path.append(new_location)
        location = new_location
    return(path)

path = np.array(walk(20000))

plt.figure(figsize=(10,10), dpi=300)
plt.axis("off")
plt.scatter(path[:,0],path[:,1],s=1,marker='o',color='black')

plt.savefig("walk.png")

"""
start


"""