import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.optimize import fsolve

def f(x):
  return 0.48*x**5+1.71*x**4-0.67*x**3-4.86*x**2-1.33*x+1.50

def df(x):
  return 2.4*x**4+6.84*x**3-2.01*x**2-9.72*x-1.33

r_grubus = 11.125
r_teig = 1 + sqrt(4.86/0.48)
r_neig = -(1 + 1.71/0.48)
x = np.arange(r_neig, r_teig, 0.001)

iteration =0
iter_max = 1000
#paprastoji iteracija. metodas
#parenkame alpha koeficienta
alpha =-18
#pradinys artinys x0
x0= 0.5

while(abs(f(x0)) > 1e-9 and iteration <= iter_max):
    kitas_x = x0+(1/alpha)*f(x0)
    print("{0:3d}      |  {1:7.9f}  -  {2:7.9f} |  {3:.10e}".format(iteration,x0,kitas_x,abs(f(x0))))
    iteration+=1
    x0=kitas_x

plt.plot(x,f(x))
axes = plt.gca()
axes.set_ylim([-10, 10])
plt.grid()
#plt.show()