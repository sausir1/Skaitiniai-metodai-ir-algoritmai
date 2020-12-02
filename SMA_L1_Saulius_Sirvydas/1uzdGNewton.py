import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.optimize import fsolve

def g(x):
  return np.e**-x*np.sin(x**2)+0.001

def dg(x):
  return np.e**-x*(2*x*np.cos(x**2)-np.sin(x**2))


y = np.arange(5,10,0.001)



iteration = 0
iter_max = 1000

##Niutono algoritmas
#x0 - pradinis artinys
x0 = 7
count = 0
print("Iteracija      Intervalas             F(x) reiksme")
while(abs(g(x0)) >= 1e-11 and iteration <= iter_max):
    xi = x0 - g(x0)/dg(x0)
    print("{0:3d}      |  {1:7.9f}  -  {2:7.9f} |  {3:.10e}".format(iteration, x0, xi, abs(g(x0))))
    x0 = xi
    iteration+=1

plt.plot(y,g(y))
plt.grid()
plt.show()