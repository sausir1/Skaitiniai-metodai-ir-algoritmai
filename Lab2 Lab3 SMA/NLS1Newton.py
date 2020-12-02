import  matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from scipy.optimize import fsolve

def x_delta(J,f):

    return np.linalg.solve(J,f)
def ff(X1,X2):
    return np.array([[X1**2+2*((X2-np.cos(X1))**2)-20],[X1**2*X2-2]])

def newFF(X1X2):
    X1,X2 = X1X2
    return [X1**2+2*(X2-np.cos(X1))**2-20,
            X1**2*X2-2]
def J(X1,X2):
    return np.array([[2*X1 - 2*np.sin(2*X1)+4*X2*np.sin(X1),2],[2*X1*X2, X1**2]])

def NewJ(X1X2):
    X1,X2=X1X2
    return [[2*X1 - 2*np.sin(2*X1)+4*X2*np.sin(X1), 2],
            [2*X1*X2,X1**2]]
xne0 = [-1,2]
sol = fsolve(newFF,xne0,fprime=NewJ,full_output=0)

#pradinis artinys x0

iter_max = 2000
iteration = 0
count = 0
alpha = 0.1
#apskaiciuojam
x0 = np.array([[0.6],[3]]).astype(float)
ff_aps = -1 * (ff(x0[0, 0], x0[1, 0]))
while(iteration<iter_max and abs(ff_aps[0,0]) > 1e-13):
    #Apskaiciuojamos jakobiano ir funkcijos reiksmes artinyje
    J_aps = J(x0[0, 0], x0[1, 0])
    ff_aps = -1 * (ff(x0[0, 0], x0[1, 0]))
    print("Funkcija = \n{0}\nJakobianas=\n{1} ".format(ff_aps, J_aps))
    #Tada atliekamas gauso metodas
    deltaX = x_delta(J_aps,ff_aps)
    print("DeltaX = {0}".format(deltaX))
    xi =alpha * deltaX + x0
    print("Iteracija : {0:3d}\n|x0={1}\nxi={2}|\nff_abs[0,0] = {3:.10e}".format(iteration, x0, xi, abs(ff_aps[0,0])))
    x0 = xi
    iteration += 1

print(ff_aps)
print("Atsakymas yra \n{0}".format(x0))

print('solution exercice fsolve:', sol)