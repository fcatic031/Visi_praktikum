import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

pozadinsko_zr=0,476*60

toron1=[2,2,-1,-7]
toron2=[9,7,3,2]

t=[i for i in range(60,300,60)]


def model(x,a,b,c):
    return a*(x-b)**2+c

popt,pcov=curve_fit(model,t,toron1,p0=[3,2,-16])
x_model1=np.linspace(min(t),max(t),1000)
y_model1=model(x_model1,popt[0],popt[1],popt[2])

popt1,pcov1=curve_fit(model,t,toron2,p0=[3,2,-16])
x_model2=np.linspace(min(t),max(t),1000)
y_model2=model(x_model2,popt1[0],popt1[1],popt1[2])



plt.grid()
plt.plot(t,toron1,'ob')
plt.plot(t,toron2,'or')
plt.xlim(0,t[-1]+50)
plt.xlabel("Vrijeme/s")
plt.ylabel("Impulsi u 60 s")
plt.plot(x_model1,y_model1,label="1. mjerenje")
plt.plot(x_model2,y_model2,label="2. mjerenje",c='red')

plt.legend()
plt.show()