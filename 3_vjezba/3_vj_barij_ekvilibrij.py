import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

#podaci dobiveni mjerenjem zračenja barija
ekvilibrij=[1087,1033,614,662,762,832,862,893,942,992,982,948]
t=[i for i in range(60,780,60)]

#polinomna interpolacija
x1=np.linspace(t[0],t[-1],1000)
f=interp1d(t,ekvilibrij,kind='cubic')
y1=f(x1)

#grafički prikaz
plt.grid()
plt.plot(x1,y1)
plt.xlabel("Vrijeme/s")
plt.ylabel("Impulsi u 60s")
plt.plot(t,ekvilibrij,'ob')
plt.plot([150]*2,[0,1200],':')
plt.show()