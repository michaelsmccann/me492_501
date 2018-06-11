#cleanup.py


import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


pins = [4,17,18,27]
GPIO.setup(pins, GPIO.OUT)
GPIO.cleanup()
