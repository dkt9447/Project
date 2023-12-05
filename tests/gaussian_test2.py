import numpy as np
import matplotlib.pyplot as plt
import gaussian
from matplotlib.animation import FuncAnimation
def Cut_off(k,l):
    return np.abs(k*(1-np.exp(-(k/4l)**2)))
def non_con_cut_off(k,l):
    np.where(np.abs(k)<l,0,k**2)
def Large_K(k,l):
    return k**l
def low(k):
    return k**.5

L=.12
n=-1
c=10
import PSF


gauss_test=PSF.square(2**8,.1)

plt.imshow(gauss_test.add_noise(Cut_off,10)[0])

units,ticks=S.labels(5)
plt.xticks(ticks,units)
plt.yticks(np.flip(ticks),units)
plt.xlabel("micrometers")

plt.show()
plt.imshow(gauss_test.add_noise(Large_K,10)[0])


units,ticks=S.labels(5)
plt.xticks(ticks,units)
plt.yticks(np.flip(ticks),units)
plt.xlabel("micrometers")
plt.show()
fig=plt.figure()
ax=plt.axes()
plot=ax.imshow(gauss_test.PSF_diffraction())
def init():
    plot.set_data(gauss_test.PSF_diffraction())
    return [plot]
def animate(i):
    plot.set_data(gauss_test.add_noise(low)[0])
    return [plot]
anim = FuncAnimation(fig, animate, init_func=init,frames=50,interval=5,blit=True)

anim.save('exposure.gif',dpi=100)
