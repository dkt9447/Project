import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button, RadioButtons
import PSF

def clip(A):
    return np.clip(A-np.mean(A),0,1)


N=2**8
r0=.001

i=0
number0=0
dk=np.linspace(-1,1,N)
x,y=np.meshgrid(dk,dk)
def circle(x,y,r):
    return x**2+y**2<r**2
def square(x,y,r):
    return np.logical_and(np.abs(x)<r,np.abs(y)<r)

c=np.array([PSF.PSF(N,circle,.1),PSF.PSF(N,square,.1)])


fig, ax = plt.subplots()
plot = ax.imshow(clip(c[i].color_psf(1)))

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.


axCol=fig.add_axes([0.2, 0.25, 0.0225, 0.63])
col_slider = Slider(
    ax=axCol,
    label="Wavelength (l/750 nm)",
    valmin=380/750,
    valmax=1,
    valinit=1,
    orientation="vertical"
)
def update(val):
    plot.set_data(clip((c[i]).color_psf(col_slider.val)))
    fig.canvas.draw_idle()
col_slider.on_changed(update)

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
circax=fig.add_axes([.3,.125,.1,.04])
squareax=fig.add_axes([.4,.125,.1,.04])
circleButton= Button(circax,"Circle",hovercolor='0.975')
squareButton=Button(squareax,"Square",hovercolor='0.975')
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    col_slider.reset()
def SetCircl(event):
    global i
    i=0
def SetSquare(event):
    global i
    i=1
button.on_clicked(reset)
circleButton.on_clicked(SetCircl)
squareButton.on_clicked(SetSquare)
 



plt.show()

