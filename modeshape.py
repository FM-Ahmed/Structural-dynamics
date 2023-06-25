import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# beam parameters
L = 100 # Length
E = 2.1e11 # Elastic modulus
nu = 0.3 # Poissons number
srho = 7850 # Density of steel

B = L/100 # width
H = L/100 # height
Ix = B*H**3/12 # inertia x-dir
Iy = B*H**3/12 # inertia y-dir
I = Iy
y = np.linspace(0, 100, 101) # array along beam
V = B*H*L # volume of beam
m = srho*V/L # mass of beam

def func(x):
    return (1 + np.cosh(x)*np.cos(x))

Nmodes = 4 # how many modeshapes you want to solve for
beta = []
i = 1
while (i <= 101 and len(beta) < Nmodes):
    ans = round(float(fsolve(func, [i])), 4)
    beta.append(ans)
    beta = list(dict.fromkeys(beta))
    i += 1

# plotting the modeshapes
ii = 0
while (ii < Nmodes):
    phi = (np.cosh(beta[ii]*y/L)-np.cos(beta[ii]*y/L))+((np.cosh(beta[ii])+np.cos(beta[ii]))*(np.sin(beta[ii]*y/L)-np.sinh(beta[ii]*y/L)))/(np.sin(beta[ii])+np.sinh(beta[ii]))
    phi = phi/np.max(np.abs(phi))
    plt.figure(figsize = [10, 2])
    plt.plot(y, phi, label = ii+1, color = 'k')
    plt.grid(True, 'both')
    plt.legend(loc = 'best')
    plt.xlabel('L')
    plt.ylabel('$\phi$')
    ii += 1
