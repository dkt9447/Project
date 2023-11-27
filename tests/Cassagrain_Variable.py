import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button, RadioButtons


N=2**8
r0=.2
r2_0=0
number0=0
dk=np.linspace(-1,1,N)
x,y=np.meshgrid(dk,dk)
def P(x,y,r,r2,num):
    p=np.zeros(x.shape)
    donut=np.logical_and(x**2+y**2>r2**2,x**2+y**2<r**2)
    struts=np.full(x.shape, False)
    if num!=0:
        for i in range(int(num)):
            struts=np.logical_or(((x*np.cos(np.pi*i/num)-y*np.sin(np.pi*i/num))**2<0.0002),struts)
    struts=np.logical_not(struts)
    p[np.logical_and(donut,struts)]=1
    return p
# plt.imshow(P(x,y,.1,.05,3))
def PFT(x,y,r,r2,num):
    p=P(x,y,r,r2,num)
    pf=np.fft.fft2(p)
    pf=np.fft.fftshift(pf)
    return (np.abs(pf))





fig, ax = plt.subplots(2)
plot = ax[0].imshow(PFT(x,y,r0,r2_0,number0))
plot2= ax[1].imshow(P(x,y,r0,r2_0,number0))
fig.set_figheight(25)
fig.set_figwidth(25)
# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axRad = fig.add_axes([0.25, 0.1, 0.65, 0.03])
rad_slider = Slider(
    ax=axRad,
    label='Radius',
    valmin=0.01,
    valmax=.5,
    valinit=r0,
)
axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
rad2_slider = Slider(
    ax=axamp,
    label="Inner Radius",
    valmin=0,
    valmax=rad_slider.val,
    valinit=0,
    orientation="vertical"
)
axStrut=fig.add_axes([0.2, 0.25, 0.0225, 0.63])
strut_slider = Slider(
    ax=axStrut,
    label="Struts",
    valmin=0,
    valmax=6,
    valinit=0,
    orientation="vertical"
)
def update(val):
    plot.set_data(PFT(x,y,rad_slider.val,rad2_slider.val,strut_slider.val))
    plot2.set_data(P(x,y,rad_slider.val,rad2_slider.val,strut_slider.val))
    fig.canvas.draw_idle()
rad_slider.on_changed(update)
rad2_slider.on_changed(update)
strut_slider.on_changed(update)
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')
def reset(event):
    rad_slider.reset()
    rad2_slider.reset()
button.on_clicked(reset)
plt.show()