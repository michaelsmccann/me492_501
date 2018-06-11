#Lab_2.py
from matplotlib.pyplot import *
from numpy import *

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(12, GPIO.LOW)

try:
	while True:
		GPIO.output(12, GPIO.input(11))
except KeyboardInterrupt:
	GPIO.cleanup()
