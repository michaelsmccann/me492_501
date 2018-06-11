#hw2p1.py
#Michael McCann

from matplotlib.pyplot import *
from numpy import *

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #use pin number
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

number = int(input("Please enter a number between 1 and 3. : "))
if number==1:
	GPIO.output(11, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(11, GPIO.LOW)
elif number==2:
	GPIO.output(13, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(13, GPIO.LOW)
elif number==3:
	GPIO.output(15, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(11, GPIO.LOW)
else:
	print('Error!')
	print('A number between 1 and 3 should have been chosen.')

GPIO.cleanup()

