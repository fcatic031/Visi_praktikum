from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

class graficki_prikaz():
    def __init__(self) -> None:
        pass
    def pol_interpol(x,y,n):
        x1=np.linspace(min(x),max(x),n)
        f=interp1d(x,y,kind='cubic')
        y1=f(x1)
        plt.grid()
        plt.plot(x1,y1)
        plt.plot(x,y,'ob')
        plt.show()

    def linearna_regresija(x1,y1):
        x=np.linspace(min(x1),max(x1),1000)
        a,b,r_val,p_val,std_error=linregress(x1,y1)
        y=a*x+b
        plt.grid()
        plt.plot(x,y)
        plt.plot(x1,y1,'ob')
        plt.show()
    