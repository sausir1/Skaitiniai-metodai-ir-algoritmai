import matplotlib.pyplot as plt
import numpy as np
from math import *


def g(x):
  return np.e**-x*np.sin(x**2)+0.001

y = np.arange(5,10,0.001)
##skenavimo su mazejanciu zingsniu algoritmas
iteration = 0
iter_max = 1000
found = False
alpha = 0.01
y0 = 6.5
y1 = y0 + alpha
count = 0

print("Iteracija      Intervalas             g(x) reiksme")

while(iteration <=iter_max and y0 < 7):
# Randam intervala kur saknis
  if(g(y0) >= 0 and g(y1) <= 0 or g(y0) <= 0 and g(y1) >= 0 ):
    found = True
    print("rasta saknis yra intervale ({0:7.6f} ; {1:7.6f})".format(y0,y1))
    step = alpha/10
    s0=y0
    s1=s0+step
    while(iteration < iter_max and abs(g(s0))>=1e-7 and s1<=y1):
      print("{0:3d}      |  {1:7.8f}  -  {2:7.8f} |  {3:.10e}".format(iteration,s0,s1,abs(g(s0))))
      #jeigu keicia zenkla
      if(g(s0) >= 0 and g(s1) <= 0 or g(s0) <= 0 and g(s1) >= 0 ):
        #pranesame, jog radome sakni intervale (s0 ; s1) ir maziname zingsni
        print("patikslinus, saknis yra intervale ({0:7.8f} ; {1:7.8f}) | {2:.10e}".format(s0,s1, abs(g(s0))))
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
  y0=y1
  y1 +=alpha
  print("{0:3d}      |  {1:7.6f}  -  {2:7.6f} |  {3:.10e}".format(iteration,y0,y1,g(y0)))



##
## transcendentinei funkcijai spausidinti

plt.plot(y, g(y))
plt.grid()
plt.show()
##Pabaiga g(x) rodymo

