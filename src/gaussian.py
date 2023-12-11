
"Prep work 3"
import numpy as np
import matplotlib.pyplot as plt
def a(k,l,kc):
    return np.where(k<=.10,0,k**l)
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
    dk=np.linspace(-1,1,N)
    kx,ky=np.meshgrid(dk,dk)
    kmag=np.sqrt(kx**2+ky**2)
    
    kmag=np.fft.ifftshift(kmag)

    fnoise=np.random.normal(0,p(kmag,*args),(N,N))+1j*np.random.normal(0,p(kmag,*args),(N,N))
    #symmeterizing the field
    fnoise[:0:-1,:-N//2:-1]=np.conjugate(fnoise[1:,1:N//2])
    fnoise[0,:-N//2:-1]=np.conjugate(fnoise[0,1:N//2])
    fnoise[:-N//2:-1,0]=np.conjugate(fnoise[1:N//2,0])
    fnoise[:-N//2:-1,N//2]=np.conjugate(fnoise[1:N//2,N//2])
    fnoise[N//2,:-N//2:-1]=np.conjugate(fnoise[N//2,1:N//2])
    fnoise[0,0]=fnoise[0,N//2]=fnoise[N//2,0]=fnoise[N//2,N//2]=0
    noise=np.fft.ifft2(fnoise)
    return np.abs(noise/np.max(noise))*2*np.pi