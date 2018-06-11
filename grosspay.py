#grosspay.py
#Michael McCann

from matplotlib.pyplot import *
from numpy import *

Hours = int(input("Please enter the number of hours:"))
RPH = int(input("please enter the rate per hour:"))

if (Hours < 40):
	print('You worked less than 40 hours and your rate of pay is $'+str(RPH)+' per hour.')
	grosspay_under40= (Hours*RPH)
	print('You will receive $'+str(grosspay_under40)+' this week.')
elif (Hours ==40):
	print('You worked exactly 40 hours and your rate of pay is $'+str(RPH)+ ' per hour.')
	grosspay_40= (Hours*RPH)
	print('You will receive $'+str(grosspay_40)+' this week.')
elif (Hours > 40):
	print('You worked more than 40 hours and your rate of pay is $'+str(RPH)+' per hour.')
	grosspay_40 =(40*RPH)
	grosspay_over40= (1.5*(Hours-40)*RPH)
	total_grosspay=(grosspay_40+grosspay_over40)
	print('You will receive $'+str(total_grosspay)+' this week.')
