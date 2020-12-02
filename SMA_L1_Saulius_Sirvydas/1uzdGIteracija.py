import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.optimize import fsolve

def g(x):
  return np.e**-x*np.sin(x**2)+0.001

x = np.arange(5, 10, 0.001)

iteration =0
iter_max = 1000
#paprastoji iteracija. metodas
#parenkame alpha koeficienta
alpha =-0.1
#pradinys artinys x0
x0= 6.5


while(abs(g(x0)) > 1e-9 and iteration <= iter_max):
    kitas_x = x0+(1/alpha)*g(x0)
    print("{0:3d}      |  {1:7.9f}  -  {2:7.9f} |  {3:.10e}".format(iteration,x0,kitas_x,abs(g(x0))))
    iteration+=1
    x0=kitas_x

plt.plot(x,g(x))
axes = plt.gca()
axes.set_ylim([-10, 10])
plt.grid()
#plt.show()