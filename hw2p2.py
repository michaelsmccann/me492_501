#hw2p2.py
#Michael McCann

from matplotlib.pyplot import *
from numpy import *

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #use pin number
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

try:
	while True:
		GPIO.output(11, GPIO.input(29))
		
		GPIO.output(11, GPIO.input(31))
		GPIO.output(13, GPIO.input(31))
		
		GPIO.output(11, GPIO.input(32))
		GPIO.output(13, GPIO.input(32))
		GPIO.output(15, GPIO.input(32))
	
except KeyboardInterrupt:
	GPIO.cleanup()
