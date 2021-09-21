import numpy as np
from matplotlib import pyplot as plt

A = np.zeros((2,2))
A[0,0], A[0,1] = 1, 2
A[1,0], A[1,1] = 2, 4

f = lambda x: np.sum(x * (A @ x), axis=0)/np.linalg.norm(x,axis=0)**2

N = 1000 # An even number is important to avoid meshing (0,0) as a point.
grid = np.linspace(-3,3,N)

x, y = np.meshgrid(grid, grid)
X = np.vstack((x.flatten(), y.flatten()))
fX = np.reshape(f(X), (N,N))


fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')

surf = ax.plot_surface(x, y, fX, cmap='coolwarm', edgecolor='none')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f_A(x)$')

ax = fig.add_subplot(1, 2, 2)
contour = plt.contour(x, y, fX, levels=30, cmap='coolwarm')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
fig.colorbar(surf, shrink=0.5, aspect=10)

plt.show()
