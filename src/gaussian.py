import numpy as np
import matplotlib.pyplot as plt
def a(k,l,kc):
    p=k**l
    p[0][0]=0
    return p
def gaussian_rand_field(N:int,l,kc):
    dk=np.linspace(-N//2,N//2-1,N)
    kx,ky=np.meshgrid(dk,dk)
    kmag=np.sqrt(kx**2+ky**2)
    kmag=np.fft.ifftshift(kmag)
    fnoise=np.random.normal(0,a(kmag,l,kc),(N,N))+1j*np.random.normal(0,a(kmag,l,kc),(N,N))
    fnoise[:0:-1,:-N//2:-1]=np.conjugate(fnoise[1:,1:N//2])
    fnoise[0,:-N//2:-1]=np.conjugate(fnoise[0,1:N//2])
    fnoise[:-N//2:-1,0]=np.conjugate(fnoise[1:N//2,0])
    fnoise[:-N//2:-1,N//2]=np.conjugate(fnoise[1:N//2,N//2])
    fnoise[N//2,:-N//2:-1]=np.conjugate(fnoise[N//2,1:N//2])
    fnoise[0,0]=fnoise[0,N//2]=fnoise[N//2,0]=fnoise[N//2,N//2]=0
    noise=np.fft.ifft2(fnoise)
    return noise
