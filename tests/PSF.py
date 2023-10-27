import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

from matplotlib import cm
from matplotlib.ticker import LinearLocator

np.seterr(divide = 'ignore') #investigate this

def calculate_2dft(input):
    ft = np.fft.ifftshift(input)
    ft = np.fft.fft2(ft)
    ft = np.fft.fftshift(ft)
    return ft

def calculate_fft(input):
    ft = fftpack.fft2(input)
    return ft

N = 10001
x = np.arange(-500,501,1)
y = np.arange(-500,501,1)
X, Y = np.meshgrid(x, y)

#we compute the fourier transform of the outer circle with value 1
circle_x, circle_y, r= 0, 0, 400
pts = (X-circle_x)**2+(Y-circle_y)**2 >= r**2
M = np.ones(X.shape)
M[pts] = 0
ft = calculate_2dft(M)

#we compute the fourier transform of just the inner circle with value 1
circle_x, circle_y, r= 0, 0, 100
pts1 = (X-circle_x)**2+(Y-circle_y)**2 >= r**2
M1 = np.ones(X.shape)
M1[pts1]=0
ft_1 = calculate_2dft(M1)

#this is the FT of the aperture (donut-shaped)
M2 = np.ones(X.shape)
M2[pts]=0
pts2 = (X-circle_x)**2+(Y-circle_y)**2 <= r**2
M2[pts2]=0
ft_ape = calculate_2dft(M2)

fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
surf = ax.plot_surface(x,y,ft_1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
ax.set_xlim(-200,200)
ax.set_ylim(200,-200)
fig.colorbar(surf,shrink=0.5,aspect=5)

plt.show()




