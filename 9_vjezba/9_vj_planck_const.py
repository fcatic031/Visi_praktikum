import pandas as pd
import numpy as np
from scipy.stats import linregress 
from scipy.constants import speed_of_light,elementary_charge,Planck
import matplotlib.pyplot as plt

podaci=pd.read_csv("Praktikum/Visi_Praktikum/9_vj.csv")
valna_duljina=np.array(podaci['valna_duljina']) #u nanometrima izrazeno
U1=np.array(podaci['U1'])
U2=np.array(podaci['U2'])
U3=np.array(podaci['U3'])

#ARITMETICKA SREDINA
U=np.array([(U1[i]+U2[i]+U3[i])/3 for i in range(len(U3))])

#FREKVENCIJA
frekvencija=np.array([speed_of_light/(i*(10**(-9))) for i in valna_duljina])

#MNK
x=np.linspace(min(frekvencija),max(frekvencija),1000)
a,b,r_val,p_val,std_error=linregress(frekvencija,U)
y=a*x+b
print('a={}'.format(a))
print('b={}'.format(b))
print('Formula je y = {:.2e}x + ({:.2f})'.format(a,b))

#određivanje Planckove konstanste
h=a*elementary_charge
print('Naš iznos Planckove konstante je {:.2e}'.format(h))

#Uspredba s pravom Planckovom konstantom
relativna_pogreska=(np.absolute(Planck-h)/h)*100
print('Relativna pogreška iznosi {:.2f}%'.format(relativna_pogreska))
print('Standardna pogreška iznosi {:.2e}'.format(std_error))

#grafički prikaz
plt.grid()
plt.plot(x,y,':',c='red')
plt.ylim(0,max(y)*1.2)
plt.ylabel("U[V]")
plt.xlabel("frekvencija[Hz]")
plt.plot(frekvencija,U,'ob')
plt.show()

