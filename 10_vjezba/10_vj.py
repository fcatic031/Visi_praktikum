import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

#FRANCK-HERTZOV POKUS S Ne-CIJEVI

podaci=pd.read_csv("Praktikum/Visi_Praktikum/10_vjezba.csv")
U=podaci['U1/V']
I=podaci['IA/nA']

def model(x,a,b,c):
    return a*(x-b)**2+c
popt,pcov=curve_fit(model,U,I,p0=[3,2,-16])
x_model=np.linspace(min(U),max(U),len(U))
y_model=model(x_model,popt[0],popt[1],popt[2])

"""x_interaction=[]
y_interaction=[]
indexovi=[]

for i in range(len(U)):
    if (I[i]==round(y_model[i],2) and U[i]==round(x_model[i],2)):
        x_interaction.append(U[i])
        y_interaction.append(I[i])
        indexovi.append(i)
"""

idx = np.argwhere(np.diff(np.sign(I - y_model))).flatten()

lista=[]
lista2=[]
peaks_x=[]
peaks_y=[]
x=0
for i in range(len(I)):
    lista.append(I[i])
    lista2.append(I[i])
    if i in idx:
        x+=1
        if x%2==0:
            peaks_y.append(max(lista))
        else:
            peaks_y.append(min(lista))
        lista=[]

print(peaks_y)

plt.plot(U,y_model,c='r')
plt.plot(U[idx], I[idx], 'ob')            
plt.plot(U,I)
plt.ylabel("I/nA")
plt.xlabel("U/V")
plt.show()