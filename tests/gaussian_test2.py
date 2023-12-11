import numpy as np
import matplotlib.pyplot as plt
import gaussian
from matplotlib.animation import FuncAnimation

def cut_off(k,l,u):
    k=k
    fil=np.logical_and(np.abs(k)>l,np.abs(k)<u)
    k[fil]=k[fil]**2
    k[np.logical_not(fil)]=0 
    return k
def Large_K(k,l):
    return k**l
def low(k):

    return (k**.5)

L=.12
n=-1
c=10
import PSF


gauss_test=PSF.circle(2**8,.1)
units,ticks=gauss_test.labels(5)
plt.xticks(ticks,units)
plt.yticks(np.flip(ticks),units)
plt.xlabel("micrometers")


# # #wavelengths of order grid size (1.4 meters or so)
# # gauss_test.add_noise(cut_off,1.4 , 1.51 )

# # plt.imshow(gauss_test.white_light(15))

# # plt.show(2)
# gauss_test.remove_noise()
# #smaller order wavelengths, order 2 cm or so
# plt.imshow(gauss_test.add_noise(cut_off, 1.39, 1.4)[0])

# # animation for repeated exposures  



fig=plt.figure()
ax=plt.axes()
plot=ax.imshow(gauss_test.PSF_diffraction())
plt.xticks(ticks,units)
plt.yticks(np.flip(ticks),units)
plt.xlabel("micrometers")
def init():
    plot.set_data(gauss_test.PSF_diffraction())
    return [plot]
def animate(i):
    plot.set_data(gauss_test.add_noise(cut_off,0,.015)[0])
    return [plot]
anim = FuncAnimation(fig, animate, init_func=init,frames=50,interval=5,blit=True)

anim.save('bin/exposure.gif',dpi=100)




