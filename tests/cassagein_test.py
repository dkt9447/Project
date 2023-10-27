import numpy as np
import matplotlib.pyplot as plt
N=2**9
r0=2
r2_0=0
number0=0
dk=np.linspace(-10,10,N)
x,y=np.meshgrid(dk,dk)
def P(x,y,r,r2,num):
    p=np.zeros(x.shape)
    p[np.logical_and(x**2+y**2<r**2,x**2+y**2>r2**2)]=1
    if num!=0:
        for i in range(int(num)):
            p[(x*np.cos(np.pi*i/num)-y*np.sin(np.pi*i/num))**2<.001]=1
    return p

        
R2=0
def PFT(x,y,r,r2,num):
    p=P(x,y,r,r2,num)
    pf=np.fft.fft2(p)
    pf=np.fft.fftshift(pf)
    return (np.abs(pf))
# for i in range(1,4):
#     for j in range(0,i+1):
#         r1=5*10**(i-3)
#         r2=2.5**(j-3)
#         plt.figure(2**i+3**j)
#         plt.axis("off")
#         plt.title("Outer Radius="+str(r1/10)+ " inner Radius="+str(r2/10))
#         plt.imshow(PFT(x, y, r1, r2, 0),cmap='jet')
plt.imshow(PFT(x, y, .5, .01, 0),cmap='jet')
plt.title("Outer Radius="+str(.5/10)+ " inner Radius="+str(0))