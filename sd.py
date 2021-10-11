# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 18:49:58 2021

@author: vnarayana
"""

from scipy.stats import truncnorm
import matplotlib.pyplot as plt

def get_truncated_normal(mean=1.7, sd=0.5, low=5, upp=20):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

X = get_truncated_normal(mean=8, sd=2, low=1, upp=10)
a = X.rvs(10)


fig, ax = plt.subplots()
ax.hist(X.rvs(400), density=True,bins =10)
plt.show()