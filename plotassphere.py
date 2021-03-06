# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:23:13 2021

@author: vnarayana
"""


from numpy import pi, cos, sin, arccos, arange
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib import cm
from matplotlib import animation
import math
from random import randrange
from scipy.stats import truncnorm

def get_truncated_normal(mean=1.7, sd=0.5, low=5, upp=20):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

def checkCollision(a,b,c,d):
    return pow(pow(a-b,2)+pow(c-d,2),0.5)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])
Nos = 4
num_pts = 40000
X = get_truncated_normal(mean=20, sd=2, low=10, upp=30)
radii=X.rvs(Nos*num_pts)
indices = arange(0, num_pts, dtype=float) + 0.5
r = 1
R = 0.01
phi = arccos(1 - 2*indices/num_pts)
theta = pi * (1 + 5**0.5) * indices

x = []
y = []
z = []
X = []
Y = []
Z = []
aggx1 = []
aggx2 = []
aggy1 = []
aggy2 = []
aggz1 = []
aggz2 = []
aggradii1 = []
aggradiix2 = []

for k in range(0,2):
    for i in range(0,2):
        x.append( (r * cos(theta) * sin(phi)) + i*r*2)
        y.append( (r * sin(theta) * sin(phi)))
        z.append( (r*cos(phi))+k*r*2)

        
ax.scatter(x, y, z, s = radii/100, color="b")
ax.set_xlim([-2,3])
ax.set_ylim([-2,3])
ax.set_zlim([-2,3])
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

fig, ax = plt.subplots()
ax.hist(radii/1000, density=True,bins =10)
plt.show()


time = 2
for i in range(0, time):
    print(i)
    for j in range(0,Nos):
        for k in range(0,num_pts):
            
            x[j][k] = x[j][k] + randrange(10)/100
            y[j][k] = y[j][k] - randrange(10)/100
            z[j][k] = z[j][k] + randrange(10)/100
        
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1,1,1])
    ax.scatter(x, y, z,s=radii/100, color="b")
    ax.set_xlim([-2,3])
    ax.set_ylim([-2,3])
    ax.set_zlim([-2,3])
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

def checkCollision(a,b,c,d,e,f):
    return pow(pow(a-b,2)+pow(c-d,2)+pow(e-f,2),0.5)

for k in range(0,Nos):
    print('updating values')
    for i in range(0,num_pts):
        X.append(x[k][i])
        Y.append(y[k][i])
        Z.append(z[k][i])
        
points = [x]
Minimum_distances =[]   
for i in range(0,Nos*num_pts):
    distances = []
    print(i)
    for j in range(0,Nos*num_pts):
        if i>j:
            x1 = X[i]
            x2 = X[j]
            y1 = Y[i]
            y2 = Y[j]
            z1 = Z[i]
            z2 = Z[j]
            #a = checkCollision(x1,x2,y1,y2,z1,z2)
            distances.append(checkCollision(x1,x2,y1,y2,z1,z2))
        else: distances = [0]
        if i>j:
            if checkCollision(x1,x2,y1,y2,z1,z2)< (radii[i] + radii[j])/1000:
                aggx1.append(x1)
                aggx2.append(x2)
                aggy1.append(y1)
                aggy2.append(y2)
                aggz1.append(z1)
                aggz2.append(z2)
                aggradii1.append(radii[i])
                aggradiix2.append(radii[j])
    Minimum_distances.append(min(distances))
    
fig, ax = plt.subplots()          
ax.hist(Minimum_distances*1000, density=True, bins=5)  # density=False would make counts
plt.ylabel('Interlamellar Spacing (2*Lambda)')
plt.xlabel('Data'); 
 
aggradii1=np.true_divide(aggradii1, 10)
aggradiix2=np.true_divide(aggradiix2, 10)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])
ax.scatter(x, y, z,s=radii/100, color="b")
ax.scatter(aggx1, aggy1, aggz1,s=aggradii1, c='r')
ax.scatter(aggx2, aggy2,aggz1,s=aggradiix2,c ='r')
ax.set_xlim([-2,3])
ax.set_ylim([-2,3])
ax.set_zlim([-2,3])
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])  

     
