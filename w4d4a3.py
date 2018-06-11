#w4d4a3
from matplotlib.pyplot import *
from numpy import *

N = input("Please enter a num as an upper limit:")
N = int(N)

for i in range(2,N):
	check_var = True
	for k in range(2,i):
		if (i%k) == 0:
			check_var = False
		if check_var:
			print(i)
