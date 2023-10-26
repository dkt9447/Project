import math
import numpy as np
import matplotlib.pyplot as plt
np.seterr(divide = 'ignore')

def calculate_2dft(input):
    ft = np.fft.ifftshift(input)
    ft = np.fft.fft2(ft)
    ft = np.fft.fftshift(ft)
    return ft

N = 10001
x = np.arange(-500,501,1)
y = np.arange(-500,501,1)
circle_x, circle_y, r= 0, 0, 250
X, Y = np.meshgrid(x, y)
plt.set_cmap("gray")

#we compute the fourier transform of the square with value 1
M = np.meshgrid(x,y)
M = np.ones(X.shape)
ft = calculate_2dft(M)

#we compute the fourier transform of just the circle with value 1
pts1 = (X-circle_x)**2+(Y-circle_y)**2 >= r**2
M1 = np.ones(X.shape)
M1[pts1]=0
ft_1 = calculate_2dft(M1)

#this is the FT of the aperture
M2 = np.ones(X.shape)
pts2 = (X-circle_x)**2+(Y-circle_y)**2 <= r**2
M2[pts2]=0
ft_2 = calculate_2dft(M2)

#we plot all the results in the same graph
fig,((ax1,ax2,ax3),(ax4,ax5,ax6)) = plt.subplots(2,3)
ax1.imshow(M)
ax2.imshow(M1)
ax3.imshow(M2)
ax4.imshow(np.log(abs(ft)))
ax5.imshow(np.log(abs(ft_1)))
ax6.imshow(np.log(abs(ft_2)))
plt.show()


#we plot the FT of the aperture next to the FT of the square 
#subtract the FT of the circle
ft_ape = ft - ft_1
plt.subplot(121)
plt.imshow(np.log(abs(ft_2)))
plt.subplot(122)
plt.imshow(np.log(abs(ft_ape)))
plt.show()





