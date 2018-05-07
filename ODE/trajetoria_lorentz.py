import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(state, t):
	x, y, z = state  # unpack the state vector
	return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # derivatives

state01 = [1.0, 1.0, 1.0]
state02 = [1.001, 1.0, 1.0]
t = np.arange(0.0, 20.0, 0.01)

states1 = odeint(f, state01, t)
states2 = odeint(f, state02, t)

N2 = len(t)

xf1, yf1, zf1 = states1[1999]
xf2, yf2, zf2 = states2[1999]

#print xf1, yf1, zf1

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(states1[:,0], states1[:,1], states1[:,2], '-r', lw = 1)
ax.plot(states2[:,0], states2[:,1], states2[:,2], '-b', lw = 1)
ax.plot([1.0], [1.0], [1.0],'sk', ms = 7)
ax.plot([xf1], [yf1], [zf1], 'or', ms = 7)
ax.plot([xf2], [yf2], [zf2], 'ob', ms = 7)
plt.savefig('trajetoria_lorentz.pdf', dpi = 400)
plt.show()