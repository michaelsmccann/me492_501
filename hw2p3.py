#hw2p3.py
#Michael McCann

from matplotlib.pyplot import *
from numpy import *

x = int(input("Please enter a number. :"))
y = int(input("Please enter a second number. :"))
z = int(input("Please enter a final number. :"))

l=(x % 2)
m=(y % 2)
n=(z % 2)
odd_list = []
if (l>0):
	odd_list.extend([x])

if (m>0):
	odd_list.extend([y])

if (n>0):
	odd_list.extend([z])

if not odd_list:
	print('None of the numbers provided were odd.')
else:
	largest_odd_value = max(odd_list)
	print(str(largest_odd_value)+(' is the largest odd number provided.'))
