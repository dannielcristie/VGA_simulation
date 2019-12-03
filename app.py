<<<<<<< HEAD
import numpy as np 

vecU = np.array([1,-2,0])
vecV = np.array([0,2,2])
a = vecU
print(a)
=======
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
>>>>>>> 44e3820a34169dabaa00bc27c484cb10f8472ad8
