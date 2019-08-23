import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

xmin, xmax = -5, 5
mu1_min, mu1_max = -5, ((3/2)-math.sqrt(2))
mu2_min, mu2_max = ((3/2)+math.sqrt(2)), 5

fig = plt.figure()

ax = plt.axes(xlim=(xmin, xmax), ylim=(-10, 10))
line, = ax.plot([], [], lw=2)
ax.plot([xmin, xmax], [0,0], 'm')
ax.plot([0, 0], [-10, 10], 'm')

def init():
    line.set_data([], [])
    return line,

def animate(mu):
    x = np.linspace(xmin, xmax, 100)
    y = mu + x/2 - x/(1+x)
    line.set_data(x, y)
    return line,

def animate_2(mu):
    x = np.linspace(xmin, xmax, 100)
    y = mu + x/2 - x/(1+x)
    line.set_data(x, y)
    return line,


bifurcation = FuncAnimation(fig, animate, init_func=init,frames=np.linspace(mu1_min, mu1_max, 100),interval=100, blit=True)
bifurcation2 = FuncAnimation(fig, animate_2, init_func = init, frames = np.linspace(mu2_min,mu2_max,100),interval = 100, blit = True)

plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.tick_params(labelsize=15)
bifurcation2.save('2.mp4')
plt.show()
