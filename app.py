import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def f(x,y):
    return print(2*x**2+y**2)

u = np.linspace(-2,2,10); v = np.linspace(-2,2,10)

u, v = np.meshgrid(u, v)

x = u; y = v; z = f(x,y)

fig = plt.figure()

ax = plt.axes(projection='3d')

ax.contour3D(x, y, 30)
plt.show()
