 #loop_ex5.py
from matplotlib.pyplot import *
from numpy import *

myvect1= ['a','b','c','d','e']
for i in range(10):
	print('i = '+str(i))
	if i>5:
		print('Breaking')
		break
	print('i = '+str(i))
	for item in myvect1:
		print(item)
	print('item = '+str(item))
print('this is the end of the loop')
