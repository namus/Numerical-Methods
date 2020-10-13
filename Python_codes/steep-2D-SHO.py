 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def grad(x,y,kx=1.0, ky=1.0):
    dfx = kx * x
    dfy = ky * y
    return dfx, dfy

def nrg(x,y,kx=1.0,ky=1.0):
    return 0.5*(kx*x**2 + ky*y**2)

# Initialise
x = y = 8.0
kx = 3.0
ky = 1.0
steps = 1000
alpha = 0.1
tol = 1.0e-3

xlist = [x]
ylist = [y]

# Start Steepest Descent
for step in range(steps):
    dfx, dfy = grad(x,y,kx,ky)
    if dfx**2 + dfy**2 < tol:
        print(50*"#")
        print(f'Converged after {step} steps!')
        print(50*"#")
        break
    
    x -= alpha*dfx
    y -= alpha*dfy
    xlist.append(x)
    ylist.append(y)
    print(f'Energy = {nrg(x,y,kx,ky)}')

# Plotting starts here ...

fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.0, 0.0, 1.0, 1.0
ax = fig.add_axes([left, bottom, width, height]) 

start, stop, n_values = -10, 10, 1000

x_vals = np.linspace(start, stop, n_values)
y_vals = np.linspace(start, stop, n_values)
X, Y = np.meshgrid(x_vals, y_vals)

Z = 0.5*(kx*X**2 + ky*Y**2)

cp = plt.contourf(X, Y, Z)
plt.colorbar(cp)

ax.set_title('Steepest descent')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.plot(xlist,ylist,"ro-")
plt.show()