#Cylon Test
#hw3p1_cylon.py
#Michael McCann

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


try:
	while True:
		# Up 4
		GPIO.setup(4, GPIO.OUT)
		GPIO.output(4, GPIO.HIGH) #sets to 3.3V\
		time.sleep(0.08)
		
		GPIO.output(4, GPIO.LOW)   #SETS TO 0V
		time.sleep(0.08)

		# Up 17
		GPIO.setup(17, GPIO.OUT)
		GPIO.output(17, GPIO.HIGH) #sets to 3.3V\
		time.sleep(0.08)
		
		GPIO.output(17, GPIO.LOW)   #SETS TO 0V
		time.sleep(0.08)

		# Up 18
		GPIO.setup(18, GPIO.OUT)
		GPIO.output(18, GPIO.HIGH) #sets to 3.3V\
		time.sleep(0.08)
		
		GPIO.output(18, GPIO.LOW)   #SETS TO 0V
		time.sleep(0.08)
		
		# Up 27
		GPIO.setup(27, GPIO.OUT)
		GPIO.output(27, GPIO.HIGH) #sets to 3.3V\
		time.sleep(0.08)
		
		GPIO.output(27, GPIO.LOW)   #SETS TO 0V
		time.sleep(0.08)
		
		# Down 18
		GPIO.setup(18, GPIO.OUT)
		GPIO.output(18, GPIO.HIGH) #sets to 3.3V\
		time.sleep(0.08)
		
		GPIO.output(18, GPIO.LOW)   #SETS TO 0V
		time.sleep(0.08)

		# Down 17
		GPIO.setup(17, GPIO.OUT)
		GPIO.output(17, GPIO.HIGH) #sets to 3.3V\
		time.sleep(0.08)
		
		GPIO.output(17, GPIO.LOW)   #SETS TO 0V
		time.sleep(0.08)

except KeyboardInterrupt:
	GPIO.cleanup()
