 #loop_ex3.py
from matplotlib.pyplot import *
from numpy import *

myvect1= ['a','b','c']
myvect2= [5,10,20]

for item1,item2 in zip(myvect1,myvect2):
	print('item1 =' +str(item1))
	print('item2 =' +str(item2))

print('this is the end of the loop')
