import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as color
import PSF
def polygon(x,y,c,n):
    theta=np.arctan2(x,y)
    r=np.sqrt(x**2+y**2)
    return r<=c/np.cos(theta-2*np.pi/n*np.floor((n*theta+np.pi)/(2*np.pi)))
def in_out_struts(x,y,r1,r2,n):
    
    donut=np.logical_and(x**2+y**2<r2**2,x**2+y**2>r1**2)
    struts=np.full(x.shape, False)
    if n!=0:
        for i in range(int(n)):
            struts=np.logical_or(((x*np.cos(np.pi*i/n)-y*np.sin(np.pi*i/n))**2<0.0001),struts)
    struts=np.logical_not(struts)
    
    return np.logical_and(donut,struts)

Ncolors=1

Nsize=8
S=PSF.PSF(2**Nsize,in_out_struts,0,.2,6)


plt.imshow(S.white_light(9))
units,ticks=S.labels(5)
plt.xticks(ticks,units)
plt.yticks(np.flip(ticks),units)
plt.xlabel("micrometers")


