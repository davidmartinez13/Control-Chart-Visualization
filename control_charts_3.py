import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

data1=np.array([3,34.5
               ,4,34.2
               ,4,31.6
               ,4,31.5
               ,5,35
               ,6,34.1
               ,4,32.6
               ,3,33.8
               ,7,34.8
               ,8,33.6
               ,3,31.9
               ,9,38.6
               ,8,35.4
               ,6,34
               ,5,37.1
               ,7,34.9
               ,4,33.5
               ,3,31.7
               ,8,34
               ,4,35.1
               ,2,33.7
               ,1,32.8
               ,3,33.5
               ,2,34.2])

data1=data1.reshape((24,2))
d2=2.326 
D3=0
D4=2.114
n=5
R= data1[:,1]#range n=4 calculation
Rbar=sum(R)/24
sigma=float(Rbar)/d2#find sigma as the average of ranges/d2
print(sigma)

Xbar=data1[:,0] #average of samples
Xbar2=sum(Xbar)/24

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
plt.hlines(UCLx,0,24)
plt.hlines(LCLx,0,24)
plt.hlines(Xbar2,0,24)

plt.subplot(1,2,2)
plt.title("R chart (in statistical control)")
plt.xlabel("Time")
plt.ylabel("Range")
plt.plot(R)
plt.hlines(UCLR,0,24)
plt.hlines(LCLR,0,24)
plt.hlines(Rbar,0,24)

plt.show()