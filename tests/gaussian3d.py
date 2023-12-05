import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def a(k,l):
    
    return np.where(k==0,0,k**l)
def gaussian_rand_field(N:int,p,*args):
    """
    

    Parameters
    ----------
    N : int
       Size of Gaussian Field
    p : TYPE
        Callable function of the form P(k,args).
    *args : TYPE
        arguments for p

    Returns
    -------
    noise :NxN array of real valued noise

    """
    dk=np.linspace(-N//2,N//2-1,N)
    kx,ky,kz,=np.meshgrid(dk,dk,dk)
    kmag=np.sqrt(kx**2+ky**2+kz**2)
    kmag=np.fft.ifftshift(kmag)
    fnoise=np.random.normal(0,p(kmag,*args),(N,N,N))+1j*np.random.normal(0,p(kmag,*args),(N,N,N))
    
    noise=np.fft.ifftn(fnoise)
    return np.abs(noise)

noise3d=gaussian_rand_field(2**8, a, -2)

plt.imshow(noise3d[0])
fig=plt.figure()
ax=plt.axes()
plot=ax.imshow(noise3d[0],cmap='jet')
def init():
    plot.set_data(noise3d[0])
    return [plot]
def animate(i):
    plot.set_data(noise3d[i%256])
    return [plot]
anim = FuncAnimation(fig, animate, init_func=init,frames=2**8+1,interval=1,blit=True)

anim.save('3dnoise.gif',dpi=300)