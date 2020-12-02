import matplotlib.pyplot as plt
import numpy as np
from math import *


def g(x):
  return np.e**-x*np.sin(x**2)+0.001

y = np.arange(5,10,0.001)
iteration = 0
iter_max = 1000

##skenavimo algoritmas
alpha = 0.1
x0 = 5
x1 = x0 + alpha
count = 0

print("Iteracija      Intervalas             g(x) reiksme")

while(iteration <=iter_max and x0< 10):

  if(g(x0) >= 0 and g(x1) <= 0):
    print("rasta saknis yra intervale ({0:7.6f} ; {1:7.6f})".format(x0,x1))
    count += 1
  if(g(x0) <= 0 and g(x1) >= 0):
    print("rasta saknis yra intervale ({0:7.6f} ; {1:7.6f})".format(x0,x1))
    count +=1

  x0=x1
  x1 += alpha
  iteration += 1
  print("{0:3d}      |  {1:7.6f}  ;  {2:7.6f} |  {3:.10e}".format(iteration,x0,x1,g(x0)))

print("rastas saknu skaicius yra {0}".format(count))


##
## transcendentinei funkcijai spausidinti

plt.plot(y, g(y))
plt.grid()
plt.show()
##Pabaiga g(x) rodymo

