import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as color
import PSF

def in_out_struts(x,y,r1,r2,n):
    donut=np.logical_and(x**2+y**2<r2**2,x**2+y**2>r1**2)
    struts=np.full(x.shape, False)
    if n!=0:
        for i in range(int(n)):
            struts=np.logical_or(((x*np.cos(np.pi*i/n)-y*np.sin(np.pi*i/n))**2<0.0002),struts)
    struts=np.logical_not(struts)
    
    return np.logical_and(donut,struts)

Ncolors=100
colors=0
Nsize=8
s=PSF.PSF(2**Nsize,in_out_struts,.05,.1,6)
for i in np.linspace(380/750, 1,Ncolors):
    colors+=s.color_psf(i)

colorsA=colors-np.mean(colors)
colorsA/=np.ptp(colors)

plt.imshow(np.clip(colorsA,0,1))

