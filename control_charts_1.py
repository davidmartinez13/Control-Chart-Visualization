import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

data1=np.array([6,9,10,15
               ,10,4,6,11
               ,7,8,10,5
               ,8,9,6,13
               ,9,10,7,13
               ,12,11,10,10
               ,16,10,8,9
               ,7,5,10,4
               ,9,7,8,12
               ,15,16,10,13
               ,8,12,14,16
               ,6,13,9,11
               ,16,9,13,15
               ,7,13,10,12
               ,11,7,10,16
               ,15,10,11,14
               ,9,8,12,10
               ,15,7,10,11
               ,8,6,9,12
               ,13,14,11,15])

data1=data1.reshape((20,4))
d2=2.059 
D3=0
D4=2.282
A2=0.729
n=4
R= abs(np.amax(data1, axis=1)-np.amin(data1, axis=1))#range n=4 calculation
Rbar=sum(R)/20
sigma=float(Rbar)/d2#find sigma as the average of ranges/d2
print(sigma)

Xbar=np.sum(data1, axis=1)/n #average of samples
Xbar2=sum(Xbar)/20

#X bar Chart
# UCLx=Xbar2+(A2*Rbar)
# LCLx=Xbar2-(A2*Rbar)
UCLx=Xbar2+3*(Rbar/(d2*math.sqrt(n)))
LCLx=Xbar2-3*(Rbar/(d2*math.sqrt(n)))
# R chart
UCLR= D4*Rbar
LCLR = D3*Rbar

plt.subplot(1,2,1)
plt.title("X bar Chart (in statistical control)")
plt.figtext(0.5, 0.01, "STD="+str(sigma), ha="center", fontsize=18, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
plt.xlabel("Time")
plt.ylabel("Sample Mean")
plt.plot(Xbar)
plt.hlines(UCLx,0,20)
plt.hlines(LCLx,0,20)
plt.hlines(Xbar2,0,20)

plt.subplot(1,2,2)
plt.title("R chart (in statistical control)")
plt.xlabel("Time")
plt.ylabel("Range")
plt.plot(R)
plt.hlines(UCLR,0,20)
plt.hlines(LCLR,0,20)
plt.hlines(Rbar,0,20)


plt.show()
