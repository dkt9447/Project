import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quadrature
import scipy
import matplotlib.cm as cm

#prep work
#a calculating J1

def integrand(theta,x):
    integrand = (1/np.pi)*np.cos(theta - x*np.sin(theta))
    return integrand

def J1_quadrature(x):
    f = lambda theta:(1/np.pi)*np.cos(theta - x*np.sin(theta))
    res = quadrature(f,0.,np.pi)
    return (res)

#using simpsons rule to check the integral
def J1_simpson(x):
    range = [0.,np.pi]
    num = 101
    theta = range[0] + (range[1] - range[0]) * (np.arange(num, dtype=np.float64)) / np.float64(num - 1.)
    dtheta = (range[1] - range[0]) / np.float64(num - 1.)
    simps_weights = np.zeros(num, dtype=np.float64)
    simps_weights[0] = 1. / 3.
    simps_weights[-1] = 1. / 3.
    simps_weights[1:-1:2] = np.zeros(num // 2, dtype=np.float64) + 4. / 3.
    simps_weights[2:-1:2] = np.zeros(num // 2 - 1, dtype=np.float64) + 2. / 3.
    simps_integral = (integrand(theta,x)*simps_weights*dtheta).sum()
    return (simps_integral)


print(J1_quadrature(1)[0])
print(J1_simpson(1))
print(J1_quadrature(1)[0]-J1_simpson(1))

#plot the fourier transform
