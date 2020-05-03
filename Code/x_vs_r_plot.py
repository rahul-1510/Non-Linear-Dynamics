import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

x1=np.linspace(3,12,1000)
y1=(1/2 - x1 + ((x1*x1)-3*x1+0.25)**(0.5))

x2=np.linspace(-6,0,1000)#(3+(5**(0.5))/2)3-(5**(0.5))/2)
y2=(1/2 - x2 + ((x2*x2)-3*x2+0.25)**(0.5))

x3=np.linspace(3,12,1000)#(3+(5**(0.5))/2)(3-(5**(0.5))/2)
y3=(1/2 - x3 - ((x3*x3)-3*x3+0.25)**(0.5))

x4=np.linspace(-6,0,1000)
y4=(1/2 - x4 - ((x4*x4)-3*x4+0.25)**(0.5))

plt.plot(x1,y1)
plt.plot(x2,y2,linestyle='dashed')
plt.plot(x3,y3,linestyle='dashed')
plt.plot(x4,y4)

plt.xlabel('r', fontsize=15)
plt.ylabel('x', fontsize=15)
plt.savefig('q3')
show()
