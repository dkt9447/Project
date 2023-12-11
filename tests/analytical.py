import numpy as np
import matplotlib.pyplot as plt
import PSF
import scipy.special as sp
from scipy import fftpack
res=np.empty(10)
print(res.shape)
def anal(x,y,d):
    x*=d
    y*=d
    r=np.sqrt(x**2+y**2)
    return sp.jv(1,r)/r

I=2**10
x,y=np.meshgrid(np.linspace(-I,I-1,I),np.linspace(-I,I-1,I))
for j in range(10):
        rad= 2**j/I
        #radius ranges from .1 to 
        
        pf=PSF.circle(I,rad).pf
        a=anal(x,y,(np.pi*rad)/2)
        a=a/np.max(a)
        pf=pf/np.max(pf)
        residual=np.abs(pf-a)
        res[j]=np.sum(residual)/np.sum(np.abs(a))

plt.plot(res)
plt.xlabel("radius size (2^(n-10)) of total grid")
plt.ylabel('residual compared to J1')
