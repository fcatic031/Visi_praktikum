import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import speed_of_light
from scipy.optimize import curve_fit

#FRANCK-HERTZOV POKUS S Ne-CIJEVI
#Preuzimanje podataka izvedenog pokusa
podaci=pd.read_csv("Praktikum/Visi_Praktikum/10_vjezba.csv")
U=podaci['U1/V']
I=podaci['IA/nA']

#Stvaranje krivulje koja aproksimira vrijednostima U-I
def model(x,a,b,c):
    return a*(x-b)**2+c
popt,pcov=curve_fit(model,U,I,p0=[3,2,-16])
x_model=np.linspace(min(U),max(U),len(U))
y_model=model(x_model,popt[0],popt[1],popt[2])

#Točke u kojima se dvije krivulje sijeku
idx = np.argwhere(np.diff(np.sign(I - y_model))).flatten()

#Određivanje peakova krivulje
lista=[]
lista2=[]
peaks_x=[]
peaks_y=[]
x=0
for i in range(len(I)):
    lista.append(I[i])
    lista2.append(U[i])
    if i in idx:
        x+=1
        if x%2==0:
            peaks_y.append(max(lista))
            index_mx=lista.index(max(lista))
            peaks_x.append(lista2[index_mx])
        else:
            peaks_y.append(min(lista))
            index_mn=lista.index(min(lista))
            peaks_x.append(lista2[index_mn])
        lista=[]
        lista2=[]

#rezultati dobiveni pomoću Measure sofvera
peaks_measure_x=[0,15.33,21.95,32.08,38.68,49.13,56.09,68.18,74.67,88.08,93.25]
peaks_measure_y=[0,1.09,0.02,2.21,0.05,3.48,0.97,5.73,3.66,10.82,10.18]

print("Usporedba peakova dobivenih preko Pythona i Measure-a:")
for i in range (len(peaks_y)):
    if i%2==0:
        print('Minimum: ({} , {}) , ({} , {}) '
              .format(peaks_x[i],peaks_y[i],peaks_measure_x[i],peaks_measure_y[i]))
    else:
        print('Maximum: ({} , {}) , ({} , {}) '
              .format(peaks_x[i],peaks_y[i],peaks_measure_x[i],peaks_measure_y[i]))


#plt.plot(peaks_measure_x,peaks_measure_y,'og')
plt.plot(peaks_x,peaks_y,'or')
plt.plot(U,y_model,c='r')
plt.plot(U[idx], I[idx], 'ob')            
plt.plot(U,I)
plt.ylabel("I/nA")
plt.xlabel("U/V")
plt.title('Franck-Hertzov pokus s Ne-cijevi')
plt.show()