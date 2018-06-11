#test1p2.py

from matplotlib.pyplot import *
from numpy import *

myclasses= []
classgrade= []
tot = 0
num_classes = int(input('Please enter the number of classes you took last semester. :'))

for i in range(num_classes):
	print('i = '+str(i))
	name = str(input('Please enter the name of the class. :'))
	myclasses.append[name]
	grade = int(input('And what grade did you get in class ' +str(class_name)+'?'))
	classgrade.append[grade]
	tot=(tot + grade)
	print(tot)
ave_grade = (tot / num_classes) 
