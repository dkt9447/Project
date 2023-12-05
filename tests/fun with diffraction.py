import numpy as np
import matplotlib.pyplot as plt
import PSF
def displace(x,y,dx,dy):
    return x+dx,y+dy
def polygon(x,y,c,n):
    theta=np.arctan2(x,y)
    r=np.sqrt(x**2+y**2)
    return r<=c/np.cos(theta-2*np.pi/n*np.floor((n*theta+np.pi)/(2*np.pi)))
def repeated(x,y,r):
    X=2*np.mod(.5*(x-r),r)-r
    Y=2*np.mod(.5*(y-r),r)-r
    limit=np.logical_and(np.abs(x)<.1,np.abs(y)<.1)
    return np.logical_and(X**2+Y**2<=r**2,limit)
def beads(x,y,c):
    hor=np.logical_and(-c*np.abs(np.sin(x/c))<y,c*np.abs(np.sin(x/c))>y)
    vert=np.logical_and(-c*np.abs(np.sin(y/c))<x,c*np.abs(np.sin(y/c))>x)
    return np.logical_or(hor,vert)
s=PSF.PSF(2**8, polygon, .2 ,6)
repeat=PSF.PSF(2**8,repeated,.01)
b=PSF.PSF(2**8,beads,.05)

plt.imshow(s.PSF_diffraction())