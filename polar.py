"""
Demo of custom tick-labels with user-defined rotation.
"""
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons


z = int(input("how long you wanna go? "))
n1 = 2
n2 = int(input("another number "))
xcor = []
ycor =[]
lcor=[]
x = 0
i = 0


for j in range(0,z):
	lcor.append(j*(math.log(2,math.e)/math.log(3,math.e)))


def pycode(x):
    n = math.ceil(x*(math.log(n2,math.e)/math.log(n1,math.e))-1)#a1
    return n
while x <= z:
    x += 1
    ycor.append((n2**x/n1**pycode(x)))
    ycor.append((n1**(pycode(x)+1)/n2**x))
while i <= z*2+1: #math done to allign x and y coordinates
    i+=1
    xcor.append(i)
labels = []
   
#plt.subplot(111,polar=True)

plt.plot(xcor[0:z:2], ycor[0:z:2], 'co')
plt.plot(xcor[1:z:2], ycor[1:z:2], 'ro')

plt.plot((n2**x/n1**pycode(x)),'k')


#plt.plot(xcor,ycor,'k')
# You can specify a rotation for the tick labels in degrees or with keywords.
#plt.xticks(lor, labels, rotation='vertical')
plt.xticks(xcor, labels, rotation='vertical')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
plt.show()
