import  matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from scipy.optimize import fsolve

def fff(x1,x2,x3,x4):

    return np.array([[x2-x3+x4-1],[5*x1+4*x3*x4+26],[5*x2**3-x3**2+634],[4*x1-3*x2+2*x3-17]]).astype(float)
def new_fff(x1x2x3x4):
    x1,x2,x3,x4 = x1x2x3x4
    return  [x2-x3+x4-1,5*x1+4*x3*x4+26,5*x2**3-x3**2+634,4*x1-3*x2+2*x3-17]

def new_J(x1x2x3x4):
    x1, x2, x3, x4 = x1x2x3x4
    return [ [0,1,-1,1],
             [5,0,4*x4,4*x3],
             [0,15*x2**2,-2*x3,0],
             [4,-3,2,0]]

def J(x1,x2,x3,x4):

    return np.array([[0,1,-1,1],
                     [5,0,4*x4,4*x3],
                     [0,15*x2**2,-2*x3,0],
                     [4,-3,2,0]]).astype(float)

def x_delta(J,f):

    return np.linalg.solve(J,f)

xne0 = [-5,-5,-5,-5]
sol = fsolve(new_fff,xne0,fprime=new_J,full_output=0)

#pradinis artinys x0
iter_max = 1000
iteration = 0
#apskaiciuojam
x0 = np.array([[-5],[-5],[-5],[-5]]).astype(float)
ff_aps = -1 * (fff(x0[0, 0], x0[1, 0],x0[2, 0],x0[3, 0]))
while(iteration<iter_max and abs(ff_aps[2,0]) >= 1e-16):
    #Apskaiciuojamos jakobiano ir funkcijos reiksmes artinyje
    J_aps = J(x0[0, 0], x0[1, 0],x0[2, 0],x0[3, 0])
    ff_aps = -1 * (fff(x0[0, 0], x0[1, 0],x0[2, 0],x0[3, 0]))
    print("Funkcija = \n{0}\nJakobianas=\n{1} ".format(ff_aps, J_aps))
    #Tada atliekamas gauso metodas
    deltaX = x_delta(J_aps,ff_aps)
    print("DeltaX = {0}".format(deltaX))
    #sekantis artinys xi
    xi = deltaX + x0
    print("Iteracija : {0:3d}\n|x0={1}\nxi={2}|\nff_aps[0,0] = {3:.10e}".format(iteration, x0, xi, abs(ff_aps[0,0])))
    x0 = xi
    iteration += 1

print("Atsakymas yra \n{0}".format(x0))
print(ff_aps)

print('solution exercice fsolve:', sol)