#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:52:04 2019

@author: Suman
"""

import matplotlib.pyplot as plt
import numpy as np

def force(pos):
    f = np.zeros((len(pos),2))
    for i in range(len(pos)-1):
        for j in range(i+1, len(pos)):
            r = np.linalg.norm(pos[i]-pos[j])
            f[i] += (6/r**2)*(2/r**12 - 1/r**6)*(pos[i]-pos[j])
            f[j] -= f[i]
    return f

def potnrg(pos):
    nrg = 0.0
    for i in range(len(pos)-1):
        for j in range(i+1, len(pos)):
            r = np.linalg.norm(pos[i]-pos[j])
            nrg += 1/r**12 - 1/r**6
    return nrg

#Initialise ...
boxl = 3
npart = boxl**2 # Number of particles
steps = 1000
alpha = 0.001
tol = 1.0e-4
nrglist = []
# Initialise coordinates on a square grid with spacing 1.5 units
pos = np.zeros((npart,2))
for i in range(boxl):
    for j in range(boxl):
        pos[3*i+j] = 1.5*np.array([i,j])

oldnrg = potnrg(pos)
nrglist.append(oldnrg)

plt.figure(1,figsize=(18, 6))
plt.subplot(121)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Coordinates')
# Initial coordinates
plt.scatter(pos[:,0],pos[:,1],s=100,c="b") # Before

#Steepest descent starts
for step in range(steps):
    pos += alpha*force(pos)
    newnrg = potnrg(pos)
    nrglist.append(newnrg)
    print("Energy = ", newnrg)
    if abs(newnrg-oldnrg) < tol:
        print(f"Converged after {step} steps!")
        break
    oldnrg = newnrg
    
# Final coordinates
plt.scatter(pos[:,0],pos[:,1],s=100,c="r") # After

plt.subplot(122)
plt.xlabel('Steps')
plt.ylabel('Energy')
plt.title('Energy convergence')
plt.plot(nrglist)
plt.show()

