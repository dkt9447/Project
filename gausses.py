import numpy as np
import matplotlib.pyplot as plt
import gaussian
def Large_K(k,l):
    return np.abs(50*(1-np.exp(-(k/l)**2)))
L=.2
import PSF
noise=gaussian.gaussian_rand_field(2**8, Large_K,L)
noise=np.exp(1j*2*np.pi*noise)
k_cut_off=PSF.circle(2**8,.1)
plt.imshow(k_cut_off.add_noise(Large_K,L)[0])


