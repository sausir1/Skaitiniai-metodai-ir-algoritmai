import  matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from scipy.optimize import fsolve

def SplineMatrixLooseEnds(x):
    n = x.size
    d = np.zeros((n - 1))
    for i in range(n - 1):
        d[i] = x[i + 1] - x[i]
    Matrica = np.zeros((n - 2, n-2))
    for i in range(n - 2):
        for j in range(i, i + 1):
            if(i>0):
                Matrica[i][j - 1] = d[i]/6
            Matrica[i][j] = (d[i]+d[i+1])/3
            if(i+1!=n-2):
                Matrica[i][j + 1] = d[i+1]/6
    return Matrica

def SplineYs(y,x):
    n = x.size
    Y = np.zeros(n-2)
    d = np.zeros((n - 1))
    for i in range(n - 1):
        d[i] = x[i + 1] - x[i]
    for i in range(n-2):
        Y[i] = ((y[i+2]-y[i+1])/d[i+1])-((y[i+1]-y[i])/d[i])
    return  Y

f_temps = np.array([4.3428,4.71047,6.44371,9.99282,13.1694,18.0087,18.9351,19.7021,17.2087,13.2821,6.92157,3.88708])
f_month=np.arange(0,12,1)

Ys=SplineYs(f_temps,f_month)
Matrix1=SplineMatrixLooseEnds(f_month)

Derivatives2=np.linalg.solve(Matrix1,Ys)

print("Koeficientai:")
print(Derivatives2)

smoothX = np.arange(0,13,0.1)
#y_interpolation = np.polyval(polynomial,smoothX)

#plt.plot(smoothX,Spline,'g-', linewidth=1, label="Spline")
plt.plot(f_month,f_temps,'ro', label="Interpoliaciniai taškai")

plt.grid()
plt.show()