import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as color
import PSF




Ncolors=100
colors=0
Nsize=8
s=PSF.square(2**Nsize,.1)
for i in np.linspace(380/750, 1,Ncolors):
    colors+=s.color_psf(i)

colorsA=colors-np.mean(colors)
colorsA/=np.ptp(colors)

plt.imshow(np.clip(colorsA,0,1))

