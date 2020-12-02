import  matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from scipy.optimize import fsolve

def g(x, n):
    return np.array([x ** i for i in range(n)]).T.astype(np.float)

y = np.array([4.3428,4.71047,6.44371,9.99282,13.1694,18.0087,18.9351,19.7021,17.2087,13.2821,6.92157,3.88708])
x = np.arange(1,13,1)

def f(x, coefficients):
    result = 0
    polynomial = ""
    for i in range(len(coefficients)):
        result += coefficients[i] * x ** i
        polynomial += "{0:1.5} * x^{1} +".format(coefficients[i], i)

    print(polynomial)
    return result

n=3

G = g(x,n)
print(G)
coefficients = np.linalg.solve(G.T.dot(G), G.T.dot(y))
xx = np.arange(0, 13, 0.1)
plt.plot(x, y, 'ro', label=f'taskai\nn={len(x)}')
plt.plot(xx, f(xx, coefficients), 'b-', label=f'approximation\nn={n-1}')
plt.grid()
plt.legend()
plt.show()