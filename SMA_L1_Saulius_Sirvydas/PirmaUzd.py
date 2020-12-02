import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.optimize import fsolve

def f(x):
  return 0.48*x**5+1.71*x**4-0.67*x**3-4.86*x**2-1.33*x+1.50

#Daugianario isvestine
def df(x):
  return 2.4*x**4+6.84*x**3-2.01*x**2-9.72*x-1.33

r_grubus = 11.125
r_teig = 1 + sqrt(4.86/0.48)
r_neig = -(1 + 1.71/0.48)
x = np.arange(r_neig, r_teig, 0.001)




iteration = 0
iter_max = 1000

plt.plot(-11.125,0,'ro',label='Grubus ivertis')
plt.plot(11.125,0,'ro')
plt.plot(r_neig,0,'gs')
plt.plot(r_teig,0,'gs',label='Tikslesnis ivertis')


##skenavimo algoritmas

alpha = 0.1
x0 = r_neig
x1 = x0 + alpha
count = 0

print("Iteracija        Intervalas             F(x) reiksme")

while(iteration <=iter_max and x0< r_teig):

  if(f(x0) >= 0 and f(x1) <= 0):
    print("rasta saknis yra intervale ({0:7.6f} ; {1:7.6f})".format(x0,x1))
    count += 1
  if(f(x0) <= 0 and f(x1) >= 0)

    print("rasta saknis yra intervale ({0:7.6f} ; {1:7.6f})".format(x0,x1))
    count +=1

  x0=x1
  x1 += alpha
  iteration += 1
  print("{0:3d}      |  {1:7.6f}  ;  {2:7.6f} |  {3:.10e}".format(iteration,x0,x1,f(x0)))

print("rastas saknu skaicius yra {0}".format(count))

plt.plot(x,f(x))
plt.grid()
axes = plt.gca()
axes.set_ylim([-10, 10])
plt.legend()
plt.show()
