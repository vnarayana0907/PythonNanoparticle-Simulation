# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 17:19:10 2021

@author: vnarayana
"""

import numpy as np 
from matplotlib.patches import Circle 
from matplotlib.collections import PatchCollection 
import matplotlib.pyplot as plt 
from matplotlib import cm 
from matplotlib import animation 
  
  
fig, ax = plt.subplots() 
  
x = []
y = []
Nos = 2
N = 50
r = 50
radii = np.random.uniform(low=5, high=17.3, size=(Nos*N))
for j in range(0,Nos):
    for i in range(0,N):
        theta = 360/N*i
        a =(r * np.cos(theta)) + (100*Nos)
        b = (r * np.sin(theta)) 
        x.append(a)
        y.append(b)
        print(j)
        i = i+1
fig, ax = plt.subplots(1, 1)
ax.scatter(x, y, s=5)
fig.show()

ax.set_xlim([-50,200])
ax.set_ylim([-50,200])