import  matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

X = np.arange(-5,5,0.1)
Y = np.arange(-5,5,0.1)

XX, YY = np.meshgrid(X,Y)

Z1 = XX**2+2*(YY-np.cos(XX))**2-20 #pirma lygtis
Z2 = XX**2*YY-2 #antra lygtis

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(XX,YY,Z1,cmap=cm.viridis,alpha =0.7)
surfZ = ax.plot_surface(XX,YY,np.zeros(np.shape(Z1)),antialiased=False, alpha = 0.2)
cp = ax.contour(X,Y,Z1,levels = 0,colors = 'red')
plt.show() #Pirmos lygties grafike pavaizdavimas

fig2 = plt.figure()
ax = fig2.gca(projection = '3d')
surf = ax.plot_surface(XX,YY,Z2, cmap=cm.inferno,
                       antialiased=False,alpha=0.7)
surfZ = ax.plot_surface(XX,YY,np.zeros(np.shape(Z1)),antialiased=False,alpha=0.2)
cp=ax.contour(X,Y,Z2,levels=0,colors = 'blue')

plt.show(); #atvaizduojama antra lygtis grafiskai

fig3=plt.figure()
ax= fig3.gca()
ax.grid(color='#fcba03', linestyle='-',linewidth=0.5)
cp = ax.contour(X,Y,Z1,levels=0,colors='red')
cp = ax.contour(X,Y,Z2,levels=0,colors='blue')
plt.show()