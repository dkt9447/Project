import matplotlib.pyplot as plt
import sys
import gaussian as g
import numpy as np
def a(k,l,kc):
    p=k**l*np.exp(-k/kc)
    p[0][0]=0
    return p
for alpha in [-4.0, -3.0, -2.0]:
    for beta in [.01,.1,1,10]:
        out = g.gaussian_rand_field(256,alpha,beta,a )
        label="a="+str(alpha)+" kc="+str(beta)
        plt.figure(label=label)
        plt.imshow(out.real,label=str(alpha), interpolation='none',cmap='jet')
