import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button

N=2**8
r0=2
r2_0=0
dk=np.linspace(-10,10,N)
x,y=np.meshgrid(dk,dk)
def P(x,y,r,r2):
    p=np.zeros(x.shape)
    p[np.logical_and(x**2+y**2<r,x**2+y**2>r2)]=1
    return p

def PFT(x,y,r,r2):
    p=P(x,y,r,r2)
    pf=np.fft.fft2(p)
    pf=np.fft.fftshift(pf)
    return (np.abs(pf))





fig, ax = plt.subplots()
plot = ax.imshow(PFT(x,y,r0,r2_0))

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axRad = fig.add_axes([0.25, 0.1, 0.65, 0.03])
rad_slider = Slider(
    ax=axRad,
    label='Radius',
    valmin=0.1,
    valmax=5,
    valinit=r0,
)
axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
rad2_slider = Slider(
    ax=axamp,
    label="Inner Radius",
    valmin=0,
    valmax=5,
    valinit=0,
    orientation="vertical"
)

def update(val):
    plot.set_data(PFT(x,y,rad_slider.val,rad2_slider.val))
    fig.canvas.draw_idle()
rad_slider.on_changed(update)
rad2_slider.on_changed(update)
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')
def reset(event):
    rad_slider.reset()
    rad2_slider.reset()
button.on_clicked(reset)
plt.show()