import numpy as np
import matplotlib.pyplot as plt
import gaussian
def Large_K(k,l):
    return 10*np.abs(k**1*(1-np.exp(-(k/l)**5)))
L=1
import PSF
plt.imshow(np.real(gaussian.gaussian_rand_field(2**8, Large_K,L)),cmap="jet")
k_cut_off=PSF.circle(2**8,.1)

k_cut_off.add_noise(Large_K, .21)

plt.imshow(k_cut_off.PSF_diffraction())