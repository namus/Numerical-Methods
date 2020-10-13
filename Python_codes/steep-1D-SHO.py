#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:43:00 2019

@author: Suman
"""

import matplotlib.pyplot as plt

def dfx(x):
    k = 2.0
    return -k*x

x = 10.0
a = 0.1
tol = 1.0e-5

listx = [x]

for _ in range(100):
    if abs(dfx(x)) < tol:
        break
    x += a*dfx(x)
    listx.append(x)
    print(x)

plt.plot(listx)
plt.show()



