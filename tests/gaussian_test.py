import matplotlib.pyplot as plt
import sys
import gaussian as g
import numpy as np
def a(k,l,kc):
    p=k**l*np.exp(-k**2/kc**2)
    p[0][0]=0
    return p
fig,axs=plt.subplots(3,3)
for i in range(0,3):
    for j in range(0,3):
        alpha=-2*(i+1)
        beta=10**(j)
        out = g.gaussian_rand_field(256,alpha,beta,a )
        axs[i,j].imshow(out.real, interpolation='none',cmap='jet')
        label="l="+str(alpha)+" kc="+str(beta)
        axs[i,j].set_title(label)
        axs[i,j].axis('off')

fig.tight_layout()



