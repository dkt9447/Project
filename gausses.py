import numpy as np
import matplotlib.pyplot as plt
import gaussian
from matplotlib.animation import FuncAnimation
def Cut_off(k,l):
    return np.abs(k*(1-np.exp(-(k/l)**2)))
def Large_K(k):
    return k**2
def low(k):
    return k**.5
def normal_modulated(k,c,n):
    k[k==0]=10**15
    return 10*np.abs(k)**n*np.exp(-(k/c)**2)
L=.12
n=-1
c=10
import PSF


gauss_test=PSF.circle(2**8,.1)

    
fig=plt.figure()
ax=plt.axes()
plot=ax.imshow(gauss_test.PSF_diffraction())
def init():
    plot.set_data(gauss_test.PSF_diffraction())
    return [plot]
def animate(i):
    plot.set_data(gauss_test.add_noise(low)[0])
    return [plot]
anim = FuncAnimation(fig, animate, init_func=init,frames=25,interval=5,blit=True)

anim.save('exposure.gif',dpi=100)