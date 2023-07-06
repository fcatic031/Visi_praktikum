import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from scipy.interpolate import interp1d

t=[60,120,180,240,300,360,420]
meta_barij=[3594,2619,2030,1543,1173,883,638]
meta_barij_log=np.log(meta_barij)


x=np.linspace(t[0],t[-1],1000)
a,b,r_val,p_val,std_error=linregress(t,meta_barij_log)
y=a*x+b

poluraspad=(meta_barij_log[0]/2-b)/a
print(poluraspad)
print(a)
print(b)
print(meta_barij_log[0])

fig,ax=plt.subplots()
plt.grid()
plt.plot(x,y)
plt.plot(t,meta_barij_log,'ob')
#ax.set_xscale('log')
ax.set_ylabel("log(C-C0)")
ax.set_xlabel("vrijeme/s")
ax.set_yscale('log')
#ax.set_ylim(0,10)
plt.show()