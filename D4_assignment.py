import numpy as np
from matplotlib.pyplot import *
from numpy import *

t = arange(1,3,0.02)
T=(6*np.log(t))-(7*np.e**(0.2*t)) 

figure(1)
clf()

plot(t,T)
xlabel('time (min)')
ylabel('Temperature (C)')
ylabel('$Temperature (C)$')
xlabel('$time (min)$')
title('McCann-Plot')

show()


print('Hello World! I just wrote my first Python program. Yayyyyyyyy!')
print('Michael McCann')

