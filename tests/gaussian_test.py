import matplotlib.pyplot as plt
import sys
sys.path.append('Project/src')
import gaussian as g
for alpha in [-4.0, -3.0, -2.0]:
    for beta in [.01,.1,1,10]:
        out = g.gaussian_rand_field(256,alpha,beta )
        label="a="+str(alpha)+" kc="+str(beta)
        plt.figure(label=label)
        plt.imshow(out.real,label=str(alpha), interpolation='none',cmap='jet')
