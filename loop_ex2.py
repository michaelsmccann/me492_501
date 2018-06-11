 #loop_ex2.py
from matplotlib.pyplot import *
from numpy import *

myvect= ['a','b',3]

N = len(myvect)
for i in range(N):
	item = myvect[i]
	print('i = '+str(i))
	print('item = '+str(item))

for item in myvect:
	print(item)
print('this is the end of the loop')
