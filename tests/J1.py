import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quadrature
from scipy.special import j1


#prep work
#a calculating J1

def integrand(theta,x):
    integrand = (1/np.pi)*np.cos(theta - x*np.sin(theta))
    return integrand

def J1_quadrature(x):
    f = lambda theta:(1/np.pi)*np.cos(theta - x*np.sin(theta))
    res = quadrature(f,0.,np.pi)
    return (res[0])

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

def J1_func(a,b,N):
    x = np.linspace(a,b,N)
    y = np.zeros(N)
    for i in range(N):
        y[i] = J1_simpson(x[i])
    return(x,y)

def J1_plot(a,b,N):
    x_qua,y_qua = J1_func(a,b,N)
    x_sci = np.linspace(a,b,N)
    y_sci = j1(x_sci)
    residual = y_qua - y_sci
    fig,axs = plt.subplots(3)
    for ax in axs:
        ax.axvline(x=0,color = 'k')
        ax.axhline(y=0,color = 'k')
        ax.set_xlabel("x")
        ax.set_ylabel("y")
    axs[0].plot(x_qua,y_qua)
    #axs[0].xlabel("x")
    #axs[0].ylabel("y")
    axs[0].title.set_text("J1 from simpson's rule")
    axs[1].plot(x_sci,y_sci)
    axs[1].title.set_text("J1 from scipy")
    axs[2].plot(x_qua,residual)
    axs[2].title.set_text("residuals of simpson's rule and scipy")
    fig.tight_layout()
    plt.legend(loc="upper right")
    plt.show()
a=0.
b=50.
N=1001
J1_plot(a,b,N)
    


