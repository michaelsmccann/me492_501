#Lab_1.py
from matplotlib.pyplot import *
from numpy import *

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, GPIO.HIGH) #sets to 3.3V

time.sleep(3)

GPIO.output(12, GPIO.LOW)   #SETS TO 0V

GPIO.cleanup()
