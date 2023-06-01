import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

#uzimanje podataka koje smo dobili na pokusu
podaci_auerove_mrezice=pd.read_csv("Praktikum/Visi_Praktikum/auerova_mrezica.csv")
mjerenja=[1,2,3,4,5]

#Prosječna vrijednost zračenja kad stavimo određeni materijal/medij između detektora i aureove mrežice
prosjecna_zrak=np.mean(podaci_auerove_mrezice["impulsi(zrak)/60s"])
prosjecna_papir=np.mean(podaci_auerove_mrezice["impulsi(papir)/60s"])
prosjecna_aluminij=np.mean(podaci_auerove_mrezice["impulsi(aluminij)/60s"])
prosjecna_olovo=np.mean(podaci_auerove_mrezice["impulsi(olovo)/60s"])

#lista prosječnih vrijednosti
prosjecne_vrijednosti=[prosjecna_zrak,prosjecna_papir,prosjecna_aluminij,prosjecna_olovo]
popis_materijala=['zrak','papir','aluminij','olovo']

fig,(ax,bx)=plt.subplots(1,2)

ax.grid()
ax.plot(mjerenja,podaci_auerove_mrezice["impulsi(zrak)/60s"],label='zrak')
ax.plot(mjerenja,podaci_auerove_mrezice["impulsi(zrak)/60s"],'ob')
ax.plot( mjerenja,[prosjecna_zrak]*5 ,':')

ax.plot(mjerenja,podaci_auerove_mrezice["impulsi(papir)/60s"],label='s papirom ')
ax.plot(mjerenja,podaci_auerove_mrezice["impulsi(papir)/60s"],'ob')
ax.plot( mjerenja,[prosjecna_papir]*5 ,':',c='blue')

ax.plot(mjerenja,podaci_auerove_mrezice["impulsi(aluminij)/60s"],label='aluminij')
ax.plot(mjerenja,podaci_auerove_mrezice["impulsi(aluminij)/60s"],'ob')
ax.plot( mjerenja,[prosjecna_aluminij]*5 ,':')

ax.plot(mjerenja,podaci_auerove_mrezice["impulsi(olovo)/60s"],label='olovo')
ax.plot(mjerenja,podaci_auerove_mrezice["impulsi(olovo)/60s"],'ob')
ax.plot(mjerenja, [prosjecna_olovo]*5 ,':')

ax.set_xlabel("Mjerenja")
ax.set_ylabel("Impulsi u 60s")
ax.legend()
ax.set_ylim(0,699)

bx.grid(zorder=3)
bx.set_axisbelow(True)
bx.bar(popis_materijala,prosjecne_vrijednosti,align='center',color='skyblue')
for i in range(len(prosjecne_vrijednosti)):
    bx.annotate(prosjecne_vrijednosti[i],xy=(i-0.2,prosjecne_vrijednosti[i]+10))
bx.set_ylim(0,699)

plt.show()

