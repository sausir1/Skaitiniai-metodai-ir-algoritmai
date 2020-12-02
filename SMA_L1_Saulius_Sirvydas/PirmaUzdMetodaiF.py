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

##skenavimo su mazejanciu zingsniu algoritmas
iteration = 0
iter_max = 1000
found = False
alpha = 0.01
x0 = 1
x1 = x0 + alpha
count = 0

print("Iteracija      Intervalas             F(x) reiksme")

while(iteration <=iter_max and x0< 2):
# Randam intervala kur saknis
  if(f(x0) >= 0 and f(x1) <= 0 or f(x0) <= 0 and f(x1) >= 0 ):
    found = True
    print("rasta saknis yra intervale ({0:7.6f} ; {1:7.6f})".format(x0,x1))
    step = alpha/10
    s0=x0
    s1=s0+step
    while(iteration < iter_max and abs(f(s0))>=1e-7 and s1<=x1):
      print("{0:3d}      |  {1:7.8f}  -  {2:7.8f} |  {3:.10e}".format(iteration,s0,s1,abs(f(s0))))
      #jeigu keicia zenkla
      if(f(s0) >= 0 and f(s1) <= 0 or f(s0) <= 0 and f(s1) >= 0 ):
        #pranesame, jog radome sakni intervale (s0 ; s1) ir maziname zingsni
        print("patikslinus, saknis yra intervale ({0:7.8f} ; {1:7.8f}) | {2:.10e}".format(s0,s1, abs(f(s0))))
        #s0 nesikeicia, o s1 patoliname nuo s0 per sumazinta zingsni
        step= step/10
        s1=s0+step
      #Jei ne, tikriname kita intervala
      else:
        s0+=step
        s1+=step
      #Skaiciuojam kaip dar viena iteracija
      iteration+=1

  iteration +=1
  x0=x1
  x1 +=alpha
  print("{0:3d}      |  {1:7.6f}  -  {2:7.6f} |  {3:.10e}".format(iteration,x0,x1,f(x0)))


plt.plot(x,f(x))
plt.grid()
axes = plt.gca()
axes.set_ylim([-10, 10])

plt.show()
