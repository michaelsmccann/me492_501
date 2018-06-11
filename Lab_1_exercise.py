#Lab_1_exercise.py
from matplotlib.pyplot import *
from numpy import *

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
try:
	while True:
		GPIO.setup(12, GPIO.OUT)
		GPIO.output(12, GPIO.HIGH) #sets to 3.3V\
		time.sleep(2)
		
		GPIO.output(12, GPIO.LOW)   #SETS TO 0V
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
