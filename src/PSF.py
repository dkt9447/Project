import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import matplotlib.colors as color
import gaussian as gauss

import colour

def normalize(A):
    if np.ptp(A)==0:
        return np.zeros(A.shape)
    return (A-np.min(A))/np.ptp(A)


class PSF:
    """
    

    Parameters
    ----------
    size : int
       Size of PFT Field
    A : TYPE
        Callable function of the form P(x,y,args) that returns bool for each index. Determines apature shape
    *args : TYPE
        arguments for A
    l:float between .5 and 1
        wavelength of light divided by 750nm ie ratio with trespect to red light
        
    p: array
        shape of apature
    pf: array
        fft of p or pft
    """

    
    def __init__(self,size:int,A:callable,*args): 
        self.size=size
        self.args=args
        self.A=A
        dk=np.linspace(-1,1,self.size)
        self.x,self.y=np.meshgrid(dk,dk)
        self.pf=self.PSF_diffraction(l=1)
    def PSF_diffraction(self,l=1):
        '''
        Preforms Diffraction pattern, sets self.pf to it


        Parameters
        ----------
        l : TYPE, optional
            DESCRIPTION. The default is 1.

        Returns
        -------
        pf : TYPE
            Defraction pattern given wavlength l

        '''
        x,y=self.x,self.y
        x=x*l
        y=y*l
        self.p=np.zeros(x.shape)
        self.p[self.A(x,y,*self.args)]=1
        pf=fftpack.fft2(self.p)
        pf=fftpack.fftshift(pf)
        return np.abs(pf)
    def add_noise(self,P:callable,*args):
        '''
        
        multiply
        Parameters
        ----------
        P : callable
            Power spectrum of the form P(k,args).
        *args : TYPE
            DESCRIPTION.

        modifies apature shape with gaussian noise
        returns PSF and modulated Apature
        -------
    

        '''
        field=gauss.gaussian_rand_field(self.size,P,*args)
        field=np.exp(1j*2*np.pi*field)
        p=self.p
        p=p*field
        self.p=p
        return np.abs(fftpack.fftshift(fftpack.fft2(p))),np.real(p)

    def color_psf(self,l=1):
        if l <380/750:
            raise Exception("Walengths below 380nm are not visible")
        '''        
        Parameters
        ----------
        l : TYPE, optional
            DESCRIPTION. The default is 1. ratio of wavelength to default red light i.e. red is 1, purple is .5

        Returns
        -------
        TYPE
            DESCRIPTION. size by size arry of rgb values for diffaction

        '''
        RGB=colour.XYZ_to_RGB(colour.wavelength_to_XYZ(l*750),"sRGB")
        pf=np.abs(self.PSF_diffraction(l))
        pf=normalize(pf)
        R=RGB[0]*pf
        G=RGB[1]*pf
        B=RGB[2]*pf
        "gamma correction???"
        # R=np.power(np.abs(R),.42)
        # G=np.power(np.abs(G),.42)
        # B=np.power(np.abs(B),.42)
        return np.clip(10*(np.stack([R,G,B],axis=-1)),0,1)

    def PSFshow(self,**kwargs):
        '''
        

        Parameters
        ----------
        **kwargs : TYPE
            DESCRIPTION.

        Identitcal to imshow(pf, **kwargs)

        '''
        plt.imshow(np.abs(self.pf),**kwargs)
    def APAshow(self,**kwargs):
        '''
        

        Parameters
        ----------
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        Identitcal to imshow(apature, **kwargs)

        '''
        plt.imshow(np.abs(self.p),**kwargs)
    def white_light(self,Ncolors):
        '''
        

        Parameters
        ----------
        Ncolors : int
            number of colors.

        Returns
        -------
        colorsA : size by size by 3 rgb image array .

        '''
        colors=0
        for i in np.linspace(380/750, 1,Ncolors):
            colors+=self.color_psf(i)
        # colors=colors-np.mean(colors)
        # colors/=np.ptp(colors)
        return normalize(colors)
    def labels(self,t,angle=False):
        '''
        

        Parameters
        ----------
        t : int
            number of ticks.

        Returns
        -------
        units : labels in micrometers.
        ticks : array indecies for units
            DESCRIPTION.

        '''
        N=self.size
        ticks=np.linspace(0,N,t)
        units=(ticks-N/2)*2*np.pi*750/10**6
        units=np.round(units,2)
        if angle:
            units*=10**6
        return units,ticks
class circle(PSF):   
    def __init__(self, size, radius=.1):
        PSF.__init__(self, size, ___circ___, radius)
class square(PSF):
    def __init__(self, size, radius=.1):
        PSF.__init__(self, size, ___squa___, radius)
class two_slits(PSF):
    def __init__(self, size, width=.1,distance=.5):
        PSF.__init__(self, size, ___two_slits___, width,distance)
class one_slit(PSF):
    def __init__(self, size, width=.1):
        PSF.__init__(self, size, ___one_slit___, width)


class polygon(PSF):
    def __init__(self,size,c=.1,sides=3):
        PSF.__init__(self,size,___polygon___,c,sides)




def f(x,y,r,r2):
    return np.logical_and(x**2+y**2<r**2,x**2+y**2>r2**2)

def a(k,l,kc):
    p=k**l*np.exp(-k/k)
    p[0][0]=0
    return 10*p

##common shapes
def ___circ___(x,y,r):
    return x**2+y**2<r**2
def ___squa___(x,y,r):
    return np.logical_and(np.abs(x)<r,np.abs(y)<r)

def ___polygon___(x,y,c,n):
    theta=np.arctan2(x,y)
    r=np.sqrt(x**2+y**2)
    return r<=c/np.cos(theta-2*np.pi/n*np.floor((n*theta+np.pi)/(2*np.pi)))
def ___two_slits___(x,y,a,d):
    return np.logical_or((x-d/2)**2<a**2,(x+d/2)**2<a**2)
def ___one_slit___(x,y,a):
    return x**2<a**2
