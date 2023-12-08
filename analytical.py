import numpy as np
import matplotlib.pyplot as plt
import PSF
import scipy.special as sp
Grids=[]
i=2**4

I=7
x,y=np.meshgrid(np.linspace(i,i,2**I),np.linspace(i,i,2**I))

def anal(x,y,d):
    return (sp.jv(1,np.sqrt((d*x)**2+(d*y)**2))/np.sqrt((d*x)**2+(d*y)**2))**2


plt.imshow(x)