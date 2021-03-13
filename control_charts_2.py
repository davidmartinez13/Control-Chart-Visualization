import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

data1=np.array([-30,50,-20,10,30,
                0,50,-60,-20,30,
                -50,10,20,30,20,
                -10,-10,30,-20,50,
                20,-40,50,20,10,
                0,0,40,-40,20,
                0,0,20,-20,-10,
                70,-30,30,-10,0,
                0,0,20,-20,10,
                10,20,30,10,50,
                40,0,20,0,20,
                30,20,30,10,40,
                30,-30,0,10,10,
                30,-10,50,-10,-30,
                10,-10,50,40,0,
                0,0,30,-10,0,
                20,20,30,30,-20
                ,10,-20,50,30,10,
                50,-10,40,20,0,
                50,0,0,30,10])

data1=data1.reshape((20,5))
d2=2.326 
D3=0
D4=2.114
n=5
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
