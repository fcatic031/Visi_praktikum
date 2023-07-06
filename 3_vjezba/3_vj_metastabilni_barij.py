import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from scipy.interpolate import interp1d

#rezultati mjerenja zračenja metastabilnog barija ovisno o vremenu
t=[0,60,120,180,240,300,360]
meta_barij=[3594,2619,2030,1543,1173,883,638]

#interpolacija
x1=np.linspace(t[0],t[-1],1000)
f=interp1d(t,meta_barij,kind="cubic")
y1=f(x1)

#Odredjivanje poluraspada metastabilnog barija
for i in range(len(x1)):
    if round(y1[i],0)==(meta_barij[0]/2):
        poluraspad=round(x1[i],2)

pravi_poluraspad=156
relativna_pogreska=np.absolute(pravi_poluraspad-poluraspad)/pravi_poluraspad

print("Relativna pogreska iznosi ",relativna_pogreska)

plt.grid()
plt.plot(x1,y1)
plt.xlabel("Vrijeme/s")
plt.ylabel("Impulsi u 60 s")
plt.plot(t,meta_barij,'ob')
plt.show()