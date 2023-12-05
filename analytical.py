import numpy as np
import matplotlib.pyplot as plt
import PSF
import scipy.special as sp
Grids=[]
for i in [5,6,7,8,9,10]:
    Grids.append(np.meshgrid(np.linspace(-1,1,2**i),np.linspace(-1,1,2**i)))
n=6
def anal(x,y,d):
    return (sp.jv(1,np.sqrt((d*x)**2+(d*y)**2))/np.sqrt((d*x)**2+(d*y)**2))**2
plt.imshow(np.log((anal(Grids[4][0],Grids[4][1],40))))
plt.show(2)
plt.imshow(np.log(PSF.circle(2**8,.1).pf**2))

t=3
N=2**8
ticks=np.linspace(N/2,N,t)
units=(ticks-N/2)*2*np.pi*750/10**6
units=np.round(units,2)
plt.xticks(ticks, units)
plt.xlabel("micrometers")